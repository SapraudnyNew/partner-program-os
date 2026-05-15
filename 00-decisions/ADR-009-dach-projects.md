# ADR-009: DACH Projects as Day 2 Supporting Artifacts

**Date:** 2026-05-15
**Status:** Accepted
**Supersedes:** None. Extends ADR-008 without amending it.

## Decision

The Akamai HVO bundle (Layer 3) ships with two supporting artifacts produced specifically for the DACH market:

1. **ABM/TAS DACH Partner Project:** 30 partner candidates scored, 10 longlisted with full Ideal Partner Profile, 9-box prioritization, and one-page profile per partner.
2. **ABSM DACH Sprint:** full 32-artifact ABSM methodology executed for Germany Mittelstand Zero Trust, 3 target accounts deep + 1 publicly-named showcase account.

These projects are deliverables on equal footing with the HVO memo itself, not appendices.

## Context

ADR-008 froze the Day 2 sprint to produce: Akamai diagnosis scorecard, HVO warm referral memo, HVO direct approach version, spider chart, PDF export, revision pass. The structure assumed the HVO is the headline artifact and the diagnosis is the supporting evidence.

After Day 1 completion and a re-review on Day 2 morning, the structure was inverted. The HVO memo is a diagnostic memo. Diagnostic memos without proof of execution capability read like consulting pitches. Mark Shelepov, the warm referrer, is a Principal Lead Architect on a technical track. He vouches for judgment and execution at a generalized level. He cannot vouch for the specific DACH channel marketing competency the role requires. The HVO must close that gap on its own.

Three structural options were considered:

1. **HVO + diagnosis only (ADR-008 as written).** Cleanest, fastest. Risk: the hiring manager reads a 3.5-page memo and concludes the candidate has frameworks but no operating evidence at the DACH partner marketing level.
2. **HVO + diagnosis + proof metrics from Boon Edam.** ADR-008 decision 12 path. Risk: Boon Edam is industrial B2B equipment, not cybersecurity. The proof translates conceptually but not operationally. Boon Edam metrics establish that the candidate ran a partner program. They do not establish DACH cybersecurity channel marketing capability.
3. **HVO + diagnosis + two DACH-native execution projects.** The HVO becomes the doorway. The ABM/TAS partner project demonstrates how the candidate would build the German partner pipeline. The ABSM sprint demonstrates how the candidate would convert NIS2 regulatory pressure into partner-sourced revenue. Both are DACH-native, both are Zero Trust specific, both show operating depth that no metric from a different industry can match.

Option 3 wins on three grounds: it answers the question Shelepov cannot, it lets the hiring manager read execution work rather than infer execution capability, and it is replicable for any future target company (the projects become a portable skill demonstration, not an Akamai-specific one).

## Resolution

### Project 1: ABM/TAS DACH Partner Project

**Purpose:** Demonstrate the candidate would systematically build Akamai's DACH partner pipeline using Target Account Selection discipline applied to partner recruitment.

**Methodology source:** Stage 1 (Recruit) of the Partner Growth Method. ABM/TAS skill section.

**Scope:**
- Target market: DACH cybersecurity channel ecosystem
- Candidates pool: 30 partners identified through web search, partner directory mining, and competitor partner intelligence
- Longlist: 10 partners prioritized through Ideal Partner Profile scoring (five dimensions: strategic fit, capability, market access, financial health, cultural alignment)
- Output for each of 10: weighted score, 9-box quadrant, one-page profile covering business model, current Akamai-competitor relationships, geographic coverage, Zero Trust certifications held, and identified executive contacts

**Deliverable bundle:**
- `03-dach-projects/abm-tas-partners/00-context.md` (project intent and methodology applied)
- `03-dach-projects/abm-tas-partners/01-scoring-matrix.xlsx` (Excel matrix, 30 candidates, scored)
- `03-dach-projects/abm-tas-partners/02-target-account-list.md` (top 10 longlist with rationale)
- `03-dach-projects/abm-tas-partners/profiles/01-partner-name.pdf` through `10-partner-name.pdf` (10 one-page partner profiles)

### Project 2: ABSM DACH Sprint

**Purpose:** Demonstrate the candidate would convert NIS2 regulatory pressure into German Mittelstand Zero Trust pipeline through structured Account-Based Sales and Marketing executed jointly with channel partners.

**Methodology source:** Stage 4 (Co-sell) ABSM skill section. Full 6-stage pipeline: Context Architect, Target Account Selector, Deep Intel Profiler, Strategy Master, Execution Arsenal, Infrastructure and Launch.

