"""Vérification automatique de l'ancrage des extractions dans le texte source.

Pour chaque citation (page + extrait verbatim), on vérifie que l'extrait se trouve
réellement sur la page citée. Une citation introuvable = information non prouvée,
à revoir en priorité par l'humain. La comparaison ignore espaces, casse et ponctuation
typographique, ce qui la rend robuste aux PDF dont la couche texte est espacée
(ex. « I NSE R M »).
"""
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass

from .schema import SourceRef, StudyModel

_TRANSLATE = str.maketrans({"’": "'", "‘": "'", "“": '"', "”": '"', "–": "-", "—": "-", "−": "-", " ": " "})


def _norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s).translate(_TRANSLATE).lower()
    return re.sub(r"\s+", "", s)


@dataclass
class RefCheck:
    where: str
    ref: SourceRef
    found_on_page: bool
    found_elsewhere: list[int]


def check(model: StudyModel, pages: list[str]) -> list[RefCheck]:
    normed = [_norm(p) for p in pages]
    out: list[RefCheck] = []

    def one(where: str, ref: SourceRef) -> None:
        q = _norm(ref.quote)
        ok = 1 <= ref.page <= len(pages) and q in normed[ref.page - 1]
        else_ = [] if ok else [i + 1 for i, p in enumerate(normed) if q and q in p]
        out.append(RefCheck(where, ref, ok, else_))

    for v in model.visits:
        for r in v.sources:
            one(f"visite {v.id}", r)
    for p in model.procedures:
        for r in p.sources:
            one(f"procédure {p.id}", r)
    for a in model.ambiguities:
        for r in a.sources:
            one("ambiguïté", r)
    return out


def summary(model: StudyModel, pages: list[str]) -> dict:
    checks = check(model, pages)
    n = len(checks)
    ok = sum(c.found_on_page for c in checks)
    wrong_page = sum((not c.found_on_page) and bool(c.found_elsewhere) for c in checks)
    unsourced = [v.id for v in model.visits if not v.sources] + [p.id for p in model.procedures if not p.sources]
    return {
        "citations": n,
        "ancrees_page_exacte": ok,
        "trouvees_autre_page": wrong_page,
        "introuvables": n - ok - wrong_page,
        "taux_ancrage": round(ok / n, 3) if n else None,
        "elements_sans_source": unsourced,
        "echecs": [
            {"element": c.where, "page": c.ref.page, "citation": c.ref.quote, "trouvee_pages": c.found_elsewhere}
            for c in checks if not c.found_on_page
        ],
    }


def integrity(model: StudyModel) -> list[str]:
    """Cohérence interne du modèle : références de visites, ancrages, bras. Liste vide = OK."""
    errs: list[str] = []
    ids = [v.id for v in model.visits]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        errs.append(f"identifiants de visite dupliqués : {sorted(dup)}")
    idset, arms = set(ids), {a.id for a in model.arms}
    refs = [v for v in model.visits if v.anchor is None]
    if not refs:
        errs.append("aucune visite de référence (anchor = null)")
    for v in model.visits:
        if v.anchor and v.anchor not in idset:
            errs.append(f"visite {v.id} : ancrage inconnu {v.anchor}")
        for a in v.arm_ids:
            if a not in arms:
                errs.append(f"visite {v.id} : bras inconnu {a}")
    for p in model.procedures:
        for vid in p.visit_ids:
            if vid not in idset:
                errs.append(f"procédure {p.id} : visite inconnue {vid}")
        for n in p.visit_notes:
            if n.visit_id not in p.visit_ids:
                errs.append(f"procédure {p.id} : note sur la visite {n.visit_id} où la procédure n'est pas prévue")
    return errs
