# Recruitability Scoring Framework — DACH Partner Pursuit

**Version:** v1 — 2026-05-18
**Owner:** D2-RC (Channel Intelligence)
**Companion to:** `01-entanglement-matrix.md`, `02-deep-profiles.md`
**Parent decision context:** ADR-011 (Recruitability dimension); D3-1 ABM/TAS DACH Partner Project disposition decisions.

---

## 1. Why this framework exists

The Akamai DACH Partner Program OS needs a *defensible*, *repeatable* way to rate each candidate partner for the probability we can recruit them (or deepen them, in the case of existing partners) to a meaningful share of Akamai pipeline within 12 months. The judgement has to:

- Combine **public, source-citable** signal with **private, sales-process** signal in a single rubric.
- Survive a partner-relationship-management (PRM) audit, i.e. each score has to be traceable to a specific evidence cell.
- Generalise from the four signal layers in ADR-011 (Contract, Equity, Flagship, Executive) to a *forward-looking* probability, not just a snapshot of competitor entanglement.
- Be coarse enough (5-point Likert) that two analysts arrive at the same score from the same evidence.

The Recruitability score (1-5) is **separate from** the entanglement signals because the entanglement is *what we observe today*, while Recruitability is the analyst's *forecast* of pipeline-share lift over the next 12 months given that observation, the macro picture (NIS2 / DORA / KRITIS), Akamai's own competitive position in the deal segments the partner sells, and partner-specific elasticity (Mittelstand vendor-flex pattern vs. Diamond-Innovator structural lock).

---

## 2. The six sub-criteria

Each partner is scored on six sub-criteria, each on a 1-5 Likert. The sub-criteria are weighted (sum to 1.0) and aggregated to a continuous score, which is then bucketed back to the integer 1-5 published in File 1.

### S1 — Competitor entanglement depth (weight 0.30)

How many of the four ADR-011 layers (L1 Contract, L2 Equity, L3 Flagship, L4 Executive) are *active* with at least one of Akamai's primary competitors (Illumio, Palo Alto Networks, Zscaler, Cloudflare, Cisco Security, Fortinet, Check Point)?

| S1 | Layer depth observed |
|---|---|
| 1 | 3+ layers active, including at least one of L1 (exclusive contract) or L2 (equity) |
| 2 | 2 layers active including L1 or L2 |
| 3 | 2 layers active but only at L3 / L4 (marketing + people, no structural contract) |
| 4 | 1 layer active, typically L3 marketing only |
| 5 | 0 layers active — competitor-whitespace partner |

> Inversion note: S1 is scored such that *higher = more recruitable*. A partner with no competitor lock scores 5; a partner with three layers of Illumio lock plus a Cloudflare exclusive scores 1.

### S2 — Vendor-stack diversity (weight 0.15)

Is the partner structurally a multi-vendor systemhaus (broad vendor set, no single anchor more than ~25% of revenue), or a near-mono-vendor specialist?

| S2 | Pattern |
|---|---|
| 1 | Near-mono-vendor; one named flagship-tier vendor accounts for the practice identity (e.g. KAEMI ↔ Illumio + Cloudflare, NTS ↔ Cisco, Indevis ↔ PANW + Fortinet) |
| 2 | 2 anchor vendors at flagship tier |
| 3 | 3 anchor vendors at meaningful tier; multi-flagship pattern |
| 4 | 4+ named vendors, no single dominant; "best-of-breed" stated philosophy |
| 5 | Vendor-neutral consulting / advisory / distribution by mandate |

> A high S2 score means the partner is *structurally open* to adding a new flagship vendor; a low S2 score means they have committed identity to a small set.

### S3 — Akamai-product-gap fit (weight 0.20)

Does the partner's current vendor stack have a *named technical gap* that Akamai's core portfolio (Guardicore micro-segmentation, API Security, App & API Protector, Cloud Acceleration, EAA/MFA, DDoS Edge) closes well?

| S3 | Product-gap fit |
|---|---|
| 1 | Partner's stack already covers the relevant Akamai product spaces with competitor SKUs (e.g. PANW Prisma + Zscaler ZIA + Illumio = full coverage of segmentation + SASE/ZTNA + edge security) |
| 2 | Partial overlap — Akamai brings 1 differentiator (e.g. API Security where PANW Prisma Cloud is thinner) |
| 3 | Akamai brings 2-3 differentiators across micro-segmentation, API Security, or edge |
| 4 | Akamai brings a clear product-gap fill in a regulated vertical (NIS2 / KRITIS / DORA) that the partner is actively monetising |
| 5 | Akamai is the natural anchor — partner has explicit edge / DDoS / segmentation pipeline with no flagship vendor today |

