# X thread — version française

---

**1/12**
Le Togo a un portail open data. Il tourne sur le même logiciel libre que data.gouv.fr.

J'ai audité ses 1 550 datasets et les chiffres sont… inattendus.

Thread 🧵🇹🇬

---

**2/12**
Premier chiffre :

99,7 % des datasets n'ont pas été modifiés depuis janvier 2025.

Le portail n'est pas un flux — c'est un instantané qui date.

---

**3/12**
Deuxième chiffre :

0 vue, 0 téléchargement, 0 réutilisation enregistrée par le portail. Sur 1 550 datasets.

(Selon ses propres compteurs accessibles à `/api/1/site/`.)

---

**4/12**
Troisième chiffre, le plus dérangeant :

Le Ministère des Armées (18 datasets) et celui de la Sécurité (7 datasets) publient à 100 % des fichiers VIDES.

Uniquement le dictionnaire des colonnes. 0 ligne de donnée.

---

**5/12**
Le Ministère de l'Économie Numérique — celui dont l'open data est censé être le métier — atteint 87 % de fichiers vides.

Les Transports : 49 %.
L'Enseignement Supérieur : 71 %.

---

**6/12**
À l'inverse :

L'INSEED, le Ministère de l'Agriculture, celui des Travaux Publics : 99–100 % de datasets avec des données réelles, exploitables.

La compétence existe. Elle n'est juste pas outillée à l'échelle du portail.

---

**7/12**
Côté géoportail (geodata.gouv.tg) — la trouvaille m'a fait sourire :

Le service WMS public expose 1 seul layer.

Et la fiche de contact officielle est restée sur les valeurs par défaut de GeoServer :
« Claudius Ptolomaeus, Empire romain, Alexandria » 🤦

(Capture dans le rapport.)

---

**8/12**
Comparaison régionale :

🇫🇷 France: 74 000 datasets, MAJ quotidienne — même logiciel
🇬🇧 UK: ~30 000
🇬🇭 Ghana: 271
🇨🇮 Côte d'Ivoire: 177
🇹🇬 Togo: 1 550, gelé depuis 16 mois

Le Togo n'est pas en retard volume. Il est en retard gouvernance.

---

**9/12**
Sur 11 portails comparés, le Togo est le SEUL :

❌ Pas signataire de l'Open Data Charter
❌ Pas membre de l'Open Government Partnership

Tous les pays voisins (Bénin, Burkina, CI, Ghana, Sénégal, Nigeria) sont à l'OGP.

---

**10/12**
Le constat n'est pas technique. **Il est organisationnel.**

Les fonctions qui rendraient le portail crédible (DCAT-AP, /site/quality, harvesting) sont DÉJÀ DANS LE CODE.

Elles ne sont pas activées.

---

**11/12**
Le rapport propose 10 recommandations classées par effort.

Les 3 plus rapides (jours) :
1. Activer DCAT-AP — 5 lignes
2. Activer /site/quality — paramètre
3. Reconfigurer le GeoServer — 10 min

Coût total : 0 FCFA.

---

**12/12**
Rapport complet (FR + EN, 35 pages, 102 datasets vides identifiés un par un) + scripts Python reproductibles + données brutes :

🔗 github.com/gausoft/togo-opendata-audit

Toute correction factuelle d'une administration sera intégrée en v1.1.
