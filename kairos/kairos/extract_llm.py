"""Extraction protocole PDF -> StudyModel avec Claude (sorties structurées).

Nécessite des identifiants Anthropic (ANTHROPIC_API_KEY ou `ant auth login`).
Usage :
    python -m kairos.extract_llm data/text/NCT02886624.json --nct NCT02886624 -o data/extractions/NCT02886624.llm.json

Garde-fous :
- le texte est fourni page par page, balisé <page n="...">, et chaque élément
  doit citer sa page + un extrait verbatim ;
- la sortie est ensuite contrôlée par kairos.verify (ancrage) puis validée par un humain ;
- aucun calcul de date n'est confié au modèle (voir kairos.engine).
"""
from __future__ import annotations

import argparse
import base64
import sys
from pathlib import Path

import anthropic

from .pdf_text import as_tagged_text, load_pages
from .schema import StudyModel

MODEL = "claude-opus-5-5"

SYSTEM = """Tu es un ingénieur de protocole clinique. Tu convertis un protocole d'essai clinique en un modèle
opérationnel exécutable par un moteur de règles, destiné aux attachés de recherche clinique (ARC) d'un centre.

Règles impératives :
1. N'invente rien. Chaque visite et chaque procédure doit citer au moins une source : numéro de page
   (attribut n de la balise <page>) et un extrait COURT copié mot pour mot de cette page.
2. Calendrier : pour chaque visite, indique la visite d'ancrage (anchor) et le décalage en jours
   (offset_days) entre la date RÉELLE de l'ancrage et la date cible. Respecte la convention du protocole :
   avec « Day 1 » = jour de l'ancrage, « Day 8 » donne offset_days = 7 ; avec « D0 », « W4 » donne 28.
   Une visite ancrée sur un évènement (ex. fin de traitement, rappel) s'ancre sur la visite correspondante.
   La visite de référence (inclusion / première administration) a anchor = null.
   La sélection (screening) s'ancre sur la visite de référence avec un offset négatif.
3. Fenêtres : cherche-les partout (tableau de visites, notes de bas de tableau, section dédiée parfois
   loin du tableau). Si aucune fenêtre n'est donnée, mets 0/0 et signale-le dans extraction_notes.
4. Bras : si le calendrier dépend du bras, crée une visite par bras (arm_ids) avec ses propres offsets.
5. Procédures : une entrée par ligne du tableau des visites, avec les visites cochées et les restrictions
   des notes de bas de tableau dans condition.
6. Signale dans ambiguities toute contradiction entre le tableau et le texte, toute coquille ou imprécision
   qui pourrait causer une déviation.
"""


def extract(pages: list[str], nct_id: str, client: anthropic.Anthropic | None = None,
            pdf_path: str | Path | None = None) -> StudyModel:
    """pdf_path : envoie aussi le PDF (lecture visuelle des tableaux). Recommandé : dans le test H3,
    2 protocoles sur 3 avaient une couche texte inexploitable seule (lettres espacées, colonnes désalignées)."""
    client = client or anthropic.Anthropic()
    doc = as_tagged_text(pages)
    pdf_block = []
    if pdf_path:
        data = base64.standard_b64encode(Path(pdf_path).read_bytes()).decode("ascii")
        pdf_block = [{"type": "document", "source": {"type": "base64", "media_type": "application/pdf", "data": data}}]
    with client.beta.messages.stream(
        model=MODEL,
        max_tokens=64000,
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        thinking={"type": "adaptive"},
        output_config={"effort": "high"},
        system=SYSTEM,
        output_format=StudyModel,
        messages=[{
            "role": "user",
            "content": [
                *pdf_block,
                {"type": "text", "text": f"<protocole nct=\"{nct_id}\">\n{doc}\n</protocole>",
                 "cache_control": {"type": "ephemeral"}},
                {"type": "text", "text": "Produis le modèle opérationnel complet de ce protocole. Les numéros de page "
                                         "à citer sont ceux des balises <page>, identiques aux pages du PDF joint ; "
                                         "lis les tableaux sur le PDF si la couche texte est désalignée."},
            ],
        }],
    ) as stream:
        msg = stream.get_final_message()
    if msg.stop_reason == "refusal":
        raise RuntimeError(f"Refus du modèle : {msg.stop_details}")
    if msg.stop_reason == "max_tokens":
        raise RuntimeError("Sortie tronquée (max_tokens) : protocole trop volumineux, découper par sections.")
    text = next(b.text for b in msg.content if b.type == "text")
    return StudyModel.model_validate_json(text)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pages_json", help="Fichier JSON des pages (produit par kairos.pdf_text)")
    ap.add_argument("--nct", required=True)
    ap.add_argument("-o", "--out", required=True)
    ap.add_argument("--pdf", help="PDF du protocole à joindre (recommandé)")
    a = ap.parse_args(argv)
    model = extract(load_pages(a.pages_json), a.nct, pdf_path=a.pdf)
    Path(a.out).write_text(model.model_dump_json(indent=2), encoding="utf-8")
    print(f"Modèle écrit dans {a.out} : {len(model.visits)} visites, {len(model.procedures)} procédures")
    return 0


if __name__ == "__main__":
    sys.exit(main())
