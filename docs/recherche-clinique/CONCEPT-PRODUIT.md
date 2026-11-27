# Concept produit — « KAIROS » (nom de travail)

### Le protocole exécutable du centre investigateur

*Livrable 2 — concept, à confronter au terrain. Construit à partir des découvertes 1, 2, 4, 6, 7 et 10 du rapport (`RAPPORT.md`, § 14).*

---

## 1. Le constat qui justifie le produit

Une phrase résume les découvertes du rapport :

> **Le protocole est le document le plus important de l'essai, mais au centre investigateur il n'existe que sous forme de PDF de 150 pages. L'ARC le retraduit à la main, de mémoire, pour chaque patient et chaque visite, dans 10 à 20 études en parallèle.**

Tout en découle :
- Une déviation est presque toujours un écart entre ce que le protocole exigeait *ce jour-là, pour ce patient, dans cette version* et ce qui a été fait. Exemples : fenêtre dépassée, examen oublié, mauvaise version de consentement, critère mal lu.
- Le CRA découvre ces écarts **des semaines plus tard**, en visite de monitoring.
- La personne qui savait éviter le piège finit par partir (forte rotation), et le savoir part avec elle.
- Aucun outil ne voit **toutes** les études du centre, car chaque outil appartient à **un** promoteur.

Les applis « génériques » (CTMS, eISF, chat sur PDF) **décrivent** ou **stockent** le protocole.
**Personne ne l'exécute du côté du centre.**

---

## 2. La proposition

**KAIROS transforme chaque protocole en un modèle exécutable, puis s'en sert pour dire à l'équipe du centre, pour chaque patient et chaque jour, exactement ce qui doit se passer. Il empêche ainsi les déviations au lieu de les constater.**

Le produit appartient au **centre** et couvre **tous ses promoteurs**. Il ne demande aucune intégration aux systèmes des promoteurs pour démarrer.

### Les trois idées qui le distinguent

| # | Idée | Pourquoi c'est une rupture |
|---|---|---|
| 1 | **Du PDF au protocole exécutable** : l'IA lit le protocole et ses amendements et en extrait un modèle structuré (visites, fenêtres, procédures par visite, critères d'éligibilité, règles de sécurité, versions). Un humain le valide une fois, et il sert ensuite des milliers de fois. | ICH M11 et CDISC USDM normalisent cette structure *côté promoteur* depuis 2025–2026, mais rien n'existe côté centre. KAIROS est compatible M11 : quand le promoteur fournira un protocole M11, l'extraction devient automatique. |
| 2 | **Zéro déviation par conception (poka-yoke)** : le système connaît la règle en vigueur *pour ce patient, à cette date, dans cette version*. Il prévient avant que l'erreur ne survienne, au lieu de laisser le CRA la constater après. | Le contrôle passe de l'aval à l'amont, exactement comme le demande ICH E6(R3) (*quality by design*). C'est la découverte n° 7 : supprimer le contrôle plutôt que l'automatiser. |
| 3 | **La mémoire du centre** : chaque question résolue, chaque piège rencontré et chaque déviation évitée ou subie est rattaché à la règle du protocole concernée, puis resservi automatiquement au bon moment, dans cette étude et dans les suivantes. | La connaissance tacite devient un actif du centre qui survit à la rotation du personnel (découverte n° 6). |

---

## 3. Ce que l'ARC vit concrètement (scénarios)

**Lundi 7 h 50 — le brief du jour.**
« 4 visites aujourd'hui. Patient 014 (étude ONCO-B) : J15 ±2 jours, la fenêtre se ferme mercredi. Bilan hépatique et ECG triplicate *avant* administration (amendement 3 : l'ECG passe de simple à triplicate). Le kit PK doit partir à T+2 h. Patient 022 (étude CARDIO-X) : il est sorti de la fenêtre de la visite 6 si la visite n'a pas lieu avant jeudi. »

**10 h — une question au fil de l'eau.**
« Le patient 014 a pris de l'ibuprofène hier, c'est autorisé ? »
→ Réponse avec **citation exacte du protocole** (version 4.0, section 6.4.2, page 61), et la mention : *« Interdit dans les 48 h avant administration. Mme L. (ancienne ARC) avait obtenu en 2025 une confirmation écrite du medical monitor pour ce cas : voir la note. »*
Si le système n'est pas sûr, il le dit et prépare la question pour le CRA ou le medical monitor.

**14 h — avant l'inclusion.**
Une check-list d'éligibilité générée depuis le protocole, critère par critère, avec la date de validité de chaque examen (« la créatinine date de 16 jours, le protocole exige ≤ 14 jours »).

