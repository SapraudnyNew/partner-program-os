# Akamai Partner Program Maturity Scorecard

> **Status: DRAFT v1.2.** Initial scoring complete. Gap 2 dispositions populated from D2-RC research (2026-05-18, `02-akamai/research/outputs/entanglement/`). Revenue impact discussion restructured as directional framing, not committed estimates. Deliver/Renew scoring caveated per maturity framework methodology.
>
> **Scope:** Akamai DACH cybersecurity partner program, Q2 2026 snapshot.
> **Lens:** Outside-in, based on public sources only. No insider data.
> **Sources:** `02-akamai/research/outputs/company/` (6 files) + `02-akamai/research/outputs/partner-program/akamai-partner-program-dach-dossier.md`.
> **Method:** Applied `01-method/maturity-model/scorecard-template.md`.
> **Date:** 2026-05-18 (v1.2 patched 2026-05-19).

## Top-line

| Stage | Maturity score | Tag |
|---|---|---|
| 1. Recruit | **Basic** | Thin DACH roster + no systematic recruitment pipeline |
| 2. Onboard | **Basic** | Global infrastructure, no DACH operational layer |
| 3. Enable | **Basic** (global infrastructure at Professional; DACH execution at Basic) | Greenfield — no DACH channel marketing function |
| 4. Co-sell | **Basic** | Structural infrastructure, thin DACH execution |
| 5. Deliver | **Basic+ [INFERRED ceiling: Professional]** | GCSP-certified partners deliver lifecycle; no Professional checkpoint verified |
| 6. Renew | **Basic+ [INFERRED ceiling: Professional]** | Subscription model + channel ownership; no Professional checkpoint verified |
| 7. Expand | **Basic** | Portfolio breadth without DACH orchestration |

**Scoring note on Deliver and Renew:** the maturity framework (`00-maturity-framework.md`) requires ALL Professional-level checkpoints to be verified as present before a Professional score is awarded. For Stages 5 and 6, none of the Professional checkpoints (5.4–5.7, 6.4–6.7) could be verified from public sources — all are GATED behind internal data. The structural characteristics of Akamai's subscription model and GCSP-certified delivery suggest the *ceiling* is Professional, but the floor may be Basic. The Basic+ tag captures this uncertainty. During the interview process, verifying even one Professional checkpoint (e.g., tiered service levels operationalized, or renewal pipeline managed with 90/180/365-day cadence) would confirm the upgrade.

### Spider chart input data

Numeric conversion per maturity framework: Basic=1, Basic+=1.5 (interpolated for chart only), Professional=2, World-class=3.

| Stage | Current | World-class target | 90-day realistic |
|---|---|---|---|
| Recruit | 1 | 3 | 2 |
| Onboard | 1 | 3 | 1 |
| Enable | 1 | 3 | 2 |
| Co-sell | 1 | 3 | 2 |
| Deliver | 1.5 [inferred ceiling] | 3 | 2 |
| Renew | 1.5 [inferred ceiling] | 3 | 2 |
| Expand | 1 | 3 | 1 |
| **Total area** | **8 / 21 (38%)** | **21 / 21** | **12 / 21 (57%)** |

### Shape interpretation

Low and lopsided. The four front-half stages (Recruit through Co-sell) are uniformly Basic. Deliver and Renew carry structural advantages from Akamai's subscription model and GCSP-certified partner delivery, placing the ceiling at Professional — but without verified checkpoints, the confirmed floor is Basic. Expand sits low. The shape says: Akamai DACH has the economics of a subscription security business with strong renewal mechanics, but the front-half partner motion (acquire-onboard-enable-cosell) is materially underbuilt and the back-half maturity is assumed rather than demonstrated.

The 90-day realistic target of 12/21 closes Recruit, Enable, and Co-sell from Basic to Professional. Onboard and Expand stay Basic in 90 days because they require DACH onboarding playbook construction and portfolio orchestration infrastructure that take longer than a quarter to build. Deliver and Renew move to confirmed Professional (2.0) as internal data verification during onboarding converts the inferred ceiling into verified score.

---

## How to read the revenue impact estimates in the three gaps below

These are **directional framing, not committed projections.** Each rests on layers of assumption that compound:

