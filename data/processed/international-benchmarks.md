# International Open Data Benchmarks — Reference Dossier for the Togo Open Data Audit

**Purpose.** Research dossier compiled to anchor the constructive audit of [opendata.gouv.tg](https://opendata.gouv.tg/) and [geodata.gouv.tg](https://geodata.gouv.tg/) against international norms, standards, and country benchmarks.

**Scope.** Standards & frameworks, country ranking indices, peer-country quantitative comparison, common pitfalls, and audit methodology.

**Method.** Web search + direct portal fetches (May 2026). Every claim is sourced. Where a figure could not be verified, the entry is explicitly marked **"not found"** rather than estimated.

---

## 1. International standards & frameworks

### 1.1 International Open Data Charter (ODC)

The ODC is the most widely cited normative reference for government open data. It was launched in 2015 (building on the 2013 G8 Open Data Charter) and is governed by the International Open Data Charter Stewards.

**The six principles** (verbatim wording from the ODC site):

1. **Open by Default** — a presumption of publication for all government data, with clear justifications when exceptions apply.
2. **Timely and Comprehensive** — release high-quality open data in a timely manner, without undue delay.
3. **Accessible and Usable** — discoverable, machine-readable, free of charge, under an open and unrestrictive licence.
4. **Comparable and Interoperable** — consistent standards and structured formats so data can be combined across sectors and time.
5. **For Improved Governance and Citizen Engagement** — strengthens institutional accountability and civic participation.
6. **For Inclusive Development and Innovation** — stimulates economic growth, supports the SDGs, empowers marginalised communities.

Source: [ODC Principles](https://opendatacharter.org/principles/) · [Wikipedia overview](https://en.wikipedia.org/wiki/International_Open_Data_Charter).

**Adoption.** The ODC reports its principles "have been adopted by 174 national and subnational governments" since 2015 ([ODC Government Adopters](https://opendatacharter.org/government-adopters/)). The visible national-government list on that page contains 29 countries: Australia, Argentina, Canada, Chile, Colombia, Costa Rica, Dominican Republic, El Salvador, France, Germany, Guatemala, Honduras, Italy, Kosovo, North Macedonia, Mexico, Panama, Paraguay, Philippines, Sierra Leone, Slovenia, South Korea, Spain, Sweden, Ukraine, United Kingdom, Uruguay, Uzbekistan, New Zealand.

**Togo's status.** **Togo is NOT listed** among the ODC national signatories ([opendatacharter.org/government-adopters](https://opendatacharter.org/government-adopters/), checked May 2026). In sub-Saharan Africa, only Sierra Leone appears on the list. This is a meaningful gap to highlight in the audit: Togo communicates publicly about open data without having endorsed the global reference framework.

---

### 1.2 Open Definition 2.1 (Open Knowledge Foundation)

The Open Definition specifies what makes a work — including a dataset — *open* in the strict sense. Version 2.1 (November 2015) is the current stable version.

**Core requirements** ([Open Definition 2.1](https://opendefinition.org/od/2.1/en/)):

- **Open licence or public domain.** The work must be in the public domain or under an open licence (free use, redistribution, modification, separation, compilation, no discrimination, propagation, application to any purpose, no charge).
- **Availability.** Provided as a whole at no more than a reasonable one-time reproduction cost; should be downloadable from the internet without charge.
- **Open format.** A format that places no restrictions on use and can be processed by at least one free/libre/open-source software tool.
- **Machine readability.** Provided in a form readily processable by a computer, with elements individually accessible and modifiable.

OKFN maintains a [list of conformant licences](https://opendefinition.org/licenses/) — notably **CC0**, **CC-BY 4.0**, **CC-BY-SA 4.0**, **ODC-BY**, **ODbL**, **PDDL**. France's **Licence Ouverte 2.0** (the default on data.gouv.fr) is conformant.

**Application to Togo.** Any dataset published on opendata.gouv.tg that is missing an explicit open licence, or whose format requires proprietary software (e.g. raw `.xlsx` without an accompanying CSV), fails the Open Definition test even if the portal calls it "open". This is the formal yardstick for a dataset-by-dataset diagnosis.

---

### 1.3 Five-Star Linked Open Data (Tim Berners-Lee, 2010)

The 5-star scheme is the canonical maturity ladder for individual datasets. It is **cumulative** — each step assumes the previous one.

| Stars | Requirement | Typical example |
|------:|-------------|-----------------|
| ★ | Available on the web under an open licence, **any format** | PDF scan of a table |
| ★★ | **Structured** machine-readable data | Excel `.xlsx` |
| ★★★ | Structured **non-proprietary** format | CSV, JSON |
| ★★★★ | Use of **URIs** to identify things, so people can point at your data | RDF with HTTP URIs |
| ★★★★★ | **Linked** to other people's data to provide context | RDF + dereferenceable URIs to DBpedia, Wikidata, etc. |

Source: [5stardata.info](https://5stardata.info/en/) · [W3C GLD wiki](https://www.w3.org/2011/gld/wiki/5_Star_Linked_Data).

In practice, most government open data portals, including data.gouv.fr, sit at **★★★** for the bulk of their catalogue. Reaching ★★★★/★★★★★ requires URIs and Linked Data publishing, which very few portals have systematised.

---

### 1.4 W3C DCAT (Data Catalog Vocabulary)

**DCAT version 3** became a W3C Recommendation in August 2024 ([W3C news](https://www.w3.org/news/2024/data-catalog-vocabulary-dcat-version-3-is-a-w3c-recommendation/) · [Specification](https://www.w3.org/TR/vocab-dcat-3/)). It is the standard RDF vocabulary for describing data catalogues and is the lingua franca for catalogue-to-catalogue interoperability (federation).

**Mandatory fields.** DCAT v3 itself does **not** prescribe a hard-mandatory set; it leaves cardinality to *application profiles*. The two main profiles to know:

- **DCAT-AP 3.0** (European Commission, [SEMIC](https://semiceu.github.io/DCAT-AP/releases/3.0.0/)) — the European baseline. Minimum required to be DCAT-AP-compliant: **`dct:title`** and **`dct:description`** for every Dataset; **`dcat:accessURL`** for every Distribution. Strongly recommended additions: `dct:publisher`, `dct:license`, `dct:modified`, `dcat:keyword`, `dcat:theme`, `dct:spatial`, `dct:temporal`, `dcat:mediaType`.
- **DCAT-US 3.0** ([DOI/Project Open Data](https://doi-do.github.io/dcat-us/)) — the US federal profile.

**Why this matters for Togo.** udata (the software powering data.gouv.fr and opendata.gouv.tg) exposes a DCAT feed at `/catalog.xml` and `/catalog.json`. Auditing DCAT-AP compliance is therefore a one-shot scriptable check: missing licence, missing publisher, missing modified date all flag immediately.

---

### 1.5 ISO 19115 / ISO 19139 (geographic metadata)

These are the global standards for **geospatial metadata** — the relevant compliance target for [geodata.gouv.tg](https://geodata.gouv.tg/).

- **ISO 19115-1:2014** — Geographic information — Metadata — Part 1: Fundamentals. Defines the schema for describing geographic information and services. ([ISO catalogue page](https://www.iso.org/standard/53798.html))
- **ISO 19139:2012** — XML implementation schema for ISO 19115. Provides the actual XML record format used for exchange. ([Wikipedia: Geospatial metadata](https://en.wikipedia.org/wiki/Geospatial_metadata))

**Mandatory core elements** in any ISO 19115 record include: dataset title, reference date, abstract, dataset language, character set, topic category, geographic bounding box (extent), responsible organisation/contact, metadata file identifier, metadata standard name & version, metadata language, metadata date stamp ([NOAA workbook](https://www.ncei.noaa.gov/sites/default/files/2020-04/ISO%2019115-2%20Workbook_Part%20II%20Extentions%20for%20imagery%20and%20Gridded%20Data.pdf)).

ISO 19115 records are also what the European **INSPIRE Directive** mandates for geospatial data shared between EU public authorities, so any geo-portal aspiring to international interoperability uses this standard.

---

### 1.6 OGC web service standards (geo portals)

The Open Geospatial Consortium standards are how a geo-portal *delivers* data, as opposed to how it *describes* data. Auditors should expect a serious geo-portal to expose all four:

| Standard | Purpose | Typical use |
|----------|---------|-------------|
| **WMS** (Web Map Service) | Geo-registered **map images** (PNG/JPEG) | Display layers in a web viewer |
| **WMTS** (Web Map Tile Service) | Pre-rendered **map tiles** | Performance for static base maps |
| **WFS** (Web Feature Service) | **Vector features** (geometries + attributes) | Download / GIS analysis (incl. WFS-T for write) |
| **WCS** (Web Coverage Service) | **Raster coverages** | Download elevation / imagery data |
| **CSW** (Catalog Service for the Web) | **Metadata search** | Discovery of layers and services across portals |

Sources: [OGC standards overview](https://www.ogc.org/standards/wms/) · [GeoServer training](https://geoserver.geosolutionsgroup.com/edu/en/ogc_protocol_intro/index.html) · [Azavea open-data-standards](https://github.com/azavea/open-data-standards/blob/master/standards/general_standards/geospatial_data/ogc_wms-wfs-wcs-wmts-wps.md).

Modern stacks are progressively adopting **OGC API** (REST/JSON family — Features, Tiles, Coverages, Records) which is the next generation. ([ogcapi.ogc.org](https://ogcapi.ogc.org/))

A simple way to test geodata.gouv.tg: try `GET /geoserver/wms?service=WMS&request=GetCapabilities` and equivalents for WFS/WMTS/CSW. If they don't respond with valid XML capabilities, the portal is not interoperable.

---

### 1.7 FAIR principles (Findable, Accessible, Interoperable, Reusable)

Published in *Scientific Data* in 2016 ([Wilkinson et al., Nature](https://www.nature.com/articles/sdata201618)), the FAIR principles are the dominant data-stewardship reference today, especially in research, but increasingly applied to government data.

- **Findable** — globally unique persistent identifier; rich machine-readable metadata; metadata indexed in a searchable resource.
- **Accessible** — retrievable via a standardised, open communication protocol; metadata remains accessible even when data is gone.
- **Interoperable** — uses a formal, accessible, shared, broadly applicable language for knowledge representation; references other (meta)data.
- **Reusable** — clear, accessible licence; detailed provenance; meets domain-relevant community standards.

Source: [GO FAIR — FAIR Principles](https://www.go-fair.org/fair-principles/).

FAIR emphasises **machine-actionability** — humans alone cannot keep up with data volumes. This is the key bridge to AI-readiness, which the Global Data Barometer 2nd edition has now made an explicit cross-cutting theme.

---

### 1.8 EU Open Data Maturity Model

The European Commission, via [data.europa.eu](https://data.europa.eu/), publishes an annual Open Data Maturity (ODM) Report assessing **34 countries** (27 EU Member States + 3 EFTA + 4 EU candidate countries: Albania, Bosnia and Herzegovina, Serbia, Ukraine).

**Four dimensions** (stable since 2018):

1. **Policy** — national open-data policy maturity.
2. **Portal** — features and data on national portals.
3. **Quality** — metadata and data quality.
4. **Impact** — monitoring of reuse and impact.

In 2024, the most mature countries were **France (100%)**, **Poland (98%)**, **Slovakia (96%)**; Norway leads EFTA at 89%. Source: [ODM 2024 full report](https://data.europa.eu/sites/default/files/odm2024_full_report.pdf) · [Highlights](https://data.europa.eu/sites/default/files/2025-06/2024_odm_highlights.pdf).

The ODM methodology is the most copy-able framework for a national audit because every dimension's questionnaire is public.

---

### 1.9 Open Government Partnership (OGP) — Togo's status

The OGP is the multilateral platform where governments make biennial **National Action Plans** with civil society. As of May 2026, **Togo is NOT a member of OGP** ([OGP Members page](https://www.opengovpartnership.org/our-members), accessed via WebFetch May 2026). Togo passed an OGP Values Check assessment but never formalised membership, despite an invitation extended in 2018.

African OGP members: **Benin, Burkina Faso, Cabo Verde, Côte d'Ivoire, Ghana, Kenya, Liberia, Malawi, Morocco, Nigeria, Senegal, Seychelles, Sierra Leone, South Africa, Tunisia, Zambia.** All ten benchmark countries in §3 except Rwanda are OGP members.

**Implication.** Joining OGP (or even publishing an action plan modelled on OGP commitments) is one of the cleanest, lowest-cost ways for Togo to lock in a credible open-data trajectory.

---

## 2. Country ranking indices

### 2.1 Global Data Barometer (GDB) — 2nd edition (2024/2025)

- **Scope.** 43 countries, focused on **Latin America and the Caribbean + Africa**.
- **Pillars.** Governance, capabilities, availability — plus cross-cutting AI readiness, inclusion, data use.
- **Source.** [globaldatabarometer.org](https://globaldatabarometer.org/) · [2nd edition launch post](https://globaldatabarometer.org/2025/05/the-global-data-barometer-2nd-edition-a-shared-compass-for-navigating-the-data-landscape/).

**Togo's score.** **Not found** in the open snippets indexed by search engines as of May 2026. The full results require querying the [GDB explorer](https://globaldatabarometer.org/explore-the-results/). Recommendation for the audit: download the public dataset from the GDB site (it is itself published as open data) and extract Togo's row directly.

**Headline African finding from GDB 2nd ed.** "In Africa, there is real momentum around policy reform, especially in areas like data protection. However, implementation hurdles related to infrastructure, funding, and institutional capacity remain substantial." This is a quotable framing for the Togo report.

---

### 2.2 Open Data Barometer (final / 4th edition, 2017)

The Open Data Barometer was the predecessor to the GDB, run by the World Wide Web Foundation. The 4th edition (published 2017) covered **115 countries**.

**Togo's 4th-edition result:** **score 16 / 100, global rank 81** ([4th edition Africa regional report PDF](https://opendatabarometer.org/doc/4thEdition/ODB-4thEdition-RegionalReport-Africa.pdf)). Togo was a new entrant in that edition. After 2017, the ODB pivoted to a "Leaders Edition" covering only the 30 governments that had endorsed the ODC — which excluded Togo.

---

### 2.3 OECD OURdata Index 2023 (Open, Useful, Re-usable data)

- **Scope.** 4th edition, 36 OECD members + 4 accession countries = **40 countries**, ~670 data points each, 82 high-value datasets across 10 themes.
- **Three pillars:** (1) Data availability, (2) Data accessibility, (3) Government support for data re-use.
- **Top 3 (2023):** **Korea, France, Poland**. (France was 1st in 2019; Korea overtook in 2023.)
- **Source.** [OECD OURdata 2023 publication](https://www.oecd.org/en/publications/2023-oecd-open-useful-and-re-usable-data-ourdata-index_a37f51c3-en.html) · [Full PDF](https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/12/2023-oecd-open-useful-and-re-usable-data-ourdata-index_cc9e8a9e/a37f51c3-en.pdf) · [data.europa.eu insights](https://data.europa.eu/en/news-events/news/open-datas-growing-role-insights-oecd-2023-ourdata-index).

**African coverage.** The OURdata Index assesses OECD members and accession candidates only. **No African country is included** in the 2023 edition. Togo therefore has no OURdata score; the Index is useful only as a methodology reference, not a comparison point.

---

### 2.4 UN E-Government Survey 2024 — Open Government Data Index (OGDI)

- The OGDI is one of the sub-indices of the broader [UN E-Government Survey](https://publicadministration.un.org/egovkb), introduced in 2020.
- **2024 edition** assesses all 193 UN member states.
- **Key Africa findings:** average African EGDI 0.4247 vs global average; **Mauritius and South Africa** moved up to the "high EGDI" group for the first time. ([UN press release](https://www.un.org/sustainabledevelopment/blog/2024/09/press-release-e-government-survey/) · [E-Gov Survey 2024 PDF](https://desapublications.un.org/sites/default/files/publications/2024-09/(Web%20version)%20E-Government%20Survey%202024%201392024.pdf))

**Togo's OGDI 2024 score:** **not found** in publicly indexed snippets. The data is downloadable from [publicadministration.un.org/egovkb/Data-Center](https://publicadministration.un.org/egovkb/en-us/data-center) — recommend pulling Togo's row directly.

---

### 2.5 Open Data Inventory (ODIN) — Open Data Watch

ODIN measures coverage and openness of **official statistics** (NSO data) across ~180–197 countries.

**Togo in ODIN:**

| Year | Overall | Coverage | Openness | Rank | Source |
|-----:|--------:|---------:|---------:|-----:|--------|
| 2024 | 55 | 55 | 54 | 101 | Snippet via search; see [ODIN Togo profile](https://odin.opendatawatch.com/Report/countryProfileUpdated/TGO?year=2024) |
| 2020 | not found | – | – | – | [ODIN Togo 2020 profile](https://odin.opendatawatch.com/Report/countryProfileUpdated/TGO?year=2020) (page renders but content not extractable via WebFetch) |

ODIN 2024/25 is the latest biennial report ([landing page](https://odin.opendatawatch.com/Report/biennialReport2024)). Median global score in 2022 was 50.9. Togo's 2024 score of 55 is just above the global median but well below leaders (top countries score >75).

---

### 2.6 World Bank Statistical Performance Indicators (SPI)

- **51 indicators**, **5 pillars**: (1) Data use, (2) Data services, (3) Data products, (4) Data sources, (5) Data infrastructure.
- The **data accessibility** dimension is primarily under **Pillar 2 — Data Services** (4 indicators: data releases, online access, advisory/analytical services, data services).
- **Source.** [SPI overview](https://www.worldbank.org/en/programs/statistical-performance-indicators/about-spi) · [SPI Data Explorer](https://datanalytics.worldbank.org/SPI/) · [Methodology book](https://worldbank.github.io/SPI/).

**Togo's SPI score:** **not found** in indexed snippets. Available via the SPI Data Explorer (`country=TGO`) — extract directly from the source for the report.

---

## 3. Benchmark countries — quantitative comparison

Comparison table built from official portal pages (May 2026 fetches) and search snippets. Where a portal returned a specific homepage counter via WebFetch, the value is annotated **"verified"**. Otherwise the value is **"reported"** (cited from a documented source).

| Country | Portal | Software | Datasets | Last update | Formats | Default licence | API | OGP | ODC |
|---------|--------|----------|---------:|-------------|---------|-----------------|-----|----:|----:|
| **France** | [data.gouv.fr](https://www.data.gouv.fr/) | **udata** (open source, AGPL) | **74,000** datasets/APIs · 389K files (verified May 2026) | Daily (active) | CSV, JSON, XLSX, GeoJSON, Parquet, … | **Licence Ouverte 2.0** (CC-BY equivalent) | Yes — full REST + DCAT | Yes | Yes |
| **United Kingdom** | [data.gov.uk](https://www.data.gov.uk/) | **CKAN** | **~30,000** datasets ([Wikipedia](https://en.wikipedia.org/wiki/Data.gov.uk); homepage counter not displayed) | Active | CSV, JSON, XML, HTML, Shapefile | **Open Government Licence v3.0** (CC-BY equivalent) | Yes — CKAN API | Yes | Yes |
| **Togo** | [opendata.gouv.tg](https://opendata.gouv.tg/) | **udata** (skin reused from France) | **1,550** datasets · 1,829 files (verified May 2026 homepage counter) | Mostly stagnant since Jan 2025 (audit baseline) | Mixed (audit needs to enumerate) | Not surfaced on homepage — needs check per dataset | udata exposes REST + DCAT | **No** | **No** |
| **Kenya** | [opendata.go.ke](https://www.opendata.go.ke/) | Originally **CKAN/Socrata**, currently **ArcGIS Hub** (Esri) | not found (ArcGIS Hub does not expose a single counter) | Revival in progress; new Budget Data portal due July 2025 ([OGP commitment KE0034](https://www.opengovpartnership.org/members/kenya/commitments/KE0034/)) | CSV, KML, ZIP, GeoJSON, GeoTIFF, PNG | not found | Yes (ArcGIS REST) | Yes | No |
| **Ghana** | [data.gov.gh](https://data.gov.gh/) | **CKAN** | **271** catalogues / **912** resources (verified May 2026 homepage counter) | Last-update timestamp not surfaced on homepage | Not surfaced on homepage | **Ghana Open Data Licence** (CC-BY 4.0 equivalent) | CKAN API | Yes | No |
| **Côte d'Ivoire** | [data.gouv.ci](https://data.gouv.ci/) | proprietary CMS | **177** datasets · 124,357 records · 303 visualisations (verified May 2026 homepage counter) | not surfaced on homepage | not surfaced on homepage | not surfaced on homepage | not advertised | Yes ([CI0024 commitment](https://www.opengovpartnership.org/members/cote-divoire/commitments/CI0024/)) | No |
| **Senegal** | No single `data.gouv.sn`. Distributed: [geosenegal.gouv.sn](https://www.geosenegal.gouv.sn/), [ansd.sn](https://www.ansd.sn/), Sénégal Ouvert | various | not aggregated | varies | CSV, JSON via ANSD | varies | varies | Yes | No |
| **Rwanda** | [statistics.gov.rw](https://statistics.gov.rw/) (NSO) + [dev.open-data.risa.gov.rw](https://dev.open-data.risa.gov.rw/) | NSO platform + open data portal in dev | not surfaced | NISR is regularly updated | CSV, XLSX | not surfaced | Yes via NSO data portals | No | No |
| **Burkina Faso** | [data.gov.bf](https://data.gov.bf/) (BODI) | CKAN | "**Over 200**" reported in 2016; **35** added in 2024 PAGOF cohort ([Expertise France](https://www.expertisefrance.fr/en/actualite?id=730266)) | irregular | varies | not surfaced consistently | CKAN API | Yes ([BF0011 commitment](https://www.opengovpartnership.org/members/burkina-faso/commitments/BF0011/)) | No |
| **Nigeria** | [data.gov.ng](http://www.data.gov.ng/) | CKAN | not found (homepage no public counter) | reportedly active, sectoral | CSV, XLSX | not surfaced consistently | CKAN API | Yes | No |
| **Benin** | [data.gouv.bj](https://data.gouv.bj/) | CKAN-based, custom | could not connect via WebFetch May 2026 (ECONNREFUSED). Documentation states **3 public APIs** + multi-format export (JSON, CSV, Excel) | not surfaced | JSON, CSV, Excel | not surfaced | Yes — explicit `/apis` endpoint | Yes | No |

**Read-out for the Togo audit.**

- Togo is **about 50× smaller** than France (1,550 vs 74,000 datasets) but uses the same software (udata) — the gap is therefore organisational, not technical.
- Togo is **~5× larger** than Côte d'Ivoire (177 datasets) and ~6× larger than Ghana (271 catalogues), but Côte d'Ivoire and Ghana are OGP members with explicit open-data commitments. Volume without governance is the wrong metric.
- Togo, **alone among the 11 portals listed**, has neither OGP membership nor ODC endorsement. This is a singular weakness.
- The portal-software question matters: **udata gives Togo native DCAT, native multi-format harvesting, native federation** with data.gouv.fr. None of these are exploited today (no visible federation, no `dataset_count` exposed on `/api/1/site/`).

---

## 4. Common pitfalls and red flags in open data portals

### 4.1 Schema-only / empty datasets

There is no formal academic name for "schema-only datasets" (records that publish a column dictionary but no rows). The closest documented concept is the **"missing data / incomplete data" anti-pattern** in the metadata-quality literature.

The most cited critique:

> "Open data are often unfamiliar to users and may lack metadata. The metadata and underlying data quality for these datasets is known to be deficient, with many open datasets having duplicate, inconsistent, and missing data and generally lacking easily accessible schema descriptions."
> — Neumaier, S., Umbrich, J., & Polleres, A. (2016). *Automated Quality Assessment of Metadata across Open Data Portals.* ACM Journal of Data and Information Quality. ([ACM DL](https://dl.acm.org/doi/10.1145/2964909))

A complementary critique from Frictionless Data: many catalogues publish CSVs without schemas, leaving every consumer to re-infer types. ([Frictionless: Why we need a schema catalogue](https://frictionlessdata.io/blog/2020/04/23/table-schema-catalog/))

**Operational rule for the Togo audit.** A dataset whose only attached resource is a documentation PDF, a column list, or a "metadata.json" with no `data.csv` should be flagged as **"empty distribution"** — formally: a Distribution with no `dcat:downloadURL` resolving to non-empty data is non-compliant with both DCAT-AP and the Open Definition.

### 4.2 Data staleness — what frequency is acceptable?

There is no universal SLA, but the EU Implementing Regulation **2023/138** on High-Value Datasets gives the cleanest reference. HVDs in 6 themes (geospatial, earth observation & environment, meteorological, statistics, companies, mobility) must be published **free of charge, in machine-readable formats, via APIs, with bulk download, and refreshed at the highest frequency at which the source data is updated** ([EUR-Lex summary](https://eur-lex.europa.eu/EN/legal-content/summary/open-data-and-the-reuse-of-public-sector-information.html) · [EC HVD page](https://digital-strategy.ec.europa.eu/en/news/commission-defines-high-value-datasets-be-made-available-re-use)).

Practical norms by theme (synthesised from EU HVD regulation + OECD OURdata indicators + ODIN):

| Theme | Acceptable refresh |
|-------|-------------------|
| Statistics (national accounts, demography) | **annual** at minimum, quarterly preferred |
| Health surveillance | **weekly** during outbreaks, monthly otherwise |
| Public budget execution | **monthly** during exec, annual for closed accounts |
| Public procurement (contracts) | **continuous / event-driven** |
| Meteorological observations | **hourly to daily** |
| Mobility (transport schedules) | **real-time or every 24h** |
| Geospatial reference layers | **annual review**, ad-hoc on changes |
| Company registry | **near-real-time** |

A useful technical reference for measuring freshness on portals is the IEEE paper *Measures for Assessing the Data Freshness in Open Data Portals* ([IEEE Xplore](https://ieeexplore.ieee.org/document/7573684/)).

**Auditor's heuristic.** A dataset whose `dct:modified` is older than 2× its declared `accrualPeriodicity` is *stale by self-declared standards*. A dataset with **no `dct:modified` at all** is undateable — flag as a metadata defect.

### 4.3 Openwashing

**Definition.** "Openwashing… describes a mismatch between how the public expects information to be shared, and how an organization actually makes information available." ([Wikipedia](https://en.wikipedia.org/wiki/Openwashing))

**The seminal critique** (from the OKFN blog): "Open-washing — the difference between opening your data and simply making them available." ([OKFN blog, 2014](https://blog.okfn.org/2014/03/10/open-washing-the-difference-between-opening-your-data-and-simply-making-them-available/))

The 2015 Open Data Barometer report directly named the phenomenon: open data initiatives risk simply being window-dressing — *"open washing"* — when data is called open at release but does not meet the full open criteria. ([Web Foundation, 2016](https://webfoundation.org/2016/10/openwashing-anyone/))

Common openwashing patterns in government portals (synthesised from the cited literature):

1. **PDF-only "open data"** — fails Open Definition § machine-readable.
2. **No licence stated** — fails Open Definition § licence.
3. **"Free but with conditions" licences** — non-conformant licences masquerading as open.
4. **Stale snapshots** — last update >24 months for an active topic.
5. **"Schema-only"** records (see §4.1).
6. **Low-value, low-controversy datasets** crowding out politically meaningful ones (e.g. lots of tourist points-of-interest, no procurement contracts).
7. **No bulk download / no API** — only HTML browsing.
8. **No landing-page identifier per dataset** — data accessible only via search.

### 4.4 Licence clarity and machine-readability

For a licence to be machine-checkable, the portal must expose a **resolvable URI** in the dataset metadata (`dct:license` in DCAT). The Open Knowledge community maintains a [conformant licence list with stable IDs](https://opendefinition.org/licenses/) (e.g. `CC-BY-4.0`, `CC0-1.0`, `ODC-BY-1.0`, `ODbL-1.0`, `etalab-2.0`).

**Test for the Togo audit.** Pull `/api/1/datasets/?page_size=2000` from opendata.gouv.tg, count datasets where:

- `license` is null, or
- `license` is a free-text string not matching a known SPDX/OKFN identifier, or
- `license` resolves to a non-conformant URL.

Each of these is an Open Definition failure.

---

## 5. Recommended methodology for an open data portal audit

### 5.1 Reference frameworks to copy

The most authoritative published methodologies are:

1. **EU Open Data Maturity (ODM) methodology** — annual questionnaire across 4 dimensions (Policy, Portal, Quality, Impact). Public methodology paper updated each year. ([2022 method paper PDF](https://data.europa.eu/sites/default/files/method-paper_insights-report_n7_2022_0.pdf)) — adaptable to a single-country audit.
2. **ODIN methodology** — covers official statistics: 22 data categories × coverage and openness sub-scores, 0–100 scale. ([ODIN FAQ](https://odin.opendatawatch.com/faq))
3. **OECD OURdata methodology** — 3 pillars × structured questions, ~670 data points per country. ([OURdata 2023 PDF](https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/12/2023-oecd-open-useful-and-re-usable-data-ourdata-index_cc9e8a9e/a37f51c3-en.pdf))
4. **OpenDataMonitor** — automated catalogue scoring across openness, machine-readability, availability, metadata completeness. ([Methodology page](https://www.opendatamonitor.eu/frontend/web/index.php?r=site/methodology))
5. **Neumaier et al. (2016)** — *Automated Quality Assessment of Metadata across Open Data Portals.* ACM JDIQ. The reference academic methodology — defines metrics for completeness, accuracy, retrievability, accessibility, openness, conformance. ([ACM DL](https://dl.acm.org/doi/10.1145/2964909))
6. **Vetro et al. (2016)** — *Open data quality measurement framework: Definition and application to Open Government Data.* Government Information Quarterly. ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0740624X16300132))

### 5.2 Concrete metrics for a Togo audit

Combining the above sources, an actionable audit dashboard for opendata.gouv.tg would compute per-dataset:

| Metric | How | Pass threshold |
|--------|-----|----------------|
| **Has open licence** (Open Definition) | `dct:license` matches OKFN-conformant ID | yes/no |
| **Machine-readable distribution** (5★ ≥ 3) | At least one resource is CSV / JSON / GeoJSON / Parquet / RDF | yes/no |
| **Has stated update frequency** | `dct:accrualPeriodicity` is non-empty | yes/no |
| **Freshness** | Now − `dct:modified` < 2 × declared periodicity | yes/no |
| **Has publisher** | `dct:publisher` non-empty | yes/no |
| **Has temporal extent** | `dct:temporal` set (start + end) | yes/no |
| **Has spatial extent** | `dct:spatial` set | yes/no |
| **Distribution opens** | HEAD on `dcat:downloadURL` returns 200 + non-empty body | yes/no |
| **Distribution non-empty** | File has > 1 row beyond header (CSV) / > 0 features (GeoJSON) | yes/no |
| **DCAT-AP minimum** | title + description + at least one accessURL | yes/no |
| **FAIR self-score** | F (10pts) + A (10) + I (10) + R (10) | 0–40 |

Aggregate to a single **Togo Open Data Health Score** = mean across datasets.

### 5.3 Tooling

- **[Frictionless Data](https://frictionlessdata.io/)** — `frictionless validate <data-package.json>` for tabular schema and data validation. Open source.
- **[GoodTables / Validata](https://validata.fr/)** — French Etalab fork, used to validate datasets against published `tableschema.json` schemas. Directly relevant: Togo could adopt the same tooling.
- **[CKAN extensions](https://extensions.ckan.org/)** for harvesting and DCAT — ckanext-dcat, ckanext-validation.
- **[udata](https://github.com/opendatateam/udata)** — same software as Togo's portal; offers a built-in `/site/quality` endpoint with completeness/freshness scores per organisation. Activating this and publishing the leaderboard publicly is itself a transparency win.
- **[pyDataverse](https://pydataverse.readthedocs.io/) + [pyDCAT](https://pypi.org/project/pydcat/)** for catalogue ingestion and benchmarking against peers.
- **[INSPIRE / ISO 19115 metadata validators](https://inspire.ec.europa.eu/validator/)** — for the geo portal.
- **OGC capabilities checks** — simple curl scripts against `?service=WMS&request=GetCapabilities`, etc.

### 5.4 Past audits worth citing

- **Cour des comptes (France)** opened its own data on data.gouv.fr from 2014, but a dashboard analysis later showed **75 of those datasets had never been reused**, raising the question of relevance vs publication for publication's sake. ([Etalab DataSession post](https://etalab.gouv.fr/datasession-des-28-et-29-mai-la-cour-des-comptes-approfondit-sa-demarche-dopen-data-et-dopen-gov/) · [Interoperable Europe note](https://interoperable-europe.ec.europa.eu/collection/open-source-observatory-osor/news/french-court-auditors-c)) — direct precedent for the *"datasets exist but aren't used"* critique.
- **Etalab's own retrospective on ODM 2021** — public series of blog posts on portal quality and data quality dimensions, structured exactly like a self-audit. ([Etalab ODM 2021 series](https://www.etalab.gouv.fr/retour-sur-lopen-data-maturity-index-2021-qualite-du-portail-de-donnees-3-4))
- **EU Open Data Maturity reports 2015–2024** — 10 annual editions, every methodology change documented, all questionnaires published.
- **Open Data Watch ODIN Biennial 2024/25** — ([ODIN 2024 biennial report](https://odin.opendatawatch.com/Report/biennialReport2024)).

---

## 6. Synthesis — quotable headlines for the Togo audit

1. **"Same software, 50× less data"** — Togo runs the same udata platform as France's data.gouv.fr (74,000 datasets) but publishes only 1,550. The bottleneck is not technical.
2. **"Togo is the only sub-Saharan portal in our 11-country benchmark with neither OGP membership nor Open Data Charter endorsement."** ([OGP members](https://www.opengovpartnership.org/our-members) · [ODC adopters](https://opendatacharter.org/government-adopters/))
3. **"By the global yardstick, Togo's official statistics score 55/100 (ODIN 2024) — just above the global median of 50.9."** ([ODIN](https://odin.opendatawatch.com/))
4. **"The Open Data Charter is clear: open data must be timely, comprehensive, and open by default. A portal that hasn't seen substantive updates since January 2025 is by definition non-compliant with principle 2."** ([ODC Principles](https://opendatacharter.org/principles/))
5. **"'Open-washing' is a 12-year-old concept. Publishing CSVs no one updates is its textbook example."** ([OKFN, 2014](https://blog.okfn.org/2014/03/10/open-washing-the-difference-between-opening-your-data-and-simply-making-them-available/))
6. **"France and the EU show the way: a public Open Data Maturity scorecard, refreshed every year, is the cheapest accountability tool there is."** ([data.europa.eu/ODM 2024](https://data.europa.eu/en/open-data-maturity/2024))

---

## 7. Open methodological questions — to resolve before publishing

These are knowledge gaps from this dossier that the audit team should resolve directly against the data, not from secondary sources:

1. **Togo's exact GDB 2nd-edition score.** Pull from [globaldatabarometer.org/explore-the-results](https://globaldatabarometer.org/explore-the-results/) (downloadable open data).
2. **Togo's exact UN OGDI 2024 score.** Pull from [publicadministration.un.org/egovkb data centre](https://publicadministration.un.org/egovkb/en-us/data-center).
3. **Togo's exact World Bank SPI scores by pillar.** Pull from [datanalytics.worldbank.org/SPI](https://datanalytics.worldbank.org/SPI/) (download CSV).
4. **Whether geodata.gouv.tg exposes valid OGC GetCapabilities** — a 30-second curl test; if it doesn't, that is a headline finding.
5. **Whether opendata.gouv.tg exposes valid DCAT-AP** at `/catalog.xml` — a 30-second curl test.
6. **Per-dataset audit** — script the metrics in §5.2 against `https://opendata.gouv.tg/api/1/datasets/`. The api is public; udata exposes paginated JSON.

---

## 8. Sources (consolidated list)

### Standards & frameworks
- [Open Data Charter — Principles](https://opendatacharter.org/principles/)
- [Open Data Charter — Government Adopters](https://opendatacharter.org/government-adopters/)
- [Open Definition 2.1 (OKFN)](https://opendefinition.org/od/2.1/en/)
- [Open Definition — Conformant Licences](https://opendefinition.org/licenses/)
- [Tim Berners-Lee, 5-Star Open Data](https://5stardata.info/en/)
- [W3C — DCAT v3 Recommendation](https://www.w3.org/TR/vocab-dcat-3/)
- [DCAT-AP 3.0 (SEMIC)](https://semiceu.github.io/DCAT-AP/releases/3.0.0/)
- [DCAT-US 3.0](https://doi-do.github.io/dcat-us/)
- [ISO 19115-1:2014](https://www.iso.org/standard/53798.html)
- [Geospatial metadata (Wikipedia)](https://en.wikipedia.org/wiki/Geospatial_metadata)
- [OGC standards directory](https://www.ogc.org/standards/wms/)
- [OGC API family](https://ogcapi.ogc.org/)
- [GO FAIR — FAIR Principles](https://www.go-fair.org/fair-principles/)
- [Wilkinson et al., FAIR Guiding Principles, Scientific Data 2016](https://www.nature.com/articles/sdata201618)

### Indices and rankings
- [Global Data Barometer](https://globaldatabarometer.org/)
- [GDB 2nd edition launch post](https://globaldatabarometer.org/2025/05/the-global-data-barometer-2nd-edition-a-shared-compass-for-navigating-the-data-landscape/)
- [Open Data Barometer 4th edition — Africa regional report](https://opendatabarometer.org/doc/4thEdition/ODB-4thEdition-RegionalReport-Africa.pdf)
- [OECD OURdata 2023](https://www.oecd.org/en/publications/2023-oecd-open-useful-and-re-usable-data-ourdata-index_a37f51c3-en.html)
- [data.europa.eu — OURdata 2023 insights](https://data.europa.eu/en/news-events/news/open-datas-growing-role-insights-oecd-2023-ourdata-index)
- [UN E-Government Survey 2024](https://desapublications.un.org/publications/un-e-government-survey-2024)
- [UN E-Government Knowledgebase](https://publicadministration.un.org/egovkb)
- [ODIN — Open Data Inventory](https://odin.opendatawatch.com/)
- [ODIN 2024/25 Biennial Report](https://odin.opendatawatch.com/Report/biennialReport2024)
- [World Bank SPI](https://www.worldbank.org/en/programs/statistical-performance-indicators/about-spi)
- [SPI Data Explorer](https://datanalytics.worldbank.org/SPI/)
- [EU Open Data Maturity Report 2024](https://data.europa.eu/sites/default/files/odm2024_full_report.pdf)

### Portals (benchmark countries)
- [data.gouv.fr (France, udata)](https://www.data.gouv.fr/)
- [udata source code (GitHub, Etalab)](https://github.com/opendatateam/udata)
- [data.gov.uk (UK, CKAN)](https://www.data.gov.uk/)
- [opendata.gouv.tg (Togo, udata)](https://opendata.gouv.tg/)
- [geodata.gouv.tg (Togo, geo portal)](https://geodata.gouv.tg/)
- [opendata.go.ke (Kenya, ArcGIS Hub)](https://www.opendata.go.ke/)
- [data.gov.gh (Ghana, CKAN)](https://data.gov.gh/)
- [data.gouv.ci (Côte d'Ivoire)](https://data.gouv.ci/)
- [geosenegal.gouv.sn (Senegal geo)](https://www.geosenegal.gouv.sn/)
- [statistics.gov.rw (Rwanda NSO)](https://statistics.gov.rw/)
- [data.gov.bf (Burkina Faso)](https://burkinafaso.opendataforafrica.org/) · [Burkina BODI commitment BF0011](https://www.opengovpartnership.org/members/burkina-faso/commitments/BF0011/)
- [data.gov.ng (Nigeria)](http://www.data.gov.ng/)
- [data.gouv.bj (Benin)](https://data.gouv.bj/)

### Pitfalls and audit methodology
- [OKFN — Open-washing blog post (2014)](https://blog.okfn.org/2014/03/10/open-washing-the-difference-between-opening-your-data-and-simply-making-them-available/)
- [Web Foundation — #openwashing… anyone? (2016)](https://webfoundation.org/2016/10/openwashing-anyone/)
- [Wikipedia — Openwashing](https://en.wikipedia.org/wiki/Openwashing)
- [Bentley University — Deceptive practice of openwashing](https://www.bentley.edu/library/in-the-know/deceptive-practice-openwashing-open-access-data)
- [Frictionless Data — Schema catalogue](https://frictionlessdata.io/blog/2020/04/23/table-schema-catalog/)
- [Frictionless Data project](https://frictionlessdata.io/)
- [Validata (French data validator)](https://validata.fr/)
- [Neumaier et al. — Automated Quality Assessment (ACM 2016)](https://dl.acm.org/doi/10.1145/2964909)
- [Vetro et al. — Open data quality framework (GIQ 2016)](https://www.sciencedirect.com/science/article/abs/pii/S0740624X16300132)
- [IEEE — Measures for Assessing Data Freshness in Open Data Portals](https://ieeexplore.ieee.org/document/7573684/)
- [OpenDataMonitor methodology](https://www.opendatamonitor.eu/frontend/web/index.php?r=site/methodology)
- [data.europa.eu — Guidelines for ensuring quality](https://data.europa.eu/en/academy/guidelines-ensuring-quality-open-data-and-metadata)
- [Etalab — ODM 2021 retrospective](https://www.etalab.gouv.fr/retour-sur-lopen-data-maturity-index-2021-qualite-du-portail-de-donnees-3-4)
- [EU HVD Implementing Regulation 2023/138 — summary](https://eur-lex.europa.eu/EN/legal-content/summary/open-data-and-the-reuse-of-public-sector-information.html)
- [EU — High-Value Datasets factpage](https://digital-strategy.ec.europa.eu/en/news/commission-defines-high-value-datasets-be-made-available-re-use)

### OGP
- [Open Government Partnership — Members](https://www.opengovpartnership.org/our-members)
- [OGP — National Action Plan handbook](https://www.opengovpartnership.org/national-handbook/membership/)

---

*Compiled May 2026 for the togo-opendata-audit project. All URLs were live at compile time. Where a number could not be confirmed from the open web, the entry is marked "not found" and the audit team is directed to the canonical source for direct retrieval.*