### S4 — Regulatory tailwind alignment (weight 0.10)

Does the partner's stated practice align with NIS2 (in-force Oct-2024, DE implementation pending), DORA (in-force Jan-2025), KRITIS Dachgesetz, BSI guidance, FINMA (CH), and the Schweizer NIS2-equivalent (under consultation)? This proxies for pipeline elasticity over the next 12-24 months.

| S4 | Regulatory posture |
|---|---|
| 1 | No public regulatory positioning observed |
| 2 | Generic compliance content; no flagship verticals |
| 3 | At least one regulatory narrative actively marketed (NIS2 *or* DORA *or* KRITIS) |
| 4 | Multi-narrative regulatory positioning; named vertical practice (e.g. KRITIS healthcare, BaFin-regulated finance) |
| 5 | Regulatory-narrative *thought leader* with ISG Leader, BSI APT-Response, BSI C5 audit, or analyst-recognised SOC/MDR practice |

### S5 — Partner organisational elasticity (weight 0.10)

Independent of competitor entanglement, is the partner organisationally able to bring a new flagship vendor on in 12 months? Considers M&A integration state, leadership stability, headcount growth, and whether the partner has a track record of *adding* vendors at flagship tier over the last 24 months.

| S5 | Organisational elasticity |
|---|---|
| 1 | Active divestiture / restructuring / distressed; vendor portfolio frozen (e.g. Materna SE exiting MSS Apr-2025; Atos/Eviden ongoing restructuring) |
| 2 | Stable but vendor-portfolio mature; no new flagships added in 24m |
| 3 | Mid-M&A integration (e.g. Axians + Fernao Oct-2025 consolidation) — *opportunistic moment* for new vendor adds |
| 4 | Stable, growing headcount; 1-2 new vendor flagships added in 24m |
| 5 | High-growth phase; visible track record of flagship-tier adds (e.g. Westcon-Comstor adding twin Zscaler specialisation Apr-2025 *while* keeping PANW flagship) |

### S6 — Geographic / vertical reach Akamai needs (weight 0.15)

Does the partner cover a geography or vertical where Akamai DACH currently has thin field coverage? Romandie (Swiss-French), Austrian Mittelstand outside Vienna, German federal Bonn/Berlin axis, healthcare KRITIS, OT/manufacturing, banking BaFin.

| S6 | Reach value |
|---|---|
| 1 | Partner adds no incremental geography / vertical Akamai does not already have |
| 2 | Partner overlaps an existing well-covered Akamai field territory |
| 3 | Partner has 1 named territory or vertical Akamai has on its gap-coverage map |
| 4 | Partner has 2+ named territories / verticals on Akamai's gap-coverage map |
| 5 | Partner is the *only* visible regional / vertical anchor for an Akamai field-coverage gap (e.g. Navixia for Romandie if no other Akamai partner is in Lausanne / Geneva) |

---

## 3. Aggregation

Continuous Recruitability score *R* is:

```
R = 0.30·S1 + 0.15·S2 + 0.20·S3 + 0.10·S4 + 0.10·S5 + 0.15·S6
```

bucketed back to the integer 1-5 by:

| Bucket | Range | Meaning |
|---|---|---|
| 1 | R ≤ 1.6 | Drop or treat as competitor surface |
| 2 | 1.6 < R ≤ 2.4 | Contain — opportunistic only |
| 3 | 2.4 < R ≤ 3.4 | Pursue — disciplined, named-account |
| 4 | 3.4 < R ≤ 4.2 | Pursue — priority |
| 5 | R > 4.2 | Pursue — flagship recruitment target |

---

## 4. Worked examples — calibrating the matrix in File 1

### Example A — KAEMI (Berlin)

