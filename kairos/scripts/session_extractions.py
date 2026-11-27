"""Extractions réalisées « à la main » par Claude pendant la session de conception (27/11/2026),
à partir de la lecture des PDF (texte + images des tableaux), SANS appel API.

Elles jouent le rôle de la sortie attendue de kairos.extract_llm pour le test H3 :
- ancrage automatique : python -m kairos.cli verify ...
- validation humaine : à faire par un ARC (voir docs/recherche-clinique/TEST-H3.md).

Exécution : python scripts/session_extractions.py  (écrit data/extractions/*.json)
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from kairos.schema import Ambiguity, Arm, Procedure, SourceRef as S, StudyModel, Visit, VisitNote as N  # noqa: E402

OUT = ROOT / "data" / "extractions"


# ---------------------------------------------------------------------------
# 1. NCT02564523 — Janssen, vaccin Ebola, phase II (promoteur industriel)
# ---------------------------------------------------------------------------
def janssen() -> StudyModel:
    nct = "NCT02564523"
    boost_day = {"G1": 29, "G2": 57, "G3": 85}
    visits = [
        Visit(id="SCR", label="Screening (≤8 weeks)", anchor="PRIME", offset_days=-28,
              window_minus_days=28, window_plus_days=28,
              sources=[S(page=27, quote="(≤8 weeks)")]),
        Visit(id="PRIME", label="Day 1 – Prime vaccination", anchor=None, is_dosing=True,
              sources=[S(page=27, quote="Study Vaccine Administration")]),
        Visit(id="PP7", label="Day 8 – 7 days post-prime", anchor="PRIME", offset_days=7,
              window_minus_days=2, window_plus_days=2,
              sources=[S(page=79, quote="Seven Days Post-prime Vaccination Day 8 for all groups ±2 days")]),
        Visit(id="PP14", label="Day 15 – 14 days post-prime", arm_ids=["G2", "G3"], anchor="PRIME", offset_days=14,
              window_minus_days=2, window_plus_days=2,
              sources=[S(page=79, quote="Fourteen Days Post-prime Vaccination Day 15 for Group 2 ±2 days")]),
        Visit(id="Y1", label="Day 365 – 1 year post-prime", anchor="PRIME", offset_days=364,
              window_minus_days=30, window_plus_days=30,
              sources=[S(page=79, quote="Follow-up 1 Year Post-prime Day 365 for all groups ±30 days")]),
    ]
    for g, bd in boost_day.items():
        gi = g[1]
        visits += [
            Visit(id=f"BOOST_{g}", label=f"Day {bd} – Boost vaccination", arm_ids=[g], anchor="PRIME",
                  offset_days=bd - 1, window_minus_days=3, window_plus_days=3, is_dosing=True,
                  sources=[S(page=79, quote=f"Day {bd} for Group {gi}"), S(page=79, quote="Boost Vaccination")]),
            Visit(id=f"PB7_{g}", label=f"Day {bd + 7} – 7 days post-boost", arm_ids=[g], anchor=f"BOOST_{g}",
                  offset_days=7, window_minus_days=2, window_plus_days=2,
                  sources=[S(page=79, quote=f"Day {bd + 7} for Group {gi}")]),
            Visit(id=f"PB21_{g}", label=f"Day {bd + 21} – 21 days post-boost", arm_ids=[g], anchor=f"BOOST_{g}",
                  offset_days=21, window_minus_days=3, window_plus_days=3,
                  sources=[S(page=79, quote=f"Day {bd + 21} for Group {gi}")]),
            Visit(id=f"PB42_{g}", label=f"Day {bd + 42} – 42 days post-boost", arm_ids=[g], anchor=f"BOOST_{g}",
                  offset_days=42, window_minus_days=3, window_plus_days=3,
                  sources=[S(page=79, quote=f"Day {bd + 42} for Group {gi}")]),
            Visit(id=f"PB6M_{g}", label=f"Day {bd + 180} – 6 months post-boost", arm_ids=[g], anchor=f"BOOST_{g}",
                  offset_days=180, window_minus_days=15, window_plus_days=15,
                  sources=[S(page=79, quote=f"Day {bd + 180} for Group {gi}")]),
        ]
    G = ["G1", "G2", "G3"]
    B = [f"BOOST_{g}" for g in G]

    def per(prefix: str) -> list[str]:
        return [f"{prefix}_{g}" for g in G]

    procs = [
        Procedure(id="ICF", label="Informed consent/assent", visit_ids=["SCR"], sources=[S(page=27, quote="Informed consent/assent")]),
        Procedure(id="IE", label="Inclusion/exclusion criteria", visit_ids=["SCR"], sources=[S(page=27, quote="Inclusion/exclusion criteria")]),
        Procedure(id="TOU", label="Test of Understanding (TOU)", visit_ids=["SCR"], condition="après lecture, avant signature du consentement",
                  sources=[S(page=27, quote="Test of Understanding (TOU)")]),
        Procedure(id="ECG", label="Electrocardiogram (ECG)", visit_ids=["SCR"], condition="sujets ≥18 ans (cohortes 1 et 2a)",
                  sources=[S(page=27, quote="Electrocardiogram (ECG)")]),
        Procedure(id="RAND", label="Randomization", visit_ids=["PRIME"], sources=[S(page=27, quote="Randomization")]),
        Procedure(id="VAX", label="Study vaccine administration", visit_ids=["PRIME", *B],
                  sources=[S(page=27, quote="Study Vaccine Administration")]),
        Procedure(id="UPT", label="Urine pregnancy test", visit_ids=["PRIME", *B], condition="avant vaccination",
                  sources=[S(page=27, quote="Urine Pregnancy test")]),
        Procedure(id="PE", label="Physical examination",
                  visit_ids=["SCR", "PRIME", "PP7", *B, *per("PB7"), *per("PB21"), *per("PB42"), *per("PB6M"), "Y1"],
                  visit_notes=[N(visit_id=x, note="avant vaccination") for x in ["PRIME", *B]],
                  sources=[S(page=27, quote="Physical examination")]),
        Procedure(id="VS", label="Vital signs", visit_ids=["SCR", "PRIME", *B], sources=[S(page=27, quote="Vital signs")]),
        Procedure(id="DIARY_DIST", label="Distribution of subject diary", visit_ids=["PRIME", *B],
                  sources=[S(page=27, quote="Distribution of subject diary")]),
        Procedure(id="DIARY_REV", label="Review of diary by site staff", visit_ids=["PP7", *per("PB7")],
                  sources=[S(page=27, quote="Review of diary by site staff")]),
        Procedure(id="CHEM", label="Chemistry, hematology (10 mL)", visit_ids=["SCR", "PRIME", "PP7", *B, *per("PB7")],
                  sources=[S(page=28, quote="Chemistry, hematology (10 mL)")]),
        Procedure(id="CD4", label="CD4+ cell count (2 mL)", visit_ids=["SCR", "PRIME", *B, *per("PB42")],
                  condition="sujets VIH+ uniquement", sources=[S(page=28, quote="CD4+ cell count (2 mL)")]),
        Procedure(id="UA", label="Urinalysis", visit_ids=["SCR"], sources=[S(page=28, quote="Urinalysis")]),
        Procedure(id="SERUM", label="Blood sampling (serum) – humoral immunity (10 mL)",
                  visit_ids=["PRIME", "PP14", *B, *per("PB7"), *per("PB21"), *per("PB6M"), "Y1"],
                  visit_notes=[N(visit_id=x, note="cohortes 1 et 2a uniquement") for x in per("PB7")]
                  + [N(visit_id=x, note="avant vaccination") for x in ["PRIME", *B]],
                  sources=[S(page=28, quote="assessment of humoral immune")]),
        Procedure(id="PBMC", label="Blood sampling (PBMC) – cellular immunity (40 or 20 mL)",
                  visit_ids=["PRIME", "PP14", *B, *per("PB7"), *per("PB21"), *per("PB6M"), "Y1"],
                  condition="centres sélectionnés",
                  visit_notes=[N(visit_id=x, note="cohortes 1 et 2a uniquement") for x in per("PB7")]
                  + [N(visit_id=x, note="avant vaccination") for x in ["PRIME", *B]],
                  sources=[S(page=28, quote="assessment of cellular immune")]),
    ]
    amb = [
        Ambiguity(description=(
            "Les fenêtres (Table 3, p.79) sont exprimées en jours d'étude comptés depuis le Day 1 (ex. « Day 36 for Group 1 »), "
            "alors que le tableau des visites exprime les visites post-rappel relativement au rappel (« +7d pb »). "
            "Si le rappel est fait à J31 (dans sa fenêtre ±3 j), la visite post-rappel est-elle due à J36 ou J38 ? "
            "KAIROS ancre sur la date réelle du rappel : choix à confirmer par le promoteur."),
            sources=[S(page=79, quote="Seven Days Post-boost Vaccination Day 36 for Group 1 ±2 days"),
                     S(page=28, quote="d pp: days post-prime; d pb: days post-boost")]),
        Ambiguity(description=(
            "Les fenêtres de visite ne figurent pas dans le tableau des visites (p.27-28) mais dans une table séparée "
            "52 pages plus loin (p.79), et une autre table (Table 6, section 9.1.7) s'applique à la sous-étude de la cohorte 1."),
            sources=[S(page=79, quote="Refer to Table 6 (Section 9.1.7) for the visit windows that will be allowed for the Cohort 1 substudy.")]),
    ]
    return StudyModel(
        nct_id=nct, title="Ad26.ZEBOV / MVA-BN-Filo prime-boost (VAC52150EBL2002)", sponsor="Janssen Vaccines & Prevention B.V.",
        protocol_version="Amendment 3", protocol_date="2017-05-04", day_convention="day1",
        arms=[Arm(id="G1", label="Group 1 – boost J29"), Arm(id="G2", label="Group 2 – boost J57"), Arm(id="G3", label="Group 3 – boost J85 (cohorte 1)")],
        visits=visits, procedures=procs, ambiguities=amb,
        extraction_notes=("Périmètre : cohorte 1 et cohortes 2a/2b (tableau p.27-28). Cohortes 3/4, sous-étude et rappels tardifs non modélisés. "
                          "La couche texte du PDF perd l'alignement des colonnes du tableau : lecture de l'image nécessaire."),
    )


# ---------------------------------------------------------------------------
# 2. NCT02886624 — IMEA / SAHIV, hépatite C aiguë (promoteur académique français)
# ---------------------------------------------------------------------------
def imea() -> StudyModel:
    nct = "NCT02886624"
    visits = [
        Visit(id="SCR", label="Screening (D-28 à D-7)", anchor="D0", offset_days=-14, window_minus_days=14, window_plus_days=7,
              conditional="uniquement si les résultats biologiques d'éligibilité ne sont pas disponibles (1 à 4 semaines avant D0)",
              sources=[S(page=28, quote="This visit will take place from D-28 to D-7 before the inclusion visit (D0)."),
                       S(page=31, quote="+7/-14 days for screening visit,")]),
        Visit(id="D0", label="D0 – Inclusion, début du traitement", anchor=None, is_dosing=True,
              sources=[S(page=27, quote="Screeninga D0 W4 W8 PT4 PT12 PT48")]),
        Visit(id="W4", label="W4", anchor="D0", offset_days=28, window_minus_days=7, window_plus_days=7,
              sources=[S(page=31, quote="+/-7 days for visits W4, W8, PT4, PT12, and PT48.")]),
        Visit(id="W8", label="W8 – fin de traitement", anchor="D0", offset_days=56, window_minus_days=7, window_plus_days=7,
              sources=[S(page=15, quote="Anti-HCV treatment: 8 weeks"),
                       S(page=31, quote="+/-7 days for visits W4, W8, PT4, PT12, and PT48.")]),
        Visit(id="PT4", label="PT4 – 4 semaines post-traitement (SVR4)", anchor="W8", offset_days=28, window_minus_days=7, window_plus_days=7,
              sources=[S(page=31, quote="+/-7 days for visits W4, W8, PT4, PT12, and PT48.")]),
        Visit(id="PT12", label="PT12 – 12 semaines post-traitement (SVR12, critère principal)", anchor="W8", offset_days=84,
              window_minus_days=7, window_plus_days=7,
              sources=[S(page=31, quote="+/-7 days for visits W4, W8, PT4, PT12, and PT48.")]),
        Visit(id="PT48", label="PT48 – 48 semaines post-traitement (fin de suivi)", anchor="W8", offset_days=336,
              window_minus_days=7, window_plus_days=7,
              sources=[S(page=31, quote="The theoretical date of end of patient follow-up in the study is PT48."),
                       S(page=15, quote="Follow up: 48 weeks following the end of the treatment")]),
    ]
    ALL = ["SCR", "D0", "W4", "W8", "PT4", "PT12", "PT48"]
    procs = [
        Procedure(id="ICF", label="Eligibility criteria / Informed Consent", visit_ids=["SCR"],
                  visit_notes=[N(visit_id="SCR", note="à faire à D0 si la visite de screening n'a pas lieu")],
                  sources=[S(page=27, quote="Eligibility criteria / Informed Consent")]),
        Procedure(id="EXAM", label="Clinical examination (sitting BP, weight)", visit_ids=ALL,
                  sources=[S(page=27, quote="Clinical examination (including sitting blood pressure,")]),
        Procedure(id="CONMED", label="Concomitant treatments", visit_ids=ALL[:5],
                  sources=[S(page=27, quote="Concomitant treatments (After 30 days post-study")]),
        Procedure(id="AE", label="Serious or not serious adverse events", visit_ids=ALL[:5], condition="jusqu'à 30 jours après la fin du traitement",
                  sources=[S(page=27, quote="Serious or not serious adverse events (until 30 days")]),
        Procedure(id="GENO", label="HCV Genotype", visit_ids=["SCR"], sources=[S(page=27, quote="HCV Genotype")]),
        Procedure(id="HCVRNA", label="HCV RNA", visit_ids=ALL, visit_notes=[N(visit_id="PT48", note="si positif : analyse phylogénétique (rechute vs réinfection)")],
                  sources=[S(page=27, quote="HCV RNA")]),
        Procedure(id="HCVAB", label="HCV antibodies (ELISA and Rapid test)", visit_ids=["D0", "W4"],
                  condition="première infection aiguë uniquement",
                  visit_notes=[N(visit_id="W4", note="seulement si négatif à D0")],
                  sources=[S(page=27, quote="HCV antibodies (ELISA and Rapid test)")]),
        Procedure(id="HIVAB", label="HIV antibodies", visit_ids=["SCR"], condition="patients mono-infectés VHC uniquement",
                  sources=[S(page=27, quote="HIV antibodies (only for HCV mono-infected patients)")]),
        Procedure(id="HBS", label="HBs Ag", visit_ids=["SCR"], condition="seulement si aucun résultat ≤ 3 mois avant D0",
                  sources=[S(page=27, quote="HBs Agc")]),
        Procedure(id="LFT", label="AST, ALT, total and conjugated bilirubin, GGT, ALP", visit_ids=ALL,
                  sources=[S(page=27, quote="AST, ALT, Total and cinjugated bilirubin, GGT, ALP")]),
        Procedure(id="CD4", label="CD4, CD8", visit_ids=["D0", "PT12"], condition="co-infectés VIH uniquement",
                  sources=[S(page=27, quote="CD4, CD8 (only for HIV co-infected patients)")]),
        Procedure(id="HIVRNA", label="HIV RNA", visit_ids=["D0", "PT12"], condition="co-infectés VIH uniquement",
                  sources=[S(page=27, quote="HIV RNA (only for HIV co-infected patients)")]),
        Procedure(id="FBC", label="FBC, platelets", visit_ids=ALL[:6], sources=[S(page=27, quote="FBC, platelets")]),
        Procedure(id="CREAT", label="Blood creatinine and creatinine clearance (CKD-EPI)", visit_ids=ALL[1:6],
                  sources=[S(page=27, quote="Blood creatinine and creatine clearance (CKD-EPI)")]),
        Procedure(id="PREG", label="Beta-HCG (screen) or urinary pregnancy test", visit_ids=ALL[:6], condition="si applicable",
                  sources=[S(page=27, quote="Beta-HCG (Screen) or urinary pregnancy test (if")]),
        Procedure(id="ADH", label="Adherence self-questionnaire", visit_ids=["W4", "W8"], sources=[S(page=27, quote="Adherence self-questionnaire")]),
        Procedure(id="QOL", label="Quality of life questionnaire", visit_ids=["D0", "PT12"], sources=[S(page=27, quote="“Quality of life” Questionnaire")]),
        Procedure(id="SERUM", label="Blood for serum collection (7/8 mL, dry tubes)", visit_ids=ALL[1:],
                  sources=[S(page=27, quote="Blood for serum collection (7/8 mL in dry tubes)")]),
        Procedure(id="PLASMA", label="Blood for plasma collection (7/8 mL, EDTA)", visit_ids=ALL[1:],
                  sources=[S(page=27, quote="Blood for plasma collection (7/8 mL in EDTA tubes)")]),
        Procedure(id="DISP", label="Treatment dispensation/return (grazoprevir/elbasvir)", visit_ids=["D0", "W4", "W8"],
                  sources=[S(page=27, quote="Grazoprevir / Elbasvir")]),
    ]
    amb = [
        Ambiguity(description=("Coquille dans la description des visites post-traitement : « Quality of life questionnaire (only at and PT12) » — "
                               "un mot manque. Le tableau des visites indique D0 et PT12 ; KAIROS retient le tableau."),
                  sources=[S(page=31, quote="“Quality of life” questionnaire (only at and PT12)")]),
        Ambiguity(description=("Les visites PT sont définies après la fin du traitement. En cas d'arrêt prématuré du traitement, "
                               "le protocole ne dit pas explicitement si PT4/PT12/PT48 se calculent depuis la date réelle d'arrêt ou depuis W8 théorique. "
                               "KAIROS ancre sur la visite W8 : à adapter si arrêt précoce."),
                  sources=[S(page=15, quote="Follow up: 48 weeks following the end of the treatment")]),
    ]
    return StudyModel(
        nct_id=nct, title="SAHIV – Short duration therapy of acute hepatitis C (grazoprevir/elbasvir 8 weeks)",
        sponsor="Institut de Médecine et d'Épidémiologie Appliquée (IMEA)", protocol_version="5.0", protocol_date="2018-01-19",
        day_convention="day0", visits=visits, procedures=procs, ambiguities=amb,
        extraction_notes="Tableau des visites lisible dans la couche texte (p.27). Fenêtres trouvées en section 9.8 (p.31).",
    )


# ---------------------------------------------------------------------------
# 3. NCT02453048 — INSERM, vaccin coqueluche BPZE1 phase Ib (promoteur Inserm)
# ---------------------------------------------------------------------------
def inserm() -> StudyModel:
    nct = "NCT02453048"
    V = lambda i, lab, off, m, p, src, **kw: Visit(id=i, label=lab, anchor="V2", offset_days=off,  # noqa: E731
                                                   window_minus_days=m, window_plus_days=p, sources=src, **kw)
    visits = [
        V("V1", "Visit 1 – screening (1 à 6 semaines avant V2)", -7, 35, 0,
          [S(page=10, quote="Visit 1 (screening 1-6 weeks before vaccination)")]),
        Visit(id="V2", label="Visit 2 – Day 0, vaccination", anchor=None, is_dosing=True,
              sources=[S(page=10, quote="Visit 2 (day 0, the day of vaccination)")]),
        V("V3", "Visit 3 – Day 4 ±1", 4, 1, 1, [S(page=10, quote="Visit 3 (4±1 days after vaccination)")]),
        V("V4", "Visit 4 – Day 7 ±1", 7, 1, 1, [S(page=10, quote="Visit 4 (7±1 days after vaccination)")]),
        V("V5", "Visit 5 – Day 11 ±1", 11, 1, 1, [S(page=11, quote="Visit 5 (11±1 days after vaccination)")]),
        V("V6", "Visit 6 – Day 14 ±1", 14, 1, 1, [S(page=11, quote="Visit 6 (14±1 days after vaccination)")]),
        V("V7", "Visit 7 – Day 21 ±1", 21, 1, 1, [S(page=11, quote="Visit 7 (21±1 days after vaccination)")]),
        V("V8", "Visit 8 – Day 28 (-1 ; +7)", 28, 1, 7, [S(page=11, quote="Visit 8 (28 (-1;+7) days after vaccination)")]),
        V("V8b", "Visit 8' – Day 45 (-5 ; +10)", 45, 5, 10,
          [S(page=31, quote="Visit 8’, 45 (-5;+10) days after visit 2")],
          conditional="uniquement si la culture nasopharyngée de J28 est positive"),
        V("V9", "Visit 9 – Month 6 ±1 month", 182, 30, 30, [S(page=11, quote="Visit 9 (6±1 months after vaccination)")]),
    ]
    ALL = [v.id for v in visits]
    post = ALL[1:]
    procs = [
        Procedure(id="REC", label="Recruitment, medical record number, screen form", visit_ids=["V1"],
                  sources=[S(page=16, quote="Recruitment, Medical record number, Screen")]),
        Procedure(id="ICF", label="Information and study consent", visit_ids=["V1"], condition="avant toute procédure spécifique",
                  sources=[S(page=16, quote="Information and study consent")]),
        Procedure(id="DEMO", label="Demographic information", visit_ids=["V1"], sources=[S(page=16, quote="Demographic information (age, gender,")]),
        Procedure(id="VAX", label="Vaccination", visit_ids=["V2"], condition="surveillance 6 h sur site après administration",
                  sources=[S(page=16, quote="Vaccination:"), S(page=29, quote="The subject should stay at the clinic for 6 hours after administration of the vaccine")]),
        Procedure(id="MH", label="Complete medical history", visit_ids=["V1"], sources=[S(page=16, quote="Complete medical history")]),
        Procedure(id="PE", label="Physical examination incl. vital signs", visit_ids=ALL,
                  visit_notes=[N(visit_id="V1", note="examen complet")] + [N(visit_id=x, note="examen limité") for x in post],
                  sources=[S(page=16, quote="Physical examination include. vital signs")]),
        Procedure(id="DIARY", label="Interim history / diary (AEFI, concomitant medication)", visit_ids=post,
                  sources=[S(page=16, quote="Interim History/Diary (AEFI documentation,")]),
        Procedure(id="RAND", label="Randomization", visit_ids=["V2"], sources=[S(page=16, quote="Randomization")]),
        Procedure(id="ECG", label="ECG", visit_ids=["V1"], sources=[S(page=16, quote="ECG")]),
        Procedure(id="HEMA", label="Hematology", visit_ids=["V1", "V2", "V4", "V6", "V8", "V9"], sources=[S(page=16, quote="Hematology")]),
        Procedure(id="CHEM", label="Blood chemistry", visit_ids=["V1"], sources=[S(page=16, quote="Blood chemistry")]),
        Procedure(id="SERO", label="Screening for HIV, hepatitis B and C", visit_ids=["V1"],
                  sources=[S(page=16, quote="Screening for HIV, hepatitis B and C")]),
        Procedure(id="PTIGG", label="Serum pertussis toxin and pertactin IgG antibodies", visit_ids=["V1"],
                  sources=[S(page=16, quote="Serum pertussis toxin and pertactin IgG")]),
        Procedure(id="URINE", label="Urine analysis (+ dipstick pregnancy test at V2 and V8)", visit_ids=["V1", "V2", "V8"],
                  visit_notes=[N(visit_id="V2", note="test de grossesse urinaire AVANT randomisation (exclusion si positif)"),
                               N(visit_id="V8", note="test de grossesse urinaire")],
                  sources=[S(page=16, quote="Urine analysis"),
                           S(page=16, quote="Urine dipstick pregnancy test is to be done at visit 2 before randomization")]),
        Procedure(id="NPA", label="Nasopharyngeal aspirate for BPZE1 culture", visit_ids=["V3", "V4", "V5", "V6", "V7", "V8", "V8b"],
                  visit_notes=[N(visit_id="V8", note="si culture positive : programmer V8' (J45 -5/+10)")],
                  sources=[S(page=16, quote="Nasopharyngeal aspirate for BPZE1 culture")]),
        Procedure(id="SERAB", label="Binding pertussis serum antibodies", visit_ids=["V2", "V4", "V6", "V7", "V8", "V9"],
                  sources=[S(page=16, quote="Binding pertussis serum antibodies")]),
        Procedure(id="NPAB", label="Binding pertussis nasopharyngeal antibodies", visit_ids=["V3", "V4", "V6", "V7", "V8", "V9"],
                  sources=[S(page=16, quote="Binding pertussis nasopharyngeal antibodies")]),
        Procedure(id="NPCYT", label="Nasopharyngeal cytokines", visit_ids=["V3", "V4", "V5", "V6", "V7", "V8", "V9"],
                  sources=[S(page=16, quote="Nasopharyngeal cytokines")]),
        Procedure(id="LPR", label="Lymphoproliferative response", visit_ids=["V2", "V3", "V6", "V8", "V9"],
                  visit_notes=[N(visit_id="V3", note="groupe 3 (haute dose) uniquement")], sources=[S(page=16, quote="Lymphoproliferative response")]),
        Procedure(id="CRYO", label="Cryo-preserved cells", visit_ids=["V2", "V6", "V8", "V9"], sources=[S(page=16, quote="Cryo-preserved cells")]),
    ]
    amb = [
        Ambiguity(description=("Visite 9 : fenêtre « 6±1 months ». La conversion en jours n'est pas définie par le protocole ; "
                               "KAIROS utilise 182 ±30 jours. À confirmer (calendaire vs 30 jours)."),
                  sources=[S(page=31, quote="Visit 9, 6±1 months after visit 2")]),
        Ambiguity(description=("Visite 8' conditionnelle : déclenchée par un résultat de laboratoire (culture J28 positive). "
                               "Le centre doit être prévenu du résultat à temps pour programmer J45 (-5) = J40 au plus tôt."),
                  sources=[S(page=31, quote="Visit 8’, 45 (-5;+10) days after visit 2")]),
    ]
    return StudyModel(
        nct_id=nct, title="BPZE1 nasal live attenuated pertussis vaccine – Phase Ib", sponsor="INSERM",
        protocol_version="Study Protocol 2015-09-01", protocol_date="2015-09-01", day_convention="day0",
        arms=[], visits=visits, procedures=procs, ambiguities=amb,
        extraction_notes=("La couche texte du PDF est dégradée (lettres espacées : « I NSE R M ») : le tableau des visites (p.16) "
                          "a été lu sur l'image. La vérification d'ancrage ignore les espaces, ce qui la rend robuste à ce défaut."),
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for m in (janssen(), imea(), inserm()):
        path = OUT / f"{m.nct_id}.session.json"
        path.write_text(m.model_dump_json(indent=2), encoding="utf-8")
        print(f"{path.relative_to(ROOT)} : {len(m.visits)} visites, {len(m.procedures)} procédures, {len(m.ambiguities)} ambiguïtés")


if __name__ == "__main__":
    main()
