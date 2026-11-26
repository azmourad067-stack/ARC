# Étude stratégique d'innovation HealthTech — Recherche clinique

**Date :** 26 novembre 2026
**Commanditaire :** un attaché de recherche clinique (ARC) qui veut créer une entreprise
**Méthode :** 22 recherches web ciblées (publications Tufts CSDD, ICH, EMA, FDA, enquêtes ACRP/SCRS/Advarra/WCG/AACI, communication des éditeurs), puis analyse critique.

---

## 0. Comment lire ce document

Chaque affirmation porte une étiquette :

| Étiquette | Sens |
|---|---|
| **[F]** | Fait documenté par une source publiée et vérifiable (étude, texte réglementaire, enquête). |
| **[V]** | Chiffre ou affirmation d'un **éditeur ou d'un acteur intéressé**. Utile, mais non vérifié de façon indépendante. |
| **[T]** | Témoignage, panel ou retour d'expérience qualitatif. |
| **[H]** | Hypothèse de l'équipe d'experts : raisonnement de terrain, **pas une preuve**. |
| **[P]** | Projection (marché, coûts, calendrier) : un ordre de grandeur, pas une prévision. |

**Limites honnêtes de la recherche :**
- Je n'ai pas pu accéder directement aux fils Reddit ni aux discussions LinkedIn : la recherche n'a renvoyé aucun fil Reddit exploitable. **Aucun témoignage n'est donc inventé ici.** Les éléments de « terrain » viennent d'enquêtes publiées et de panels, ou sont étiquetés [H].
- Plusieurs chiffres récents ne sont repris que par des sites secondaires (par exemple IntuitionLabs). Je les signale comme tels.
- Les bases PubMed et ClinicalTrials.gov n'étaient pas joignables depuis cet environnement. Les références scientifiques ont été trouvées par recherche web générale.

---

## 1. Résumé exécutif

**Le constat central.** Le protocole est le « code source » d'un essai. Pourtant, sur le terrain, personne ne l'**exécute** : on le **lit**, on l'**interprète**, puis on le **recopie** à la main dans des modèles de source, des checklists, des calendriers Excel et des mémos. Chaque recopie et chaque amendement est une occasion d'erreur.

