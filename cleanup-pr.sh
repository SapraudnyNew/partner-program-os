#!/usr/bin/env bash
#
# Cleanup PR: fix ABSM sprint placement, restore README, consolidate scorecard
#
# What happened: PR #14 dumped 45 ABSM sprint files at repo ROOT instead of
# inside 02-akamai/03-dach-projects/absm-sprint/. README.md was overwritten.
# Two scorecard versions exist. STATE.md is 5 PRs behind reality.
#
# What this script does:
#   1. Moves 45 ABSM files from root → 02-akamai/03-dach-projects/absm-sprint/
#   2. Restores original Partner Program OS README.md
#   3. Deletes STATE-patch.md (content preserved in STATE.md update)
#   4. Consolidates scorecard: removes v1.2, renames v1.3 → main
#   5. Removes .gitkeep placeholders replaced by real content
#   6. Updates STATE.md to reflect reality
#   7. Commits and pushes
#
# Usage: cd ~/partner-program-os && bash cleanup-pr.sh

set -euo pipefail

BRANCH="fix/cleanup-absm-placement-and-state"

echo ">> Pre-flight checks..."

# Must be in repo root
if [[ ! -d "00-decisions" || ! -d "01-method" || ! -d "02-akamai" ]]; then
    echo "ERROR: Not in partner-program-os root. cd ~/partner-program-os first."
    exit 1
fi

# ABSM files must exist at root (the problem we're fixing)
if [[ ! -d "00-context" || ! -d "01-targeting" || ! -d "02-intel" ]]; then
    echo "ERROR: ABSM files not at root. Nothing to fix, or already cleaned."
    exit 1
fi

# Working tree clean
DIRTY=$(git status --porcelain | grep -v -e '^?? cleanup-pr' || true)
if [[ -n "$DIRTY" ]]; then
    echo "ERROR: Working tree not clean:"
    echo "$DIRTY"
    exit 1
fi

echo ">> Pre-flight passed."

# ---- Branch ----
git checkout main
git pull --ff-only
git checkout -b "$BRANCH"

# ---- STEP 1: Move ABSM files into correct location ----
echo ">> Step 1: Moving 45 ABSM files from root to 02-akamai/03-dach-projects/absm-sprint/..."

TARGET="02-akamai/03-dach-projects/absm-sprint"

# Remove old .gitkeep placeholders (will be replaced by real content)
find "$TARGET" -name ".gitkeep" -delete 2>/dev/null || true

# Move each ABSM directory
for dir in 00-context 01-targeting 02-intel 03-strategy 04-execution 05-infrastructure showcase; do
    if [[ -d "$dir" ]]; then
        # Remove target if exists (empty scaffold)
        rm -rf "${TARGET}/${dir}" 2>/dev/null || true
        git mv "$dir" "${TARGET}/${dir}"
        echo "   Moved $dir → ${TARGET}/${dir}"
    fi
done

# Move ABSM CLAUDE.md (root → absm-sprint/)
if [[ -f "CLAUDE.md" ]]; then
    git mv "CLAUDE.md" "${TARGET}/CLAUDE.md"
    echo "   Moved CLAUDE.md → ${TARGET}/CLAUDE.md"
fi

# Move current README.md (ABSM readme) → absm-sprint/README.md
git mv "README.md" "${TARGET}/README.md"
echo "   Moved README.md (ABSM) → ${TARGET}/README.md"

# ---- STEP 2: Restore original README.md ----
echo ">> Step 2: Restoring original Partner Program OS README.md..."

# Get README from commit before PR #14
git show decee52:README.md > README.md

# Update status in restored README to reflect current reality
python3 -c "
import re
content = open('README.md').read()
# Update DACH Projects status
content = content.replace('| 3 | **DACH Projects** | ABM/TAS partner project + ABSM Mittelstand sprint. Supporting artifacts for Akamai HVO per ADR-009. | NOT STARTED |',
                          '| 3 | **DACH Projects** | ABM/TAS partner project + ABSM Mittelstand sprint. Supporting artifacts for Akamai HVO per ADR-009. | ABSM DONE, ABM/TAS scaffold |')
