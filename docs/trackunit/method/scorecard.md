# Integration Program Maturity Scorecard

Working diagnostic tool for the seven-stage integration partner lifecycle. Score each stage by verifying capability checkpoints (binary: present or absent) and measuring KPI performance against thresholds.

Scoring rule: a stage earns a maturity level when all checkpoints for that level and all levels below are present, and the KPI thresholds for that level are met. If capabilities are present but KPIs fall short, the score stays at the level below and the gap is tagged "infrastructure ahead of performance."

All KPI thresholds are reference targets for a platform integrations program. They are calibration starting points, adjustable per company during the diagnostic.

---

## Stage 1: Source

**Capability checkpoints**

| Level | # | Checkpoint | Present? |
|---|---|---|---|
| Basic | 1.1 | Inbound integration requests are logged in one place with a defined response process | |
| Basic | 1.2 | One person owns integration partner sourcing as a named responsibility | |
| Basic | 1.3 | A written description exists of what a good integration partner looks like | |
| Professional | 1.4 | Category map covers the software customers already run (ERP, rental, fleet, industry applications) with named candidates per category | |
| Professional | 1.5 | Candidate pipeline is tracked in CRM or PRM with stage progression | |
| Professional | 1.6 | Sourcing plan is reviewed quarterly against the connector launch target | |
| World-class | 1.7 | Customer demand signals (support tickets, sales losses, product telemetry) feed the candidate list automatically | |
| World-class | 1.8 | Competitive integration catalogs are monitored and gaps drive outreach | |
| World-class | 1.9 | Sourcing conversion benchmarks are set and tracked per category | |

**KPIs (reference targets)**

| KPI | Formula | Basic | Professional | World-class |
|---|---|---|---|---|
| Qualified candidates added | New candidates passing initial screen per quarter | >2 | >5 | >10 |
| Pipeline coverage | Candidates in pipeline ÷ annual connector launch target | >1x | >2x | >3x |

---

## Stage 2: Qualify

**Capability checkpoints**

| Level | # | Checkpoint | Present? |
|---|---|---|---|
| Basic | 2.1 | Candidates are screened against minimum criteria before any technical work starts | |
| Basic | 2.2 | Shared customer overlap is estimated for every candidate | |
| Basic | 2.3 | A go/no-go decision is recorded with a reason for every candidate | |
| Professional | 2.4 | Consumption potential scoring model exists with weighted criteria: customer overlap, expected data volume, use-case fit, partner commitment | |
| Professional | 2.5 | Customer overlap is verified from account data, not partner claims | |
| Professional | 2.6 | Qualification review runs on a fixed cadence with cross-functional input (product, engineering, commercial) | |
| World-class | 2.7 | Predicted consumption per candidate is modeled from comparable live connectors | |
| World-class | 2.8 | Scoring model accuracy is back-tested: predicted versus actual consumption at 12 months | |
| World-class | 2.9 | Low-scoring candidates are routed to a self-service tier instead of consuming pod capacity | |

**KPIs (reference targets)**

| KPI | Formula | Basic | Professional | World-class |
|---|---|---|---|---|
| Scoring coverage | Candidates with a completed consumption potential score ÷ candidates evaluated | >50% | >90% | 100% |
| Qualification conversion | Qualified candidates reaching signed scope ÷ candidates qualified | >20% | >35% | >50% |

---

## Stage 3: Scope

**Capability checkpoints**

| Level | # | Checkpoint | Present? |
|---|---|---|---|
| Basic | 3.1 | Every integration has a written scope before development starts | |
| Basic | 3.2 | Target use cases are named and tied to at least one real customer | |
| Basic | 3.3 | Commercial terms are agreed before build begins | |
| Professional | 3.4 | Scope template covers data contracts, API surface, error handling, security requirements, and launch plan | |
| Professional | 3.5 | Every scope includes quantified success criteria: target accounts, expected consumption, launch date | |
| Professional | 3.6 | Scope sign-off is a formal gate with named approvers on both sides | |
| World-class | 3.7 | Scoping is templated per integration pattern (ERP sync, telematics feed, application embed) and reused across partners | |
| World-class | 3.8 | Consumption targets in scope documents are tracked post-launch and reviewed at partner QBRs | |
| World-class | 3.9 | Scope changes after sign-off follow a change-control process with commercial impact assessed | |

**KPIs (reference targets)**

| KPI | Formula | Basic | Professional | World-class |
|---|---|---|---|---|
| Time-to-signed-scope | Days from qualification to scope sign-off | <90 | <45 | <21 |
| Scope stability | Integrations built without major scope change ÷ integrations built | >60% | >80% | >95% |

---

## Stage 4: Build

**Capability checkpoints**

| Level | # | Checkpoint | Present? |
|---|---|---|---|
| Basic | 4.1 | Partners get API documentation and sandbox access within 5 business days of scope sign-off | |
| Basic | 4.2 | A named technical contact answers partner build questions | |
| Basic | 4.3 | Integrations are tested against real data before any customer sees them | |
| Professional | 4.4 | Certification gate verifies data quality, security, error handling, and rate-limit behavior before production access | |
| Professional | 4.5 | Reference implementations and sample code exist for the common integration patterns | |
| Professional | 4.6 | Build progress is tracked against scope milestones with stalled builds flagged and escalated | |
| World-class | 4.7 | Self-service developer platform: partners register, build, and submit for certification without manual provisioning | |
| World-class | 4.8 | Certification is automated: test suites run against the partner build and produce a pass/fail report | |
| World-class | 4.9 | Build-stage telemetry identifies where partners get stuck and feeds documentation improvements | |

