#!/usr/bin/env bash
#
# Update STATE.md with HVO site decisions + remove orphaned cleanup-pr.sh
# + enable GitHub Pages structure
#
# Usage: cd ~/partner-program-os && bash state-update-and-pages-prep.sh

set -euo pipefail

BRANCH="feat/hvo-site-state-update-and-pages-prep"

echo ">> Pre-flight..."
if [[ ! -d "00-decisions" ]]; then
    echo "ERROR: Not in partner-program-os root."
    exit 1
fi

git checkout main
git pull --ff-only
git checkout -b "$BRANCH"

# ---- Remove orphaned cleanup-pr.sh ----
if [[ -f "cleanup-pr.sh" ]]; then
    git rm cleanup-pr.sh
    echo ">> Removed orphaned cleanup-pr.sh"
fi

# ---- Update STATE.md ----
echo ">> Updating STATE.md..."

python3 << 'PYEOF'
from datetime import date

content = open('STATE.md').read()

# Update header
content = content.replace(
    '**Last updated:** 2026-05-18\n**Session:** Day 3 - Post-cleanup: ABSM relocated, STATE.md synced to repo reality\n**Updated by:** Forge (Claude)',
    f'**Last updated:** {date.today().isoformat()}\n**Session:** Day 3.5 - HVO site architecture locked, 18 decisions, build starting\n**Updated by:** Forge (Claude)'
)

# Update Layer 3 status
content = content.replace(
    '| Layer 3: HVO Wrapper (Akamai bundle) | DRAFT | Memo + exec summary exist (v1, need rewrite). Spider chart not started |',
    '| Layer 3: HVO Wrapper (Akamai bundle) | IN PROGRESS | Architecture locked: GitHub Pages mini-site. Memo v2 = homepage. 3 perspectives + artifacts. Spider chart = framework illustration. Ship today. |'
)

# Add new session log entry
new_entry = f"""### {date.today().isoformat()} - Day 3.5: HVO site architecture locked — 18 decisions

**Format decision:** HVO is a GitHub Pages mini-site (not PDF-first). Motivation letter with proof-of-work artifacts.
- Homepage = memo v2 (2 pages printed). Storytelling intro + Three Perspectives + 30/60/90.
- Perspective 1: Method & Vision (method/) — 7-stage lifecycle + maturity framework + spider chart (framework illustration, NO Akamai scores)
- Perspective 2: Partner Mapping & Prioritization (partner-mapping/) — 6-dim IPP + 33-partner matrix + entanglement + Pursue Five
- Perspective 3: ABSM Partner Enablement for Axians (absm-sprint/) — 4 clients (Hörmann, Reinhausen, Witte, Trumpf) + AI angle
- Each perspective has landing page + inline links to artifact files
- URL: sapraudnynew.github.io/partner-program-os

**18 decisions locked:**
1. Cisco ABM: helped implement ABM at Cisco partners, passwordless authentication, partner portal playbooks
2. Section naming: "Three Perspectives" (not gaps)
3. Maturity: framework only, no Akamai scores
4. Partner research: full 33-partner matrix with "first pass" caveat. Entanglement shown.
5. ABSM: all 4 companies named
6. Hosting: GitHub Pages from /docs/, repo private
7. AI: dedicated point in ABSM section
8. CV: separate file, parallel track
9. Memo: 2 pages max, links to details
10. Site structure: homepage + 3 perspectives + detail pages
11. Design: minimal professional consulting-style
12. Domain: default github.io
13. Privacy: artifacts copied to /docs/, rest stays private
14. Mark receives: CV + 1 PDF (memo) + site link
15. Spider chart: framework illustration (no scores)
16. Timeline: ship today
17. Trumpf: 4th client, not separate showcase
18. URL naming: partner-mapping/ (title: "Partner Mapping & Prioritization")

**30/60/90 rewrite:**
- Days 1-30: learn Akamai inside, study best practices, shadow best partner manager, meet partners
- Days 31-60: validate research with internal data, begin Pursue partner conversations
- Days 61-90: first joint pipeline review, activate co-marketing, establish measurement cadence

**Intro storytelling (new):**
- Physical security → IT evolution (not random switch)
- Boon Edam: built partner program from scratch, global clients/partners, conservative company
- Russia: ABM implementation for Cisco partners
- Wants to grow into developed IT company like Akamai

**Method refinement:** needed before HVO ships. Approach: don't rewrite 01-method/ source files. Create adapted web versions in docs/method/. Source stays as detailed reference.

**Cleanup:** removed orphaned cleanup-pr.sh from repo.

**Next:** Build the site. Start with Perspective 1 (Method) in next chat session.

**Blockers:** none.

"""

