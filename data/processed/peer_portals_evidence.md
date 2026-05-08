# Peer-portal evidence sheet — verified May 2026

> **Method.** Each peer portal was probed with `curl -A "Mozilla/5.0"` and a battery of well-known open-data endpoints (CKAN `/api/3/action/package_list`, udata `/api/1/datasets/`, DKAN `data.json`, Opendatasoft `/api/explore/v2.1/`, ArcGIS Hub `/api/feed/dcat-us/...`). Every claim below names the exact URL that produced the proof. Reproducible: `python3 scripts/05_probe_peers.py` + the manual probes documented in this file.

> **Why this file exists.** Earlier draft of the report stated software stacks ("CKAN", "200+ datasets", "n.c.") for peers without checking. This evidence sheet is the corrective ground truth.

---

## TL;DR

| Country | Live URL (May 2026) | Real software | Datasets | Most recent update | Evidence |
|---------|---------------------|---------------|---------:|--------------------|----------|
| **Togo** 🇹🇬 | `opendata.gouv.tg` | **udata** | **1 550** | **2025-10-28** | `https://opendata.gouv.tg/api/1/datasets/?page_size=1` returns valid JSON with `"total": 1550` |
| **Ghana** 🇬🇭 | `data.gov.gh` | **DKAN (Drupal 7)** | **272** | **2020-08-29** (frozen ~5.7 yr) | `<meta name="Generator" content="Drupal 7">` + `https://data.gov.gh/api/3/action/package_list` returns 272 names + `https://data.gov.gh/data.json` is a 568 KB DCAT-US catalog |
| **Côte d'Ivoire** 🇨🇮 | `data.gouv.ci` | **Custom Nuxt + proprietary backend** (`/api/v1/portals/{portalId}`) | **177** | unknown (auth-gated) | Number "177 jeux de données" in HTML; portal API endpoint `/api/v1/portals/yCWsyaGpA` returns HTTP 401 (auth required) |
| **Kenya** 🇰🇪 | `www.opendata.go.ke` | **ArcGIS Hub** — **subscription canceled** | n/a | n/a | `https://www.opendata.go.ke/data.json` returns `{"error":"SB_0006: Subscription is canceled, the item is not accessible"}` |
| **Burkina Faso** 🇧🇫 | `data.gov.bf` | **Marketing landing page** for an internal data-lake stack — **no public catalog exists** | n/a | n/a | Page title is `Modern Data Platform - Data Lake & Analytics`; only links are to admin tools (`airflow.`, `minio.`, `nessie.`, `portainer.`, `superset.`, `trino.data.gov.bf`) |
| **Nigeria** 🇳🇬 | `nigeriadata.gov.ng` | **Custom proprietary "IDSPGateway"** (auth-gated) | n/a (login required) | n/a | JS bundle hard-codes `baseURL: "https://nigeriadata.gov.ng/IDSPGateway/PortalService"`; only public endpoint is `DataHub/getToken` which returns `{"responseMessage":"Invalid_Credentials"}` |
| **Sénégal** 🇸🇳 | (none functional) | — | — | — | `data.gouv.sn` DNS unresolvable; `senegal.opendataforafrica.org` Cloudflare 403; `senegalstats.opendata.arcgis.com/data.json` returns `{"error":"Domain record(s) not found"}`; `geosenegal.gouv.sn` HTTP 415 |
| **Bénin** 🇧🇯 | (none functional) | — | — | — | `data.gouv.bj` DNS unresolvable; alternative hosts (`opendata.gouv.bj`, `opendata.bj`, `opendata.gov.bj`) all DNS-fail; `data.bj` returns Cloudflare HTTP 521 (origin down) |

---

## Headline corrections to the audit's earlier draft

