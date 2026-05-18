# Maschinenfabrik Reinhausen (MR) — Company Brief

> **Account 2 · Stage 2 Intel** · D3-2 ABSM Sprint
> **Last researched:** 2026-05-18
> **Primary sources:** reinhausen.com, cio.de, powersystems.technology, weltmarktfuehrerindex.de, linkedin.com, industrie40award.com, solvares-fieldservice.com

---

## At a Glance

| Field | Value | Confidence |
|-------|-------|------------|
| Legal entity | Maschinenfabrik Reinhausen GmbH | ✅ |
| HQ | Falkensteinstraße 8, 93059 Regensburg, Bavaria | ✅ |
| Founded | 1868 (Andreas Scheubeck) | ✅ |
| Ownership | 100% Scheubeck Holding Verwaltungs-GmbH, Neutraubling — **6th generation family-owned majority** | ✅ |
| Revenue (FY2024) | **€1.2 billion** (€1,224,999,936) | ✅ |
| Revenue (FY2021) | €741.6M — significant recent growth | ✅ |
| Employees worldwide | **~5,400** (including 400 engineers + 200+ service technicians) | ✅ |
| Locations | 60 (including 7 training centers) in 28 countries; 39 associated companies | ✅ |
| Export share | **92.1%** (sales outside Germany) | ✅ |
| Global market share | ~6% (in regulated transformer technology overall; MR claims ~50% in OLTC niche) | ✅ |
| Awards 2025 | **Innovation-Champion 2025** (Handelsblatt/Wirtschaftswoche, Munich Strategy) — 2nd in revenue ranking | ✅ |
| Industrie 4.0 award | **First German recipient of the Industrie 4.0 Award** | ✅ |
| Patents | **>1,500 worldwide** | ✅ |

---

## What MR Makes

MR is the **world market leader in on-load tap-changers (OLTC)** — the components that allow power transformers to adjust voltage under load. Their products regulate **50% of the electrical energy transported worldwide**.

| Product family | Core technology | Position |
|----------------|-----------------|----------|
| **VACUTAP®** | Vacuum-technology OLTCs (VBO, VM, VI generations) | Global market leader |
| **TAPCON®** | Voltage regulators / transformer controllers | Market-defining |
| **ETOS®** | Open operating system for intelligent transformers | First-in-world |
| **MTraB®** | Intelligent dehydrating breathers | Premium niche leader |
| **TESSA® APM** | Asset Performance Management software (Siemens Xcelerator partnership) | Software-defined infrastructure |
| **Composite hollow insulators / GFK pipes** | Glass-fiber-reinforced plastic for HV applications | Secondary business line |
| **De-energized tap-changers** | For transformer manufacturers | Established product |

**Customer base:**
- Energy producers (utilities, IPPs)
- Public grid operators (TSOs, DSOs)
- Industrial grid operators
- Transformer manufacturers (Siemens Energy, Hitachi Energy/ABB, Hyundai, etc.)

**The strategic position:** MR sits *inside* the equipment that critical infrastructure operates with. Every transformer at a substation that uses MR's OLTC technology routes voltage decisions through MR firmware, MR sensors, and increasingly MR's cloud telemetry.

---

## Leadership

### Executive Board (Geschäftsführung)

| Name | Role | Confidence | Source |
|------|------|-----------|--------|
| **Dr. Nicolas Maier-Scheubeck** | Spokesman of the Executive Board (CEO equivalent) | ✅ | reinhausen.com newsroom |
| **Wilfried Breuer** | Managing Director Sales & Systems | ✅ | reinhausen.com Innovation Champion announcement |
| **Holger Michalka** | Managing Director (Operations / Investment) | ✅ | onload.reinhausen.com capacity announcement |

### Other Senior Roles (LinkedIn-verified)

| Name | Role | Source |
|------|------|--------|
| **Jürgen Ach** | Director of Automation | powersystems.technology interview |
| **Christian Hengl** | Leiter Process Engineering | cio.de S/4HANA case |
| **Stefan Schneider** | Head of System Architecture (since May 2022) | LinkedIn |
| **Dr. Hubert Feyrer** | Cyber Security Expert | reinhausen.com impulses; LinkedIn linkedin.com/in/hubertf |
| **Johannes Gebauer** | Director Sales Europe | LinkedIn |
| **Christian Hillinger** | Senior Manager Portfolio Actuators | LinkedIn |
| **Markus Mascha** | Projektmanager Automation (Electronic & Software) | LinkedIn |

