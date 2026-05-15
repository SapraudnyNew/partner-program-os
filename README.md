# Partner Program OS

**Owner:** Alex M.
**Mission:** Reverse Job Search Method (RJSM) deliverable — three artifacts built on a shared methodology.
**Status:** Active build. Phase 0 (foundation) complete. Phase 1 in progress.

---

## What is this repo

Three artifacts. One methodology underneath.

| # | Artifact | Purpose | Status |
|---|---|---|---|
| 1 | **HVO Universal Template** | Reusable 7-stage partner program framework. Source of truth for any partner-program HVO. | Skeleton ready |
| 2 | **Akamai HVO** | Leave-behind memo for warm referral path. Target: Senior Channel Marketing Manager, DACH, Zero Trust. | Context drafted |
| 3 | **BEGE Rollout Map** | Dual-version implementation plan for Boon Edam Partner Program. Public version = portfolio piece. Private version = real internal rollout. | Operations section drafted |

---

## How to navigate

```
partner-program-os/
├── 00-decisions/   → architectural decision records (ADRs). Read before changing structure.
├── 01-method/      → the HVO Universal Template (7-stage lifecycle)
├── 02-akamai/      → Akamai-specific application
├── 03-boon-edam/   → BEGE-specific application
├── prompts/        → starter prompts for new chats (handover machinery)
└── docs/           → GitHub Pages publishable subset (sanitized)
```

---

## Foundational decisions (read first)

| ADR | Decision |
|---|---|
| ADR-001 | Repo private, with selective public publishing via /docs on GitHub Pages |
| ADR-002 | All artifacts in English (rynok language) |
| ADR-003 | HVO structure = 7-stage partner lifecycle (Recruit → Onboard → Enable → Co-sell → Deliver → Renew → Expand) |
| ADR-004 | Three-reader model: CEO/Board + Head of Channel/CRO/CMO + dual-layer in same document |
| ADR-005 | Evidence in appendix, not inline. Main documents stay clean. |
| ADR-006 | Akamai HVO is a warm-referral leave-behind, NOT cold outreach. Bait-and-switch positioning: enter at Senior Manager level, signal value to skip-level. |
| ADR-007 | BEGE rollout map = two versions. Public (sanitized, portfolio-grade). Private (BEGE-specific, internal-grade). |

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

## Current sprint

- [x] Phase 0: Foundation — decisions, structure, handover prompt
- [ ] Phase 1: Universal Template — fill 7 lifecycle stages with content
- [ ] Phase 2: Akamai HVO — draft leave-behind memo + talking points
- [ ] Phase 3: BEGE Rollout Map — both versions, with timeline and gates
- [ ] Phase 4: GitHub Pages publish — sanitized subset to /docs

---

## How to continue work in a new chat

Use `prompts/master-handover-prompt.md`. Drop the entire content into a new Claude chat. The new chat will have full context.

For phase-specific work, use the specialized prompts in `prompts/`.