| Earlier claim | Verified reality | Direction |
|---------------|------------------|-----------|
| Ghana: "CKAN, 271/912" | Ghana runs **DKAN on Drupal 7**, exposes **272 datasets**, last update **2020-08-29** | Software wrong, count close, *but freshness much worse than reported* |
| Burkina Faso: "CKAN, 200+" | **No public catalog exists**; portal URL is a marketing splash for internal Airflow/MinIO/Trino infrastructure | Software wrong; "200+ datasets" claim is **unsupported** |
| Nigeria: "CKAN" | Custom proprietary IDSPGateway behind authentication | Software wrong |
| Côte d'Ivoire: "propriétaire, 177" | Custom Nuxt SPA + proprietary `/api/v1/portals/...` backend; 177 confirmed | ✅ correct |
| Sénégal: "écosystème distribué, varies" | **No nationally-hosted open data catalog reachable**; the only documented Knoema-hosted mirror sits behind Cloudflare; the ArcGIS sub-portal returns "Domain record not found" | Direction right but vaguer than reality |
| Kenya: "ArcGIS Hub, en relance" | Hub shell still loads but **the underlying ArcGIS Online subscription is canceled** (server returns SB_0006) | More definitive than "en relance" |
| **"Le portail togolais affiche 5 à 10 fois plus de datasets que ceux du Ghana et de la Côte d'Ivoire"** | Verified: Togo 1 550 vs Ghana 272 (= **5.7×**) vs Côte d'Ivoire 177 (= **8.8×**) | ✅ The original claim is true |

---

## Country-by-country detail with command-line proofs

### 🇹🇬 Togo — `opendata.gouv.tg`

```
$ curl -s "https://opendata.gouv.tg/api/1/datasets/?page_size=1&sort=-last_update" | jq '{total, latest: .data[0] | {title, last_update}}'
{
  "total": 1550,
  "latest": {
    "title": "Indicateurs Démographiques (RGPH 2022)",
    "last_update": "2025-10-28T08:44:45.856000+00:00"
  }
}
```

→ **udata** confirmed (canonical udata API), **1 550 datasets**, latest update **2025-10-28**.

### 🇬🇭 Ghana — `data.gov.gh`

```
$ curl -s https://data.gov.gh/ | grep -i 'meta name="Generator"'
<meta name="Generator" content="Drupal 7 (http://drupal.org)" />

$ curl -s "https://data.gov.gh/api/3/action/package_list" | jq '.result | length'
272

$ curl -s "https://data.gov.gh/data.json" | jq '[.dataset[].modified] | max, min, length'
"2020-08-29"
"2016-02-05"
272
```

→ **DKAN on Drupal 7**, **272 datasets**, **frozen since 2020-08-29** (~5.7 years stale at audit time).
→ Notable upside vs Togo: Ghana **does expose** a DCAT-US `data.json` feed (568 KB) — the very interoperability standard that opendata.gouv.tg has *not* activated.

### 🇨🇮 Côte d'Ivoire — `data.gouv.ci`

```
$ curl -s "https://data.gouv.ci/datasets" | grep -oE '[0-9]+ jeux? de données' | head -1
177 jeux de données

$ curl -s -o /dev/null -w "%{http_code}" "https://data.gouv.ci/api/v1/portals/yCWsyaGpA"
401
```

→ Custom Nuxt SPA backed by proprietary `/api/v1/portals/{portalId}` endpoints. The only public count visible is **177 datasets**. Recent-update timestamp is not exposed publicly without authentication.

### 🇰🇪 Kenya — `www.opendata.go.ke`

```
$ curl -s -o /dev/null -w "%{http_code}\n" https://www.opendata.go.ke/
200

$ curl -s "https://www.opendata.go.ke/data.json"
{"error":"SB_0006: Subscription is canceled, the item is not accessible"}
```

→ ArcGIS Hub front-end is up, but the **ArcGIS Online subscription powering it has been canceled**. The HTML shell loads; the catalog is empty as far as the public API is concerned.

### 🇧🇫 Burkina Faso — `data.gov.bf`

```
$ curl -s https://data.gov.bf/ | grep -oE '<title>[^<]+</title>'
<title>Modern Data Platform - Data Lake & Analytics</title>

$ curl -s https://data.gov.bf/ | grep -oE 'href="https://[a-z]+\.data\.gov\.bf"'
href="https://airflow.data.gov.bf"
href="https://minio.data.gov.bf"
href="https://nessie.data.gov.bf"
href="https://portainer.data.gov.bf"
href="https://superset.data.gov.bf"
href="https://trino.data.gov.bf"

$ curl -sI https://portainer.data.gov.bf/ | head -1
HTTP/2 307
```

