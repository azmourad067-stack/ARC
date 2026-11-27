"""Extraction du texte d'un PDF, page par page (via pdftotext / poppler)."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path


def pdf_pages(pdf_path: str | Path) -> list[str]:
    """Retourne la liste des pages (texte) du PDF, index 0 = page 1."""
    out = subprocess.run(
        ["pdftotext", "-layout", "-enc", "UTF-8", str(pdf_path), "-"],
        check=True, capture_output=True,
    ).stdout.decode("utf-8", errors="replace")
    pages = out.split("\f")
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    return pages


def save_pages(pdf_path: str | Path, out_path: str | Path) -> list[str]:
    pages = pdf_pages(pdf_path)
    Path(out_path).write_text(json.dumps(pages, ensure_ascii=False), encoding="utf-8")
    return pages


def load_pages(path: str | Path) -> list[str]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def as_tagged_text(pages: list[str]) -> str:
    """Texte complet avec balises de page, pour que le LLM puisse citer ses sources."""
    return "\n".join(f"<page n=\"{i}\">\n{p}\n</page>" for i, p in enumerate(pages, start=1))
