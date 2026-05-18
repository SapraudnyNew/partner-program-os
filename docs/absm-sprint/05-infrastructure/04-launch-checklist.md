# Launch Checklist — Partner Intelligence Program Go-Live

> **Stage 5 Infrastructure · D3-2 ABSM Sprint**
> **Program:** Axians × Akamai Guardicore PIP — DACH Sprint
> **Owner:** Axians IT Security Practice Lead + Akamai DACH Channel Manager
> **Target Go-Live:** Week 6 from sprint handoff

---

## How to Use This Checklist

Work through phases in order. Each phase has a gate — do not proceed until all items in the current phase are complete. Owner abbreviations:

- **AX-ISP** — Axians IT Security Practice Lead
- **AX-MKT** — Axians Marketing
- **AX-AE** — Axians Account Executive (territory-based)
- **AK-CM** — Akamai DACH Channel Manager
- **AK-SE** — Akamai Solutions Engineer

---

## Phase 0 — Stakeholder Alignment (Days 1–3)

> Gate: Axians IT Security leadership approves PIP launch and assigns owners.

- [ ] **AX-ISP** — Schedule kick-off call with Akamai DACH Channel Manager: confirm PIP scope, account list, MDF budget commitment
- [ ] **AX-ISP** — Assign AEs to accounts by territory:
  - Hörmann (Steinhagen NRW) → NRW AE
  - Witte Automotive (Velbert NRW) → NRW AE
  - Reinhausen (Regensburg BY) → BW/BY AE
- [ ] **AK-CM** — Confirm Hörmann as warm-path priority; brief Akamai overlay SE on NEO cross-portfolio play
- [ ] **AX-ISP** — Confirm Axians NEO contacts for Hörmann warm path: Alexandra Kempe (Projektleiterin Service VKG) + Lennard Eichler (Teamleiter Customer Cloud VKG)
- [ ] **AX-ISP** — Review all 12 Stage 4 PDFs and confirm Axians legal/compliance clearance for external distribution
- [ ] **AX-ISP + AK-CM** — Submit MDF pre-approval for Q1 activities (AE training, LinkedIn ads, roundtable)

**Phase 0 gate:** ☐ All items checked → proceed to Phase 1

---

## Phase 1 — HubSpot CRM Configuration (Days 4–10)

> Gate: HubSpot is configured and tested with sample data before any accounts are loaded.

### 1A — Company Object Setup
- [ ] **AX-MKT** — Add custom property `pip_target` (Boolean) to Company object
- [ ] **AX-MKT** — Add `pip_nis2_status` (Dropdown: Essential entity / Important entity / Unclear / Not in scope)
- [ ] **AX-MKT** — Add `pip_axians_relationship` (Dropdown: None / NEO Solutions / IT Security / Network / Cloud / Multiple)
- [ ] **AX-MKT** — Add `pip_primary_contact_linkedin` (URL)
- [ ] **AX-MKT** — Add `pip_intent_score` (Number 0–100)
- [ ] **AX-MKT** — Add `pip_triple_obligation` (Checkbox: NIS2 / KRITIS cascade / TISAX)
- [ ] **AX-MKT** — Add `pip_incumbent_seg_vendor` (Single-line text)
- [ ] **AX-MKT** — Add `pip_intel_kit_url` (URL)

### 1B — Deal Object Setup
- [ ] **AX-MKT** — Create "Guardicore PIP" deal pipeline (separate from existing Axians pipelines)
- [ ] **AX-MKT** — Configure 9 deal stages: PIP Routed / First Contact Sent / Meeting Booked / Discovery Complete / POC Proposed / POC In Progress / Business Case Submitted / Verbal Commit / Closed Won
- [ ] **AX-MKT** — Add lost reasons: Illumio / No budget / Timing / No executive sponsor / Other
- [ ] **AX-MKT** — Add `pip_account_type` (Dropdown: Warm path / Cold direct / Showcase)
- [ ] **AX-MKT** — Add `pip_guardicore_arp` (Currency — annual recurring price)
- [ ] **AX-MKT** — Add `pip_deployment_scope` (Multi-select)
- [ ] **AX-MKT** — Add `pip_axians_portfolio_referrer` (Single-line text)

