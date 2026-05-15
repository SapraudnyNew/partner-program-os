# Stage 5: Deliver

## Strategic intent

Execute from signed order through commissioned-and-handed-over installation. The partner owns commercial responsibility for end-customer satisfaction. The manufacturer provides product, technical sign-off, and back-office discipline.

Deliver is where the partnership either compounds trust or accumulates debt. Every operational failure in this stage (late delivery, spec error, missed site readiness, disputed invoice) destroys trust that Stages 1-4 built. Every operational success (on-time, on-spec, on-budget, clean handover) deposits trust that Stages 6 and 7 withdraw.

The critical output of this stage is not the installed product. It is the install base data. Every commissioned unit must register serial number, end-customer contact, and warranty terms into a shared install base. Without this data, Stage 6 (Renew) has no foundation for service revenue and Stage 7 (Expand) has no foundation for cross-sell. Handover is a data transfer event, not a signature on a piece of paper. [P-16] [P-21]

---

## Maturity levels

| Level | Capabilities | KPIs |
|---|---|---|
| Basic | Order submission process exists (portal, EDI, or structured email). Order confirmation issued within defined timeframe. Delivery dates communicated before shipment. | Spec-complete PO rate >60%. On-time delivery >75%. Install base capture >50%. |
| Professional | Spec sign-off gate: orders not accepted without validated configuration. Tiered service levels operationalized (different lead times, PM support, payment terms by tier). Site readiness verification required before installation release. AR overdue triggers automatic order suspension. | Spec-complete PO rate >80%. On-time delivery >90%. Site readiness on time >85%. DSO <60. Install base capture >90%. Project margin protection >95%. |
| World-class | Two-way data visibility: partner sees production status, manufacturer sees project status in real time. Handover documentation auto-populates install base. NPS call to end-customer within 7 days of handover, results fed to Stage 6. | Spec-complete PO rate >95%. On-time delivery >95%. Site readiness 100%. DSO <30. Install base capture 100%. Project margin protection >98%. |

Full checkpoint detail: see [maturity-model/scorecard-template.md](maturity-model/scorecard-template.md), Stage 5.

---

## The system

### Order-to-handover process

The Deliver stage runs through nine sequential sub-stages. Each has a defined owner, a gate condition, and a deliverable. The gates are hard: a sub-stage does not advance until the gate condition is met. No manual overrides without VP-level approval, logged.

| # | Sub-stage | Gate condition | Manufacturer role | Partner role | End-customer role |
|---|---|---|---|---|---|
| 1 | Order placement | Spec-complete PO submitted through portal | I | R, A | C |
| 2 | Contract administration | Signed contract (manufacturer provides templates; co-signs for Global Accounts only) | C | R, A | R (signs) |
| 3 | Order confirmation and lead time lock | Order confirmed within SLA (target: 24h). Delivery date locked. | R, A | I | I |
| 4 | Manufacturing and outbound logistics | Product manufactured. Outbound freight arranged. Delivery date confirmed. | R, A | R (inbound logistics, site access) | C (site access) |
| 5 | Storage and site staging | Partner takes custody. Storage conditions per manufacturer guidelines. | C (guidelines) | R, A (custody, storage) | R (provides storage area) |
| 6 | Financial operations | Payment milestones executed per agreement. AR managed. Overdue = automatic suspension. | A (AR management, suspension enforcement) | R (payment execution) | A (invoice approval) |
| 7 | Site readiness verification | Site readiness checklist submitted and approved. Silver tier: partner self-certifies. Gold/Platinum: manufacturer co-signs. | C (Silver) / R (Gold/Platinum co-sign) | R, A | R (delivers compliant site) |
| 8 | Installation release | Installation order released after readiness sign-off. | A (releases) | R (mobilizes crew) | I |
| 9 | Handover and documentation | Handover package complete: installation report, commissioning certificate, serial registration, NPS survey triggered. | R (NPS call, product registration) | R, A (handover package, documentation quality) | A (signs acceptance) |

### Tiered service levels

Partners at different tiers receive different operational treatment. The tiers must have teeth: a Gold partner must feel a measurable difference from a Silver partner in their P&L and their customer's experience. [E-02]

| Parameter | Silver | Gold | Platinum |
|---|---|---|---|
| Order confirmation SLA | 48 hours | 24 hours | 4 hours |
| Dedicated project manager | No | Shared | Dedicated |
| Production priority | Standard queue | Priority queue | Express |
| Payment terms | Net 30 | Net 45 | Net 60 |
| Site readiness verification | Partner self-certifies | Manufacturer co-signs | Manufacturer co-signs + pre-visit |
| Handover support | Standard | Enhanced documentation review | On-site manufacturer presence |

### Hard gates

Three gates prevent the most expensive operational failures. Each gate is binary: pass or do not pass. No exceptions without documented VP approval. [P-19] [P-20]