| Sub | Score | Justification |
|---|---|---|
| S1 | 1 | L1 Cloudflare exclusive ASDP × 2 services + L3 Illumio EMEA POY FY2026 = 2 layers including L1. *Borderline 1 / 2 — pulled to 1 because both Cloudflare and Illumio are top-of-pyramid awards in the same year.* |
| S2 | 1 | Near-mono-vendor (Illumio + Cloudflare twin identity). |
| S3 | 2 | Akamai Guardicore is direct technical substitute for Illumio, but partner mind-share is identity-bound to current flagships. |
| S4 | 3 | NIS2 narrative present in marketing (Zero Trust + microsegmentation alignment). |
| S5 | 2 | Stable, owner-operated, but no recent track record of adding *new* flagships outside Illumio + Cloudflare. |
| S6 | 2 | Berlin geography is well-covered already by larger Akamai partners (Computacenter, Controlware). |

R = 0.30·1 + 0.15·1 + 0.20·2 + 0.10·3 + 0.10·2 + 0.15·2 = 0.30 + 0.15 + 0.40 + 0.30 + 0.20 + 0.30 = **1.65** → bucket **2**.

Note: File 1 publishes KAEMI as Recruitability 1, not 2. The discrepancy is the analyst's qualitative override (R = 1.65 is at the boundary; the FY2026 fresh-POY status and owner-founder identity argue for the lower bucket). Override is documented; revisited at next quarterly review.

### Example B — Axians DE + Fernao

| Sub | Score | Justification |
|---|---|---|
| S1 | 4 | Only 1 layer (L3 Fortinet visible). No PANW / Cisco / Zscaler / Illumio / Cloudflare flagship lock. |
| S2 | 4 | 4+ named vendors (Arista, Bluecat, Fortinet, IBM, Netbrain, Semperis). |
| S3 | 4 | NIS2/KRITIS pipeline + OT focus = Guardicore + API Security clean fit. |
| S4 | 5 | ISG Leader DE 2025 × 4 cyber categories = regulatory thought-leader. |
| S5 | 3 | Mid Fernao integration; opportunistic moment. |
| S6 | 4 | Mid-market NIS2 + OT + KRITIS — well-aligned with Akamai gap map. |

R = 0.30·4 + 0.15·4 + 0.20·4 + 0.10·5 + 0.10·3 + 0.15·4 = 1.20 + 0.60 + 0.80 + 0.50 + 0.30 + 0.60 = **4.00** → bucket **4**. Matches File 1.

### Example C — Computacenter

| Sub | Score | Justification |
|---|---|---|
| S1 | 1 | L1 (Zscaler top-3 self-attested) + L3 (Cisco × 3 + Zscaler × 1 + NetApp + NVIDIA + Nexthink) + L3 (Illumio MSP) = 3+ layers across multiple competitors. |
| S2 | 2 | 2-3 anchor vendors at multi-flagship tier (Cisco + Zscaler primarily, PANW second-tier). |
| S3 | 2 | Akamai brings limited new product space; partner already covers segmentation (Illumio MSP), SASE (Zscaler), edge security (own Microsoft / NetApp). |
| S4 | 4 | ISG Leader DE 6 consecutive years; multi-narrative. |
| S5 | 4 | Track record of adding flagship vendors (NVIDIA networking POY 2026, Tanium strategic partnership Aug-2025). |
| S6 | 2 | Computacenter covers all major DACH geographies already; Akamai field has access. |

R = 0.30·1 + 0.15·2 + 0.20·2 + 0.10·4 + 0.10·4 + 0.15·2 = 0.30 + 0.30 + 0.40 + 0.40 + 0.40 + 0.30 = **2.10** → bucket **2**.

But File 1 publishes Recruitability **1**. Override rationale: the *content* of the multi-flagship vendor portfolio (Cisco + PANW + Zscaler + Microsoft + NetApp + NVIDIA + Tanium) is so dense and the partner is so large (£9.2B group revenue) that incremental Akamai pipeline at any non-Premier-upgrade tier sits below the level of named-account decision-makers' attention. The override moves the score down one bucket. *Documented; revisit if Computacenter formally upgrades the Akamai relationship beyond Select.*

### Example D — Navixia (Ecublens)

