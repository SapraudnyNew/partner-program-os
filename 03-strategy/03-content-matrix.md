# Content Matrix

> **Stage 3 Strategy · D3-2 ABSM Sprint**
> **Purpose:** Map which content asset goes to which role at which stage of the buying journey. Guides Stage 4 execution arsenal curation and informs the Axians IT Security AE on how to sequence materials.

---

## Buying Stages Defined

| Stage | Name | What the buyer is doing | Guardicore conversation objective |
|-------|------|------------------------|-----------------------------------|
| 0 | **Unaware** | Not thinking about microsegmentation | Create awareness; connect to NIS2/TISAX obligation |
| 1 | **Aware** | Knows there's a compliance gap; hasn't prioritized | Drive urgency; show that the gap is quantifiable |
| 2 | **Considering** | Actively evaluating security architecture options | Win the shortlist; differentiate from Illumio/NSX |
| 3 | **Evaluating** | Running a POC or RFP | Win the technical and business evaluation |
| 4 | **Deciding** | Executive sign-off | Close the deal; manage procurement |
| 5 | **Live** | Deployed and running | Expand; get the reference |

Most DACH Mittelstand accounts enter the funnel at Stage 0 or 1. The PIP architecture is designed to surface them at Stage 1 (intent signals) and bring them to Stage 2 (first meeting) within 4–6 weeks.

---

## The Roles and What They Need

| Role | Primary question | Pain pattern | What they need |
|------|-----------------|--------------|----------------|
| **CISO / Leiter IT Security** | "What does segmentation look like and how do we implement it?" | 2, 1, 3 | Technical credibility + peer references |
| **IT Infrastructure Lead** | "Will this break my network? Who deploys it?" | 2, 8 | Agentless story + deployment guide |
| **CIO** | "What does it cost, what does it deliver, and how does it fit the roadmap?" | 8, 7 | Business case + ROI framing |
| **CDO / Digital Lead** | "Does this work in our cloud environment and smart factory?" | 3, 6 | Architecture brief + cloud-native story |
| **MD / Geschäftsführer (Mittelstand owner)** | "Why now? What happens if we don't?" | 1, 7 | One-page executive brief + risk framing |
| **Financial controller** | "Is the ROI real and what's the total cost?" | 7 | Forrester TEI + TCO model |
| **Plant manager / OT lead** | "Will this touch my machines?" | 3, 4 | Agentless OT brief + NVIDIA BlueField story |
| **Procurement/Legal** | "What are the contract terms, data residency, GDPR?" | — | EU/GDPR data sheet + DPA template |

---

## Content Matrix — The Full Grid

### Stage 0 → 1 (Awareness to Urgency)

Goal: Make the account understand they have a measurable problem.

| Audience | Content | Format | Key message | Delivery channel |
|----------|---------|--------|-------------|-----------------|
| CISO / IT Sec lead | NIS2 Article 21 segmentation obligation briefing | 1-page PDF | "Article 21.5 and 21.9 both mandate network segmentation. Your registration deadline passed March 6, 2026." | LinkedIn DM + email |
| CISO / IT Sec lead | DACH Mittelstand manufacturer NIS2 readiness survey (Axians data) | Infographic | "Only 38.5% of obligated entities registered by the March 2026 deadline — are you on the BSI list?" | Email + event handout |
| MD / Owner | Cyber insurance requirements 2025/26 market brief | 1-page PDF | "Insurers are requiring documented segmentation for coverage renewal. What does your renewal say?" | Executive event |
| CIO | SAP S/4HANA migration segmentation risk brief | 2-page PDF | "The most common lateral movement path during S/4HANA migrations runs from corporate IT to legacy ECC to production OT." | CIO roundtable, event |
| Plant manager | KRITIS-Dachgesetz physical + cyber security brief | 1-page | "Your production systems are part of your customers' KRITIS compliance picture." | Trade association |

---

### Stage 1 → 2 (Urgency to Active Consideration)

Goal: Make Guardicore the natural first call when the buying process starts.

| Audience | Content | Format | Key message | Delivery channel |
|----------|---------|--------|-------------|-----------------|
| CISO / IT Sec lead | Guardicore product overview for manufacturing | 4-page PDF | "Discover first, enforce never-without-permission. Works with your legacy PLCs, your KUKA robots, your SAP." | Email or first meeting handout |
| CISO + CIO | Forrester TEI — Akamai Guardicore (152% ROI, $9.6M, 6-month payback) | Analyst report | "A manufacturer similar to yours — €1B revenue, 5,000 employees — showed this return." | Meeting / email follow-up |
| IT Infrastructure Lead | "How Guardicore deploys without touching your machines" — agentless brief | 1-page technical | "No agents on PLCs. No downtime. First 6 weeks: observe only." | First technical call |
| OT lead | NVIDIA BlueField + Guardicore agentless OT brief | 1-page technical | "Now GA Q2 2026 — segment OT assets that can't run agents." | First technical call + Hannover Messe |
| MD / Geschäftsführer | Account-specific one-page executive brief | Custom 1-page (Stage 4 asset) | Account-specific: Hörmann / MR / Witte version | Through Axians relationship |

