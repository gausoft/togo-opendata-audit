"""
Sample resources, classify each as:
- schema_only: header looks like a column dictionary
- data_geo: has geometry / lat-lon column
- data_tabular: has rows of actual data
- empty: 0 or 1 line
- error: HTTP failure
- non_csv: skipped (xlsx, etc.)

Strategy: download first ~32KB of each resource. Detect schema-only by header pattern.
"""
import csv
import io
import json
import re
import time
from collections import Counter, defaultdict
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw" / "datasets_metadata.json"
OUT = ROOT / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)

SCHEMA_HEADER_RE = re.compile(r"^\s*(no\.?|n°|numéro|number)\s*,.*nom\s+du\s+champ", re.I)
GEO_HINTS = ["geometry", "lat", "lon", "longitude", "latitude", "x_coord", "y_coord", "point", "wkt"]


def head_bytes(url: str, n: int = 32768, timeout: int = 30) -> tuple[int, bytes]:
    headers = {"User-Agent": "togo-opendata-audit/1.0", "Range": f"bytes=0-{n-1}"}
    try:
        req = Request(url, headers=headers)
        with urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read(n)
    except HTTPError as e:
        return e.code, b""
    except (URLError, TimeoutError, ConnectionResetError):
        return 0, b""


def classify_csv(payload: bytes) -> tuple[str, dict]:
    if len(payload) < 30:
        return "empty", {"bytes": len(payload)}
    try:
        text = payload.decode("utf-8", errors="replace")
    except Exception:
        text = payload.decode("latin-1", errors="replace")
    lines = text.splitlines()
    if len(lines) < 2:
        return "empty", {"lines": len(lines)}
    header = lines[0].strip()
    # Schema-only: header pattern OR all rows look like field metadata
    if SCHEMA_HEADER_RE.search(header):
        return "schema_only", {"header": header[:120], "lines": len(lines)}
    # Detect geographic data
    header_low = header.lower()
    has_geo = any(h in header_low for h in GEO_HINTS)
    # Detect single-cell aggregate data (1 column, 1-2 rows = "Value" type)
    cols = header.count(",") + 1
    info = {"header": header[:120], "lines": len(lines), "cols": cols, "has_geo": has_geo}
    if cols <= 2 and len(lines) <= 5:
        return "tiny_aggregate", info
    if has_geo:
        return "data_geo", info
    return "data_tabular", info


