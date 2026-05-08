"""
Probe African peer open data portals to verify:
- Software stack (CKAN / udata / ArcGIS Hub / DKAN / proprietary)
- Reachability (HTTP status)
- Dataset count (via API)
- Last dataset update (via API)

Outputs a Markdown evidence sheet AND raw JSON for each country.
Reproducible: anyone can run python3 scripts/05_probe_peers.py
"""
import json
import socket
import ssl
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw" / "peer_probes"
RAW.mkdir(parents=True, exist_ok=True)
OUT = ROOT / "data" / "processed" / "peer_portals_evidence.md"

UA = "Mozilla/5.0 (compatible; togo-opendata-audit/1.1; +https://github.com/gausoft/togo-opendata-audit)"
TIMEOUT = 25

# Allow self-signed / expired certs to PROBE — we record the cert error as a finding,
# but we still want to know what the server says.
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

# Candidate URLs per country. We try several because operators move portals.
COUNTRIES = {
    "Kenya": [
        "https://www.opendata.go.ke/",
        "https://opendata.go.ke/",
        # Kenya migrated to ArcGIS Hub
        "https://kenya.opendataforafrica.org/",
        "https://kenya-kcbs.opendata.arcgis.com/",
    ],
    "Ghana": [
        "https://data.gov.gh/",
        "https://www.data.gov.gh/",
    ],
    "Côte d'Ivoire": [
        "https://data.gouv.ci/",
        "https://www.data.gouv.ci/",
    ],
    "Sénégal": [
        "https://senegal.opendataforafrica.org/",
        "https://www.data.gouv.sn/",
        "https://data.gouv.sn/",
        "https://www.geosenegal.gouv.sn/",
    ],
    "Burkina Faso": [
        "https://www.data.gov.bf/",
        "https://data.gov.bf/",
        "https://burkinafaso.opendataforafrica.org/",
    ],
    "Nigeria": [
        "https://data.gov.ng/",
        "http://www.data.gov.ng/",
        "https://nigeria.opendataforafrica.org/",
        "https://nigeriadata.gov.ng/",
    ],
    "Bénin": [
        "https://data.gouv.bj/",
        "https://www.data.gouv.bj/",
        "https://benin.opendataforafrica.org/",
    ],
    "Togo (référence)": [
        "https://opendata.gouv.tg/fr/",
    ],
}

# Endpoints used to fingerprint software
PROBES = [
    # (path, software_if_200_with_keyword, keyword_to_match_in_body)
    ("api/3/action/status_show", "CKAN", b"ckan"),
    ("api/3/action/package_search?rows=0", "CKAN", b'"success": true'),
    ("api/1/datasets/?page_size=1", "udata", b"data"),
    ("api/1/site/", "udata", b"datasets"),
    # ArcGIS Hub typically exposes /api/feed/dcat-us/1.1.json
    ("api/feed/dcat-us/1.1.json", "ArcGIS Hub", b"dataset"),
    ("api/search/v1", "ArcGIS Hub", b""),
    # DKAN (Drupal) exposes /api/dataset/query
    ("api/dataset/query", "DKAN", b""),
    # Knoema (opendataforafrica.org)
    ("api/1.0/data", "Knoema", b""),
]


def fetch(url: str, timeout: int = TIMEOUT):
    try:
        req = Request(url, headers={"User-Agent": UA, "Accept": "application/json,*/*"}, method="GET")
        with urlopen(req, timeout=timeout, context=CTX) as r:
            return {"ok": True, "status": r.status, "url_final": r.geturl(), "body": r.read(200_000), "headers": dict(r.headers)}
    except HTTPError as e:
        try:
            body = e.read(20_000)
        except Exception:
            body = b""
        return {"ok": False, "status": e.code, "url_final": url, "body": body, "headers": dict(e.headers or {}), "error": f"HTTP {e.code}"}
    except (URLError, socket.timeout, ConnectionError) as e:
        return {"ok": False, "status": None, "url_final": url, "body": b"", "headers": {}, "error": str(e)}
    except Exception as e:
        return {"ok": False, "status": None, "url_final": url, "body": b"", "headers": {}, "error": f"{type(e).__name__}: {e}"}