→ `data.gov.bf` is **a marketing splash page for an internal data-lake architecture** (Airflow / MinIO / Iceberg-Nessie / Trino / Superset). There is **no public open-data catalog or DCAT/CKAN/udata API**.
→ Side finding: `portainer.data.gov.bf` (the Docker-management UI) is **publicly reachable** — a configuration that should not be on the open internet.

### 🇳🇬 Nigeria — `nigeriadata.gov.ng`

```
$ curl -s https://nigeriadata.gov.ng/static/js/main.a5276892.js | grep -oE 'baseURL:"[^"]+"'
baseURL:"https://nigeriadata.gov.ng/IDSPGateway/PortalService"

$ curl -s https://nigeriadata.gov.ng/IDSPGateway/DataHub/getToken
{"responseCode":"01","responseMessage":"Invalid_Credentials","token":null}
```

→ Custom proprietary backend named **IDSPGateway** ("Integrated Data Sharing Portal"). The catalog is gated behind authentication; no public dataset count or last-update timestamp is reachable without an account.

### 🇸🇳 Sénégal — no live national open-data portal

```
$ for u in data.gouv.sn opendata.gouv.sn opendata.sec.gouv.sn catalog.ansd.sn; do \
    code=$(curl -sLI --max-time 8 -o /dev/null -w "%{http_code}" "https://$u/"); \
    echo "  $u -> $code"; \
  done
  data.gouv.sn -> 000          # DNS unresolvable
  opendata.gouv.sn -> 000      # DNS unresolvable
  opendata.sec.gouv.sn -> 000  # DNS unresolvable
  catalog.ansd.sn -> 000       # DNS unresolvable

$ curl -s https://senegalstats.opendata.arcgis.com/data.json
{"error":"Domain record(s) not found :: A domain record with hostname = senegalstats.opendata.arcgis.com does not exist :: 404"}
```

→ The Knoema-hosted mirror `senegal.opendataforafrica.org` is behind Cloudflare 403; the ArcGIS sub-portal `senegalstats.opendata.arcgis.com` is shell-only (subscription record missing); none of the gouv.sn open-data candidates resolve.

### 🇧🇯 Bénin — no live national open-data portal

```
$ for u in data.gouv.bj opendata.gouv.bj opendata.bj opendata.gov.bj data.bj; do \
    code=$(curl -sLI --max-time 8 -o /dev/null -w "%{http_code}" "https://$u/"); \
    echo "  $u -> $code"; \
  done
  data.gouv.bj -> 000     # DNS unresolvable
  opendata.gouv.bj -> 000 # DNS unresolvable
  opendata.bj -> 000      # DNS unresolvable
  opendata.gov.bj -> 000  # DNS unresolvable
  data.bj -> 521          # Cloudflare: origin down
```

---

## Implications for the report

1. The "**5–10× more datasets than Ghana/CI**" claim is **defensible** (Togo 1 550 vs Ghana 272 = 5.7×, vs Côte d'Ivoire 177 = 8.8×) but the framing must immediately pivot to: *quantity is not maturity.*
2. **Ghana wins on interoperability** despite having far fewer datasets: it ships a DCAT-US `data.json` catalog out-of-the-box — the very standard Togo's udata install has switched off.
3. **Burkina Faso's "open data portal" doesn't exist as a public catalog** — it's a marketing page for internal infra. Any prior count of "200+ datasets" was unsourced.
4. **Kenya, Sénégal, Bénin** show the regional pattern: portal shells survive while underlying subscriptions/DNS records die. This is the **regional-portal-collapse finding** of §6 — now backed by HTTP-level proofs, not anecdote.
5. **OGP membership is uncorrelated with portal health** here: Côte d'Ivoire, Burkina Faso, Sénégal, Bénin, Nigeria, Ghana, Kenya are **all OGP members**. None of them currently runs a healthier public open-data catalog than non-member Togo on the metrics that are publicly testable. That tension deserves its own paragraph in the report.
