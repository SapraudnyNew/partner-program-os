# CRM Specification — HubSpot Configuration for the Partner Intelligence Program

> **Stage 5 Infrastructure · D3-2 ABSM Sprint**
> **CRM platform:** HubSpot (confirmed via cookie tracking on axians.de)
> **Purpose:** Define the HubSpot configuration required to operationalize the PIP at Axians, including deal object structure, automation, and Akamai data ingestion.

---

## Context: Why HubSpot and Why This Configuration

Axians uses HubSpot as its primary CRM (confirmed by HubSpot cookie presence on axians.de). The PIP requires HubSpot to do three things it doesn't currently do:

1. **Receive intent-signal-routed accounts** from Akamai (via HubSpot API or CSV import)
2. **Attach account intelligence packages** to Company and Deal objects as structured data
3. **Trigger cross-portfolio routing workflows** when an intent-routed account matches an existing Axians customer

---

## HubSpot Object Model for the PIP

### 1. Company Object — PIP-Specific Custom Properties

Add the following custom properties to the HubSpot Company object:

| Property name | Type | Values | Purpose |
|---------------|------|--------|---------|
| `pip_target` | Boolean | Yes/No | Whether this company is in the active PIP target universe |
| `pip_nis2_status` | Single-line text | "Essential entity" / "Important entity" / "Unclear" / "Not in scope" | NIS2 classification |
| `pip_axians_relationship` | Dropdown | "None" / "NEO Solutions" / "IT Security" / "Network" / "Cloud" / "Multiple" | Existing Axians portfolio engagement |
| `pip_primary_contact_linkedin` | URL | LinkedIn profile URL | CISO / IT Security lead verified contact |
| `pip_intent_score` | Number (0–100) | Akamai 6sense composite score | Monthly update from Akamai |
| `pip_triple_obligation` | Checkbox list | NIS2 / KRITIS cascade / TISAX | Which obligation layers apply |
| `pip_incumbent_seg_vendor` | Single-line text | e.g., "Illumio", "None known", "NSX" | Known competitive situation |
| `pip_intel_kit_url` | URL | Link to account intel folder | Axians-accessible drive link |

### 2. Deal Object — PIP Deal Stage Mapping

Map the PIP buying stages to HubSpot deal stages in the IT Security pipeline:

| HubSpot Stage | PIP Stage | Exit criteria |
|---------------|-----------|---------------|
| PIP Routed | 0 — Unaware | Account intel kit assigned; AE reviewed |
| First Contact Sent | 1 — Aware | First LinkedIn/email touch sent |
| Meeting Booked | 1→2 — Considering | Meeting confirmed in calendar |
| Discovery Complete | 2 — Considering | Pain confirmed; budget holder identified |
| POC Proposed | 2→3 — Evaluating | POC scope doc sent and under review |
| POC In Progress | 3 — Evaluating | Guardicore deployed in test environment |
| Business Case Submitted | 3→4 — Deciding | Formal ROI doc submitted to CFO/CIO |
| Verbal Commit | 4 — Deciding | Verbal approval from budget holder |
| Closed Won | 5 — Live | Contract signed; deployment started |
| Closed Lost | — | Record reason: Illumio / No budget / Timing / Other |

Custom deal properties to add:

| Property | Type | Purpose |
|----------|------|---------|
| `pip_account_type` | Dropdown | "Warm path (cross-portfolio)" / "Cold (direct)" / "Showcase" |
| `pip_guardicore_arp` | Currency | Annual recurring price agreed |
| `pip_deployment_scope` | Multi-select | "Germany only" / "EU" / "Global" / "OT only" / "IT + OT" |
| `pip_axians_portfolio_referrer` | Single-line text | Which Axians portfolio made the intro (e.g., "NEO Solutions — Hörmann") |

### 3. Association: Company → Axians Account Manager

For cross-portfolio routing, create an Association between the Company object and the Axians employee who currently manages the relationship:

- `axians_neo_am` — User lookup (Axians NEO account manager)
- `axians_it_security_ae` — User lookup (IT Security AE assigned)

