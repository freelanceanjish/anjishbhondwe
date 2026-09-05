#!/usr/bin/env bash
set -euo pipefail

BUILD_DIR="/workspace/.cv-build"
OUT_DIR="/workspace/applications/leaseweb-agile-team-manager"

render_pdf() {
  local html="$1"
  local pdf="$2"
  local profile="/tmp/chrome-pdf-$$-$RANDOM"
  timeout 60 /usr/bin/google-chrome-stable --headless=new --disable-gpu --no-sandbox \
    --no-pdf-header-footer --disable-dev-shm-usage \
    --user-data-dir="$profile" --remote-debugging-port=0 \
    --print-to-pdf="$pdf" "file://$html" 2>/dev/null
  rm -rf "$profile"
  echo "Rendered: $(basename "$pdf")"
}

mkdir -p "$OUT_DIR"

for html in "$BUILD_DIR"/anjish-bhondwe-*.html; do
  base="$(basename "$html" .html)"
  render_pdf "$html" "$OUT_DIR/${base}.pdf"
done

ls -lh "$OUT_DIR"/anjish-bhondwe-*.pdf
