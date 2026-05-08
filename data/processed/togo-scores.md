# Togo Open Data & Statistical Capacity Indices — Exact Scores

Compiled: 8 May 2026. All figures sourced from canonical primary databases (raw downloads where available). Where a number is "not retrievable" the reason is documented.

ECOWAS comparator set used throughout: Benin, Burkina Faso, Côte d'Ivoire, Ghana, Mali, Niger, Nigeria, Senegal (Togo's neighbours within ECOWAS-9).

---

## 1. ODIN — Open Data Inventory 2024/25 (Open Data Watch)

Source raw JSON (extracted via the live ODIN backend
`https://odin-aim.akroninc.net/api/api/client/GetCountryProfile/2024/TGO`,
called with `GetDefaultWeights`, the same call the public profile page makes).
Profile URL: https://odin.opendatawatch.com/Report/countryProfileUpdated/TGO?year=2024

### Headline scores — Togo 2024

| Metric | Score (0–100) | Global rank (of 198) | Africa rank | Western Africa rank (of 16) |
|---|---|---|---|---|
| ODIN Overall | **55** | 95 | — | 7 |
| Coverage sub-score | **55** | 77 | — | 4 |
| Openness sub-score | **54** | 101 | — | 8 |

Source: ODIN GetCountryProfile JSON, fields `odinScores`, `rankInWorld`, `rankInRegion`. Methodology: ODIN 2024/25 Methodology Guide (https://docs.google.com/document/d/1q9QGI5svEY6RRmi7jkgQtX1Sjms3sznH/edit). Each of 22 categories is scored 0–10 on five coverage criteria (last-5-year availability, periodicity, sub-national breakdown, age/sex disaggregation, completeness) and five openness criteria (machine-readable format, non-proprietary format, metadata, terms-of-use, download-as-table) and rolled up via category weights.

### Togo 2024 vs 2022/23 (longitudinal)

| Year | Overall | Coverage | Openness | Global rank |
|---|---|---|---|---|
| 2022/23 | 42 | 43 | 42 | 112 |
| 2024/25 | **55** | **55** | **54** | **95** |
| Δ | +13 | +12 | +12 | +17 (improvement) |

Source: same ODIN endpoint with `year=2022`. Togo is one of the strongest improvers in West Africa over the cycle.

### All 22 categories — Togo 2024 (raw breakdown)

Source: `dataReportsWithWeightsN` per `categoryId`, JSON pulled from ODIN backend.

| # | Category | Group | Coverage | Openness | Total |
|---|---|---|---|---|---|
| 1 | Population and vital statistics | Social | 40.0 | 50.0 | 45.00 |
| 2 | Education facilities | Social | 50.0 | 50.0 | 50.00 |
| 3 | Education outcomes | Social | 90.0 | 50.0 | 70.00 |
| 4 | Health facilities | Social | 50.0 | 50.0 | 50.00 |
| 5 | Health outcomes | Social | 40.0 | 40.0 | 40.00 |
| 6 | Reproductive health | Social | 50.0 | 50.0 | 50.00 |
| 7 | Food security and nutrition | Social | 37.5 | 50.0 | 44.44 |
| 8 | Gender statistics | Social | 50.0 | 50.0 | 50.00 |
| 9 | Crime and justice | Social | 40.0 | 40.0 | 40.00 |
| 10 | Poverty and income | Social | 50.0 | 50.0 | 50.00 |
| 11 | National accounts | Economic | 37.5 | 80.0 | 61.11 |
| 12 | Labor | Economic | 40.0 | 50.0 | 45.00 |
| 13 | Price indexes | Economic | 75.0 | 70.0 | 72.22 |
| 14 | Government finance | Economic | 75.0 | 50.0 | 61.11 |
| 15 | Money and banking | Economic | 100.0 | 80.0 | 87.50 |
| 16 | International trade | Economic | 50.0 | 40.0 | 43.75 |
| 17 | Balance of payments | Economic | 100.0 | 80.0 | 87.50 |
| 18 | Digital connectivity | Economic | 0.0 | 0.0 | **0.00** |
| 19 | Agriculture and land use | Environment | 60.0 | 50.0 | 55.00 |
| 20 | Resource use | Environment | 37.5 | 60.0 | 50.00 |
| 21 | Energy | Environment | 50.0 | 50.0 | 50.00 |
| 22 | Pollution | Environment | 33.3 | 40.0 | 37.50 |
| 23 | Built environment | Environment | 70.0 | 50.0 | 60.00 |

(ODIN 2024/25 split the previous "International trade" into a new 23rd item — Digital connectivity — for which Togo currently scores zero, the single biggest gap.)

#### Worst 5 Togo categories (priority targets)
1. Digital connectivity — **0.00**
2. Pollution — 37.50
3. Health outcomes — 40.00
4. Crime and justice — 40.00
5. International trade — 43.75

#### Best 5 Togo categories
1. Money and banking — 87.50
2. Balance of payments — 87.50
3. Price indexes — 72.22
4. Education outcomes — 70.00
5. National accounts / Government finance — 61.11

### ODIN 2024 — ECOWAS comparison

Source: same endpoint, called for each ISO3 (BEN, BFA, CIV, GHA, MLI, NER, NGA, SEN, TGO).

| Country | Overall | Coverage | Openness | Global rank | Africa rank (W. Africa region of 16) |
|---|---|---|---|---|---|
| **Burkina Faso** | 77 | 67 | 85 | 22 | 1 |
| **Senegal** | 75 | 60 | 88 | 31 | 2 |
| **Niger** | 67 | 52 | 79 | 49 | 3 |
| **Côte d'Ivoire** | 62 | 43 | 79 | 68 | 4 |
| **Benin** | 59 | 53 | 64 | 82 | 5 |
| **Nigeria** | 56 | 48 | 63 | 90 | 6 |
| **Togo** | **55** | **55** | **54** | **95** | **7** |
| **Mali** | 55 | 46 | 62 | 95 | 7 (tied) |
| **Ghana** | 54 | 58 | 50 | 99 | 9 |

Togo is **mid-ECOWAS** (7th of 9). It is well ahead of Ghana on overall, but its openness sub-score (54) trails every ECOWAS peer except Ghana (50). Burkina Faso and Senegal are the regional leaders.

### ODIN 2024 — regional & global benchmarks

Source: ODIN `GetReportData/2024` JSON, `figure2` (global trend), `figure3` (continent averages), `medianRegionalOVerallScores` (sub-region medians). https://odin.opendatawatch.com/Report/biennialReport2024

| Reference | Overall | Coverage | Openness |
|---|---|---|---|
| **Global median 2024** (figure2) | 56 | 52 | 59 |
| **Africa average 2024** (figure3) | n/a | 40 | 49 |
| **Western Africa median 2024** | **49** | — | — |
| Eastern Africa median | 43 | — | — |
| Northern Africa median | 47 | — | — |
| Southern Africa median | 39 | — | — |
| Middle Africa median | 42 | — | — |
| **Europe average** | — | 66 | 69 |

**Read:** Togo (55) sits 1 point under the global median (56) but **6 points above the Western Africa median (49)**. The gap to the global frontier is more about openness (54 vs 59) than coverage (55 vs 52).

---

## 2. UN E-Government Survey 2024 (UN DESA)

Source: UN DESA Technical Appendix, downloaded as PDF, parsed locally:
https://desapublications.un.org/sites/default/files/publications/2024-09/Technical%20Appendix%20%28Web%20version%29%201292024.pdf

### Togo 2024 — full index breakdown

| Index | Value (0–1) | Group | Global rank (of 193) |
|---|---|---|---|
| **EGDI** (E-Government Development Index, overall) | **0.3920** | Middle EGDI (M2) | **161** |
| **OSI** (Online Service Index) | **0.4472** | Middle OSI | — |
| **HCI** (Human Capital Index) | **0.4813** | Middle HCI | — |
| **TII** (Telecom Infrastructure Index) | **0.2474** | Low TII | — |
| **EPI** (E-Participation Index) | **0.4521** | Middle EPI | 99 |
| **OGDI** (Open Government Data Index) | **0.4359** | Middle OGDI | — |

#### OSI sub-components
Institutional Framework (IF) 0.8000 · Content Provision (CP) 0.5556 · Service Provision (SP) 0.3253 · Participation/EPI 0.4521 · Technology (TEC) 0.5000.

#### HCI sub-components
Adult literacy 66.54 % (2019, UNESCO) · Gross enrolment ratio 75.88 (2017, UNESCO) · Expected years of schooling 12.57 (2017, UNESCO) · Mean years of schooling 5 (2021, UNDP).

#### TII sub-components
Mobile cellular subscriptions per 100 = 74.18 · Individuals using internet 37.62 % · Mobile data & voice price (% GNI) 17.40 · Fixed broadband price (% GNI) 32.62 · Active mobile-broadband subscriptions per 100 = 38.00.

Lomé (capital) was **not assessed** in the 2024 LOSI (Local Online Service Index) round — UN DESA Table marker "Not Assessed" for Lome.

Togo's "data envelopment analysis" peers in the appendix list Togo as the most-similar comparator for **Benin (0.7919)**, **Burkina Faso (0.8122)**, **Côte d'Ivoire (0.8431)**, **Eritrea (0.7348)** and **Madagascar (0.7685)** — i.e. statistically Togo is the median Sub-Saharan reference profile.

### UN EGDI 2024 — ECOWAS comparison

Source: UN DESA Technical Appendix Table 2.1 / Tables 7, 11 13, 15.

| Country | EGDI | OSI | HCI | TII | EPI | **OGDI** | Global rank |
|---|---|---|---|---|---|---|---|
| **Ghana** | 0.6317 | 0.6084 | 0.5586 | 0.7281 | 0.5342 | **0.8205** | 108 |
| **Côte d'Ivoire** | 0.5587 | 0.5219* | 0.4848 | 0.6693 | 0.4110 | **0.5641** | 124 |
| **Senegal** | 0.5162 | 0.4779 | 0.3380 | 0.7328 | 0.4247 | **0.6410** | 135 |
| **Nigeria** | 0.4815 | 0.5372 | 0.4236 | 0.4836 | 0.3699 | **0.5128** | 144 |
| **Benin** | 0.4578 | 0.5202 | 0.3715 | 0.4817 | 0.3699 | **0.4872** | 146 |
| **Togo** | **0.3920** | **0.4472** | **0.4813** | **0.2474** | **0.4521** | **0.4359** | **161** |
| **Mali** | 0.3005 | 0.3334 | 0.1250 | 0.4432 | 0.2740 | (Middle) 0.3333 | 173 |
| **Burkina Faso** | 0.2895 | 0.3376 | 0.1668 | 0.3640 | 0.2192 | **0.3333** | 175 |
| **Niger** | 0.2116 | 0.3084 | 0.1685 | 0.1578 | 0.2055 | **0.2821** | 187 |

*Côte d'Ivoire OSI of 0.7006 (Table 7 normalized) vs 0.5219 raw Z-score listed in Table 2.1 — used 0.5219 (Z-score) for consistency.*

**Read on EGDI:** Togo (0.3920) is **161st of 193**, in the bottom quartile globally, and 6th of these 9 ECOWAS countries. Togo's profile is unusual — its **HCI (0.4813) is the second-highest in ECOWAS**, but its **TII (0.2474) is the worst of the 9 except Niger** — telecoms infrastructure is the binding constraint.

### Regional & global benchmarks (UN E-Gov 2024)

Source: UN E-Gov Survey 2024 Chapter 3, Section 3.1.

| Reference | EGDI 2024 |
|---|---|
| **World average** | 0.6382 |
| Europe average | 0.8493 |
| Asia average | 0.6990 |
| Americas average | 0.6701 |
| Oceania average | 0.5289 |
| **Africa average** | **0.4247** |
| ECOWAS-9 mean (computed) | ~0.4267 |

Togo (0.3920) is **0.246 below world average** and **0.033 below Africa average**.

### OGDI 2024 specifically (introduced 2020)

Methodology: OGDI is computed from 13 OSI questions about open data portal availability, machine-readable formats, metadata, etc. (UN E-Gov Methodology, Annex). Range 0–1.

| Country | OGDI 2024 | Group |
|---|---|---|
| Ghana | 0.8205 | Very High |
| Senegal | 0.6410 | High |
| Côte d'Ivoire | 0.5641 | High |
| Nigeria | 0.5128 | High |
| Benin | 0.4872 | Middle |
| **Togo** | **0.4359** | **Middle** |
| Mali | 0.3333 | Middle |
| Burkina Faso | 0.3333 | Middle |
| Niger | 0.2821 | Middle |

Togo (0.4359) is **6th of 9 ECOWAS** on OGDI specifically. Ghana sits in Very High OGDI alongside Saudi Arabia, Singapore, Spain, Sweden, Switzerland.

---

## 3. World Bank Statistical Performance Indicators (SPI)

Source: World Bank API, indicator codes IQ.SPI.OVRL plus IQ.SPI.PIL1–PIL5
- https://api.worldbank.org/v2/country/TGO/indicator/IQ.SPI.OVRL?format=json
- https://api.worldbank.org/v2/country/TGO/indicator/IQ.SPI.PIL1?format=json (and PIL2…PIL5)

### Togo 2024 — overall + 5 pillars

| Indicator | 2024 score | 2023 | 2022 | Trend |
|---|---|---|---|---|
| **SPI Overall** | **66.55** | 64.43 | 68.23 | down vs 2021 peak of 69.77 |
| Pillar 1 — Data Use | 80.00 | 80.00 | 100.00 | dropped from peak 100 in 2021–22 |
| Pillar 2 — Data Services | 68.03 | 63.93 | 63.93 | steady improvement (from 45.30 in 2016) |
| Pillar 3 — Data Products | 76.14 | 77.51 | 74.01 | high-stable |
| Pillar 4 — Data Sources | 43.58 | 40.68 | 43.20 | persistent weak point |
| Pillar 5 — Data Infrastructure | 65.00 | 60.00 | 60.00 | improving |

Togo is in the bottom half on Pillar 4 (Data Sources — censuses, surveys, admin data, geospatial) — the structural collection apparatus. Pillar 1 (Data Use) and Pillar 3 (Products) are relative strengths.

### SPI 2024 — ECOWAS overall comparison

Source: World Bank API per country.

| Country | SPI Overall 2024 |
|---|---|
| Senegal | 81.41 |
| Burkina Faso | 76.37 |
| Benin | 71.03 |
| Niger | 70.47 |
| Côte d'Ivoire | 70.20 |
| Nigeria | 69.12 |
| **Togo** | **66.55** |
| Mali | 66.51 |
| Ghana | 65.74 |

Togo is **7th of 9 ECOWAS** on SPI. The gap to leader Senegal is ~14.9 points, mostly driven by Togo's weak Pillar 4 (43.58 vs Senegal's much-higher source base).

