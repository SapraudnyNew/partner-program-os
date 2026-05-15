# Stage 5: Deliver

> **Status:** Draft (most developed stage). Built from Session 1 deep research on order-to-handover operations.

## What this stage is

The window from signed order through commissioned-and-handed-over installation. The partner takes commercial responsibility for end-customer satisfaction; the manufacturer provides product, technical sign-off, and back-office discipline. Deliver is where the partnership either compounds trust or accumulates debt.

## What "good" looks like

1. **Zero-paper digital order flow.** Every transactional document (PO, contract, invoice, handover sign-off) lives in one partner portal. No email attachments as system-of-record. [E-04]
2. **Hard gates between stages.** Spec sign-off blocks order entry. Site readiness sign-off blocks installation release. Payment milestone blocks next order. Gates are automated, not negotiated case by case. [E-09]
3. **Tiered service levels with teeth.** Silver/Gold/Platinum tiers have measurably different lead times, payment terms, and PM support — and partners actually feel the difference in their P&L. [E-02]
4. **Two-way data visibility.** Manufacturer sees partner's project status. Partner sees manufacturer's production status. Neither side has to ask.
5. **Handover produces install base data.** Every commissioned unit registers serial number, end-customer contact, and warranty terms into a shared install base — the foundation for Stages 6 (Renew) and 7 (Expand).

## Common failure modes

- **Spec errors at order entry.** Largest single cause of project margin erosion. Hilti's PMO model addresses this with mandatory pre-order engineering sign-off. [E-08]
- **Storage cost absorbed silently.** Partner doesn't pick up, manufacturer holds inventory, no one is invoiced. Standard contractual hooks exist but go unenforced.
- **Handover-as-handshake.** Acceptance is signed but the signed document is unstructured, doesn't enter the install base, and doesn't trigger the customer success motion.
- **No site readiness gate.** Installation crew arrives, opening isn't to spec, crew goes home, partner blames manufacturer, manufacturer blames partner. [E-08]
- **AR overdue without consequence.** Partner pays late, new orders still process. No automatic block. Eventually the manufacturer holds tens of millions in aged AR.

## Diagnostic questions

1. Where does the partner submit the PO today: portal/ERP, email, or through a human?
2. What's the rate of spec-complete POs that don't need revision before order acceptance?
3. What's the manufacturer's order confirmation SLA, and is it actually hit?
4. Who owns the inbound logistics from the manufacturer's warehouse to the job site?
5. Who carries storage cost when the partner delays pickup, and is it ever invoiced?
6. What's the site-readiness checklist, who signs it, how many days before installation?
7. Is installation order release automated based on readiness, or is it manual?
8. What does the handover package contain, and where does it go after signature?
9. What's the install-base completeness rate after handover?
10. Does AR overdue trigger automatic block of new orders, or does it require a human decision?

## Intervention library

### Play: Single Digital Order Channel

- **Source:** dormakaba SAP Business Network model [E-04]
- **Applicability:** Manufacturers with partner-driven business and email-as-PO patterns.
- **Description:** Move every order, contract, invoice, and payment confirmation to a single portal. Email submissions are rejected at intake.
- **Lead time:** 6–9 months including partner change management.

### Play: Pre-Order Technical Sign-Off

- **Source:** Hilti PMO [E-08]
- **Applicability:** Configurable products with high spec-error rates.
- **Description:** Certified engineer signs off every order's specification before ERP entry. Partner-side technical contact gets named and trained.
- **Lead time:** 90 days to pilot, 6 months to full rollout.

### Play: Tiered Site Readiness Gate

- **Source:** Hilti + Atlas Copco [E-08, E-07]
- **Applicability:** Site-installed products with site-dependent timing.
- **Description:** Partner submits site readiness checklist 5 business days before scheduled install. Silver tier: self-certified. Gold: manufacturer technical review. Platinum: manufacturer PM co-sign. Installation order release blocked until readiness confirmed.
- **Lead time:** 60 days to template, 90 days to enforcement.