This enables automated notification workflows.

---

## Automation Workflows

### Workflow 1 — Monthly PIP Account Import

**Trigger:** Akamai delivers "Hot 20 DACH Accounts" CSV on the first business day of each month.

**Steps:**
1. Import CSV via HubSpot API (`/crm/v3/objects/companies`) — creates or updates Company objects
2. Set `pip_target = Yes` and `pip_intent_score` from import
3. Check if `pip_axians_relationship` ≠ "None" — if match found, trigger Workflow 2
4. Enroll all new PIP-target companies in Deal pipeline at stage "PIP Routed"
5. Assign `axians_it_security_ae` based on account geography (NRW accounts → NRW AE, BW accounts → BW AE, etc.)
6. Send AE notification email with link to account intel kit

### Workflow 2 — Cross-Portfolio Routing Alert

**Trigger:** Company object has both `pip_target = Yes` AND `pip_axians_relationship` ≠ "None"

**Steps:**
1. Email to `axians_it_security_ae` AND `axians_neo_am` simultaneously
2. Subject: "PIP Cross-Portfolio Alert: [Company Name] — existing relationship + Guardicore opportunity"
3. Body includes: company name, NIS2 status, triple obligation flags, existing relationship type, primary CISO contact name
4. Creates a shared task: "Schedule cross-portfolio intro call within 10 business days"
5. Logs all activities on the Company object timeline

### Workflow 3 — POC Milestone Notification

**Trigger:** Deal stage moves to "POC In Progress"

**Steps:**
1. Notify Akamai overlay (channel manager) via email
2. Create 30-day countdown task: "POC review meeting with [Company Name] + [CISO contact]"
3. Attach Guardicore POC documentation kit from linked Google Drive
4. Set deal `closedate` = 90 days from POC start (default close timeline)

### Workflow 4 — Competitive Alert

**Trigger:** `pip_incumbent_seg_vendor` updated to "Illumio"

**Steps:**
1. Notify AE: "Competitive deal — Illumio identified at [Company Name]"
2. Attach competitive battlecard (PDF-07 link)
3. Tag deal with `competitive = True` for pipeline reporting
4. Alert Axians IT Security practice lead for deal support

---

## Account Intel Kit — Attachment Structure

For each PIP account, create a Google Drive folder and link it via `pip_intel_kit_url`:

```
[COMPANY NAME] — Guardicore PIP Kit/
├── 01-company-brief.md
├── 02-pain-map.md
├── 03-relationship-map.md
├── 04-axians-connection.md
├── XX-executive-brief.pdf       (Stage 4 PDF)
├── ASSETS/
│   ├── 01-nis2-segmentation-brief.pdf
│   ├── 02-triple-obligation-poster.pdf
│   └── [other relevant Stage 4 PDFs]
└── OUTREACH/
    └── email-sequence.txt
```

This structure mirrors the ABSM sprint deliverable format exactly.

---

## Reporting Dashboard (HubSpot)

Create a PIP Pipeline dashboard with the following reports:

| Report | Metric | Filter |
|--------|--------|--------|
| PIP Funnel | Count of deals per stage | `pip_target = Yes` |
| Cross-portfolio velocity | Time from "PIP Routed" to "Meeting Booked" | `pip_account_type = Warm path` |
| Cold vs warm conversion | % of warm-path vs cold accounts reaching POC | Both types |
| Intent score distribution | Histogram of `pip_intent_score` | All PIP accounts |
| ARR by deal type | Sum of `pip_guardicore_arp` | Won deals only |
| Competitive loss rate | % lost to Illumio | `competitive = True`, `Closed Lost` |

---

## Implementation Timeline

| Week | Activity |
|------|----------|
| 1 | Add custom properties to Company and Deal objects |
| 2 | Configure deal pipeline stages |
| 3 | Build Workflows 1–4 and test with sample data |
| 4 | Connect Akamai 6sense API (or set up CSV import routine) |
| 5 | Create reporting dashboard; train AEs |
| 6 | First live monthly import — "Hot 20 DACH Accounts" |

---

**End of CRM specification.**