def detect_software(base: str) -> dict:
    """Return dict with software name + evidence URL + sample body."""
    # Strip language locale prefix (e.g. /fr/, /en/) so /api/... resolves at root
    from urllib.parse import urlparse, urlunparse
    p = urlparse(base.rstrip("/") + "/")
    path = p.path
    if len(path) >= 4 and path[1:3] in {"fr", "en", "pt", "es"} and path[3] == "/":
        path = path[3:]
    api_root = urlunparse((p.scheme, p.netloc, path, "", "", ""))
    api_root = api_root.rstrip("/") + "/"
    # First, try the home page to get headers (Generator, X-Powered-By)
    home = fetch(base)
    home_headers = home.get("headers", {})
    home_body = home.get("body", b"")
    fingerprints = {
        "home_status": home.get("status"),
        "api_root_used": api_root,
        "home_headers": {k: v for k, v in home_headers.items() if k.lower() in {"server", "x-generator", "generator", "x-powered-by"}},
        "home_body_keywords": {},
        "api_probes": [],
    }
    for kw in [b"ckan", b"udata", b"opendatasoft", b"socrata", b"dkan", b"drupal", b"arcgis", b"esri", b"hub.arcgis", b"junar"]:
        if kw in home_body.lower():
            fingerprints["home_body_keywords"][kw.decode()] = True

    detected = None
    for path, sw, kw in PROBES:
        url = api_root + path
        r = fetch(url, timeout=15)
        body = r.get("body", b"")
        snippet = body[:300].decode(errors="replace")
        ctype = (r.get("headers") or {}).get("Content-Type", "") or (r.get("headers") or {}).get("content-type", "")
        # Strict: must be HTTP 200 AND response must be parseable JSON (or arcgis text/html with esri keywords)
        is_json = False
        try:
            json.loads(body.decode(errors="replace"))
            is_json = True
        except Exception:
            pass
        fingerprints["api_probes"].append({
            "url": url,
            "status": r.get("status"),
            "ok": r.get("ok"),
            "content_type": ctype,
            "is_json": is_json,
            "first_300": snippet,
            "error": r.get("error"),
        })
        valid = False
        if r.get("ok") and r.get("status") == 200:
            if sw == "ArcGIS Hub":
                valid = is_json and (b"dataset" in body.lower() or b"esri" in body.lower() or b"@type" in body.lower())
            else:
                valid = is_json and (not kw or kw in body.lower())
        if valid and detected is None:
            detected = (sw, url)
        time.sleep(0.2)
    fingerprints["detected_software"] = detected[0] if detected else "unknown / proprietary / offline"
    fingerprints["detected_via"] = detected[1] if detected else None
    return fingerprints


def ckan_count_and_freshness(base: str) -> dict:
    """For CKAN portals, fetch dataset count + most recent metadata_modified."""
    from urllib.parse import urlparse, urlunparse
    p = urlparse(base.rstrip("/") + "/")
    path = p.path
    if len(path) >= 4 and path[1:3] in {"fr", "en", "pt", "es"} and path[3] == "/":
        path = path[3:]
    base = urlunparse((p.scheme, p.netloc, path, "", "", "")).rstrip("/") + "/"
    out = {}
    r = fetch(base + "api/3/action/package_search?rows=1")
    if r.get("ok") and r.get("status") == 200:
        try:
            j = json.loads(r["body"])
            out["count"] = j.get("result", {}).get("count")
        except Exception as e:
            out["count_error"] = str(e)
    # Sort by metadata_modified desc
    r = fetch(base + "api/3/action/package_search?rows=5&sort=metadata_modified%20desc")
    if r.get("ok") and r.get("status") == 200:
        try:
            j = json.loads(r["body"])
            results = j.get("result", {}).get("results", [])
            out["most_recent_5"] = [
                {
                    "name": d.get("name"),
                    "title": d.get("title"),
                    "metadata_modified": d.get("metadata_modified"),
                    "metadata_created": d.get("metadata_created"),
                    "organization": (d.get("organization") or {}).get("name"),
                }
                for d in results
            ]
        except Exception as e:
            out["recent_error"] = str(e)
    return out


def udata_count_and_freshness(base: str) -> dict:
    from urllib.parse import urlparse, urlunparse
    p = urlparse(base.rstrip("/") + "/")
    path = p.path
    if len(path) >= 4 and path[1:3] in {"fr", "en", "pt", "es"} and path[3] == "/":
        path = path[3:]
    base = urlunparse((p.scheme, p.netloc, path, "", "", "")).rstrip("/") + "/"
    out = {}
    r = fetch(base + "api/1/datasets/?page_size=1&sort=-last_update")
    if r.get("ok") and r.get("status") == 200:
        try:
            j = json.loads(r["body"])
            out["count"] = j.get("total")
            data = j.get("data") or []
            if data:
                out["most_recent_1"] = {
                    "title": data[0].get("title"),
                    "last_update": data[0].get("last_update"),
                    "created_at": data[0].get("created_at"),
                }
        except Exception as e:
            out["error"] = str(e)
    return out


