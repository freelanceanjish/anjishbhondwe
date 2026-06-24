#!/bin/bash
# Generate all v2 playbook PDFs via headless Chrome (branded footer, no file:// URL)
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
OUT="$DIR"

chrome_pdf() {
  local html="$1"
  local pdf="$2"
  local profile="/tmp/chrome-pdf-$$-$RANDOM"
  mkdir -p "$profile"
  /usr/bin/google-chrome-stable --headless=new --disable-gpu --no-sandbox \
    --no-pdf-header-footer --disable-dev-shm-usage \
    --user-data-dir="$profile" \
    --print-to-pdf="$pdf" "file://$html" 2>/dev/null
  rm -rf "$profile"
  echo "Created: $(basename "$pdf")"
}

chrome_pdf "$DIR/01-executive-brief.html" "$OUT/01-Executive-Brief.pdf"
chrome_pdf "$DIR/02-practitioner-playbook.html" "$OUT/02-Practitioner-Playbook.pdf"
chrome_pdf "$DIR/03-workshop-kit.html" "$OUT/03-Workshop-Kit.pdf"
chrome_pdf "$DIR/04-steerco-pack.html" "$OUT/04-SteerCo-Pack.pdf"
chrome_pdf "$DIR/../enterprise-agile-enablement-playbook.html" "$DIR/../Enterprise-Agile-Enablement-Study-Bible-and-Playbook.pdf"

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
writer.write(str(out / "00-Full-Pack-Combined.pdf"))
writer.close()
print("Merged: 00-Full-Pack-Combined.pdf")
PY

echo "Done."
ls -lh "$OUT"/*.pdf "$DIR/../Enterprise-Agile-Enablement-Study-Bible-and-Playbook.pdf"
