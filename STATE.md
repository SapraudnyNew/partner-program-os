# Project State

> **Always current. Single source of truth for project status.**
> Replaces the previous HANDOVER.md and handover-day2-v2.md.
> Discipline defined in ADR-010 (session continuity).

**Last updated:** 2026-05-17
**Session:** Day 2 - research integration + documentation sync
**Updated by:** Forge (Claude)

---

## Project: Partner Program OS

Reverse Job Search Method (RJSM) deliverable. Three-layer architecture per ADR-008, DACH projects supporting layer added per ADR-009.

Target role: Senior Channel Marketing Manager, Akamai DACH, Zero Trust.
Path: warm referral via Mark Shelepov (Principal Lead Architect, Akamai US).

## Layer status

| Layer | Status | Notes |
|---|---|---|
| Layer 1: The Method | COMPLETE | 7 stages filled to depth, evidence library (P-01..P-50, E-01..E-12), maturity scorecard, glossary |
| Layer 2: Playbook Engine (Akamai specialization) | IN PROGRESS | Research complete; diagnosis scorecard, ABM/TAS, ABSM next |
| Layer 3: HVO Wrapper (Akamai bundle) | NOT STARTED | Depends on Layer 2 |

## Day-by-day execution status

| Block | Deliverable | Status |
|---|---|---|
| D1-1 to D1-8 | Method universal template (overview + 7 stages + scorecard + maturity framework) | DONE |
| D2-1 | Akamai initial research (akamai-research.md) | DONE |
| D2-R | Deep research prompts v2 (company + partner program) | DONE |
| D2-RA | Akamai company deep research (6 files, ~30pp, 60+ pages combined) | DONE |
| D2-RB | Akamai partner program DACH dossier (50 named partners, 7 sections) | DONE |
| D2-2 | Akamai diagnosis scorecard (apply maturity model to Akamai using new research) | NEXT |
| D3-1 | ABM/TAS DACH Partner Project (30 candidates -> 10 longlist + IPP + 9-box + profiles) | TODO |
| D3-2 | ABSM DACH Sprint (32 artifacts, Mittelstand manufacturing, 3 deep + 1 showcase) | TODO |
| D2-3 | HVO main memo (3.5pp, diagnosis + top 3 gaps + 90-day plan + fit) | TODO |
| D2-3a | 1-page executive summary (skip-level readable, VP forwarding) | TODO |
| D2-4 | HVO direct approach version (VP/Director-level frame, fallback) | TODO |
| D2-5 | Spider chart (3 design options presented, then static + interactive build) | TODO |
| D2-5a | Web hosting decision and setup for interactive artifacts | TODO |
| D2-6 | PDF export of HVO main bundle | TODO |
| D2-7 | Revision pass across deliverables, rate target 8+ on Forge scale | TODO |

## Locked context (do not relitigate)

Per ADR-008, ADR-009, and the 22 locked decisions on May 15:

- **Referrer:** Mark Shelepov, Principal Lead Architect at Akamai (US, Rhode Island). 2nd-degree connection. Path: Mark sends internal referral. Akamai sends Alex application invitation. Alex does NOT apply through job posting.
- **Role:** Senior Channel Marketing Manager, DACH, Zero Trust.
- **Positioning:** bait-and-switch per ADR-006. Manager-grade content, executive-grade signals.
- **Headline artifact:** HVO bundle per ADR-009, not standalone memo. Includes 1pp exec summary + 3.5pp memo + ABM/TAS bundle + ABSM bundle + spider chart.
- **HVO opening:** opens cold with diagnosis. Referrer NOT named in cover.
- **Boon Edam:** removed from main HVO proof layer. May appear briefly in fit section as credibility anchor.
- **ABSM territory:** Germany only. Austria and Switzerland excluded for research depth.
- **ABSM vertical:** Mittelstand manufacturing, NIS2 essential and important entities.
- **ABSM target band:** EUR 100M-2B revenue, 1000-10000 employees, below Akamai direct sales threshold.
- **ABSM funnel:** 30 candidates -> 10 scored -> 3 deep + 1 publicly-named showcase.
- **Target naming:** real DACH companies named in ABSM artifacts.

## Research outputs (committed to repo)