---

## Tech Stack — Confirmed Public Signals

### Enterprise IT
- ✅ **SAP S/4HANA** — *just migrated from SAP R/3 (which had been the backbone for 25 years)* — completed via All for One + SNP using Bluefield/Crystal Bridge approach
- ✅ **3,600 active SAP users** on the new system
- ✅ Planned 2026 expansion: SAP Fiori strategy per process; Enterprise Search; SAP Business Technology Platform; SAP Build Work Zone; **SAP Joule (AI)**
- ✅ SAP CS, SAP SD historically
- ✅ Solvares MOBILE X for field service (250+ certified service technicians globally)
- ✅ Atlassian Cloud (Confluence, Jira)
- ✅ Siemens Xcelerator partnership (TESSA APM software)

### Product / OT
- ✅ **VxWorks 5** as the embedded OS for ETOS firmware
- ✅ ISM® (Intelligent Sensor Module) edge computing on transformers
- ✅ ETOS-MD-IV variant for US market (regional cloud)
- ✅ TLS 1.2 encryption + RBAC + cryptographic firmware signing
- ✅ Standards compliance: **IEC 62443, IEC 62351, BDEW Whitepaper 2.0, IEEE 1686, OWASP, BSI TR 02102, FIPS-PUB 180-4**
- ✅ ISO 27001 ISMS being built (currently in progress, focused on ETOS and ETOS update delivery)

### IT Integrator Landscape
| Integrator | Service | Source |
|------------|---------|--------|
| **All for One** | SAP S/4HANA implementation partner | cio.de Jan 2026 |
| **SNP** | Migration platform (Kyano + Crystal Bridge), Bluefield approach | cio.de |
| **PIKON SAP Consulting International** | Additional SAP consulting | pikon.com |
| **Solvares** | Field-service software (MOBILE X) | solvares-fieldservice.com |
| **Siemens Xcelerator** | Industrial software platform (TESSA APM) | siemens.com |
| **Axians** | ❌ **No public engagement found** | — |

**The implication:** Reinhausen has a well-developed integrator stack — but Axians is not in it. This makes the account **cold but technically primed**: they're sophisticated enough to evaluate Guardicore rigorously, but Axians has no warm bridge.

---

## Strategic Posture (2025–2027)

### Investment offensive

In July 2025, MR announced its **largest single investment in company history** — a multi-year, **three-digit-million-euro** capacity expansion program. Per MD Holger Michalka:

- **Doubling Regensburg capacity** at the Haslbach commercial area, completing in phases starting Q4 2025; final headcount target ~1,800 at this single site
- US production expansion (focused on OLTCs)
- "Glocalization" — partial localization of value-creation steps along the global supply chain
- AI-supported technologies in production roadmap

> "With the largest single investment in the company's history, we are completely reorganizing our production around the globe over the next four years and doubling our capacities!" — Holger Michalka

### Innovation Champion 2025

In September 2025, the Munich Strategy / Handelsblatt / Wirtschaftswoche study named MR one of Germany's 30 most innovative medium-sized enterprises, evaluating 4,000 companies with 400 on the shortlist. MR ranked **2nd in the top 30 in revenue terms** — a position that signals scale + innovation simultaneously.

### Digital strategy direction

From Dr. Maier-Scheubeck's public statements:
- "We see ourselves as **THE POWER BEHIND POWER**"
- "Global energy transition is not possible without solutions from Reinhausen"
- Heavy emphasis on **digitalization and resilience of critical grid infrastructure** as a public theme

The strategic narrative MR projects is: We are not just a transformer-parts supplier; we are the digital intelligence layer of the grid.

---

## Cyber Security Maturity — Mixed and Asymmetric

### What MR has built (strong)

✅ **ProductCERT (MR-CERT)** — dedicated cyber security emergency response team for products; advisories published publicly:
- MRSA-2021-1201: log4j (CVSS 10.0)
- MRSA-2022-0801: ETOS/ISM SW 3-3 vulnerability
- MRSA-2023-1101: ETOS®/ISM® Broken Authorization
- MRSA-2024-0401: xz vulnerability