### Play: Storage SLA with Teeth

- **Source:** Industry standard B2B premium equipment [E-07]
- **Applicability:** Any manufacturer holding inventory after partner delay.
- **Description:** Free storage = 7 working days after notification of readiness for collection. After that, €/day per SKU automatically posted to partner account. No manual invoicing.
- **Lead time:** 30 days (the policy exists in most contracts; activation is the work).

### Play: Handover → Install Base

- **Source:** Daikin install-base monetization model [E-11]
- **Applicability:** Long-life capital equipment with downstream service revenue.
- **Description:** Handover is not complete until: signed installation report, commissioning cert, end-user training record, warranty registration, end-customer contact captured. Each item is a database field, not a paragraph.
- **Lead time:** 90 days to define, 6 months to enforce 95% completeness.

### Play: AR Hard Block

- **Source:** Cisco partner agreement model [E-03]
- **Applicability:** Any partner program with recurring transactions.
- **Description:** AR > 30 days overdue automatically suspends new order processing. Suspension lifts within 24h of payment receipt. No human override; exceptions require VP approval and are logged.
- **Lead time:** 30 days to system change, 60 days to partner education.

### Play: NPS Trigger to End-Customer

- **Source:** Existing manufacturer practice + ELG "pierce the veil" principle [E-01]
- **Applicability:** Any manufacturer with partner-installed product reaching end-customer.
- **Description:** Manufacturer calls end-customer within 7 days of confirmed handover. Bypasses partner filter on customer voice. Data feeds Stage 6 (Renew) decisions.
- **Lead time:** Immediate if already happening; 90 days otherwise.

## KPIs

| KPI | Formula | Silver target | Gold target | Platinum target | Source |
|---|---|---|---|---|---|
| Spec-complete PO rate | Orders accepted without revision ÷ total orders | 80% | 90% | 95% | [E-08] |
| Order confirmation SLA | % confirmed within 24h | 95% | 95% | 99% | [E-03] |
| On-time delivery | % delivered within confirmed window | 85% | 90% | 95% | [E-07] |
| Site readiness on time | % checklists submitted 5+ business days before install | 85% | 95% | 100% | [E-08] |
| DSO | Days sales outstanding | 60 | 45 | 30 | [E-03] |
| AR overdue rate | % AR aged > 30 days | <10% | <5% | 0% | [E-04] |
| Handover doc completeness | % of required fields populated | 90% | 95% | 100% | [E-04] |
| Install base capture rate | Serials registered ÷ units shipped | 90% | 95% | 100% | [E-11] |
| Project margin protection | Actual margin ÷ quoted margin at handover | ≥95% | ≥97% | ≥98% | [E-08] |

## RACI within the stage

| Activity | Manufacturer | Partner | End-Customer |
|---|---|---|---|
| Order placement | I | R, A | C |
| Contract execution | C (templates only; co-sign for Global Accounts) | R, A | R |
| Order confirmation | R, A | I | I |
| Manufacturing + outbound logistics | R, A | R (inbound from warehouse) | C |
| Storage and site staging | C | R, A | R (provides storage area) |
| Financial milestones | A | R | A |
| Site readiness verification | C/R (tier-dependent) | R, A | R |
| Installation release | A | R | I |
| Handover and documentation | R (NPS, registration) | R, A | A |

## Source mapping

Principles from `appendix/evidence-library.md` that primarily apply to this stage:
- P-16 (Operations as ecosystem maturity indicator)
- P-17 (Digital order placement as baseline)
- P-18 (One process, local exceptions)
- P-19 (Site readiness hard gate)
- P-20 (AR overdue = automatic block)
- P-21 (Handover as data transfer)
- P-22 (Storage SLA with teeth)
- P-23 (NPS as manufacturer-direct channel)

Secondary alignment: P-36 (governance), P-42 (data layer), P-44 (install base).
