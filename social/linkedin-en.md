# LinkedIn — English version

---

I spent 12 hours auditing Togo's open data portals. Here are the numbers that flipped my view.

🇹🇬 opendata.gouv.tg + geodata.gouv.tg — 1,550 datasets advertised, audited at 100%, compared to 10 peer portals (France, UK, Kenya, Ghana, Côte d'Ivoire, Senegal, Rwanda, Burkina Faso, Nigeria, Benin).

**Five numbers to anchor it.**

→ 99.7% of datasets have not been modified since January 2025
→ 0 views, 0 downloads, 0 reuses recorded by the portal itself (per its own counters)
→ The Ministry of Defence and the Ministry of Security publish 100% empty files — only the column dictionary, no data rows
→ The geoportal exposes 1 single cartographic layer through open standards. Its official contact card is still GeoServer's factory placeholder: "Claudius Ptolomaeus, Roman Empire"
→ Of 11 portals compared, Togo is the only one in neither the Open Data Charter nor the Open Government Partnership

**Yet — the tools are there.**

opendata.gouv.tg runs on **udata**, the same open-source software as France's data.gouv.fr. Same codebase, same native features. The difference: data.gouv.fr publishes 74,000 datasets and refreshes them daily. Togo has 1,550 and hasn't touched them in 16 months.

The gap is not technical. **It is organisational.**

**What works.**

INSEED (Togo's national statistics institute), the Ministry of Agriculture, the Ministry of Public Works — 99–100% of their datasets contain real, clean, usable data. The skill exists. It just isn't tooled or standardised across the portal.

**What it would take to transform the picture in one quarter.**

10 recommendations in the report. The three quickest:

1. Activate udata's native DCAT-AP feed (5 lines of config) → instantly harvestable by data.europa.eu
2. Activate the native `/site/quality` endpoint → public per-organisation quality dashboard
3. Reconfigure the GeoServer profile (10 minutes) — at minimum, remove Claudius Ptolomaeus

All free. All already in the production code.

**Why publish this.**

Because Togo invested in an infrastructure it doesn't use. Because 102 empty datasets have been live for 16 months and nobody has raised a hand. Because public data has real economic value, and publishing it badly leads to the wrong conclusion that it interests no one.

📊 Full report (FR + EN, 35 pages) + reproducible scripts + raw data:
🔗 github.com/gausoft/togo-opendata-audit

Intent is constructive. Any factual correction from an agency is welcome and will be integrated into v1.1.

#OpenData #GovTech #Togo #WestAfrica #DataGov #FAIR #OpenGovernment
