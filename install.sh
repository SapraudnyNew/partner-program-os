#!/bin/bash
# ============================================================
# install.sh — HVO Mini-Site · Deploy archive into repo
# Usage: bash install.sh <path-to-archive.tar.gz>
# Run from repo root: partner-program-os/
# ============================================================

set -e

ARCHIVE="${1:-hvo-handover-2026-05-18.tar.gz}"

if [ ! -f "$ARCHIVE" ]; then
  echo "❌  Archive not found: $ARCHIVE"
  echo "    Usage: bash install.sh hvo-handover-2026-05-18.tar.gz"
  exit 1
fi

echo "📦  Unpacking $ARCHIVE..."
tar -xzf "$ARCHIVE"

echo "📋  Copying STATE.md and MASTER_HANDOVER.md to repo root..."
# They unpack to root already — just verify
[ -f STATE.md ] && echo "   ✅  STATE.md" || echo "   ⚠️  STATE.md missing"
[ -f MASTER_HANDOVER.md ] && echo "   ✅  MASTER_HANDOVER.md" || echo "   ⚠️  MASTER_HANDOVER.md missing"

echo "🌐  Verifying docs/ structure..."
HTML_COUNT=$(find docs/ -name "*.html" | wc -l | tr -d ' ')
MD_COUNT=$(find docs/ -name "*.md" | wc -l | tr -d ' ')
echo "   HTML pages : $HTML_COUNT"
echo "   MD files   : $MD_COUNT"
echo "   CSS        : $(find docs/ -name "*.css" | wc -l | tr -d ' ')"

echo ""
echo "✅  Done. Next steps:"
echo ""
echo "   1. git add docs/ STATE.md MASTER_HANDOVER.md"
echo "   2. git commit -m 'feat: HVO mini-site build 2026-05-18'"
echo "   3. git push origin main"
echo ""
echo "   Then enable GitHub Pages:"
echo "   Settings → Pages → Source: /docs/ from main"
echo ""
echo "   Live at: https://sapraudnynew.github.io/partner-program-os/"