### 1C — Association Setup
- [ ] **AX-MKT** — Add `axians_neo_am` user lookup association on Company object
- [ ] **AX-MKT** — Add `axians_it_security_ae` user lookup association on Company object
- [ ] **AX-MKT** — Set Alexandra Kempe as `axians_neo_am` for Hörmann Company record

### 1D — Workflow Configuration
- [ ] **AX-MKT** — Build Workflow 1: Monthly PIP Account Import (CSV trigger → Company update → Deal creation → AE notification)
- [ ] **AX-MKT** — Build Workflow 2: Cross-Portfolio Routing Alert (trigger: pip_target=Yes AND pip_axians_relationship≠None)
- [ ] **AX-MKT** — Build Workflow 3: POC Milestone Notification (trigger: deal stage = POC In Progress)
- [ ] **AX-MKT** — Build Workflow 4: Competitive Alert (trigger: pip_incumbent_seg_vendor = "Illumio")
- [ ] **AX-MKT** — Test Workflow 2 with Hörmann test record (should fire immediately — pip_axians_relationship = "NEO Solutions")

### 1E — Reporting Dashboard
- [ ] **AX-MKT** — Create "PIP Pipeline" dashboard with 6 reports (PIP funnel / cross-portfolio velocity / cold vs warm conversion / intent score distribution / ARR by deal type / competitive loss rate)
- [ ] **AX-MKT** — Share dashboard access with: AX-ISP, NRW AE, BY AE, AK-CM

**Phase 1 gate:** ☐ All items checked; Workflow 2 test fire confirmed → proceed to Phase 2

---

## Phase 2 — Account Intel Kit Deployment (Days 8–12)

> Gate: All 4 accounts have complete intel kits in Google Drive with HubSpot links attached.

### 2A — Google Drive Folder Structure
- [ ] **AX-ISP** — Create Google Drive parent folder: "Axians Guardicore PIP — DACH Sprint" with Axians IT Security team access
- [ ] **AX-ISP** — Create sub-folder for each account: Hörmann / Reinhausen / Witte Automotive / Trumpf (showcase)

### 2B — Hörmann Intel Kit
- [ ] **AX-AE (NRW)** — Upload to Drive: hoermann-company-brief.md, hoermann-pain-map.md, hoermann-relationship-map.md, hoermann-axians-connection.md
- [ ] **AX-AE (NRW)** — Upload: 08-hoermann-executive-brief.pdf + relevant Stage 4 PDFs (01, 02, 04, 05, 07)
- [ ] **AX-AE (NRW)** — Set `pip_intel_kit_url` on Hörmann Company record in HubSpot
- [ ] **AX-AE (NRW)** — Verify Rian Redinger LinkedIn URL is set in `pip_primary_contact_linkedin`
- [ ] **AX-AE (NRW)** — Confirm Hörmann `pip_axians_relationship = NEO Solutions`; verify Workflow 2 fires

### 2C — Reinhausen Intel Kit
- [ ] **AX-AE (BY)** — Upload intel files; link executive brief (PDF-09)
- [ ] **AX-AE (BY)** — Set `pip_intel_kit_url` on Reinhausen record
- [ ] **AX-AE (BY)** — Note: Dr. Feyrer is public author — LinkedIn contact approach; attach relevant content (PDF-01, PDF-04)

### 2D — Witte Automotive Intel Kit
- [ ] **AX-AE (NRW)** — Upload intel files; link executive brief (PDF-10)
- [ ] **AX-AE (NRW)** — Set `pip_intel_kit_url` on Witte record
- [ ] **AX-AE (NRW)** — Flag: Christian Kaczmarczyk (former CTO) left July 2025 — technology leadership in transition; confirm Patrick Demant's current mandate before outreach
- [ ] **AX-AE (NRW)** — Verify `pip_triple_obligation` = NIS2 + TISAX (Witte is NOT KRITIS-direct; remove if previously set)

