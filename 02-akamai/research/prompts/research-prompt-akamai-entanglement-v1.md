# Deep Research Mission: Akamai DACH Partner Entanglement and Recruitability Dossier

## Mission identity

You are an executive research analyst preparing a confidential channel intelligence dossier focused on a single question: which DACH cybersecurity partners are structurally available to deepen with Akamai, and which are entangled with Akamai's competitors to the point that recruitment investment would be wasted?

The output feeds the Recruitability dimension of the Ideal Partner Profile (per ADR-011) and the disposition decisions in the ABM/TAS DACH Partner Project (D3-1). Each partner gets a disposition: Pursue, Contain, Monitor, or Drop.

This is OSINT entanglement-mapping. The output is a working document, not a presentation.

## Available tools

Two Exa tools, used aggressively and in priority order:

1. **`web_search_exa`** - real-time neural search. Use for discovery of overlap signals, partner statements, executive movements, exclusive distribution agreements, and event co-sponsorships. Neural search rewards descriptive queries. Write queries the way you would brief a junior analyst.

2. **`web_fetch_exa`** - full content extraction from URLs surfaced by search. Use after every productive search hit. Snippets do not surface tier designations, partnership terms, exclusivity language, or board composition.

Expect 100-180 tool calls. The 30-partner entanglement matrix alone will require 60-100 searches across 4 vendors and multiple data layers per partner.

## Hard requirements

Non-negotiable:

- **Minimum output length: 20-25 pages across 4 files.** Less than 20 pages means the mission is incomplete.
- **Minimum 30 partners in the entanglement matrix.** Source list: anchor with the 50 partners named in `02-akamai/research/outputs/partner-program/akamai-partner-program-dach-dossier.md`, prioritize the 20 detailed profiles, supplement with any newly surfaced DACH partners.
- **Minimum 12 partners with deep entanglement profiles.** Subset of high-priority targets: 5 anchor partners + 4 top displacement candidates + 3 top recruitment candidates.
- **Minimum 60 cited sources across the dossier.** Each citation: full URL, date accessed.
- **Refuse-to-summarize protocol:** if at any point tempted to write "for the sake of brevity" or "in summary" or "due to length constraints" - stop. Continue researching.
- **Sectioned output: produce 4 separate markdown files.** Do not concatenate. Each file standalone with its own sources list.
- **Every entanglement claim cross-referenced against minimum 2 independent sources** OR marked single-sourced (⚠️) OR marked inferred (🧠) OR marked blind spot (❌).
- **Distinguish four data quality tiers throughout:**
  - **Confirmed:** 2+ independent reputable sources
  - **Single-sourced:** ⚠️ one source only
  - **Inferred:** 🧠 logical extension from data
  - **Blind spot:** ❌ cannot verify externally

## What we are looking for

Four entanglement signal layers. Search for all four per target partner.

### Layer 1: Distribution exclusivity locks

Contractual relationships that lock a partner into a competitor's go-to-market. Examples already known:
- Arrow ECS Switzerland holds both Akamai Guardicore distribution AND Illumio exclusive Swiss distribution (since 2017 and June 2017 respectively)
- Infinigate Germany holds Akamai distribution, Illumio distribution, AND exclusive Cloudflare MSSP distribution (since 25 September 2025)
- Exclusive Networks distributes Akamai in some EMEA geographies

Verify and expand. Look for:
- Exclusivity language in press releases announcing distribution partnerships
- Country-by-country distribution rights mapping (DACH split by DE / AT / CH)
- Multi-year distribution agreements with announced end dates
- Distributor revenue concentration (where partner website prioritizes one vendor in security category)

### Layer 2: Equity, board, or executive overlap with competitors (PUBLIC ONLY)

Verify only when surfaced via public sources. Examples already known:
- Computacenter is publicly listed as Illumio investor (verify exact relationship)
- Pavel Gurvich (Guardicore co-founder, ex-Akamai SVP) founded Tenzai with $75M funding November 2024

Sources to check:
- Northdata.com (German Handelsregister, board composition, shareholders)
- Bundesanzeiger (German official gazette for filings)
- Crunchbase company pages (investor lists, funding rounds)
- LinkedIn company pages (board members visible if listed)
- PitchBook references in press
- Partner annual reports (if publicly listed)

Do NOT speculate. If the link is not in a public document, mark as blind spot (❌).

### Layer 3: Joint Partner-of-Year or flagship designations (LAST 24 MONTHS)