def main() -> None:
    datasets = json.loads(RAW.read_text())

    rows = []
    by_outcome = Counter()
    by_org_outcome = defaultdict(Counter)
    schema_only_examples = []
    empty_examples = []
    real_data_examples = []

    print(f"Auditing {len(datasets)} datasets...\n")

    for i, d in enumerate(datasets, 1):
        org = (d.get("organization") or {}).get("name") or "(no org)"
        slug = d.get("slug")
        title = d.get("title") or ""
        resources = d.get("resources") or []
        if not resources:
            outcome = "no_resource"
            rows.append({"slug": slug, "org": org, "outcome": outcome, "title": title})
            by_outcome[outcome] += 1
            by_org_outcome[org][outcome] += 1
            continue

        # Take first CSV resource
        csv_res = next((r for r in resources if (r.get("format") or "").lower() == "csv"), None)
        if not csv_res:
            outcome = "non_csv"
            rows.append({"slug": slug, "org": org, "outcome": outcome, "title": title})
            by_outcome[outcome] += 1
            by_org_outcome[org][outcome] += 1
            continue

        url = csv_res.get("url")
        if not url:
            outcome = "no_url"
            rows.append({"slug": slug, "org": org, "outcome": outcome, "title": title})
            by_outcome[outcome] += 1
            by_org_outcome[org][outcome] += 1
            continue

        status, payload = head_bytes(url)
        if status not in (200, 206):
            outcome = f"http_{status}"
            rows.append({"slug": slug, "org": org, "outcome": outcome, "title": title, "status": status})
            by_outcome[outcome] += 1
            by_org_outcome[org][outcome] += 1
            continue

        outcome, info = classify_csv(payload)
        row = {
            "slug": slug, "org": org, "title": title, "outcome": outcome,
            "filesize": csv_res.get("filesize"), "n_resources": len(resources),
            "lines": info.get("lines"), "cols": info.get("cols"),
            "has_geo": info.get("has_geo", False),
        }
        rows.append(row)
        by_outcome[outcome] += 1
        by_org_outcome[org][outcome] += 1

        if outcome == "schema_only" and len(schema_only_examples) < 10:
            schema_only_examples.append({"title": title, "slug": slug, "org": org})
        if outcome in ("empty", "tiny_aggregate") and len(empty_examples) < 10:
            empty_examples.append({"title": title, "slug": slug, "org": org, "outcome": outcome})
        if outcome in ("data_geo", "data_tabular") and len(real_data_examples) < 10:
            real_data_examples.append({"title": title, "slug": slug, "org": org, "lines": info.get("lines")})

        if i % 50 == 0:
            print(f"  {i}/{len(datasets)}  outcomes so far: {dict(by_outcome.most_common())}", flush=True)
        time.sleep(0.05)

    # Per-org % real data
    org_quality = {}
    for org, counts in by_org_outcome.items():
        total = sum(counts.values())
        real = counts.get("data_geo", 0) + counts.get("data_tabular", 0)
        schema = counts.get("schema_only", 0)
        empty = counts.get("empty", 0) + counts.get("tiny_aggregate", 0)
        org_quality[org] = {
            "total": total,
            "real_data": real,
            "real_data_pct": round(100 * real / total, 1) if total else 0,
            "schema_only": schema,
            "schema_only_pct": round(100 * schema / total, 1) if total else 0,
            "empty_or_tiny": empty,
            "empty_or_tiny_pct": round(100 * empty / total, 1) if total else 0,
            "errors_or_other": total - real - schema - empty,
        }

    # Multi-resource datasets: real data may be in resource #2
    # Recount: if a dataset has 2+ resources and outcome is schema_only, it might still have data in #2
    multi_res_count = sum(1 for d in datasets if len(d.get("resources") or []) > 1)
    schema_in_multi = sum(1 for r in rows if r.get("outcome") == "schema_only" and r.get("n_resources", 0) > 1)

    out = {
        "summary": {
            "total_audited": len(rows),
            "outcomes": dict(by_outcome.most_common()),
            "schema_only_pct": round(100 * by_outcome.get("schema_only", 0) / len(rows), 1),
            "real_data_pct": round(
                100 * (by_outcome.get("data_geo", 0) + by_outcome.get("data_tabular", 0)) / len(rows), 1
            ),
            "datasets_multi_resource": multi_res_count,
            "schema_only_in_multi_res": schema_in_multi,
        },
        "by_organization": {k: v for k, v in sorted(org_quality.items(), key=lambda x: -x[1]["total"])},
        "schema_only_examples": schema_only_examples,
        "empty_examples": empty_examples,
        "real_data_examples": real_data_examples,
    }

    (OUT / "content_audit.json").write_text(json.dumps(out, ensure_ascii=False, indent=2))
    rows_file = OUT / "content_audit_rows.json"
    rows_file.write_text(json.dumps(rows, ensure_ascii=False, indent=2))

    print(f"\nWrote {OUT / 'content_audit.json'}")
    print("\n" + "=" * 70)
    print("CONTENT AUDIT SUMMARY")
    print("=" * 70)
    for k, v in by_outcome.most_common():
        pct = 100 * v / len(rows)
        print(f"  {v:5d}  ({pct:5.1f}%)  {k}")

    print("\nPer-organization quality (top 15 by volume):")
    for org, q in list(org_quality.items())[:15]:
        print(
            f"  {org[:55]:55s}  total={q['total']:4d}  "
            f"real={q['real_data_pct']:5.1f}%  schema={q['schema_only_pct']:5.1f}%  "
            f"empty/tiny={q['empty_or_tiny_pct']:5.1f}%"
        )


if __name__ == "__main__":
    main()
