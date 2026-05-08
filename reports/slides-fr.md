---
marp: true
theme: slate
paginate: true
title: Audit indépendant de l'open data togolais
author: Gauthier Eholoum
date: Mai 2026
---

# Audit indépendant
# de l'open data togolais

**Diagnostic chiffré et benchmark international**

Mai 2026 — Gauthier Eholoum, Lomé

[github.com/gausoft/togo-opendata-audit](https://github.com/gausoft/togo-opendata-audit)

---

## Le portail togolais en deux portails

**opendata.gouv.tg** — propulsé par *udata*, même logiciel libre que data.gouv.fr 🇫🇷

**geodata.gouv.tg** — géoportail React + GeoServer institutionnel

Les outils sont là. Les standards aussi (Open Data Charter, DCAT-AP, FAIR, 5★).

---

## La méthodologie en 30 secondes

- **100 % des 1 550 datasets** de opendata.gouv.tg téléchargés et classifiés
- **8 endpoints OGC** sondés sur le géoportail
- **10 portails pairs** comparés (France, UK, Kenya, Ghana, CI, Sénégal, Rwanda, Burkina, Nigeria, Bénin)
- Tout le code reproductible : [`github.com/gausoft/togo-opendata-audit`](https://github.com/gausoft/togo-opendata-audit)

---

## Cinq chiffres pour situer le diagnostic

# 99,7 %

**des datasets n'ont pas été modifiés depuis janvier 2025**

Le portail est un instantané gelé, pas un flux vivant.

---

## Cinq chiffres (suite)

# 0 / 0 / 0 / 0

**vue, téléchargement, réutilisation, discussion** — sur 1 550 datasets

Selon les compteurs renvoyés par `/api/1/site/`. **13** comptes utilisateurs au total.

---

## Cinq chiffres (suite)

# 100 %

**des datasets du Ministère des Armées et de la Sécurité sont des fichiers vides**

Uniquement le dictionnaire des colonnes. 0 ligne de donnée. (18 + 7 datasets concernés)

---

## Cinq chiffres (suite)

# 1

**seul layer cartographique** exposé par le géoportail en standard ouvert WMS

Workspace : `prise_freely_available`. Contact officiel : *« Claudius Ptolomaeus, Empire romain »* (placeholder GeoServer).

---

## Cinq chiffres (fin)

# Seul

**portail des 11 comparés** à n'être ni signataire de l'Open Data Charter, ni membre de l'Open Government Partnership

Tous les voisins (Bénin, Burkina, CI, Ghana, Sénégal, Nigeria) sont à l'OGP.

---

## D'où viennent vraiment les données

| Producteur | Datasets | Part |
|------------|---------:|-----:|
| Banque Mondiale (re-publication) | 733 | **47 %** |
| INSEED | 479 | **31 %** |
| Tous les ministères togolais combinés | 287 | **18 %** |
| Autres (HDX, OCDE, particuliers) | 51 | 3 % |

**78 % du portail est de la re-publication d'indicateurs déjà accessibles ailleurs.**

---

## Les ministères qui publient des fichiers vides

| Ministère | Datasets | % schema-only |
|-----------|---------:|--------------:|
| Armées | 18 | **100 %** |
| Sécurité & Protection Civile | 7 | **100 %** |
| Économie Numérique | 23 | **87 %** |
| Enseignement Supérieur | 7 | 71 % |
| Commerce et Artisanat | 16 | 56 % |
| Transports | 43 | 49 % |

---

## Les ministères qui publient propre

| Ministère | Datasets | % vraies données |
|-----------|---------:|----------------:|
| Agriculture | 26 | **100 %** |
| Travaux Publics | 5 | **100 %** |
| Planification du Développement | 5 | **100 %** |
| Action Sociale | 13 | 92 % |
| Économie et Finances | 10 | 90 % |
| INSEED (référence) | 479 | **99,6 %** |

**La compétence existe. Elle n'est juste pas standardisée.**

---

## Le géoportail — la trouvaille du jour

**Capabilities WMS officielles, copie verbatim :**

```xml
<ContactPerson>Claudius Ptolomaeus</ContactPerson>
<ContactOrganization>OSGeo</ContactOrganization>
<City>Alexandria</City>
<Country>Roman Empire</Country>
<Email>claudius.ptolomaeus@mercury.olympus.gov</Email>
```

C'est le placeholder par défaut de GeoServer. **Jamais reconfiguré.**

---

## Comparaison régionale

| Pays | Datasets | OGP | ODC |
|------|---------:|----|----|
| 🇫🇷 France (udata, **même logiciel**) | 74 000 | ✅ | ✅ |
| 🇬🇧 UK (CKAN) | ~30 000 | ✅ | ✅ |
| 🇹🇬 Togo (udata) | **1 550** | ❌ | ❌ |
| 🇧🇫 Burkina Faso | 200+ | ✅ | ❌ |
| 🇬🇭 Ghana | 271 | ✅ | ❌ |
| 🇨🇮 Côte d'Ivoire | 177 | ✅ | ❌ |

---

## Le constat

**Le gap n'est pas technique. Il est organisationnel.**

- Les fonctions DCAT-AP, /site/quality, harvesting **sont déjà dans le code en production**
- L'INSEED prouve que la publication propre est possible au Togo
- Le portail a été produit (livraison de projet) mais pas mis en service (cycle d'exploitation)

---

## 10 recommandations

**Quick wins (jours, coût 0 FCFA) :**

1. Activer DCAT-AP natif (5 lignes de config) → fédération data.europa.eu
2. Activer `/site/quality` → tableau de bord public qualité
3. Reconfigurer fiche GeoServer → 10 minutes

---

## 10 recommandations (suite)

**Court terme (semaines) :**

4. Republier les 102 datasets schema-only identifiés
5. Documenter publiquement l'API du géoportail
6. Ouvrir le service WFS en lecture anonyme

---

## 10 recommandations (suite)

**Moyen terme (trimestre) :**

7. Politique de fraîcheur par thème
8. Validation CI pré-publication (Frictionless)
9. Activer les métriques utilisateurs

**Structurant (année) :**

10. Adhésion OGP + signature Open Data Charter

---

## En résumé

Le Togo a **investi dans une infrastructure qu'il n'utilise pas.**

L'écart se rattrape :

- ⚙️ **dix paramètres de configuration** activés
- 📂 **cent datasets** corrigés
- ✍️ **deux engagements internationaux** signés

→ en un trimestre, position transformée dans les classements internationaux **et** valeur effective de la donnée publique togolaise.

---

## Le rapport complet

📊 **Rapport bilingue FR + EN** (35 pages)
📦 **Scripts Python reproductibles** (MIT)
📁 **Données brutes** des 1 550 fiches (CC-BY 4.0)
🔄 **Méthodologie** vérifiable en 15 minutes par toute personne disposant de Python 3

🔗 **github.com/gausoft/togo-opendata-audit**

---

## Contact

**Gauthier Eholoum** — Lomé, Togo

✉️ gauthier.eholoum@gmail.com
🐙 [github.com/gausoft](https://github.com/gausoft)

*Toute correction factuelle d'une administration sera intégrée en v1.1 du rapport.*

**L'intention est explicitement constructive.**