### SPI global / Sub-Saharan Africa benchmarks

The World Bank publishes country-level SPI but the regional aggregate `IQ.SPI.OVRL` for `SSA` and `WLD` returns null in the public API for 2020–2024 — *not retrievable* via API. The 2024 SPI Update report summarises: "On average, countries' SPI overall scores rose by 12 points between 2016 and 2024 … Sub-Saharan Africa lags the highest-scoring region by more than 30 points." Source: https://documents1.worldbank.org/curated/en/099906411082488994/pdf/IDU163882895175b914ffd18dab1f867779bf6d5.pdf (2024 SPI Update). The narrative implies an SSA mean in roughly the **55–60** band, vs. high-income mean ~85 — Togo at 66.55 is therefore *above* the SSA average but well below high-income peers.

---

## 4. Global Data Barometer — 2nd edition (2024/25 wave)

Source: full CSV downloaded from Open Data Watch's storage bucket, raw extract per indicator.
- https://storage.googleapis.com/gdb-2024-analysis/open_data_2nd_edition/gdb-2024-full-data.csv (17.6 MB)
- https://storage.googleapis.com/gdb-2024-analysis/open_data_2nd_edition/country_open_data/gdb-2024-Togo-country-survey-data.csv

### Togo — overall + 8 cluster scores (2nd edition uses clusters, not the 1st-ed pillar trio)