**Gate 1: spec sign-off.** No order enters production without validated configuration. Spec errors at order entry are the largest single cause of project margin erosion. The pre-order engineering sign-off catches configuration mistakes before they become manufacturing mistakes. [E-08]

**Gate 2: site readiness.** No installation crew mobilizes without a signed site readiness checklist confirming the opening is to spec, the power supply is available, the floor is level, and access is clear. Mobilizing a crew to an unprepared site costs the partner money and the manufacturer credibility. [E-08]

**Gate 3: AR suspension.** No new orders process for a partner with AR overdue beyond 30 days. The system blocks automatically. Exceptions require VP approval and are logged. This is the enforcement mechanism that prevents the manufacturer from holding tens of millions in aged receivables while continuing to supply a non-paying partner. [P-20]

### Handover as data transfer

The handover is not complete when the end-customer signs the acceptance form. It is complete when the install base register contains:

- Serial number of every installed unit
- End-customer company name and site address
- End-customer primary contact (name, email, phone)
- Partner who delivered
- Installation date
- Warranty start and end dates
- Service contract status (attached at sale or not)
- NPS survey response (triggered within 7 days)

This data feeds Stage 6 (Renew: service contracts, spare parts, retrofit, modernization) and Stage 7 (Expand: cross-sell, portfolio coverage). Without it, the downstream stages operate blind. [P-21] [P-44]

---

## Common failure modes

**Spec errors at order entry.** Largest single cause of project margin erosion. Pre-order engineering sign-off (Gate 1) prevents this. Without the gate, errors propagate through manufacturing and arrive at site as wrong configurations. [E-08]

**Storage cost absorbed silently.** Partner does not pick up delivered product. Manufacturer holds inventory. No one invoices for storage. Standard contractual hooks exist but go unenforced. The fix: storage SLA with fee trigger after defined period. [P-22]

**Handover-as-handshake.** Acceptance is signed but the document is unstructured, does not enter the install base, and does not trigger the NPS or customer success motion. The data dies on paper.

**No site readiness gate.** Installation crew arrives. Opening is not to spec. Crew goes home. Partner blames manufacturer. Manufacturer blames partner. Gate 2 prevents this entirely. [E-08]

**AR overdue without consequence.** Partner pays late. New orders still process. Eventually the manufacturer holds tens of millions in aged AR. Gate 3 eliminates this by making the consequence automatic and impersonal. [P-20]

---

## Diagnostic questions

1. Where does the partner submit the PO today: portal/ERP, email, or through a human?
2. What is the rate of spec-complete POs that do not need revision before order acceptance?
3. What is the manufacturer's order confirmation SLA, and is it actually met?
4. Do different partner tiers receive measurably different service levels?
5. Is there a site readiness checklist? Is it mandatory?
6. What happens when a partner's AR exceeds 30 days? Is there an automatic block?
7. How is the handover documented? Does it populate the install base automatically?
8. Do you call the end-customer after handover to measure satisfaction (NPS)?
9. What is the project margin protection rate (actual margin vs quoted margin at handover)?
10. What percentage of installed units have complete records in the install base register?

---

## Intervention library

### Play: spec sign-off gate implementation

- **Applicability:** companies with >10% PO revision rate. The play that stops margin erosion at the source.
- **Description:** require pre-order engineering validation for every PO. Build a configuration checklist in the order portal. Orders that fail the checklist cannot be submitted. Track PO revision rate monthly. Target: <5%.
- **Source:** [E-08] Hilti PMO pre-order sign-off model. [P-19]
- **Lead time:** 30 days for checklist build. 60 days for portal integration. Impact on margin within one quarter.

### Play: site readiness gate implementation

- **Applicability:** any company with partner-installed products where installation failures occur due to site conditions.
- **Description:** define site readiness checklist per product type. Make checklist submission mandatory before installation release. Silver partners self-certify. Gold/Platinum require manufacturer co-sign. Track submission rate and on-time compliance. [P-19]
- **Source:** [E-08] Hilti energy and industry site readiness protocol.
- **Lead time:** 2 weeks for checklist design. 4 weeks for process implementation. Impact immediate.

### Play: AR suspension automation

- **Applicability:** companies where partner AR management is manual and inconsistent.
- **Description:** configure ERP to automatically block new orders for any partner with AR overdue >30 days. No manual override. Exceptions require VP approval, logged. Communicate the rule to all partners before activation. Execute consistently. [P-20]
- **Source:** [E-04] dormakaba: zero overdue as condition for order continuity.
- **Lead time:** 30 days for system configuration. 60 days for partner communication and activation.

### Play: install base capture at handover

