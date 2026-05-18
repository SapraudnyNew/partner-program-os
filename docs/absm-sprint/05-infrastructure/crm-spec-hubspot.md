# CRM Specification — HubSpot (Axians ABSM Program)

---

## Pipeline structure

**Pipeline name:** Axians–Akamai Guardicore

| Stage | Probability | Definition |
|---|---|---|
| Identified | 5% | Account in program; no contact yet |
| Contacted | 10% | First outreach sent |
| Meeting scheduled | 20% | Call or meeting confirmed |
| Technical briefing | 35% | Technical session completed; interest confirmed |
| POC proposed | 50% | POC proposal submitted or agreed |
| POC in progress | 65% | Active POC running |
| Proposal submitted | 75% | Commercial proposal sent |
| Verbal yes | 85% | Verbal commitment; legal review |
| Closed won | 100% | Signed |
| Closed lost | 0% | Opportunity ended |

---

## Custom properties (deal level)

| Property | Type | Options |
|---|---|---|
| ICP score | Number | 0–30 |
| Primary trigger | Dropdown | NIS2 / TISAX / Post-incident / OT convergence / SAP migration |
| Guardicore deployment scope | Text | OT-only / IT-only / Hybrid |
| Competitor at account | Dropdown | Illumio / PANW / Cisco / None / Unknown |
| MDF activated | Yes/No | — |
| MDF amount (€) | Number | — |
| Partner (Axians rep) | Contact | — |

---

## Custom properties (contact level)

| Property | Type |
|---|---|
| Decision-making role | Dropdown: CISO / CIO / Security Architect / Champion / Influencer |
| NIS2 awareness level | Dropdown: None / Aware / Actively addressing / Compliance project active |
| TISAX status | Dropdown: Not applicable / Required / Audit scheduled / Certified |
| Last meaningful interaction | Date |

---

## Reporting views

1. **Pipeline by stage** — where are the 4 accounts right now
2. **Activity by rep** — calls, emails, meetings per week
3. **Content engagement** — which PDFs/briefs were shared and opened (HubSpot tracking)
4. **MDF ROI** — cost per meeting, cost per opportunity, cost per closed deal

---

## Integration requirements

- **Akamai Partner Hub:** Sync deal registrations from HubSpot to Akamai deal registration system
- **Email tracking:** HubSpot email open/click tracking enabled for all program outreach
- **Meeting scheduling:** Calendly or HubSpot Meeting Links for first meeting booking

---

*May 2026 · Spec for Axians HubSpot instance setup*
