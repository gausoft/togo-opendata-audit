# Source verification — May 2026

Audited **121 URLs** cited across all public-facing Markdown files.

| Status | Count |
|---|---:|
| OK | 96 |
| BROKEN_ACCEPTED | 11 |
| SPA_TRAP_ACCEPTED | 7 |
| REDIRECT_ACCEPTED | 7 |

## ❌ Unexpected issues — must be fixed

_None. All non-OK URLs are accounted for in `data/processed/url_allowlist.json`._

## ✅ Accepted non-OK URLs (status IS the audit finding)

These URLs are flagged BROKEN/REDIRECT/SPA_TRAP intentionally — their failure mode is itself documented in the report. See `data/processed/url_allowlist.json` for full justification.

| Status | HTTP | URL | Reason |
|---|---|---|---|
| BROKEN | conn-err | `http://www.data.gov.ng/` | Nigeria national portal offline as of May 2026 — finding §6 (regional portal degradation) |
| BROKEN | 404 | `https://api.geodata.gouv.tg/` | Togo geodata API has no public root/docs page — finding §3 (geodata API undocumented) |
| BROKEN | 500 | `https://burkinafaso.opendataforafrica.org/` | Burkina Faso portal returns HTTP 500 — finding §6 (regional portal degradation) |
| SPA_TRAP | 200 | `https://data.europa.eu/en/` | European Data Portal homepage hydrates client-side; loads fine in any browser |
| BROKEN | conn-err | `https://data.gouv.bj/` | Benin domain unresolvable as of May 2026 — finding §6 (regional portal degradation) |
| BROKEN | conn-err | `https://dev.open-data.risa.gov.rw/` | Rwanda dev portal offline — finding §6 |
| BROKEN | 403 | `https://dl.acm.org/doi/10.1145/2964909` | ACM Cloudflare anti-bot 403 to scripts; resolves in browsers |
| REDIRECT | 200 | `https://doi.org/10.1016/j.giq.2016.02.001` | DOI canonical; redirects to publisher are normal |
| REDIRECT | 200 | `https://doi.org/10.1038/sdata.2016.18` | DOI canonical; Nature cookie banner is normal |
| SPA_TRAP | 202 | `https://eur-lex.europa.eu/EN/legal-content/summary/open-data-and-the-reuse-of-public-sector-information.html` | EUR-Lex summary page hydrates with JS; readable in any browser |
| BROKEN | 404 | `https://geoserver.geoportail.gouv.tg/` | GeoServer root unconfigured — finding §3 (default placeholder install) |
| REDIRECT | 200 | `https://github.com/gausoft/togo-opendata-audit.git` | Git clone URL; canonical for cloning, GitHub strips .git for browser |
| BROKEN | 404 | `https://odin-aim.akroninc.net/api/api/client/` | ODIN internal backend (used to fetch Togo JSON); not a user-facing reference |
| BROKEN | 405 | `https://odin-aim.akroninc.net/api/api/client/GetCountryProfile/2024/TGO` | ODIN internal backend (POST-only endpoint, GET=405); see data/raw/odin_tgo_2024.json for archived response |
| SPA_TRAP | 200 | `https://odin.opendatawatch.com/Report/biennialReport2024` | ODIN is a SPA — JSON archived in data/raw/odin_report_2024.json |
| SPA_TRAP | 200 | `https://odin.opendatawatch.com/Report/countryProfileUpdated/TGO?year=2020` | ODIN SPA — historical profile referenced for trend |
| SPA_TRAP | 200 | `https://odin.opendatawatch.com/Report/countryProfileUpdated/TGO?year=2024` | ODIN SPA — JSON archived in data/raw/odin_tgo_2024.json |
| SPA_TRAP | 200 | `https://odin.opendatawatch.com/faq` | ODIN SPA — methodology FAQ |
| SPA_TRAP | 200 | `https://pydataverse.readthedocs.io/en/latest/` | ReadTheDocs SPA; full docs render in browser |
| REDIRECT | 200 | `https://web.archive.org/web/2024/https://etalab.gouv.fr/datasession-des-28-et-29-mai-la-cour-des-comptes-approfondit-sa-demarche-dopen-data-et-dopen-gov/` | Wayback short-form intentionally resolves to nearest snapshot |
| REDIRECT | 200 | `https://web.archive.org/web/2024/https://webfoundation.org/2016/10/openwashing-anyone/` | Wayback short-form intentionally resolves to nearest snapshot |
| REDIRECT | 200 | `https://web.archive.org/web/2024/https://www.ansd.sn/` | Wayback short-form intentionally resolves to nearest snapshot |
| REDIRECT | 200 | `https://web.archive.org/web/2024/https://www.etalab.gouv.fr/retour-sur-lopen-data-maturity-index-2021-qualite-du-portail-de-donnees-3-4` | Wayback short-form intentionally resolves to nearest snapshot |
| BROKEN | 403 | `https://www.oecd.org/en/publications/2023-oecd-open-useful-and-re-usable-data-ourdata-index_a37f51c3-en.html` | OECD Cloudflare anti-bot 403 to scripts; resolves in browsers |
| BROKEN | 404 | `https://www.opendata.go.ke/` | Kenya portal returns 404 as of May 2026 — finding §6 |

