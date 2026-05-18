# 00 · Context Architect

> **Stage 0 deliverable** · D3-2 ABSM Sprint · Akamai DACH Partner Project
> **Date:** 2026-05-18 · **Sprint version:** 2.0
>
> This document is the foundation of the sprint. Everything downstream — targeting, intel, strategy, execution — rests on what's defined here.

---

## Sprint Frame

**Partner:** Axians (formerly Fernao) — ICT brand of VINCI Energies
**Product:** Akamai Guardicore Segmentation
**Vertical:** German Mittelstand manufacturing (NIS2-obligated)
**Territory:** Germany
**Account band:** €100M–€2B revenue · 1,000–10,000 employees · below Akamai direct coverage
**Showcase account:** Trumpf GmbH (Ditzingen, BW)

---

## 1 · Partner Brief — Axians

### Identity

Axians is the ICT brand of VINCI Energies, the €18B+ industrial conglomerate's technology arm. Axians describes itself as part of "the global brand network for ICT solutions by VINCI Energies" with 16,000 specialists across 37 countries.

**Tagline:** "The best of ICT with a human touch"

**Positioning phrases observed in 2025–2026 campaigns:**
- "Secure. Connect. Empower." (it-sa 2025, post-Fernao integration campaign)
- "Industrial Solutions. Proven. Secured." (Hannover Messe 2026, with Actemium)
- "Keep IT simple and secure" (internal mantra)

### Germany footprint ✅

Axians in Deutschland operates an agile corporate network of specialized ICT service providers across 65 locations in Germany.

| Metric | Value | Source |
|--------|-------|--------|
| Revenue 2024 | €685M (DE) + €260M ex-Fernao = ~€945M combined | ⚠️ pre-research input |
| Employees | ~4,000 (DE post-integration) | ⚠️ pre-research input |
| German locations | 65 | ✅ axians.de |
| 2026 ranking | Top 3 in highest revenue class (>€1B) — "Bester IT-Dienstleister 2026" | ✅ |
| ISG Benchmark 2025 | Leader in 4 cyber categories: TSS, SSS, Next-Gen SOC/MDR, Next-Gen SOC/MDR – Midmarket | ✅ |

### The Fernao integration (open portfolio window)

The 2024 acquisition of fernao-Gruppe into the VINCI Energies group strengthened Axians' cybersecurity capacity. The full operational rebranding under the Axians brand was announced at **it-sa October 2025** under the "Secure. Connect. Empower." campaign. As of May 2026, integration is **ongoing but not complete** — many former Fernao customers and security capabilities are still being absorbed into the Axians portfolio. This is the **portfolio window** for adding Guardicore as a new line of defense.

The legacy Fernao brand persists at `axians-secure.de` (former Fernao Group security portal), explicitly addressing manufacturing pain: "Ob Automotive, Maschinenbau oder Prozessindustrie – in der Produktion darf es keinen Stillstand geben."

### Sister brand: Actemium ⚡ critical

Within the VINCI Energies ecosystem, **Actemium** is the industrial automation/OT specialist brand. Axians explicitly partners with Actemium for OT work: "Wir bei Axians kommen aus der IT-Welt und arbeiten dafür mit unserer Schwestermarke Actemium aus der OT-Welt zusammen."

The combination Axians (IT/cyber) + Actemium (OT/automation) at **Hannover Messe 2026 (April 20–24)** under the slogan "Industrial Solutions. Proven. Secured." with an **OT-Smart-Factory demo, AI applications, and interactive project showcases** in Hall 14, Stand J28, is the natural channel for Guardicore in manufacturing.

### Key people 🎯

| Name | Role | Confidence |
|------|------|------------|
| **Alain de Pauw** | Divisionsleiter IT Security Services DE + CH | ✅ axians.de press releases |
| **Jacques Diaz** | COO Axians Deutschland (returning April 1, 2026) | ✅ axians.de press release |
| **Burim Mirakaj** | CEO VINCI Energies DACH & CEE ICT | ✅ axians.com |
| **Martin Lutz** | Leader Cyber Squad & Deputy CISO – Central & Eastern Europe | ✅ ap-verlag interview |

### Portfolio (cyber-relevant)

From axians.de portfolio: Broadband & Carrier Solutions, Business Applications & Data Analytics, Business Resilience, Cloud & Data Center Infrastructures, Cyber Security, Digital Workspace, Enterprise Networks, Managed Services, SAP Solutions & Operations.