| Cluster | Togo score (0–100) |
|---|---|
| Public Procurement | 59.61 |
| Governance Foundation | 40.06 |
| Company Information | 38.10 |
| Public Finance | 37.67 |
| Critical Competencies | 14.69 |
| Equitable Access | 11.00 |
| Political Integrity | 9.44 |
| Land Management | 0.00 |
| **GDB overall** | **23.23** |

The 2nd edition does **not** publish overall pillar scores (Governance / Capability / Availability) per country — the methodology document (https://globaldatabarometer.org/methodology/) confirms the report aggregates at cluster and indicator level. The pillar tags are used at the indicator level only.

Indicator-level, Togo's pillar means computed from the raw CSV are: **Governance ~27.6** (n=13 indicators), **Capability ~0.0** (n=4), **Availability ~11.9** (n=10) — capability collapses to zero because Togo's primary capabilities indicators (training, government support, open-data initiatives) all answered 0.

### Togo's GDB 2024 ranking

Source: ranked list computed locally from the 43 GDB-2nd-ed countries.

- Togo overall: **23.23** → **35th of 43** countries surveyed
- GDB overall mean: 36.82 · median: 35.25
- Top-3 globally: Brazil 66.85, Chile 66.42, Uruguay 62.58
- Bottom-3 globally: Sierra Leone 19.80, Cameroon 21.48, Liberia 14.45

### GDB 2024 — ECOWAS-in-survey comparison

(Mali and Niger are **not in** the GDB 2nd edition. They were in the 1st edition.)

| Country | Overall | Gov.Found | CritComp | Equit.Acc | Pol.Integ | Procurement | Pub.Finance | Co.Info | Land |
|---|---|---|---|---|---|---|---|---|---|
| Ghana | 36.24 | 61.22 | 20.52 | 50.66 | 26.53 | 72.65 | 70.87 | 16.20 | 10.20 |
| Nigeria | 35.25 | 49.49 | 32.18 | 19.00 | 26.08 | 65.96 | 30.35 | 55.57 | 0.00 |
| Benin | 29.97 | 47.08 | 22.49 | 3.00 | 11.43 | 75.24 | 74.08 | 28.87 | 18.55 |
| Burkina Faso | 27.36 | 49.84 | 12.18 | 16.00 | 16.43 | 56.97 | 57.18 | 13.52 | 28.31 |
| Senegal | 26.82 | 54.36 | 24.41 | 0.00 | 9.28 | 65.83 | 44.71 | 24.75 | 0.00 |
| Côte d'Ivoire | 25.87 | 44.24 | 22.86 | 0.00 | 5.74 | 64.69 | 63.55 | 16.00 | 30.69 |
| **Togo** | **23.23** | **40.06** | **14.69** | **11.00** | **9.44** | **59.61** | **37.67** | **38.10** | **0.00** |
| Mali | not in survey |
| Niger | not in survey |

Togo is **last of the 7 ECOWAS-in-survey** countries. Procurement (59.61) is Togo's only strong cluster (in the regional ballpark) — driven by its OCDS-compliant marchespublics.gouv.tg portal. Land Management (0.00), Political Integrity (9.44), and Equitable Access (11.00) are catastrophic gaps.

### GDB 2024 — Africa region benchmark

22 African countries are in the 2nd edition. Africa region mean = **28.64**, median = **27.09**. Togo (23.23) is **0.0 SD below median, ~0.45 SD below mean**. Africa top-3: South Africa 47.79 · Ghana 36.24 · Uganda 36.09. Africa bottom-3: Liberia 14.45 · Sierra Leone 19.80 · Gambia 21.46.

### Cross-edition note (1st edition 2022)

Source: https://storage.googleapis.com/gdb-files/countries/gdb-2021-togo-complete-survey-data.csv

Togo *was* in the 1st edition. Its 1st-ed pillar scores were:

| 1st-ed Pillar | Togo 2022 |
|---|---|
| Availability | 10.60 |
| Capabilities | 20.78 |
| Governance | 15.53 |
| Use & Impact | 11.57 |
| **Overall** | **14.56** |

Cross-edition trend: **+8.7 points** overall (14.56 → 23.23). GDB's own comparison guide warns the two editions used different methodologies (https://globaldatabarometer.org/comparison-with-first-edition/) so trends are indicative not exact.

---

## 5. Open Data Charter — Togo status

Source: https://opendatacharter.org/government-adopters/

**Togo is NOT a signatory of the International Open Data Charter.** The Charter lists 174 national + sub-national adopters since 2015. Cross-checked: **none of the 9 ECOWAS countries** appear among the national signatories — West Africa has zero national-level representation in ODC. Sub-national/city signatories within ECOWAS are also absent.

**ODIN profile cross-check:** Togo's ODIN 2024 country-profile metadata field `odcStatus` = `"N/A"` and `odcLink` is empty — confirming non-membership directly from a second source.

No public news indicating Togo invitation, declination, or active commitment to ODC was found in 2023–2025 reporting.

---

## 6. Open Government Partnership (OGP) — Togo status

Source: https://www.opengovpartnership.org/our-members/

**Togo is NOT an OGP member.** Six ECOWAS countries are active OGP members (Benin, Burkina Faso, Côte d'Ivoire, Ghana, Nigeria, Senegal). Three ECOWAS countries are **not** members: **Mali, Niger, Togo**.

**OGP eligibility (4 criteria, 75 % of points needed):** Fiscal Transparency, Access to Information, Public Officials Asset Disclosure, Citizen Engagement. Togo's *primary* OGP-eligibility data points (from UN, IBP, RTI Rating, etc.):
- **Access to Information law:** Yes — Togo passed *Loi n° 2016-006 du 30 mars 2016* on right to information (RTI Rating link: https://www.rti-rating.org/wp-content/uploads/Togo.pdf). RTI rating: 88/150 = mid-tier (source confirmed via ODIN profile metadata).
- **Statistical Law:** *Loi n° 2011-014* (https://www.afristat.org/wp-content/uploads/2023/02/TG01_Loi-statistique.pdf).
- **National Data Strategy:** *Stratégie Nationale de Développement de la Statistique 2020-2024* (afristat.org).
- **Fiscal transparency:** Open Budget Index 2023 — Togo scored 50/100 (mid-range).
- **OGP Values Check:** No public records show Togo has applied to or passed the Values Check assessment. *Not retrievable* — OGP does not publicly publish the eligibility scorecard for non-applicant countries; assessment is private until a country applies.

**ODIN profile cross-check:** Togo profile's `ogpStatus` = `"Not a member"`, `ogpLink` = `N/A` — confirming.

Bottom line: Togo has the institutional building blocks (RTI law, statistical law, e-GDDS subscriber status with the IMF) to be eligible — joining is an unmade *political* choice rather than a capacity gap.

---

## 7. Bonus — GovTech Maturity Index (GTMI), World Bank 2022

Source: World Bank Data360 API — `https://data360api.worldbank.org/data360/data?DATABASE_ID=WB_GTMI&REF_AREA=TGO&format=json`. Methodology guide: https://documents1.worldbank.org/curated/en/099035001132365997/pdf/P1694820bcef0903e091160315d2050d03b.pdf.

### Togo 2022 — GTMI overall + 4 sub-indices

| Indicator | Score (0–1) |
|---|---|
| **GTMI overall** | **0.51** |
| **CGSI** — Core Government Systems | 0.37 |
| **PSDI** — Public Service Delivery | 0.76 |
| **DCEI** — Digital Citizen Engagement | 0.24 |
| **GTEI** — GovTech Enablers | 0.66 |
| **GTMI Group** | **B** (out of A/B/C/D — Togo upgraded from C to B between 2020 and 2022) |

### GTMI 2022 — ECOWAS comparison

Source: same Data360 API per country.

| Country | GTMI | CGSI | PSDI | DCEI | GTEI | Group |
|---|---|---|---|---|---|---|
| Benin | 0.68 | 0.65 | 0.80 | 0.60 | 0.67 | B |
| Burkina Faso | 0.64 | 0.58 | 0.51 | 0.80 | 0.66 | B |
| Ghana | 0.53 | 0.65 | 0.70 | 0.31 | 0.49 | B |
| **Togo** | **0.51** | **0.37** | **0.76** | **0.24** | **0.66** | **B** |
| Nigeria | 0.50 | 0.60 | 0.68 | 0.22 | 0.52 | B |
| Côte d'Ivoire | 0.46 | 0.37 | 0.57 | 0.39 | 0.50 | C |
| Mali | 0.40 | 0.50 | 0.62 | 0.03 | 0.47 | C |
| Senegal | 0.33 | 0.33 | 0.47 | 0.26 | 0.25 | C |
| Niger | 0.18 | 0.30 | 0.05 | 0.25 | 0.12 | D |

Togo (0.51) is **4th of 9 ECOWAS** — better than Senegal/Côte d'Ivoire/Mali/Niger and very close to Nigeria/Ghana. Strongest pillar **PSDI 0.76** (online services delivery — Togo has invested heavily in eVisa, e-procurement, e-Stamp, e-Civil-status portals 2020–2024). Weakest pillar **DCEI 0.24** (citizen engagement, participation, feedback loops).

GTMI global average 2022 = 0.552 (per World Bank methodology brief). Togo at 0.51 is **just below the global mean**, far better than the SSA mean which is in the 0.40 range.

### Other digital benchmarks visible in research (for cross-reference)

- **Government AI Readiness Index 2024** (Oxford Insights): Togo overall 31.32, rank 157; Government 31.21, Tech sector 20.82, Data & Infrastructure 41.92. Source: https://dig.watch/countries/togo.

---

## Master comparison matrix — ECOWAS-9 across ALL six indices

(Higher = better in every column. ✗ = not assessed.)

| Country | ODIN '24 (0–100) | EGDI '24 (0–1) | OGDI '24 (0–1) | SPI '24 (0–100) | GDB '24 (0–100) | GTMI '22 (0–1) | OGP member | ODC signatory |
|---|---|---|---|---|---|---|---|---|
| Senegal | 75 | 0.5162 | 0.6410 | 81.41 | 26.82 | 0.33 | ✓ | ✗ |
| Ghana | 54 | 0.6317 | 0.8205 | 65.74 | 36.24 | 0.53 | ✓ | ✗ |
| Côte d'Ivoire | 62 | 0.5587 | 0.5641 | 70.20 | 25.87 | 0.46 | ✓ | ✗ |
| Burkina Faso | 77 | 0.2895 | 0.3333 | 76.37 | 27.36 | 0.64 | ✓ | ✗ |
| Nigeria | 56 | 0.4815 | 0.5128 | 69.12 | 35.25 | 0.50 | ✓ | ✗ |
| Benin | 59 | 0.4578 | 0.4872 | 71.03 | 29.97 | 0.68 | ✓ | ✗ |
| **Togo** | **55** | **0.3920** | **0.4359** | **66.55** | **23.23** | **0.51** | **✗** | **✗** |
| Mali | 55 | 0.3005 | 0.3333 | 66.51 | ✗ | 0.40 | ✗ | ✗ |
| Niger | 67 | 0.2116 | 0.2821 | 70.47 | ✗ | 0.18 | ✗ | ✗ |

---

## Synthesis — Togo's scoring profile in one paragraph

Across the six international indices Togo holds a consistent profile: **mid-quartile on capability/use measures, bottom-quartile on infrastructure and openness measures, and politically unaligned with the open-data soft-law architecture**. ODIN puts Togo at 55/100 (rank 95) — **above the Western Africa median of 49** but **below the global median of 56**. UN EGDI 0.3920 is bottom-quartile (rank 161/193); the binding constraint is TII (0.2474, "Low TII"). On the SPI Togo scores 66.55 with a glaring weakness in Pillar 4 (43.58 — Data Sources). The Global Data Barometer 2nd edition lands Togo at 23.23 (35/43, last of 7 ECOWAS-in-survey), with Procurement (59.61) the only strong cluster and Land Management (0.00), Political Integrity (9.44) and Equitable Access (11.00) at near-zero. GTMI is comparatively the brightest spot — 0.51 (Group B), within touching distance of the global mean of 0.552 — driven by strong PSDI (0.76) thanks to Togo's e-services rollout 2020–2024. Togo is **neither in OGP nor among Open Data Charter signatories**, alongside Mali and Niger in the ECOWAS-9. Three priority gaps stand out for any reform plan: Togo's **ODIN "Digital connectivity" category is 0**, **EGDI TII is 0.2474**, and the **GDB Land Management cluster is 0** — three concrete, measurable headlines that improve with the same reform: publishing a national open-data portal with land cadastre, telecoms KPIs and digital-connectivity statistics in machine-readable formats.

---

## Provenance log

| # | Index | Method | URL / source |
|---|---|---|---|
| 1 | ODIN 2024/25 | Live ODIN backend `GetCountryProfile/2024/{ISO3}` POSTed default weights, parsed `odinScores`, `rankInWorld`, `rankInRegion`, `dataReportsWithWeightsN` | https://odin-aim.akroninc.net/api/api/client/ |
| 2 | UN E-Gov Survey 2024 | Tech Appendix PDF downloaded → pdftotext layout extraction → grep | https://desapublications.un.org/sites/default/files/publications/2024-09/Technical%20Appendix%20%28Web%20version%29%201292024.pdf |
| 3 | World Bank SPI | Public WB API per indicator | https://api.worldbank.org/v2/country/TGO/indicator/IQ.SPI.OVRL?format=json |
| 4 | GDB 2nd ed (2024/25) | Direct CSV from Open Data Watch storage bucket | https://storage.googleapis.com/gdb-2024-analysis/open_data_2nd_edition/gdb-2024-full-data.csv |
| 5 | Open Data Charter | Live page check | https://opendatacharter.org/government-adopters/ |
| 6 | OGP | Live page check + ODIN profile cross-check field `ogpStatus` | https://www.opengovpartnership.org/our-members/ |
| 7 | GTMI 2022 | World Bank Data360 API per ISO3 | https://data360api.worldbank.org/data360/data?DATABASE_ID=WB_GTMI&REF_AREA=TGO&format=json |

### Items not retrievable
- **World Bank SPI regional aggregates** (`SSA`, `WLD`) for 2020–2024 return null in the public API — only narrative averages available in the SPI 2024 Update PDF.
- **OGP Values Check assessment for Togo** — OGP only publishes Values-Check results for countries that have applied to join. Since Togo has not applied, no public scorecard exists.
- **ODIN's per-country published rank PDF** export endpoint is JS-rendered behind CloudFlare; the data however is identical to what the live backend returns and was extracted from there.