content = content.replace(
    "## Session log\n\nAppend-only. Newest first.\n\n### 2026-05-18 - Day 3:",
    "## Session log\n\nAppend-only. Newest first.\n\n" + new_entry + "### 2026-05-18 - Day 3:"
)

open('STATE.md', 'w').write(content)
PYEOF

git add STATE.md
echo ">> STATE.md updated."

# ---- Prepare /docs/ skeleton ----
echo ">> Creating /docs/ skeleton..."

mkdir -p docs/assets/css
mkdir -p docs/method
mkdir -p docs/partner-mapping/entanglement
mkdir -p docs/partner-mapping/pursue-five
mkdir -p docs/absm-sprint/01-targeting
mkdir -p docs/absm-sprint/02-strategy
mkdir -p docs/absm-sprint/03-clients/hoermann
mkdir -p docs/absm-sprint/03-clients/reinhausen
mkdir -p docs/absm-sprint/03-clients/witte
mkdir -p docs/absm-sprint/03-clients/trumpf
mkdir -p docs/absm-sprint/04-collateral
mkdir -p docs/absm-sprint/05-infrastructure

# Placeholder index so GitHub Pages has something
cat > docs/index.html << 'HTML'
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Partner Program OS — Coming Soon</title></head>
<body><h1>Site under construction</h1><p>Full content launching shortly.</p></body>
</html>
HTML

# Add .nojekyll to use raw HTML (no Jekyll processing)
touch docs/.nojekyll

git add docs/
echo ">> /docs/ skeleton created."

# ---- Stage and commit ----
git add -A

echo ""
echo ">> Changes:"
git diff --cached --stat
echo ""

read -p "Commit and push? [y/N] " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Aborted."
    exit 0
fi

git commit -m "feat: HVO site architecture locked — STATE.md update + /docs/ skeleton + cleanup

18 decisions from architecture session locked in STATE.md session log.
Layer 3 status updated to IN PROGRESS.

/docs/ directory structure created matching agreed site architecture:
- docs/method/ (Perspective 1: 7-stage lifecycle + maturity)
- docs/partner-mapping/ (Perspective 2: IPP + entanglement + Pursue Five)
- docs/absm-sprint/ (Perspective 3: ABM for Axians × 4 clients)
- docs/.nojekyll (raw HTML, no Jekyll processing)
- Placeholder index.html

Removed orphaned cleanup-pr.sh from PR #15.

Next: populate /docs/ with content in build session."

git push -u origin "$BRANCH"

echo ""
echo "=========================================="
echo "DONE. Create PR:"
REPO_URL=$(git config --get remote.origin.url | sed 's/\.git$//' | sed 's/git@github.com:/https:\/\/github.com\//')
echo "  ${REPO_URL}/compare/main...${BRANCH}"
echo ""
echo "Title: feat: HVO site architecture + /docs/ skeleton"
echo ""
echo "After merge:"
echo "  git checkout main && git pull && rm state-update-and-pages-prep.sh"
echo ""
echo "THEN enable GitHub Pages:"
echo "  1. Go to: ${REPO_URL}/settings/pages"
echo "  2. Source: Deploy from a branch"
echo "  3. Branch: main"
echo "  4. Folder: /docs"
echo "  5. Save"
echo "=========================================="