- `02-akamai/research/prompts/` - the two v2 research mission prompts (DONE earlier)
- `02-akamai/research/outputs/company/` - 6 files, ~30 pages: corporate fundamentals, DACH regional intelligence, cultural and operational intelligence, channel marketing organization, risks and questions, master summary (COMING IN PR #2)
- `02-akamai/research/outputs/partner-program/akamai-partner-program-dach-dossier.md` - 7-section dossier, 50 named DACH partners, displacement targets identified (COMING IN PR #2)
- `02-akamai/akamai-research.md` - initial research synthesis (now serves as pointer/index to deep research)

## Key displacement targets from partner research

For ABM/TAS work:
- **KAEMI GmbH** (Berlin) - Illumio EMEA Partner of the Year. Top displacement target.
- **Navixia SA** (Ecublens, CH) - first EMEA partner to reach Illumio ZTS Professional. Top displacement target.
- **Computacenter** - dual partner (both Akamai and Illumio). Tier upgrade opportunity Select -> Premier.

For anchor deepening:
- Deutsche Telekom Security
- Bechtle AG / Bechtle Schweiz
- Controlware
- InfoGuard (CH)

For Mittelstand recruitment:
- SVA, Cancom, Axians (systemhauser)

## Active ADRs

| ADR | Decision |
|---|---|
| ADR-001 | Repo private + selective public via /docs |
| ADR-002 | English canonical, no Russian fork |
| ADR-003 | 7-stage lifecycle structure |
| ADR-004 | Three-reader model in one document |
| ADR-005 | Evidence in appendix, [P-NN] and [E-NN] refs |
| ADR-006 | Akamai HVO is warm-referral leave-behind, bait-and-switch |
| ADR-007 | BEGE rollout map dual versions (public + internal) |
| ADR-008 | Three-layer architecture frozen |
| ADR-009 | DACH projects as Day 2 supporting artifacts |
| ADR-010 | Session continuity via STATE.md discipline |

## Repo structure (current)

```
partner-program-os/
├── STATE.md                    (this file, canonical state)
├── README.md
├── 00-decisions/               (ADR-001 through ADR-010)
├── 01-method/                  (Layer 1, COMPLETE)
│   ├── 00-method-overview.md
│   ├── 01-recruit.md
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
│   ├── akamai-research.md      (initial synthesis)
│   └── research/
│       ├── prompts/
│       └── outputs/             (PR #2 adds this)
├── 03-boon-edam/               (FROZEN per ADR-008)
├── 03-dach-projects/           (NOT STARTED, scaffolded per ADR-009)
│   ├── 00-context.md
│   ├── abm-tas-partners/       (scaffold only)
│   └── absm-sprint/            (scaffold only)
├── prompts/
│   ├── master-handover-prompt.md
│   ├── prompt-akamai-hvo.md
│   ├── prompt-bege-rollout.md
│   └── _archive/                (deprecated prompts)
└── docs/                        (GitHub Pages, Phase 4)
```

## Next session opener

1. Open new Claude chat with project files attached.
2. Paste content of `prompts/master-handover-prompt.md`.
3. STATE.md loads automatically as project knowledge.
4. First instruction in the new chat: "продолжаем" or specify next deliverable.
5. Forge picks up from the row marked **NEXT** in Day-by-day execution status above.

## Session log

Append-only. Newest first.

### 2026-05-16 - Day 2: research integration + documentation sync

**Done:**
- Audited repo for documentation inconsistencies. Found 9 stale references where Phase 1 status, ADR count, and file references no longer matched repo reality.
- Ran PR #1: replaced HANDOVER.md and handover-day2-v2.md with STATE.md as canonical state. Rewrote master-handover-prompt.md to be lean. Archived prompt-template-build.md (Phase 1 complete, no longer relevant). Fixed file references in prompt-akamai-hvo.md. Updated README.md ADR table. Updated 02-akamai/00-context.md research checklist. Updated 02-akamai/01-leave-behind-memo.md skeleton to match ADR-009 bundle structure.
- Created ADR-010 (session continuity via STATE.md).
- Ran PR #2: integrated 60+ pages of Akamai research into `02-akamai/research/outputs/`. Six company-level files + one partner program DACH dossier. Updated akamai-research.md to serve as synthesis pointer.

**Next session:**
- D2-2: Akamai diagnosis scorecard. Apply maturity model from `01-method/maturity-model/` to Akamai using the new research base. Output: filled scorecard, top 3 gaps with revenue impact, spider chart input data (current state coordinates).
- Then D3-1 (ABM/TAS) using the 50-partner dossier as input.

**Blockers:** none.

**Notes:**
- Two PRs intentionally separated: PR #1 documentation cleanup, PR #2 research content integration. Clean history.
- The partner program dossier identifies clear displacement targets (KAEMI, Navixia, Computacenter) and anchor partners (Deutsche Telekom Security, Bechtle, Controlware, InfoGuard). These feed directly into D2-2 diagnosis (where Akamai is weak in DACH partner depth) and D3-1 (ABM/TAS scoring).
