# X thread — English version

---

**1/12**
Togo has an open data portal. It runs on the same open-source software as France's data.gouv.fr.

I audited its 1,550 datasets. The numbers are… unexpected.

Thread 🧵🇹🇬

---

**2/12**
Number 1:

99.7% of datasets haven't been modified since January 2025.

The portal isn't a stream — it's a dated snapshot.

---

**3/12**
Number 2:

0 views, 0 downloads, 0 reuses recorded by the portal. Across 1,550 datasets.

(Per its own counters, available at `/api/1/site/`.)

---

**4/12**
Number 3 — the most uncomfortable:

The Ministry of Defence (18 datasets) and the Ministry of Security (7 datasets) publish 100% EMPTY files.

Only the column dictionary. 0 data rows.

---

**5/12**
The Ministry of Digital Economy — for which open data should be core business — hits 87% empty files.

Transport: 49%.
Higher Education: 71%.

---

**6/12**
By contrast:

INSEED (national statistics), the Ministry of Agriculture, the Ministry of Public Works: 99–100% of datasets carry real, usable data.

The skill exists. It just isn't tooled at portal scale.

---

**7/12**
The geoportal finding made me smile:

The public WMS service exposes 1 single layer.

And the official contact card is still GeoServer's factory placeholder:
"Claudius Ptolomaeus, Roman Empire, Alexandria" 🤦

(Screenshot in the report.)

---

**8/12**
Regional comparison:

🇫🇷 France: 74,000 datasets, daily updates — same software
🇬🇧 UK: ~30,000
🇬🇭 Ghana: 271
🇨🇮 Côte d'Ivoire: 177
🇹🇬 Togo: 1,550, frozen for 16 months

Togo isn't behind on volume. It's behind on governance.

---

**9/12**
Across 11 compared portals, Togo is the ONLY one:

❌ Not an Open Data Charter signatory
❌ Not an Open Government Partnership member

Every neighbour (Benin, Burkina, CI, Ghana, Senegal, Nigeria) is in OGP.

---

**10/12**
The gap is not technical. **It's organisational.**

The features that would make the portal credible (DCAT-AP, /site/quality, harvesting) are ALREADY IN THE CODE.

They just aren't switched on.

---

**11/12**
The report proposes 10 recommendations ranked by effort.

The 3 quickest (days):
1. Activate DCAT-AP — 5 lines
2. Activate /site/quality — config flag
3. Reconfigure GeoServer — 10 minutes

Total cost: $0.

---

**12/12**
Full report (FR + EN, 35 pages, 102 empty datasets listed one by one) + reproducible Python scripts + raw data:

🔗 github.com/gausoft/togo-opendata-audit

Any factual correction from an agency will be integrated into v1.1.
