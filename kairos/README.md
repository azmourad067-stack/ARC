# KAIROS — prototype « protocole exécutable »

Prototype du test **H3** du concept (`docs/recherche-clinique/CONCEPT-PRODUIT.md`) :
*une IA peut-elle transformer un protocole PDF en un calendrier de visites exploitable par un ARC ?*

## Architecture

```
PDF du protocole ──► pdf_text.py ──► pages texte ─┐
       │                                          ├─► extract_llm.py (Claude, sortie structurée)
       └──────────── PDF joint (lecture visuelle) ┘          │
                                                             ▼
                                                   StudyModel (schema.py)
                                       chaque visite / procédure = page + citation verbatim
                                                             │
                     ┌───────────────────────────────────────┼─────────────────────────────┐
                     ▼                                       ▼                             ▼
          verify.py : ancrage des citations      cli sheet : fiche de validation    engine.py : moteur DÉTERMINISTE
          + cohérence interne (automatique)      humaine (ARC, à cocher)            fenêtres, statuts, brief du jour
```

**Règle de conception :** l'IA lit et structure ; elle ne calcule jamais une date. Les fenêtres et
les alertes viennent d'un moteur de règles classique, testé, qui s'appuie sur le modèle validé.

## Utilisation

```bash
pip install pydantic anthropic requests pytest   # + poppler-utils (pdftotext)
```

```bash
python -m kairos.cli fetch NCT02886624
```

```bash
python -m kairos.cli verify NCT02886624
```

```bash
python -m kairos.cli plan NCT02886624 --ref 2026-10-06 --done W4=2026-11-12 --today 2026-11-27 --procedures
```

```bash
python -m kairos.cli demo --today 2026-11-27
```

```bash
python -m kairos.cli sheet NCT02886624
```

Extraction automatique par l'API Claude (nécessite `ANTHROPIC_API_KEY`) :

```bash
python -m kairos.extract_llm data/text/NCT02886624.json --nct NCT02886624 --pdf data/protocols/NCT02886624.pdf -o data/extractions/NCT02886624.llm.json
```

```bash
python -m kairos.cli verify NCT02886624 --kind llm
```

```bash
python -m pytest -q tests
```

## Contenu

| Fichier | Rôle |
|---|---|
| `kairos/schema.py` | Modèle opérationnel du protocole (inspiré USDM / ICH M11), avec sources obligatoires |
| `kairos/engine.py` | Calcul des fenêtres (ancrage sur la date **réelle** de la visite de référence), statuts, brief multi-études |
| `kairos/verify.py` | Contrôle automatique : chaque citation existe-t-elle sur la page citée ? Références cohérentes ? |
| `kairos/extract_llm.py` | Extraction par Claude (`claude-opus-5-5`, sortie structurée, PDF joint) |
| `scripts/session_extractions.py` | Extractions des 3 protocoles réalisées pendant la session de conception |
| `data/extractions/*.session.json` | Modèles extraits (Janssen, IMEA, Inserm) |
| `validation/*.md` | Fiches de validation humaine à cocher contre les PDF |

Les PDF et textes (`data/protocols`, `data/text`) ne sont pas versionnés : `python -m kairos.cli fetch <NCT>` les retélécharge.
Le téléchargement nécessite l'accès réseau à `clinicaltrials.gov` et `cdn.clinicaltrials.gov`.

**Données patients :** la démonstration n'utilise que des patients fictifs (numéros et dates inventés).
