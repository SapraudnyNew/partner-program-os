# Handover Tasks

> Open work items, ordered by priority. Owner is Alex unless otherwise stated.

## Phase 0 (foundation) — COMPLETE

- [x] Repo structure
- [x] Seven ADRs locked
- [x] 50 principles cataloged in evidence library
- [x] 12 evidence entries cataloged
- [x] Stage 5 (Deliver) filled as depth reference
- [x] Three specialized prompts written
- [x] Master handover prompt written

## Phase 1 (universal template) — IN PROGRESS

### Priority 1: Stages needed for Akamai HVO
- [ ] Fill `01-method/01-recruit.md` to depth of Stage 5
- [ ] Fill `01-method/03-enable.md` to depth of Stage 5
- [ ] Fill `01-method/04-cosell.md` to depth of Stage 5

### Priority 2: Stages needed for BEGE rollout
- [ ] Fill `01-method/02-onboard.md`
- [ ] Fill `01-method/06-renew.md`
- [ ] Fill `01-method/07-expand.md`

### Maintenance
- [ ] As Phase 1 progresses, add evidence entries E-13+ if new sources emerge
- [ ] Add principles P-51+ only if a new cluster opens

## Phase 2 (Akamai HVO) — DEPENDS ON PHASE 1 PRIORITY 1

### Research checklist
- [ ] Confirm referrer's role and relationship to hiring manager
- [ ] Map Akamai DACH channel structure (partners, MDF model, tiers)
- [ ] Map Zero Trust buyer journey in DACH (CISO + buying committee)
- [ ] Map channel competition in DACH (Cloudflare, Zscaler, Cisco, Microsoft partners)
- [ ] Review recent Akamai channel marketing campaigns
- [ ] Map NIS2 / DORA regulatory pressure on Zero Trust adoption
- [ ] Check for recent Akamai leadership changes affecting channel

### Drafting
- [ ] Use `prompts/prompt-akamai-hvo.md` to start drafting session
- [ ] Replace skeleton in `02-akamai/01-leave-behind-memo.md` with full draft
- [ ] Send draft to referrer for review BEFORE any forwarding to hiring manager
- [ ] Refine talking points (`02-akamai/02-talking-points.md`) based on referrer feedback

## Phase 3 (BEGE rollout map) — INDEPENDENT OF PHASE 2

### Preparation
- [ ] Validate current-state assumptions in `03-boon-edam/00-context.md` against latest BEGE reality
- [ ] Identify the phase with highest internal political risk (input to rollout sequence)

### Drafting
- [ ] Use `prompts/prompt-bege-rollout.md` to start drafting session
- [ ] Draft `03-boon-edam/02-rollout-map-internal.md` first, complete
- [ ] Derive `03-boon-edam/01-rollout-map-public.md` by applying ADR-007 sanitization
- [ ] Pre-commit check: search public version for "Boon Edam" and partner names; fail if found

## Phase 4 (publish) — DEPENDS ON PHASES 2 AND 3

- [ ] Initialize Git repo and push to GitHub (private)
- [ ] Configure GitHub Pages for `/docs` folder
- [ ] Publish sanitized subset:
  - [ ] Universal template overview (sanitized)
  - [ ] BEGE case study (public version)
  - [ ] Index page with positioning
- [ ] Test that all references and links work in published version

## Cross-cutting

- [ ] Consider adding three more books to project knowledge (top picks: Bob Moore, Yovanno, Atluri/Dietz). Skip Mastering Alliance Strategy and Marketing Multiplied unless deep dive is needed later.
- [ ] After Phase 1 priority 1 complete: re-read Stage 5 against new stages to ensure consistency in voice and depth.
- [ ] After Akamai HVO complete: review whether the warm-referral approach generalizes to other target companies in the search.