### 2E — Trumpf Showcase Record
- [ ] **AX-ISP** — Create Trumpf Company record with `pip_account_type = Showcase`
- [ ] **AX-ISP** — Upload trumpf intel kit; link PDF-11
- [ ] **AX-ISP** — Flag: Trumpf is above ICP band (€4.3B); editorial / aspirational only — no active outreach without partner approval

**Phase 2 gate:** ☐ All 4 intel kits uploaded; HubSpot links set; Hörmann Workflow 2 confirmed → proceed to Phase 3

---

## Phase 3 — Sales Enablement (Days 10–17)

> Gate: AEs are trained and ready to execute outreach.

### 3A — AE Training Workshop
- [ ] **AK-SE** — Deliver Guardicore technical training: agentless OT, Illuminate platform, NVIDIA BlueField GA Q2 2026 roadmap
- [ ] **AX-ISP** — Deliver PIP account briefings: run through Hörmann, Reinhausen, Witte pain maps
- [ ] **AX-ISP** — Deliver competitive handling workshop: Illumio objections, Victorinox displacement story
- [ ] **AX-AE** — Complete 2-question Guardicore qualification quiz (pass mark: both correct)
- [ ] **AX-ISP** — Walk AEs through HubSpot PIP pipeline; demonstrate Workflow 2 alert

### 3B — Outreach Materials Distribution
- [ ] **AX-ISP** — Distribute to each AE: full Stage 4 PDF kit (12 PDFs) + account-specific executive brief
- [ ] **AX-ISP** — Confirm all AEs have physical or digital battlecard access (PDF-07)
- [ ] **AX-AE (NRW)** — Write personalized LinkedIn connection note for Rian Redinger (Hörmann CISO); review with AX-ISP before sending
- [ ] **AX-AE (NRW)** — Write personalized LinkedIn connection note for Rainer Schulten (Witte); review with AX-ISP before sending
- [ ] **AX-AE (BY)** — Identify Dr. Feyrer's most recent public article; prepare content-led outreach opening

### 3C — Warm Path Coordination — Hörmann
- [ ] **AX-ISP** — Schedule internal call: NRW AE + Alexandra Kempe (NEO Solutions) + Lennard Eichler
- [ ] **AX-ISP** — Brief Kempe/Eichler on IT Security cross-portfolio play; confirm they are comfortable with intro email
- [ ] **AX-AE (NRW)** — Draft intro email from Kempe to Rian Redinger (Hörmann CISO); send for Kempe approval
- [ ] **AX-AE (NRW)** — Confirm intro meeting date within 10 business days of email send

**Phase 3 gate:** ☐ AEs trained and quizzed; Hörmann warm-path intro email approved and sent → proceed to Phase 4

---

## Phase 4 — Digital & Marketing Activation (Days 12–20)

> Gate: Digital channels live; MDF pre-approvals confirmed.

### 4A — LinkedIn ABM Campaign
- [ ] **AX-MKT** — Create LinkedIn Campaign Manager audience: NRW/BW/BY · 1K–10K employees · IT/Security · Director+ · Manufacturing
- [ ] **AX-MKT** — Upload Triple Obligation creative (adapted from PDF-02); test 2 headline variants
- [ ] **AX-MKT** — Set UTM parameters → HubSpot form → auto-tag `pip_target = Yes`
- [ ] **AX-MKT** — Submit MDF pre-approval to AK-CM for LinkedIn spend (Q1 allocation: €1,500)
- [ ] **AX-MKT** — Set weekly spend cap: €300; review at 2-week mark

### 4B — Email Nurture Setup
- [ ] **AX-MKT** — Build 3-touch sequence in HubSpot Email
- [ ] **AX-MKT** — Configure personalization tokens: {{contact.firstname}}, {{company.name}}, primary obligation tag
- [ ] **AX-MKT** — QA all three emails (test send to AX-ISP)
- [ ] **AX-MKT** — Enroll Hörmann, Reinhausen, Witte contacts in sequence (**only after** Phase 3 warm-path intro is sent for Hörmann — do not run parallel campaigns)