**Arrivée d'un amendement.**
KAIROS compare les versions : « 7 changements opérationnels. 3 patients en cours sont concernés. Le patient 009 doit signer le consentement v5 à sa prochaine visite (le 12/12). La visite 4 ajoute un prélèvement. »

**Départ d'une collègue.**
Le nouvel ARC hérite des études **avec leur mémoire** : pièges, contacts, réponses déjà obtenues, particularités de chaque promoteur.

**Côté CRA (moniteur).**
Le centre peut partager, s'il le choisit, un **journal de conformité** : visites réalisées dans les fenêtres, alertes évitées, questions posées. La visite de monitoring devient ciblée. Le centre se transforme en centre « à faible risque », ce qui est un argument commercial face aux promoteurs.

---

## 4. Pourquoi ce n'est pas une appli générique

| Ce qui existe | Ce qu'il fait | Ce qu'il ne fait pas |
|---|---|---|
| CTMS de centre (CRIO, OnCore, Easy Clinical…) | Planifie et facture à partir d'un calendrier saisi à la main | Il ne *comprend* pas le protocole et ne prévient pas les déviations à partir des règles |
| eISF / eReg (Florence, SiteVault) | Stocke les documents et leurs versions | Il ne transforme pas le document en règles actionnables |
| EDC (Rave, Veeva…) | Contrôle les données *après* la saisie (*edit checks*) | Il est mono-promoteur et arrive après la visite |
| Outils de conception de protocole (ex. Faro Health), IA des grandes suites | Optimisent le protocole *chez le promoteur* | Rien pour le centre qui exécute |
| « ChatGPT sur le PDF » | Répond à des questions | Pas de version, pas de patient, pas de date, pas de mémoire, pas de traçabilité, des risques d'hallucination non maîtrisés |

**Le terrain libre se situe à l'intersection : protocole structuré × patient × date × version × mémoire, côté centre, multi-promoteurs.**

---

## 5. Le pari technique (et ses garde-fous)

1. **Extraction protocole → modèle** : LLM + schéma cible inspiré de USDM/M11 (calendrier des visites, *schedule of activities*, critères, règles conditionnelles).
   - *Garde-fou* : **validation humaine obligatoire**, champ par champ, avec renvoi à la page source. Le modèle n'est actif qu'une fois validé. Toute réponse cite sa source et la version.
2. **Moteur de règles déterministe** : le calcul des fenêtres et des procédures dues ne repose **pas** sur l'IA. Il repose sur le modèle validé. L'IA sert à lire et à expliquer ; un moteur classique sert à calculer. C'est ce qui rend le produit auditable.
3. **Gestion des versions** : chaque patient est rattaché à la version du protocole et du consentement qui s'applique à lui.
4. **Mémoire** : des notes structurées, rattachées à une règle du protocole et non à un document, avec auteur, date et source (e-mail du CRA, réponse du medical monitor).
5. **Données patient minimales** : au départ, uniquement le numéro patient de l'étude et les dates des visites. Pas de nom ni de dossier médical. Cela réduit fortement le risque et le temps nécessaire pour la mise en conformité.

---

## 6. Réglementation et risques — ce qu'il faut savoir tout de suite

| Sujet | Position | Niveau de risque |
|---|---|---|
| **Dispositif médical (MDR)** | Le produit aide à respecter un protocole ; il ne pose ni diagnostic ni décision thérapeutique. L'aide à l'éligibilité est une zone grise : elle doit rester une *check-list documentaire* qui reproduit le protocole, et non une décision médicale. **Avis d'un expert réglementaire indispensable.** | Moyen |
| **RGPD / hébergement HDS (France)** | Même pseudonymisées (numéro patient + dates), les données restent des données de santé à caractère personnel. Il faut un hébergeur certifié HDS et une analyse d'impact (AIPD). | Moyen, maîtrisable |
| **Validation informatique (GCP / Part 11)** | Si le produit devient source de vérité ou génère des documents de l'étude, il faut une validation du système et un journal d'audit. Le MVP doit rester un **outil d'aide** qui ne remplace pas les documents sources. | Moyen |
| **IA (AI Act, FDA)** | Usage opérationnel avec un humain dans la boucle : c'est la catégorie la moins contrainte. Il faut documenter les limites. | Faible à moyen |
| **Confidentialité des protocoles** | Les protocoles sont confidentiels (CDA). Il faut un LLM sans réutilisation des données pour l'entraînement, hébergé en UE, et une vérification que les CDA autorisent ce traitement. **Point bloquant potentiel n° 1.** | **Élevé** |
| **Erreur du modèle** | Une fenêtre mal extraite pourrait *causer* une déviation. Les réponses à la validation humaine, à la citation systématique et au moteur déterministe sont la base de la confiance. | Élevé si négligé |

