"""
Analyze metadata only (no downloads). Compute:
- Dataset counts by organization
- Format distribution
- License distribution
- Frequency declaration
- Last_modified distribution (freshness histogram)
- Resources per dataset
- Tags / themes
"""
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw" / "datasets_metadata.json"
OUT = ROOT / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)


def parse_dt(s: str | None):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except (ValueError, TypeError):
        return None


def main() -> None:
    datasets = json.loads(RAW.read_text())
    total = len(datasets)
    print(f"Total datasets: {total}\n")

    # Organizations
    by_org = Counter()
    by_org_resources = defaultdict(int)
    for d in datasets:
        org = (d.get("organization") or {}).get("name") or "(no org)"
        by_org[org] += 1
        by_org_resources[org] += len(d.get("resources") or [])

    # Formats
    formats = Counter()
    resource_count = 0
    for d in datasets:
        for r in d.get("resources") or []:
            resource_count += 1
            formats[(r.get("format") or "?").lower()] += 1

    # Licenses
    licenses = Counter()
    for d in datasets:
        licenses[d.get("license") or "(unset)"] += 1

    # Frequency declared
    frequencies = Counter()
    for d in datasets:
        frequencies[d.get("frequency") or "(unset)"] += 1

    # Tags
    tags = Counter()
    for d in datasets:
        for t in d.get("tags") or []:
            tags[t] += 1

    # Freshness: last_modified distribution
    now = datetime.now(timezone.utc)
    freshness_buckets = Counter()
    last_mod_dates = []
    for d in datasets:
        lm = parse_dt(d.get("last_modified") or d.get("last_update"))
        if lm is None:
            freshness_buckets["unknown"] += 1
            continue
        last_mod_dates.append(lm)
        days = (now - lm).days
        if days < 30:
            freshness_buckets["<1 month"] += 1
        elif days < 90:
            freshness_buckets["1-3 months"] += 1
        elif days < 180:
            freshness_buckets["3-6 months"] += 1
        elif days < 365:
            freshness_buckets["6-12 months"] += 1
        elif days < 730:
            freshness_buckets["12-24 months"] += 1
        else:
            freshness_buckets[">24 months"] += 1

    # Resources per dataset
    res_per_ds = Counter()
    for d in datasets:
        res_per_ds[len(d.get("resources") or [])] += 1

    # Spatial coverage
    has_spatial = sum(1 for d in datasets if d.get("spatial"))
    has_temporal = sum(1 for d in datasets if d.get("temporal_coverage"))

    # Description length (proxy for documentation quality)
    desc_lens = [len(d.get("description") or "") for d in datasets]
    desc_lens.sort()
    median_desc = desc_lens[len(desc_lens) // 2] if desc_lens else 0
    p25 = desc_lens[len(desc_lens) // 4] if desc_lens else 0
    p75 = desc_lens[3 * len(desc_lens) // 4] if desc_lens else 0

    # Empty descriptions
    empty_desc = sum(1 for d in datasets if not (d.get("description") or "").strip())

    # Reuses, discussions, followers (engagement signals)
    metrics_sum = defaultdict(int)
    for d in datasets:
        m = d.get("metrics") or {}
        for k, v in m.items():
            if isinstance(v, (int, float)):
                metrics_sum[k] += int(v)

    # Output report
    report = {
        "total_datasets": total,
        "total_resources": resource_count,
        "by_organization": by_org.most_common(),
        "resources_by_organization": dict(by_org_resources),
        "formats": formats.most_common(),
        "licenses": licenses.most_common(),
        "frequencies": frequencies.most_common(),
        "freshness_buckets": dict(freshness_buckets),
        "freshness_oldest_iso": min(last_mod_dates).isoformat() if last_mod_dates else None,
        "freshness_newest_iso": max(last_mod_dates).isoformat() if last_mod_dates else None,
        "resources_per_dataset_distribution": dict(res_per_ds.most_common()),
        "datasets_with_spatial_coverage": has_spatial,
        "datasets_with_temporal_coverage": has_temporal,
        "description_length": {"p25": p25, "median": median_desc, "p75": p75},
        "datasets_with_empty_description": empty_desc,
        "engagement_metrics_total": dict(metrics_sum),
        "top_tags": tags.most_common(30),
    }

    out_file = OUT / "metadata_analysis.json"
    out_file.write_text(json.dumps(report, ensure_ascii=False, indent=2))
    print(f"Wrote analysis to {out_file}\n")

    # Print key findings
    print("=" * 70)
    print("KEY METADATA FINDINGS")
    print("=" * 70)
    print(f"\nTotal datasets: {total}  |  Total resources: {resource_count}")
    print(f"Avg resources/dataset: {resource_count/total:.2f}")
    print(f"\nDatasets with empty description: {empty_desc} ({100*empty_desc/total:.1f}%)")
    print(f"Description length p25/median/p75: {p25} / {median_desc} / {p75} chars")
    print(f"\nDeclared license distribution:")
    for lic, n in licenses.most_common():
        print(f"  {n:5d}  {lic}")
    print(f"\nDeclared frequency distribution:")
    for fr, n in frequencies.most_common():
        print(f"  {n:5d}  {fr}")
    print(f"\nFreshness (last_modified):")
    for b, n in sorted(freshness_buckets.items(), key=lambda x: -x[1]):
        print(f"  {n:5d}  {b}")
    print(f"\nFormat distribution:")
    for f, n in formats.most_common(15):
        print(f"  {n:5d}  {f}")
    print(f"\nTop 15 organizations by datasets:")
    for org, n in by_org.most_common(15):
        print(f"  {n:5d}  {org[:60]}")
    print(f"\nEngagement (totals):")
    for k, v in metrics_sum.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