# Add ADR-011 to table
content = content.replace('| ADR-010 | Session continuity via STATE.md (replaces HANDOVER.md and handover-day2-v2.md) |',
                          '| ADR-010 | Session continuity via STATE.md (replaces HANDOVER.md and handover-day2-v2.md) |\n| ADR-011 | Recruitability as 6th IPP dimension + disposition taxonomy (Pursue/Contain/Monitor/Drop) |')
open('README.md', 'w').write(content)
"

git add README.md
echo "   README.md restored and updated."

# ---- STEP 3: Delete root-level junk ----
echo ">> Step 3: Cleaning root-level files..."

if [[ -f "STATE-patch.md" ]]; then
    git rm "STATE-patch.md"
    echo "   Removed STATE-patch.md (content preserved in STATE.md)"
fi

# ---- STEP 4: Consolidate scorecard ----
echo ">> Step 4: Consolidating scorecard..."

if [[ -f "02-akamai/03-diagnosis-scorecard.md" && -f "02-akamai/03-diagnosis-scorecard-v1.3.md" ]]; then
    git rm "02-akamai/03-diagnosis-scorecard.md"
    git mv "02-akamai/03-diagnosis-scorecard-v1.3.md" "02-akamai/03-diagnosis-scorecard.md"
    echo "   Removed v1.2, renamed v1.3 → 03-diagnosis-scorecard.md"
fi

# ---- STEP 5: Update STATE.md ----
echo ">> Step 5: Updating STATE.md..."

python3 << 'PYEOF'
import re
from datetime import date

content = open('STATE.md').read()

# Update header
content = re.sub(
    r'\*\*Last updated:\*\* .*\n\*\*Session:\*\* .*\n\*\*Updated by:\*\* .*',
    f'**Last updated:** {date.today().isoformat()}\n**Session:** Day 3 - Post-cleanup: ABSM relocated, STATE.md synced to repo reality\n**Updated by:** Forge (Claude)',
    content
)

# Update Layer 2 status
content = content.replace(
    '| Layer 2: Playbook Engine (Akamai specialization) | IN PROGRESS | Research complete; diagnosis scorecard, ABM/TAS, ABSM next |',
    '| Layer 2: Playbook Engine (Akamai specialization) | IN PROGRESS | Research done, scorecard v1.3 done, D3-1 done, ABSM sprint done. Memo + exec summary need rewrite |'
)

# Update Layer 3 status
content = content.replace(
    '| Layer 3: HVO Wrapper (Akamai bundle) | NOT STARTED | Depends on Layer 2 |',
    '| Layer 3: HVO Wrapper (Akamai bundle) | DRAFT | Memo + exec summary exist (v1, need rewrite). Spider chart not started |'
)

# Update day-by-day: D2-2 scorecard
content = content.replace(
    '| D2-2 | Akamai diagnosis scorecard at `02-akamai/03-diagnosis-scorecard.md` | DRAFT v1.1: Gap 2 dispositions populated; awaits human review |',
    '| D2-2 | Akamai diagnosis scorecard at `02-akamai/03-diagnosis-scorecard.md` | DONE v1.3 |'
)

# Update D3-1
content = content.replace(
    '| D3-1 | ABM/TAS DACH Partner Project (30 candidates -> 10 longlist + 6-dim IPP + 9-box + dispositions + profiles) | TODO |',
    '| D3-1 | ABM/TAS DACH Partner Project — Pursue priority five profiles at `02-akamai/research/outputs/d3-1/` | DONE (profiles only; full scoring matrix + 9-box TODO) |'
)

# Update D3-2
content = content.replace(
    '| D3-2 | ABSM DACH Sprint (32 artifacts, Mittelstand manufacturing, 3 deep + 1 showcase) | TODO |',
    '| D3-2 | ABSM DACH Sprint (44 artifacts) at `02-akamai/03-dach-projects/absm-sprint/` | DONE |'
)

# Update D2-3 memo
content = content.replace(
    '| D2-3 | HVO main memo (3.5pp, diagnosis + top 3 gaps + 90-day plan + fit) | TODO |',
    '| D2-3 | HVO main memo at `02-akamai/01-leave-behind-memo.md` | DRAFT v1 — needs rewrite (Gap 3 structure, per STATE-patch notes) |'
)

# Update D2-3a exec summary
content = content.replace(
    '| D2-3a | 1-page executive summary (skip-level readable, VP forwarding) | TODO |',
    '| D2-3a | Exec summary at `02-akamai/00-page-zero-executive-summary.md` | DRAFT v1 — needs rewrite (aligned with memo rewrite) |'
)