**Cyber Security sub-areas relevant to this sprint:**
- Industrial & OT Security (existing offering)
- Managed Security Services (10 European SOCs, 2 in Germany: Hamburg + Ulm)
- NIS2 consulting & implementation
- Zero Trust Network Access
- Network visibility & vulnerability management

**Already mentioned in their portfolio:** "Identity and Access Management (IAM), Mikrosegmentierung und IT/OT-SOC-Services" — microsegmentation is already in their vocabulary but they have no dominant vendor partnership for it. This is the white space Guardicore fills.

### Known Mittelstand customers — confirmed manufacturing references

From axians.de "Referenzen" gallery (✅ publicly displayed):
- **Viessmann Werke GmbH & Co. KG** (heating systems manufacturer, ~€4B revenue, family-owned)
- **Hörmann KG** (doors, gates manufacturer, ~€1.5B revenue)
- **HeidelbergCement AG** (now Heidelberg Materials, building materials, DAX 40)
- **Miele & Cie. KG** (premium appliances, ~€5B revenue, family-owned)
- **Phoenix Pharmahandel** (pharma distribution)
- **DB Stationsservice AG** (rail infrastructure)
- **Deutsche Messe AG / NürnbergMesse** (trade fair operators)
- **Avacon** (utility/KRITIS)
- **DE-CIX** (internet exchange)
- **Windcloud** (sustainable data center)

**Pre-research inputs (from sprint parameters):**
- Hochland SE (food manufacturing, Managed SOC)
- IAV GmbH (automotive engineering, network segmentation)
- Flughafen München (KRITIS)
- fischerwerke GmbH (manufacturing, security awareness)
- Anonymous Autoteile-Zulieferer (automotive OT segmentation in progress)

### Existing technology stack signals

- **No public Illumio partnership** (✅ verified — no Illumio mentions on axians.de)
- **No public Akamai partnership** (✅ verified — opportunity for new vendor relationship)
- **Marketing/CRM stack:** **HubSpot** confirmed (✅ cookie tracking on axians.de) — also LinkedIn tag
- **Premier VMware/Broadcom partner** (✅ Feb 2026 press release)
- **SAP Gold Partner** (✅ confirmed)
- **Strategic partners on website:** broad partner ecosystem, but no microsegmentation specialist named

---

## 2 · Market Brief — German Mittelstand Manufacturing × NIS2

### The NIS2 reality as of May 2026

The window for sales motion around NIS2 is wide open and getting wider. Key facts:

**Legislative status:**
- German NIS2 Implementation Act came into force on 6 December 2025 with no transition period
- Registration deadline with the BSI was 6 March 2026
- Approximately 29,850 entities in Germany are expected to fall within scope
- Only 11,500 had registered by the March 6 deadline — a registration rate of 38.5%
- That leaves **~18,000 obligated entities still non-compliant** as of May 2026

**Why manufacturing matters:**
- Covered sectors include: "Mechanical engineering; manufacture of motor vehicles; manufacture of medical devices; manufacture of electrical equipment"
- Most entities are in scope if they have >€10M turnover or >49 employees — meaning virtually all Mittelstand manufacturers qualify

**The sting:**
- Fines of up to EUR 10 million or, for large very important organizations, up to 2% of their annual turnover
- "Significant" incidents require an initial notice within 24 hours, a detailed report within 72 hours, and a final report
- Operators of critical facilities face additional obligations under §39 BSIG, including initial evidence of implementation no later than three years after the law comes into effect, i.e., from 2027, with ongoing evidence every three years thereafter

**The mismatch:** Companies are obligated to enforce risk management measures including network segmentation **today** (Article 21 of the EU Directive), but most have not started, and the BSI's audit cycle begins in 2027. This creates a 12–18 month sweet spot for an outreach motion that says: *"You have time to do this properly — but only if you start now."*

### The OT/IT convergence pain pattern

"Industrial enterprises must increasingly secure automation technologies and AI with OT security to avoid entry points for criminals — for example through Identity and Access Management (IAM), microsegmentation, and IT/OT SOC services. OT environments are already a popular target for attacks, and increasing networking continues to expand the attack surface. In 2023, a quarter of companies worldwide experienced at least one attack on OT environments"

The specific manufacturing pain pattern in 2026:
1. Industrie 4.0 digitalization brought OT systems onto TCP/IP networks
2. Most OT networks were originally air-gapped → now flat, with no internal segmentation
3. Legacy machine controllers (Siemens S7, Beckhoff, Rockwell PLCs) can't run security agents
4. A single compromised office laptop can now traverse the corporate network into the production floor — and shut down a factory
5. Cyber insurance premiums are rising; carriers are now requiring documented network segmentation as a condition of coverage
6. NIS2 Article 21 explicitly requires "network security" measures — but doesn't prescribe how, leaving CISOs with audit anxiety

