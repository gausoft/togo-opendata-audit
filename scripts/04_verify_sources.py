"""
Verify every URL cited across the audit's Markdown files.

Classifies each URL as:
- OK: HTTP 200, content distinct from the domain homepage
- SPA_TRAP: HTTP 200 but content is the homepage shell (e.g. ODIN profiles)
- REDIRECT: final URL differs from cited URL
- BROKEN: HTTP 4xx/5xx or connection error
- INCOMPLETE: malformed URL (placeholder, trailing punctuation)

Outputs a Markdown table to data/processed/source_verification.md.
"""
import hashlib
import json
import re
import time
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "processed" / "source_verification.md"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; togo-opendata-audit/1.1; +https://github.com/gausoft/togo-opendata-audit)"}


def collect_urls() -> list[str]:
    files = list(ROOT.glob("reports/*.md")) + [ROOT / "README.md"] + list((ROOT / "data" / "processed").glob("*.md"))
    # Don't scan our own output (avoids feedback loop on flagged URLs)
    files = [f for f in files if f.name != "source_verification.md"]
    urls = set()
    pat = re.compile(r"https?://[^\s)>\"\\\]]+")
    for f in files:
        if not f.exists():
            continue
        for u in pat.findall(f.read_text(errors="replace")):
            u = u.rstrip(".,;:!?`>\"'")
            urls.add(u)
    return sorted(urls)


def fetch(url: str, timeout: int = 30) -> tuple[int, str, bytes]:
    try:
        req = Request(url, headers=HEADERS, method="GET")
        with urlopen(req, timeout=timeout) as r:
            body = r.read(120_000)
            return r.status, r.geturl(), body
    except HTTPError as e:
        try:
            body = e.read(2000)
        except Exception:
            body = b""
        return e.code, url, body
    except (URLError, TimeoutError, ConnectionResetError, ConnectionRefusedError) as e:
        return 0, url, str(e).encode()
    except Exception as e:
        return -1, url, str(e).encode()


def is_incomplete(url: str) -> bool:
    if "<" in url or ">" in url:
        return True
    if url.endswith(("`", "'", "\"", "(")):
        return True
    if url.count("(") != url.count(")"):
        return True
    return False


def text_signature(body: bytes) -> str:
    """Cheap signature for SPA-trap detection: collapse whitespace + take a sample of inner content."""
    txt = body.decode("utf-8", errors="replace")
    txt = re.sub(r"<script[^>]*>.*?</script>", "", txt, flags=re.S | re.I)
    txt = re.sub(r"<style[^>]*>.*?</style>", "", txt, flags=re.S | re.I)
    txt = re.sub(r"<!--.*?-->", "", txt, flags=re.S)
    txt = re.sub(r"\s+", " ", txt).strip()
    return hashlib.sha256(txt[:8000].encode()).hexdigest()


def page_title(body: bytes) -> str:
    m = re.search(rb"<title[^>]*>(.*?)</title>", body, flags=re.S | re.I)
    if not m:
        return ""
    return re.sub(r"\s+", " ", m.group(1).decode("utf-8", errors="replace")).strip()[:120]


def homepage(url: str) -> str:
    p = urlparse(url)
    return f"{p.scheme}://{p.netloc}/"