1. **Market size assumptions** from outside-in sources (Mordor Intelligence, IDC, Grand View Research). Public TAM/SAM data, not Akamai's internal targets.
2. **Capture-rate assumptions** based on Akamai's public market position vs competitor share. Not verified against Akamai's internal share targets, which are gated.
3. **Velocity assumptions** based on "what does a multi-quarter gap in DACH channel marketing function cost in a market with NIS2 deadline pressure." This is the softest layer — no public benchmark exists for the specific velocity impact.

The qualitative argument (gap exists, it costs money, the scale is material) is the load-bearing claim. Specific dollar figures, where included, are illustrative of magnitude. They should not be taken as forecasts.

**The candidate's job during the hiring interview is to ask the hiring manager for actual internal targets, then re-anchor these estimates on real data.** That re-anchoring conversation is itself a demonstration of the analytical capability the role requires.

---

## Stage-by-stage detail

### Stage 1: Recruit — Basic

| # | Checkpoint | Present? | Evidence |
|---|---|---|---|
| 1.1 | Written partner description | Yes | Partner Connect program documentation, 3 tiers (Select/Premier/Elite), 8 partner types |
| 1.2 | Named recruitment owner | Global only | Pablo Onnias (global channel programs); no DACH-specific recruitment owner identified |
| 1.3 | Inbound inquiry process | Yes | partners.akamai.com, partner directory operational |
| 1.4 | IPP with weighted scoring (5+ dimensions) | No | No public evidence of DACH-specific IPP. Tier qualification is revenue-based, not capability+market+culture-weighted. Note: ADR-011 adds Recruitability as 6th dimension; even if Akamai had a 5-dim IPP, it would not pass the entanglement-aware standard |
| 1.5 | Partner pipeline in CRM/PRM | Inferred low | DACH partner roster anchored by 5 named partners (Deutsche Telekom Security, Bechtle, Controlware, InfoGuard, Computacenter). No Berlin-based security specialist in the program despite Berlin being a major German cybersecurity hub — and no evidence of a systematic pipeline to recruit one. This is not about any single locked partner being absent; it is about no visible recruitment pipeline targeting the gap |
| 1.6 | Scoring matrix → ranked TAL quarterly | No public evidence | |
| 1.7 | 9-box invest/maintain/exit | No public evidence | |
| 1.8-1.10 | World-class checkpoints | N/A | |