### The Mittelstand sweet spot

The sprint's hard filter (€100M–€2B, 1K–10K employees) targets companies that are:
- **Large enough** to have a real OT footprint, a real CISO/IT security role, and budget authority for a six-figure security project
- **Small enough** to be below Akamai's direct sales coverage threshold (Akamai's named-account team typically focuses on DAX 40, larger MDAX, and KRITIS operators)
- **Conservative enough** to value a partner like Axians who can serve as the "trusted advisor with German engineers and local support" rather than a direct US-vendor relationship
- **Under regulatory pressure** from NIS2 to take action now

These are the "missing middle" accounts: too big to ignore, too small for Akamai to chase directly. Perfect partner territory.

---

## 3 · Product Brief — Akamai Guardicore Segmentation

### What it is

Akamai Guardicore Segmentation is a Zero Trust microsegmentation platform that "enforces precise segmentation policies with exposure-aware guidance — quickly, safely, and without disrupting the business. AI helps to map application dependencies and auto-label unknown assets for a single, real-time view of what's communicating in your network."

**One-line value proposition:** Stop ransomware and lateral movement inside the network — across hybrid IT, cloud, Kubernetes, and OT — without ripping out existing infrastructure.

### Core architecture — what makes it different

1. **Agent + agentless hybrid.** Includes both agent-based and agentless options. Agents are recommended for maximum visibility and control. Agentless is ideal for in-cloud PaaS, IoT, and OT environments.
2. **AI-driven labeling and policy.** As of March 2026: new AI-powered capabilities discover application behavior, generate explainable enforcement-ready policies, simulate impact, and validate readiness before enforcement.
3. **Single visualization across legacy, OT, and cloud.** Complete visibility across legacy, OT, and cloud systems through identification of known, unknown, and unmanaged assets.
4. **Legacy OS support.** Runs on old Windows Server, AIX, Solaris — assets that EDR/XDR vendors don't support. Critical for manufacturers with 10–20 year old line-of-business systems.

### The OT differentiator — Akamai + NVIDIA BlueField (Q2 2026 GA) ⚡

This is the headline news for the sprint:

Akamai and NVIDIA launched an agentless Zero Trust segmentation solution combining Akamai Guardicore Segmentation with NVIDIA BlueField DPUs to protect OT and ICS, including "un-agentable" industrial equipment. The hardware-isolated approach enforces real-time policies, improves visibility and anomaly detection, and is expected globally in Q2 2026.

Translation: for the first time, manufacturers can apply microsegmentation policy to PLCs, HMIs, and legacy machine controllers **without installing anything on them**. The policy is enforced in the network fabric via NVIDIA's data-processing unit. This solves the central technical objection ("we can't put agents on our Siemens controllers") and lands Q2 2026 — right when the sprint outreach hits inboxes.

### Proof points — Forrester TEI (Dec 2024)

The Forrester Total Economic Impact study is the single most powerful number-driven asset for business cases:

Forrester's Total Economic Impact of Akamai Guardicore Segmentation found:
- Total benefit of $9.6 million over 3 years
- 152% ROI
- Payback period of less than 6 months
- $4.1 million recouped via revenue retention from reduced downtime
- $2.9 million saved by reducing or eliminating legacy firewalls
- 33% fewer cybersecurity professionals needed (savings $1.4M over 3 years)
- 70% reduction in incident management effort by year 3

The composite organization in the study: a $1B revenue, 5,000-employee enterprise across 10 global locations — **almost exactly the Mittelstand profile of this sprint**.

### Customer references for content library

✅ **Confirmed manufacturing references for use in outreach:**

**Victorinox** — Swiss family-run manufacturer, 120+ countries, fourth-generation business Stefan Epp, Head of IT Infrastructure, evaluated both Illumio and Akamai Guardicore Segmentation. "It was clear right away that Akamai Guardicore Segmentation made it easier to define and implement policies. The console interface, with its labels, was straightforward and offered better process visibility than Illumio." 260 servers segmented from 3 zones to granular microsegmentation. **Direct head-to-head win over Illumio — quote-worthy.**

**Anonymous Manufacturing Company (Akamai-published case study)** — Multiple sites globally, mixed office and manufacturing facilities. Deployed Guardicore to ~2,000 workstations in phase one. Quote: "With a single agent on a machine, we've solved the problem of an endpoint attack by lateral movement for good and can now go from a workstation with no policies to the full implementation of security controls in 30 seconds."

