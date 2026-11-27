# Test H3 — l'IA peut-elle extraire le calendrier des visites d'un protocole ?

*27 novembre 2026 — premier passage. Prototype : `kairos/`.*

## 1. Protocole de test

| | |
|---|---|
| **Question** | Un modèle de langage peut-il transformer un protocole PDF en un calendrier exécutable (visites, fenêtres, procédures par visite), avec une source vérifiable pour chaque élément ? |
| **Corpus** | 3 protocoles publics de ClinicalTrials.gov, volontairement hétérogènes : un industriel, un académique français, un promoteur Inserm |
| **Critère d'arrêt (défini avant le test)** | Moins de 90 % des éléments justes avant correction, ou plus d'1 h de correction par protocole |
| **Qui a extrait** | Claude, **pendant la session de conception, sans appel API** : lecture du texte et des images des tableaux. Le script `kairos/extract_llm.py`, qui fait la même chose via l'API, est prêt mais n'a **pas** été exécuté (aucune clé API dans l'environnement). |
| **Qui valide** | **Vous**, avec les fiches `kairos/validation/*.md`. C'est la seule mesure de justesse qui compte : je ne peux pas noter mes propres extractions. |

| Protocole | Promoteur | Type | Pages | Qualité du texte du PDF |
|---|---|---|---|---|
| NCT02564523 — vaccin Ebola, 3 groupes, primo-vaccination + rappel | Janssen (industriel) | Phase II | 140 | Texte propre, **mais colonnes du tableau désalignées** |
| NCT02886624 — SAHIV, hépatite C aiguë | IMEA (académique, France) | Phase II/III | 71 | Bon |
| NCT02453048 — BPZE1, vaccin coqueluche nasal | **Inserm** | Phase Ib | 89 | **Dégradé** : lettres espacées (« I NSE R M ») |

## 2. Résultats mesurés automatiquement

| | Janssen | IMEA | Inserm | Total |
|---|---|---|---|---|
| Visites modélisées | 20 (3 calendriers par groupe) | 7 | 10 | 37 |
| Procédures modélisées | 16 | 20 | 20 | 56 |
| Citations sources | 42 | 32 | 34 | 108 |
| **Citations retrouvées mot pour mot sur la page indiquée** | 42/42 | 32/32 | 34/34 | **108/108** |
| Erreurs de cohérence interne (visites inconnues, ancrages) | 0 | 0 | 0 | 0 |
| Ambiguïtés du protocole détectées | 2 | 2 | 2 | 6 |

**Ce que ce 100 % prouve et ne prouve pas.** Chaque information est rattachée à un passage qui existe réellement dans le protocole : rien n'a été inventé. Cela **ne prouve pas** que l'interprétation est juste, par exemple qu'un « X » a été attribué à la bonne colonne. C'est l'objet de la validation humaine (§ 4).

Le vérificateur détecte bien les citations inventées ou mal placées : c'est testé dans `kairos/tests/test_kairos.py`.

## 3. Ce que le test a appris (avant même votre validation)

1. **Le texte du PDF ne suffit pas.** Sur 2 protocoles sur 3, la couche texte était inexploitable seule. Sur le protocole Inserm, les lettres sont espacées. Sur le protocole Janssen, l'alignement des colonnes est perdu : les « X » ne tombent plus sous la bonne visite. Il a fallu lire l'**image** des tableaux.
   → L'extracteur joint désormais le PDF au modèle (`--pdf`). Le vérificateur ignore les espaces, il fonctionne donc même sur le PDF Inserm dégradé.
2. **Les fenêtres de visite sont rarement là où on les attend.**
   - Janssen : le tableau des visites est en p.27-28, mais les fenêtres sont dans une table séparée p.79, soit 52 pages plus loin. Une autre table s'applique à une sous-étude.
   - IMEA : les fenêtres sont dans le tableau et répétées en section 9.8.
   - Inserm : les fenêtres sont dans l'en-tête du tableau et dans la description de chaque visite.
   → C'est exactement la « retraduction » que fait un ARC à la main.
3. **Chaque protocole contenait des ambiguïtés capables de provoquer une déviation.** Exemples réels :
   - *Janssen* : les fenêtres sont exprimées en jours depuis J1, alors que les visites post-rappel sont définies « +7 j après le rappel ». Si le rappel a lieu à J31 (dans sa fenêtre), la visite suivante est-elle due à J36 ou à J38 ?
   - *IMEA* : une coquille, « Quality of life questionnaire (only at **and** PT12) », où un mot manque. Le tableau dit D0 et PT12. Rien n'est prévu non plus en cas d'arrêt précoce du traitement pour le calcul des visites post-traitement.
   - *Inserm* : la fenêtre « 6±1 mois » n'est pas convertie en jours. La visite 8' n'a lieu que si la culture de J28 est positive : le centre doit recevoir ce résultat à temps.
   → **Constat produit :** faire remonter ces ambiguïtés au promoteur dès la mise en place est déjà une valeur en soi, et aucun outil ne le fait aujourd'hui.
4. **Les calendriers par groupe se gèrent bien.** Pour Janssen, le rappel tombe à J29, J57 ou J85 selon le groupe, et les visites post-rappel suivent la date réelle du rappel. Le moteur gère ces 3 calendriers.

## 4. Ce qu'il vous reste à faire (la vraie mesure de H3)

1. Ouvrez une fiche `kairos/validation/NCTxxxxx.md` et le PDF correspondant sur ClinicalTrials.gov :
   - Janssen : <https://cdn.clinicaltrials.gov/large-docs/23/NCT02564523/Prot_000.pdf>
   - IMEA : <https://cdn.clinicaltrials.gov/large-docs/24/NCT02886624/Prot_SAP_000.pdf>
   - Inserm : <https://cdn.clinicaltrials.gov/large-docs/48/NCT02453048/Prot_SAP_000.pdf>
2. Cochez chaque ligne exacte et corrigez les autres. Notez le **temps passé**.
3. H3 est validée si au moins 90 % des lignes sont justes et si la correction prend moins d'1 h par protocole.
4. L'idéal serait de répéter le test sur **un protocole sur lequel vous travaillez réellement**, sous réserve de l'accord de confidentialité. Vous connaissez ses pièges : vous verrez tout de suite si l'outil les attrape.

## 5. Limites de ce premier passage

- Les extractions ont été faites par Claude « en conversation » et non par le script API. Les résultats du script peuvent différer ; c'est à mesurer avec une clé API.
- 3 protocoles seulement, dont 2 en vaccinologie (calendriers courts et denses). Il manque l'oncologie (cycles, fenêtres conditionnelles aux toxicités) et des études longues.
- Le périmètre Janssen est partiel : cohortes 1/2 uniquement, sans les rappels tardifs ni la sous-étude.
- Le modèle ne gère pas encore les **cycles** (oncologie : « J1 de chaque cycle de 21 jours ») ni les visites déclenchées par un événement (toxicité, progression). C'est la prochaine extension du schéma.
