# Glossary and Stage Dependencies

---

## Glossary

| Term | Definition |
|---|---|
| ABSM | Account-Based Sales and Marketing. A structured sprint targeting specific high-value accounts through deep research, personalized outreach, and coordinated multi-stakeholder engagement. Sits within Stage 4 (Co-sell) as a separate execution stream. |
| ABM/TAS | Account-Based Marketing / Target Account Selection. The partner recruitment discipline embedded in Stage 1 (Recruit): Ideal Partner Profile, scoring matrix, 9-box prioritization, Target Account List. |
| Attach rate | Percentage of new equipment deliveries that include a service contract at point of sale. BCG benchmark: top performers attach 31% more than average. Stage 6 KPI. |
| DSO | Days Sales Outstanding. Average time to collect payment from partners. Stage 5 KPI. |
| GE/McKinsey 9-box | Portfolio prioritization grid with two axes (attractiveness vs strategic fit). Used in Stage 1 to classify partners into invest/maintain/exit tiers. |
| GCSE | Guardicore Certified Solutions Engineer. Akamai's technical certification for Guardicore Segmentation. |
| GCSP | Guardicore Certified Service Provider. Akamai's service delivery certification. |
| HVO | High-Value Offer. An executive value letter for a specific employer, built from the method. Layer 3 of the architecture. |
| ICP | Ideal Customer Profile. The target buyer definition used in ABSM campaigns. Not to be confused with IPP. |
| IPP | Ideal Partner Profile. The target partner definition used in Stage 1 (Recruit). Five dimensions: strategic fit, capability, market access, financial health, cultural alignment. |
| Install base | The register of all delivered and commissioned units with serial numbers, end-customer contacts, warranty terms, and service contract status. Created in Stage 5, maintained in Stage 6, consumed in Stage 7. |
| JBP | Joint Business Plan. A shared commitment between manufacturer and partner with revenue targets, campaign plans, and review cadence. Stage 4 artifact. |
| LSP | Local Service Provider. A partner type that installs, maintains, and services products post-sale. Revenue model: service fee + parts margin + service contract revenue. |
| MAP | Mutual Action Plan. A joint timeline with milestones, owners, and deliverables shared between manufacturer and target account during an ABSM campaign. Stage 4 artifact. |
| MDF | Market Development Funds. Budget allocated to partners for co-marketing campaigns. Requires pre-approved campaign brief with pipeline target and post-campaign ROI measurement. |
| MEDDPICC | Metrics, Economic Buyer, Decision Criteria, Decision Process, Paper Process, Identify Pain, Champion, Competition. Enterprise sales qualification framework used in ABSM Stage 2 (Deep Intel Profiler). |
| MTBC | Mean Time Between Callbacks. Average days between unplanned service calls. Elevator industry standard metric. Good: >365 days. |
| MTTR | Mean Time To Repair. Hours from failure report to operational restoration. Good: <4 hours (urban). |
| NRR | Net Revenue Retention. (Renewed + expansion - contraction - churn) / beginning period value. >100% means the installed base grows without new sales. Stage 6 KPI. |
| NPS | Net Promoter Score. Customer satisfaction metric captured at handover (Stage 5) and used as churn signal (Stage 6). |
| PRM | Partner Relationship Management. The system of record for partner profiles, tiers, deal registration, and portal experience. Technology category relevant across all seven stages. |
| RACI | Responsible, Accountable, Consulted, Informed. Role assignment matrix used in every stage to clarify who does what across manufacturer, partner, and end-customer. |
| SI | System Integrator. A partner type that designs, installs, and integrates products into larger solutions. Revenue model: project fee + product margin. |
| SPIFF | Sales Performance Incentive Fund. Bonus payments to individual partner sales reps for specific deal types or products. |
| Sweet Spot | The campaign theme selected in ABSM Stage 3 that best matches the pain patterns across target accounts. Defined by: name, thesis, target persona, anchor pain, proof points. |
| TAL | Target Account List. The ranked output of Stage 1 scoring: prioritized partners with scores, recommended approach per tier, assigned owner, and timeline. |
| XaaS | Anything-as-a-Service. Umbrella term for subscription-based delivery models: SaaS, equipment-as-a-service, monitoring-as-a-service. Stage 6 digital services context. |

---

## Stage dependency map

The seven stages are not independent. Each stage produces outputs that downstream stages consume. Running a stage without its upstream inputs produces incomplete results.

```
Stage 1: RECRUIT
  │ Output: signed partner, IPP score, partner type classification
  │ Feeds: Stage 2 (which partners to onboard), Stage 4 (account mapping data)
  ▼
Stage 2: ONBOARD
  │ Output: activated partner, completed training, first pipeline
  │ Feeds: Stage 3 (which partners need enablement), Stage 4 (ready-to-co-sell partners)
  ▼
Stage 3: ENABLE
  │ Output: certified partner, content library access, marketing motion capability
  │ Feeds: Stage 4 (co-sell readiness), Stage 6 (service certification)
  ▼
Stage 4: CO-SELL ◄──────────────── Stage 1 (account mapping data)
  │ Output: pipeline, closed deals, ABSM campaigns
  │ Feeds: Stage 5 (signed orders to deliver)
  │ Receives from: Stage 6 (retrofit/modernization opportunities), Stage 7 (expansion deals)
  ▼
Stage 5: DELIVER
  │ Output: installed product, install base data, NPS score
  │ Feeds: Stage 6 (every field in the install base register)
  ▼
Stage 6: RENEW ◄──────────────── Stage 5 (install base data)
  │ Output: service revenue (7 streams), churn data, retrofit/modernization pipeline
  │ Feeds: Stage 7 (cross-sell recommendations, coverage gaps, lifecycle triggers)
  │ Feeds back to: Stage 4 (modernization deals re-enter co-sell pipeline)
  ▼
Stage 7: EXPAND ◄──────────────── Stage 6 (install base + service data)
  │ Output: new products per partner, new segments, new geographies
  │ Feeds back to: Stage 1 (coverage gaps requiring new partner recruitment)
  └──────────────────────────────► Stage 1 (recruitment triggered by coverage gaps)
```

**Critical dependencies:**

- Stage 6 cannot function without Stage 5 install base data. If handover does not capture serial numbers, end-customer contacts, and contract status, the entire service business operates blind.
- Stage 7 cannot function without Stage 6 service data. Cross-sell recommendations, retrofit triggers, and modernization timing all depend on install base and service history.
- Stage 4 ABSM campaigns require Stage 3 enablement (content, certification) and Stage 1 account mapping data.
- Stage 6 retrofit and modernization opportunities feed back into Stage 4 as co-sell pipeline. This creates a revenue loop: deliver, service, identify expansion, co-sell the expansion, deliver again.

**The revenue loop:** Stages 4 → 5 → 6 → 7 → 4 form a reinforcing cycle. Each pass through the loop adds revenue and deepens the customer relationship. The maturity of the loop determines whether the partner program grows linearly (one pass) or compounds (multiple passes per customer).