**Anonymous Specialty Manufacturer (Forrester TEI quote)** — "What tilted things in favor of Guardicore? Legacy operating system support was one of the big ones that some of the [competing products] did not support. The other piece was the scalability and visibility, as well as the ease of the learning period through enforcement."

**Anonymous Global Manufacturer (Ransomware recovery story)** — After a successful propagating malware attack, the breach remediation team deployed Guardicore agents across 3,000 servers within three hours. Two crucial production applications running the only functioning manufacturing line were secured via a policy restricting infected subnets — a task that would have taken weeks with legacy firewalls.

### Guardicore content library — assets available for personalization

| Asset | Type | URL |
|-------|------|-----|
| Akamai Guardicore Segmentation product page | Webpage | akamai.com/products/akamai-guardicore-segmentation |
| Segmentation for IoT and OT product brief | PDF | akamai.com (Nov 2024) |
| Akamai-NVIDIA BlueField announcement | Press release | Feb 23, 2026 |
| AI-powered capabilities announcement | Press release | Mar 24, 2026 |
| Victorinox customer story | Customer story | akamai.com (2025) |
| Manufacturing Company case study | Customer story | akamai.com |
| Ransomware recovery case study | Customer story | akamai.com |
| State University OT case study | Customer story | akamai.com (building automation, OT-adjacent) |
| Forrester TEI study | Study + blog | akamai.com (Dec 2024) |
| Gartner Peer Insights reviews | Third-party social proof | gartner.com/reviews |

### Known weaknesses (be honest, anticipate objections)

From PeerSpot reviews "What we hear most from customers is that it requires a kernel module... I think the pricing is very high... Kubernetes is not installed in the way we need it" — confirmed real-world friction:
- Kernel-module agent installation (mitigated by agentless option for OT)
- Pricing perceived as premium (mitigated by Forrester ROI numbers)
- SaaS update cadence can be challenging
- Kubernetes implementation requires care

---

## 4 · Axians Brand Style Guide (researched)

For use in all Stage 4 PDF execution materials.

### Brand colors ✅

Source: Axians logo (verified via whatthelogo.com extraction, cross-referenced with axians.de visuals)

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| Primary | Axians Blue | `#0068B6` | Headers, primary CTAs, logo, key data |
| Accent | Axians Magenta | `#AC006D` | Highlights, secondary CTAs, callouts |
| Background | White | `#FFFFFF` | Primary canvas (`meta-theme-color: #ffffff` confirmed on axians.de) |
| Text | Near-black | `#1A1A1A` | Body text |
| Muted | Cool gray | `#6B7280` | Captions, metadata |
| Surface | Light gray | `#F4F6F8` | Cards, panels, table rows |

### Typography

Axians.de uses a clean modern sans-serif. For PDFs (without licensing the exact corporate font), use the closest royalty-free analog:

| Use | Font (PDF) | Weights |
|-----|------------|---------|
| Display / H1 | **Inter** (or Roboto fallback) | 700 Bold |
| Headers H2–H4 | Inter | 600 Semibold |
| Body | Inter | 400 Regular, 500 Medium |
| Data tables | Inter or system monospace for numbers | 500/600 |

### Tone of voice 🗣️

Voice patterns extracted from axians.de and press releases:

| Pattern | Example | Implication |
|---------|---------|-------------|
| Partnership at eye-level | "partnerschaftlich auf Augenhöhe" | Treat customers as peers, not buyers |
| Holistic thinking | "ganzheitlich", "integrativ", "360°" | Always position as integrated, not point-solution |
| Pragmatic security | "Keep it simple and secure" | Reject complexity-for-complexity's-sake |
| Human-centric ICT | "with a human touch" | Technology serves people, not the reverse |
| Action triplets | "Secure. Connect. Empower." / "Proven. Secured." | Use rhythmic three-beat structures in headlines |
| Direct industry framing | "Automotive, Maschinenbau, Prozessindustrie" | Speak directly to manufacturing verticals by name |

