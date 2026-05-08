# Togo Open Data Audit / Audit de l'open data togolais

> **Status — May 2026.** Independent, constructive audit of Togo's official open data infrastructure: [opendata.gouv.tg](https://opendata.gouv.tg/fr/) and [geodata.gouv.tg](https://geodata.gouv.tg/), benchmarked against international standards (Open Data Charter, DCAT-AP, FAIR, 5★ Linked Open Data) and against peer portals across ECOWAS, France, the UK, and Kenya.
>
> **Statut — mai 2026.** Audit indépendant et constructif de l'infrastructure open data officielle du Togo : [opendata.gouv.tg](https://opendata.gouv.tg/fr/) et [geodata.gouv.tg](https://geodata.gouv.tg/), comparée aux standards internationaux (Open Data Charter, DCAT-AP, FAIR, 5★ Linked Open Data) et aux portails pairs en CEDEAO, France, Royaume-Uni et Kenya.

---

## 🇫🇷 En français

### Le constat en une ligne

Le Togo dispose du même logiciel que data.gouv.fr (74 000 datasets) mais publie 1 550 datasets dont 99,7 % n'ont pas été modifiés depuis janvier 2025, le portail enregistre 0 vue / 0 téléchargement / 0 réutilisation, et le géoportail expose un seul jeu cartographique avec les métadonnées par défaut de GeoServer (contact : « Claudius Ptolomaeus, Empire romain »).

### Livrables

- 📊 [`reports/report-fr.md`](reports/report-fr.md) — Rapport complet (FR)
- 📊 [`reports/report-en.md`](reports/report-en.md) — Full report (EN)
- 📁 [`data/raw/`](data/raw/) — Métadonnées brutes des 1 550 datasets
- 📁 [`data/processed/`](data/processed/) — Analyses dérivées (JSON, Markdown)
- 🛠️ [`scripts/`](scripts/) — Scripts Python reproductibles

### Reproduire l'audit

```bash
git clone https://github.com/gausoft/togo-opendata-audit.git
cd togo-opendata-audit
python3 scripts/01_fetch_metadata.py     # Pull all dataset metadata
python3 scripts/02_analyze_metadata.py   # Compute aggregate stats
python3 scripts/03_content_audit.py      # Sample resources, classify
```

---

## 🇬🇧 In English

### The headline

Togo runs the same software as France's data.gouv.fr (74,000 datasets), publishes 1,550 of which 99.7% haven't been modified since January 2025, the portal records 0 views / 0 downloads / 0 reuses, and the geoportal exposes a single cartographic layer with GeoServer's default placeholder metadata (contact: "Claudius Ptolomaeus, Roman Empire").

### Deliverables

- 📊 [`reports/report-en.md`](reports/report-en.md) — Full report (EN)
- 📊 [`reports/report-fr.md`](reports/report-fr.md) — Rapport complet (FR)
- 📁 [`data/raw/`](data/raw/) — Raw metadata for all 1,550 datasets
- 📁 [`data/processed/`](data/processed/) — Derived analyses (JSON, Markdown)
- 🛠️ [`scripts/`](scripts/) — Reproducible Python scripts

---

## License

- **Scripts** (`scripts/`): MIT
- **Report and analyses** (`reports/`, `data/processed/`): CC-BY 4.0
- **Raw metadata** (`data/raw/`): same licence as the source portal (CC-BY 4.0 declared on opendata.gouv.tg for the majority of datasets)

## Acknowledgements

Compiled by [@gausoft](https://github.com/gausoft) — independent author based in Lomé, Togo. The intent of this audit is **constructive**: every finding is paired with a benchmark and a recommendation. Government engagement is welcomed via [GitHub issues](https://github.com/gausoft/togo-opendata-audit/issues).