| Sub | Score | Justification |
|---|---|---|
| S1 | 3 | L3 Illumio ZTS Professional + L3 marketing as "primary technology partner". 2 layers at L3 only. |
| S2 | 3 | 4 named vendors (Illumio, Check Point, Cisco Security, F5, Microsoft, Quest, Thales) — multi-flagship pattern. |
| S3 | 2 | Direct substitute play with Guardicore; Romandie market may already have Check Point ZTNA preferred. |
| S4 | 3 | Swiss FINMA / FedPol regulatory narrative implied; not flagship. |
| S5 | 3 | Stable senior-professional team, no recent visible flagship vendor add. |
| S6 | 5 | Romandie geography is *the* Akamai field-coverage gap if Akamai has no Lausanne / Geneva partner above Navixia in maturity. |

R = 0.30·3 + 0.15·3 + 0.20·2 + 0.10·3 + 0.10·3 + 0.15·5 = 0.90 + 0.45 + 0.40 + 0.30 + 0.30 + 0.75 = **3.10** → bucket **3**.

File 1 publishes **2** (Contain). The discrepancy is again a qualitative override: the *publicly visible* "1st EMEA, 3rd globally" Illumio ZTS Professional status is the partner's single largest piece of free-PR equity. Asking Navixia to compete that asset for Akamai segmentation deals would invite a public dilution that Navixia's senior partners are unlikely to accept inside 12 months. Override is therefore *time-limited*: revisit at next Illumio ZTS Professional re-certification cycle.

---

## 5. Scoring discipline — what to *not* do

The following are common biases the framework is built to suppress:

- **Recency bias toward award announcements.** A POY award is L3 evidence, not L1 contract evidence. Do not double-count by treating the announcement as both flagship recognition and contractual depth.
- **Geographic visibility bias.** A partner with a large LinkedIn following and frequent trade-press placements (e.g. KAEMI) is not more recruitable than a quieter Mittelstand systemhaus that already has whitespace in our portfolio.
- **Headcount halo bias.** A 11,475-employee partner is not automatically more attractive than a 770-employee partner; the Mittelstand-fit pattern often inverts the relationship.
- **Vendor-self-attestation bias.** "Top-3 worldwide Zscaler reseller" is self-attestation by Computacenter; the corresponding Zscaler statement is "Premier Partner". The matrix records the lower of the two when both are available.
- **Distressed-target bias.** Materna's exit from MSS (Apr-2025) makes them *less* recruitable, not more — there is no MSS channel to win pipeline through, regardless of their consulting strength. Score 2; disposition Monitor.
- **Distributor-as-partner conflation.** Distributors are scored on a separate rubric (mindshare lift) because their channel economics are not symmetric with resellers / SIs.

---

## 6. Tripwires — when a partner's score should be reviewed

A formal mid-cycle review is triggered when any of the following occur for a partner currently scored 3 or below:

1. Lapse of an exclusive-tier contract (L1) — Cloudflare ASDP renewal, PANW Distributor exclusivity, Illumio Radiate re-certification, Fortinet EPSP re-certification.
2. Public investor / equity change at the partner.
3. Senior executive departure (named in File 2's leadership lines) within 90 days.
4. Loss of an analyst leadership position (ISG Leader, Forrester Wave Leader, Gartner MQ Leader, IDC MarketScape Major Player).
5. Vendor partner-program structural change at a competitor (Cisco 360 PVI launched Jan-2026; PANW NextWave changes; Illumio Enlighten Partner Program adjustments).
6. Public M&A or restructuring announcement at the partner's parent.

For Recruitability 4-5 partners, the review cadence is quarterly regardless of tripwires.

---

## 7. Distributor-specific rubric (compact form)

Distributors are not scored on S1-S6; they are scored on *mindshare contestation*:

| D-score | Pattern |
|---|---|
| 1 | Vendor monolock (e.g. Exclusive Networks ↔ PANW, Westcon-Comstor ↔ Zscaler/PANW) — Akamai displacement unrealistic; Drop |
| 2 | Vendor preference is heavy on competitor; Akamai sits at the bottom of distributor mindshare |
| 3 | Multi-vendor distributor where Akamai already has named-distributor status and contested mindshare with 2-3 competitors is achievable (Infinigate, Arrow ECS CH) — Pursue mindshare lift |
| 4 | Akamai-preferred distributor with growing share-of-pipe |
| 5 | Akamai's distributor of choice with measurable mindshare leadership |

No DACH distributor currently sits at D-score 4 or 5; Infinigate and Arrow ECS CH are the realistic targets to lift from 3 to 4.

— *End of File 3 of 4.*