Public flagship designations binding a partner to a specific vendor. Examples already known:
- KAEMI GmbH - Illumio EMEA Partner of the Year (year unspecified, verify)
- Navixia SA - first EMEA partner to reach Illumio ZTS Professional, third globally
- Computacenter - Cisco Partner of the Year Germany 2024 (multiple categories)

Sources:
- Vendor partner news / partner awards pages (Akamai, Illumio, Palo Alto, Zscaler, Cisco, Cloudflare, Fortinet)
- Channel press: channelpartner.de, channelfutures.com, channelbuzz.ca, channele2e.com, channeldive.com, channelnewsasia, ARN
- Partner own press releases announcing awards
- Conference attendee / sponsor pages (it-sa, IWT 2025, RSA, Black Hat Europe)

For each designation surfaced: year, exact title, vendor, partner. If vendor stops awarding the designation after 2024, note as a tripwire signal.

### Layer 4: Executive migration trajectory

Movement of senior people between vendor, competitor, and partner. Examples already known:
- Nadine Anders (Head of Channel Sales DACH Akamai, 6 years) departed February 2025 to Kong Inc.
- Pavel Gurvich (Guardicore co-founder, SVP GM Enterprise Security Akamai) departed November 2024 to start Tenzai
- Mark Shelepov (Principal Lead Architect Akamai US) - the referral path for this engagement

Sources:
- LinkedIn profile movements (search via Exa for specific company pages)
- Press releases announcing leadership hires
- Channel press coverage of executive moves
- Partner websites leadership pages

For each migration: from-company, to-company, date if known, role, public statements upon departure / arrival if any.

## Output structure

Four files in sequence.

---

## File 1: 01-entanglement-matrix.md (target: 5-7 pages)

A 30-partner matrix mapping entanglement signals.

### Section 1.1: Methodology

Brief paragraph: how partners were selected, what each signal column means, how scoring is performed, what confidence markers apply.

### Section 1.2: The matrix

A wide table. One row per partner. 30 rows minimum. Columns:

| # | Partner | HQ | Akamai relationship | Competitor primary | Distribution lock (L1) | Equity/board (L2) | POY designation (L3) | Exec migration (L4) | Recruitability score (1-5) | Disposition (P/C/M/D) | Confidence |

For each row:
- Partner: legal name
- HQ: city, country
- Akamai relationship: current Akamai tier or "not in program"
- Competitor primary: which competitor (Illumio, Palo Alto, Zscaler, Cisco, Cloudflare, Fortinet, Microsoft, Check Point, multiple, none)
- L1 distribution lock: brief description with year, mark ⚠️/🧠/❌ as needed
- L2 equity/board: brief description, mark accordingly
- L3 POY: year and vendor, mark accordingly
- L4 exec migration: name + direction (e.g., "co-founder → competitor 2024"), mark accordingly
- Recruitability score: 1-5 weighted across 4 layers per ADR-011
- Disposition: P=Pursue, C=Contain, M=Monitor, D=Drop
- Confidence: High / Medium / Low

### Section 1.3: Aggregate statistics

- Count of partners by disposition
- Count of partners by primary competitor
- Count of partners with each entanglement layer flagged
- 5 most-locked partners (highest entanglement signal count)
- 5 most-recruitable partners (lowest entanglement signal count)

### Section 1.4: Confidence assessment

Per-column confidence. Where matrix has thin data, identify blind spots.

### Section 1.5: Sources

Full URL list, deduplicated.

---

## File 2: 02-deep-profiles.md (target: 10-12 pages)

12-15 deep entanglement profiles. Each profile 0.7-1 page.

### Profile structure (apply to each partner)

**Profile N: [Legal Partner Name]**

- HQ, country, employee count if known, revenue if known
- Akamai relationship details: tier, products carried, certified head count if known, joint case studies, joint events
- Layer 1 entanglements: every distribution lock with source URL + year + exclusivity language
- Layer 2 entanglements: every public equity/board overlap with source
- Layer 3 entanglements: every POY or flagship designation in last 24 months with source
- Layer 4 entanglements: every executive movement with source
- Vendor stack public statements: how the partner publicly describes their security portfolio (e.g., partner website "We work with Cisco, Illumio, and Akamai" → ranking signal)
- Tripwire conditions: events that would change disposition (founder departure, contract expiry, M&A target, leadership transition)
- Recruitability scoring with line-by-line rationale
- Disposition recommendation with explicit reasoning
- Sources for this profile

### Required subset