def main() -> None:
    urls = collect_urls()
    print(f"Auditing {len(urls)} URLs from Markdown files...\n")

    # Cache homepage signatures per domain to detect SPA-trap
    home_sig: dict[str, str] = {}

    rows = []
    for i, url in enumerate(urls, 1):
        if is_incomplete(url):
            rows.append({"url": url, "status": "INCOMPLETE", "code": "-", "title": "malformed URL", "final": "-"})
            print(f"  {i:3d}/{len(urls)}  INCOMPLETE  {url}")
            continue

        code, final, body = fetch(url)
        if code == 0:
            rows.append({"url": url, "status": "BROKEN", "code": "conn-err", "title": body.decode(errors="replace")[:60], "final": "-"})
            print(f"  {i:3d}/{len(urls)}  BROKEN     {url}")
            continue
        if code >= 400:
            rows.append({"url": url, "status": "BROKEN", "code": str(code), "title": page_title(body), "final": "-"})
            print(f"  {i:3d}/{len(urls)}  HTTP {code}  {url}")
            continue

        title = page_title(body) or "(no title)"
        is_redirect = final != url and final.rstrip("/") != url.rstrip("/")
        sig = text_signature(body)

        # SPA-trap detection: only if URL has a path beyond "/"
        host_home = homepage(url)
        spa_trap = False
        if urlparse(url).path not in ("", "/"):
            if host_home not in home_sig:
                _, _, hbody = fetch(host_home)
                home_sig[host_home] = text_signature(hbody)
                time.sleep(0.2)
            if home_sig[host_home] == sig:
                spa_trap = True

        if spa_trap:
            status = "SPA_TRAP"
        elif is_redirect:
            status = "REDIRECT"
        else:
            status = "OK"

        rows.append({"url": url, "status": status, "code": str(code), "title": title, "final": final if is_redirect else "-"})
        print(f"  {i:3d}/{len(urls)}  {status:8s}  {code}  {url[:90]}")
        time.sleep(0.15)

    # Apply allow-list — reclassify intentional findings as ACCEPTED_*
    allowlist_path = ROOT / "data" / "processed" / "url_allowlist.json"
    accepted = {"BROKEN": set(), "REDIRECT": set(), "SPA_TRAP": set()}
    accepted_reasons = {}
    if allowlist_path.exists():
        al = json.loads(allowlist_path.read_text())
        for entry in al.get("expected_broken", []):
            accepted["BROKEN"].add(entry["url"]); accepted_reasons[entry["url"]] = entry["reason"]
        for entry in al.get("expected_redirect", []):
            accepted["REDIRECT"].add(entry["url"]); accepted_reasons[entry["url"]] = entry["reason"]
        for entry in al.get("expected_spa_trap", []):
            accepted["SPA_TRAP"].add(entry["url"]); accepted_reasons[entry["url"]] = entry["reason"]
    for r in rows:
        if r["status"] in accepted and r["url"] in accepted[r["status"]]:
            r["accepted"] = True
            r["reason"] = accepted_reasons[r["url"]]
        else:
            r["accepted"] = False

    # Summary
    counts = {}
    for r in rows:
        key = r["status"] + ("_ACCEPTED" if r["accepted"] else "")
        counts[key] = counts.get(key, 0) + 1

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("# Source verification — May 2026\n\n")
        f.write(f"Audited **{len(rows)} URLs** cited across all public-facing Markdown files.\n\n")
        f.write("| Status | Count |\n|---|---:|\n")
        for k, v in sorted(counts.items(), key=lambda x: -x[1]):
            f.write(f"| {k} | {v} |\n")

        unexpected = [r for r in rows if r["status"] != "OK" and not r["accepted"]]
        f.write("\n## ❌ Unexpected issues — must be fixed\n\n")
        if not unexpected:
            f.write("_None. All non-OK URLs are accounted for in `data/processed/url_allowlist.json`._\n")
        else:
            f.write("| Status | HTTP | URL | Title | Final URL after redirect |\n")
            f.write("|---|---|---|---|---|\n")
            for r in unexpected:
                url = r["url"].replace("|", "%7C")
                final = r["final"].replace("|", "%7C") if r["final"] != "-" else "-"
                title = r["title"].replace("|", "/").replace("\n", " ")[:80]
                f.write(f"| **{r['status']}** | {r['code']} | `{url}` | {title} | {final} |\n")

        accepted_rows = [r for r in rows if r["status"] != "OK" and r["accepted"]]
        f.write("\n## ✅ Accepted non-OK URLs (status IS the audit finding)\n\n")
        f.write("These URLs are flagged BROKEN/REDIRECT/SPA_TRAP intentionally — their failure mode is itself documented in the report. See `data/processed/url_allowlist.json` for full justification.\n\n")
        f.write("| Status | HTTP | URL | Reason |\n|---|---|---|---|\n")
        for r in accepted_rows:
            url = r["url"].replace("|", "%7C")
            reason = r["reason"].replace("|", "/")
            f.write(f"| {r['status']} | {r['code']} | `{url}` | {reason} |\n")

        f.write("\n## All OK URLs\n\n")
        f.write("| HTTP | URL | Title |\n|---|---|---|\n")
        for r in rows:
            if r["status"] != "OK":
                continue
            url = r["url"].replace("|", "%7C")
            title = r["title"].replace("|", "/").replace("\n", " ")[:80]
            f.write(f"| {r['code']} | `{url}` | {title} |\n")

    unexpected_n = sum(1 for r in rows if r["status"] != "OK" and not r["accepted"])
    print(f"\n{'='*60}\nSUMMARY: {dict(counts)}\nUnexpected issues: {unexpected_n}\nWrote report to {OUT}")
    if unexpected_n:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
