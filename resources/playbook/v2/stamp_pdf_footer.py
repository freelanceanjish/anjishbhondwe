#!/usr/bin/env python3
"""Stamp branded footer on every page of playbook PDFs."""
from __future__ import annotations

import sys
from io import BytesIO
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

LEFT = "Anjish Bhondwe"
RIGHT = "anjishbhondwe.com"
FOOTER_COLOR = HexColor("#8d8d8d")
LINE_COLOR = HexColor("#c6c6c6")
MARGIN_X = 14 * mm
FOOTER_Y = 10 * mm
LINE_Y = 14 * mm


def _overlay_page(page) -> None:
    w = float(page.mediabox.width)
    h = float(page.mediabox.height)
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(w, h))
    c.setStrokeColor(LINE_COLOR)
    c.setLineWidth(0.5)
    c.line(MARGIN_X, LINE_Y, w - MARGIN_X, LINE_Y)
    c.setFillColor(FOOTER_COLOR)
    c.setFont("Helvetica", 8)
    c.drawString(MARGIN_X, FOOTER_Y, LEFT)
    c.drawRightString(w - MARGIN_X, FOOTER_Y, RIGHT)
    c.save()
    overlay = PdfReader(packet).pages[0]
    page.merge_page(overlay)


def stamp(input_path: Path, output_path: Path, *, skip_first: bool = False) -> None:
    reader = PdfReader(str(input_path))
    writer = PdfWriter()
    for index, page in enumerate(reader.pages):
        if not (skip_first and index == 0):
            _overlay_page(page)
        writer.add_page(page)
    with output_path.open("wb") as handle:
        writer.write(handle)


def main() -> None:
    if len(sys.argv) < 3:
        raise SystemExit("Usage: stamp_pdf_footer.py <input.pdf> <output.pdf> [--skip-first]")
    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    skip_first = "--skip-first" in sys.argv
    stamp(input_path, output_path, skip_first=skip_first)
    print(f"Stamped: {output_path}")


if __name__ == "__main__":
    main()