### 4C — MDF Pre-Approvals
- [ ] **AX-MKT + AK-CM** — Submit pre-approval: NRW Automotive Roundtable (Month 3 · €3,000 MDF)
- [ ] **AX-MKT + AK-CM** — Submit pre-approval: NIS2 whitepaper (Month 4 · €2,000 MDF)
- [ ] **AK-CM** — Confirm Victorinox case study reference rights (required before 4.D)

### 4D — Victorinox Case Study Localization (if approved)
- [ ] **AX-MKT** — Engage Axians design team for German-language layout
- [ ] **AK-CM** — Provide Akamai-approved English source text + Stefan Epp quote approval
- [ ] **AX-MKT** — Deliver final PDF to AX-AEs for use in Hörmann and Witte conversations

**Phase 4 gate:** ☐ LinkedIn campaign live; email sequence built and QA'd; MDF pre-approvals submitted → proceed to Phase 5

---

## Phase 5 — Ongoing Operations (Month 2+)

> Recurring operational cadence once program is live.

### Weekly
- [ ] **AX-AE** — Update HubSpot deal stage for all active PIP accounts (every Monday)
- [ ] **AX-ISP** — Review PIP Pipeline dashboard; flag any deals stalled >2 weeks without activity
- [ ] **AX-AE** — Log all outreach touches on Company object timeline in HubSpot (no dark activity)

### Monthly
- [ ] **AK-CM** — Deliver "Hot 20 DACH Accounts" intent data CSV (first business day of month)
- [ ] **AX-MKT** — Import CSV via HubSpot API; verify Workflow 1 fires correctly
- [ ] **AX-ISP + AK-CM** — Monthly PIP sync call: pipeline review, blockers, upcoming events
- [ ] **AX-MKT** — Pull cross-portfolio velocity report: time from PIP Routed to Meeting Booked for warm vs cold

### Quarterly
- [ ] **AX-ISP + AK-CM** — QBR (Quarterly Business Review): ARR pipeline, MDF utilization, POC status, Win/Loss review
- [ ] **AX-MKT** — Submit MDF claims for prior quarter activities (deadline: 30 days after quarter close)
- [ ] **AX-ISP** — Refresh account intel kits with new Exa research on active accounts
- [ ] **AX-ISP** — Evaluate account scores; add/remove accounts from active PIP universe based on pipeline activity

---

## Escalation Matrix

| Situation | Escalate To | SLA |
|-----------|------------|-----|
| HubSpot workflow not firing | AX-MKT + HubSpot support | 24 hours |
| Hörmann warm path blocked (Kempe/Eichler unavailable) | AX-ISP direct outreach to Rian Redinger | 5 business days |
| Competitive deal (Illumio identified) | AK-CM + Axians IT Security Practice Lead | 48 hours |
| MDF pre-approval rejected | Resubmit with stronger ROI justification; AK-CM to escalate to Akamai DACH Partner Manager | 5 business days |
| POC scope creep / technical blocker | AK-SE overlay; escalate to Akamai Channel Manager | 48 hours |
| Trumpf opportunity opens unexpectedly | AX-ISP + AK-CM joint plan; Trumpf is above ICP — requires partner leadership approval | 24 hours |

---

## Program Readiness Sign-Off

Before first external outreach, confirm all Phase 0–4 items are complete:

| Workstream | Owner | Sign-Off Date |
|-----------|-------|--------------|
| HubSpot CRM configured and tested | AX-MKT | |
| Account intel kits uploaded | AX-ISP | |
| AEs trained + quizzed | AX-ISP | |
| Hörmann warm-path intro email approved | NRW AE | |
| LinkedIn campaign live | AX-MKT | |
| MDF pre-approvals submitted | AX-MKT + AK-CM | |
| Akamai partner portal updated with PIP accounts | AK-CM | |

**Program declared live when all 7 sign-offs are complete.**

---

**End of launch checklist.**