**KPIs (reference targets)**

| KPI | Formula | Basic | Professional | World-class |
|---|---|---|---|---|
| Time-to-certified-build | Days from scope sign-off to certification pass | <180 | <90 | <45 |
| Certification first-pass rate | Builds passing certification on first submission ÷ builds submitted | >40% | >70% | >90% |

---

## Stage 5: Launch

**Capability checkpoints**

| Level | # | Checkpoint | Present? |
|---|---|---|---|
| Basic | 5.1 | Every certified integration is listed in a public catalog or marketplace | |
| Basic | 5.2 | At least one customer is committed to go live before launch | |
| Basic | 5.3 | Both partners announce the integration through at least one channel | |
| Professional | 5.4 | Launch plan is part of the scope: listing, announcement, enablement content, and first accounts named before certification | |
| Professional | 5.5 | Sales teams on both sides receive enablement: what it does, who it is for, how it is priced | |
| Professional | 5.6 | First production usage is verified and reported within 30 days of launch | |
| World-class | 5.7 | Launch engine is standardized: every connector ships with listing, demo assets, and joint campaign on a fixed timeline | |
| World-class | 5.8 | Field and regional teams carry launch targets for new connectors in their accounts | |
| World-class | 5.9 | Launch performance is reviewed per connector at 30 and 90 days with a defined intervention if usage is zero | |

**KPIs (reference targets)**

| KPI | Formula | Basic | Professional | World-class |
|---|---|---|---|---|
| Time-to-first-credit | Days from certification to first production consumption | <120 | <60 | <30 |
| Live-within-90 rate | Connectors with an active customer within 90 days of launch ÷ connectors launched | >50% | >80% | >95% |

---

## Stage 6: Adopt

**Capability checkpoints**

| Level | # | Checkpoint | Present? |
|---|---|---|---|
| Basic | 6.1 | Usage per connector is measured: which accounts are active and how much they consume | |
| Basic | 6.2 | One person owns adoption for each live connector | |
| Basic | 6.3 | Dormant connectors (zero usage for 90 days) are identified and reviewed | |
| Professional | 6.4 | Target account list per connector is built from verified customer overlap and worked jointly with the partner | |
| Professional | 6.5 | Adoption is reviewed at partner QBRs against the consumption targets set in scope | |
| Professional | 6.6 | Stuck accounts are diagnosed with root cause categories: technical, enablement, commercial, or fit | |
| World-class | 6.7 | Usage signals trigger automated adoption plays: onboarding nudges, expansion prompts, health alerts | |
| World-class | 6.8 | Customer-facing teams see connector usage in their account views and act on it | |
| World-class | 6.9 | Adoption benchmarks per connector category exist and underperformers are managed against them | |

**KPIs (reference targets)**

| KPI | Formula | Basic | Professional | World-class |
|---|---|---|---|---|
| Active accounts per connector | Accounts with production usage at 6 months post-launch | >3 | >10 | >25 |
| Account activation rate | Active accounts ÷ target accounts identified for the connector | >20% | >40% | >60% |

---

## Stage 7: Scale

**Capability checkpoints**

| Level | # | Checkpoint | Present? |
|---|---|---|---|
| Basic | 7.1 | At least one connector has deployed to a second account without a new build | |
| Basic | 7.2 | Consumption through partner integrations is reported as a separate line | |
| Basic | 7.3 | Lessons from each integration are captured and reused in the next scope | |
| Professional | 7.4 | Connectors are productized: versioned, documented, deployable to a new account without custom development | |
| Professional | 7.5 | Partners sell the connector independently with their own enablement and pricing motion | |
| Professional | 7.6 | The lifecycle playbook is documented end to end and each new partner moves through it faster than the last | |
| World-class | 7.7 | Marketplace handles discovery, provisioning, and billing for connectors without pod involvement per deal | |
| World-class | 7.8 | Consumption per connector compounds: growth comes from existing connectors, not only new launches | |
| World-class | 7.9 | Partner-built extensions appear on top of existing connectors without being sourced by the program | |

**KPIs (reference targets)**

| KPI | Formula | Basic | Professional | World-class |
|---|---|---|---|---|
| Partner consumption share | Platform consumption through partner integrations ÷ total platform consumption | >5% | >15% | >30% |
| Connector reuse rate | Connectors live in 3+ accounts without custom work ÷ connectors launched 12+ months ago | >30% | >60% | >85% |

---

## How to use this scorecard

Score each stage in order. Mark every checkpoint present or absent, with no partial credit: if the answer is "partially" or "in progress," the checkpoint is absent. A stage scores at the highest level where all checkpoints at that level and below are present and both KPI thresholds are met. Plot the seven scores on the spider chart (Basic = 1, Professional = 2, World-class = 3), identify the top three gaps by consumption impact, and select 3-5 interventions for a 90-day sprint. Re-score quarterly. Every re-score should show movement in at least one stage; stagnation across two consecutive quarters signals a governance problem, not an execution problem.

*Framework illustration. Maturity thresholds are reference targets, not Trackunit scores.*