✅ **BDEW Whitepaper 2.0 full compliance** — ETOS independently audited; the technical implementation meets all requirements of the BDEW/OE Whitepaper 2.0 in full

✅ **ETOS-specific ISO 27001 ISMS** — currently being built, with Plan-Do-Check-Act cycle implementation across all relevant technical and administrative areas

✅ **Public cyber expert (Dr. Hubert Feyrer)** — quoted in detailed technical articles on automation security, security-by-design, ETOS/TESSA encryption architecture, Cyber Resilience Act readiness

✅ **Defense-in-depth at the product level** — pre-configured firewall, hardened VxWorks 5 OS, hardware interface deactivation, encrypted firmware, RBAC

### What's less clear (potential gaps)

⚠️ The published cyber narrative is **almost entirely product-focused**. Coverage of corporate IT security, manufacturing OT segmentation, or supply-chain security from the *consumer* side is not public.

⚠️ The ISO 27001 ISMS is being built **for ETOS specifically** — not for the broader MR corporate environment.

⚠️ With ~5,400 employees, 60 locations, doubling Regensburg, and a major S/4HANA migration just landed, the **internal IT attack surface has grown substantially in 2024–2025** — but no public statements about how that growth is being segmented.

⚠️ No named CISO at corporate level visible (Dr. Feyrer is "Cyber Security Expert" in the product/automation organization)

### The Guardicore angle

**Reinhausen has mastered product security; Guardicore is for everything around it.** Their ETOS product is rigorously secured against external threats — but the manufacturing floors that *build* ETOS, the SAP S/4HANA system that *manages* MR's business, and the corporate networks where Dr. Feyrer's team *operates* are a different scope. Microsegmentation of corporate-IT-to-OT (and OT-to-customer-cloud connections via TESSA) is the white space.

---

## NIS2 Exposure

MR is an **essential entity** under §28 of the new BSIG:

| Criterion | MR situation |
|-----------|--------------|
| Sectoral coverage | ✅ Annex I — manufacturer of electrical equipment for energy infrastructure |
| Size threshold | ✅ Far above thresholds (€1.2B revenue, ~5,400 employees) |
| Critical-infrastructure-supply chain | ✅ Products deployed in nearly every TSO/DSO globally |
| Registration deadline | March 6, 2026 — status undocumented publicly |
| Article 21 compliance | All 10 measures apply; segmentation core to several |

**The double scope:** MR is itself NIS2-essential, AND its customers (utilities) are universally KRITIS operators worldwide. **The supply chain question is asked twice:** in MR's own audit, and in every utility customer's KRITIS reporting.

---

## What This Account Brings to the Sprint

| Strategic dimension | What MR provides |
|--------------------|------------------|
| **Geographic** | Bavaria — diversifies from Trumpf (BW), Hörmann/Witte (NRW) |
| **Sub-sector** | Electrical equipment for grid infrastructure — unique vs. building hardware (Hörmann) and auto Tier 1 (Witte) |
| **Narrative angle** | "Cold-but-bullseye" — perfect ICP, no Axians warm path. Demonstrates how PIP would surface a new account |
| **Maturity signal** | Higher cyber sophistication than peers — they have a real CERT, real standards engagement. The Guardicore conversation is **adjacent** to their strength, not corrective |
| **Timing trigger** | Just completed S/4HANA migration; investment offensive doubling capacity; ETOS ISMS in build phase — multiple buying triggers active simultaneously |
| **Industry visibility** | Innovation Champion 2025 + Industrie 4.0 first-mover award = highest possible Mittelstand credibility |

---

## What Stage 2 Could Not Verify (❌)

- Whether MR has registered with BSI under NIS2 (registration not public)
- The specific incumbent firewall, EDR, SIEM vendors at corporate-IT level
- Whether MR has previously evaluated Illumio or another microsegmentation vendor
- Specific budget/headcount for Dr. Feyrer's cyber team
- Internal OT security maturity at the production floors (vs. product side)
- Whether any prior Akamai engagement exists

**Stage 4 outreach approach:** these gaps are the first-meeting discovery questions.

---

**End of Reinhausen company brief.** Pain map next.