Les données convergent :
- En phase III, on compte en moyenne **environ 119 déviations par protocole**, qui touchent environ **un tiers des participants** [F] ([Tufts CSDD, PMC8979478](https://pmc.ncbi.nlm.nih.gov/articles/PMC8979478) ; [Applied Clinical Trials](https://www.appliedclinicaltrialsonline.com/view/quantifying-protocol-deviation-experience-by-clinical-phase)).
- **Trois protocoles sur quatre** ont au moins un amendement substantiel, avec en moyenne **3,3 amendements par protocole** (Tufts CSDD 2023, environ 2 200 amendements) [F] ([ACT](https://www.appliedclinicaltrialsonline.com/view/shining-a-light-on-the-inefficiencies-in-amendment-implementation)).
- Entre l'approbation interne d'un amendement et la dernière approbation éthique, il s'écoule **environ 260 jours**. Pendant ce temps, des centres appliquent des **versions différentes** du protocole [F] (Tufts 2023, via [ACT](https://www.appliedclinicaltrialsonline.com/view/shining-a-light-on-the-inefficiencies-in-amendment-implementation)).
- Mettre en œuvre un amendement substantiel coûte **en médiane 141 000 $ en phase II et 535 000 $ en phase III** (Tufts 2016) [F] ([DIJ/TIRS](https://journals.sagepub.com/doi/abs/10.1177/2168479016632271)).
- La SDV exhaustive (100 %) ne corrige qu'**environ 1,1 %** des données eCRF saisies par les sites [F] ([Sheetz et al., TIRS 2014](https://link.springer.com/article/10.1177/2168479014554400)). L'effort de contrôle porte donc **après coup** sur ce qui compte peu.
- L'ICH E6(R3), en vigueur dans l'UE depuis le **23 juillet 2025**, impose une approche fondée sur le risque et sur les facteurs critiques pour la qualité, **intégrés dès la conception** [F] ([EMA](https://www.ema.europa.eu/sl/ich-e6-good-clinical-practice-scientific-guideline)).

**L'angle mort.** Le marché s'attaque au protocole par deux bouts :
- **Côté promoteur** : digitalisation du protocole (ICH M11, CDISC USDM), avec Medable, Verily, IQVIA et Faro Health. Le but est de propager les changements vers l'EDC, l'IRT et le reste du système d'information.
- **Côté documentaire** : l'eISF et les agents IA documentaires, avec Florence.

Mais **personne ne calcule de façon fiable, patient par patient et visite par visite, ce qui doit se passer, selon la version du protocole applicable à CE patient, avec les contraintes réelles de CE centre, et ce qui risque de mal tourner avant que ça arrive.**

**Recommandation finale (développée en partie 13) : KAIROS, le jumeau opérationnel du patient-sujet.** C'est un moteur qui « compile » le protocole, ses amendements, les manuels (laboratoire, pharmacie, imagerie) et les clarifications du promoteur en **règles exécutables**. Il les applique à l'état réel de chaque participant pour **prévenir les déviations**, plutôt que de les constater pendant la visite de monitoring.

Le marché d'entrée, ce sont les centres et les CRO. Le fossé concurrentiel, c'est un **référentiel inter-études qui relie les déviations aux éléments du protocole qui les provoquent**. Ce référentiel se revend ensuite aux promoteurs sous forme de « score d'exécutabilité » des protocoles avant finalisation.

---

## 2. Étude de marché et de terrain : les faits

### 2.1 Complexité croissante des protocoles

- Depuis 2005, le nombre de procédures a augmenté de **139 %**, celui des critères d'évaluation de **214 %** et celui des points de données collectés de **600 %**. Ces chiffres viennent d'un article TIRS 2022 cité par IQVIA [F, de seconde main] ([IQVIA, janv. 2026](https://www.iqvia.com/blogs/2026/01/assessing-protocol-complexity-and-its-impact-on-trial-outcomes)).
- Les protocoles à forte charge pour les sites ont plus d'abandons : **22 %**, contre **19 %** pour les protocoles moins lourds. Source : Tufts CSDD Impact Report de sept./oct. 2024, cité par IQVIA [F, de seconde main].

### 2.2 Déviations au protocole

- Moyennes par protocole : **119 en phase III** et **75 en phase II**. La variabilité est forte (coefficient de variation entre 1,7 et 2,0), ce qui rend le nombre de déviations d'un protocole **difficile à prévoir par des moyennes** [F] ([PMC8979478](https://pmc.ncbi.nlm.nih.gov/articles/PMC8979478)).
- En oncologie, les déviations touchent **47 % des volontaires** [F] ([ACT](https://www.appliedclinicaltrialsonline.com/view/quantifying-protocol-deviation-experience-by-clinical-phase)).
- Une étude sur trois centres passés du papier aux modèles de source électroniques rapporte **54 % de déviations en moins** générées par l'un des centres. L'échantillon est petit [F, faible niveau de preuve] ([ACRP Clinical Researcher, avril 2023](https://acrpnet.org/2023/04/electronic-source-reduces-protocol-deviations-compared-to-paper-source-in-clinical-trials/)).
- CRIO annonce 20 % à 40 % de déviations en moins selon les pages de son site. Les chiffres ne concordent pas entre elles [V] ([CRIO](https://clinicalresearch.io/products/esource/site-esource/)).
- **Enseignement [H] :** une partie importante des déviations ne vient pas de la négligence. Elle vient de la **traduction manuelle** du protocole en outils de terrain. C'est ce que CRIO dit explicitement : chaque centre réécrit ses propres modèles et peut « coder » une déviation dans son modèle.

### 2.3 Amendements

- Fréquence : **3,3 amendements substantiels** par protocole en moyenne, et **76 %** des protocoles amendés selon une synthèse secondaire de 2026 [F/V] ([IntuitionLabs](https://intuitionlabs.ai/articles/clinical-trial-protocol-amendments-cost-data)).
- Dans l'étude Tufts 2024 portant sur des données de 2022, **77 %** des amendements sont jugés « inévitables » [F] ([Springer TIRS 2024](https://link.springer.com/content/pdf/10.1007/s43441-024-00622-9.pdf)).
- **Conséquence [H] :** on ne fera pas disparaître les amendements. Il faut **industrialiser leur absorption**.
- Enquête AACI auprès de 43 centres de cancérologie (automne 2025) : les amendements avant activation retardent **de 4 à 6 semaines** dans la plupart des cas, **≥ 10 semaines pour près de 20 %** des centres. **Plus de 40 %** des centres consacrent des ressources dédiées à la mise en œuvre des amendements [F, petit échantillon] ([AACI 2026](https://www.aaci-cancer.org/Files/Admin/2026-June-AACI-White-Paper-Accelerating-Clinical-Trial-Activation.pdf)).
- WCG (plus de 600 réponses) : ce sont surtout les **défauts de communication**, plus que la complexité réglementaire, qui retardent la mise en œuvre. Certains centres **ferment les inclusions** ou **se retirent** d'études à cause de ces retards [V/T] ([WCG, guide promoteur](https://www.wcgclinical.com/wp-content/uploads/2026/09/Sponsor-Guide-on-Protocol-Amendments-Reducing-Site-Burden_v2-1.pdf) ; [ACRP, août 2026](https://acrpnet.org/2026/08/11/navigating-protocol-amendments-understanding-the-growing-burden-and-charting-a-path-forward)).
- Panel Advarra : les centres **apprennent souvent qu'une nouvelle version existe avant d'avoir reçu le protocole annoté ou le nouveau formulaire de consentement** [T] ([Advarra](https://www.advarra.com/blog/what-protocol-amendments-reveal-about-trial-design/)).
- Re-consentement : c'est le comité d'éthique (ou l'IRB) qui décide s'il faut un re-consentement complet, une simple information ou rien. Continuer sous l'ancien consentement après un changement important constitue une déviation [F] ([CASRAI](https://casrai.org/guides/when-should-informed-consent-be-obtained)).
- **Aucune étude trouvée ne mesure le taux d'erreurs liées aux versions** (mauvaise version appliquée à un patient, re-consentement oublié). C'est un **trou de données**, qui est aussi une opportunité.

### 2.4 Monitoring et contrôle qualité

- La SDV corrige environ **1,1 %** des données (1 168 études, 53 promoteurs) [F] ([Sheetz 2014](https://link.springer.com/article/10.1177/2168479014554400)).
- TransCelerate recommande de privilégier la **revue des données sources (SDR)** et la vérification de conformité, plutôt que la recherche d'erreurs de transcription [F] ([ACT](https://www.appliedclinicaltrialsonline.com/view/distinct-rbm-divisions-source-document-verification-and-source-data-review)).
- Selon Veeva, pour 1 000 rapports de visite, les CRA passent **plus de 780 jours** dans différents systèmes [V, chiffre d'éditeur] ([Veeva](https://www.veeva.com/blog/simplify-cras-return-to-sites-with-offline-monitoring/)).

### 2.5 Fragmentation technologique des centres

- Enquête Advarra 2024 : une étude d'oncologie typique ajoute **jusqu'à 17 systèmes** à ceux du centre. **32 %** seulement des centres peuvent utiliser leurs propres identifiants [F/V] ([DIA Global Forum, janv. 2025](https://globalforum.diaglobal.org/issue/january-2025/technology-at-clinical-sites-the-good-the-bad-and-what-sponsors-can-do-to-turn-it-around/)).
- Près de **70 %** des centres gèrent **6 identifiants ou plus par étude** [F/V] ([ACRP, « Death by a thousand portals », 2026](https://acrpnet.org/2026/08/11/death-by-a-thousand-portals-addressing-technology-fragmentation-and-site-burden-in-clinical-research)).
- **Conséquence pour notre concept [H] :** tout nouvel outil qui ajoute **un portail de plus** sera rejeté. L'outil doit **réduire** le nombre d'endroits où l'on va chercher l'information, ou vivre à l'intérieur des outils existants.

### 2.6 Ressources humaines et dépendance aux personnes clés

- Le turnover des CRA en CRO est passé à **28 % en 2021** puis **32 % en 2022** [F] ([ACRP Clinical Researcher, févr. 2025](https://acrpnet.org/2025/02/14/cra-turnover-within-contract-research-organizations-post-covid-19-a-cross-sectional-study)). Il revient lentement vers ses niveaux historiques [F] ([BDO 2023/24](https://www.bdo.com/insights/tax/2023-2024-clinical-research-organization-compensation-turnover-insights-report)).
- La pénurie touche surtout les **profils expérimentés**. Les pénuries de coordinateurs et d'infirmiers de recherche persistent [F/T] ([PharmaVoice](https://www.pharmavoice.com/news/clinical-trials-staffing-crunch-hiring-cra/708614/)).
- **Conséquence [H] :** la connaissance d'une étude (interprétations validées, particularités du centre, historique des écarts) vit dans la tête et la boîte mail des personnes. Elle s'évapore à chaque départ.

### 2.7 Finances des centres

- Délais de paiement de **90 à 120 jours** ; **23 %** des centres subissent des retards de 90 jours ou plus. Selon le CTTI, **jusqu'à 40 %** des centres abandonnent des études à cause des retards de paiement [F, données 2016-2019] ([SCRS](https://myscrs.org/wp-content/uploads/2024/08/Site-Payments-and-Patient-Reimbursements-Global-Perspective.pdf) ; [Clinical Leader 2025](https://www.clinicalleader.com/doc/site-payments-are-still-a-mess-but-takeda-is-trying-to-help-0001)).
- Le marché est déjà occupé (Greenphire/Suvoda, IQVIA, Florence). **Ce n'est pas un angle mort.**

### 2.8 Cadre réglementaire qui crée l'opportunité

| Texte | Ce qui change | Effet pour un produit |
|---|---|---|
| **ICH E6(R3)** (principes et Annexe 1 adoptés par l'ICH le 6 janv. 2025, en vigueur dans l'UE le 23 juil. 2025 ; Annexe 2 annoncée par l'EMA pour 2027, à vérifier) [F] ([Sidley](https://www.sidley.com/en/insights/newsupdates/2025/02/international-council-finalizes-modernized-global-good-clinical-practice-guideline) ; [EMA](https://www.ema.europa.eu/sl/ich-e6-good-clinical-practice-scientific-guideline)) | Approche proportionnée et fondée sur le risque, facteurs critiques pour la qualité, qualité intégrée dès la conception, exigences sur les systèmes informatisés. | Un outil qui **montre** une qualité intégrée et pilotée par le risque, **au niveau du centre**, répond directement au texte. |
| **ICH M11** (protocole structuré, approuvé fin 2025) et **CDISC USDM v4** (début 2026) [F] ([Clinical Leader, janv. 2026](https://www.clinicalleader.com/doc/digital-protocols-are-at-an-inflection-point-a-conversation-with-novartis-and-transcelerate-leaders-0001)) | Le protocole devient une **donnée** structurée et non plus un PDF. | C'est la **condition technique** d'un moteur d'exécution. Cela abaisse le coût d'entrée, pour nous **comme pour les concurrents**. |
| **Règlement UE 536/2014 (CTR)** : seul applicable depuis le 31 janv. 2025 [F] ([EMA](https://www.ema.europa.eu/en/documents/presentation/presentation-transition-clinical-trials-elena-garcia-mendez_en.pdf)) | Modifications substantielles centralisées dans CTIS, parties I et II. | Le suivi des versions applicables par centre et par patient devient plus structuré, donc **modélisable**. |
| **FDA, Q&R sur les systèmes et dossiers électroniques** (final, oct. 2024) [F] ([Cooley](https://www.cooley.com/news/insight/2024/2024-10-24-fda-finalizes-guidance-on-use-of-part-11-electronic-systems-records-and-signatures-in-clinical-investigations)) | Validation proportionnée au risque, exigences de la partie 11. | Cadre de validation du produit. |
| **FDA, projet de guide sur l'IA en appui aux décisions réglementaires** (janv. 2025) [F] ([FDA](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/considerations-use-artificial-intelligence-support-regulatory-decision-making-drug-and-biological)) | Cadre de crédibilité des modèles d'IA, gradué selon le risque. | Il faut un **usage contextuel délimité** et une validation humaine. |

---

## 3. Analyse des besoins par intervenant

> Une remarque critique d'abord. Lister « dix frustrations » pour chacun des plus de 20 intervenants produirait surtout du remplissage. J'ai retenu pour chacun les points **les plus structurants**, avec leur niveau de preuve. Le détail complet est fourni pour les rôles de terrain, où se trouve l'opportunité.

### 3.1 Terrain clinique

#### ARC / CRC / TEC de centre investigateur (le cœur du sujet)

| Dimension | Contenu |
|---|---|
| **Frustrations** | 1) Multiplication des portails et identifiants [F]. 2) Amendements appris avant de recevoir les documents [T]. 3) Plusieurs versions en vigueur en même temps [F]. 4) Fenêtres de visite calculées à la main, souvent dans Excel [H]. 5) Modèles de source réécrits pour chaque étude [V/T, CRIO]. 6) Questions d'interprétation envoyées par mail au CRA, avec des réponses longues à venir et non partagées [H]. 7) Requêtes EDC sur des points qui auraient pu être évités au moment de la visite [H]. 8) Manuels laboratoire, pharmacie et imagerie séparés du protocole, parfois contradictoires [H]. 9) Charge des re-consentements [F/T]. 10) Responsabilité ressentie sans visibilité d'ensemble : « ai-je oublié quelque chose pour ce patient ? » [H]. |
| **Tâches chronophages** | Préparer les visites, saisir dans l'EDC, répondre aux requêtes, préparer les visites de monitoring, tenir l'ISF, mettre en œuvre les amendements, gérer le planning des patients [H/F]. |
| **Erreurs fréquentes et conséquences** | Visite hors fenêtre, examen oublié, mauvaise version du consentement, médicament concomitant interdit non repéré, délai de washout non respecté, horaire de prélèvement PK manqué. Conséquences : déviation, donnée inexploitable, risque pour la sécurité du patient, constat d'audit [F pour les volumes, H pour la typologie]. |
| **Encore manuel** | Calendriers, checklists de visite, comparaison de versions, suivi des re-consentements, réconciliation des manuels [H]. |
| **Informations difficiles à obtenir** | « Qu'est-ce qui change *pour ce patient* avec l'amendement 4 ? » ; « Le promoteur a-t-il déjà répondu à cette question pour un autre centre ? » [H]. |
| **Prêt à payer pour…** | Le centre a peu de budget [F]. Il paiera ou fera payer le promoteur si le temps gagné est **démontré** et si l'outil **réduit** le nombre de portails [H]. |

#### CRA (moniteur côté promoteur ou CRO)

| Dimension | Contenu |
|---|---|
| **Frustrations** | Rapports de visite longs à rédiger [T/V]. SDV peu utile [F]. Découverte des déviations après coup, à la visite. Charge de 6 à 10 centres ou plus [H]. Turnover et reprises d'études sans historique [F/H]. Rôle d'intermédiaire entre le centre et le moniteur médical pour les questions d'interprétation [H]. |
| **Erreurs** | Déviation non détectée, suivi d'actions perdu, mauvaise version de document vérifiée [H]. |
| **Information manquante** | Le risque **prospectif** par centre et par patient, et pas seulement les indicateurs rétrospectifs du RBQM [H]. |
| **Prêt à payer** | Le CRA ne paie pas. La **CRO** paie, si l'outil augmente le nombre de centres gérés par CRA à qualité égale [H]. |

#### Investigateur principal et médecins investigateurs

- Frustrations : temps de signature et de revue (eCRF, éligibilité, événements indésirables), délégation et formation, responsabilité légale sans visibilité en temps réel [H].
- Erreurs : éligibilité validée sur une information incomplète. Les échecs de sélection sont fréquents : **51 %** dans un audit de 15 essais, dont **55 %** pour critères d'inclusion non remplis [F] ([PMC9934872](https://pmc.ncbi.nlm.nih.gov/articles/PMC9934872)).
- Prêt à payer : rarement de façon directe. L'intérêt est d'attirer plus d'études vers le service [H].

#### Infirmiers de recherche clinique

- Frustrations : procédures horodatées (PK, ECG en série), kits de laboratoire, contraintes de jeûne et de préparation, changements de manuel laboratoire [H].
- Besoin : une **feuille de route minute par minute** de la visite, à jour de la dernière version [H].

#### Pharmaciens hospitaliers

- Frustrations : comptabilité des médicaments expérimentaux, excursions de température, fiches de dispensation, changements de posologie à la suite d'amendements, aveugle [H].
- Déjà partiellement couvert par les IRT/RTSM et les outils de pharmacie. Moins d'angle mort [H].

### 3.2 Pilotage des études

| Acteur | Points structurants |
|---|---|
| **Clinical Trial / Project Manager** | Visibilité sur le risque de dérive par centre ; coût et durée des amendements [F] ; « Qui applique quelle version ? » ; besoin de **prédire** plutôt que de constater [H]. |
| **Clinical Operations Manager** | Productivité des CRA et attrition ; standardisation entre études [F/H]. |
| **Data Manager** | Volume de requêtes ; données collectées mais inutiles (+600 % de points de données [F]) ; conformité aux contrôles d'édition après amendement [H]. |
| **Medical Monitor** | Questions d'interprétation récurrentes et non capitalisées ; dérogations d'éligibilité [H]. |
| **Qualité / AQ** | Recherche de cause racine des déviations, actions correctives et préventives (CAPA) peu efficaces, préparation des inspections ; exigence de qualité intégrée de l'E6(R3) [F]. |
| **Affaires réglementaires** | Modifications substantielles dans CTIS, cohérence parties I/II par État membre [F]. |

### 3.3 Écosystème

| Acteur | Points structurants |
|---|---|
| **Promoteurs industriels** | Coût des amendements (141 k$ à 535 k$ chacun [F]) ; protocoles inapplicables sur le terrain ; pression pour une surveillance réglementaire continue (FDA), au moins dans le discours des éditeurs [V]. |
| **CRO** | Marges sur le monitoring, attrition des CRA, différenciation par la qualité [F/H]. |
| **Centres, hôpitaux, CHU** | Financement, fragmentation des outils [F], perte de savoir-faire [H]. En France, les DRCI sont à la fois **promoteurs institutionnels et centres** : un terrain d'expérimentation unique [H]. |
| **Comités d'éthique** | Volume de modifications ; cohérence des consentements [H]. |
| **Patients et associations** | Charge des visites, compréhension des changements (re-consentement), visites inutiles ou manquées [F pour la charge, H pour le reste]. |
| **Autorités** | Évolution vers une surveillance fondée sur le risque et sur les données [F]. |

---

## 4. Les angles morts du marché

| Question | Réponse |
|---|---|
| Quelles tâches essentielles reposent encore sur des chaînes de mails ? | **Les clarifications de protocole** (centre → CRA → moniteur médical → retour), la **notification des amendements** et le **suivi des re-consentements** [T/H]. |
| Quelles informations sont dispersées ? | Protocole, amendements, manuels laboratoire/pharmacie/imagerie, lettres de clarification, mémos administratifs, procédures locales du centre, agenda des patients [H]. **Aucun système ne les fusionne en une vérité opérationnelle par patient.** |
| Quels problèmes sont détectés trop tard ? | Les déviations, découvertes à la visite de monitoring ou lors de la revue des données, plusieurs semaines après les faits [F/H]. |
| Quelles erreurs pourraient être anticipées ? | Fenêtres, washouts, médicaments concomitants interdits, versions de consentement, examens imposés par un amendement, horaires PK, échéances de sécurité [H]. **Toutes sont déterministes une fois le protocole structuré.** |
| Quelle connaissance se perd au départ d'un collaborateur ? | Les interprétations validées, les particularités du centre, l'historique des écarts et des solutions [H]. |
| Quoi repenser entièrement plutôt qu'automatiser ? | **Le monitoring rétrospectif → la prévention prospective.** On ne vérifie plus ce qui a été fait : on garantit ce qui *va* être fait [H]. |
| Ce que les éditeurs ne comprennent pas | Le travail réel d'un ARC n'est pas la saisie. C'est **l'anticipation** : la charge mentale de « ne rien oublier pour chaque patient, sous la bonne version ». Les éditeurs vendent des systèmes d'enregistrement, pas des systèmes d'anticipation [H]. |
| Données inexploitées | **Les déviations elles-mêmes.** Chaque promoteur les enregistre, mais personne ne les relie, d'une étude à l'autre, aux éléments de protocole qui les causent [H]. |
| Difficultés qui n'apparaissent qu'à plusieurs | La version en vigueur diffère selon le centre et le pays (CTR parties I/II), et la même question est posée N fois par N centres [F/H]. |

**Problèmes invisibles retenus :** la charge mentale d'anticipation, la dépendance aux personnes clés et la dette d'interprétation, c'est-à-dire l'écart entre ce que dit le protocole et ce que le centre croit qu'il dit.

---

## 5. Technologies : celles qui comptent vraiment

| Technologie | Verdict | Pourquoi |
|---|---|---|
| **Protocole structuré (M11/USDM) + extraction documentaire par LLM** | **Indispensable** | Transformer protocole et manuels en objets (activités, fenêtres, conditions). Verily annonce 60 à 70 % de temps de digitalisation en moins [V] ([Verily](https://verily.com/perspectives/the-role-of-ai-in-powering-digital-protocols)). |
| **Moteur de règles déterministe et versionné** | **Indispensable, et sous-estimé** | La conformité au protocole **ne doit pas** dépendre d'un LLM probabiliste. Le LLM extrait les règles, un humain les valide, puis un moteur déterministe exécute. C'est la clé de la validation GxP. |
| **Graphe de connaissances** | Utile | Relier élément de protocole → version → centre → patient → déviation → clarification. |
| **Agents IA avec validation humaine** | Utile mais encadré | Préparer des brouillons (notifications d'amendement, checklists, réponses aux requêtes). Jamais de décision clinique. |
| **Modèles prédictifs** | Phase 2 | Prédire les déviations exige des données. IQVIA annonçait plus de 70 % de précision en 2022 [V] ([IQVIA](https://www.iqvia.com/ru-kz/blogs/2022/04/ai-and-rbm-is-this-the-future-of-clinical-trials)). Aucune validation publiée récente n'a été trouvée. |
| **Jumeau numérique de processus** | **Oui, si on le prend au sens strict** | Le « jumeau » est l'état calculé de chaque patient au regard du protocole. Ce n'est pas un gadget 3D. |
| IA multimodale, conversationnel | Accessoire | Interfaces d'accès : elles ne différencient pas. |

---

## 6. Quinze concepts réellement différents

> Format compact pour chaque concept : Problème • Utilisateurs • Fonctionnement • Innovation • Pourquoi l'existant ne suffit pas • Exemple • Gain • Modèle économique • Difficulté technique • Réglementation/sécurité • Potentiel commercial.

### C1. KAIROS : jumeau opérationnel du patient-sujet
- **Problème :** les déviations évitables, causées par une traduction manuelle du protocole et des versions multiples.
- **Utilisateurs :** ARC/CRC, infirmiers, PI, CRA.
- **Fonctionnement :** le protocole, les amendements, les manuels et les clarifications sont compilés en règles versionnées. L'outil connaît l'état de chaque patient (visites, dates, médicaments, consentement signé) et calcule *ce qui doit arriver, quand, sous quelle version*. Il signale les conflits **avant** la visite.
- **Innovation :** on passe du constat à la prévention. C'est un moteur d'exécution, pas un dépôt de documents.
- **Pourquoi l'existant ne suffit pas :** l'eSource (CRIO) structure la saisie, mais les modèles restent conçus par étude et la logique inter-documents et inter-versions par patient est limitée [V/H]. Les CTMS planifient des visites, pas la conformité fine.
- **Exemple :** amendement 3 : ajout d'un ECG à J15 pour les patients randomisés après approbation, et nouveau délai de washout pour un inhibiteur du CYP3A4. KAIROS liste les 4 patients concernés, les 2 re-consentements nécessaires et un patient dont le traitement concomitant déclenche une alerte.
- **Gain [H] :** réduction d'une partie des déviations évitables et de la préparation des visites. À mesurer en pilote.
- **Modèle économique :** abonnement par étude et par centre, payé par la CRO ou le promoteur ; version centre en freemium.
- **Difficulté :** élevée (fiabilité de l'extraction, validation GxP).
- **Réglementation :** données de santé (RGPD, hébergement HDS en France), validation du système informatisé, qualification « non dispositif médical » à vérifier.
- **Potentiel :** très élevé.

### C2. Navigateur d'amendements
- **Problème :** les quelque 260 jours de versions concurrentes et l'impact d'un amendement mal compris [F].
- **Fonctionnement :** comparaison sémantique entre versions ; impact par patient, par centre et par document (consentement, modèles de source, EDC) ; plan de mise en œuvre attribué.
- **Innovation :** comparer le *sens* des versions, pas leur texte.
- **Pourquoi l'existant ne suffit pas :** Medable (agent DDF, juin 2026) propage les changements vers les **systèmes du promoteur** [V] ([Medable](https://www.medable.com/newsroom/medable-introduces-digital-data-flow-agent-laying-the-foundation-for-end-to-end-agentic-clinical-development)), pas vers **les patients d'un centre**.
- **Modèle :** paiement par amendement ou par étude.
- **Difficulté :** moyenne. **Potentiel :** élevé, mais c'est en réalité **un module de C1**.

### C3. Banc d'essai d'exécutabilité du protocole
- **Problème :** les protocoles conçus sans tester leur faisabilité sur le terrain.
- **Fonctionnement :** simuler des parcours de patients virtuels et des contraintes de centres (horaires, équipements), puis prédire les points de déviation et la charge.
- **Pourquoi l'existant ne suffit pas :** Faro Health estime déjà la charge pour le patient et le site [V] ([Faro](https://www.newswire.com/news/faro-health-secures-20-million-to-scale-the-digital-transformation-of-21951519)). L'élément manquant, c'est la **réalité terrain des déviations**.
- **Potentiel :** élevé **si** la solution s'alimente de vraies données de déviation, ce que C1 produit.

### C4. Mémoire d'étude (passation sans perte)
- **Problème :** la connaissance perdue lors du turnover [F].
- **Fonctionnement :** capture passive des décisions, clarifications et particularités du centre, reliées aux éléments du protocole ; dossier de passation généré automatiquement.
- **Innovation :** mémoire *structurée par le protocole*, pas un wiki.
- **Limite :** sans moteur d'usage quotidien, personne n'alimente la base [H]. **Meilleur comme fonction de C1.**

### C5. Bourse des clarifications de protocole
- **Problème :** la même question d'interprétation est posée N fois par N centres, par mail.
- **Fonctionnement :** une question est liée à un élément du protocole, puis validée par le moniteur médical et publiée à **tous** les centres, versionnée, avec piste d'audit.
- **Innovation :** transformer l'interprétation en **donnée réglementaire partagée**. Une clarification fréquente est un **signal d'amendement**.
- **Pourquoi l'existant ne suffit pas :** des FAQ promoteur existent sous forme de PDF ou de mails [H]. Aucune solution liée au protocole structuré n'a été trouvée dans mes recherches. Cela ne prouve pas qu'elle n'existe pas.
- **Potentiel :** moyen seul, **fort comme fonction de C1**.

### C6. Compteur de charge réelle des centres
- **Problème :** budgets sous-estimés, négociation sans preuve.
- **Fonctionnement :** mesure passive du temps par procédure et par visite, puis benchmark entre centres et dossier de négociation.
- **Limite :** sensible sur le plan social (perception de surveillance du personnel) et soumis au droit du travail [H].
- **Potentiel :** moyen.

### C7. Facturation auto-déclenchée
- **Problème :** paiements à 90-120 jours [F].
- **Fonctionnement :** l'événement clinique validé déclenche la facture.
- **Verdict :** **marché occupé** (Greenphire/Suvoda, Florence, IQVIA). Peu différenciant.

### C8. Copilote de rapport de visite de monitoring
- **Verdict :** déjà adressé par Veeva, IQVIA et d'autres [V]. **Écarté comme produit principal.**

### C9. Laboratoire de compréhension du consentement
- **Problème :** consentement signé mais mal compris, surtout lors d'un re-consentement.
- **Fonctionnement :** mesure de la compréhension section par section, contenu adapté, signal pour l'investigateur.
- **Limite :** l'eConsent est déjà sur le marché (Medrio, Medable, Signant, etc.). Différenciation faible.

### C10. Registre de charge du patient
- **Problème :** abandons liés à la charge (22 % contre 19 % [F]).
- **Fonctionnement :** le patient déclare sa charge réelle (trajets, attente), ce qui donne un risque d'abandon et des actions possibles.
- **Potentiel :** moyen. L'adoption par les patients est incertaine.

### C11. Jumeau pharmacie du médicament expérimental
- **Fonctionnement :** reconnaissance visuelle des kits, réconciliation de la comptabilité, impact des amendements sur la dispensation.
- **Limite :** chevauche les IRT/RTSM [H]. Marché étroit.

### C12. Radar réglementaire vers procédures internes
- **Fonctionnement :** suivi de l'évolution des textes (E6(R3) Annexe 2, CTR, Annexe 11), cartographie des écarts dans les procédures du centre ou de la CRO, brouillon de révision.
- **Limite :** utile mais ponctuel, et du conseil existe déjà. Potentiel moyen.

### C13. Simulateur d'inspection
- **Fonctionnement :** un agent pose les questions d'un inspecteur sur le TMF/ISF et suit la traçabilité des preuves.
- **Limite :** des outils d'« inspection readiness » existent déjà dans les eTMF (Veeva, etc.) [H]. Différenciation partielle.

### C14. Dossier d'éligibilité opposable
- **Problème :** des échecs de sélection et des erreurs d'éligibilité [F].
- **Fonctionnement :** chaque critère est relié à une preuve source citée, puis validé par l'investigateur, avec un dossier vérifiable par le CRA.
- **Concurrence :** pré-screening IA (Triomics, Reify StudyTeam, ConcertAI) [V] ([Bioxconomy](https://www.bioxconomy.com/clinical-and-research/medable-launches-ai-agent-to-streamline-clinical-trial-data-assessment-for-principal-investigators)). Le dossier opposable est un **module naturel de C1**.
- **Risque :** cela s'approche de l'aide à la décision clinique, avec une qualification MDR possible.

### C15. Passeport de qualification du personnel des centres
- **Fonctionnement :** formations, CV et délégations réutilisables d'une étude à l'autre.
- **Verdict :** TransCelerate (Shared Investigator Platform, reconnaissance mutuelle des formations GCP) couvre déjà une partie du sujet. Faible.

---

## 7. Grille de notation (/100)

Ces notes sont des **jugements d'experts [H]**, pas des mesures.

| # | Concept | Intensité (20) | Originalité (20) | Valeur op. (15) | Commercial (15) | Faisabilité (10) | Avantage conc. (10) | Adoption (10) | **Total** |
|---|---|---|---|---|---|---|---|---|---|
| C1 | KAIROS, jumeau patient | 19 | 17 | 15 | 14 | 5 | 9 | 8 | **87** |
| C2 | Navigateur d'amendements | 18 | 14 | 13 | 12 | 7 | 6 | 8 | **78** |
| C5 | Bourse des clarifications | 15 | 16 | 11 | 9 | 8 | 7 | 8 | **74** |
| C3 | Banc d'exécutabilité | 16 | 13 | 11 | 13 | 5 | 7 | 6 | **71** |
| C4 | Mémoire d'étude | 15 | 13 | 11 | 9 | 7 | 6 | 6 | **67** |
| C14 | Dossier d'éligibilité opposable | 15 | 10 | 12 | 11 | 6 | 5 | 7 | **66** |
| C6 | Compteur de charge | 13 | 12 | 9 | 10 | 7 | 6 | 4 | **61** |
| C10 | Registre charge patient | 13 | 11 | 9 | 9 | 7 | 5 | 5 | **59** |
| C13 | Simulateur d'inspection | 12 | 9 | 10 | 10 | 7 | 4 | 7 | **59** |
| C12 | Radar réglementaire | 11 | 10 | 9 | 9 | 7 | 5 | 7 | **58** |
| C9 | Compréhension consentement | 12 | 8 | 8 | 9 | 7 | 4 | 6 | **54** |
| C11 | Jumeau pharmacie | 11 | 9 | 9 | 8 | 6 | 5 | 6 | **54** |
| C7 | Facturation auto | 14 | 3 | 10 | 10 | 7 | 2 | 7 | **53** |
| C15 | Passeport qualification | 11 | 4 | 9 | 8 | 7 | 3 | 7 | **49** |
| C8 | Copilote rapport de visite | 12 | 2 | 9 | 9 | 8 | 2 | 7 | **49** |

**Top 3 : C1 (87), C2 (78), C5 (74).**

---

## 8. Analyse approfondie du top 3

### C1. KAIROS (87)
- **Forces :** il s'attaque au problème le mieux documenté (déviations et versions). Il fait passer de la constatation à la prévention, ce qui est aligné sur l'E6(R3). Il crée une **donnée propriétaire** : les déviations évitées et les causes reliées aux éléments du protocole. Il absorbe C2, C4, C5 et C14 en fonctions, ce qui donne un produit cohérent plutôt qu'une juxtaposition.
- **Faiblesses :**
  1. **Fiabilité de l'extraction** : une règle mal extraite est pire que pas de règle (fausse assurance). Il faut une validation humaine systématique et une traçabilité vers le paragraphe source.
  2. **Intégration** : il faut l'état des patients (dates de visite, médicaments), qui vit dans l'EDC, le DPI et le CTMS. Sans intégration, la saisie double tue l'adoption.
  3. **Convergence concurrentielle** : CRIO (eSource), Medable (DDF), Florence (agent Farr, MCP) pourraient s'en approcher [V].
  4. **Coût de validation GxP.**
- **Risque majeur :** devenir « le 18e portail ». Parade : extension/intégration et **zéro saisie supplémentaire** comme principe de conception.

### C2. Navigateur d'amendements (78)
- **Forces :** une douleur aiguë, datée et mesurable (coût par amendement, délais AACI/WCG). Achat facile à justifier : un seul amendement de phase III coûte en médiane 535 k$ [F].
- **Faiblesses :** usage épisodique (3,3 fois par étude), donc peu d'habitude créée. Les éditeurs côté promoteur s'en approchent.
- **Conclusion :** c'est **la meilleure porte d'entrée commerciale** (« wedge ») vers C1.

### C5. Bourse des clarifications (74)
- **Forces :** simple à construire et à adopter. Effet réseau entre centres d'une même étude. Produit un **signal précoce d'amendement**.
- **Faiblesses :** le promoteur doit l'accepter (gouvernance du moniteur médical, statut réglementaire de la clarification). La valeur monétisable seule est faible.
- **Conclusion :** une fonction de C1 à fort pouvoir d'adoption.

---

## 9. Le concept ultime : KAIROS

### 9.1 Nom et positionnement
**KAIROS**, du grec *kairos*, « le moment juste ».
> *« Le moteur d'exécution du protocole : chaque patient, chaque visite, la bonne version, sans déviation évitable. »*

Catégorie créée : **Protocol Execution Intelligence**. Ce n'est ni un CTMS, ni un eSource, ni un eISF. C'est une couche de calcul **entre** le protocole (côté promoteur) et le soin (côté centre).

### 9.2 Vision à 5 ans [P]
Devenir la **référence mondiale de l'exécutabilité des protocoles**.
- Côté centres et CRO : la vérité opérationnelle de chaque patient.
- Côté promoteurs : un **score d'exécutabilité**, calculé avant finalisation du protocole à partir de centaines d'études, qui prédit où les déviations surviendront.
- À terme : un standard de fait pour échanger « règles d'exécution + preuves de conformité » avec les autorités, dans l'esprit de la surveillance continue.

### 9.3 Le problème fondamental
**Le protocole n'est pas exécutable.** C'est un texte interprété par des humains surchargés, dans des versions qui changent, réparties dans plusieurs documents. Résultat : des déviations massives [F], un contrôle rétrospectif peu rentable [F] et une connaissance qui se perd à chaque départ [F/H].

### 9.4 Fonctionnement détaillé

```
 [Sources]                          [Compilation]                     [Exécution]                 [Sorties]
 Protocole PDF/M11/USDM  ─┐
 Amendements & redlines  ─┤     Extraction LLM  →  Règles candidates   Moteur déterministe      • Brief pré-visite
 Manuels labo/pharma/IRM ─┼──►  (citation au §)    → Validation humaine ─► versionné (par pays,  ─► • Alertes préventives
 Lettres de clarification─┤     (double validation   (ARC/CRA/MedMon)     centre, patient)        • Impact amendement
 Contraintes du centre   ─┘      pour règles critiques)                    ▲                     • Dossier d'éligibilité
                                                                            │                     • Mémoire d'étude
 [État patient] EDC/CTMS/DPI (lecture) ─────────────────────────────────────┘                     • Données déviation→cause
```

1. **Compiler.** Le LLM extrait activités, fenêtres, conditions, interdictions, dépendances et horaires. Chaque règle est **citée** (document, version, section). Un humain valide, avec double validation pour les règles « critiques pour la qualité » au sens de l'E6(R3).
2. **Versionner.** Chaque règle a une période de validité par pays, par centre (selon l'approbation du comité d'éthique ou de l'autorité) et par patient (selon le consentement signé et la date de randomisation).
3. **Exécuter.** Un moteur **déterministe**, sans LLM à l'exécution, calcule pour chaque patient l'échéancier, les prérequis et les conflits.
4. **Apprendre.** Les déviations réelles, les quasi-incidents évités et les clarifications enrichissent un graphe « élément de protocole → type de déviation ».

### 9.5 Architecture fonctionnelle
- **Couche Sources** : connecteurs documentaires (eISF/eTMF, mail, CTIS en lecture d'export), import M11/USDM.
- **Couche Compilateur** : pipeline LLM, revue humaine, bibliothèque de règles types (fenêtre, washout, médicament interdit, horaire PK, re-consentement, jeûne…).
- **Couche Moteur** : moteur de règles temporelles versionnées (logique de type calendrier, contraintes), auditable.
- **Couche État** : modèle patient minimal et pseudonymisé ; lecture depuis l'EDC/CTMS/DPI via API, FHIR ou import.
- **Couche Expérience** : « brief du jour », vue patient, vue amendement, vue CRA multi-centres, vue chef de projet.
- **Couche Preuve** : piste d'audit (règle → source → validateur → alerte → action), export pour l'inspection.
- **Couche Intelligence** (phase 2+) : graphe inter-études anonymisé et score d'exécutabilité.

### 9.6 Fonctionnalités principales
1. Échéancier de conformité par patient, avec fenêtres exactes et la version applicable.
2. Brief pré-visite : ce qu'il faut faire, préparer et vérifier, avec ce qui a changé depuis la dernière visite.
3. Alertes préventives : washout, médicament interdit, re-consentement, fenêtre en danger, horaires PK.
4. Impact d'un amendement par patient et par centre, avec plan d'action.
5. Bourse des clarifications liée aux règles.
6. Dossier d'éligibilité avec preuve par critère (validation par l'investigateur).
7. Dossier de passation automatique (mémoire d'étude).
8. Piste d'audit et export pour l'inspection.

### 9.7 Les fonctionnalités « WOW »
- **« Diff patient »** : à la réception d'un amendement, en quelques minutes : « 7 patients concernés, 3 re-consentements, 2 visites à replanifier, 1 conflit de médicament concomitant ». Aujourd'hui, ce travail prend des jours de lecture croisée [H].
- **« Pourquoi ? » cliquable** : chaque alerte renvoie à la phrase exacte du protocole ou du manuel, dans la bonne version. Fini le « je crois que c'est écrit quelque part ».
- **« Cette question a déjà été posée »** : quand un ARC pose une question, l'outil montre la clarification déjà validée pour un autre centre.
- **« Météo des déviations »** pour le CRA : les centres et patients où une déviation est probable **dans les 14 prochains jours**. Ce sont des règles, et non une prédiction statistique, au départ.
- **Score d'exécutabilité** (phase 3) : le promoteur charge son projet de protocole, et l'outil lui répond : « Ce washout de 28 jours combiné à cette fenêtre de ±2 jours a généré des déviations dans des études comparables. »

### 9.8 Avantage concurrentiel
1. **Moteur déterministe validable** plutôt qu'un agent LLM « boîte noire » : c'est un avantage réglementaire.
2. **Donnée inter-études** reliant déviations et causes : effet réseau, difficile à copier. Les éditeurs mono-promoteur ne voient que leurs propres études.
3. **Neutralité** : ni CRO, ni EDC, ni eISF. Le produit s'intègre à tous, ce que les grands éditeurs font mal par intérêt [H].
4. **ADN terrain** : le fondateur est ARC. La conception part de la charge mentale d'anticipation, ce que les éditeurs comprennent peu [H].

### 9.9 Qui paie
- **CRO** (premier payeur) : productivité des CRA, qualité, différenciation dans les appels d'offres.
- **Promoteurs** : coûts d'amendement et de déviations, conformité à l'E6(R3), puis score d'exécutabilité.
- **Réseaux de centres / SMO / CHU** : moins de déviations, capacité à prendre plus d'études avec la même équipe.
- **Utilisateurs non payeurs** : ARC/CRC, infirmiers, investigateurs, gratuit au niveau du centre pour l'adoption.

### 9.10 Modèle économique [P]
- **Licence par étude et par centre actif**, payée par le promoteur ou la CRO : ordre de grandeur de 300 à 1 000 € par centre et par mois selon la complexité. **À valider**, aucune donnée de prix publique fiable n'a été trouvée.
- **Module amendement** facturé à l'événement, pour l'entrée commerciale.
- **Abonnement réseau de centres** (SMO, CHU) pour l'usage multi-études.
- **Score d'exécutabilité** : forfait par protocole évalué (phase 3), sur des données anonymisées et agrégées, avec consentement contractuel des contributeurs.

### 9.11 Intégrations
- Protocoles : ICH M11, CDISC USDM v4 (importation native).
- EDC : Medidata Rave, Veeva Vault EDC, Ennov, REDCap (académique), en lecture.
- eISF/eTMF : Florence (MCP ouvert en 2026 [V]), Veeva.
- CTMS : lecture des dates de visite.
- DPI hospitalier : FHIR ou HL7 quand c'est possible ; sinon, export manuel minimal.
- Messagerie et agenda : notifications, pas de nouveau portail obligatoire.

### 9.12 Expansion internationale
L'ICH E6(R3) est mondial et ICH M11 aussi. Le moteur est multi-juridiction par conception (versions par pays). Séquence [P] : France (CHU, DRCI, réseaux d'oncologie) → UE (CTR harmonisé) → États-Unis (SMO, réseaux de centres, CRO), où la volonté de payer est plus forte.

---

## 10. Une journée avec KAIROS

> Ce scénario est **illustratif [H]**. Étude fictive : ONCO-302, phase III, 14 patients actifs dans le centre. L'amendement 4 vient d'être approuvé par le comité d'éthique.

### 07 h 55 : Léa, ARC investigateur (CHU)
**À l'ouverture**, pas de tableau de bord à 40 tuiles, mais **trois lignes** :
1. « Amendement 4 approuvé pour votre centre hier. **5 patients concernés.** Re-consentement requis pour 3 (nouveau risque hépatique). Formulaire v6.0 reçu dans l'ISF. »
2. « Patient 302-014, visite C3J1 aujourd'hui à 10 h. **Nouveau depuis l'amendement 4 : bilan hépatique obligatoire avant administration.** Kit labo : référence modifiée (manuel labo v3.2, §4.1). »
3. « Patient 302-009 : traitement par clarithromycine saisi au DPI hier. **Inhibiteur puissant du CYP3A4, interdit** (protocole v5.0, §6.4.2). Prévenir l'investigateur avant la prochaine prise. »

**Ce que l'outil a compris seul :** la version applicable à chaque patient selon sa date de consentement ; le changement de manuel labo ; la nouvelle ligne de traitement au DPI.
**Ce qu'il anticipe :** la fenêtre de C4 du patient 011 tombe un 1er mai. Il propose de l'avancer à J-1, dans la fenêtre.
**Ce qu'il ne fait pas :** il ne prend aucune décision clinique. Il cite la source et l'investigateur décide.

Léa clique sur « Pourquoi ? » à côté de l'alerte du patient 009 : la phrase du protocole s'affiche, surlignée. Elle transmet au Dr Martin en un clic, et l'accusé de lecture est tracé.

### 11 h 30 : Léa a une question
« Le scanner de réévaluation peut-il être fait en externe ? » KAIROS répond : « **Clarification CL-012** validée par le moniteur médical le 14/10 pour le centre de Lyon : oui, si le scanner respecte les critères de l'annexe imagerie. Applicable à tous les centres. » Il n'y a pas eu de mail ni d'attente de trois jours.

### 09 h 00 (même jour) : Karim, CRA, 8 centres
**À l'ouverture : la météo des déviations à 14 jours.**
- Centre de Lille : 2 re-consentements de l'amendement 4 en retard, avec une visite prévue avant la date limite. **Risque élevé.**
- Centre de Nantes : un nouveau coordinateur arrivé il y a 10 jours. KAIROS a généré son **dossier de passation** (12 clarifications locales, 3 particularités du centre, historique des écarts).
- Centre du CHU de Léa : alerte de médicament concomitant traitée à 08 h 12, accusé de lecture de l'investigateur. **Risque maîtrisé.**

Karim prépare sa visite de Lille : KAIROS prépare la **liste des points à revoir** à partir des règles critiques, et non une SDV à 100 %. Le rapport de visite est pré-rempli **à partir des preuves** (alertes, actions, signatures).

### 16 h 00 : Sophie, chef de projet clinique (promoteur)
- **Vue amendement 4 sur 41 centres** : 29 ont mis en œuvre, 9 sont en attente de l'avis du comité d'éthique, 3 appliquent la nouvelle version **avant** l'approbation locale. Ces trois cas sont détectés et bloqués avant qu'une déviation n'arrive.
- **Signal** : la clarification CL-012 a été demandée par 11 centres. KAIROS suggère : « Candidat pour la prochaine version du protocole ou un mémo administratif. »
- **Coût évité estimé**, avec la méthode affichée et des hypothèses modifiables. C'est une estimation, pas une promesse.

### Pourquoi on ne s'en passe plus [H]
- Le matin, l'ARC n'a plus à *se demander* ce qu'il a oublié : l'outil le lui dit, avec la preuve.
- Le CRA passe de « trouver les erreurs » à « empêcher les erreurs ».
- Le chef de projet *voit* la mise en œuvre d'un amendement au lieu de la reconstituer par mails.
- L'habitude quotidienne vient du brief du matin : c'est le levier de rétention.

---

## 11. La concurrence : vérification sérieuse

| Acteur | Ce qu'il fait (selon ses communications) | Recouvrement avec KAIROS | Ce qui manque |
|---|---|---|---|
| **CRIO** (eSource) | Modèles eSource centralisés avec contrôles intégrés ; annonce −20 à −40 % de déviations [V] ([CRIO](https://clinicalresearch.io/products/esource/central-esource/)) | **Fort sur la saisie en visite** | Il faut adopter tout l'eSource CRIO. Pas de calcul d'impact d'amendement par patient trouvé dans mes recherches. Pas de mémoire de clarifications, pas de lecture du DPI. **C'est le concurrent le plus dangereux.** |
| **Medable** (agent DDF, juin 2026) | Protocole en USDM 4.0, propagation des amendements vers les systèmes [V] ([R&D World](https://www.rdworldonline.com/medables-digital-data-flow-agent-focuses-on-protocol-translation-as-the-agentic-race-accelerates/)) | Moyen (même socle technique) | Vision **promoteur vers systèmes**, pas **centre vers patient**. Agent d'investigateur annoncé [V]. **Peut converger.** |
| **Florence** (eISF, agent Farr, MCP) | 88 000 centres annoncés ; agent IA pour les équipes d'étude [V] ([PRNewswire](https://www.prnewswire.com/news-releases/florence-healthcare-unlocks-agentic-ai-across-global-site-network-at-dia-2026-302800686.html)) | Moyen (documents, présence dans les centres) | Une logique **documentaire**, pas un moteur de règles temporelles par patient. **C'est un partenaire d'intégration possible** grâce à MCP. |
| **Verily, IQVIA** (digitalisation du protocole) | Protocole PDF vers JSON [V] | Faible à moyen | Côté promoteur. |
| **Faro Health** | Conception de protocole, estimation de la charge [V] | Moyen avec le module « score » | Pas de données réelles de déviation terrain. |
| **ConcertAI ACT, Tilda, Triomics, Reify** | Agents pour accélérer, pré-screening [V] | Faible (éligibilité) | Pas de moteur de conformité versionné. |
| **RBQM** (CluePoints, Medidata, etc.) | Surveillance centralisée, indicateurs de risque [F/V] | Moyen côté CRA | **Rétrospectif** : il travaille sur des données déjà saisies, et non de façon prospective sur ce qui doit arriver. |
| **CTMS / EDC** (Veeva, Medidata) | Planification des visites, contrôles d'édition | Faible à moyen | Contrôles *après* saisie ; fenêtres seulement, pas l'ensemble des prérequis inter-documents. |

**Verdict honnête :**
- **Ce qui n'est PAS nouveau** : la digitalisation du protocole, l'eSource avec contrôles, les agents IA pour les centres, le RBQM, la planification des visites. Je ne présente aucun de ces éléments comme révolutionnaire.
- **Ce qui semble réellement non couvert** (aucune offre trouvée dans mes recherches, ce qui **ne prouve pas** qu'elle n'existe pas) : la **combinaison** de quatre éléments.
  1. Un moteur déterministe versionné **par patient** qui fusionne protocole, amendements, manuels et clarifications.
  2. Une lecture de l'état réel du patient (DPI, EDC) sans saisie supplémentaire.
  3. Le calcul d'impact d'un amendement au niveau du patient.
  4. Un graphe inter-études « élément du protocole → déviation ».
- **Comment être 10 fois plus utile que CRIO ou Medable :** (a) **pas de remplacement** de l'eSource ou de l'EDC, on s'y superpose, ce qui réduit fortement la barrière d'adoption ; (b) une vue **multi-documents et multi-versions** que ni l'eSource ni l'EDC ne modélisent ; (c) une **donnée inter-promoteurs** qu'aucun acteur lié à un promoteur ne peut agréger.
- **Fenêtre d'opportunité [H] : 18 à 30 mois** avant qu'un grand acteur ne converge. **La rapidité d'exécution et l'accès aux données des centres sont décisifs.**
- **Action recommandée avant tout investissement :** 20 entretiens structurés (ARC, CRA, chefs de projet) et des démonstrations à CRIO, Florence et Medable pour **vérifier en direct** les capacités réelles de calcul d'impact par patient.

---

## 12. Stratégie de lancement

### 12.1 MVP en 3 mois : « Diff patient + brief pré-visite »
**But :** prouver qu'on extrait des règles fiables et qu'un ARC gagne du temps sur un amendement réel.

Fonctions indispensables :
1. Import du protocole et de deux versions amendées (PDF), extraction LLM des règles de 6 types (fenêtre, procédure obligatoire, washout, médicament interdit, re-consentement, horaire PK) **avec citation**.
2. Interface de validation humaine des règles.
3. Saisie minimale de l'état patient (dates de consentement, randomisation, visites) par import CSV de l'EDC ou du CTMS, **pseudonymisé**.
4. Sortie « impact amendement par patient » et brief pré-visite.
5. Piste d'audit élémentaire.

**Hors périmètre du MVP :** lecture du DPI, prédiction, score d'exécutabilité, multi-pays.
**Méthode de preuve :** rejouer 3 à 5 amendements **réels et passés** (protocoles publics sur ClinicalTrials.gov ou protocoles académiques avec accord), puis comparer au travail manuel d'ARC expérimentés. On mesure la précision et le rappel des règles et le temps gagné.

**Équipe [P] :** fondateur ARC (produit et métier), 1 ingénieur full-stack senior, 1 ingénieur ML/LLM, appui à temps partiel d'un consultant qualité GxP. **Coût : environ 120 à 200 k€** (salaires ou équivalents, infrastructure, juridique). Ordre de grandeur, pas un devis.

### 12.2 Version commercialisable en 6 mois
- Moteur déterministe versionné par centre et par patient.
- Bourse des clarifications.
- Rôles et droits (centre, CRA, chef de projet), authentification unique (SSO).
- Hébergement **HDS** (France) ; dossier de validation (spécifications des besoins utilisateurs, analyse de risque, IQ/OQ/PQ proportionnés, selon GAMP 5).
- 2 à 3 pilotes payants.
- **Équipe :** 6 à 8 personnes. **Cumul de 0,6 à 1 M€** [P].

### 12.3 Version avancée à 12 mois
- Import ICH M11/USDM ; intégrations EDC (REDCap, Ennov ; puis Medidata, Veeva) ; connecteur Florence/MCP.
- Lecture des médicaments concomitants depuis le DPI (FHIR) pour les CHU volontaires.
- Vue CRA multi-centres, « météo des déviations » par règles.
- Dossier d'éligibilité avec preuves.
- Premières données inter-études anonymisées.

### 12.4 Déploiement international à 24 mois
- UE multi-pays (versions CTR par État membre).
- États-Unis : réseaux de centres et SMO, conformité 21 CFR Part 11, SOC 2 Type II, HIPAA (BAA).
- Bêta du score d'exécutabilité auprès de 3 à 5 promoteurs.
- **Levée de série A à prévoir [P].**

### 12.5 Premiers clients à cibler
1. **DRCI de CHU français**, à la fois promoteurs académiques et centres : un seul interlocuteur pour les deux côtés, accès aux protocoles et à l'état des patients, et une forte sensibilité aux amendements et au turnover. Faible budget, mais un **excellent terrain de preuve**.
2. **Réseaux d'oncologie** (centres de lutte contre le cancer, groupes coopérateurs académiques) : protocoles complexes, 47 % de patients touchés par les déviations [F].
3. **CRO de taille moyenne** européennes, qui cherchent à se différencier en qualité.
4. Ensuite seulement, les grands promoteurs. Leurs cycles de vente durent 12 à 18 mois et leur processus d'achat est lourd [H].

### 12.6 Données nécessaires
- Protocoles et amendements : publics (ClinicalTrials.gov publie de nombreux protocoles), académiques sous convention, puis ceux des clients.
- Déviations historiques : celles des clients pilotes, sous convention et anonymisées.
- État des patients : **minimal et pseudonymisé** (dates, statut du consentement, catégories de médicaments). **Pas besoin de l'identité.**

### 12.7 Exigences réglementaires et de sécurité

| Domaine | Exigence et approche |
|---|---|
| **RGPD** | Données de santé, catégorie particulière (art. 9). Rôle de **sous-traitant** (art. 28) du centre ou du promoteur. Minimisation et pseudonymisation dès la conception. Analyse d'impact (AIPD) obligatoire. En France, articulation avec les méthodologies de référence de la CNIL pour la recherche (MR-001 / MR-003) applicables au responsable de traitement. |
| **Hébergement** | Certification **HDS** obligatoire en France pour héberger des données de santé : choisir un hébergeur certifié. Hébergement dans l'UE, attention aux transferts hors UE et aux fournisseurs de LLM. Privilégier des modèles déployés dans l'UE, sans rétention des données. |
| **Confidentialité** | Les protocoles non publiés sont des secrets industriels : cloisonnement strict par client, pas d'entraînement de modèle sur les données client sans accord. |
| **Cybersécurité** | ISO 27001 visée à 18-24 mois ; SOC 2 pour les États-Unis ; tests d'intrusion ; chiffrement ; journalisation. |
| **Traçabilité / ALCOA+** | Piste d'audit horodatée, non modifiable : qui a validé quelle règle, à partir de quelle source, quelle alerte a été générée, quelle action a été prise. |
| **Validation des systèmes informatisés** | ICH E6(R3) (systèmes informatisés, approche par le risque), **GAMP 5 (2e éd.)**, EU GMP **Annexe 11** (en révision : vérifier la version applicable), **21 CFR Part 11** et Q&R FDA d'oct. 2024. Validation **proportionnée** : le moteur déterministe est validable de façon classique. La partie LLM est une **aide à la rédaction de règles sous validation humaine**, ce qui réduit fortement le risque de validation. |
| **IA** | Le projet de guide FDA de janv. 2025 propose un cadre de crédibilité fondé sur le risque. L'**AI Act européen** impose une qualification : le niveau de risque dépend surtout de l'éventuel statut de dispositif médical. |
| **Dispositif médical (MDR)** | **Point critique.** Un outil de conformité opérationnelle au protocole n'est *a priori* pas un dispositif médical. Mais les alertes de médicaments interdits ou l'aide à l'éligibilité peuvent s'en rapprocher. → **Analyse de qualification formelle avant commercialisation** (guide MDCG 2019-11) et formulation des alertes comme rappels de **conformité au protocole**, jamais comme recommandations thérapeutiques. |
| **GCP** | L'outil ne remplace pas la responsabilité de l'investigateur ni la supervision du promoteur. Il doit être intégré au plan de monitoring et au système qualité, et décrit dans les procédures. |

### 12.8 Risques majeurs et parades

| Risque | Probabilité | Parade |
|---|---|---|
| Règles mal extraites, donnant une fausse assurance | Élevée | Validation humaine obligatoire ; citation de la source ; indicateurs de précision publiés ; règles critiques doublement validées. |
| Saisie double, donc pas d'adoption | Élevée | Import et lecture à partir des systèmes existants ; brief envoyé par mail et dans l'eISF ; aucune obligation de nouveau portail. |
| Convergence de CRIO, Medable ou Florence | Moyenne à élevée | Vitesse ; neutralité ; donnée inter-études ; partenariats plutôt que confrontation. |
| Cycles de vente longs | Élevée | Entrée par le module amendement, payé à l'événement ; pilotes avec les CHU. |
| Requalification en dispositif médical | Moyenne | Analyse MDCG en amont ; périmètre strictement opérationnel. |
| Accès aux données de déviation inter-études | Moyenne | Clauses contractuelles de mutualisation anonymisée, avec contrepartie (benchmark offert). |

---

## 13. Réponse finale

> **« Si tu étais à ma place, avec mon expérience du métier d'ARC, quelle application créerais-tu pour bouleverser le secteur de la recherche clinique, pourquoi, et comment la transformerais-tu en entreprise rentable à fort potentiel ? »**

### Je créerais KAIROS : le moteur d'exécution du protocole, patient par patient.

**Quoi.** Un système qui transforme protocole, amendements, manuels et clarifications en **règles exécutables, versionnées et sourcées**. Il les applique à l'état réel de chaque participant pour dire, chaque matin, à l'ARC, au CRA et au chef de projet : *ce qui doit se passer, pour qui, sous quelle version, et ce qui va mal se passer si on ne fait rien*. Avec, pour chaque alerte, la phrase exacte du document qui la justifie.

**Pourquoi celle-ci et pas une autre :**
1. **Le problème est massif, documenté et coûteux** : environ 119 déviations par protocole de phase III, 3,3 amendements par protocole, environ 260 jours de versions concurrentes, et 141 k$ à 535 k$ par amendement [F]. Ce n'est pas une intuition.
2. **Le moment est unique** : ICH M11 et USDM rendent enfin le protocole structurable. L'E6(R3) exige une qualité intégrée et pilotée par le risque. Les LLM rendent l'extraction abordable. **Rien de cela n'était réuni il y a trois ans.**
3. **Les acteurs regardent ailleurs** : vers les systèmes du promoteur (Medable, Verily), vers les documents (Florence), vers la saisie (CRIO). **Le patient, au centre, dans la bonne version, reste un trou** : c'est ce que montrent mes recherches, à confirmer par des démonstrations concurrentes.
4. **Votre avantage injuste, c'est votre métier.** Les éditeurs ne savent pas ce que c'est que de préparer une C3J1 la veille d'un amendement, avec un patient sous un médicament douteux et un nouveau kit labo. Vous, si. C'est cette connaissance qui fait la différence entre un outil adopté et un 18e portail.
5. **Ce n'est pas « de l'IA »** : l'IA sert à compiler, mais c'est un **moteur déterministe validable** qui exécute. C'est à la fois plus fiable, plus défendable devant un inspecteur et plus difficile à copier par un concurrent qui se contente de brancher un chatbot.

**Comment en faire une entreprise rentable à fort potentiel :**
1. **Mois 0 à 1 : valider avant de coder.** 20 entretiens (ARC, CRA, chefs de projet, qualité), rejouer à la main 3 amendements réels, faire une démonstration des concurrents (CRIO, Florence, Medable) pour vérifier qu'ils ne font pas déjà le « diff patient ». **Si un concurrent le fait déjà bien, pivotez vers la bourse des clarifications et la mémoire d'étude, ou arrêtez.** Soyez prêt à cette conclusion.
2. **Mois 1 à 3 : MVP « diff patient + brief »** avec un associé technique (indispensable : ne sous-traitez pas le cœur du produit). Preuve sur des amendements passés.
3. **Mois 3 à 9 : deux ou trois pilotes avec des DRCI de CHU et un réseau d'oncologie**, puis une CRO moyenne. Mesurer : déviations évitées, temps gagné par amendement, satisfaction des ARC. **Ces chiffres seront votre argument de vente** ; aujourd'hui, ils n'existent pas.
4. **Monétiser là où est l'argent** : gratuit pour les utilisateurs des centres, payant pour les CRO et promoteurs (par étude et par centre, plus un module amendement à l'événement). Les centres créent l'usage, les promoteurs paient la valeur.
5. **Construire le fossé dès le premier jour** : contractualiser l'usage anonymisé des données « déviation → élément du protocole ». À 50 ou 100 études, vous possédez ce que personne n'a : **la carte des pièges des protocoles**. Elle se vend aux promoteurs **avant** qu'ils finalisent leur protocole, et c'est là que se trouve la marge et la valorisation.
6. **Financement [P]** : amorçage (BPI, French Tech Emergence, business angels HealthTech) pour environ 0,8 à 1,5 M€ jusqu'aux premiers revenus récurrents ; série A conditionnée à des pilotes convertis et au lancement américain.
7. **Ce qui vous ferait échouer** : un produit qui ajoute de la saisie ; une IA qui « décide » ; viser les grands promoteurs trop tôt ; négliger la validation GxP et la question du dispositif médical.

**En une phrase :** ne construisez pas un outil pour *ranger* ou *rechercher* le protocole. Construisez celui qui l'**exécute** à la place de la mémoire des ARC. C'est le problème que vous vivez chaque jour, et le marché ne l'a pas encore traité comme une catégorie à part.

---

## Sources

**Complexité, déviations, amendements**
- [Tufts CSDD : déviations par phase (PMC8979478)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8979478)
- [Applied Clinical Trials : quantification des déviations par phase](https://www.appliedclinicaltrialsonline.com/view/quantifying-protocol-deviation-experience-by-clinical-phase)
- [CenterWatch : rapport CSDD sur la complexité](https://centerwatch.com/articles/25921-no-end-in-sight-for-trial-complexity-csdd-report-reveals)
- [Tufts 2016 : coût des amendements (TIRS)](https://journals.sagepub.com/doi/abs/10.1177/2168479016632271)
- [Tufts 2024 : amendements (Springer TIRS)](https://link.springer.com/content/pdf/10.1007/s43441-024-00622-9.pdf)
- [ACT : inefficiences de mise en œuvre des amendements](https://www.appliedclinicaltrialsonline.com/view/shining-a-light-on-the-inefficiencies-in-amendment-implementation)
- [IntuitionLabs : données sur les amendements (source secondaire)](https://intuitionlabs.ai/articles/clinical-trial-protocol-amendments-cost-data)
- [AACI : livre blanc 2026 sur l'activation des essais](https://www.aaci-cancer.org/Files/Admin/2026-June-AACI-White-Paper-Accelerating-Clinical-Trial-Activation.pdf)
- [WCG : guide promoteur sur les amendements](https://www.wcgclinical.com/wp-content/uploads/2026/09/Sponsor-Guide-on-Protocol-Amendments-Reducing-Site-Burden_v2-1.pdf)
- [ACRP : la charge croissante des amendements (2026)](https://acrpnet.org/2026/08/11/navigating-protocol-amendments-understanding-the-growing-burden-and-charting-a-path-forward)
- [Advarra : ce que révèlent les amendements](https://www.advarra.com/blog/what-protocol-amendments-reveal-about-trial-design/)
- [IQVIA : complexité des protocoles (2026)](https://www.iqvia.com/blogs/2026/01/assessing-protocol-complexity-and-its-impact-on-trial-outcomes)
- [CASRAI : quand obtenir le consentement](https://casrai.org/guides/when-should-informed-consent-be-obtained)
- [PMC9934872 : audit des échecs de sélection](https://pmc.ncbi.nlm.nih.gov/articles/PMC9934872)

**Monitoring, centres, ressources humaines, finances**
- [Sheetz et al. 2014 : SDV (TIRS)](https://link.springer.com/article/10.1177/2168479014554400)
- [ACT : SDV et SDR](https://www.appliedclinicaltrialsonline.com/view/distinct-rbm-divisions-source-document-verification-and-source-data-review)
- [Veeva : monitoring hors ligne](https://www.veeva.com/blog/simplify-cras-return-to-sites-with-offline-monitoring/)
- [DIA Global Forum : la technologie dans les centres (2025)](https://globalforum.diaglobal.org/issue/january-2025/technology-at-clinical-sites-the-good-the-bad-and-what-sponsors-can-do-to-turn-it-around/)
- [ACRP : « Death by a thousand portals » (2026)](https://acrpnet.org/2026/08/11/death-by-a-thousand-portals-addressing-technology-fragmentation-and-site-burden-in-clinical-research)
- [ACRP : turnover des CRA (2025)](https://acrpnet.org/2025/02/14/cra-turnover-within-contract-research-organizations-post-covid-19-a-cross-sectional-study)
- [BDO : rapport rémunération et turnover des CRO](https://www.bdo.com/insights/tax/2023-2024-clinical-research-organization-compensation-turnover-insights-report)
- [PharmaVoice : tensions de recrutement](https://www.pharmavoice.com/news/clinical-trials-staffing-crunch-hiring-cra/708614/)
- [SCRS : paiement des centres](https://myscrs.org/wp-content/uploads/2024/08/Site-Payments-and-Patient-Reimbursements-Global-Perspective.pdf)
- [Clinical Leader : paiements des centres (2025)](https://www.clinicalleader.com/doc/site-payments-are-still-a-mess-but-takeda-is-trying-to-help-0001)
- [ACRP : eSource et déviations (2023)](https://acrpnet.org/2023/04/electronic-source-reduces-protocol-deviations-compared-to-paper-source-in-clinical-trials/)

**Réglementation**
- [EMA : ICH E6 (R3)](https://www.ema.europa.eu/sl/ich-e6-good-clinical-practice-scientific-guideline)
- [Sidley : finalisation de l'ICH E6(R3)](https://www.sidley.com/en/insights/newsupdates/2025/02/international-council-finalizes-modernized-global-good-clinical-practice-guideline)
- [EMA : transition vers le CTR](https://www.ema.europa.eu/en/documents/presentation/presentation-transition-clinical-trials-elena-garcia-mendez_en.pdf)
- [Cooley : Q&R FDA sur la partie 11 (2024)](https://www.cooley.com/news/insight/2024/2024-10-24-fda-finalizes-guidance-on-use-of-part-11-electronic-systems-records-and-signatures-in-clinical-investigations)
- [FDA : projet de guide sur l'IA (2025)](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/considerations-use-artificial-intelligence-support-regulatory-decision-making-drug-and-biological)
- [Clinical Leader : ICH M11 et protocoles numériques (2026)](https://www.clinicalleader.com/doc/digital-protocols-are-at-an-inflection-point-a-conversation-with-novartis-and-transcelerate-leaders-0001)

**Concurrence**
- [CRIO : eSource centralisé](https://clinicalresearch.io/products/esource/central-esource/) ; [CRIO : eSource centre](https://clinicalresearch.io/products/esource/site-esource/)
- [Medable : agent DDF](https://www.medable.com/newsroom/medable-introduces-digital-data-flow-agent-laying-the-foundation-for-end-to-end-agentic-clinical-development) ; [R&D World](https://www.rdworldonline.com/medables-digital-data-flow-agent-focuses-on-protocol-translation-as-the-agentic-race-accelerates/) ; [ACT, DIA 2026](https://www.appliedclinicaltrialsonline.com/view/2026-dia-global-annual-meeting-structured-protocols-enable-automated-amendments-real-time-fda-oversight)
- [Florence : IA agentique (DIA 2026)](https://www.prnewswire.com/news-releases/florence-healthcare-unlocks-agentic-ai-across-global-site-network-at-dia-2026-302800686.html)
- [Verily : protocoles numériques](https://verily.com/perspectives/the-role-of-ai-in-powering-digital-protocols)
- [IQVIA : du PDF à la plateforme](https://www.iqvia.com/blogs/2026/04/from-pdf-to-platform-building-an-ai-ready-clinical-trial-through-digital-protocols)
- [Faro Health : financement de 20 M$](https://www.newswire.com/news/faro-health-secures-20-million-to-scale-the-digital-transformation-of-21951519)
- [Bioxconomy : agent Medable pour les investigateurs](https://www.bioxconomy.com/clinical-and-research/medable-launches-ai-agent-to-streamline-clinical-trial-data-assessment-for-principal-investigators)
- [ConcertAI ACT](https://www.concertai.com/news/concertai-launches-accelerated-clinical-trials-leveraging-agentic-ai-to-streamline-trial-timelines)
- [IQVIA : IA et RBM (2022)](https://www.iqvia.com/ru-kz/blogs/2022/04/ai-and-rbm-is-this-the-future-of-clinical-trials)
