# Project State

> **Always current. Single source of truth for project status.**
> Replaces the previous HANDOVER.md and handover-day2-v2.md.
> Discipline defined in ADR-010 (session continuity).

**Last updated:** 2026-05-18
**Session:** Day 3 - Post-cleanup: ABSM relocated, STATE.md synced to repo reality
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
| Layer 2: Playbook Engine (Akamai specialization) | IN PROGRESS | Research done, scorecard v1.3 done, D3-1 done, ABSM sprint done. Memo + exec summary need rewrite |
| Layer 3: HVO Wrapper (Akamai bundle) | DRAFT | Memo + exec summary exist (v1, need rewrite). Spider chart not started |

## Day-by-day execution status

| Block | Deliverable | Status |
|---|---|---|
| D1-1 to D1-8 | Method universal template (overview + 7 stages + scorecard + maturity framework) | DONE |
| D2-1 | Akamai initial research (akamai-research.md) | DONE |
| D2-R | Deep research prompts v2 (company + partner program) | DONE |
| D2-RA | Akamai company deep research (6 files, ~30pp, 60+ pages combined) | DONE |
| D2-RB | Akamai partner program DACH dossier (50 named partners, 7 sections) | DONE |
| D2-2 | Akamai diagnosis scorecard at `02-akamai/03-diagnosis-scorecard.md` | DONE v1.3 |
| D2-RC | Entanglement & Recruitability research (4-file dossier at `02-akamai/research/outputs/entanglement/`) | DONE |
| D2-2.5 | IPP refactor: 6-dimension scoring applied (in 01-recruit.md); Recruitability scores in scorecard Gap 2 + entanglement/ outputs | DONE |
| D3-1 | ABM/TAS DACH Partner Project — Pursue priority five profiles at `02-akamai/research/outputs/d3-1/` | DONE (profiles only; full scoring matrix + 9-box TODO) |
| D3-2 | ABSM DACH Sprint (44 artifacts) at `02-akamai/03-dach-projects/absm-sprint/` | DONE |
| D2-3 | HVO main memo at `02-akamai/01-leave-behind-memo.md` | DRAFT v1 — needs rewrite (Gap 3 structure, per STATE-patch notes) |
| D2-3a | Exec summary at `02-akamai/00-page-zero-executive-summary.md` | DRAFT v1 — needs rewrite (aligned with memo rewrite) |
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

- `02-akamai/research/prompts/` - 3 research mission prompts (company v2, partner-program v2, entanglement v1)
- `02-akamai/research/outputs/company/` - 6 files, ~30 pages: corporate fundamentals, DACH regional intelligence, cultural and operational intelligence, channel marketing organization, risks and questions, master summary
- `02-akamai/research/outputs/partner-program/akamai-partner-program-dach-dossier.md` - 7-section dossier, 50 named DACH partners
- `02-akamai/research/outputs/entanglement/` - 4 files, D2-RC: 33-partner entanglement matrix, 12 deep profiles, Recruitability scoring framework, recommended dispositions + 90-day execution plan
- `02-akamai/akamai-research.md` - initial research synthesis (now serves as pointer/index to deep research)

## Key targets from partner research (post-D2-RC dispositions)

For ABM/TAS work — Pursue (priority five, full plan in `02-akamai/research/outputs/entanglement/04-recommended-dispositions.md`):
- **Axians/Fernao** (DE, Mannheim) - Recruitability 4. ISG Leader 2025 x 4 cyber categories, multi-vendor, NIS2/KRITIS aligned
- **AVANTEC** (CH, Zürich) - Recruitability 4. Zscaler + Netskope flagship with displaceable Illumio side-bet
- **SVA** (DE, Wiesbaden) - Recruitability 3. Federal Business POY (PANW 2025), Mittelstand
- **ACP Gruppe** (AT, Vienna) - Recruitability 3. Multi-vendor AT systemhaus, no flagship lock
- **InfoGuard** (CH, Baar) - Recruitability 3. Already public Akamai partner, deepen to Premier

For Contain (residual product gaps only, no flagship MDF):
- Computacenter (Cisco/PANW/Zscaler triple-anchor; Guardicore east-west + API Security niche)
- Bechtle AG / Bechtle Schweiz (PANW Diamond + Cisco POY)
- Cancom (Cisco SMB POY + PANW Diamond + Zscaler Platinum)
- Controlware (Cisco DE 2024 Networking POY + PANW DE 2025 VAR POY; NIS2 narrative co-author)
- NTT Data Germany (PANW DE 2025 GSI POY)
- Navixia (Illumio embedded; non-segmentation portfolio play in Romandie)
- Deutsche Telekom Security: split disposition — Pursue for Guardicore (additive), Contain for SASE/ZTNA (PANW/Zscaler locked)