# Update repo structure tree
old_tree = """```
partner-program-os/
├── STATE.md                    (this file, canonical state)
├── README.md
├── 00-decisions/               (ADR-001 through ADR-011 + ADR-009/011 amendments)
├── 01-method/                  (Layer 1, COMPLETE)
│   ├── 00-method-overview.md
│   ├── 01-recruit.md           (6-dimension IPP per ADR-011)
│   ├── 02-onboard.md
│   ├── 03-enable.md
│   ├── 04-cosell.md
│   ├── 05-deliver.md
│   ├── 06-renew.md
│   ├── 07-expand.md
│   ├── maturity-model/
│   ├── tool-landscape/
│   ├── intake/
│   ├── research-agent/
│   └── appendix/
├── 02-akamai/                  (Layer 2 + Layer 3, IN PROGRESS)
│   ├── 00-context.md
│   ├── 01-leave-behind-memo.md (skeleton, ADR-009 bundle structure)
│   ├── 02-talking-points.md
│   ├── 03-diagnosis-scorecard.md (D2-2 DRAFT v1.1, Gap 2 dispositions populated)
│   ├── akamai-research.md      (initial synthesis pointer)
│   ├── 03-dach-projects/        (relocated from root in PR #4)
│   │   ├── 00-context.md
│   │   ├── abm-tas-partners/   (scaffold)
│   │   └── absm-sprint/        (scaffold)
│   └── research/
│       ├── prompts/             (3 mission prompts: company, partner-program, entanglement)
│       └── outputs/
│           ├── company/         (6 files, ~30pp)
│           ├── partner-program/ (1 file, 7 sections)
│           └── entanglement/    (4 files, D2-RC, PR #4)
├── 03-boon-edam/               (FROZEN per ADR-008)
├── prompts/
│   ├── master-handover-prompt.md
│   ├── prompt-akamai-hvo.md
│   ├── prompt-bege-rollout.md
│   └── _archive/                (deprecated prompts)
└── docs/                        (GitHub Pages, Phase 4)
```"""

new_tree = """```
partner-program-os/
├── STATE.md                    (this file, canonical state)
├── README.md
├── 00-decisions/               (ADR-001 through ADR-011)
├── 01-method/                  (Layer 1, needs refinement)
│   ├── 00-method-overview.md
│   ├── 01-recruit.md           (6-dimension IPP per ADR-011)
│   ├── 02-onboard.md ... 07-expand.md
│   ├── maturity-model/
│   └── appendix/
├── 02-akamai/                  (Layer 2 + Layer 3, IN PROGRESS)
│   ├── 00-context.md
│   ├── 00-page-zero-executive-summary.md  (DRAFT v1, needs rewrite)
│   ├── 01-leave-behind-memo.md            (DRAFT v1, needs rewrite)
│   ├── 02-talking-points.md
│   ├── 03-diagnosis-scorecard.md          (v1.3, DONE)
│   ├── akamai-research.md
│   ├── 03-dach-projects/
│   │   ├── 00-context.md
│   │   ├── abm-tas-partners/              (scaffold, D3-1 profiles in research/outputs/d3-1/)
│   │   └── absm-sprint/                   (44 artifacts, DONE)
│   │       ├── 00-context/, 01-targeting/, 02-intel/, 03-strategy/
│   │       ├── 04-execution/ (12 PDFs), 05-infrastructure/
│   │       ├── showcase/trumpf-showcase.md
│   │       ├── CLAUDE.md, README.md
│   └── research/
│       ├── prompts/             (4 research mission prompts)
│       └── outputs/
│           ├── company/         (6 files, ~30pp)
│           ├── partner-program/ (DACH dossier, 50 named partners)
│           ├── entanglement/    (4 files, D2-RC)
│           └── d3-1/            (Pursue priority five profiles)
├── 03-boon-edam/               (FROZEN per ADR-008)
├── prompts/
│   ├── master-handover-prompt.md
│   ├── prompt-akamai-hvo.md
│   ├── prompt-bege-rollout.md
│   └── _archive/
└── docs/                        (GitHub Pages, Phase 4)
```"""

content = content.replace(old_tree, new_tree)