---

## 7. Modèle économique (hypothèses)

1. **Centre (SaaS)** : par ARC ou par étude active. Cible de départ : centres privés et réseaux de sites (SMO), qui sont rentables à l'étude et sensibles aux déviations, ainsi que les DRCI de CHU (cycle d'achat plus long, marchés publics).
2. **Plus tard, le promoteur paie pour ce que le centre accepte de partager** : un indicateur de conformité, des protocoles M11 pré-chargés, ou un retour quantifié sur la charge réelle de son protocole. Ce dernier point ouvre la découverte n° 2 : faire remonter au concepteur le coût réel de la complexité.
3. **L'actif stratégique de long terme** : la base agrégée et anonymisée de la charge réelle des protocoles et des déviations évitées. Personne ne la possède aujourd'hui.

---

## 8. MVP — ce qu'il faut construire en premier (8 à 10 semaines)

**Périmètre volontairement étroit :** un ARC investigateur, 3 à 5 de ses études réelles, sans intégration.

1. Import d'un protocole (PDF) et d'un amendement → extraction du calendrier des visites et des procédures → écran de validation humaine avec renvoi à la page.
2. Ajout de patients (numéro + date de référence) → calcul automatique des fenêtres et des procédures dues.
3. **Brief du jour / de la semaine** pour toutes les études.
4. Question sur le protocole → réponse **avec citation et version**, ou « je ne sais pas ».
5. Comparaison d'amendements : liste des changements opérationnels et des patients impactés.
6. Notes de mémoire rattachées à une règle du protocole.

**Ce qu'on n'y met pas :** facturation, eISF, intégration EDC, éligibilité automatisée, application patient.

---

## 9. Tests qui peuvent tuer l'idée (à faire AVANT de coder)

| Hypothèse | Test | Critère d'arrêt |
|---|---|---|
| H1 — Les ARC investigateurs perdent un temps significatif à retraduire les protocoles et gèrent les fenêtres sur des outils personnels | 10 entretiens + demander à voir leurs tableurs ou agendas | Moins de 6 sur 10 ont un système « maison » |
| H2 — Une part importante des déviations vient de la complexité et de la mémoire (fenêtres, procédures, versions) | Analyser 30 à 50 déviations réelles anonymisées d'un centre | Moins de 40 % de déviations « évitables par rappel ou règle » |
| H3 — L'IA extrait correctement le calendrier des visites | Tester sur 5 protocoles réels (ou sur des protocoles publics de ClinicalTrials.gov, qui en publie beaucoup) | Moins de 90 % des champs justes avant correction, ou correction > 1 h par protocole |
| H4 — Les CDA et les DPO acceptent le traitement du protocole par un LLM hébergé en UE | Demander à 2 DRCI et 2 centres privés | Refus systématique → il faudrait une version en local, ce qui change le produit |
| H5 — Quelqu'un paie | Proposer un pilote payant (même symbolique) à 3 centres | Aucun engagement |

H3 peut être testée **dès cette semaine** sur des protocoles publics. Si vous le souhaitez, je peux construire ce prototype d'extraction dans ce dépôt.

---

## 10. Pourquoi maintenant

- **Les LLM** lisent désormais un protocole de 150 pages de façon exploitable, ce qui était impossible il y a 3 ans.
- **ICH M11 et USDM (2025–2026)** fournissent un schéma cible standard et, à terme, des protocoles directement structurés.
- **ICH E6(R3)** valorise la qualité intégrée dès la conception et la proportionnalité au risque, c'est-à-dire exactement la prévention plutôt que le contrôle.
- **La pénurie de personnel et la rotation** rendent la mémoire organisationnelle critique.
- **Le marché regarde ailleurs** : toutes les suites IA ciblent le promoteur (découverte n° 10). Le centre est le segment délaissé.

---

## 11. Ce que ce concept ne résout pas (honnêteté)

- **Le recrutement** (découverte n° 5) : KAIROS ne trouve pas de patients. Une extension naturelle viendra plus tard (les critères structurés + le DPI), mais elle relève d'un autre produit, avec une autre réglementation.
- **La fragmentation des outils promoteurs** : KAIROS ne supprime pas les connexions aux EDC et IRT. Il ajoute un outil, mais un outil qui *réduit* la charge mentale. Il faudra le prouver.
- **Le côté CRA** est servi indirectement. Si votre poste est celui de CRA (moniteur) plutôt que d'ARC investigateur, il existe un concept miroir (« le CRA qui voit le centre en continu »), à discuter.