For distributor mindshare lift (Pursue):
- Infinigate (contested mindshare: Akamai + Illumio + Cloudflare exclusive MSSP DACH)
- Arrow ECS Switzerland (Akamai Guardicore distributor since 2017 + only Illumio CH distributor)

For Drop (remove from TAL):
- KAEMI (Illumio Radiate + Cloudflare ASDP double-lock)
- Open Systems (competitor by nature — own SASE platform)
- genua (sovereign vendor, not a channel)
- Exclusive Networks DE (PANW 16+ year exclusive)
- Westcon-Comstor (Zscaler + PANW distribution lock)

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
| ADR-011 | Recruitability as 6th IPP dimension + disposition taxonomy (Pursue/Contain/Monitor/Drop) |

## Repo structure (current)

```
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
```

## Next session opener

Project knowledge in Claude.ai is a snapshot, not GitHub-synchronized. The new chat does NOT see live STATE.md or recent ADRs. Workflow requires manual paste from VPS.

Procedure for opening a new chat:

1. On VPS: `cat ~/partner-program-os/prompts/master-handover-prompt.md`. Copy output.
2. Open new Claude chat inside the Partner Program OS project (project knowledge has the three partnership books + RJSM books that Forge needs as background).
3. Paste the master handover prompt content as the first message.
4. On VPS: `cat ~/partner-program-os/STATE.md`. Copy output. Append to the same message (or send as second message), prefixed with `---\n## Current STATE.md (authoritative, from repo)`.
5. End the message with `продолжаем` (or specific instruction like `Start D3-1`). Forge picks up from the NEXT row.
6. If specific files are needed during the session (research outputs, stage docs, scorecards), `cat` them on VPS and paste on demand.
7. At session end: ask Forge to produce a PR script that updates STATE.md with a new session log entry (per ADR-010).

For parallel research missions (D2-RC and any future research), open a separate chat using the same procedure, but additionally paste the relevant `02-akamai/research/prompts/research-prompt-*.md` content and instruct Forge to execute the mission.

The full operator-instructions section lives at the top of `prompts/master-handover-prompt.md` for reference.

## Session log

Append-only. Newest first.

### 2026-05-18 - Day 3: Cleanup — ABSM relocated, STATE.md synced, scorecard consolidated

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

### 2026-05-18 - Day 2.7: D2-RC integrated, dach-projects relocated, ADR-011 amended

**Done:**
- D2-RC research mission (entanglement & Recruitability) completed in parallel chat per `research-prompt-akamai-entanglement-v1.md`. 4 output files committed to `02-akamai/research/outputs/entanglement/`: 33-partner entanglement matrix, 12 deep profiles, 6-sub-criterion Recruitability scoring framework, recommended dispositions plus 90-day execution plan.
- Repo structure correction: `03-dach-projects/` relocated from root to `02-akamai/03-dach-projects/`. Architectural rationale: all Akamai-specialisation artifacts (HVO bundle, research, supporting DACH projects per ADR-009) belong under one folder. The original root-level scaffold was a leftover from initial bootstrap.
- ADR-011 amendment: retracted the claim that Computacenter is publicly an Illumio investor. D2-RC verified Illumio funding history (Series C-F) and found no Computacenter participation. The actual relationship is MSP service partnership plus co-exhibition with KAEMI at Illumio World Tour Germany 2025. The Contain disposition for Computacenter stands; the rationale shifts from "equity-locked" to "service-MSP-locked + triple-anchor systemhaus".
- ADR-009 amendment: path references `03-dach-projects/` updated to `02-akamai/03-dach-projects/` throughout, repo structure tree refreshed inside the ADR body.
- D2-2 scorecard refreshed (DRAFT v1 → DRAFT v1.1): Gap 2 dispositions populated from D2-RC. Pursue priority five (Axians/Fernao, AVANTEC, SVA, ACP, InfoGuard) plus Contain rationale for triple-anchor systemhauser. KAEMI moved from "top displacement target" to Drop disposition. Computacenter tier-upgrade play deprecated. "Post-D2-RC refresh required" section replaced with "D2-RC refresh complete" with cross-references to entanglement outputs.
- README.md, prompts/prompt-akamai-hvo.md, 02-akamai/00-context.md, 02-akamai/01-leave-behind-memo.md, and 02-akamai/research/outputs/README.md path references updated to the new dach-projects location.

**Next session:**
- Human review of D2-2 scorecard v1.1 (especially Gap 2 disposition table)
- D3-1: ABM/TAS DACH Partner Project execution against the Pursue list (5 priority + 4 disciplined + 2 distributor) with full per-partner one-page profiles and 9-box positioning. Inputs ready: `02-akamai/research/outputs/entanglement/04-recommended-dispositions.md` 90-day plan is the operational sequencing for this work.
- D3-2: ABSM DACH Sprint with Axians/Fernao or SVA as partner front for the showcase account
- D2-3: HVO main memo drafts after D2-2 review and at least one D3-1 partner profile is in place