Profiles MUST include:
- All 5 Akamai DACH anchor partners (Deutsche Telekom Security, Bechtle, Controlware, InfoGuard, Computacenter)
- KAEMI GmbH, Navixia SA, Computacenter (in their displacement context separate from anchor profile if needed)
- Top 3-5 Mittelstand SI recruitment candidates (SVA, Cancom, Axians, ACP, Materna - profile whichever surfaces most data)

---

## File 3: 03-recruitability-scoring-framework.md (target: 3-4 pages)

Operationalize the 6th IPP dimension defined in ADR-011.

### Section 3.1: The 6-sub-criterion rubric

For each of 6 sub-criteria (per ADR-011), provide:
- What the sub-criterion measures
- Scoring rubric: what a 5 looks like, what a 3 looks like, what a 1 looks like
- Data sources: where to find evidence
- One real example from the entanglement matrix that illustrates each score level

### Section 3.2: Aggregation logic

How sub-criterion scores roll up to the Recruitability dimension score (1-5).

### Section 3.3: Disposition thresholds

Per ADR-011: Recruitability ≥3.5 = Pursue, 2.0-3.4 = Contain, below 2.0 with tripwire = Monitor, below 2.0 without tripwire = Drop.

For each threshold:
- Example partner from the matrix
- What investment posture means in practice (MDF, executive sponsorship, named relationship owner, deal types)

### Section 3.4: Calibration

How to recalibrate the Recruitability dimension as market signals change. Quarterly review cadence. Trigger events that force re-scoring across the portfolio.

---

## File 4: 04-recommended-dispositions.md (target: 3-4 pages)

The decision document. For the high-priority subset only (anchors + top displacement + top recruitment).

### Section 4.1: Pursue list

Partners scoring ≥3.5 on Recruitability. For each:
- Why pursue (one paragraph)
- First action in 30 days
- Investment level recommended

### Section 4.2: Contain list

Partners scoring 2.0-3.4. For each:
- Why contain rather than pursue (one paragraph)
- Permitted deal types (geographic gap, product gap, vertical gap)
- Excluded investment categories (no flagship MDF, no executive co-marketing, no joint case studies featuring competing technology)
- Tripwire conditions monitored quarterly

### Section 4.3: Monitor list

Partners scoring below 2.0 WITH defined tripwire event in 24-month horizon. For each:
- Specific tripwire (e.g., "Illumio contract scheduled to renew Q4 2026, monitor for non-renewal signals")
- Re-assessment cadence
- Trigger threshold for moving to Contain or Pursue

### Section 4.4: Drop list

Partners scoring below 2.0 WITHOUT plausible tripwire. For each:
- Reasoning (must be explicit and source-backed)
- Resource reallocation: which Contain or Pursue partner gains the budget?

### Section 4.5: 90-day disposition execution plan

- Week 1-2: dispositions presented to channel leadership for sign-off
- Week 3-4: Pursue list outreach plans built; Contain list deal-type playbooks built
- Month 2: first pursue contact made; first contain deal supported
- Month 3: tripwire monitoring infrastructure operational (named owner, quarterly review cadence)

---

## Tone of output

Analytical, source-cited, no marketing language. Treat this as a channel investment portfolio analysis written for the incoming Senior Channel Marketing Manager. Active voice. Specific facts and named entities throughout. No fluff. No diplomatic softening.

When the data is thin, say so. The Contain disposition is not a soft pass. It is a deliberate choice to preserve optionality while not burning investment capital.

## Final delivery instructions

When all 4 files are complete:

1. Verify total length across all files is minimum 20 pages (target 22-28).
2. Verify the entanglement matrix has minimum 30 partners.
3. Verify minimum 12 deep profiles.
4. Verify minimum 60 cited sources across the dossier.
5. Verify every Layer 1-4 claim has 2+ sources OR is flagged with ⚠️ / 🧠 / ❌.
6. Output all 4 files in sequence in the chat: File 1 first, then File 2, etc.

If context window is running out, prioritize completing whichever file is in progress fully before terminating. Do not produce truncated files. If context runs out mid-mission, output what is complete and list which files remain.

## Critical reminder

The user is using this research to make portfolio capital allocation decisions, not to build a thesis. The Recruitability dimension and disposition taxonomy will rebalance how 10-30 working days of channel investment is allocated across the DACH partner portfolio. Soft conclusions, hedged language, or unverified inferences cost real money downstream.

Default to skepticism. When evidence is ambiguous, mark accordingly. When the dossier from `02-akamai/research/outputs/partner-program/` already covers a partner, build on it rather than restating.

Begin with File 1, Section 1.1. Execute `web_search_exa` immediately on the 5 Akamai DACH anchor partners.
