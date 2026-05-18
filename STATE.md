# STATE.md — Partner Program OS
> **APPEND-ONLY.** Never rewrite. Add new entries at the bottom.
> Format: `## SESSION YYYY-MM-DD · [topic]`

---

## SESSION 2026-05-18 · Site Build — Method + Partner Mapping + ABSM skeleton

### What was done
- Built complete `docs/` site structure: 8 HTML pages + 37 MD placeholders + CSS
- Established design system: Source Serif 4 + DM Sans, consulting-minimal, warm neutrals

### Files created (complete, no stubs)
| File | Status |
|---|---|
| `docs/index.html` | ✅ Memo — story arc, Three Perspectives, 30/60/90 |
| `docs/assets/css/main.css` | ✅ Full design system |
| `docs/method/index.html` | ✅ 7-stage lifecycle + 7×3 maturity table |
| `docs/method/spider-chart.html` | ✅ Interactive radar — draggable, no Akamai scores |
| `docs/method/scorecard-template.html` | ✅ Full 7×3 scorecard with KPI tags |
| `docs/partner-mapping/index.html` | ✅ 6-dim IPP, research overview, disposition table |
| `docs/partner-mapping/dach-landscape.html` | ✅ 33-partner matrix, filterable |
| `docs/partner-mapping/pursue-five/index.html` | ✅ 5 partner profiles with outreach hooks |
| `docs/absm-sprint/index.html` | ✅ 5-phase program, 4 client cards, AI angle |

### Files created (stubs — need repo content)
- `docs/partner-mapping/entanglement/*.md` (4 files) ← copy from `02-akamai/research/outputs/entanglement/`
- `docs/partner-mapping/pursue-five/*.md` (5 files) ← split from `02-akamai/research/outputs/d3-1/d3-1-pursue-priority-five.md`
- `docs/absm-sprint/01-targeting/*.md` (5 files) ← copy from `02-akamai/03-dach-projects/absm-sprint/01-targeting/`
- `docs/absm-sprint/02-strategy/*.md` (4 files) ← copy from `02-akamai/03-dach-projects/absm-sprint/02-strategy/`
- `docs/absm-sprint/03-clients/**/*.md` (16 files) ← copy from `02-akamai/03-dach-projects/absm-sprint/03-clients/`
- `docs/absm-sprint/05-infrastructure/*.md` (3 files) ← copy from `02-akamai/03-dach-projects/absm-sprint/05-infrastructure/`

### Not yet built
- `docs/absm-sprint/05-infrastructure/kpi-dashboard.html` — build new
- `docs/absm-sprint/04-collateral/*.pdf` — copy 12 PDFs from `02-akamai/03-dach-projects/absm-sprint/04-execution/`
- `docs/absm-sprint/03-clients/*/executive-brief.pdf` — copy per-client PDFs
- PDF export of homepage for Mark

### Decisions locked this session
- Partner Mapping URL: `partner-mapping/` ✓
- Pursue Five: Axians+Fernao, AVANTEC, SVA, ACP Gruppe, InfoGuard ✓
- InfoGuard: deepen existing (already Akamai partner), not cold recruit ✓
- Scorecard v1.3 (concrete Akamai scores): reference only, NOT published ✓

---
<!-- ADD NEW SESSIONS BELOW THIS LINE -->

## SESSION 2026-05-19 · Redesign Brief + KPI Dashboard + Docs Fill

### What was done
- Built `kpi-dashboard.html` — full interactive dashboard adapted from Axians dark-theme to docs site design system
- Ran `fill-docs-stubs.sh` — copied 46 source files into docs/ (0 warnings, 78 total files in docs/)
- Created `REDESIGN_BRIEF.md` — comprehensive spec for site v2 (12 design decisions locked)

### Decisions locked this session (12)
1. CSS: Akamai-inspired palette + clean spacing (show 2 variants)
2. MD rendering: every .md → full .html with nav, styles, sidebar
3. TOC: collapsible sidebar on every page
4. Back nav: sidebar sufficient
5. Exec summaries: McKinsey-style bullet-list with anchor links
6. Language: keep source file languages as-is
7. Sidebar: visible desktop, hamburger mobile
8. Reading guide: short block on homepage
9. Workflow: brief → Opus 4.7 (copy) → Opus 4.6 (code) → OpenClaw merge
10. Copy scope: homepage + 3 perspective pages
11. Name: A. Marushevsky everywhere
12. Timeline: ship today

### Commit log
- c14daee: fill docs stubs + kpi-dashboard (46 files, 0 warnings)
- [pending]: REDESIGN_BRIEF.md + STATE.md patch

### Next steps
- Opus 4.7 chat: copywriting (homepage + 3 perspectives)
- Opus 4.6 chat: new CSS + sidebar + MD→HTML conversion
- OpenClaw: merge all
