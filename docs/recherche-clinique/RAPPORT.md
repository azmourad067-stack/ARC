# Recherche clinique : état des lieux mondial, besoins réels, transformations et territoires d'innovation

*Livrable 1 — investigation documentaire. Version du 26 novembre 2026.*

---

## 0. Avertissement méthodologique (à lire en premier)

**Ce que ce rapport est :** une synthèse documentaire construite à partir de publications scientifiques, d'enquêtes professionnelles, de textes réglementaires et de rapports d'organismes (Tufts CSDD, ACRP, SCRS, CISCRP, EMA, FDA, ICH, Leem, TransCelerate, CDISC). Il s'appuie aussi sur la connaissance que j'ai du fonctionnement opérationnel des essais.

**Ce qu'il n'est pas :**
- **Aucun entretien n'a été conduit.** Les « réalités de terrain » décrites ici viennent de la littérature et d'enquêtes publiées, pas d'observations directes. La section 13 propose un protocole d'entretiens pour combler ce manque.
- **Pas d'accès aux bases payantes.** Je n'ai pas eu accès à PubMed (connecteur indisponible dans cette session), ni aux rapports intégraux de Tufts, IQVIA ou Citeline, ni aux forums (Reddit, LinkedIn) en lecture directe. Les verbatims de forums ne sont donc pas cités. Je décris seulement les thèmes que l'on y retrouve habituellement, avec un niveau de confiance **faible**.
- **Chiffres secondaires signalés.** Quand un chiffre provient d'une source secondaire (presse spécialisée, blog d'éditeur), il est marqué **[secondaire]**. Il doit être vérifié dans la source primaire avant tout usage public.

**Niveaux de confiance utilisés :**
- **Élevé** : publication à comité de lecture, texte réglementaire, ou enquête large et reproduite.
- **Moyen** : enquête professionnelle d'un seul organisme, ou source secondaire cohérente avec d'autres.
- **Faible** : source éditeur ou commerciale, échantillon réduit, extrapolation ou interprétation de ma part.

**Biais connus des sources :**
- Beaucoup d'enquêtes « sites » sont financées ou co-réalisées par des éditeurs (Greenphire, Advarra, Florence, Oracle, Medidata), qui ont intérêt à documenter le problème qu'ils vendent.
- Les données de Tufts CSDD viennent majoritairement de grands promoteurs industriels. Elles sous-représentent la recherche académique.
- Les données américaines dominent ; les données françaises sont rares et surtout industrielles (Leem).

---

## 1. Synthèse exécutive

1. **La recherche clinique est un système de coordination, pas seulement un système scientifique.** Un essai de phase III mobilise typiquement un promoteur, une ou plusieurs CRO, des dizaines à des centaines de centres, des comités d'éthique et des autorités, des fournisseurs technologiques et des patients. La majorité des retards et des coûts naissent aux **interfaces** entre ces acteurs, plutôt qu'à l'intérieur d'un métier.

2. **La complexité des protocoles augmente plus vite que la capacité des centres.** Entre 2016 et 2021, les essais de phase III ont connu environ +37 % de critères d'évaluation et +42 % de procédures **[secondaire, Tufts CSDD 2023]** ([Applied Clinical Trials](https://appliedclinicaltrialsonline.com/view/rising-clinical-trial-complexity-continues-vex-drug-developers)). En parallèle, 76 % des protocoles ont au moins un amendement (57 % auparavant), avec une moyenne de 3,3 amendements par protocole ([Tufts/TIRS 2024](https://link.springer.com/content/pdf/10.1007/s43441-024-00622-9.pdf)). Confiance : **élevée**.