**Blockers:** none. D2-2 review unblocks D2-3 drafting; D3-1 and D3-2 can run in parallel.

**Notes:**
- D2-2.5 is logically DONE: the 6-dimension IPP refactor lives in `01-method/01-recruit.md` (committed earlier) and the Recruitability scores for top DACH partners are in scorecard Gap 2 and in `02-akamai/research/outputs/entanglement/`. D3-1 will be the full portfolio application.
- The disposition discipline is the structural learning from D2-RC: 11 of 33 partners are recruitable (Pursue), 10 are Contain (work residual gaps without flagship investment), 8 are Monitor (tripwire-conditional), 5 are Drop. The Pursue-first allocation of channel marketing budget is the immediate action item.

### 2026-05-18 - Day 2.6: scorecard v1 committed, handover discipline patched

**Done:**
- Committed D2-2 Akamai diagnosis scorecard v1 to repo at `02-akamai/03-diagnosis-scorecard.md`. Outside-in scoring across 7 stages (Recruit/Onboard/Enable/Co-sell = Basic; Deliver/Renew = Professional [inferred]; Expand = Basic). Spider chart input data table (current vs world-class vs 90-day realistic). Top 3 gaps with revenue impact (caveated as order-of-magnitude estimates). 5 interview-grade questions for hiring manager. Sections requiring post-D2-RC refresh explicitly marked.
- Patched `prompts/master-handover-prompt.md`: added OPERATOR INSTRUCTIONS section explaining manual paste workflow for opening new chats (project knowledge is a snapshot, not GitHub-synchronized). Adjusted the in-prompt FORGE PROMPT to acknowledge STATE.md will arrive via paste, not project knowledge.
- Patched STATE.md Next session opener section with the same Variant B procedure.

**Next session:**
- D2-RC research mission: execute in dedicated parallel chat using the procedure documented in master-handover-prompt.md OPERATOR INSTRUCTIONS
- D2-2 scorecard review: human read of the committed v1; refinements as needed; sections marked for D2-RC refresh updated when research returns
- D2-3 HVO main memo: drafts after scorecard review converges

**Blockers:** none. Both D2-RC (parallel chat) and D2-2 review (this chat or future main chat) are unblocked.

**Notes:**
- The scorecard is committed as v1-DRAFT, not as final. Gap 2 partner dispositions and Recruitability scoring populate after D2-RC.
- Revenue numbers in the scorecard carry explicit caveat sections. Treat them as directional, not committed. During interview, the candidate asks the hiring manager for internal targets and re-anchors estimates on real data.
- The manual paste workflow is now the supported procedure for handover discipline (ADR-010). Project knowledge limitation documented in master-handover-prompt.md.

### 2026-05-18 - Day 2.5: Recruitability dimension + entanglement research initiated

**Done:**
- Identified entanglement risks across DACH partner roster from D2-RA/D2-RB outputs: Computacenter co-invested in Illumio + simultaneously Akamai Select; KAEMI GmbH (Berlin) is Illumio EMEA Partner of the Year; Arrow ECS Switzerland holds both Akamai Guardicore and Illumio exclusive distribution; Infinigate carries triple exposure (Akamai + Illumio + Cloudflare MSSP exclusive)
- Created ADR-011: Recruitability as 6th IPP dimension; Pursue/Contain/Monitor/Drop disposition taxonomy; default disposition for sub-threshold partners is Contain, not Drop
- Refactored `01-method/01-recruit.md`: rebalanced 5 existing dimension weights, added Recruitability dimension with 6 sub-criteria and scoring rubric, added disposition taxonomy section, updated scoring matrix template to 6 dimensions
- Wrote `02-akamai/research/prompts/research-prompt-akamai-entanglement-v1.md` for D2-RC mission: 4 output files, 20-25 pages, 30-partner matrix + 12 deep profiles + Recruitability scoring framework + recommended dispositions

**Next session:**
- D2-2: complete Akamai diagnosis scorecard draft -> review -> commit to repo (draft already produced in chat, awaits Alex review)
- D2-RC: execute research mission in parallel chat using the new prompt; produces source data for Recruitability scoring
- D2-2.5: once D2-RC returns, populate Recruitability scores for top partners, refresh IPP for D3-1

**Blockers:** none. D2-RC runs in parallel chat, does not block D2-2 review.

**Notes:**
- D2-2 scorecard draft remains valid post-ADR-011. The maturity model checkpoint "Ideal Partner Profile exists with weighted scoring criteria across 5+ dimensions" is satisfied by the new 6-dimension IPP (>=5). Maturity model structure unchanged.
- Critical principle from ADR-011: default disposition is Contain, not Drop. Drop requires explicit justification, not just low Recruitability score. Contained partners produce revenue in narrow deal types without burning flagship investment.

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
