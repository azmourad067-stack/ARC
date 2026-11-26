# Adaptation de l'étude au réseau DAI-PP

**Date :** 26 novembre 2026
**Complément de :** `docs/etude-innovation-recherche-clinique.md` (concept KAIROS)
**Source sur DAI-PP :** uniquement le site public [dai-pp.com](https://dai-pp.com/) et sa liste publique des centres (`/centres-network-dai-pp.csv`), lus le 26/11/2026. Je n'ai eu accès à **aucun protocole, aucune donnée et aucun document interne**.

Les étiquettes sont les mêmes que dans l'étude principale : **[F]** fait (ici, ce que dit le site), **[H]** hypothèse d'expert, **[P]** projection.

---

## 1. Ce qu'est DAI-PP, d'après le site

- **Réseau français de recherche** sur les défibrillateurs automatiques implantables (DAI), fondé en **2012** et **promu par l'Inserm** [F].
- **Cohorte DAI-PP** : 10 000 patients implantés en prévention primaire ou secondaire, suivis **en temps réel pendant 10 ans par télécardiologie** (depuis 2018) [F].
- Le réseau s'est étendu à **l'ensemble des dispositifs de gestion du rythme cardiaque** et coordonne plusieurs études multicentriques **observationnelles et interventionnelles** [F] :

| Étude | Type (d'après le site) | Centres listés |
|---|---|---|
| Cohorte DAI-PP | Cohorte prospective, 10 000 patients, télécardiologie sur 10 ans | 19 |
| HONEST | Cohorte nationale, 5 000 premiers DAI sous-cutanés | 150 |
| FOREVER | Cohorte, 1 000 premiers DAI extravasculaires | 54 |
| DAI-T4F | Registre national, tétralogie de Fallot avec DAI | 45 |
| AV-CESAR | Cohorte, 1 000 premiers Micra AV (pacemaker sans sonde) | 42 |
| PROFID EHRA | Essai randomisé européen, post-infarctus avec FEVG réduite : traitement médical seul ou avec DAI | 19 |
| DILEMMA | Essai randomisé, DAI en prévention primaire chez les plus de 70 ans | 18 |
| HERO | Essai randomisé, télésurveillance HeartLogic™ contre suivi classique | 15 |
| HEARTLOGIC | Étude nationale, insuffisants cardiaques avec algorithme HeartLogic | non listé |
| ALLEGRO | Trajectoires de soins en vie réelle dans la base nationale (SNDS) | non listé |

- **Ampleur du réseau** (calculée à partir de la liste publique) : **154 centres distincts** et **362 couples étude-centre** [F]. Beaucoup de centres participent à **5 à 8 études du réseau en même temps** (CHU de Poitiers, Grenoble, Amiens, La Timone, HEGP, Pitié-Salpêtrière, Clinique Pasteur…) [F].
- **Axes affichés** : prédiction de la mort subite (modèles de stratification du risque, algorithmes prédictifs) et évaluation des technologies, y compris des « outils de diagnostic basés sur l'IA » [F].

---

## 2. Ce que ça change par rapport à KAIROS (lecture critique)

KAIROS a été pensé pour des **essais interventionnels à visites protocolisées** : fenêtres, washouts, médicaments interdits, amendements. Or **DAI-PP est surtout un réseau de cohortes observationnelles de long terme**, avec trois essais randomisés. Plaquer KAIROS tel quel serait une erreur.

| Hypothèse de KAIROS | Réalité DAI-PP | Conséquence |
|---|---|---|
| Visites rapprochées, protocole très prescriptif | Cohortes : suivi long, souvent calqué sur le soin courant et la télésurveillance [F/H] | Le module « fenêtres et médicaments interdits » ne sert surtout qu'à DILEMMA, PROFID et HERO. |
| Une étude, des dizaines de centres | **Un réseau de 8 à 10 études, 154 centres, des centres engagés dans jusqu'à 8 études** [F] | La bonne unité n'est pas l'étude : c'est **le centre et le patient implanté, toutes études confondues**. |
| Données issues de l'EDC et du dossier patient | **Télécardiologie** : des flux en continu provenant des plateformes de plusieurs fabricants [F/H] | Le gisement de valeur, ce sont **les événements détectés à distance**. |
| Déviations, le problème n° 1 | Pour une cohorte, ce sont plutôt **l'exhaustivité du recrutement, la complétude sur 10 ans, les perdus de vue, la qualification des événements** [H] | La qualité se joue sur la **complétude** et l'**adjudication**, plus que sur la conformité aux visites. |
| Turnover, un problème parmi d'autres | **Un suivi sur 10 ans**, c'est la quasi-certitude que les ARC, TEC et infirmiers de télécardiologie changeront dans chaque centre [H] | La **mémoire du réseau** devient centrale. |

**Conclusion :** le cœur de KAIROS reste valable (compiler les protocoles en règles exécutables et tenir à jour l'état de chaque patient). Mais pour DAI-PP, il doit être réorienté vers **trois problèmes propres à un réseau de cohortes de dispositifs implantables**.

---

## 3. Le concept adapté : **KAIROS Rythme**, le système d'exploitation d'un réseau de cohortes

> *Pour chaque patient implanté, savoir dans quelle(s) étude(s) il doit entrer, ce qui lui arrive et ce qu'il manque, sur 10 ans, dans 154 centres.*

### Module 1 : Routeur d'inclusion à l'implantation
**Problème [H] :** au moment d'une implantation, le centre doit savoir à quelles études du réseau le patient est éligible. Selon le dispositif et le profil, il peut s'agir de HONEST (DAI sous-cutané), FOREVER (extravasculaire), AV-CESAR (Micra AV), DAI-T4F (Fallot), DILEMMA (plus de 70 ans en prévention primaire), PROFID (post-infarctus), HERO ou HEARTLOGIC (HeartLogic), et la cohorte DAI-PP. Dans un centre engagé dans 8 études, il est facile d'oublier une inclusion, d'utiliser la mauvaise notice d'information ou de mal articuler deux études.

**Fonctionnement :**
- Les critères de chaque protocole sont compilés en règles.
- À partir de quelques données d'implantation (type et modèle de dispositif, indication, âge, contexte), l'outil produit une **liste des études éligibles**, la **bonne notice d'information ou de non-opposition** dans sa version en vigueur, et les **compatibilités ou incompatibilités de co-inclusion**.
- L'investigateur valide. L'outil ne décide pas.

**Valeur :** exhaustivité du recrutement des cohortes. Pour une cohorte des « 1 000 premiers patients » ou des « 5 000 premiers », un oubli d'inclusion est un **biais de sélection**, pas un simple retard [H].

### Module 2 : Pipeline télécardiologie → événements d'étude → adjudication
**Problème [H] :** les critères de jugement du réseau (thérapies appropriées ou inappropriées du DAI, arythmies, mort subite, décompensations) sont **détectés d'abord par la télésurveillance**. Ces données arrivent sur **plusieurs plateformes de fabricants**, chacune avec son format. Les transformer en événements d'étude, puis en dossiers pour le comité d'adjudication (tracés d'électrogramme, contexte clinique), est un travail manuel, lent et hétérogène d'un centre à l'autre.

**Fonctionnement :**
- **Extraction multimodale** des rapports de transmission (PDF, tracés) pour en tirer un événement candidat.
- **Dédoublonnage** et rattachement au bon patient et aux bonnes études.
- **Dossier d'adjudication pré-assemblé** (tracés, contexte, données manquantes signalées).
- Pré-classification **indicative**, par exemple « probablement inappropriée, compatible avec une sur-détection d'onde T », **toujours tranchée par les adjudicateurs**.

**Valeur :** délai entre l'événement et sa qualification, homogénéité entre centres, charge des infirmiers et ARC de télécardiologie. C'est aussi **le module le plus aligné sur l'axe « IA et prédiction » affiché par le réseau** [F].

**Point de vigilance majeur :** on reste strictement dans l'usage **recherche**, pour qualifier un critère de jugement. Si l'outil servait à la prise en charge (alerter un médecin pour traiter), il deviendrait très probablement un **dispositif médical** (règlement MDR). Il faut l'écrire noir sur blanc dans la conception.

### Module 3 : Moteur de complétude longitudinale (10 ans)
**Problème [H] :** sur une cohorte de 10 ans, la valeur scientifique dépend de la **complétude** : statut vital, transmissions interrompues (patient déconnecté, boîtier non transmis), changements de dispositif (explantation, changement de boîtier, passage d'un DAI sous-cutané à un DAI endocavitaire), patients perdus de vue, déménagements entre centres.

**Fonctionnement :**
- Un jumeau de chaque patient indique ce qu'on sait, ce qu'on devrait savoir et ce qui manque, avec une **liste de travail priorisée** par centre. Exemples : « 23 patients sans transmission depuis plus de 90 jours », « 4 changements de boîtier non documentés ».
- Pour la partie **ALLEGRO / SNDS**, l'outil ne lit pas la base nationale : il **prépare et contrôle la cohérence** des éléments transmis via les circuits réglementaires autorisés.

**Valeur :** moins de données manquantes, donc plus de puissance statistique. C'est mesurable en pilote : taux de complétude avant et après.

### Module 4 : Mémoire du réseau et clarifications partagées
**Problème [H] :** avec 154 centres et une équipe qui change sur 10 ans, la même question est posée des dizaines de fois au centre coordinateur (« Ce patient implanté avant la date X entre-t-il dans HONEST ? », « Comment saisir un changement de boîtier ? »). Les réponses restent dans des mails.

**Fonctionnement :** les questions sont reliées aux règles des protocoles. Une réponse validée par le centre coordinateur est publiée à **tous** les centres concernés, versionnée. Quand une personne arrive dans un centre, l'outil génère **automatiquement** son dossier de prise de poste.

**Valeur :** moins de sollicitations pour l'équipe de coordination et moins d'erreurs à chaque arrivée. C'est le module **le plus simple à construire et le plus rapide à adopter**.

### Module 5 : KAIROS classique pour les essais randomisés
Pour **DILEMMA, PROFID EHRA et HERO**, on retrouve l'usage d'origine : échéancier par patient, version applicable du protocole, impact patient par patient des amendements, rappels de conformité.

---

## 4. Priorisation

| Module | Douleur pour DAI-PP [H] | Effort technique | Rapidité de preuve | Priorité |
|---|---|---|---|---|
| 4. Mémoire et clarifications | Moyenne à forte | Faible | 2 à 3 mois | **1. Porte d'entrée** |
| 1. Routeur d'inclusion | Forte (exhaustivité des cohortes) | Moyen | 3 à 4 mois | **2** |
| 3. Complétude longitudinale | Forte | Moyen (dépend de l'accès aux données) | 4 à 6 mois | **3** |
| 2. Télécardiologie → adjudication | **Très forte, et différenciante** | **Élevé** (multi-fabricants, multimodal) | 6 à 12 mois | **4. Le cœur de la valeur à terme** |
| 5. KAIROS pour les essais randomisés | Moyenne (3 essais) | Moyen | 4 à 6 mois | 5 |

**Recommandation :** commencer par les modules 4 et 1, qui demandent peu de données sensibles, sont rapides et sont visibles par tous les centres. Ils servent à gagner la confiance du réseau. Le module 2 se construit ensuite, avec les données et les adjudicateurs du réseau. C'est **lui** qui a un potentiel au-delà de DAI-PP.

---

## 5. Pourquoi DAI-PP est un terrain pilote exceptionnel [H]

- **Un seul promoteur académique (Inserm), un réseau, 154 centres** : on peut tester un outil multi-centres sans négocier avec dix promoteurs.
- **Un domaine où les données sont déjà numériques et continues** (télécardiologie) : c'est rare en recherche clinique.
- **Une forte cohérence de domaine** (dispositifs de rythmologie) : le vocabulaire, les événements et les critères de jugement se ressemblent d'une étude à l'autre, ce qui rend les règles réutilisables.
- **Un réseau international** (PROFID est européen, partenariat EHRA [F]) : une porte vers l'Europe.
- **Un débouché naturel au-delà de DAI-PP** : les autres réseaux de cohortes de dispositifs implantables (cardiologie, neurostimulation, etc.), les registres de matériovigilance, et les **fabricants de dispositifs**, qui ont des obligations de **suivi clinique après commercialisation** au titre du MDR [H, à étudier].

---

## 6. Les points juridiques à régler AVANT d'écrire du code

Ce point est le plus important de ce document.

1. **Propriété intellectuelle.** En droit français, les droits sur un logiciel créé par un salarié dans l'exercice de ses fonctions appartiennent en principe à l'**employeur** (article L113-9 du Code de la propriété intellectuelle). Si vous développez cet outil dans le cadre de votre poste pour DAI-PP, il appartiendra très probablement à votre employeur (Inserm, AP-HP, association ou autre), pas à vous. Les options :
   - le développer **comme projet interne** et le revendiquer comme réalisation professionnelle ;
   - **négocier en amont** une création d'entreprise avec la structure de valorisation (Inserm Transfert pour l'Inserm ; la SATT ou le service de valorisation selon l'employeur), avec licence ou essaimage ;
   - le développer **hors de votre temps de travail, sans aucun moyen ni information de l'employeur**. Ce chemin est risqué si le sujet recoupe directement vos missions.
   → **À valider avec un juriste en propriété intellectuelle et avec votre employeur avant de commencer.**
2. **Données.** Aucune donnée de patient de DAI-PP ne doit être utilisée hors des cadres prévus : protocoles, notices d'information, autorisations CNIL ou méthodologies de référence, conventions. Un nouvel outil qui traite ces données doit figurer dans l'analyse d'impact (AIPD) et les registres de traitement du promoteur, et être hébergé chez un **hébergeur HDS**.
3. **Données des fabricants.** Les données de télésurveillance transitent par les plateformes des fabricants, avec leurs propres conditions contractuelles. Leur réutilisation automatisée doit être **vérifiée contractuellement**.
4. **Statut de dispositif médical.** Le module 2 doit rester un outil de **recherche** (qualification des critères de jugement). Il faut une analyse de qualification formelle (guide MDCG 2019-11).
5. **Confidentialité.** Les protocoles non publiés et les résultats intermédiaires ne doivent jamais être envoyés à un service d'IA externe sans accord et sans garanties contractuelles (pas de rétention, hébergement dans l'UE).

---

## 7. Plan d'action concret pour vous

| Quand | Action |
|---|---|
| **Semaine 1-2** | Clarifier votre position : outil interne ou future entreprise ? En parler à votre responsable et vous renseigner auprès de la structure de valorisation de votre employeur. |
| **Semaine 2-4** | 10 à 15 entretiens dans le réseau : ARC et TEC de centres multi-études, infirmiers de télécardiologie, équipe de coordination, membres du comité d'adjudication. Questions clés : combien de temps prennent les inclusions, combien d'oublis, combien de temps pour qualifier un événement, quelles questions reviennent ? |
| **Mois 1-3** | Prototype des modules 4 et 1 **sans données de patients** : uniquement les règles extraites des protocoles et des questions anonymisées. Test dans 3 à 5 centres volontaires. |
| **Mois 3-6** | Mesurer : sollicitations évitées, inclusions retrouvées, satisfaction. Présentation possible à la **réunion des investigateurs du réseau**. |
| **Mois 6-12** | Si les résultats sont là : cadrage réglementaire du module 2 et financement. Pistes : appels à projets Inserm ou ministériels sur l'innovation organisationnelle, Bpifrance, partenariat académique avec un laboratoire de traitement du signal. Le site cite le LTSI parmi ses partenaires [F]. |

---

## 8. Réponse courte

**Oui, c'est adaptable, et DAI-PP est même un meilleur terrain que la moyenne.** Pour ce réseau, KAIROS ne doit pas d'abord « empêcher les déviations de visite ». Il doit devenir le **système d'exploitation d'un réseau de cohortes de dispositifs implantables**, sur quatre fronts :
- ne manquer **aucune inclusion** à l'implantation ;
- transformer **automatiquement** les alertes de télécardiologie en événements d'étude prêts pour l'adjudication ;
- garantir la **complétude sur 10 ans** ;
- **ne rien perdre** quand les équipes changent.

La première étape n'est pas technique : c'est de **régler la question de la propriété intellectuelle avec votre employeur**, puis de valider la douleur par des entretiens dans le réseau.

---

### Sources
- [DAI-PP Network : site officiel](https://dai-pp.com/) (accueil, études, centres, publications, patients, équipe ; liste publique des centres)
- Étude principale : `docs/etude-innovation-recherche-clinique.md`