3. **Le centre investigateur absorbe la complexité sans être rémunéré pour elle.** Les sites jonglent avec de multiples plateformes imposées par chaque promoteur : selon une enquête éditeur, près de 70 % des répondants ont au moins 6 identifiants par étude **[secondaire, Advarra 2023]**. Les paiements arrivent en retard : 82 % des sites se disent pénalisés ([Greenphire 2022, via SCRS](https://myscrs.org/wp-content/uploads/2024/08/Site-Payments-and-Patient-Reimbursements-Global-Perspective.pdf)). Plus de 40 % des sites signalent une pénurie de personnel ([Advarra 2025](https://resource.advarra.com/hubfs/eBook/Advarra%20Workforce%20Development%20Survey%20Report%20EB.pdf)). Confiance : **moyenne** (enquêtes d'éditeurs, mais résultats convergents).

4. **Le recrutement échoue surtout pour des raisons structurelles, pas motivationnelles.** En oncologie, plus de la moitié des patients n'ont tout simplement **aucun essai disponible** dans leur centre ([Unger et al., JNCI 2019](https://doi.org/10.1093/jnci/djy221)). Environ 11 % des centres activés n'incluent aucun patient, et 37 % n'atteignent pas leur objectif ([Tufts CSDD, 2012](https://www.clinician.com/articles/62939-patient-recruitment-and-retention-rates-struggle)). Confiance : **élevée** pour l'oncologie, **moyenne** ailleurs (données anciennes).

5. **Une part importante du travail de contrôle a une faible valeur démontrée.** Seulement 1,1 % des données saisies dans les eCRF sont corrigées à la suite de la vérification des données sources (SDV) ([Sheetz et al., TIRS 2014](https://link.springer.com/article/10.1177/2168479014554400)). Ce constat est contesté : la sensibilité de la SDV n'est pas mesurée ([revue de portée, 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11639101/)). Confiance : **moyenne**.

6. **Le cadre réglementaire bascule vers la proportionnalité au risque.** ICH E6(R3) a été adopté le 6 janvier 2025 et s'applique dans l'UE depuis le 23 juillet 2025 ; l'annexe 2 entrera en vigueur le 15 janvier 2027 ([EMA](https://www.ema.europa.eu/fr/ich-e6-good-clinical-practice-scientific-guideline)). ICH M11 (protocole structuré) a été adopté en novembre 2025 ([EMA](https://www.ema.europa.eu/en/documents/regulatory-procedural-guideline/ich-m11-clinical-electronic-structured-harmonised-protocol-cesharp-technical-specification-step-5_en.pdf)). La réglementation **autorise** désormais des façons de travailler que les outils et les organisations n'ont pas encore rattrapées. Confiance : **élevée**.

7. **Le temps est la variable économique dominante.** Selon Tufts, un jour de retard coûte environ 40 000 $ en coûts directs, jusqu'à environ 55 700 $ en phase III, et environ 500 000 $ de ventes différées ([Smith, DiMasi, Getz, TIRS 2024](https://csdd.tufts.edu/sites/default/files/2025-02/Aug2024%20Day%20of%20Delay%20White%20Paper%20Final.pdf)). Ce chiffre est critiqué, car il surestimerait la perte réelle. Confiance : **moyenne**.

8. **L'Europe et la France cherchent à regagner leur attractivité.** En France, il fallait 160 jours médians pour inclure un premier patient en 2022 : 87 jours d'ANSM + CPP, 79 jours de convention, 27 jours de mise en place et 36 jours jusqu'à la première inclusion ([Leem, 13ᵉ enquête](https://www.leem.org/sites/default/files/2024-01/CP_ENQUETE_ATTRACTIVITE%20-%20vF.pdf)). L'UE vise 66 % d'essais recrutant dans les 200 jours, contre 50 % aujourd'hui ([EMA](https://www.ema.europa.eu/fr/news/new-targets-clinical-trials-europe)). Confiance : **élevée**.

**Thèse centrale (interprétation, confiance moyenne) :** le secteur investit massivement dans des outils *par fonction* (EDC, eTMF, CTMS…), mais le coût se situe *entre les fonctions et entre les organisations*. Il se situe aussi dans une connaissance tacite que personne ne capitalise. Les territoires d'innovation les plus prometteurs se trouvent dans ces interstices (§ 11).

---

## 2. Cartographie de l'écosystème

### 2.1 Les grands types de recherche

| Dimension | Catégories | Remarques opérationnelles |
|---|---|---|
| Phase | I (tolérance, PK), II (preuve de concept, dose), III (confirmatoire), IV (post-AMM) | Les phases I et III concentrent la hausse des amendements ([Tufts 2024](https://link.springer.com/content/pdf/10.1007/s43441-024-00622-9.pdf)) |
| Nature | Interventionnelle / observationnelle | En France, la loi Jardé distingue les catégories RIPH 1, 2 et 3, avec des circuits CPP/ANSM différents |
| Promoteur | Industriel / académique (CHU, groupes coopérateurs, Unicancer…) | Les académiques ont moins de moyens et plus de contraintes de financement (PHRC, appels à projets) |
| Géographie | Monocentrique, multicentrique national, international | Le règlement UE 536/2014 impose un dossier unique via CTIS |
| Modalité | Sur site, hybride, décentralisée (DCT) | L'adoption des DCT a reculé après le pic COVID, mais reste supérieure à 2020 ([Clinical Trials Arena](https://www.clinicaltrialsarena.com/features/dct-adoption-tracker-who-and-what-is-at-the-crest-of-the-trial-decentralisation-wave/)) |
| Design | Classique, adaptatif, plateforme, panier, parapluie, pragmatique, essais emboîtés dans les registres | Ces designs complexifient les opérations : multiples bras et amendements fréquents |
| Données | Données d'essai, données de vie réelle (RWD/RWE), bras de contrôle externes | En Europe, l'EHDS (règlement UE 2025/327) organise l'usage secondaire des données de santé |

### 2.2 Schéma des flux entre acteurs

```
                     ┌──────────────────────────┐
                     │  Autorités & éthique      │
                     │ ANSM · EMA/CTIS · FDA     │
                     │ CPP / IRB / EC            │
                     └──────────▲───────────────┘
                     dossiers · │ · avis, RFI, inspections
                                │
┌───────────────┐   contrat  ┌──┴─────────────┐   délégation   ┌───────────────┐
│ Financeurs     ├──────────▶│   PROMOTEUR     ├──────────────▶│     CRO        │
│ (PHRC, ANR,    │           │ industriel/acad.│               │ (CRA, PM, DM,  │
│  industriels)  │           └──┬──────────▲───┘               │  safety, RA)   │
└───────────────┘   protocole, │          │ données, SAE,      └──┬─────────▲───┘
                    budget,    │          │ déviations            │ monitoring
                    outils     ▼          │                       ▼         │
┌───────────────────────────────────────────────────────────────────────────────┐
│                         CENTRE INVESTIGATEUR                                   │
│ Investigateur principal · co-investigateurs · ARC/CRC · IRC/IDE recherche      │
│ Pharmacie (PUI) · laboratoire · imagerie · DRCI/admin · services cliniques      │
└───────────▲────────────────────────────────────────────────▲──────────────────┘
            │ consentement, visites, ePRO                     │ adressage
       ┌────┴─────┐                                      ┌────┴─────────────┐
       │ PATIENTS │◀────── information, confiance ───────│ Médecins traitants│
       │ & aidants│◀────── soutien ──── Associations      │ / adresseurs      │
       └──────────┘                                      └──────────────────┘
        Fournisseurs technologiques (EDC, IRT, eCOA, eTMF, labos centraux, imagerie)
        transversaux à tous les niveaux → multiplication des interfaces
```

**Lecture :** chaque flèche correspond à un échange d'information, souvent un e-mail, un PDF, un portail ou un tableur. **Personne n'est propriétaire de la vue de bout en bout** du point de vue du centre (interprétation, confiance moyenne).

### 2.3 Évolutions réglementaires structurantes

| Texte | Statut | Effet attendu sur le terrain | Source |
|---|---|---|---|
| ICH E6(R3) GCP | Adopté le 06/01/2025 ; UE : principes + annexe 1 applicables le 23/07/2025 ; annexe 2 (designs pragmatiques, DCT, RWD) applicable le 15/01/2027 | Qualité intégrée dès la conception (*quality by design*), proportionnalité, facteurs critiques pour la qualité, plus grande ouverture aux designs et outils numériques | [EMA](https://www.ema.europa.eu/fr/ich-e6-good-clinical-practice-scientific-guideline), [CITI](https://about.citiprogram.org/blog/ich-releases-final-version-of-e6r3-good-clinical-practice-guideline/) |
| ICH M11 (CeSHarP) | Step 4 en novembre 2025 ; UE : effet au 11/06/2026 | Protocole **structuré et lisible par machine** | [EMA](https://www.ema.europa.eu/en/documents/regulatory-procedural-guideline/ich-m11-clinical-electronic-structured-harmonised-protocol-cesharp-technical-specification-step-5_en.pdf), [FDA](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/m11-technical-specification-clinical-electronic-structured-harmonised-protocol) |
| CDISC USDM (Digital Data Flow) | v4 ; M11 est un sous-ensemble de USDM | Permet en théorie d'automatiser la configuration de l'EDC, du calendrier des visites et du budget à partir du protocole | [FDA/DDF](https://www.fda.gov/media/164112/download), [HL7 Vulcan](https://hl7.org/fhir/uv/pharmaceutical-research-protocol/2025Sep/06-info-models.html) |
| Règlement UE 536/2014 + CTIS | Transition achevée le 30/01/2025 ; 5 088 essais migrés | Dossier unique, mais l'industrie juge CTIS perfectible et note des RFI non synchronisées entre parties I et II | [RAPS](https://www.raps.org/resource/eu-regulators-set-targets-to-promote-european-clin.html), [EMA](https://www.ema.europa.eu/fr/news/new-targets-clinical-trials-europe) |
| Objectifs ACT EU | +500 essais multinationaux sur 5 ans ; 66 % des essais recrutant en ≤ 200 jours | Pression sur les délais de mise en place | [EMA](https://www.ema.europa.eu/fr/news/new-targets-clinical-trials-europe) |
| FDA – IA et décisions réglementaires (projet) | Projet du 06/01/2025, cadre de crédibilité fondé sur le contexte d'usage | Exclut l'IA purement opérationnelle sans impact sur la sécurité ou la fiabilité des résultats, ce qui laisse beaucoup de latitude aux usages opérationnels | [FDA](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/considerations-use-artificial-intelligence-support-regulatory-decision-making-drug-and-biological), [DLA Piper](https://dlapiper.com/insights/publications/2025/01/fda-releases-draft-guidance-on-use-of-ai) |
| FDA – plans d'action diversité (FDORA) | Projet retiré en janvier 2025, puis rétabli sur décision de justice ; obligation légale toujours en vigueur ; statut final non confirmé | Incertitude pour les promoteurs sur les obligations de représentativité | [AgencyIQ](https://www.agencyiq.com/blog/fda-pulls-diversity-action-plan-guidance-other-diversity-programs-after-executive-order/), [DLA Piper](https://dlapiper.com/insights/publications/2025/01/fda-actions-addressing-diversity-in-clinical-trials), [RAPS](https://www.raps.org/resource/fda-reissues-sex-specific-data-guidance-after-sani.html) |
| AI Act (UE 2024/1689) | Application progressive 2025–2027 | Certains usages médicaux sont classés à haut risque ; l'IA purement opérationnelle est moins concernée (interprétation) | EUR-Lex |

**Constat (confiance élevée) :** l'ensemble ICH E6(R3) + M11 + USDM forme un changement de paradigme. On passe du « document » à la « donnée », et du « tout contrôler » au « contrôler ce qui compte ». Mais leur mise en œuvre dépend d'outils et de pratiques qui ne sont pas encore en place.

---

## 3. Cartographie du parcours d'un essai (15 étapes)

Légende des difficultés : ● majeure · ◐ notable · ○ mineure (appréciation qualitative de ma part, confiance moyenne).

| # | Étape | Acteurs principaux | Échanges / outils typiques | Dépendances | Difficultés documentées |
|---|---|---|---|---|---|
| 1 | Conception scientifique | Promoteur (clinique, médical, biostat), KOL, parfois associations de patients | Revues de littérature, avis scientifiques (EMA/FDA), données RWD | Stratégie produit, données précliniques | ◐ Faible prise en compte de la faisabilité terrain ; procédures « non-core » ajoutées (18,6 % du coût direct en phase III selon Tufts 2012, [National Academies](https://www.nationalacademies.org/read/18400/chapter/5)) |
| 2 | Rédaction du protocole | Medical writers, biostat, opérations, réglementaire | Word, modèles internes, de plus en plus des outils d'aide à la rédaction | Étape 1 | ● Complexité croissante, amendements évitables : 76 % des protocoles amendés ([Tufts 2024](https://link.springer.com/content/pdf/10.1007/s43441-024-00622-9.pdf)) |
| 3 | Sélection des centres | Promoteur/CRO (feasibility, start-up), investigateurs | Questionnaires de faisabilité, historiques internes, bases de données de sites | Étape 2 | ● Questionnaires répétitifs et déclaratifs, surestimation du potentiel de recrutement (11 % de centres à zéro inclusion) |
| 4 | Faisabilité | Investigateur, ARC/CRC, pharmacie, plateaux techniques | Questionnaires, CDA, visites de sélection (PSV/SQV) | Étape 3 | ◐ Estimation souvent « au doigt mouillé », peu d'accès outillé aux données de patients éligibles |
| 5 | Contrats et budgets | Juristes, DRCI/direction, promoteur/CRO, investigateur | Convention unique (France), grilles de surcoûts, négociation par e-mail | Étapes 3–4 | ● 79 jours médians en France ([Leem](https://www.leem.org/sites/default/files/2024-01/CP_ENQUETE_ATTRACTIVITE%20-%20vF.pdf)) ; budgets décorrélés de la charge réelle |
| 6 | Soumissions réglementaires et éthiques | Affaires réglementaires, CPP/EC, ANSM/EMA/FDA | CTIS (UE), SIRIPH2G (CPP France), IRB central (US) | Étape 2 | ◐ 87 jours ANSM + CPP (France, 2022) ; RFI non synchronisées ([RAPS](https://www.raps.org/resource/eu-regulators-set-targets-to-promote-european-clin.html)) |
| 7 | Mise en place (SIV) | CRA, ARC/CRC, IRC, pharmacie, labo | Formations multiples, accès aux plateformes, classeur investigateur / eISF, matériel | Étapes 5–6 | ● Formations redondantes (GCP répétée par étude) ; multiplication des identifiants ([SCRS](https://myscrs.org/resources/reducing-site-technology-burdens/)) |
| 8 | Recrutement | Investigateur, CRC, médecins adresseurs, plateformes | Requêtes manuelles du DPI, RCP, registres, annonces | Étape 7 | ● Absence d'essai adapté et inéligibilité ; dépendance à la mémoire de l'investigateur |
| 9 | Inclusion et suivi | IRC/CRC, investigateur, patient | eConsent/papier, IRT/RTSM, ePRO, agendas des visites | Étape 8 | ● Fenêtres de visite complexes, charge pour le patient, abandons (~30 % selon des sources secondaires de qualité variable) |
| 10 | Gestion des données | CRC (saisie), data managers | EDC, requêtes, codage, réconciliation labos et données externes | Étape 9 | ● Double saisie DPI → EDC : 86 % des points de données seraient transférables, 43 % via FHIR ([Sanofi/Flatiron, AMIA 2025](https://resources.flatiron.com/publications/optimizing-data-collection-assessing-ehr-to-edc-data-transfer-potential-across-structured-and-unstructured-data)) |
| 11 | Monitoring | CRA, CTM, central monitoring | Visites sur site/à distance, SDV/SDR, rapports, lettres de suivi, RBQM | Étape 10 | ◐ SDV peu productive (1,1 %), rapports de visite chronophages, rotation des CRA |
| 12 | Événements indésirables (AE/SAE) | Investigateur, CRC, pharmacovigilance, medical monitor | Formulaires SAE, base safety (Argus, ArisG…), SUSAR, DSUR | Étape 9 | ◐ Délais de déclaration de 24 h, double saisie EDC + formulaire SAE, réconciliation |
| 13 | Déviations | CRA, CRC, QA, investigateur | Logs de déviations, CTMS, CAPA | Étapes 9–11 | ◐ Découverte tardive (lors de la visite de monitoring) ; classification hétérogène entre promoteurs |
| 14 | Clôture des centres | CRA, ARC, pharmacie, archives | Réconciliation des produits, archivage du TMF/ISF, dernier paiement | Étapes 10–13 | ○/◐ Paiements de fin d'étude tardifs, archivage long (25 ans selon le CTR) |
| 15 | Analyse et valorisation | Biostat, medical writing, investigateurs | CSR, publication, résumé laïc (obligatoire dans l'UE), retour aux participants | Étape 10 | ◐ Retour d'information aux patients et aux centres rare ou tardif |

**Constat transversal (confiance moyenne) :** les étapes 3–7 (*study start-up*) et 9–11 (exécution) concentrent les irritants. La rupture la plus coûteuse est **2 → 7** : le protocole est conçu sans modèle de la charge de travail du centre qui va l'exécuter.

---

## 4. Analyse des métiers

> Sources principales : enquêtes ACRP ([workforce survey 2025](https://acrpnet.org/2025/09/24/acrp-publishes-results-from-first-ever-national-workforce-survey), [Voices from the Frontlines](https://acrpnet.org/insights/white-papers/voices-from-the-frontlines)), SCRS, Advarra, BDO, et littérature sur la rotation des professionnels de recherche clinique ([J Clin Transl Sci](https://www.cambridge.org/core/journals/journal-of-clinical-and-translational-science/article/trends-in-turnover-and-turbulence-at-a-large-academic-medical-center-before-and-during-covid19-analyzing-structured-clinical-research-professional-roles/4FCD004C1E699BA332939609FD5A1BA4)). Les colonnes « informel » et « information manquante » relèvent en grande partie de **mon interprétation** (confiance moyenne à faible) et sont à valider en entretien.

### 4.1 Professionnels de terrain

#### ARC / CRA (moniteur, côté promoteur ou CRO)
- **Rôle officiel :** vérifier la protection des participants, l'intégrité des données et le respect du protocole et des BPC au sein des centres.
- **Rôle réel :** il est le **routeur humain** entre le promoteur et le centre. Il traduit les exigences du promoteur, relance les centres, forme le personnel, rassure l'équipe, diagnostique les causes de non-recrutement et sert de mémoire de l'étude pour le centre.
- **Quotidien :** préparation et rédaction des rapports de visite, SDV/SDR, suivi des requêtes, relances par e-mail, mise à jour du CTMS, collecte de documents réglementaires pour l'eTMF, déplacements.
- **Activités chronophages :** rédaction des rapports de visite et des lettres de suivi, relances, réconciliations, recherche de documents (interprétation, confiance moyenne).
- **Difficultés :** portefeuille de centres élevé, rotation importante (taux médian de 22 % en 2024 contre 30 % en 2022 dans les CRO, [BDO](https://bdo.com/insights/tax/key-findings-from-bdos-2024-clinical-research-organization-global-compensation-turnover-survey)), rémunération et charge de travail comme moteurs de départ ([ACRP 2025](https://acrpnet.org/2025/02/14/cra-turnover-within-contract-research-organizations-post-covid-19-a-cross-sectional-study)).
- **Information manquante :** l'état réel du centre entre deux visites, la charge du personnel du centre, l'historique des échanges avec ses prédécesseurs.
- **Conséquences :** chaque changement de CRA fait perdre au centre le contexte accumulé, ce qui oblige à réexpliquer et à reformer, et peut faire baisser la qualité.

#### ARC investigateur / CRC (coordinateur, côté centre)
- **Rôle réel :** il est le **chef d'orchestre opérationnel** de l'étude au centre. Il planifie les visites, gère les échantillons, saisit les données dans l'EDC, répond aux requêtes, tient l'ISF, assure l'interface avec la pharmacie et le labo, s'occupe des remboursements des patients et soutient souvent l'investigateur pour le consentement.
- **Informel :** il garde la mémoire des particularités de chaque protocole, sert de soutien psychologique aux patients, et contourne les outils (tableurs personnels, agendas papier, post-it).
- **Chronophage :** saisie en double (DPI → EDC), formations par étude, multiples identifiants (6 ou plus par étude pour une majorité, **[secondaire]**), réponses aux requêtes.
- **Information manquante :** une vue consolidée de toutes ses études (visites à venir, fenêtres, échéances), et des réponses rapides aux questions de protocole.
- **Conséquences :** déviations par oubli de fenêtres, épuisement professionnel, dépendance du centre aux personnes expérimentées.

#### Infirmier·ère de recherche clinique (IRC)
- Réalise les actes de l'étude (prélèvements, administration, surveillance), est souvent au premier plan pour le consentement et l'éducation des patients, et gère la logistique des kits.
- **Difficulté :** tension entre la charge de soins et la charge de recherche ; actes spécifiques au protocole différents des pratiques habituelles.

#### Technicien·ne d'études cliniques (TEC — France)
- Profil proche du CRC, souvent sous contrat court financé par l'étude, ce qui crée une forte précarité et donc une forte rotation (interprétation, confiance moyenne, cohérent avec la littérature sur la rotation dans les CHU).

#### Investigateur / médecin chercheur
- **Officiel :** il porte la responsabilité médicale et légale (supervision, délégation, éligibilité, AE/SAE, consentement).
- **Réel :** il a un temps de recherche contraint par l'activité de soins, un rôle de « porte d'entrée » du recrutement (il doit *penser* à l'essai lors de la consultation), et il signe un volume important de documents.
- **Information manquante :** au moment de la consultation, quels essais ouverts correspondent à ce patient ?
- **Conséquences :** des patients éligibles ne sont jamais proposés ; la non-proposition d'un essai disponible est une barrière documentée en oncologie ([Unger 2019](https://doi.org/10.1093/jnci/djy221)).

#### Pharmacien·ne hospitalier·ère (PUI, essais cliniques)
- Gère la réception, le stockage (chaîne du froid), la dispensation et la comptabilité des produits expérimentaux, l'interface avec l'IRT/RTSM et la destruction.
- **Difficulté :** chaque promoteur a son propre IRT, ses formulaires, ses relevés de température et ses procédures d'excursion de température. Le temps pharmaceutique est souvent sous-valorisé dans les budgets (confiance moyenne).

### 4.2 Pilotage et management

| Rôle | Mission réelle | Douleurs principales | Information manquante |
|---|---|---|---|
| Clinical Trial / Project Manager | Tenir le délai, le budget et la qualité sur un ensemble de pays et de centres | Indicateurs en retard sur la réalité, consolidation manuelle de rapports multiples | Un signal précoce sur les centres qui vont décrocher |
| Clinical Operations Manager | Allouer les ressources entre études | Planification de capacité à l'aveugle, rotation | Charge réelle par personne |
| Study Start-up Specialist | Faire passer les centres de « sélectionné » à « activé » | Suivi de dizaines de documents par centre, relances | Où chaque centre est bloqué et pourquoi |
| Data Manager | Construire l'EDC, nettoyer les données | Construction de base à partir d'un protocole en Word, nombreux amendements, réconciliation de données externes | Protocole structuré (→ M11/USDM) |
| Medical Monitor | Revue médicale, éligibilité, sécurité | Volume de questions des centres, revue manuelle des listings | Synthèse patient longitudinale |
| Qualité (QA) | Audits, CAPA, préparation aux inspections | Découverte tardive des problèmes systémiques | Analyse transversale des déviations entre études |
| Affaires réglementaires | Soumissions, réponses aux RFI, amendements | Divergences nationales, CTIS, version des documents | Prévisibilité des questions des évaluateurs |

### 4.3 Structures

| Structure | Logique dominante | Tension principale |
|---|---|---|
| CHU / DRCI (France) | Mission publique, recherche académique et industrielle, valorisation (SIGAPS/SIGREC) | Personnel sous contrats précaires, outils hétérogènes, délais de convention |
| Centres privés / site networks / SMO | Rentabilité par étude, vitesse | Trésorerie : en 2018, 64 % des sites avaient moins de 3 mois de trésorerie (SCRS) ; paiements en retard ([SCRS/Greenphire](https://myscrs.org/wp-content/uploads/2024/08/Site-Payments-and-Patient-Reimbursements-Global-Perspective.pdf)) |
| Promoteur industriel | Délai de mise sur le marché, conformité | Coût de l'amendement : 141 k$ (phase II) à 535 k$ (phase III) en coût direct médian (Tufts, étude antérieure) |
| Promoteur académique | Question scientifique, financement par appels à projets | Faibles ressources opérationnelles, outillage limité |
| CRO | Exécution externalisée, marge | Rotation des CRA, standardisation contre spécificités des promoteurs |
| Réseaux (F-CRIN, Unicancer, groupes coopérateurs, ECRIN) | Mutualisation | Hétérogénéité des centres membres |

### 4.4 Institutions
- **ANSM / CPP / EMA / FDA** : leur charge d'évaluation augmente ; ils cherchent la convergence (ACT EU). Les CPP français sont tirés au sort et ont une charge variable, ce qui produit une hétérogénéité perçue des avis (confiance faible, littérature grise).
- **Financeurs** (DGOS/PHRC, ANR, Horizon Europe, NIH) : ils exigent de plus en plus le partage des données (FAIR), mais financent rarement l'infrastructure opérationnelle (interprétation).

---

## 5. Frustrations et difficultés : analyse par problème

Pour chaque problème : fréquence · population · causes · conséquences · solutions actuelles · limites · coût.

### P1. Complexité des protocoles et amendements
- **Fréquence :** quasi universelle ; 76 % des protocoles amendés, 3,3 amendements en moyenne ([Tufts 2024](https://link.springer.com/content/pdf/10.1007/s43441-024-00622-9.pdf)). **Confiance : élevée.**
- **Populations :** tous, mais surtout les centres.
- **Causes :** ajout d'objectifs exploratoires, exigences multi-pays, conception déconnectée de la faisabilité, pression pour « tout collecter » car un essai coûte cher.
- **Conséquences :** environ 260 jours entre l'identification du besoin et l'approbation finale de l'amendement, et environ 215 jours de coexistence de versions entre centres **[secondaire, non vérifié]**. S'y ajoutent les reformations, les reconfigurations de l'EDC et les déviations liées à des versions différentes.
- **Solutions actuelles :** revue de faisabilité par des panels de centres ou de patients, benchmarks de complexité (scores de complexité), outils de « protocol optimization » (Medidata, ICON…), M11/USDM.
- **Limites :** la revue de faisabilité arrive tard et reste peu quantifiée ; la charge de travail du *centre* n'est pas modélisée.
- **Coût :** 141 k$ à 535 k$ en coût direct médian par amendement substantiel (Tufts, étude antérieure), hors coûts d'opportunité.

### P2. Lenteur de la mise en place des études (*study start-up*)
- **Fréquence :** élevée ; en France, 160 jours médians jusqu'à la première inclusion (2022) ; dans l'UE, seulement 50 % des essais recrutent en ≤ 200 jours. **Confiance : élevée.**
- **Causes :** processus séquentiels (contrat → éthique → SIV), versions de documents multiples, négociations budgétaires sans référentiel commun, dépendance à des interlocuteurs surchargés.
- **Solutions :** convention unique (France), modèles de contrats, eReg, plateformes de start-up (Veeva Site Connect, Florence, WCG…), Fast Track national.
- **Limites :** les outils suivent l'avancement mais **ne parallélisent pas** le travail ; aucune visibilité partagée centre ↔ promoteur sur le « où ça bloque ».
- **Coût :** environ 40 000 $ par jour en coûts directs (Tufts 2024, discuté).

### P3. Recrutement et éligibilité
- **Fréquence :** très élevée. En oncologie aux États-Unis, 55,6 % des patients n'ont pas d'essai disponible, 21,5 % sont inéligibles et environ 8 % participent ([Unger 2019](https://doi.org/10.1093/jnci/djy221)). Environ 11 % des centres n'incluent aucun patient, 37 % en incluent moins que prévu ([Tufts 2012](https://www.clinician.com/articles/62939-patient-recruitment-and-retention-rates-struggle)). **Confiance : élevée** (oncologie), **moyenne** (autres domaines, données anciennes).
- **Causes :** critères d'éligibilité restrictifs, essais non disponibles là où sont les patients, pas de détection automatique dans le DPI, investigateurs qui ne pensent pas à l'essai, fuite du « dernier kilomètre » entre pré-sélection et inclusion ([DIA Global Forum 2024](https://globalforum.diaglobal.org/issue/september-2024/documenting-the-last-mile-leak-in-the-patient-recruitment-pipeline/)).
- **Solutions :** pré-screening sur EHR (TriNetX, Deep 6 AI, InSite/TriNetX en Europe), plateformes patients (Antidote, Clara Health…), registres et annuaires (ClinicalTrials.gov, CTIS public, Clinicaltrials.eu, en France l'outil de l'INCa).
- **Limites :** l'interopérabilité DPI reste partielle ; le texte libre est mal exploité ; le dernier kilomètre est humain (temps du CRC et du médecin pour contacter, expliquer, planifier) ; les populations sous-représentées restent difficiles à atteindre.
- **Coût :** la littérature indique qu'une part importante des arrêts d'essais est due à un recrutement insuffisant (environ 19 % des essais arrêtés pour ce motif selon [Carlisle et al., Clin Trials 2015](https://doi.org/10.1177/1740774514558307) ; confiance moyenne, à vérifier).

### P4. Rétention et pertes de suivi
- **Fréquence :** un taux d'abandon d'environ 30 % est souvent avancé, mais ce chiffre provient de **sources secondaires de qualité variable** (blogs d'éditeurs). **Confiance : faible.** La dépendance à la distance est documentée de façon ponctuelle (−10 % de rétention par tranche de 30 miles dans un essai génomique, **[secondaire]**).
- **Causes :** charge des visites, transports, coûts avancés, perte de lien avec l'équipe, absence de retour d'information, effets indésirables.
- **Solutions :** éléments décentralisés, remboursements rapides (Greenphire, Scout), applications patients.
- **Limites :** les données de rétention sont peu publiées par phase et par domaine. **Donnée manquante majeure.**

### P5. Prolifération des plateformes et surcharge technologique
- **Fréquence :** élevée. En 2026, 50 % des sites se connectent à au moins 5 systèmes par étude **[secondaire, enquête éditeur]**. L'enquête SCRS 2026 indiquerait que seulement 10,8 % des sites utilisent moins de 5 systèmes, et que 71 % consacrent au moins 11 h par mois et par personne aux formations **[secondaire, non vérifié dans la source]** ([Applied Clinical Trials, oct. 2026](https://www.appliedclinicaltrialsonline.com/view/2026-scrs-causes-technology-adoption-stall-)). L'insatisfaction est déjà documentée en 2019 ([SCRS/Oracle 2019](https://oracle.com/co/a/ocom/docs/dc/em/scrs_research-report_09oct2019_final.pdf)). **Confiance : moyenne.**
- **Cause profonde :** le **promoteur choisit les outils, le centre les subit**. Chaque promoteur optimise sa propre pile, et le coût d'intégration est transféré au centre (asymétrie de pouvoir).
- **Solutions :** SSO, portails de centre unifiés (Veeva SiteVault, Florence, Clinical Research IO, Advarra), initiatives SCRS.
- **Limites :** l'unification reste partielle et dépend des promoteurs ; les portails ajoutent souvent une couche de plus.

### P6. Double saisie et transcription
- **Fréquence :** structurelle dans tous les centres qui utilisent un EDC. Une étude Sanofi/Flatiron sur 5 essais en oncologie estime que 86 % des points de données sont éligibles à un transfert EHR → EDC ([AMIA 2025](https://resources.flatiron.com/publications/optimizing-data-collection-assessing-ehr-to-edc-data-transfer-potential-across-structured-and-unstructured-data)). **Confiance : moyenne** (une seule étude, contexte américain, données oncologiques).
- **Limites des solutions :** il faut une intégration par DPI et par centre, une gouvernance hospitalière, et une validation. Le texte libre (comptes rendus) reste majoritairement inexploité. Le déploiement reste pilote.

### P7. Monitoring, SDV et rapports
- **Constat :** la SDV corrige 1,1 % des données ; seulement 2,4 % des requêtes portent sur des données critiques et sont issues de la SDV ([Sheetz 2014](https://link.springer.com/article/10.1177/2168479014554400)). Contre-argument : sa sensibilité n'est pas mesurée ([revue 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11639101/)). **Confiance : moyenne.**
- **Réalité de terrain (interprétation) :** malgré le RBQM, de nombreuses organisations conservent une SDV étendue par aversion au risque d'inspection. Les rapports de visite restent rédigés à la main, et le monitoring central produit des alertes que le CRA doit ensuite « traduire » pour le centre.

### P8. Déviations
- **Constat (interprétation, confiance moyenne) :** les déviations sont découvertes a posteriori lors du monitoring. Leur classification varie entre promoteurs, et l'analyse des causes racines reste superficielle (« erreur humaine, re-formation »). Les mêmes déviations se répètent d'une étude à l'autre sans capitalisation.
- **Donnée manquante :** il n'existe pas de statistique publique robuste de fréquence des déviations par type et par phase.

### P9. Événements indésirables
- **Constat :** les délais réglementaires sont stricts (24 h pour un SAE), avec une double documentation (EDC + formulaire SAE + base safety) et une réconciliation périodique (pratique standard, confiance élevée). Les centres reçoivent de très nombreux rapports SUSAR à lire, avec une faible valeur perçue (confiance moyenne).

### P10. Charge mentale, rotation et formation
- Plus de 40 % des sites sont en pénurie de personnel ([Advarra 2025](https://resource.advarra.com/hubfs/eBook/Advarra%20Workforce%20Development%20Survey%20Report%20EB.pdf)). La rotation des CRA est élevée ([BDO 2024](https://bdo.com/insights/tax/key-findings-from-bdos-2024-clinical-research-organization-global-compensation-turnover-survey)), de même que celle des professionnels de recherche dans les centres académiques ([JCTS](https://www.cambridge.org/core/journals/journal-of-clinical-and-translational-science/article/trends-in-turnover-and-turbulence-at-a-large-academic-medical-center-before-and-during-covid19-analyzing-structured-clinical-research-professional-roles/4FCD004C1E699BA332939609FD5A1BA4)). **Confiance : moyenne.**
- **Formation :** les GCP sont répétées par promoteur, malgré les initiatives de reconnaissance mutuelle (TransCelerate GCP Mutual Recognition).
- **Transmission des connaissances :** l'onboarding d'un nouveau CRC se fait par compagnonnage. Aucune trace structurée des « astuces » par protocole, par promoteur ou par outil (interprétation, à valider).

### P11. Paiements et budgets
- 82 % des sites se disent pénalisés par les retards de paiement ; 23 % rapportent des retards de 90 jours ou plus ; 60 % suivent leurs créances sur papier ou tableur ([SCRS/Greenphire](https://myscrs.org/wp-content/uploads/2024/08/Site-Payments-and-Patient-Reimbursements-Global-Perspective.pdf)). Les données datent de 2016–2022. **Confiance : moyenne.**
- **Cause :** les éléments facturables dépendent de l'état des données (visites saisies, requêtes fermées) et d'annexes budgétaires non structurées.

### P12. Collaboration centre ↔ promoteur
- **Asymétrie (interprétation, confiance moyenne) :** le promoteur dispose de tableaux de bord sur le centre ; le centre n'a pas de vue équivalente sur le promoteur (délais de réponse, de paiement, qualité des outils). Les sites utilisent pourtant la rapidité de paiement pour choisir leurs études ([SCRS](https://myscrs.org/wp-content/uploads/2024/08/Site-Payments-and-Patient-Reimbursements-Global-Perspective.pdf)). Le marché de l'attention des centres existe donc, mais il est opaque.

---

## 6. Besoins non exprimés (besoins latents)

| Question directrice | Observation (hypothèse à valider) | Indice documentaire | Confiance |
|---|---|---|---|
| Difficultés devenues normales | La double saisie DPI → EDC est vécue comme « le travail », et non comme un défaut | 86 % des données transférables (Flatiron) | Moyenne |
| Tâches dues à des outils mal conçus | Tableurs personnels du CRC pour suivre les fenêtres de visite de *toutes* ses études, car aucun outil promoteur ne donne de vue transversale | Multiplication des plateformes (SCRS) | Moyenne |
| Problèmes compensés par l'expérience | Lire un protocole de 150 pages et en extraire les « pièges » ; savoir qui appeler chez tel promoteur | Complexité croissante (Tufts) | Moyenne |
| Informations recherchées manuellement | « Ce patient est-il éligible à un essai ouvert ? » ; « quelle version du document est en vigueur ? » ; « où est passé le paiement ? » | Unger 2019 ; Greenphire | Élevée / moyenne |
| Erreurs découvertes trop tard | Déviations détectées à la visite de monitoring, plusieurs semaines après les faits ; inéligibilités découvertes après l'inclusion | Pratique standard du monitoring | Moyenne |
| Relances répétitives | Collecte des documents réglementaires, signatures, réponses aux requêtes, paiements | Start-up, paiements | Élevée |
| Décisions sur information incomplète | Sélection des centres fondée sur des questionnaires déclaratifs ; budgets sans mesure de la charge réelle | 11 % de centres à zéro inclusion | Élevée |
| Connaissance enfermée dans les têtes | Historique d'un centre, d'une étude, d'une relation ; « jurisprudence » locale des CPP | Rotation élevée | Moyenne |
| Invisible pour les managers | Temps passé en formations et en connexions ; charge émotionnelle du suivi des patients | SCRS 2026 (formations) | Moyenne |
| Étapes supprimables | Questionnaires de faisabilité redondants si les données d'activité du centre étaient partagées ; SDV ciblée si les données venaient directement du DPI ; reconstruction manuelle de l'EDC si le protocole était structuré (M11) | M11/USDM, RBQM | Moyenne |

### Besoins contradictoires entre acteurs

| Besoin du promoteur | Besoin du centre | Nature de la tension |
|---|---|---|
| Outils standardisés et contrôlés par étude | Moins d'outils, une vue unifiée multi-promoteurs | Fragmentation transférée au centre |
| Collecter le maximum de données | Collecter le strict nécessaire | Le coût marginal d'une donnée est supporté par le centre |
| Visibilité en temps réel sur le centre | Autonomie, pas de micro-pilotage | Asymétrie d'information |
| Paiement à la donnée propre (*clean data*) | Trésorerie prévisible | Le paiement devient un levier de qualité, au risque de la viabilité du centre |
| Contrôle qualité exhaustif (aversion au risque d'inspection) | Proportionnalité (E6(R3)) | Inertie organisationnelle |
| Confidentialité des informations concurrentielles | Mutualisation des enseignements entre études | Frein à la capitalisation |

---

## 7. Expérience patient

> Source principale : CISCRP *Perceptions & Insights* 2023 (12 017 répondants, 54 pays) ([CISCRP](https://www.ciscrp.org/services/research-services/perceptions-and-insights-study), [article TIRS 2025](https://link.springer.com/article/10.1007/s43441-025-00751-9)) et 2025 ([rapport](https://www.ciscrp.org/wp-content/uploads/2025/11/2025-Perceptions-Insights-General-Perceptions_FINAL.pdf)). L'échantillon est en ligne et auto-sélectionné, ce qui crée un biais vers des personnes déjà connectées et intéressées.

### 7.1 Parcours patient (avant – pendant – après)

```
AVANT                         PENDANT                                APRÈS
Découverte ─▶ Compréhension ─▶ Consentement ─▶ Visites/suivi ─▶ Fin ─▶ Retour des résultats
   │              │                │                 │               │          │
 « personne     jargon,         document          déplacements,   rupture    rarement
  ne m'en a     incertitude     long, peur        attente, avance  brutale    reçu
  parlé »       randomisation   du placebo        de frais, ePRO   du lien
```

| Dimension | Constat | Source | Confiance |
|---|---|---|---|
| Connaissance | Un peu plus de la moitié des répondants se souviennent d'avoir entendu parler d'une étude dans les 6 derniers mois ; compréhension, notoriété et volonté de participer sont en baisse entre 2023 et 2025 | CISCRP 2023/2025 | Moyenne |
| Accès à un essai pertinent | Le facteur limitant majeur est l'absence d'essai disponible, plus que le refus du patient | [Unger 2019](https://doi.org/10.1093/jnci/djy221) | Élevée (oncologie) |
| Compréhension du consentement | La compréhension de notions clés (randomisation, placebo) reste partielle ; environ la moitié des participants seulement les comprennent selon une méta-analyse | [Tam et al., Br J Surg 2015](https://doi.org/10.1002/bjs.9725) | Moyenne (à vérifier) |
| Confiance | La transparence et l'implication des patients sont les leviers de confiance les plus cités ; la diversité des équipes compte | CISCRP 2023/2025 | Moyenne |
| Charge | Visites nombreuses ; la hausse des procédures (+42 % en phase III) pèse directement sur le patient | Tufts | Élevée |
| Coûts | Avances de frais de transport et d'hébergement ; les retards de remboursement sont aussi un problème mondial | [SCRS/Greenphire](https://myscrs.org/wp-content/uploads/2024/08/Site-Payments-and-Patient-Reimbursements-Global-Perspective.pdf) | Moyenne |
| Fin d'essai | Le retour d'information aux participants reste rare ; le résumé laïc est obligatoire dans l'UE (CTR), mais sa diffusion active au patient n'est pas garantie | CTR art. 37 ; interprétation | Moyenne |
| Populations sous-représentées | Barrières géographiques, linguistiques, de littératie et de confiance ; cadre réglementaire américain instable en 2025 | AgencyIQ, DLA Piper | Élevée (constat), faible (évolution) |

### 7.2 Pistes d'amélioration (au niveau des principes, sans solution)
- Le patient vit **un seul parcours de soins**, mais il est sollicité par **plusieurs systèmes** (DPI, ePRO, eConsent, remboursements), qui ne communiquent pas entre eux.
- La décision de participer se prend souvent **en dehors de la consultation** (au domicile, avec les aidants), alors que l'information est donnée **pendant** la consultation.
- Tout progrès doit préserver l'**autonomie** (droit de refus sans conséquence), la **sécurité** et la **confidentialité** (RGPD, EHDS, HDS en France).

---

## 8. Outils et acteurs du marché

> Ce paysage s'appuie sur la connaissance du marché et non sur des évaluations indépendantes exhaustives, car il existe peu d'études comparatives publiées. **Confiance : moyenne** pour l'existence et le positionnement des acteurs, **faible** pour les jugements sur leurs limites, qui doivent être vérifiés en entretien.

| Catégorie | Acteurs représentatifs | Utilisateurs | Modèle économique | Limites récurrentes (à valider) |
|---|---|---|---|---|
| Suites unifiées promoteur | Medidata (Dassault), Veeva Vault Clinical, Oracle Health Sciences, IQVIA | Promoteurs, CRO | Licence par étude ou par plateforme | Pensées pour le promoteur ; le centre subit une instance par promoteur |
| EDC | Medidata Rave, Veeva EDC, Oracle Clinical One / InForm, Castor, REDCap (académique), Ennov, OpenClinica | DM, CRC | Par étude ou volume | Saisie manuelle depuis le DPI ; construction de la base à partir d'un protocole non structuré |
| CTMS | Veeva, Medidata, Oracle Siebel, IQVIA ; côté centre : CRIO, Advarra OnCore, RealTime, Easy Clinical (France) | CTM, centres | Licence | Les CTMS promoteur et centre ne se parlent pas |
| eTMF / eISF / eReg | Veeva eTMF, Florence eBinders, Advarra eReg, Veeva SiteVault | Promoteurs, centres | Licence ou gratuit pour le centre (modèle « payé par le promoteur ») | Duplication ISF ↔ TMF, gestion des versions |
| RTSM / IRT | Suvoda, Signant Health, Endpoint Clinical, 4G Clinical, Almac, Medidata RTSM | Pharmacie, CRC | Par étude | Un système par étude pour la PUI |
| eCOA / ePRO / eConsent | Signant, Clario, Medidata, YPrime, Castor, Veeva | Patients, centres | Par patient ou étude | Fatigue applicative des patients, appareils provisionnés |
| Recrutement / pré-screening | TriNetX, Deep 6 AI, Antidote, Clara, Citeline, IQVIA | Promoteurs, centres | Abonnement / par patient | Dernier kilomètre humain ; couverture DPI inégale (notamment en Europe) |
| EHR → EDC | IgniteData, Flatiron Clinical Pipe, IQVIA, Epic/Cerner (natif), Yonalink | Centres, promoteurs | Intégration | Déploiement site par site, gouvernance |
| Monitoring / RBQM | CluePoints, Medidata Detect, IQVIA, Remarque | CTM, monitoring central | Licence | Production de signaux, mais l'action reste manuelle |
| Safety / PV | Oracle Argus, ArisGlobal LifeSphere, Veeva Vault Safety | PV | Licence | Réconciliation avec l'EDC |
| Paiements | Greenphire, Suvoda Pay, Medidata, Flywire | Promoteurs, sites, patients | Transaction | Dépendance à l'état des données et à la qualité des budgets |
| Données / analytics | Saama, Medidata, elluminate (eClinical Solutions), Snowflake/Databricks | DM, biostat | Licence | Sur-couche supplémentaire |
| IA générative appliquée | Fonctions IA des suites (rédaction de protocoles, CSR, extraction), start-up de *medical writing* et de faisabilité | Promoteurs | Variable | Preuves d'impact surtout commerciales ; validation et conformité en cours de définition |

**Lecture stratégique (interprétation, confiance moyenne) :**
1. **Le marché est organisé autour de l'acheteur, c'est-à-dire du promoteur.** Le centre reste l'utilisateur sans pouvoir d'achat, ce qui explique la fragmentation qu'il subit.
2. **La consolidation va vers des « suites »** (Veeva, Medidata, Oracle), mais chaque suite reste **mono-promoteur** du point de vue du centre.
3. **Peu d'acteurs vendent au centre lui-même**, et ceux qui le font (CRIO, Advarra, Florence) sont soit centrés sur les États-Unis, soit financés par les promoteurs.

---

## 9. Technologies émergentes et transpositions

### 9.1 Technologies

| Technologie | Applications plausibles en opérations cliniques | Maturité | Verrou principal |
|---|---|---|---|
| IA générative / LLM | Lecture et rédaction de protocole, extraction des critères d'éligibilité, brouillons de rapports, réponses aux requêtes, résumés laïcs | Pilotes nombreux | Validation, traçabilité, responsabilité (FDA : cadre de crédibilité ; exclusion des usages purement opérationnels) |
| Agents IA | Enchaînement de tâches multi-systèmes (collecte de documents, relances, préparation de visite) | Précoce | Accès aux systèmes, droits, auditabilité |
| NLP sur texte clinique | Pré-screening à partir des comptes rendus, extraction des AE | Intermédiaire | Qualité et hétérogénéité du DPI, langue (le français est moins couvert) |
| IA multimodale | Imagerie, documents scannés, formulaires | Intermédiaire | Validation |
| Analyse prédictive / ML | Prévision du recrutement par centre, risque de décrochage des centres et des patients | Intermédiaire | Données historiques rares et propriétaires |
| Graphes de connaissances | Relier protocole ↔ procédures ↔ budget ↔ EDC ↔ formation | Précoce | Ontologies (USDM et M11 aident) |
| Interopérabilité (FHIR, Vulcan, USDM, M11) | Protocole numérique, DPI → EDC | Normes disponibles, adoption naissante | Gouvernance et coût d'intégration par centre |
| Process mining | Mesure réelle des flux (start-up, requêtes, paiements) à partir des journaux d'événements | Mature dans d'autres secteurs, rare ici | Journaux dispersés entre organisations |
| Jumeaux numériques | Simulation d'un protocole contre la capacité des centres ; bras de contrôle synthétiques (Unlearn.AI) | Précoce / réglementairement encadré | Acceptabilité, validation |
| Interfaces conversationnelles | Questions de protocole au fil de l'eau (centres), information des patients | Pilotes | Fiabilité, version du protocole |
| Aide à la décision | Éligibilité, gestion des fenêtres de visite | Intermédiaire | Intégration au flux de travail |
| Traçabilité (journaux d'audit, signatures, éventuellement registres distribués) | Gestion des versions, chaîne de responsabilité | Mature (Part 11), mais fragmentée | Multi-organisation |

### 9.2 Transpositions depuis d'autres secteurs (pistes de réflexion, confiance faible à moyenne)

| Secteur | Pratique | Analogie en recherche clinique |
|---|---|---|
| Aéronautique | Check-lists, CRM (*crew resource management*), signalement non punitif des incidents (ASRS) | Les déviations sont traitées comme des fautes individuelles plutôt que comme des signaux systémiques ; pas de base partagée et anonymisée de « quasi-incidents » |
| Logistique | Tour de contrôle (*control tower*), suivi de bout en bout, ETA prédictive | Personne n'a de « tour de contrôle » du centre multi-promoteurs |
| Finance | Rapprochement automatique (*reconciliation*), règlement en temps réel, KYC partagé | Paiements de sites, réconciliation SAE ↔ EDC, « KYC » des centres (documents réglementaires ressaisis à chaque étude) |
| Cybersécurité | SOC, triage des alertes, *playbooks* | Monitoring central : beaucoup d'alertes, triage manuel |
| Gestion de crise | Situation room, information partagée, rôles clairs | Pandémie : les essais plateformes (RECOVERY) ont montré qu'un essai simple et intégré au soin est possible ([RECOVERY](https://www.recoverytrial.net/)) |
| Robotique / industrie | Poka-yoke (anti-erreur dès la conception) | Les fenêtres et procédures pourraient être verrouillées en amont plutôt que contrôlées en aval |
| Sciences cognitives | Charge cognitive, fatigue décisionnelle, conception centrée sur l'attention | Charge mentale du CRC qui gère 10 à 20 protocoles différents |
| Industrie pharmaceutique (CMC) | Quality by Design (ICH Q8) | E6(R3) transpose explicitement cette logique aux essais |

---

## 10. Étude prospective

### 10.1 Moteurs de transformation (confiance moyenne)
1. Réglementation de la proportionnalité (E6(R3)) et de la donnée structurée (M11/USDM).
2. Pression économique sur les délais (coût d'un jour de retard) et compétition entre régions (l'UE cherche à regagner des parts, la Chine monte en puissance comme lieu d'essais — tendance largement rapportée, non chiffrée ici).
3. IA générative appliquée aux documents, qui représentent une grande part de la charge de travail.
4. Pénurie de personnel dans les centres.
5. Ouverture des données de santé (EHDS, Health Data Hub).

### 10.2 Scénarios

| Horizon | Scénario central | Signaux observables | Métiers les plus touchés |
|---|---|---|---|
| **3 ans (2029)** | L'IA générative est généralisée *côté promoteur et CRO* (rédaction de protocoles, CSR, rapports de visite, revue de données). Premiers protocoles M11 en production. E6(R3) annexe 2 applicable. Les centres restent fragmentés et l'écart de productivité promoteur/centre se creuse. | Rapports de visite pré-rédigés ; baisse de la SDV totale ; pilotes EHR → EDC dans les grands CHU | Medical writers, data managers, CRA (le rapport de visite et la SDV diminuent ; le rôle de conseil au centre augmente) |
| **5 ans (2031)** | Le protocole numérique (USDM) alimente automatiquement l'EDC, le calendrier des visites et le budget de grille. EHR → EDC significatif dans les centres à fort volume. Le monitoring central devient majoritaire. Les essais pragmatiques et intégrés au soin se développent, grâce à l'annexe 2 et à l'EHDS. | Temps de construction de l'EDC réduit ; contrats partiellement standardisés à l'échelle européenne | CRC (moins de saisie, plus de coordination patient), study start-up, pharmacie (selon l'IRT) |
| **10 ans (2036)** | La recherche s'intègre au soin : l'éligibilité est détectée en continu, une partie des données est collectée directement depuis le soin, des bras de contrôle sont en partie externes ou synthétiques dans certaines indications, et la conformité est vérifiée en continu plutôt qu'a posteriori. Le centre devient une « plateforme de recherche » ; le rôle humain se concentre sur la relation au patient, le jugement médical et la gestion d'exceptions. | Inspections fondées sur les données ; nouveaux métiers (ingénieur de protocole numérique, *trial data steward*) | Tous ; le métier d'ARC devient soit un métier d'expert qualité/risque, soit un métier de relation patient |

**Scénario alternatif défavorable (à surveiller) :** l'IA multiplie les données et les exigences au lieu de les réduire (« paradoxe de Jevons » : plus on peut collecter à bas coût, plus on collecte), ce qui accroît la charge des centres. La fragmentation persiste parce que l'économie du secteur reste centrée sur l'acheteur promoteur. **Probabilité : non négligeable** (interprétation).

---

## 11. Matrice des problèmes et besoins

Échelles : Fréquence (F) et Gravité (G) de 1 à 5 ; Potentiel d'amélioration (P) de 1 à 5 ; niveau de preuve E / M / F (élevé, moyen, faible). Les scores sont des **jugements de l'auteur**, fondés sur les sources citées, et doivent être révisés après les entretiens.

| # | Problème | Acteurs | F | G | Conséquences | Solutions existantes | Insuffisances | Opportunité technologique | P | Preuve |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Complexité des protocoles et amendements | Promoteur, centres, patients | 5 | 5 | Délais, déviations, coûts, charge patient | Revues de faisabilité, scores de complexité | Pas de modèle de la charge du centre | Simulation protocole × capacité ; protocole structuré | 5 | E |
| 2 | Lenteur du start-up | Centres, promoteurs, CRO | 5 | 4 | Retard de première inclusion | Convention unique, plateformes de start-up | Suivi sans parallélisation, sans visibilité partagée | Orchestration multi-organisations | 4 | E |
| 3 | Pas d'essai disponible ou inéligibilité | Patients, investigateurs | 5 | 5 | Perte de chance, échec des essais | Pré-screening EHR | Couverture, texte libre, dernier kilomètre | NLP, critères structurés (M11), réseau d'adressage | 4 | E |
| 4 | Fuite du dernier kilomètre du recrutement | CRC, investigateurs | 4 | 4 | Patients identifiés jamais inclus | Peu de solutions | Processus humain non outillé | Coordination, rappels, aide à l'explication | 4 | M |
| 5 | Rétention et abandons | Patients, centres | 4 | 4 | Perte de puissance statistique | Composantes DCT, remboursements | Peu de mesures, peu de prédiction | Détection précoce du décrochage | 3 | F |
| 6 | Prolifération des plateformes | Centres | 5 | 3 | Temps perdu, erreurs, épuisement | SSO, portails | Mono-promoteur | Couche unifiée côté centre | 4 | M |
| 7 | Double saisie DPI → EDC | CRC, DM | 5 | 3 | Temps, erreurs de transcription, SDV | Pilotes EHR → EDC | Intégration par centre | FHIR, NLP, M11 | 5 | M |
| 8 | SDV peu productive | CRA, centres | 4 | 3 | Coût du monitoring | RBQM | Inertie, aversion au risque | Qualité intégrée dès la conception, vérification à la source | 4 | M |
| 9 | Déviations découvertes tard, non capitalisées | Centres, QA, CRA | 4 | 4 | Risque patient et données, répétition | Logs, CAPA | Analyse a posteriori, pas de partage | Détection en temps réel, base d'apprentissage | 4 | F |
| 10 | Rotation et perte de mémoire | Centres, CRO | 5 | 4 | Perte de qualité, coût de réentraînement | Compagnonnage, SOP | Connaissance tacite non capturée | Capitalisation contextuelle | 4 | M |
| 11 | Formations redondantes | Centres | 5 | 2 | Heures perdues | Reconnaissance mutuelle GCP | Adoption partielle | Portabilité des qualifications | 3 | M |
| 12 | Retards de paiement | Centres, patients | 4 | 4 | Trésorerie, choix des études, abandons | Plateformes de paiement | Dépendance aux budgets non structurés | Budget structuré lié au protocole | 4 | M |
| 13 | Asymétrie d'information centre ↔ promoteur | Centres | 5 | 3 | Mauvais appariement des études | Peu de solutions | Opacité | Transparence bilatérale des performances | 3 | F |
| 14 | Questions de protocole au quotidien | CRC, IRC, investigateurs | 5 | 3 | Déviations, attente des réponses | Contact CRA, medical monitor | Lenteur, versions multiples | Accès conversationnel fiable au protocole en vigueur | 4 | F |
| 15 | Consentement mal compris | Patients | 4 | 4 | Autonomie, confiance, abandons | eConsent | Format documentaire plutôt que pédagogique | Information adaptative | 3 | M |
| 16 | Retour aux participants absent | Patients, associations | 4 | 3 | Perte de confiance | Résumé laïc (UE) | Pas de canal de diffusion active | Canal de lien post-essai | 3 | M |
| 17 | Faisabilité déclarative | Promoteurs, centres | 5 | 4 | 11 % de centres à zéro inclusion | Questionnaires, bases de sites | Déclaratif, répétitif | Faisabilité fondée sur les données | 4 | E |
| 18 | Charge réglementaire multi-pays (RFI, CTIS) | Réglementaire | 4 | 3 | Délais | CTIS, ACT EU | Performance de CTIS, désynchronisation | Préparation prédictive des RFI | 3 | M |
| 19 | Réconciliation SAE ↔ EDC | PV, DM, CRC | 4 | 3 | Charge, risque de sécurité | Intégrations ponctuelles | Double source | Saisie unique | 3 | M |
| 20 | Charge mentale des coordinateurs multi-études | CRC, IRC | 5 | 4 | Erreurs, épuisement | Tableurs personnels | Aucune vue transversale | Planification cognitive multi-protocoles | 4 | F |

### Classement en 4 catégories

| Catégorie | Problèmes |
|---|---|
| **1. Importants mais déjà bien adressés** (beaucoup d'offre, adoption en cours) | Gestion de l'EDC en soi ; eTMF ; RTSM ; ePRO ; paiements patients (partiellement) ; analytique RBQM côté promoteur (#8 pour la partie détection) |
| **2. Importants mais insuffisamment adressés** | #1 complexité vue depuis le centre ; #2 start-up multi-organisations ; #6 fragmentation côté centre ; #7 double saisie (hors grands centres américains) ; #12 paiements ; #17 faisabilité |
| **3. Peu visibles mais potentiellement majeurs** | #4 dernier kilomètre ; #9 capitalisation des déviations ; #10 mémoire organisationnelle ; #13 asymétrie d'information ; #14 questions de protocole ; #20 charge cognitive multi-études |
| **4. Transformations futures sans solution évidente** | Exécution de protocoles M11/USDM de bout en bout ; validation et auditabilité des agents IA en environnement GCP ; recherche intégrée au soin (EHDS, annexe 2) ; nouveaux métiers et nouvelles compétences du personnel de recherche ; centre multi-promoteurs comme « plateforme » |

---

## 12. Cartographie des espaces d'innovation (découvertes, pas solutions)

| Espace | Description | Pourquoi il est inexploité (hypothèse) |
|---|---|---|
| **A. Rupture conception → exécution** | Le protocole est conçu sans représentation quantifiée du travail qu'il impose au centre et au patient | Les données de charge réelle n'existent nulle part de façon structurée ; le concepteur et l'exécutant appartiennent à des organisations différentes |
| **B. Coordination inter-organisationnelle** | Le start-up, les paiements, les documents et les requêtes traversent 3 à 5 organisations sans « propriétaire » du flux | Chaque éditeur vend à *une* organisation |
| **C. Information qui ne circule pas** | De promoteur à centre (statut des paiements, raisons des décisions), de centre à promoteur (capacité réelle), de l'essai vers le patient (résultats) | Les incitations à partager sont faibles ou contraires |
| **D. Connaissance non capitalisée** | Astuces par protocole, historique des centres, causes racines des déviations, « jurisprudence » éthique | Elle est tacite, dispersée, perdue avec la rotation, et semble trop modeste pour être vendue |
| **E. Interventions humaines répétitives** | Relances, transcriptions, réconciliations, reformatage de documents | Il faut des accès multi-systèmes et un cadre d'auditabilité, deux choses que l'IA agentique et E6(R3) rendent désormais envisageables |
| **F. Détection précoce** | Décrochage d'un centre, d'un patient, déviation imminente, amendement évitable | Les données sont dispersées et rarement historisées de façon exploitable |
| **G. Besoins communs à plusieurs métiers** | « Quelle est la règle en vigueur pour *ce* patient, *cette* visite, *cette* version ? » concerne CRC, IRC, investigateur, pharmacien et CRA | Chaque outil répond à une partie de la question |
| **H. Délaissés du marché** | Le centre comme client (surtout en Europe et dans l'académique), le patient après l'essai, la recherche académique | Faible pouvoir d'achat apparent |
| **I. Supprimer plutôt qu'automatiser** | Faisabilité déclarative, SDV systématique, formations redondantes, ressaisie de documents réglementaires, construction manuelle de l'EDC | Les standards (M11, USDM, FHIR) et la réglementation (E6(R3)) ont rendu ces suppressions possibles avant que les organisations ne s'en saisissent |

---

## 13. Méthodologie proposée pour valider les découvertes sur le terrain

### 13.1 Entretiens qualitatifs semi-directifs
- **Échantillon cible (saturation attendue vers 25–35 entretiens) :** 6 ARC/CRC investigateurs (CHU, CLCC, privé), 5 CRA (CRO, promoteur), 3 IRC, 3 investigateurs, 2 pharmaciens de PUI, 3 managers (CTM, start-up), 2 data managers, 2 responsables qualité, 2 représentants de DRCI, 3 patients ou représentants d'associations, 1–2 membres de CPP.
- **Diversité :** France et au moins un autre pays européen ; académique et industriel ; oncologie et hors oncologie.
- **Guide (extraits) :**
  1. « Racontez-moi votre dernière journée de travail, heure par heure. »
  2. « Quelle tâche faites-vous en sachant qu'elle ne sert à rien ? »
  3. « Qu'avez-vous appris dans votre poste que personne ne vous avait dit ? »
  4. « Quelle est la dernière erreur que vous avez découverte trop tard ? Comment ? »
  5. « Qui relancez-vous le plus souvent, et pour quoi ? »
  6. « Si vous partiez demain, qu'est-ce qui serait perdu ? »
  7. « Montrez-moi vos fichiers personnels de suivi. » (technique d'*artefact walkthrough*)
- **Biais à contrôler :** biais de désirabilité (« les outils sont bien »), biais de plainte, biais de sélection (les plus motivés répondent). Garder la neutralité : ne pas présenter d'hypothèse de solution.

### 13.2 Observation (shadowing)
- 2 à 3 demi-journées dans une unité de recherche clinique, avec relevé des tâches, des interruptions, des changements de système et des recherches d'information. C'est la seule méthode qui permette de mesurer le **temps réel**, alors que les enquêtes mesurent le temps déclaré.

### 13.3 Enquête quantitative
- Questionnaire de 15 minutes diffusé via les réseaux professionnels (associations d'ARC, réseaux de DRCI, groupes coopérateurs). Il servira à quantifier les hypothèses des sections 6 et 11 : nombre d'études et de systèmes par personne, heures de formation, fréquence des relances, part de saisie en double.
- Pré-enregistrer les hypothèses pour éviter la sur-interprétation.

### 13.4 Analyse de données de processus (si l'accès est possible)
- Process mining sur des journaux d'événements anonymisés d'un CTMS de centre ou d'une DRCI : délais de convention, cycle des requêtes, délais de paiement.

### 13.5 Critères de validation d'une découverte
1. Elle est citée spontanément par au moins 3 profils différents.
2. Un cas concret et daté vient l'illustrer.
3. Un coût (temps ou argent) est estimable.
4. Personne ne déclare l'avoir résolue de façon satisfaisante.

---

## 14. Les 10 découvertes les plus prometteuses

> Ce sont des **constats** destinés à ouvrir des voies d'innovation, et non des concepts de produits. Chacun est à confronter au terrain (§ 13).

1. **Le centre investigateur est le goulot d'étranglement du système, mais il n'est le client de presque personne.** Le marché technologique est structuré autour du promoteur acheteur. Le centre absorbe la fragmentation (identifiants multiples, formations répétées, paiements tardifs) sans levier pour la réduire. *(Confiance : moyenne)*

2. **Le coût de la complexité est conçu en amont et payé en aval, sans boucle de retour.** Les protocoles gagnent des procédures (+42 % en phase III) et des amendements (76 % de protocoles amendés), mais il n'existe aucune mesure partagée de la charge qu'un protocole impose à un centre et à un patient *avant* sa finalisation. *(Confiance : élevée sur la tendance, moyenne sur l'absence de boucle)*

3. **La réglementation a pris de l'avance sur les organisations.** E6(R3) (proportionnalité), M11 (protocole structuré) et l'annexe 2 (designs pragmatiques, en 2027) autorisent des pratiques que les outils et les cultures du risque n'appliquent pas encore. L'espace entre « ce qui est permis » et « ce qui est fait » constitue un territoire en soi. *(Confiance : élevée)*

4. **Le protocole est le document le plus important de l'essai, et le plus mal exploité.** Il est rédigé en texte libre, puis réinterprété manuellement des dizaines de fois (EDC, budget, calendrier, formations, check-lists de centre, questions quotidiennes). Sa structuration (M11/USDM) est désormais normalisée, mais ses effets en aval restent largement inexploités, en particulier côté centre. *(Confiance : élevée)*

5. **Le recrutement échoue moins par refus des patients que par absence de rencontre.** Il n'y a pas d'essai disponible au bon endroit, l'investigateur n'y pense pas au moment de la consultation, et les patients identifiés se perdent au « dernier kilomètre ». Il s'agit d'un problème d'appariement et de coordination plus que de persuasion. *(Confiance : élevée en oncologie)*

6. **La mémoire opérationnelle de la recherche clinique repose sur des personnes à forte rotation.** Les savoir-faire par protocole, par promoteur et par centre, ainsi que les causes réelles des déviations, ne sont pas capitalisés. Chaque départ de CRA ou de CRC détruit un capital invisible dans les tableaux de bord. *(Confiance : moyenne)*

7. **Le contrôle qualité vérifie après coup ce qui aurait pu être garanti à la source.** La SDV corrige environ 1 % des données. Les déviations sont découvertes des semaines après les faits. La double saisie DPI → EDC crée elle-même une partie des erreurs que le monitoring cherche ensuite. Le gisement se trouve dans la **suppression** d'étapes, plus que dans leur automatisation. *(Confiance : moyenne)*

8. **Les flux inter-organisationnels n'ont pas de propriétaire.** Le start-up, les paiements, les documents réglementaires et les requêtes traversent plusieurs organisations. Chacune ne voit que son segment, d'où des relances permanentes et des délais : 160 jours jusqu'à la première inclusion en France, et 50 % seulement des essais européens recrutent en ≤ 200 jours. *(Confiance : élevée sur les délais, moyenne sur la cause)*

9. **L'expérience patient est fragmentée en autant de systèmes que de fonctions, et s'interrompt brutalement à la fin de l'essai.** Le patient vit un parcours unique, mais doit composer avec le DPI, l'eConsent, l'ePRO, les remboursements et les appels du centre. Après l'essai, le lien et le retour d'information sont presque absents, alors que la confiance et la transparence sont les premiers leviers de participation cités. *(Confiance : moyenne)*

10. **L'IA risque d'accroître l'asymétrie promoteur ↔ centre avant de la réduire.** Les premiers gains de l'IA générative se concentrent chez les promoteurs et les CRO (rédaction, revue de données), là où sont les budgets. Sans évolution côté centre, la productivité de conception augmentera plus vite que la capacité d'exécution, ce qui pourrait aggraver les découvertes 1 et 2. La question de l'auditabilité des agents IA en environnement GCP reste ouverte. *(Confiance : faible à moyenne — hypothèse prospective)*

---

## 15. Bibliographie et sources

### Publications à comité de lecture et instituts académiques
- Tufts CSDD / Getz K. et al. — Protocol amendments (2024), *Therapeutic Innovation & Regulatory Science*. https://link.springer.com/content/pdf/10.1007/s43441-024-00622-9.pdf
- Smith Z., DiMasi J., Getz K. — New estimates of the cost of a delay day (2024). White paper : https://csdd.tufts.edu/sites/default/files/2025-02/Aug2024%20Day%20of%20Delay%20White%20Paper%20Final.pdf ; critique : https://firstpatientin.substack.com/p/saturday-archive-a-day-late-and-half
- Getz K., Campo R. — Trends in clinical trial design complexity (2017/2018). https://link.springer.com/10.1177/2168479017713039
- Étude sur la conception des protocoles 2013–2018 (2022), *TIRS*. https://link.springer.com/content/pdf/10.1007/s43441-022-00438-5.pdf
- Sheetz N. et al. — Evaluating source data verification as a quality control measure (2014), *TIRS*. https://link.springer.com/article/10.1177/2168479014554400
- Revue de portée sur la qualité de la SDV (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11639101/
- Unger J.M. et al. — Barrières structurelles, cliniques et médecin/patient à la participation aux essais en cancérologie (2019), *JNCI*. https://doi.org/10.1093/jnci/djy221
- Carlisle B. et al. — Unsuccessful trial accrual and human subjects protections (2015), *Clinical Trials*. https://doi.org/10.1177/1740774514558307 *(cité de mémoire, à vérifier)*
- Tam N.T. et al. — Participants' understanding of informed consent in clinical trials over three decades (2015), *Br J Surg*. https://doi.org/10.1002/bjs.9725 *(cité de mémoire, à vérifier)*
- Rotation des professionnels de recherche clinique dans un grand centre académique, *J Clin Transl Sci*. https://www.cambridge.org/core/journals/journal-of-clinical-and-translational-science/article/trends-in-turnover-and-turbulence-at-a-large-academic-medical-center-before-and-during-covid19-analyzing-structured-clinical-research-professional-roles/4FCD004C1E699BA332939609FD5A1BA4
- CISCRP Perceptions & Insights 2023 — article *TIRS* 2025. https://link.springer.com/article/10.1007/s43441-025-00751-9
- Sanofi/Flatiron — EHR-to-EDC transfer potential (AMIA 2025). https://resources.flatiron.com/publications/optimizing-data-collection-assessing-ehr-to-edc-data-transfer-potential-across-structured-and-unstructured-data
- National Academies — chapitre sur les grands essais simples et les coûts des procédures. https://www.nationalacademies.org/read/18400/chapter/5

### Réglementation et institutions
- EMA — ICH E6 Good clinical practice. https://www.ema.europa.eu/fr/ich-e6-good-clinical-practice-scientific-guideline
- CITI Program — publication finale d'E6(R3). https://about.citiprogram.org/blog/ich-releases-final-version-of-e6r3-good-clinical-practice-guideline/
- ICH M11 — spécification technique (EMA). https://www.ema.europa.eu/en/documents/regulatory-procedural-guideline/ich-m11-clinical-electronic-structured-harmonised-protocol-cesharp-technical-specification-step-5_en.pdf
- FDA — M11 technical specification. https://www.fda.gov/regulatory-information/search-fda-guidance-documents/m11-technical-specification-clinical-electronic-structured-harmonised-protocol
- FDA — Digital Data Flow / USDM. https://www.fda.gov/media/164112/download
- HL7 Vulcan — Pharmaceutical Research Protocol IG. https://hl7.org/fhir/uv/pharmaceutical-research-protocol/2025Sep/06-info-models.html
- EMA — Nouveaux objectifs pour les essais en Europe. https://www.ema.europa.eu/fr/news/new-targets-clinical-trials-europe
- RAPS — objectifs UE et transition CTR. https://www.raps.org/resource/eu-regulators-set-targets-to-promote-european-clin.html
- FDA — Projet de guidance sur l'IA dans la prise de décision réglementaire (2025). https://www.fda.gov/regulatory-information/search-fda-guidance-documents/considerations-use-artificial-intelligence-support-regulatory-decision-making-drug-and-biological ; analyse : https://dlapiper.com/insights/publications/2025/01/fda-releases-draft-guidance-on-use-of-ai
- Plans d'action diversité — retrait et statut : https://www.agencyiq.com/blog/fda-pulls-diversity-action-plan-guidance-other-diversity-programs-after-executive-order/ ; https://dlapiper.com/insights/publications/2025/01/fda-actions-addressing-diversity-in-clinical-trials ; https://www.raps.org/resource/fda-reissues-sex-specific-data-guidance-after-sani.html
- ANSM — présentation sur le nouveau règlement (2024). https://ansm.sante.fr/uploads/2024/10/24/20240201-cr-ci-medicaments-essais-cliniques-nouveau-reglement-presentation.pdf
- RECOVERY trial. https://www.recoverytrial.net/

### Enquêtes et rapports professionnels (biais éditeurs possibles)
- Leem — 13ᵉ enquête attractivité (communiqué). https://www.leem.org/sites/default/files/2024-01/CP_ENQUETE_ATTRACTIVITE%20-%20vF.pdf ; étude complète : https://www.leem.org/sites/default/files/2024-01/Etude%20Attractivit%C3%A9%20du%20Leem.pdf ; édition 2026 : https://www.leem.org/sites/default/files/2026-05/Etude-Recherche%20Clinique.pdf
- ACRP — Workforce survey (2025). https://acrpnet.org/2025/09/24/acrp-publishes-results-from-first-ever-national-workforce-survey
- ACRP — CRA turnover within CROs post-COVID (2025). https://acrpnet.org/2025/02/14/cra-turnover-within-contract-research-organizations-post-covid-19-a-cross-sectional-study
- ACRP — Voices from the Frontlines. https://acrpnet.org/insights/white-papers/voices-from-the-frontlines
- ACRP — Protocol amendments (2026). https://acrpnet.org/2026/08/11/navigating-protocol-amendments-understanding-the-growing-burden-and-charting-a-path-forward
- BDO — CRO compensation & turnover survey 2024. https://bdo.com/insights/tax/key-findings-from-bdos-2024-clinical-research-organization-global-compensation-turnover-survey
- Advarra — Workforce Development Survey. https://resource.advarra.com/hubfs/eBook/Advarra%20Workforce%20Development%20Survey%20Report%20EB.pdf
- SCRS — Reducing site technology burdens. https://myscrs.org/resources/reducing-site-technology-burdens/
- SCRS/Oracle — research report 2019. https://oracle.com/co/a/ocom/docs/dc/em/scrs_research-report_09oct2019_final.pdf
- SCRS/Greenphire — Site payments global perspective. https://myscrs.org/wp-content/uploads/2024/08/Site-Payments-and-Patient-Reimbursements-Global-Perspective.pdf
- Applied Clinical Trials — SCRS 2026 et blocage de l'adoption technologique. https://www.appliedclinicaltrialsonline.com/view/2026-scrs-causes-technology-adoption-stall-
- Applied Clinical Trials — complexité croissante. https://appliedclinicaltrialsonline.com/view/rising-clinical-trial-complexity-continues-vex-drug-developers
- CISCRP — Perceptions & Insights 2023 / 2025. https://www.ciscrp.org/services/research-services/perceptions-and-insights-study ; https://www.ciscrp.org/wp-content/uploads/2025/11/2025-Perceptions-Insights-General-Perceptions_FINAL.pdf
- DIA Global Forum — « Last mile » leak in recruitment (2024). https://globalforum.diaglobal.org/issue/september-2024/documenting-the-last-mile-leak-in-the-patient-recruitment-pipeline/
- Tufts — performance d'inclusion des centres (synthèse). https://www.clinician.com/articles/62939-patient-recruitment-and-retention-rates-struggle
- Clinical Trials Arena — DCT adoption tracker. https://www.clinicaltrialsarena.com/features/dct-adoption-tracker-who-and-what-is-at-the-crest-of-the-trial-decentralisation-wave/
- Tufts CSDD — livre blanc DCT (2025). https://csdd.tufts.edu/sites/default/files/2025-11/White%20Paper_Final.pdf

### Données manquantes identifiées
- Statistiques publiques de fréquence des déviations par type et par phase.
- Taux d'abandon robustes par aire thérapeutique (les chiffres de « 30 % » relèvent de sources secondaires).
- Mesures du temps réel passé par tâche par les CRC/ARC investigateurs en France.
- Données françaises sur la rotation des TEC et ARC en CHU.
- Évaluations indépendantes comparatives des logiciels (quasi inexistantes).
- Données sur la recherche académique (sous-représentée dans les benchmarks Tufts).

---

*Prochain livrable suggéré : grille d'entretiens détaillée et questionnaire quantitatif (§ 13), puis confrontation des 10 découvertes au terrain avant toute phase de conception.*
