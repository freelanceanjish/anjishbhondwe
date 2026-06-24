#!/bin/bash
# Generate all v2 playbook PDFs via headless Chrome
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
OUT="$DIR"
PROFILE="/tmp/chrome-pdf-v2-$$"
mkdir -p "$PROFILE"

chrome_pdf() {
  local html="$1"
  local pdf="$2"
  google-chrome --headless=new --disable-gpu --no-sandbox \
    --user-data-dir="$PROFILE" \
    --run-all-compositor-stages-before-draw \
    --virtual-time-budget=25000 \
    --print-to-pdf="$pdf" \
    "file://$html"
  echo "Created: $pdf"
}

chrome_pdf "$DIR/01-executive-brief.html" "$OUT/01-Executive-Brief.pdf"
chrome_pdf "$DIR/02-practitioner-playbook.html" "$OUT/02-Practitioner-Playbook.pdf"
chrome_pdf "$DIR/03-workshop-kit.html" "$OUT/03-Workshop-Kit.pdf"
chrome_pdf "$DIR/04-steerco-pack.html" "$OUT/04-SteerCo-Pack.pdf"

OUT_DIR="$OUT" python3 <<'PY'
import os, subprocess, sys
from pathlib import Path

out = Path(os.environ["OUT_DIR"])
parts = [
    out / "01-Executive-Brief.pdf",
    out / "02-Practitioner-Playbook.pdf",
    out / "03-Workshop-Kit.pdf",
    out / "04-SteerCo-Pack.pdf",
]
try:
    from pypdf import PdfWriter
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdf", "-q"])
    from pypdf import PdfWriter

writer = PdfWriter()
for p in parts:
    writer.append(str(p))
combined = out / "00-Full-Pack-Combined.pdf"
writer.write(str(combined))
writer.close()
print(f"Merged: {combined}")
PY

rm -rf "$PROFILE"
echo "Done. PDFs in $OUT"
ls -lh "$OUT"/*.pdf
