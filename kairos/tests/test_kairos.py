import sys
from datetime import date
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from kairos import engine, verify  # noqa: E402
from kairos.cli import load_model  # noqa: E402
from kairos.pdf_text import load_pages  # noqa: E402
from kairos.schema import Procedure, SourceRef, StudyModel, Visit  # noqa: E402

NCTS = ["NCT02564523", "NCT02886624", "NCT02453048"]
HAS_TEXT = all((ROOT / "data" / "text" / f"{n}.json").exists() for n in NCTS)


def toy() -> StudyModel:
    return StudyModel(
        nct_id="TOY", title="toy", sponsor="x", day_convention="day0",
        visits=[
            Visit(id="SCR", label="screening", anchor="D0", offset_days=-14, window_minus_days=14, window_plus_days=7),
            Visit(id="D0", label="D0", anchor=None),
            Visit(id="BOOST", label="boost", anchor="D0", offset_days=28, window_minus_days=3, window_plus_days=3),
            Visit(id="PB7", label="+7 post-boost", anchor="BOOST", offset_days=7, window_minus_days=2, window_plus_days=2),
        ],
        procedures=[Procedure(id="P", label="prélèvement", visit_ids=["D0", "PB7"],
                              sources=[SourceRef(page=1, quote="Blood sampling at D0")])],
    )


def test_windows_and_statuses():
    pt = engine.Patient("1", toy(), None, {"D0": date(2026, 1, 1)})
    plans = {p.visit.id: p for p in engine.plan(pt, today=date(2026, 1, 27))}
    assert plans["BOOST"].target == date(2026, 1, 29)
    assert (plans["BOOST"].earliest, plans["BOOST"].latest) == (date(2026, 1, 26), date(2026, 2, 1))
    assert plans["BOOST"].status == engine.Status.OPEN
    assert plans["PB7"].status == engine.Status.NOT_SCHEDULABLE
    assert plans["SCR"].status == engine.Status.PRE_ANCHOR_NOT_RECORDED


def test_anchor_on_actual_date_propagates_shift():
    # rappel fait 2 jours en retard (dans sa fenêtre) : la visite +7 suit la date réelle
    pt = engine.Patient("1", toy(), None, {"D0": date(2026, 1, 1), "BOOST": date(2026, 1, 31)})
    plans = {p.visit.id: p for p in engine.plan(pt, today=date(2026, 2, 1))}
    assert plans["BOOST"].status == engine.Status.DONE_IN_WINDOW
    assert plans["PB7"].target == date(2026, 2, 7)


def test_out_of_window_and_missed():
    pt = engine.Patient("1", toy(), None, {"D0": date(2026, 1, 1), "BOOST": date(2026, 2, 5)})
    plans = {p.visit.id: p for p in engine.plan(pt, today=date(2026, 3, 1))}
    assert plans["BOOST"].status == engine.Status.DONE_OUT_OF_WINDOW
    assert plans["PB7"].status == engine.Status.MISSED
    items = engine.brief([pt], today=date(2026, 3, 1))
    assert [i.urgency for i in items] == [0, 1]


def test_verifier_flags_fabricated_and_misplaced_quotes():
    m = toy()
    pages = ["Blood  sampling\nat D0 is mandatory", "other page"]
    assert verify.summary(m, pages)["taux_ancrage"] == 1.0
    m.procedures[0].sources = [SourceRef(page=2, quote="Blood sampling at D0")]
    s = verify.summary(m, pages)
    assert s["trouvees_autre_page"] == 1 and s["echecs"][0]["trouvee_pages"] == [1]
    m.procedures[0].sources = [SourceRef(page=1, quote="Urine sampling at D0")]
    assert verify.summary(m, pages)["introuvables"] == 1


def test_verifier_tolerates_spaced_letters():
    m = toy()
    assert verify.summary(m, ["B l o o d s a m p l i n g a t D 0"])["taux_ancrage"] == 1.0


def test_integrity_detects_bad_references():
    m = toy()
    m.procedures[0].visit_ids.append("W99")
    m.visits[3].anchor = "NOPE"
    errs = verify.integrity(m)
    assert any("W99" in e for e in errs) and any("NOPE" in e for e in errs)


@pytest.mark.parametrize("nct", NCTS)
def test_session_extractions_integrity(nct):
    assert verify.integrity(load_model(nct)) == []


@pytest.mark.skipif(not HAS_TEXT, reason="textes des protocoles non téléchargés (python -m kairos.cli fetch ...)")
@pytest.mark.parametrize("nct", NCTS)
def test_session_extractions_fully_grounded(nct):
    s = verify.summary(load_model(nct), load_pages(ROOT / "data" / "text" / f"{nct}.json"))
    assert s["taux_ancrage"] == 1.0, s["echecs"]


def test_janssen_group_specific_schedule():
    m = load_model("NCT02564523")
    pt = engine.Patient("x", m, "G3", {"PRIME": date(2026, 1, 1)})
    plans = {p.visit.id: p for p in engine.plan(pt, today=date(2026, 1, 1))}
    assert "BOOST_G1" not in plans and "PP14" in plans
    assert plans["BOOST_G3"].target == date(2026, 3, 26)  # Day 85 = J1 + 84