def main():
    report = {}
    for country, urls in COUNTRIES.items():
        print(f"\n=== {country} ===")
        country_out = {"candidates": []}
        live_base = None
        for url in urls:
            print(f"  probing {url}")
            r = fetch(url)
            entry = {
                "url": url,
                "status": r.get("status"),
                "ok": r.get("ok"),
                "url_final": r.get("url_final"),
                "error": r.get("error"),
                "body_size": len(r.get("body", b"")),
                "title": "",
            }
            body = r.get("body", b"")
            if b"<title" in body:
                try:
                    s = body.lower().find(b"<title")
                    e = body.find(b"</title>", s)
                    entry["title"] = body[s:e].split(b">", 1)[-1].decode(errors="replace")[:120]
                except Exception:
                    pass
            country_out["candidates"].append(entry)
            if r.get("ok") and r.get("status") == 200 and live_base is None:
                live_base = url
            time.sleep(0.3)
        country_out["live_base"] = live_base
        if live_base:
            print(f"  -> fingerprinting {live_base}")
            fp = detect_software(live_base)
            country_out["fingerprint"] = fp
            sw = fp.get("detected_software", "")
            if sw == "CKAN":
                country_out["dataset_metrics"] = ckan_count_and_freshness(live_base)
            elif sw == "udata":
                country_out["dataset_metrics"] = udata_count_and_freshness(live_base)
        report[country] = country_out
        # Persist raw per country
        (RAW / f"{country.replace(' ', '_').replace('/', '_').replace(chr(39), '')}.json").write_text(json.dumps(country_out, indent=2, ensure_ascii=False))

    # Markdown evidence
    md = ["# Peer-portal evidence sheet — May 2026\n"]
    md.append("> Reproducible probe of African peer portals. Each country lists "
              "(a) which URLs were tried, (b) the live one, (c) the software "
              "fingerprint with the API URL that returned the proof, (d) the "
              "live dataset count and most-recent dataset update.\n")
    md.append("Run: `python3 scripts/05_probe_peers.py` (saves raw JSON per "
              "country in `data/raw/peer_probes/`).\n")
    md.append("\n## Summary\n")
    md.append("| Country | Live URL | Software | Datasets | Most recent update | Evidence URL |")
    md.append("|---|---|---|---|---|---|")
    for country, c in report.items():
        live = c.get("live_base") or "**no live URL found**"
        fp = c.get("fingerprint") or {}
        sw = fp.get("detected_software", "—")
        via = fp.get("detected_via") or "—"
        dm = c.get("dataset_metrics") or {}
        n = dm.get("count")
        recent = ""
        if "most_recent_5" in dm and dm["most_recent_5"]:
            recent = dm["most_recent_5"][0].get("metadata_modified") or ""
        elif "most_recent_1" in dm:
            recent = dm["most_recent_1"].get("last_update") or ""
        md.append(f"| **{country}** | {live} | {sw} | {n if n is not None else '—'} | {recent or '—'} | {via} |")
    md.append("\n## Per-country detail\n")
    for country, c in report.items():
        md.append(f"### {country}\n")
        md.append("**URLs attempted**\n")
        md.append("| URL | HTTP | Title | Error |")
        md.append("|---|---|---|---|")
        for cand in c["candidates"]:
            md.append(f"| `{cand['url']}` | {cand['status'] or 'conn-err'} | {cand['title'][:60]} | {cand.get('error') or '-'} |")
        if c.get("fingerprint"):
            fp = c["fingerprint"]
            md.append(f"\n**Software detected:** `{fp['detected_software']}`")
            if fp.get("detected_via"):
                md.append(f"  \n**Evidence URL:** {fp['detected_via']}")
            md.append(f"  \n**Home page server headers:** `{fp.get('home_headers')}`")
            md.append(f"  \n**Home body keywords matched:** `{list(fp.get('home_body_keywords', {}).keys())}`")
            md.append("\n**API probes**\n")
            md.append("| Endpoint | HTTP | First 200 chars |")
            md.append("|---|---|---|")
            for p in fp["api_probes"]:
                snip = (p["first_300"] or "").replace("|", "/").replace("\n", " ")[:160]
                md.append(f"| `{p['url']}` | {p['status'] or p.get('error') or 'err'} | `{snip}` |")
        if c.get("dataset_metrics"):
            md.append("\n**Dataset metrics**\n")
            md.append("```json")
            md.append(json.dumps(c["dataset_metrics"], indent=2, ensure_ascii=False)[:4000])
            md.append("```")
        md.append("\n")

    OUT.write_text("\n".join(md))
    print(f"\nWrote {OUT}")


if __name__ == "__main__":
    main()