## All OK URLs

| HTTP | URL | Title |
|---|---|---|
| 200 | `https://5stardata.info/` | Redirecting&hellip; |
| 200 | `https://5stardata.info/en/` | 5-star Open Data |
| 200 | `https://api.worldbank.org/v2/country/TGO/indicator/IQ.SPI.OVRL?format=json` | (no title) |
| 200 | `https://api.worldbank.org/v2/country/TGO/indicator/IQ.SPI.PIL1?format=json` | (no title) |
| 200 | `https://blog.okfn.org/2014/03/10/open-washing-the-difference-between-opening-your-data-and-simply-making-them-available/` | “Open-washing” – The difference between opening your data and simply making them |
| 200 | `https://data.europa.eu/en/academy/guidelines-ensuring-quality-open-data-and-metadata` | Guidelines for ensuring quality in open data and metadata / data.europa.eu |
| 200 | `https://data.europa.eu/en/news-events/news/open-datas-growing-role-insights-oecd-2023-ourdata-index` | Open data&#039;s growing role: Insights from the OECD 2023 OURdata Index / data. |
| 200 | `https://data.europa.eu/en/open-data-maturity/2024` | Explore 2024 Open Data Maturity Report / EDP |
| 200 | `https://data.europa.eu/sites/default/files/2025-06/2024_odm_highlights.pdf` | (no title) |
| 200 | `https://data.europa.eu/sites/default/files/method-paper_insights-report_n7_2022_0.pdf` | (no title) |
| 200 | `https://data.europa.eu/sites/default/files/odm2024_full_report.pdf` | (no title) |
| 200 | `https://data.gouv.ci/` | Portail officiel des données ouvertes |
| 200 | `https://data.gov.bf/` | Modern Data Platform - Data Lake & Analytics |
| 200 | `https://data.gov.gh/` | Ghana Open Data Initiative / Ghana's Open Data Portal |
| 200 | `https://data360api.worldbank.org/data360/data?DATABASE_ID=WB_GTMI&REF_AREA=TGO&format=json` | (no title) |
| 200 | `https://datanalytics.worldbank.org/SPI/` | Statistical Performance Indicators Data Explorer |
| 200 | `https://desapublications.un.org/publications/un-e-government-survey-2024` | Public Administration / DESA Publications |
| 200 | `https://desapublications.un.org/sites/default/files/publications/2024-09/%28Web%20version%29%20E-Government%20Survey%202024%201392024.pdf` | (no title) |
| 200 | `https://desapublications.un.org/sites/default/files/publications/2024-09/Technical%20Appendix%20%28Web%20version%29%201292024.pdf` | (no title) |
| 200 | `https://dig.watch/countries/togo` | Togo / Digital Watch Observatory |
| 200 | `https://digital-strategy.ec.europa.eu/en/news/commission-defines-high-value-datasets-be-made-available-re-use` | Commission defines high-value datasets to be made available for re-use / Shaping |
| 200 | `https://docs.google.com/document/d/1q9QGI5svEY6RRmi7jkgQtX1Sjms3sznH/edit` | ODIN 2024/25 Methodology Guide.docx - Google Docs |
| 200 | `https://documents1.worldbank.org/curated/en/099035001132365997/pdf/P1694820bcef0903e091160315d2050d03b.pdf` | (no title) |
| 200 | `https://documents1.worldbank.org/curated/en/099906411082488994/pdf/IDU163882895175b914ffd18dab1f867779bf6d5.pdf` | (no title) |
| 200 | `https://ecosystem.ckan.org/extension/` | Extension - CKAN Ecosystem Catalog Beta |
| 200 | `https://en.wikipedia.org/wiki/Data.gov.uk` | data.gov.uk - Wikipedia |
| 200 | `https://en.wikipedia.org/wiki/Geospatial_metadata` | Geospatial metadata - Wikipedia |
| 200 | `https://en.wikipedia.org/wiki/International_Open_Data_Charter` | International Open Data Charter - Wikipedia |
| 200 | `https://en.wikipedia.org/wiki/Openwashing` | Openwashing - Wikipedia |
| 200 | `https://frictionlessdata.io/` | Frictionless Data / Frictionless Data |
| 200 | `https://frictionlessdata.io/blog/2020/04/23/table-schema-catalog/` | Open Data Quality, Standardization and Why we Need a Schema Catalog / Frictionle |
| 200 | `https://geodata.gouv.tg` | Geodata Togo |
| 200 | `https://geodata.gouv.tg/` | Geodata Togo |
| 200 | `https://geoserver.geosolutionsgroup.com/edu/en/ogc_protocol_intro/index.html` | Introduction to OGC &mdash; GeoServer Training |
| 200 | `https://github.com/azavea/open-data-standards/blob/master/standards/general_standards/geospatial_data/ogc_wms-wfs-wcs-wmts-wps.md` | open-data-standards/standards/general_standards/geospatial_data/ogc_wms-wfs-wcs- |
| 200 | `https://github.com/gausoft` | gausoft (Gauthier Eholoum) · GitHub |
| 200 | `https://github.com/gausoft/togo-opendata-audit` | GitHub - gausoft/togo-opendata-audit: Independent audit of Togo&#39;s open data  |
| 200 | `https://github.com/gausoft/togo-opendata-audit/blob/main/data/raw/odin_tgo_2024.json` | togo-opendata-audit/data/raw/odin_tgo_2024.json at main · gausoft/togo-opendata- |
| 200 | `https://github.com/gausoft/togo-opendata-audit/issues` | Issues · gausoft/togo-opendata-audit · GitHub |
| 200 | `https://github.com/geoserver/geoserver` | GitHub - geoserver/geoserver: Official GeoServer repository · GitHub |
| 200 | `https://github.com/opendatateam/udata` | GitHub - opendatateam/udata: Customizable and skinnable social platform dedicate |
| 200 | `https://globaldatabarometer.org/` | Global Data Barometer |
| 200 | `https://globaldatabarometer.org/2025/05/the-global-data-barometer-2nd-edition-a-shared-compass-for-navigating-the-data-landscape/` | The Global Data Barometer 2nd edition: A Shared Compass for Navigating the Data  |
| 200 | `https://globaldatabarometer.org/comparison-with-first-edition/` | Comparison with First Edition / Global Data Barometer |
| 200 | `https://globaldatabarometer.org/explore-the-results/` | Explore the Results / Global Data Barometer |
| 200 | `https://globaldatabarometer.org/methodology/` | Methodology / Global Data Barometer |
| 200 | `https://ieeexplore.ieee.org/document/7573684/` | Measures for Assessing the Data Freshness in Open Data Portals / IEEE Conference |
| 200 | `https://interoperable-europe.ec.europa.eu/collection/open-source-observatory-osor/news/french-court-auditors-c` | French Court of Auditors to c… / Interoperable Europe Portal |
| 200 | `https://knowledge-base.inspire.ec.europa.eu/news-and-publications/news/discontinuation-inspire-reference-validator-2026-04-01_en` | Discontinuation of the INSPIRE Reference Validator - INSPIRE Knowledge Base |
| 200 | `https://odin.opendatawatch.com/` | Open Data Inventory—Global Index of Open Data - Open Data Inventory |
| 200 | `https://ogcapi.ogc.org/` | OGC API |
| 200 | `https://opendata.gouv.tg/api/1/datasets/` | (no title) |
| 200 | `https://opendata.gouv.tg/fr/` | Accueil - opendata.gouv.tg |
| 200 | `https://opendatabarometer.org/doc/4thEdition/ODB-4thEdition-RegionalReport-Africa.pdf` | (no title) |
| 200 | `https://opendatacharter.org/` | Open Data Charter |
| 200 | `https://opendatacharter.org/government-adopters/` | Open Data Charter |
| 200 | `https://opendatacharter.org/principles/` | Open Data Charter |
| 200 | `https://opendefinition.org/licenses/` | Conformant Licenses - Open Definition - Defining Open in Open Data, Open Content |
| 200 | `https://opendefinition.org/od/2.1/en/` | Open Definition 2.1 - Open Definition - Defining Open in Open Data, Open Content |
| 200 | `https://publicadministration.un.org/egovkb` | EGOVKB / United Nations > Home |
| 200 | `https://publicadministration.un.org/egovkb/en-us/` | EGOVKB / United Nations > Home |
| 200 | `https://publicadministration.un.org/egovkb/en-us/data-center` | Data Center |
| 200 | `https://pypi.org/project/pydcat/` | Client Challenge |
| 200 | `https://resources.data.gov/resources/dcat-us/` | DCAT-US Schema v1.1 (Project Open Data Metadata Schema) / resources.data.gov |
| 200 | `https://semiceu.github.io/DCAT-AP/releases/3.0.0/` | DCAT-AP 3.0 |
| 200 | `https://statistics.gov.rw/` | Home / National Institute of Statistics of Rwanda |
| 200 | `https://storage.googleapis.com/gdb-2024-analysis/open_data_2nd_edition/country_open_data/gdb-2024-Togo-country-survey-data.csv` | (no title) |
| 200 | `https://storage.googleapis.com/gdb-2024-analysis/open_data_2nd_edition/gdb-2024-full-data.csv` | (no title) |
| 200 | `https://storage.googleapis.com/gdb-files/countries/gdb-2021-togo-complete-survey-data.csv` | (no title) |
| 200 | `https://validata.fr/` | Validata – Accueil |
| 200 | `https://worldbank.github.io/SPI/` | Measuring the Statistical Performance of Countries: An Overview of Updates to th |
| 200 | `https://www.afristat.org/wp-content/uploads/2023/02/TG01_Loi-statistique.pdf` | (no title) |
| 200 | `https://www.bentley.edu/library/in-the-know/deceptive-practice-openwashing-open-access-data` | The Deceptive Practice of Openwashing with Open Access Data / Bentley University |
| 200 | `https://www.data.gouv.fr/` | data.gouv.fr : Plateforme ouverte des données publiques françaises |
| 200 | `https://www.data.gov.uk/` | data.gov.uk - The home of UK public data |
| 200 | `https://www.expertisefrance.fr/en/our-news?id=730266` | Stay up to date on development cooperation / Expertise France |
| 200 | `https://www.geosenegal.gouv.sn/` | Géo Sénégal - Infrastructure nationale de gestion des données géographiques |
| 200 | `https://www.go-fair.org/fair-principles/` | FAIR Principles - GO FAIR |
| 200 | `https://www.iso.org/standard/53798.html` | ISO 19115-1:2014 - Geographic information — Metadata — Part 1: Fundamentals |
| 200 | `https://www.ncei.noaa.gov/sites/default/files/2020-04/ISO%2019115-2%20Workbook_Part%20II%20Extentions%20for%20imagery%20and%20Gridded%20Data.pdf` | (no title) |
| 200 | `https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/12/2023-oecd-open-useful-and-re-usable-data-ourdata-index_cc9e8a9e/a37f51c3-en.pdf` | (no title) |
| 200 | `https://www.ogc.org/` | OGC / Open Geospatial Standards for Location Data &amp; GIS |
| 200 | `https://www.ogc.org/standards/wms/` | Web Map Service - Open Geospatial Consortium |
| 200 | `https://www.opendatamonitor.eu/frontend/web/index.php?r=site/methodology` | OpenDataMonitor / Methodology |
| 200 | `https://www.opengovpartnership.org/` | (no title) |
| 200 | `https://www.opengovpartnership.org/members/` | (no title) |
| 200 | `https://www.opengovpartnership.org/members/burkina-faso/commitments/BF0011/` | (no title) |
| 200 | `https://www.opengovpartnership.org/members/cote-divoire/commitments/CI0024/` | (no title) |
| 200 | `https://www.opengovpartnership.org/members/kenya/commitments/KE0034/` | (no title) |
| 200 | `https://www.opengovpartnership.org/national-handbook/membership/` | (no title) |
| 200 | `https://www.rti-rating.org/wp-content/uploads/Togo.pdf` | (no title) |
| 200 | `https://www.un.org/sustainabledevelopment/blog/2024/09/press-release-e-government-survey/` | Press Release / Digital transformation accelerates, but gaps underscore need for |
| 200 | `https://www.w3.org/2011/gld/wiki/5_Star_Linked_Data` | 5 Star Linked Data - Government Linked Data (GLD) Working Group Wiki |
| 200 | `https://www.w3.org/TR/vocab-dcat-3/` | Data Catalog Vocabulary (DCAT) - Version 3 |
| 200 | `https://www.w3.org/news/2024/data-catalog-vocabulary-dcat-version-3-is-a-w3c-recommendation/` | Data Catalog Vocabulary (DCAT) - Version 3 is a W3C Recommendation / 2024 / News |
| 200 | `https://www.worldbank.org/en/programs/statistical-performance-indicators/about-spi` | SPI |
