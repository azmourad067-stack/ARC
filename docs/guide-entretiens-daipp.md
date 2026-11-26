# Guide d'entretiens de validation : réseau DAI-PP

**Objet :** vérifier, avant de construire quoi que ce soit, que les problèmes visés par KAIROS Rythme sont **réels, fréquents et coûteux** pour les équipes du réseau, et lesquels le sont le plus.
**Complément de :** `docs/adaptation-daipp.md`
**Version :** 1.0, 26/11/2026

---

## 1. Règles du jeu (à lire avant le premier entretien)

### 1.1 Ce qu'on cherche
Valider ou invalider **cinq hypothèses** (une par module) :

| # | Hypothèse à tester | Module |
|---|---|---|
| H1 | Les mêmes questions d'interprétation reviennent souvent, et les réponses se perdent (mails, départs). | 4. Mémoire et clarifications |
| H2 | À l'implantation, des patients éligibles à une étude du réseau ne sont pas inclus, ou mal orientés (mauvaise notice, mauvaise étude). | 1. Routeur d'inclusion |
| H3 | Maintenir la complétude du suivi (transmissions, changements de boîtier, statut vital) demande beaucoup de travail manuel, et des trous persistent. | 3. Complétude 10 ans |
| H4 | Transformer une alerte de télécardiologie en événement d'étude prêt pour l'adjudication est lent, manuel et hétérogène d'un centre à l'autre. | 2. Télécardiologie → adjudication |
| H5 | Dans les essais randomisés, les amendements et les fenêtres de visite créent des erreurs évitables. | 5. KAIROS d'origine |

### 1.2 Les cinq principes d'un bon entretien de validation
1. **Parler du passé, pas du futur.** On demande « Racontez-moi la dernière fois que… », pas « Est-ce que vous utiliseriez… ? ». Les gens sont polis sur le futur, mais précis sur le passé.
2. **Ne pas présenter la solution** avant la toute fin, ou pas du tout. Dès qu'on la décrit, l'interlocuteur cherche à faire plaisir.
3. **Chercher des chiffres et des exemples concrets** : combien de fois, combien de temps, la dernière occurrence, ce qui s'est passé ensuite.
4. **Écouter les contournements.** Un fichier Excel maison, un post-it ou un mail récapitulatif signalent un vrai problème. L'absence de contournement suggère un problème faible.
5. **Se taire.** Après une question, laisser le silence durer. Les meilleures informations arrivent après.

### 1.3 Cadre éthique et confidentialité (non négociable)
- **Aucune donnée de patient** ne doit être demandée, notée ou enregistrée : pas de nom, de numéro de patient, de date de naissance ni de détail permettant d'identifier quelqu'un. Si l'interlocuteur en cite, ne pas les noter.
- Ces entretiens portent sur **les pratiques professionnelles** et non sur des personnes malades. Ils ne relèvent *a priori* pas de la recherche impliquant la personne humaine. Vérifiez quand même ce point avec votre responsable ou le délégué à la protection des données (DPO) si vous comptez publier les résultats.
- **RGPD pour les personnes interviewées** : information orale au début (voir le script, partie 3), données minimales (fonction, type de centre, ancienneté), **notes anonymisées** (code E01, E02…), table de correspondance conservée à part puis détruite à la fin de l'analyse.
- **Enregistrement audio** : uniquement avec un accord explicite, et l'entretien doit pouvoir se faire sans. Pas de transcription par un service d'IA externe sans validation du DPO.
- **Pas d'évaluation des personnes ni des centres** : on cherche des problèmes de système, pas des fautes. Le dire explicitement : c'est la condition d'une parole franche.
- **Formaliser par écrit** (mail suffit) l'accord de votre responsable : objectif des entretiens, cadre (projet interne ou valorisation), utilisation des résultats.

---

## 2. Qui interroger

