# LinkedIn — version française

---

J'ai passé 12 heures à auditer les portails open data du Togo. Voici les chiffres qui m'ont fait basculer.

🇹🇬 opendata.gouv.tg + geodata.gouv.tg — 1 550 datasets affichés, audités à 100 %, comparés à 10 portails pairs (France, UK, Kenya, Ghana, Côte d'Ivoire, Sénégal, Rwanda, Burkina, Nigeria, Bénin).

**5 chiffres pour situer.**

→ 99,7 % des datasets n'ont pas été modifiés depuis janvier 2025
→ 0 vue, 0 téléchargement, 0 réutilisation enregistrée par le portail (selon ses propres compteurs)
→ Le Ministère des Armées et celui de la Sécurité publient à 100 % des fichiers vides — uniquement le dictionnaire des colonnes, sans aucune ligne de données
→ Le géoportail expose 1 seul layer cartographique en standard ouvert. Sa fiche de contact officielle est restée sur les valeurs par défaut de GeoServer : « Claudius Ptolomaeus, Empire romain »
→ Le Togo est le seul des 11 portails comparés à n'être ni signataire de l'Open Data Charter, ni membre de l'Open Government Partnership

**Et pourtant — les outils sont là.**

opendata.gouv.tg tourne sur **udata**, le même logiciel libre que data.gouv.fr. Même code source, même fonctionnalités natives. La différence : data.gouv.fr publie 74 000 datasets et les rafraîchit chaque jour. Le Togo en publie 1 550 et n'a rien touché depuis 16 mois.

Le constat n'est pas technique. **Il est organisationnel.**

**Ce qui marche déjà.**

L'INSEED, le Ministère de l'Agriculture, celui des Travaux Publics : 99-100 % de datasets avec des données réelles, propres, exploitables. La compétence existe. Le problème, c'est qu'elle n'est ni outillée ni standardisée à l'échelle du portail.

**Ce qui manquerait pour transformer la situation en un trimestre.**

10 recommandations dans le rapport. Les trois plus rapides :

1. Activer le flux DCAT-AP natif d'udata (5 lignes de config) → portail moissonnable par data.europa.eu instantanément
2. Activer l'endpoint `/site/quality` natif → tableau de bord public de la qualité par administration
3. Reconfigurer la fiche du GeoServer (10 minutes) — au minimum, retirer Claudius Ptolomaeus

Tout ça gratuit. Tout ça déjà dans le code en production.

**Pourquoi je publie ça.**

Parce que le Togo a investi dans une infrastructure qu'il n'utilise pas. Parce que 102 datasets vides circulent depuis 16 mois sans que personne ne lève la main. Parce que la donnée publique a une valeur économique réelle, et qu'à force de la publier mal on conclut, à tort, qu'elle n'intéresse personne.

📊 Rapport complet (FR + EN, 35 pages) + scripts reproductibles + données brutes :
🔗 github.com/gausoft/togo-opendata-audit

L'intention est constructive. Toute correction factuelle d'une administration est bienvenue et sera intégrée en v1.1.

#OpenData #GovTech #Togo #AfriqueDeLOuest #DataGov #FAIR #OpenGovernment
