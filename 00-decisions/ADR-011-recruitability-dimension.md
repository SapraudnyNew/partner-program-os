# ADR-011: Recruitability as Sixth IPP Dimension; Disposition Taxonomy for Entangled Partners

**Date:** 2026-05-18
**Status:** Accepted

## Decision

The Ideal Partner Profile (IPP) defined in `01-method/01-recruit.md` gains a sixth dimension: **Recruitability**. Weight: 10-15%. The dimension scores how realistically a partner can be moved into an active commercial relationship with the company given the partner's existing public commitments to competitors.

Recruitability is composed of six sub-criteria, each scored 1-5:
1. Distribution exclusivity locks with competitors (weight: 25% within dimension)
2. Equity, board, or executive overlap with competitors when publicly verifiable (20%)
3. Joint Partner-of-Year or flagship designation with competitor in last 24 months (15%)
4. Executive migration trajectory between vendor and partner (15%)
5. Joint case study density with competitor in last 24 months (15%)
6. Public statements of vendor strategy or stack preference (10%)

Existing dimension weights are rebalanced to make room:

| Dimension | Old weight | New weight |
|---|---|---|
| Strategic fit | 25-35% | 20-30% |
| Capability | 20-30% | 15-25% |
| Market access | 20-25% | 15-20% |
| Recruitability (new) | — | 10-15% |
| Financial health | 10-15% | 10-15% |
| Cultural alignment | 5-10% | 5-10% |

A new disposition taxonomy operationalizes Recruitability scores at the portfolio level. The taxonomy replaces the implicit assumption that every IPP-qualified partner is a pursue target.

| Disposition | When applied | Investment posture |
|---|---|---|
| Pursue | Recruitability score ≥3.5. Standard active recruitment per 9-box quadrant. | Standard MDF, executive sponsorship, named relationship owner |
| Contain | Recruitability score 2.0–3.4. Partner remains in scope but limited to deal types where structural overlap with competitor is minimal (geographic gap, product gap, vertical gap). | No flagship MDF investment. Reactive deal support. Tripwire conditions monitored quarterly. |
| Monitor | Recruitability score below 2.0 BUT a defined tripwire event would change disposition (founder departure, contract expiry, M&A). | No active investment. Quarterly tripwire review. |
| Drop | Recruitability score below 2.0 AND no plausible tripwire event in 24-month horizon. | Remove from TAL. Reallocate budget. |

Default disposition for partners scoring below 3.5 on Recruitability is **Contain**, not Drop. Drop requires explicit justification.

## Context

Partner research executed in D2-RA and D2-RB surfaced multiple structural entanglements between target DACH partners and Akamai's competitors:

- KAEMI GmbH (Berlin) is Illumio EMEA Partner of the Year. Headquartered inside Akamai's home territory.
- Computacenter is publicly listed as Akamai Select Partner AND co-exhibits with Illumio at IWT 2025 Germany AND is investor in Illumio. Triple-bind.
- Arrow ECS Switzerland holds Akamai Guardicore distribution (since June 2017) AND Illumio's exclusive Swiss distribution. Structural conflict.
- Infinigate distributes Akamai, Illumio, AND (since September 2025) exclusively distributes Cloudflare MSSP in Germany. Triple exposure.
- Navixia SA is first EMEA partner to reach Illumio ZTS Professional. Romandie's natural Akamai partner candidate.

The existing 5-dimension IPP cannot distinguish a "high-fit partner who can be moved" from a "high-fit partner who is structurally locked elsewhere." Both score equally well on Strategic Fit, Capability, and Market Access. The 9-box treats them identically.

Pursuing both produces predictable failure: the structurally-locked partner consumes recruitment cycles and produces no movement. Worse, the manager who chases such partners gets labeled as someone who does not do their homework.

Three options were considered:

1. **Keep 5-dimension IPP, add an exclusion list.** Maintain partners with known entanglements in a separate "do not recruit" list. Risk: opaque, brittle, hard to maintain, treats Pursue/Drop as the only options.
2. **Add Recruitability as binary qualifier.** Partner passes Recruitability or fails. Simpler but loses the gradient: Computacenter is not the same as KAEMI but binary treats them identically.
3. **Add Recruitability as scored dimension (6th) AND introduce disposition taxonomy.** Quantifies the entanglement signal. Permits nuanced portfolio decisions: Pursue / Contain / Monitor / Drop. Default to Contain captures the value in continued relationship without burning flagship investment.

Option 3 wins. It preserves the systematic nature of the IPP while introducing portfolio-level flexibility that reflects how seasoned channel leaders actually manage entangled partners.

## Resolution

### Change to 01-method/01-recruit.md

The section "ABM/TAS skill: Ideal Partner Profile" gains a sixth dimension after "5. Cultural alignment" and before "ABM/TAS skill: scoring matrix":

**6. Recruitability** (weight: 10-15%)

Detailed criteria, scoring rubric, and disposition taxonomy live in the recruit.md file. Maturity model checkpoints in `01-method/maturity-model/scorecard-template.md` are NOT changed by this ADR. The checkpoint "Ideal Partner Profile exists with weighted scoring criteria across 5+ dimensions" remains satisfied because the IPP now has 6 dimensions (>=5).

### Research dependency

The Recruitability dimension is only as good as the research that populates it. The research mission documented at `02-akamai/research/prompts/research-prompt-akamai-entanglement-v1.md` (D2-RC) produces the source data for scoring DACH partner candidates on this dimension. Without that research, Recruitability scores are guesses.

### Sequencing impact on STATE.md

A new block D2-RC is inserted between D2-2 (diagnosis scorecard) and D3-1 (ABM/TAS DACH Partner Project) in the day-by-day execution table. A small block D2-2.5 captures the IPP refactor itself once research returns. D3-1 now uses the 6-dimension IPP, not the 5-dimension version.

## Consequences

- ABM/TAS scoring produces longlists with explicit dispositions, not just rank order. The hiring manager sees not "top 10 partners to chase" but "10 partners with 10 differentiated commercial postures."
- The HVO main memo (D2-3) can reference disposition diversity as evidence of judgment, not just diligence. Pursuing all 10 partners with equal intensity would signal a marketer who does not understand portfolio capital allocation.
- Recruitability research adds 3-5 working days to the Day 2 timeline. The trade is structurally sound: 5 days of research saves quarters of wasted recruitment cycles.
- Future ABM/TAS work for any target company benefits from the same 6-dimension IPP without per-company customization. The method becomes portable.
- Maturity model and scorecard template remain unchanged. This ADR refines the contents of an existing checkpoint, not the checkpoint structure.
- The disposition taxonomy creates new artifacts downstream: D3-1 output includes per-partner disposition and tripwire conditions, not just scoring.

## Refs

- ADR-008 (architecture frozen)
- ADR-009 (DACH projects)
- `02-akamai/research/outputs/partner-program/akamai-partner-program-dach-dossier.md` (entanglement signals surfaced)
- `01-method/01-recruit.md` (IPP definition, modified by this ADR)