**In English (the sprint's working language), adapt these into:**
- Direct, peer-level address ("you" not "your organization")
- Three-beat headlines where natural
- Operational concreteness over abstractions ("48-hour POC" not "rapid value realization")
- Manufacturing-specific vocabulary ("production line", "shop floor", "PLC", "machine controller")
- Polite confidence — neither hard-sell American nor stiff corporate German

### Visual identity rules

Observed on axians.de:
- **Generous white space** — never crowd elements
- **Photography of people** — real engineers, not stock imagery
- **Clean horizontal layout** — content rarely uses diagonal/decorative shapes
- **Logo placement** — top-left corner, often paired with VINCI Energies endorsement at bottom-right
- **Iconography** — simple line icons in Axians Blue
- **Two-tone palette discipline** — blue and magenta used sparingly, never together as competing accents

### Sample headline patterns (for Stage 4)

For the sprint's English-language execution materials:
- "Microsegmentation for German Manufacturing. Proven. Secured."
- "NIS2 is law. Lateral movement isn't waiting."
- "From flat OT network to documented Zero Trust. In 60 days."
- "One platform. Office and shop floor. No agents on the PLC."

---

## 5 · Sprint Scope & Constraints (reaffirmed)

| Dimension | Constraint |
|-----------|------------|
| Account band | €100M–€2B revenue · 1,000–10,000 employees |
| Geography | Germany only |
| Vertical | Mittelstand manufacturing (mechanical engineering, automotive supply, components, machine tools, electrical equipment, industrial process) |
| Filter out | DAX 40, most MDAX, KRITIS operators with their own SOC, healthcare/finance/utility verticals (different motion) |
| NIS2 status required | Essential or Important entity under the new BSIG |
| OT/IT convergence | Must have real OT footprint (factory floor, production line, plant operations) — not pure-software companies |
| Axians reachability | Bonus: existing VINCI Energies / Axians / Actemium / Omexom relationship signal |
| Language | All artifacts in English (including email sequences and showcase) |
| Confidence markers | ✅ confirmed · ⚠️ single-sourced · 🧠 inferred · ❌ blind spot |

---

## 6 · Intent-Enabled Partner Selling — Operational Frame 🧠

This sprint operates **as if** the Partner Intelligence Program (PIP) were live. In production:
- **Layer 1 (Partner Intent Routing):** Akamai's 6sense and 1st-party telemetry surface DACH accounts in active research for microsegmentation, Zero Trust, OT security, NIS2 readiness. These accounts get shared with Axians monthly as a curated "Hot 20" list — account-level only (company + buying-stage + topic cluster), GDPR-safe.
- **Layer 2 (Account-Based Enablement):** For each flagged account, Akamai pre-builds a sales kit: research brief, personalized email sequence, relevant case study (regional where possible), and talking-point card. Axians launches outreach immediately, no desktop work delay.

For this sprint, **intent is a hypothesis overlay** — we cannot verify actual 6sense signals. The targeting in Stage 1 proceeds on firmographic and public-data criteria, with intent referenced as the operational frame this work would plug into.

---

## 7 · What Stages 1–5 Will Produce

| Stage | Output | Format |
|-------|--------|--------|
| 1 · Targeting | ICP, scoring matrix, 30-longlist, 10-shortlist, final 3+1 | Markdown |
| 2 · Intel | 16 deep-dive files (4 per account × 4 accounts) | Markdown |
| 3 · Strategy | Sweet spot, pain pattern library, content matrix, competitive angle | Markdown |
| 4 · Execution | 12 PDFs (3 per account × 4 accounts) — Axians-branded | PDF |
| 5 · Infrastructure | KPIs (HTML dashboard), CRM spec (HubSpot), MDF spec, launch checklist | HTML + Markdown |
| Showcase | Trumpf full profile — consolidated | Markdown |

Total: 43 artifacts.

---

## Confidence summary

What I'm **confident** about (✅):
- Axians corporate identity, key people, public partnerships
- Guardicore product capabilities, recent announcements, customer references
- NIS2 legal status, deadlines, scope, fines
- Axians' marketing/CRM stack (HubSpot)
- Existing Axians manufacturing customers (Viessmann, Miele, Hörmann, HeidelbergCement)

What I'm **moderately confident** about (⚠️):
- Exact revenue split between Axians DE and ex-Fernao (pre-research input)
- Exact employee count post-integration

What I'm **inferring** (🧠):
- Sister-brand Actemium plays primary OT role in customer engagements
- HubSpot is the primary marketing automation; CRM may be HubSpot CRM or a separate system
- Specific intent signals on target accounts (hypothesis overlay)

What I'm **blind to** (❌):
- Internal Axians deal registration process with vendors
- Existing vendor partnerships beyond what's publicly disclosed
- Pricing/commercial constructs Axians uses for security projects

---

**End of Stage 0.** Ready to proceed to Stage 1 (ICP, scoring matrix, longlist, shortlist) on confirmation.