### 2.1 Échantillon cible : 14 entretiens
| Profil | Nombre | Pourquoi |
|---|---|---|
| ARC / TEC de centre **engagé dans 5 études du réseau ou plus** | 4 | Le cœur de la douleur multi-études (H1, H2, H3) |
| ARC / TEC de centre **engagé dans 1 à 2 études** | 2 | Point de comparaison : la douleur augmente-t-elle avec le nombre d'études ? |
| Infirmier(e) ou technicien(ne) de **télécardiologie** | 3 | H3 et H4 |
| **Cardiologue rythmologue investigateur** | 2 | H2 (moment de l'implantation), H4 |
| **Équipe de coordination** (chef de projet, ARC coordinateur, data manager) | 2 | H1 (questions reçues), H3 (complétude vue du centre coordinateur) |
| **Membre du comité d'adjudication** | 1 | H4 (qualité et délai des dossiers reçus) |

### 2.2 Diversité à rechercher
- **Types de centres** : CHU, centre hospitalier général, clinique privée. La liste publique compte des cliniques très actives (Clinique Pasteur, Ambroise Paré, Centre Cardiologique du Nord…).
- **Ancienneté** : au moins 2 personnes arrivées depuis moins d'un an (H1, choc de prise de poste) et 2 personnes avec plus de 5 ans d'ancienneté (contournements bien installés).
- **Géographie** : Paris et au moins 3 régions ; si possible un centre d'outre-mer (La Réunion figure dans la liste).

### 2.3 Message d'invitation (à adapter)

> **Objet :** 45 minutes pour améliorer le quotidien des équipes du réseau DAI-PP ?
>
> Bonjour [Prénom],
>
> Je suis [fonction] au sein du réseau DAI-PP. Avec l'accord de [responsable], je mène une série d'entretiens auprès des équipes des centres pour comprendre **ce qui vous fait perdre du temps ou vous inquiète** dans le suivi des études du réseau : inclusions, télécardiologie, suivi au long cours, questions sur les protocoles…
>
> Ce n'est **ni un audit ni une évaluation** de votre centre. Les échanges sont anonymisés et aucune donnée de patient n'est demandée.
>
> Auriez-vous 45 minutes, en visio ou par téléphone, dans les trois prochaines semaines ? Voici quelques créneaux : […]
>
> Merci d'avance,
> [Signature]

---

## 3. Déroulé type (45 minutes)

| Temps | Étape | Contenu |
|---|---|---|
| 0-5 min | **Ouverture** | Script ci-dessous ; accord pour l'enregistrement ou la prise de notes. |
| 5-10 min | **Contexte** | Rôle, centre, études suivies, outils utilisés. |
| 10-20 min | **Journée et semaine type** | Où part le temps, ce qui inquiète. |
| 20-38 min | **Approfondissement** | 2 ou 3 blocs thématiques selon le profil (partie 4). |
| 38-43 min | **Priorisation** | Exercice de classement (partie 5). |
| 43-45 min | **Clôture** | Personnes à recommander, autorisation de recontacter. |

### Script d'ouverture
> « Merci de prendre ce temps. L'objectif est de comprendre comment se passe concrètement votre travail sur les études du réseau, ce qui marche, ce qui coince. Il n'y a pas de bonne ou de mauvaise réponse, et ce n'est pas une évaluation de votre centre. Je ne note aucune donnée de patient ; si vous en citez par réflexe, je ne la noterai pas. Vos réponses seront anonymisées : je mettrai un code, pas votre nom. Êtes-vous d'accord pour que je prenne des notes [et pour que j'enregistre, uniquement pour moi, enregistrement détruit après analyse] ? »

---

## 4. Questions

> Les questions en **gras** sont prioritaires. Les relances (→) servent à creuser si la réponse reste générale.

### 4.0 Contexte (tous profils)
1. **Pouvez-vous décrire votre rôle et la part de votre temps consacrée aux études DAI-PP ?**
2. Sur combien d'études du réseau travaillez-vous en ce moment ? Et hors réseau ?
3. **Quels outils utilisez-vous au quotidien pour ces études ?** (eCRF, plateformes de télésurveillance des fabricants, dossier patient, Excel, classeurs, mails…)
   → Combien d'identifiants différents ? Lequel vous fait perdre le plus de temps ?
4. Depuis quand êtes-vous sur ces études ? Comment s'est passée votre prise de poste ?

### 4.1 Journée et semaine type (tous profils)
5. **Racontez-moi votre dernière semaine sur les études du réseau. Qu'avez-vous fait, dans l'ordre ?**
6. **Quelle tâche vous a pris le plus de temps cette semaine-là ? Combien d'heures environ ?**
7. Qu'est-ce qui vous inquiète le plus, la crainte d'avoir oublié quelque chose ?
   → Racontez la dernière fois où vous vous êtes rendu compte d'un oubli. Comment ? Quelles conséquences ?
8. Avez-vous créé vos propres outils (tableau, check-list, rappels) ? **Pouvez-vous me le décrire ?** (Demander une capture **sans données de patients** si possible.)

### 4.2 Bloc H1 : questions sur les protocoles et transmission (ARC/TEC, coordination)
9. **Quelle est la dernière question que vous avez posée (ou reçue) sur l'interprétation d'un protocole du réseau ?**
   → À qui ? Par quel canal ? Combien de temps pour avoir la réponse ? Où est-elle conservée aujourd'hui ?
10. Combien de questions de ce type par mois, à peu près ?
11. Vous est-il arrivé de vous reposer une question déjà résolue, par vous ou par un collègue ?
12. **Quand quelqu'un quitte l'équipe, qu'est-ce qui se perd ?** Racontez la dernière passation.
13. *(Coordination)* Quelles sont les questions qui reviennent le plus de la part des centres ? Combien de temps par semaine y consacrez-vous ?
14. *(Coordination)* Comment diffusez-vous une réponse valable pour tous les centres aujourd'hui ?

### 4.3 Bloc H2 : inclusion à l'implantation (ARC/TEC, rythmologue)
15. **Comment savez-vous aujourd'hui qu'un patient qui vient d'être implanté doit entrer dans une étude du réseau ?**
    → Qui repère ? À quel moment ? Avec quelle information (programme opératoire, compte rendu, discussion) ?
16. **Racontez la dernière fois qu'un patient éligible n'a pas été inclus, ou a été inclus tardivement.** Pourquoi ?
17. Combien d'inclusions manquées par trimestre, à votre avis ? Sur quelle base l'estimez-vous ?
18. Vous est-il arrivé d'utiliser une notice d'information dans une version périmée, ou la notice d'une autre étude ?
19. Comment gérez-vous un patient potentiellement concerné par plusieurs études du réseau ?
20. *(Rythmologue)* Au moment de l'implantation, quelle information sur les études aimeriez-vous avoir sous les yeux ? Sous quelle forme ?

### 4.4 Bloc H3 : complétude du suivi au long cours (ARC/TEC, télécardiologie, coordination)
21. **Comment savez-vous aujourd'hui qu'un patient de la cohorte « manque » des données ?**
22. **Racontez le dernier patient perdu de vue ou devenu silencieux en télésurveillance.** Comment l'avez-vous repéré, au bout de combien de temps, qu'avez-vous fait ?
23. Comment sont documentés les changements de dispositif (changement de boîtier, explantation, changement de type de dispositif) ?
    → Combien de temps entre l'événement et sa saisie dans l'étude ?
24. Comment obtenez-vous le statut vital des patients qui ne sont plus suivis dans votre centre ?
25. *(Coordination)* Quel est aujourd'hui le taux de complétude, ou le taux de données manquantes, qui vous préoccupe le plus ? Comment le mesurez-vous ?
26. Combien de temps par mois consacrez-vous à relancer, compléter ou corriger ?

### 4.5 Bloc H4 : de l'alerte de télécardiologie à l'événement d'étude (télécardiologie, ARC/TEC, rythmologue, adjudication)
27. **Décrivez pas à pas ce qui se passe entre une transmission montrant un choc (ou une thérapie) et son enregistrement comme événement dans l'étude.**
    → Qui voit l'alerte ? Sur quelle plateforme ? Qui décide que c'est un événement d'étude ? Comment les tracés sont-ils récupérés ? Sous quel format ? Combien de clics, de copies, d'exports ?
28. **Combien de temps cela prend-il pour un événement, du début à la fin ?** Et entre l'événement et sa saisie ?
29. Combien de plateformes de fabricants différentes utilisez-vous ? Lesquelles posent le plus de difficultés pour récupérer les informations ?
30. Racontez un événement qui a été saisi en retard, saisi deux fois, ou qui a échappé à l'étude.
31. *(Adjudication)* **Quelle proportion des dossiers reçus sont incomplets ?** Qu'est-ce qui manque le plus souvent ?
32. *(Adjudication)* Combien de temps passez-vous par dossier ? Qu'est-ce qui vous ferait gagner le plus de temps ?
33. *(Adjudication)* Les dossiers sont-ils présentés de la même façon d'un centre à l'autre ?
34. Que penseriez-vous d'une pré-classification indicative des événements (appropriés ou inappropriés), toujours tranchée par un humain ?
    → **À poser seulement en fin de bloc**, pour recueillir réticences et conditions de confiance.

### 4.6 Bloc H5 : essais randomisés (ARC/TEC de centres DILEMMA, PROFID, HERO)
35. **Racontez la dernière fois qu'une visite est sortie de sa fenêtre, ou qu'un examen prévu a été oublié.**
36. Comment avez-vous mis en œuvre le dernier amendement ? Combien de temps ? Qu'est-ce qui a été le plus pénible ?
37. Avez-vous eu des patients à re-consentir ? Comment les avez-vous identifiés ?
38. Comment calculez-vous les dates des prochaines visites aujourd'hui ?

---

## 5. Exercice de priorisation (5 minutes, tous profils)

Lire les cinq problèmes suivants **sans évoquer de solution**, puis demander :
1. « **Classez-les du plus pénible au moins pénible pour vous.** »
2. « Si un seul pouvait disparaître demain, lequel choisiriez-vous ? »
3. « Pour celui-là, combien d'heures par mois vous ferait-il gagner, à peu près ? »

| Lettre | Problème |
|---|---|
| A | Retrouver la réponse à une question sur un protocole, ou transmettre ce qu'on sait quand on change d'équipe. |
| B | Ne pas rater l'inclusion d'un patient implanté dans la bonne étude, avec la bonne notice. |
| C | Garder un suivi complet des patients sur des années (transmissions, changements de dispositif, statut vital). |
| D | Transformer les alertes de télécardiologie en événements d'étude et en dossiers d'adjudication. |
| E | Respecter les fenêtres de visite et appliquer correctement les amendements dans les essais randomisés. |

---

## 6. Clôture (2 minutes)
- « Y a-t-il une question que je ne vous ai pas posée et que j'aurais dû poser ? »
- « Qui d'autre dans le réseau devrais-je absolument interroger ? »
- « Puis-je revenir vers vous dans quelques mois pour vous montrer une maquette ? »

> Si l'interlocuteur dit « Ce serait génial d'avoir un outil pour ça ! », ce n'est **pas** une validation. Une vraie validation, c'est : il décrit un contournement coûteux, il donne un chiffre, il accepte d'être testeur, il vous recommande quelqu'un.

---

## 7. Fiche de prise de notes (une par entretien)

```
Code entretien : E__        Date : __/__/____     Durée : ___ min
Profil : ☐ ARC/TEC multi-études  ☐ ARC/TEC 1-2 études  ☐ Télécardiologie
         ☐ Rythmologue  ☐ Coordination  ☐ Adjudication
Type de centre : ☐ CHU  ☐ CH  ☐ Privé     Région : ________
Nb études réseau : __     Ancienneté sur le poste : ___ ans
Outils cités : ______________________________________________

HYPOTHÈSES — preuves entendues (citer des faits, pas des opinions)
H1 Clarifications/mémoire : ___________________________________
   Fréquence : ____ /mois      Temps : ____ h/mois
H2 Inclusion :              ___________________________________
   Inclusions manquées estimées : ____ /trimestre
H3 Complétude :             ___________________________________
   Temps relances : ____ h/mois
H4 Télécardio→adjudication: ___________________________________
   Temps par événement : ____ min     Nb plateformes : ____
H5 Essais randomisés :      ___________________________________

Contournements maison observés : ______________________________
Citation marquante (anonymisée) : « ____________________________ »
Classement A–E : 1.__ 2.__ 3.__ 4.__ 5.__   Problème n°1 : __  Gain estimé : ___ h/mois
Intensité perçue (1 = gêne, 5 = douleur aiguë) : H1 _ H2 _ H3 _ H4 _ H5 _
Accepte d'être testeur : ☐ oui ☐ non     Recommandations : _________
Surprise / ce qui contredit mes hypothèses : ______________________
```

---

## 8. Synthèse et critères de décision

### 8.1 Tableau de synthèse (à remplir après les 14 entretiens)

| Hypothèse | Nb d'entretiens avec un **exemple concret récent** | Intensité moyenne (1-5) | Rang moyen (A-E) | Heures/mois citées (médiane) | Contournements observés | Verdict |
|---|---|---|---|---|---|---|
| H1 | | | | | | |
| H2 | | | | | | |
| H3 | | | | | | |
| H4 | | | | | | |
| H5 | | | | | | |

### 8.2 Règles de décision (fixées **avant** les entretiens, pour ne pas se mentir)

Une hypothèse est **validée** si au moins 3 de ces 4 conditions sont remplies :
1. Au moins **la moitié des personnes concernées** ont donné un **exemple concret datant de moins de 6 mois**.
2. Intensité moyenne **≥ 3,5 / 5**.
3. Au moins **3 contournements maison** décrits.
4. Une médiane **≥ 4 heures par mois** par personne, ou un impact sur la qualité scientifique clairement décrit (inclusions manquées, données manquantes, événements perdus).

**Décisions :**
- **H1 ou H2 validée** → construire le premier prototype sur ce module (sans données de patients).
- **H4 validée avec force**, surtout si l'adjudication confirme des dossiers incomplets → c'est le cœur de valeur à long terme : lancer le cadrage réglementaire et technique.
- **Aucune hypothèse validée** → **ne pas construire**. Relire les « surprises » des fiches : le vrai problème est peut-être ailleurs, et c'est un résultat précieux.
- **Problème inattendu cité par 5 personnes ou plus** → nouvelle hypothèse à explorer en priorité.

### 8.3 Livrable de restitution (à présenter à votre responsable)
1. Une page : les 3 problèmes les plus douloureux, avec chiffres et citations anonymisées.
2. Les hypothèses validées et invalidées, en appliquant les règles de la partie 8.2.
3. La proposition de premier prototype et de 3 à 5 centres testeurs volontaires.
4. Les points ouverts : juridique et propriété intellectuelle, données, statut de dispositif médical.

---

## 9. Calendrier conseillé

| Semaine | Action |
|---|---|
| S1 | Valider ce guide avec votre responsable ; confirmer par écrit le cadre ; faire 1 entretien test et ajuster les questions. |
| S2-S4 | Mener les 13 autres entretiens (4 à 5 par semaine maximum, avec 30 minutes de mise au propre juste après chacun). |
| S5 | Synthèse (partie 8), restitution à votre responsable. |
| S6 | Décision : prototype, approfondissement ou abandon. |