**Scope:**
- Territory: Germany (Austria and Switzerland excluded for research depth concentration)
- Vertical: Mittelstand manufacturing (NIS2 essential and important entities)
- Akamai solution: Akamai Guardicore Segmentation (Zero Trust microsegmentation)
- Target band: EUR 100M to EUR 2B revenue, 1,000 to 10,000 employees
- Selection hard filter: accounts must sit below Akamai direct sales coverage threshold (no DAX 40, limited MDAX presence)
- Candidates pool: 30 Mittelstand candidates scored
- Final selection: 3 accounts for full ABSM treatment + 1 publicly-named Mittelstand showcase account
- Real company names used throughout artifacts

**Deliverable bundle:**
- `03-dach-projects/absm-sprint/00-context.md` (Stage 0: Context Architect output)
- `03-dach-projects/absm-sprint/01-targeting/` (Stage 1: ICP, target matrix CSV, top 3 selection rationale)
- `03-dach-projects/absm-sprint/02-intel/` (Stage 2: 12 deep intel files, 4 per account)
- `03-dach-projects/absm-sprint/03-strategy/` (Stage 3: pain patterns, Sweet Spot, content matrix)
- `03-dach-projects/absm-sprint/04-execution/` (Stage 4: 12 emails per account, business cases, MAPs, personalized landing pages)
- `03-dach-projects/absm-sprint/05-infrastructure/` (Stage 5: measurement system, executive dashboard, CRM integration spec, budget)
- `03-dach-projects/absm-sprint/showcase/` (showcase account, publicly named)

### Sequencing

Both projects build in parallel. Shared research base: German Mittelstand market, NIS2/DORA regulatory pressure, DACH cybersecurity channel landscape. Parallel build prevents duplication.

The constraint that ABSM targets sit below Akamai direct sales coverage threshold makes ABM/TAS partner research a prerequisite input: knowing which partners cover which mid-market accounts informs which accounts to target through which partners.

### Timeline

Day 2 (this sprint, May 15) executes:
- D2-2: Akamai diagnosis scorecard
- D2-3 prep: deep research prompts drafted and approved
- Research execution: two parallel research chats run

Days 3-5 execute:
- ABM/TAS DACH project (Days 3-4)
- ABSM DACH sprint (Days 4-5, overlapping)

Day 6-7 execute:
- HVO main memo draft
- 1-page executive summary
- Spider chart (three design options presented for approval before build)
- PDF assembly
- Web hosting setup for interactive artifacts
- Revision pass and rate

Total: 5-7 days end-to-end from May 15.

### HVO bundle structure

The Akamai bundle ships as:

1. **Page 0:** 1-page executive summary, skip-level readable, standalone (for VP Channel Marketing EMEA forwarding path)
2. **Pages 1-3.5:** main memo (method overview, Akamai diagnosis, top 3 gaps, 90-day plan, fit)
3. **Linked:** ABM/TAS DACH partner package (full bundle)
4. **Linked:** ABSM DACH sprint package (full bundle)
5. **Linked:** Interactive spider chart (web-hosted)

The memo is the entry point. The supporting projects are the proof. The executive summary lets the document travel up the org without requiring the reader to consume the full bundle.

### Boon Edam status

Boon Edam proof metrics remain in the repo (`03-boon-edam/`) and may surface in the HVO Section 4 (Why this fit) as a brief credibility anchor, but are not the primary proof layer for the Akamai HVO. The DACH-native projects carry the operating-evidence burden. This reverses ADR-008 decision 12, which placed Boon Edam metrics on Page 3.5 of the HVO.

### Repo structure update

New top-level folder:

```
03-dach-projects/
├── 00-context.md (project portfolio overview)
├── abm-tas-partners/
│   ├── 00-context.md
│   ├── 01-scoring-matrix.xlsx
│   ├── 02-target-account-list.md
│   └── profiles/
│       ├── 01-{partner}.pdf
│       └── ... (10 profiles)
└── absm-sprint/
    ├── 00-context.md
    ├── 01-targeting/
    ├── 02-intel/
    ├── 03-strategy/
    ├── 04-execution/
    ├── 05-infrastructure/
    └── showcase/
```

Akamai folder remains at `02-akamai/` and receives the HVO memo, executive summary, spider chart, and links to the DACH projects.

## Consequences

- Day 2 sprint extends from 1 day to 5-7 days end-to-end. Acceptable trade because the resulting HVO operates at consulting-grade evidence depth.
- The two DACH projects are reusable. The methodology applies to any future target company; the German Mittelstand context can be re-specialized to any geography and vertical.
- Real company names in the ABSM artifacts create a paper trail. The artifacts must be handled as professionally as any commercial deliverable; any errors or unsubstantiated claims about named companies damage Alex's credibility.
- The HVO is no longer a leave-behind memo in the traditional sense. It is a leave-behind bundle. The referrer (Mark Shelepov) must understand he is forwarding a portfolio, not a memo.
- Web hosting decision deferred to D2-5 (spider chart build). Options: GitHub Pages, Cloudflare Pages, Vercel free tier.
- Spider chart design checkpoint: three options presented for approval before build, per Q13 lock.
