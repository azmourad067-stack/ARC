"""Modèle structuré d'un protocole (sous-ensemble opérationnel inspiré de CDISC USDM / ICH M11).

Principe KAIROS : chaque information extraite porte sa source (page + citation
verbatim), afin d'être vérifiable automatiquement puis validée par un humain.
"""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class SourceRef(BaseModel):
    page: int = Field(description="Numéro de page du PDF (1 = première page du fichier).")
    quote: str = Field(description="Extrait VERBATIM et court (≤ 200 caractères) du texte de cette page qui justifie l'information.")


class Arm(BaseModel):
    id: str = Field(description="Identifiant court, ex. 'G1'.")
    label: str


class Visit(BaseModel):
    id: str = Field(description="Identifiant court et stable, ex. 'V3', 'W4', 'PT12'.")
    label: str = Field(description="Libellé tel qu'écrit dans le protocole.")
    arm_ids: list[str] = Field(default_factory=list, description="Bras concernés ; liste vide = tous les bras.")
    anchor: Optional[str] = Field(
        default=None,
        description="Id de la visite de référence pour le calcul de la date. None = cette visite EST la référence (jour d'inclusion / première administration).",
    )
    offset_days: int = Field(
        default=0,
        description="Nombre de jours entre la date RÉELLE de la visite d'ancrage et la date cible de cette visite (ex. 'Day 8' avec convention Day 1 = ancrage -> 7).",
    )
    window_minus_days: int = Field(default=0, ge=0, description="Tolérance avant la date cible, en jours.")
    window_plus_days: int = Field(default=0, ge=0, description="Tolérance après la date cible, en jours.")
    is_dosing: bool = Field(default=False, description="Administration du produit à cette visite.")
    conditional: Optional[str] = Field(default=None, description="Condition de réalisation éventuelle (texte court).")
    sources: list[SourceRef] = Field(default_factory=list)


class VisitNote(BaseModel):
    visit_id: str
    note: str = Field(description="Précision qui ne vaut QUE pour cette visite (ex. 'avant vaccination', 'groupe 3 uniquement').")


class Procedure(BaseModel):
    id: str
    label: str
    visit_ids: list[str] = Field(description="Visites où la procédure est requise.")
    condition: Optional[str] = Field(default=None, description="Restriction valable à TOUTES les visites (sous-population, note de bas de tableau).")
    visit_notes: list[VisitNote] = Field(default_factory=list, description="Précisions propres à une visite donnée.")
    sources: list[SourceRef] = Field(default_factory=list)


class Ambiguity(BaseModel):
    """Contradiction, imprécision ou coquille détectée dans le protocole : à faire trancher par le promoteur."""
    description: str
    sources: list[SourceRef] = Field(default_factory=list)


class StudyModel(BaseModel):
    nct_id: str
    title: str
    sponsor: str
    protocol_version: Optional[str] = None
    protocol_date: Optional[str] = None
    day_convention: str = Field(description="'day1' si le jour de l'ancrage est noté Day 1 ; 'day0' s'il est noté Day 0 / D0.")
    arms: list[Arm] = Field(default_factory=list)
    visits: list[Visit]
    procedures: list[Procedure]
    ambiguities: list[Ambiguity] = Field(default_factory=list)
    extraction_notes: Optional[str] = Field(default=None, description="Limites connues de l'extraction.")