**KPIs (DACH-specific, where verifiable):**
- Pipeline conversion rate: GATED. Requires CRM/PRM access.
- Time-to-contract: GATED.
- Portfolio fit score: INFERRED LOW. Computacenter (Cisco's most-decorated DE partner, 3 awards 2024) sits at Akamai's lowest tier. Bechtle DE less visible than Bechtle CH. Suggests tier assignment is not driven by strategic-fit weighting.

**Why Basic:** missing IPP + missing 9-box + thin DACH roster + no visible systematic recruitment pipeline targeting strategic gaps. The structural signal is not that any specific partner is absent — it is that there is no evidence of a recruitment motion that would identify and close coverage gaps.

---

### Stage 2: Onboard — Basic

| # | Checkpoint | Present? | Evidence |
|---|---|---|---|
| 2.1 | Product training within 30 days | Yes | Akamai University, 3 training tracks, self-paced + live + labs |
| 2.2 | Portal access within 5 business days | Inferred yes | Partner portal exists, standard enterprise SaaS onboarding |
| 2.3 | Named contact at manufacturer | Global yes, DACH unclear | Without DACH channel marketing function, partners route through EMEA generic |
| 2.4 | Onboarding playbook with milestones/SLAs per type | No DACH-localized version surfaced | Modular agreements exist per partner type, no DACH playbook |
| 2.5 | Completion tracked, stalls flagged | GATED | |
| 2.6 | First-deal support process documented | GATED | |
| 2.7-2.9 | World-class checkpoints | N/A | |

**KPIs:** all GATED.

**Why Basic:** infrastructure (training, certs, portal) is global Professional-grade. DACH operational layer not visible. Without a DACH channel marketing function until this hire, new partner experience routes through EMEA generic flow. Partner Connect launched Q3 2025; onboarding velocity post-launch unknown.

---

### Stage 3: Enable — Basic (global infrastructure at Professional; DACH execution at Basic)

| # | Checkpoint | Present? | Evidence |
|---|---|---|---|
| 3.1 | Training content exists/accessible | Yes | Akamai University |
| 3.2 | Sales collateral shared | Yes | Partner portal |
| 3.3 | Pre-sales technical support | Yes | Solutions Architect track + Ask an Expert |
| 3.4 | Certification program with levels/renewal | Yes | GCSE, GCSP, APISP, AAP, recertification cadence GATED |
| 3.5 | Content library organized by sales-cycle stage, quarterly refresh | Yes globally, German-language refresh cadence unclear | |
| 3.6 | Enablement effectiveness measured | GATED for DACH | |
| 3.7 | Four marketing motions operational (TO/WITH/THROUGH/FOR) | **NO** | The structural signal. No DACH channel marketing function = motions 3 (THROUGH) and 4 (FOR) cannot exist. The role being hired is the evidence |
| 3.8-3.10 | World-class checkpoints | N/A | |

**KPIs:** GATED.

**Infrastructure vs execution gap:** Akamai has three of four Professional checkpoints present globally (3.4, 3.5, 3.6 partially). The missing Professional checkpoint (3.7: four marketing motions) is the DACH execution gap, not a global infrastructure gap. A new hire inherits Professional-grade global enablement tools and must operationalize the missing DACH marketing motions on top of that infrastructure. This is a more tractable starting position than "build everything from scratch."

**Why Basic:** checkpoint 3.7 (four marketing motions operational) is absent for DACH. Per scoring rules, all Professional checkpoints must be present for a Professional score. One missing checkpoint gates the entire stage at Basic. But the distinction between "nothing exists" and "three of four Professional checkpoints exist, one is missing" matters operationally.

---

### Stage 4: Co-sell — Basic

| # | Checkpoint | Present? | Evidence |
|---|---|---|---|
| 4.1 | Deal registration defined process | Yes | Extends from Select through Elite |
| 4.2 | One joint selling activity in 12mo | Yes | DT Security Landesbank deployment (Jan 2026 PR), Haufe Group case study, IWT 2025 with Computacenter |
| 4.3 | Partner-sourced leads tracked separately | Inferred yes | Standard partner program practice |
| 4.4 | Account mapping conducted | GATED | No public evidence of DACH partner-customer overlap mapping |
| 4.5 | Joint business plan with top partners + QBR | GATED | Annual Success Plan referenced for Premier/Elite, DACH QBR cadence unclear |
| 4.6 | Deal-reg approval SLA (48h or less) | GATED | |
| 4.7 | MDF with ROI requirements | MDF exists, ROI requirements GATED | Proposal-based MDF via Campaign Builder |
| 4.8-4.10 | World-class checkpoints | N/A | |

**KPIs:**
- Partner-sourced revenue share: 70% of new security business through channel globally per Dave Allen (VP Geo Sales, Akamai). DACH-specific split GATED.
- Deal-reg approval time: GATED.
- Co-sell pipeline coverage: GATED.
- MDF ROI: GATED.

**Why Basic:** structural infrastructure (deal-reg, MDF, certified service providers) exists at Professional level globally. DACH execution thin because of thin partner roster + missing channel marketing function. With 5 named anchor partners in DACH (Deutsche Telekom Security, Bechtle, Controlware, InfoGuard, Computacenter), joint planning + account mapping + multi-partner orchestration cannot scale.

---

### Stage 5: Deliver — Basic+ [INFERRED ceiling: Professional]

Subscription model + certified service providers + DT Security as Security Certified Service Provider for Guardicore suggest the ceiling is Professional-grade delivery infrastructure. However, no Professional checkpoint (5.4 spec sign-off gate, 5.5 tiered service levels operationalized, 5.6 site readiness verification, 5.7 AR suspension automation) could be verified from external sources. All are GATED.

Per maturity framework scoring rules: a stage scores at the highest level where ALL checkpoints are present AND KPI thresholds are met. With zero Professional checkpoints verified, the confirmed score is Basic. The structural indicators (subscription model, GCSP certification program, DT Security partnership) justify an inferred ceiling of Professional but not a confirmed Professional score.

Tag: needs internal verification during interview. Questions to ask:
- "How are Guardicore deployment SLAs structured per partner tier in DACH? Is there differentiation between Select and Premier on delivery priority?"
- "What is partner satisfaction with the Guardicore deployment lifecycle at the top 5 DACH partners? How is install base data captured and shared back to Akamai?"

---

### Stage 6: Renew — Basic+ [INFERRED ceiling: Professional]

Subscription model structurally favors high renewal. 70% new security business through channel (Dave Allen, VP Geo Sales) implies channel ownership of renewal flow. Detailed renewal KPIs GATED. Same methodology caveat as Stage 5: no Professional checkpoint (6.4–6.7) verified externally.

Tag: needs internal verification. Questions to ask:
- "What is gross retention vs net retention on Guardicore through channel in DACH?"
- "Who owns the renewal motion — Akamai direct or the partner?"

---

### Stage 7: Expand — Basic

| # | Checkpoint | Present? | Evidence |
|---|---|---|---|
| 7.1 | Identified cross-sell/upsell products | Yes | Akamai portfolio: CDN, Guardicore, API Security, Bot Manager, EAA, App & API Protector |
| 7.2 | One cross-sell in 12mo via channel | Yes | DT Security expanded from prior Akamai relationship to Guardicore (Jan 2026) |
| 7.3 | Geographic/segment gaps known | Partial | Romandie (FR-CH) gap visible. Austria near-greenfield. Mittelstand below direct-sales coverage unaddressed by current 5 anchors |
| 7.4 | Account plans with expansion targets | GATED for DACH | |
| 7.5 | Portfolio view of partner coverage | No public evidence | |
| 7.6 | Expansion vs new-logo revenue tracked separately | GATED | |
| World-class checkpoints | N/A | | |

**Why Basic:** the product portfolio breadth is a structural Professional+ asset. The orchestration layer (constellation model, partner-to-partner referrals, portfolio coverage analytics) is not visible at DACH level. Cross-sell happens (DT Security example) but not systematically.

---

## Top 3 gaps with revenue impact

### Gap 1: Enable — missing DACH channel marketing function (the role itself)

**What is missing:** No DACH channel marketing function exists. Marketing motions THROUGH partners (manufacturer content distributed via partner brand to partner audience) and FOR partners (manufacturer-funded marketing for small partners) cannot execute. No public DE-language NIS2 partner playbook surfaced in research. Campaign Builder localization for DACH status unknown.

**Why it matters now:** NIS2 affects 29,000+ German organizations [SOURCE: BSI 2024]. Window for partner-led capture of this mandatory-budget wave is 18-24 months. Competitors with staffed DACH channel marketing execute while Akamai builds.

**Revenue impact — directional framing:**

The core economic argument does not require precise dollar estimates. It rests on one verified number and one structural observation:

- **Verified:** 70% of new Akamai security business flows through channel (Dave Allen, VP Geo Sales). This means DACH security revenue growth is gated by channel execution quality.
- **Structural:** Motions 3 (THROUGH) and 4 (FOR) are the scalable channel marketing motions — they multiply the manufacturer's reach through partner distribution and execute campaigns for partners who lack in-house marketing. Neither motion can run in DACH without staffing. Every quarter without them is a quarter where channel-led pipeline generation operates on only two of four engines operate.

The German Zero Trust market grows from $2.47B (2024) to $5.6B by 2030 at 14.7% CAGR [Mordor Intelligence]. Akamai's share of that growth through the DACH channel depends on how quickly the four-motion marketing engine is operational. The velocity difference between "operational in Q3 2026" and "operational in Q1 2028" compounds over the remaining NIS2 compliance window. The exact dollar impact requires internal capture-rate targets that are gated — but the magnitude is material, not marginal, given the 70% channel dependency.

**90-day intervention (D2-2 → D3-1/D3-2 feed):**
1. Stand up DACH content stack: 3 NIS2-Mittelstand-Zero-Trust assets in German (white paper, ROI calculator, partner-brandable webinar template) by Day 60
2. Launch motion 4 (FOR partners): manufacturer-executed campaign for top 3 anchor partners (DT Security, Bechtle, Controlware), partner brand on output, leads routed to partner by Day 90
3. Establish MDF cadence with ROI gates at quarterly cycle starting Q3 2026

---

### Gap 2: Recruit — no systematic partner recruitment pipeline; recruitable Mittelstand partners sit outside the program

**What is missing:** A structured ABM/TAS partner motion does not exist in Akamai DACH today. Mittelstand systemhauser with multi-vendor flexibility and no flagship competitor lock — Axians/Fernao (DE), SVA (DE), ACP Gruppe (AT), AVANTEC (CH) — sit outside the program despite direct fit with NIS2-affected Mittelstand customers. The existing anchor partners (Computacenter, Bechtle, Cancom, Controlware) are structurally locked to Cisco/PANW/Zscaler triple-anchor stacks, limiting Akamai's share of their attention and budget to residual product-gap deals.

**Dispositions (from D2-RC, `02-akamai/research/outputs/entanglement/04-recommended-dispositions.md`):**

*Scoring note:* Recruitability scores shown are integer buckets (1-5). The scoring framework in `03-recruitability-scoring-framework.md` uses a continuous weighted score (R) across 6 sub-criteria before bucketing. Partners with integer bucket 3 may have continuous R scores at or above the 3.5 Pursue threshold when sub-criteria like regulatory tailwind alignment (S4) or geographic reach value (S6) are strong. The priority Pursue designation for SVA, ACP, and InfoGuard reflects their continuous R scores, not the integer bucket alone.

| Partner | Recruitability | Disposition | Reasoning |
|---|---|---|---|
| Axians/Fernao (DE) | 4 | Pursue (priority) | ISG Leader DE 2025 × 4 cyber categories; no flagship competitor lock at L1/L2; Fernao integration creates window; NIS2/DORA/KRITIS positioning aligned to Guardicore wedge |
| AVANTEC (CH) | 4 | Pursue (priority) | Zscaler + Netskope flagship resellers with Illumio "newcomer" side-bet; the Illumio side-bet is displaceable for Guardicore |
| SVA (DE) | 3 (continuous R above Pursue threshold) | Pursue (priority) | Federal Business POY (PANW DE 2025); no Akamai or Illumio presence; Fortinet EPSP lock applies to firewall/SD-WAN only — Guardicore micro-segmentation orthogonal |
| ACP Gruppe (AT) | 3 (continuous R above Pursue threshold)80 (priority) | Multi-vendor Austrian systemhaus; no flagship competitor lock visible; AT footprint addresses currently underserved Akamai geography |
| InfoGuard (CH) | 3 (continuous R above Pursue threshold)80 (priority) | Already public Akamai/Guardicore partner; deepen to Premier qualification |
| Computacenter (DE) | 1 | Contain | Triple-anchor systemhaus (Cisco + PANW + Zscaler +multiple flagships); Akamai works residual product gaps (Guardicore east-west, API security) within existing Select tier; no flagship MDF |
| Navixia (CH) | 2 | Contain | Illumio top-tier services embed; engage for non-segmentation portfolio (API Security, Bot Manager) where Illumio does not compete; Swiss-French gap play |
| KAEMI (DE) | 1 | Drop | Double-flagship lock (Illumio Radiate + Cloudflare ASDP); no realistic 12-month window. Monitor tripwires: Illumio Radiate lapse, Cloudflare ASDP renewal failure, founder exit |

**Why it matters now:** Mittelstand Zero Trust capture without systemhaus distribution is structurally limited. The recruitable surface concentrates in the 5 priority Pursue partners (Axians/Fernao, AVANTEC, SVA, ACP, InfoGuard) plus distributor mindshare lift at Infinigate and Arrow ECS Switzerland. The triple-anchor systemhauser (Computacenter, Bechtle, Cancom) produce residual product-gap revenue on specific deal types without flagship investment.

**Revenue impact — directional framing:**

Each strategic partner developed to Premier tier represents a meaningful annual revenue relationship. The exact threshold is gated (Akamai's DACH-localized Premier criteria under Partner Connect are not public). The directional argument: 5 priority Pursue partners, if recruited and developed to Premier over 18-24 months, constitute the DACH Mittelstand channel front that does not currently exist. The revenue case is not "how many dollars per partner" but "this market segment is currently unreachable through channel because the partners who serve it are not in the program."

Contain partners (Computacenter, Bechtle, Cancom, Controlware, NTT Data DE, Navixia) produce residual revenue in product-gap deal types without flagship investment. The investment posture is reactive deal support, not proactive recruitment spend.

**90-day intervention (D3-1: ABM/TAS DACH Partner Project):**
1. Operationalize the 5 priority Pursue partners with full 6-dimension IPP scoring (per ADR-011), 9-box positioning, named owner per partner, named-account triangulation targets — sequencing from `02-akamai/research/outputs/entanglement/04-recommended-dispositions.md` Section 2
2. Build Contain playbooks per partner: explicit deal-type rules (Computacenter = Guardicore east-west + API Security only; Navixia = non-segmentation portfolio in Romandie; Bechtle/Cancom/Controlware = NIS2 narrative co-authoring inside Select tier)
3. Distributor mindshare lift programme at Infinigate Deutschland and Arrow ECS Switzerland (quarterly Distributor Business Reviews, named DACH Akamai executive sponsor)
4. Drop list: remove KAEMI, Open Systems, genua, Exclusive Networks DE, Westcon-Comstor from TAL; reallocate budget toward Pursue list

### Gap 3: Co-sell — contested mindshare at distribution layer + Austrian greenfield

**What is missing:** Infinigate distributes Akamai, Illumio, AND Cloudflare MSSP (exclusive) in DACH. Arrow ECS CH holds both Guardicore (since 2017) and Illumio exclusive. Mindshare contested, no public Akamai Distributor Business Review cadence surfaced. Austria has no visible Akamai partner anchor.

**Why it matters now:** distributors carry 70% of new security business per Dave Allen (VP Geo Sales, Akamai). If Akamai mindshare at Infinigate sits at parity across three competing vendors, correcting to majority via active mindshare management produces shift on the highest-volume channel.

**Revenue impact — directional framing:**

The distribution layer is the highest-leverage short-term revenue surface because it is the existing channel — no recruitment required, only mindshare rebalancing. The directional case: if 70% of new security business flows through channel, and the primary DACH distributor allocates attention equally across Akamai, Illumio, and Cloudflare, Akamai receives roughly one-third of the distributor's security-portfolio promotion effort. Moving that share to majority (50-60%) through active mindshare management is a marketing execution problem, not a structural one. The Austrian recruitment anchor pair (ACP + a second AT partner) addresses the geographic greenfield separately.

**90-day intervention:**
1. Establish quarterly Distributor Business Review with named Akamai DACH executive ownership at Infinigate Deutschland and Arrow ECS Switzerland
2. Build contested-account playbook for distributor reps (when do you lead Akamai vs Illumio vs Cloudflare based on customer signal)
3. Austria gap-fill plan with ACP Gruppe as primary recruit (per Pursue priority list)

---

## Questions for the hiring manager (interview-grade)

Lifted from research and refined against scorecard findings:

1. **Computacenter and tier strategy:** What is the Akamai pipeline coming from Computacenter Germany today, and what is gating progress beyond Select — pricing, certification load, or named-account conflicts with their Cisco/PANW/Zscaler primary stacks?

2. **DT Security reference unlock:** Is the Landesbank Guardicore reference (DT Security, January 2026 PR) accessible to DACH partner marketing for repurposing, or under NDA?

3. **Illumio-locked partners:**KAEMI is Illumio's EMEA Partner of the Year and appears structurally locked with a Cloudflare ASDP double-anchor. Has Akamai attempted engagement, and what was the outcome?

4. **DACH recruitment targets:** What is the EMEA target for net-new DACH partner recruitment under Partner Connect in FY26?

5. **NIS2 partner enablement:** What is Akamai DACH's NIS2 / DORA partner enablement plan? No public DE-language playbook has surfaced.

6. **Partner portfolio assessment:** How does the channel team currently assess which DACH partners are realistically movable versus structurally committed to competing vendors? Is there a systematic framework, or is it managed relationship by relationship?

---

## D2-RC refresh complete (2026-05-18)

Gap 2 dispositions populated from D2-RC research outputs in `02-akamai/research/outputs/entanglement/`:
- 33-partner entanglement matrix (File 1)
- 12 deep partner profiles (File 2)
- 6-sub-criterion Recruitability scoring framework (File 3) — ADR-011 operationalization
- Disposition summary plus 90-day execution plan (File 4)

Recruit stage maturity score did NOT change after D2-RC. The structural gap (missing IPP execution, missing 9-box, thin DACH roster) is independent of Recruitability dimension content. Recruit stays Basic.

ADR-011 amendment (2026-05-18) retracts the prior claim that Computacenter is publicly an Illumio investor. D2-RC verified Illumio's funding history; Computacenter does not appear. The Computacenter Contain disposition stands; the rationale shifts from "equity-locked" to "service-MSP-locked + triple-anchor systemhaus".

## Method validation note

This scorecard uses the universal maturity model from `01-method/maturity-model/`. The model is portable: any partner program can be scored on these 7 stages with these capability checkpoints. The Akamai scoring above demonstrates the method, not just the diagnosis.