- **Applicability:** companies where handover documentation does not feed the install base register.
- **Description:** redesign the handover form to include all required install base fields. Make form completion a gate condition: handover is not marked complete until all fields are populated. Connect the form to the install base system (manual entry initially, automated integration at Professional maturity). Track install base capture rate monthly. [P-21] [P-44]
- **Source:** [E-11] Install base as prerequisite for Stage 6 service revenue.
- **Lead time:** 2 weeks for form redesign. 4 weeks for process implementation. 8-12 weeks for system integration.

### Play: NPS trigger to end-customer

- **Applicability:** any manufacturer with partner-installed products reaching end-customers.
- **Description:** manufacturer calls end-customer within 7 days of confirmed handover. Bypasses the partner filter on customer voice. NPS score recorded in install base. Data feeds Stage 6 churn risk assessment. [P-23]
- **Source:** [E-01] Bob Moore: "pierce the veil" principle.
- **Lead time:** immediate if resources exist. 90 days if building the outreach process from scratch.

### Play: tiered service level differentiation

- **Applicability:** companies where all partners receive the same operational treatment regardless of tier.
- **Description:** define measurably different service levels per tier (Silver/Gold/Platinum) across order confirmation SLA, PM allocation, production priority, payment terms, and handover support. Implement in ERP/operations systems. Communicate to all partners. Track tier-specific KPIs to verify the differentiation is real, not just documented. [E-02]
- **Source:** [P-12] Tiers reflect investment.
- **Lead time:** 4-6 weeks for tier definition and system configuration.

---

## RACI within the stage

| Activity | Manufacturer | Partner | End-customer |
|---|---|---|---|
| Order placement | I | R, A | C |
| Contract execution | C (templates; co-sign for Global Accounts) | R, A | R (signs) |
| Order confirmation | R, A | I | I |
| Manufacturing + outbound logistics | R, A | R (inbound from warehouse) | C |
| Storage and site staging | C | R, A | R (provides storage area) |
| Financial milestones | A | R | A |
| Site readiness verification | C/R (tier-dependent) | R, A | R |
| Installation release | A | R | I |
| Handover and documentation | R (NPS, registration) | R, A | A |

**RACI variant: companies without dedicated channel operations**

In companies with fewer than 10 active partners, Deliver is managed by the general operations or logistics team, not a dedicated channel operations function. The RACI compresses: the operations manager owns order confirmation, logistics, and gate enforcement. The sales account manager (who also manages the partner relationship) coordinates site readiness and handover. The variant is not about changing the gates or the process. It is about which person executes. The gates (spec sign-off, site readiness, AR suspension) remain mandatory regardless of team size. Without gates, small programs accumulate the same operational debt as large ones, just with fewer people to manage the consequences.

---

## Tool requirements

| Category | Requirement for Deliver | Evaluation criteria |
|---|---|---|
| ERP / order management | Order portal with spec validation, tier-specific SLA routing, AR suspension automation, delivery date locking | Configuration checklist enforcement, automatic blocks, tier-differentiated workflows |
| Project management | Site readiness checklist management, installation scheduling, handover documentation | Checklist templates per product, gate enforcement, mobile access for field teams |
| CRM / install base | Handover form feeding install base register. Serial number, end-customer, warranty, NPS all captured at handover. | Install base auto-population from handover, partner-visible install base view, NPS survey integration |
| Analytics / BI | Deliver dashboard: spec-complete rate, on-time delivery, site readiness compliance, DSO, AR aging, install base capture rate, project margin protection | Tier-level comparison, partner-level drill-down, trend analysis, exception alerting |

---

## Evidence

Principles from `appendix/evidence-library.md` that primarily apply to this stage:
- P-16 (operations is a maturity indicator, not an admin function)
- P-17 (digital order placement as baseline)
- P-18 (one process, local exceptions)
- P-19 (site readiness hard gate)
- P-20 (AR overdue = automatic block)
- P-21 (handover as data transfer)
- P-22 (storage SLA with teeth)
- P-23 (NPS as manufacturer-direct channel)

Secondary alignment: P-36 (governance), P-42 (data layer), P-44 (install base).

---

## Research refresh layer

Space for deep research agent output when available:

- Latest developments in order-to-handover operations (2024-2026): digital order portals, automated configuration validation, IoT-connected delivery tracking, digital handover with QR-code-based install base registration
- Best practices: Hilti (PMO model with mandatory pre-order engineering sign-off and site readiness verification), dormakaba (SAP Business Network SLA, zero overdue as order continuity condition), Atlas Copco (48h standard dispatch), Cisco (CCW order processing, partner field guide for payment discipline)
- Future outlook: automated spec validation using AI/ML, augmented reality for site readiness verification, blockchain-verified handover records, predictive logistics for delivery date optimization
- Confidence score per data point (high/medium/low based on source quality)

Agent output will be appended here when Mission 1 executes. See [research-agent/00-agent-spec.md](../research-agent/00-agent-spec.md).