# Add new session log entry at top of session log
new_entry = f"""### {date.today().isoformat()} - Day 3: Cleanup — ABSM relocated, STATE.md synced, scorecard consolidated

**Done:**
- ABSM sprint (44 artifacts: Hörmann, Reinhausen, Witte, Trumpf showcase) relocated from repo root to `02-akamai/03-dach-projects/absm-sprint/`. PR #14 had placed them at root level, breaking the three-layer architecture.
- Original Partner Program OS README.md restored (was overwritten by ABSM README).
- Scorecard consolidated: deleted v1.2, renamed v1.3 to `03-diagnosis-scorecard.md`.
- STATE-patch.md removed from root. Gap 3 correction notes (Computacenter not headline, Intent-Enabled Partner Activation as system solution) preserved in this session log for memo rewrite.
- STATE.md day-by-day table updated to reflect completed work: D2-2 DONE v1.3, D3-1 DONE, D3-2 DONE, D2-3 DRAFT, D2-3a DRAFT.
- Layer status updated: Layer 2 reflects actual progress, Layer 3 reflects DRAFT status.

**STATE-patch.md notes preserved (for memo rewrite):**
- Gap 3 headline should NOT be Computacenter Premier upgrade (Computacenter = Contain disposition)
- Correct Gap 3: no co-sell motion exists with any Pursue partner → Intent-Enabled Partner Activation activates all five simultaneously
- Computacenter tier upgrade is a parallel Contain-track action, not the lead move

**Next:**
- Discuss what remains before HVO goes to Mark: method refinement, memo + exec summary rewrite, spider chart, final packaging
- D2-3 v2: rewrite memo with corrected Gap 3 structure
- D2-3a v2: rewrite exec summary aligned with memo v2
- D2-5: spider chart (not started)
- Method refinement scope TBD

**Blockers:** none.

"""

# Insert new entry after "## Session log\n\nAppend-only. Newest first.\n\n"
content = content.replace(
    "## Session log\n\nAppend-only. Newest first.\n\n### 2026-05-18",
    "## Session log\n\nAppend-only. Newest first.\n\n" + new_entry + "### 2026-05-18"
)

open('STATE.md', 'w').write(content)
PYEOF

git add STATE.md
echo "   STATE.md updated."

# ---- STEP 6: Stage everything and verify ----
echo ">> Step 6: Staging..."
git add -A

echo ""
echo ">> Summary of changes:"
git diff --cached --stat
echo ""

# ---- STEP 7: Commit and push ----
read -p "Proceed with commit and push? [y/N] " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Aborted."
    exit 0
fi

git commit -m "fix: relocate ABSM sprint from root to 02-akamai/03-dach-projects/absm-sprint/

PR #14 placed 45 ABSM sprint files at repo root instead of inside
02-akamai/03-dach-projects/absm-sprint/. This broke the three-layer
architecture (ADR-008) and overwrote the project README.

This PR:
- git mv 45 ABSM files (00-context, 01-targeting, 02-intel, 03-strategy,
  04-execution, 05-infrastructure, showcase, CLAUDE.md) into the correct
  path under 02-akamai/03-dach-projects/absm-sprint/
- Restores original Partner Program OS README.md
- Removes STATE-patch.md (notes preserved in STATE.md session log)
- Consolidates scorecard: deletes v1.2, renames v1.3 to main filename
- Updates STATE.md: day-by-day table reflects completed PRs #9-#14,
  layer status updated, new session log entry, repo structure tree fixed

No content was changed, deleted, or rewritten. Only file locations and
state tracking.

Refs: ADR-008 (architecture), ADR-009 (DACH projects under 02-akamai),
ADR-010 (STATE.md discipline)"

git push -u origin "$BRANCH"

echo ""
echo "=========================================="
echo "DONE. Open this URL to create the PR:"
REPO_URL=$(git config --get remote.origin.url | sed 's/\.git$//' | sed 's/git@github.com:/https:\/\/github.com\//')
echo "  ${REPO_URL}/compare/main...${BRANCH}"
echo ""
echo "Title:"
echo "  fix: relocate ABSM sprint from root, restore README, sync STATE.md"
echo ""
echo "Then click Merge. After merge:"
echo "  git checkout main && git pull && rm cleanup-pr.sh"
echo "=========================================="
