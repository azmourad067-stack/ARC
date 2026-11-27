"""Interface en ligne de commande KAIROS.

  python -m kairos.cli fetch NCT02886624            # télécharge le protocole public + extrait le texte
  python -m kairos.cli verify NCT02886624            # contrôle d'ancrage des citations
  python -m kairos.cli plan NCT02886624 --ref 2026-11-02 [--arm G1] [--done W4=2026-11-30]
  python -m kairos.cli sheet NCT02886624             # fiche de validation humaine (markdown)
  python -m kairos.cli demo --today 2026-11-27       # brief multi-études sur des patients fictifs
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

from . import engine, verify
from .pdf_text import load_pages, save_pages
from .schema import StudyModel

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def load_model(nct: str, kind: str = "session") -> StudyModel:
    return StudyModel.model_validate_json((DATA / "extractions" / f"{nct}.{kind}.json").read_text(encoding="utf-8"))


def cmd_fetch(a: argparse.Namespace) -> None:
    import requests

    r = requests.get(f"https://clinicaltrials.gov/api/v2/studies/{a.nct}",
                     params={"fields": "NCTId,BriefTitle,LargeDocumentModule"}, timeout=30)
    r.raise_for_status()
    docs = r.json().get("documentSection", {}).get("largeDocumentModule", {}).get("largeDocs", [])
    prot = [d for d in docs if d.get("hasProtocol")]
    if not prot:
        sys.exit(f"{a.nct} : aucun protocole publié sur ClinicalTrials.gov")
    fn = prot[-1]["filename"]
    url = f"https://cdn.clinicaltrials.gov/large-docs/{a.nct[-2:]}/{a.nct}/{fn}"
    pdf = DATA / "protocols" / f"{a.nct}.pdf"
    pdf.parent.mkdir(parents=True, exist_ok=True)
    pdf.write_bytes(requests.get(url, timeout=120).content)
    pages = save_pages(pdf, DATA / "text" / f"{a.nct}.json")
    print(f"{pdf} : {len(pages)} pages")


def cmd_verify(a: argparse.Namespace) -> None:
    model = load_model(a.nct, a.kind)
    s = verify.summary(model, load_pages(DATA / "text" / f"{a.nct}.json"))
    print(json.dumps(s, ensure_ascii=False, indent=2))


def _parse_done(items: list[str]) -> dict[str, date]:
    out = {}
    for it in items or []:
        k, v = it.split("=")
        out[k] = date.fromisoformat(v)
    return out


def cmd_plan(a: argparse.Namespace) -> None:
    model = load_model(a.nct, a.kind)
    ref = next(v.id for v in model.visits if v.anchor is None)
    done = {ref: date.fromisoformat(a.ref), **_parse_done(a.done)}
    pt = engine.Patient("demo", model, a.arm, done)
    today = date.fromisoformat(a.today) if a.today else date.today()
    print(f"{model.nct_id} — {model.title}\nBras : {a.arm or 'tous'} | référence {ref} = {a.ref} | aujourd'hui {today}\n")
    for p in engine.plan(pt, today):
        win = f"{p.earliest:%d/%m/%Y} → {p.latest:%d/%m/%Y}" if p.earliest else "—"
        tgt = f"{p.target:%d/%m/%Y}" if p.target else "—"
        print(f"{p.visit.id:<9} cible {tgt:<11} fenêtre {win:<25} {p.status.value}")
        if a.procedures:
            for pr in p.procedures:
                print(f"           • {pr}")


def cmd_demo(a: argparse.Namespace) -> None:
    today = date.fromisoformat(a.today)
    J, I, B = load_model("NCT02564523"), load_model("NCT02886624"), load_model("NCT02453048")
    d = date.fromisoformat
    patients = [
        # Janssen, groupe 2 : rappel fait, visite +7 j post-rappel dont la fenêtre est ouverte
        engine.Patient("014", J, "G2", {"PRIME": d("2026-09-29"), "PP7": d("2026-10-06"), "PP14": d("2026-10-13"),
                                        "BOOST_G2": d("2026-11-23")}),
        # IMEA : W4 réalisée hors fenêtre, W8 qui approche
        engine.Patient("003", I, None, {"SCR": d("2026-09-22"), "D0": d("2026-10-06"), "W4": d("2026-11-12")}),
        # Inserm BPZE1 : V5 oubliée, V6 qui arrive
        engine.Patient("102", B, None, {"V1": d("2026-10-20"), "V2": d("2026-11-14"), "V3": d("2026-11-18"),
                                        "V4": d("2026-11-21")}),
    ]
    print(engine.format_brief(engine.brief(patients, today, horizon_days=a.horizon), today))


def sheet_markdown(model: StudyModel) -> str:
    """Fiche de validation humaine : chaque ligne est à cocher contre le PDF."""
    vids = [v.id for v in model.visits]
    L = [f"# Fiche de validation — {model.nct_id}", "",
         f"**{model.title}** — promoteur : {model.sponsor} — version : {model.protocol_version} ({model.protocol_date})", "",
         f"> {model.extraction_notes}" if model.extraction_notes else "", "",
         "Cochez chaque ligne exacte ; corrigez sinon. Mesure H3 = % de lignes justes sans correction.", "",
         "## 1. Visites et fenêtres", "",
         "| OK | Visite | Bras | Ancrage | Décalage (j) | Fenêtre | Condition | Source |",
         "|---|---|---|---|---|---|---|---|"]
    for v in model.visits:
        src = "; ".join(f"p.{r.page}" for r in v.sources)
        L.append(f"| ☐ | {v.id} — {v.label} | {', '.join(v.arm_ids) or 'tous'} | {v.anchor or '**référence**'} | "
                 f"{v.offset_days:+d} | -{v.window_minus_days} / +{v.window_plus_days} | {v.conditional or ''} | {src} |")
    L += ["", "## 2. Procédures × visites", "",
          "| OK | Procédure | " + " | ".join(vids) + " |", "|---|---|" + "---|" * len(vids)]
    for p in model.procedures:
        cells = ["X" if v in p.visit_ids else "" for v in vids]
        lab = p.label + (f" *({p.condition})*" if p.condition else "")
        L.append(f"| ☐ | {lab} (p.{', '.join(str(r.page) for r in p.sources)}) | " + " | ".join(cells) + " |")
    L += ["", "## 3. Ambiguïtés détectées (à faire trancher par le promoteur)", ""]
    for a in model.ambiguities:
        L.append(f"- {a.description} ({', '.join(f'p.{r.page}' for r in a.sources)})")
    return "\n".join(L) + "\n"


def cmd_sheet(a: argparse.Namespace) -> None:
    out = Path(a.out) if a.out else ROOT / "validation" / f"{a.nct}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(sheet_markdown(load_model(a.nct, a.kind)), encoding="utf-8")
    print(out)


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(prog="kairos")
    sub = ap.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("fetch"); f.add_argument("nct"); f.set_defaults(fn=cmd_fetch)
    v = sub.add_parser("verify"); v.add_argument("nct"); v.add_argument("--kind", default="session"); v.set_defaults(fn=cmd_verify)
    p = sub.add_parser("plan"); p.add_argument("nct"); p.add_argument("--ref", required=True)
    p.add_argument("--arm"); p.add_argument("--done", nargs="*"); p.add_argument("--today")
    p.add_argument("--kind", default="session"); p.add_argument("--procedures", action="store_true"); p.set_defaults(fn=cmd_plan)
    sh = sub.add_parser("sheet"); sh.add_argument("nct"); sh.add_argument("--kind", default="session"); sh.add_argument("-o", "--out")
    sh.set_defaults(fn=cmd_sheet)
    d = sub.add_parser("demo"); d.add_argument("--today", default="2026-11-27"); d.add_argument("--horizon", type=int, default=7)
    d.set_defaults(fn=cmd_demo)
    a = ap.parse_args(argv)
    a.fn(a)


if __name__ == "__main__":
    main()
