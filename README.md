# Partner Program OS

**Owner:** Alex M.
**Mission:** Reverse Job Search Method (RJSM) deliverable — three artifacts built on a shared methodology.
**Status:** Active build. Layer 1 (Method) complete. Layer 2 (Akamai specialization) in progress. See `STATE.md` for current execution status.

---

## What is this repo

Three artifacts. One methodology underneath. Plus DACH supporting projects per ADR-009.

| # | Artifact | Purpose | Status |
|---|---|---|---|
| 1 | **Universal Partner Method** | Reusable 7-stage partner program framework. Source of truth for any partner-program HVO. | COMPLETE |
| 2 | **Akamai HVO Bundle** | Leave-behind bundle for warm referral path. Target: Senior Channel Marketing Manager, DACH, Zero Trust. | IN PROGRESS |
| 3 | **DACH Projects** | ABM/TAS partner project + ABSM Mittelstand sprint. Supporting artifacts for Akamai HVO per ADR-009. | NOT STARTED |
| 4 | **BEGE Rollout Map** | Dual-version implementation plan for Boon Edam. Public version = portfolio piece. | SCAFFOLDED |

Detailed status in `STATE.md`.

---

## How to navigate

```
partner-program-os/
├── STATE.md                  → CURRENT STATE. Read first.
├── 00-decisions/             → Architectural decision records. Read before changing structure.
├── 01-method/                → The Universal Partner Method (7-stage lifecycle, Layer 1)
├── 02-akamai/                → Akamai-specific application (Layer 2 + Layer 3)
│   └── research/             → Akamai deep research (60+ pages)
├── 03-boon-edam/             → BEGE-specific application (frozen per ADR-008)
├── 03-dach-projects/         → ABM/TAS + ABSM supporting artifacts per ADR-009
├── prompts/                  → Starter prompts for new chats
└── docs/                     → GitHub Pages publishable subset (sanitized)
```

---

## Foundational decisions

| ADR | Decision |
|---|---|
| ADR-001 | Repo private, with selective public publishing via /docs on GitHub Pages |
| ADR-002 | All artifacts in English (market language) |
| ADR-003 | HVO structure = 7-stage partner lifecycle (Recruit → Onboard → Enable → Co-sell → Deliver → Renew → Expand) |
| ADR-004 | Three-reader model: CEO/Board + Head of Channel/CRO/CMO + dual-layer in same document |
| ADR-005 | Evidence in appendix, not inline. Main documents stay clean. [P-NN] and [E-NN] bracket refs |
| ADR-006 | Akamai HVO is a warm-referral leave-behind, NOT cold outreach. Bait-and-switch positioning |
| ADR-007 | BEGE rollout map = two versions. Public sanitized portfolio + private internal |
| ADR-008 | Three-layer architecture (Method + Playbook Engine + HVO Wrapper). FROZEN |
| ADR-009 | DACH projects (ABM/TAS + ABSM) as supporting artifacts for Akamai HVO bundle |
| ADR-010 | Session continuity via STATE.md (replaces HANDOVER.md and handover-day2-v2.md) |

Full reasoning: see `00-decisions/`.

---

## Source methodology

Built on synthesis of eight books (see `01-method/appendix/evidence-library.md`). Primary sources:

1. **Bob Moore — Ecosystem-Led Growth** (Crossbeam). Central framework.
2. **David Yovanno — The Partnership Economy** (impact.com). Third channel logic.
3. **Atluri/Dietz — The Ecosystem Economy** (McKinsey). Strategic frame: orchestrator vs participant.
4. **Bamford/Gomes-Casseres — Mastering Alliance Strategy**. Governance and capability layer.
5. **Moore/Thomas — Marketing Multiplied**. Channel marketing 4-pillars (TO/WITH/THROUGH/FOR).

Secondary: Progressive Partnerships (Laing), Strategy Rules (Yoffie), Business Partnership Essentials.

---

## How to continue work in a new chat

Use `prompts/master-handover-prompt.md`. Drop the entire content into a new Claude chat. The new chat reads STATE.md and picks up from the NEXT row in the day-by-day execution table.

For phase-specific work, use the specialized prompts:
- `prompts/prompt-akamai-hvo.md` for HVO drafting
- `prompts/prompt-bege-rollout.md` for BEGE rollout map

Archived prompts (no longer needed because their phase is complete) live in `prompts/_archive/`.
