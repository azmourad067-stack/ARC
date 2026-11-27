"""Moteur de règles DÉTERMINISTE : calcule fenêtres de visites, procédures dues et alertes.

Aucune IA ici : le calcul repose uniquement sur le modèle validé (schema.StudyModel)
et sur les dates réelles saisies. C'est ce qui rend l'outil auditable.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
from enum import Enum
from typing import Optional

from .schema import StudyModel, Visit


class Status(str, Enum):
    DONE_IN_WINDOW = "réalisée dans la fenêtre"
    DONE_OUT_OF_WINDOW = "réalisée HORS fenêtre (déviation)"
    MISSED = "fenêtre dépassée, visite non réalisée (déviation)"
    OPEN = "fenêtre ouverte"
    UPCOMING = "à venir"
    NOT_SCHEDULABLE = "non calculable (visite d'ancrage non réalisée)"
    PRE_ANCHOR_NOT_RECORDED = "antérieure à la référence, date non saisie"


@dataclass
class Patient:
    patient_id: str
    study: StudyModel
    arm_id: Optional[str] = None
    # dates réelles des visites réalisées : {visit_id: date}
    done: dict[str, date] = field(default_factory=dict)


@dataclass
class VisitPlan:
    visit: Visit
    target: Optional[date]
    earliest: Optional[date]
    latest: Optional[date]
    actual: Optional[date]
    status: Status
    procedures: list[str]


class _Today:
    """Permet de figer « aujourd'hui » (tests, démonstrations reproductibles)."""
    def __init__(self) -> None:
        self._d: Optional[date] = None

    def get(self) -> date:
        return self._d or date.today()

    def set(self, d: Optional[date]) -> None:
        self._d = d


TODAY_OVERRIDE = _Today()


def visits_for_arm(study: StudyModel, arm_id: Optional[str]) -> list[Visit]:
    return [v for v in study.visits if not v.arm_ids or arm_id is None or arm_id in v.arm_ids]


def procedures_at(study: StudyModel, visit_id: str) -> list[str]:
    out = []
    for p in study.procedures:
        if visit_id in p.visit_ids:
            notes = [p.condition] if p.condition else []
            notes += [n.note for n in p.visit_notes if n.visit_id == visit_id]
            out.append(p.label + (f" [{' ; '.join(notes)}]" if notes else ""))
    return out


def plan(patient: Patient, today: Optional[date] = None) -> list[VisitPlan]:
    """Calcule le plan de visites d'un patient. Les ancrages utilisent la date RÉELLE
    de la visite de référence (si une visite d'ancrage est décalée, les suivantes le sont aussi)."""
    today = today or TODAY_OVERRIDE.get()
    visits = visits_for_arm(patient.study, patient.arm_id)
    by_id = {v.id: v for v in visits}
    targets: dict[str, Optional[date]] = {}

    def target_of(v: Visit, depth: int = 0) -> Optional[date]:
        if depth > 50:
            raise ValueError(f"Ancrage circulaire autour de {v.id}")
        if v.id in targets:
            return targets[v.id]
        if v.anchor is None:
            t = patient.done.get(v.id)
        else:
            anchor = by_id.get(v.anchor)
            if anchor is None:
                raise ValueError(f"Visite {v.id}: ancrage inconnu {v.anchor!r}")
            anchor_date = patient.done.get(anchor.id) or None
            t = anchor_date + timedelta(days=v.offset_days) if anchor_date else None
        targets[v.id] = t
        return t

    plans = []
    for v in visits:
        t = target_of(v)
        actual = patient.done.get(v.id)
        if v.anchor is None:
            # visite de référence : pas de fenêtre calculable avant qu'elle ait lieu
            status = Status.DONE_IN_WINDOW if actual else Status.UPCOMING
            plans.append(VisitPlan(v, actual, actual, actual, actual, status, procedures_at(patient.study, v.id)))
            continue
        if t is None:
            plans.append(VisitPlan(v, None, None, None, actual, Status.NOT_SCHEDULABLE, procedures_at(patient.study, v.id)))
            continue
        lo = t - timedelta(days=v.window_minus_days)
        hi = t + timedelta(days=v.window_plus_days)
        if actual:
            status = Status.DONE_IN_WINDOW if lo <= actual <= hi else Status.DONE_OUT_OF_WINDOW
        elif v.offset_days < 0 and patient.done.get(v.anchor):
            # visite pré-inclusion (screening) : l'ancrage a déjà eu lieu, on ne peut que constater l'absence de date
            status = Status.PRE_ANCHOR_NOT_RECORDED
        elif today > hi:
            status = Status.MISSED
        elif today >= lo:
            status = Status.OPEN
        else:
            status = Status.UPCOMING
        plans.append(VisitPlan(v, t, lo, hi, actual, status, procedures_at(patient.study, v.id)))
    return plans


@dataclass
class BriefItem:
    patient_id: str
    nct_id: str
    plan: VisitPlan
    urgency: int  # 0 = critique
    message: str


def brief(patients: list[Patient], today: Optional[date] = None, horizon_days: int = 7) -> list[BriefItem]:
    """Le « brief du jour » multi-études : ce qui doit se passer, ce qui va déraper."""
    today = today or TODAY_OVERRIDE.get()
    items: list[BriefItem] = []
    for pt in patients:
        for p in plan(pt, today):
            v = p.visit
            if p.status == Status.MISSED:
                items.append(BriefItem(pt.patient_id, pt.study.nct_id, p, 0,
                    f"{v.label} : fenêtre fermée depuis le {p.latest:%d/%m/%Y} et visite non saisie → déviation probable"))
            elif p.status == Status.DONE_OUT_OF_WINDOW:
                items.append(BriefItem(pt.patient_id, pt.study.nct_id, p, 1,
                    f"{v.label} réalisée le {p.actual:%d/%m/%Y} hors fenêtre [{p.earliest:%d/%m}–{p.latest:%d/%m}] → déviation à documenter"))
            elif p.status == Status.OPEN:
                left = (p.latest - today).days
                items.append(BriefItem(pt.patient_id, pt.study.nct_id, p, 1 if left <= 2 else 2,
                    f"{v.label} : fenêtre OUVERTE, se ferme le {p.latest:%d/%m/%Y} (J-{left}). Cible {p.target:%d/%m}"))
            elif p.status == Status.UPCOMING and p.earliest and (p.earliest - today).days <= horizon_days:
                items.append(BriefItem(pt.patient_id, pt.study.nct_id, p, 3,
                    f"{v.label} : fenêtre du {p.earliest:%d/%m} au {p.latest:%d/%m} (cible {p.target:%d/%m})"))
    items.sort(key=lambda i: (i.urgency, i.plan.latest or date.max))
    return items


def format_brief(items: list[BriefItem], today: date) -> str:
    icons = {0: "🔴", 1: "🟠", 2: "🟡", 3: "🔵"}
    lines = [f"BRIEF KAIROS — {today:%A %d/%m/%Y}", ""]
    if not items:
        lines.append("Rien à signaler sur l'horizon.")
    for it in items:
        lines.append(f"{icons[it.urgency]} [{it.nct_id}] Patient {it.patient_id} — {it.message}")
        for pr in it.plan.procedures:
            lines.append(f"      • {pr}")
        src = it.plan.visit.sources[:1]
        if src:
            lines.append(f"      ↳ source : p.{src[0].page} « {src[0].quote[:90]} »")
    return "\n".join(lines)