---

### Stage 2 → 3 (Consideration to Evaluation)

Goal: Get a POC started.

| Audience | Content | Format | Key message | Delivery channel |
|----------|---------|--------|-------------|-----------------|
| CISO + IT Infra | POC proposal and scope document | 2-page PDF | "30-day production network discovery at one site. No enforcement. Full visibility." | Meeting |
| CIO + Controller | Business case template (Mittelstand edition) | Excel + PDF | Inputs: number of workloads, # production sites, current manual audit hours. Outputs: 3-year NPV, insurance premium impact, audit cost reduction. | Email follow-up to CIO meeting |
| Technical team | Guardicore technical architecture — DACH Mittelstand reference architecture | Detailed PDF | SAP + OT + cloud hybrid; German language optional | Technical pre-sales engagement |
| CISO | Victorinox case study (Guardicore beats Illumio) | 1-page case study | "Stefan Epp, Head of IT Infrastructure at Victorinox, evaluated both platforms and chose Guardicore. Here's why." | Competitive qualification call |
| Whole buying team | Axians + Akamai + Guardicore joint capabilities brief | 2-page PDF | "Local German service delivery. ISG Leader. 65 locations. The full package." | Joint Axians/Akamai presentation |

---

### Stage 3 → 4 (Evaluation to Decision)

Goal: Win the business case and close.

| Audience | Content | Format | Key message | Delivery channel |
|----------|---------|--------|-------------|-----------------|
| CFO / Controller | Final business case with account-specific inputs | Custom PDF | ROI, NPV, payback period, insurance impact — specific to this customer | Formal proposal |
| CISO + Legal | GDPR / data residency fact sheet | 1-page | EU data processing; GDPR DPA template; no data leaves Germany without permission | Legal/procurement meeting |
| MD / Owner | Executive summary — why now, why Guardicore, why Axians | 1-page | "Risk-adjusted ROI is the highest of any security investment we've modeled for German Mittelstand this year." | Final executive meeting |
| IT team | Reference customer list (DACH manufacturing) | Confidential reference sheet | 2–3 customer names + contact offers for reference calls | Sales close |

---

### Stage 4 → 5 (Post-Decision)

Goal: Successful deployment and referenceable customer.

| Audience | Content | Format | Key message |
|----------|---------|--------|-------------|
| Project team | Deployment runbook (Axians-delivered) | Technical guide | Phased rollout; discover, label, policy draft, enforce |
| CISO | NIS2 Article 21 compliance documentation template | Word/PDF | "Here is how to document your Guardicore deployment in NIS2 audit terms" |
| CIO | Quarterly business review template | Presentation | Metrics: workloads segmented, policy violations caught, audit findings addressed |
| Marketing | Case study request (when customer is live 6+ months) | Case study brief | Co-authored with customer communications; Axians + Akamai joint attribution |

---

## Account-Specific Content Priorities

Based on Stage 2 intel, each account needs a different lead asset:

| Account | Stage 0→1 lead | Stage 1→2 lead | Stage 2→3 lead |
|---------|---------------|----------------|----------------|
| **Hörmann** | Cross-portfolio handoff brief (internal Axians) | "KRITIS-Dachgesetz + NIS2 + TISAX = triple obligation for door manufacturers" | BiSecur incident reference + "5 years later" narrative |
| **Reinhausen** | Industrie 4.0 → NIS2 segmentation obligation | Greenfield segmentation for Haslbach expansion | Victorinox case study (similar precision engineering peer) |
| **Witte Automotive** | TISAX 6.0 segmentation requirements brief | "What your OEM auditors are asking for in 2026" | Guardicore TISAX compliance documentation template |
| **Trumpf** | SAP S/4HANA migration risk + NIS2 combo | Smart factory segmentation architecture brief | ISO 27001 Annex A 8.22 compliance documentation |

---

## Content Gaps to Build in Stage 4

The following assets were needed across multiple accounts but **do not yet exist**. Stage 4 should produce them:

1. **German-language "NIS2 Article 21 Network Segmentation" one-pager** — currently no Axians-branded German asset
2. **Mittelstand business case template** — needs €1B/5,000 employee Forrester TEI localization
3. **TISAX 6.0 segmentation requirements explainer** — what exactly TISAX now requires; maps to Guardicore controls
4. **"Triple obligation" one-page poster** — visual showing how one segmentation deployment satisfies NIS2 + KRITIS cascade + TISAX
5. **OT segmentation brief (NVIDIA BlueField)** — German-language, manufacturing-specific, post-GA Q2 2026
6. **Axians × Akamai joint capabilities brief (German)** — ISG recognitions, SOC certifications, local delivery

These 6 assets are the production list for Stage 4.

---

**End of content matrix.**
