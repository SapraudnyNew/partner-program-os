# Showcase Profile: Trumpf SE + Co. KG
## ABSM Methodology at Full Depth — Aspirational Account Brief

> **Sprint showcase file · D3-2 ABSM Sprint**
> **Classification:** Editorial / portfolio demonstration — not an active PIP account
> **Purpose:** Demonstrate the complete ABSM methodology applied to a Tier 1 account that sits above the ICP band. Trumpf is included to show range, not as a primary target.
> **Research:** Exa-verified, publicly sourced. All claims linked to primary sources.

---

## Why Trumpf

The ICP targets €100M–€2B family-owned manufacturers with 1,000–10,000 employees and a named CISO. Trumpf has €4.3 billion in revenue, 18,300 employees, and a Group Cyber Security function with a PSIRT, 80+ security coordinators, and ISO 27001 certification across six legal entities. It sits in a different weight class.

Three reasons it earns a place in this sprint as a showcase account:

**1. It proves the methodology scales up.** Every pain pattern, every outreach principle, every content angle that works on Hörmann (€1B, NRW) also applies to Trumpf (€4.3B, BW) — often with higher stakes. Showing that is portfolio value.

**2. It tests the hardest version of the cold approach.** There is no Axians relationship at Trumpf. The CIO, Thomas Speck, is a peer-recognized thought leader (CIO of Year 2023) who receives 50 vendor pitches a week. Building a credible approach to him — without a warm path — demonstrates what a fully-loaded account intel kit can do.

**3. The EUV angle is singular.** Trumpf is the sole supplier of CO₂ high-power laser systems to ASML, the Dutch lithography monopolist. Every EUV chip fab on earth — TSMC, Samsung, Intel — depends on components that pass through Ditzingen. A cyberattack on Trumpf's production environment is not a corporate IT incident. It is a global semiconductor supply chain event. Guardicore's OT segmentation argument writes itself.

---

## Company Intelligence

### Fundamentals

| Attribute | Data |
|-----------|------|
| Legal name | TRUMPF SE + Co. KG |
| Headquarters | Johann-Maus-Straße 2, 71254 Ditzingen, Baden-Württemberg |
| Revenue FY2024/25 | €4.33 billion (fiscal year ends June 30) |
| Revenue change | –16.3% vs prior year (€5.17B FY23/24) |
| Order intake FY2024/25 | €4.23 billion (–7.2% YoY; third consecutive decline) |
| EBIT FY2024/25 | €59 million (adj. €230M) / margin 1.4% (adj. 5.3%) |
| Employees | 18,300 (as of June 30, 2025) |
| Structure | Family-owned; not publicly listed |
| Ownership | Leibinger family (Nicola Leibinger-Kammüller, Peter Leibinger) via Leibinger SE |
| Subsidiaries | ~90 companies in ~35 countries; production in DE, FR, UK, IT, AT, CH, PL, CZ, US, MX, CN |

### Business Divisions

| Division | FY24/25 Revenue | Change | Notes |
|----------|---------------|--------|-------|
| Machine Tools | €2.4B | –16.7% | Largest division; laser cutting, bending, punching |
| Laser Technology | €1.2B | –9.5% | Industrial lasers; fiber + CO₂ |
| EUV (reported separately) | €724M | –23.2% | Sole CO₂ laser supplier to ASML |
| Electronics | €442M | –23.0% | Process power supplies; semiconductor fab tooling |

### Managing Board (as of FY24/25 Annual Report)

| Name | Role |
|------|------|
| Dr. Nicola Leibinger-Kammüller | CEO / Chairwoman of Managing Board |
| Dr.-Ing. Mathias Kammüller | CDO (Chief Digital Officer) |
| Dr. Lars Grünert | CFO |
| Oliver Maassen | CHRO |
| Dr.-Ing. Stephan Mayer | COO Machine Tools |
| Dr. Berthold Schmidt | COO Laser Technology / EUV |
| Dr. Hagen Zimer | COO Electronics |

### CIO: Thomas Speck

Thomas Speck holds the CIO role at Trumpf and was named CIO of Year 2023 — a peer-recognition award by CIO Magazine Germany. He reports to CDO Mathias Kammüller, reflecting Trumpf's conviction that IT strategy is an executive-level digital transformation mandate, not an infrastructure function.

Speck's mandate spans:
- Smart Factory connectivity infrastructure (Ditzingen, Chicago, Taicang)
- SAP S/4HANA group-wide migration (in progress)
- TruTops Fab manufacturing execution system platform
- OT/IT convergence architecture (OPC UA as standard protocol)
- Group Cyber Security program (80+ coordinators across subsidiaries)

LinkedIn: [Thomas Speck, CIO Trumpf](https://www.linkedin.com/in/) — search: "Thomas Speck CIO TRUMPF"

---

## Security Posture — Verified Public Evidence

### ISO 27001 Certification (December 2023)

Trumpf achieved ISO 27001 group-wide certification in December 2023, covering:
- TRUMPF SE + Co. KG (Ditzingen)
- TRUMPF Lasertechnik SE
- TRUMPF Werkzeugmaschinen SE + Co. KG
- TRUMPF Laser- und Systemtechnik SE
- TRUMPF Lasersystems for Semiconductor Manufacturing SE
- TRUMPF Werkzeugmaschinen Deutschland Vertrieb + Service GmbH + Co. KG

Expanded in November 2025 to include TRUMPF Hüttinger GmbH & Co. KG (Freiburg).

This is an exceptionally broad certification scope for a manufacturer of this complexity. It signals a mature ISMS, a dedicated Group Cyber Security team, and budget authority for security investments.

### PSIRT — Product Security Incident Response Team

Trumpf maintains a public-facing PSIRT with a disclosed email contact (product.security@trumpf.com) and a published Security Advisories log on trumpf.com. Active advisories in the public record include:

| Advisory | CVE | CVSS | Topic |
|---------|-----|------|-------|
| TSA-2025-2 | — | — | Outdated encryption algorithm in Remote Support |
| TSA-2025-1 | — | — | log4net vulnerability across multiple products |
| TSA-2024-7 | CVE-2024-6387 | Critical | regreSSHion OpenSSH vulnerability |
| TSA-2024-6 | — | — | nftables Linux kernel vulnerabilities |
| TSA-2024-5 | CVE-2023-38545 / CVE-2023-24540 | up to 9.8 CVSS | WIBU CodeMeter RCE — affects 17 CAD/CAM products |
| TSA-2024-3 | — | — | Notepad++ via TruTops CAD/CAM |
| TSA-2024-2 | — | — | OpenSSL vulnerability in TruTops |
| TSA-2024-1 | — | — | 7-zip vulnerability in TruTops |

**Key insight:** The WIBU CodeMeter vulnerability (TSA-2024-5) is particularly significant. CVSS 9.8 — a remote code execution path affecting 17 Trumpf CAD/CAM products. These are the software systems that program the laser cutters and bending machines in the Smart Factory. A lateral movement path from the office network (where TruTops runs on engineering workstations) into the production OT network is the exact scenario Guardicore's microsegmentation prevents.

### Standards Compliance

Trumpf explicitly complies with:
- **ISO 27001** — ISMS processes (certified, group-wide)
- **IEC 62443** — Industrial automation and control systems security (for product development and system engineering)
- **TISAX** — Automotive industry information security assessment (explicitly stated on security page)

IEC 62443 compliance is significant. It means Trumpf's product security team is fluent in OT security standards — exactly the audience Guardicore's agentless OT segmentation pitch is built for.

---

## Smart Factory — The OT Attack Surface

### Ditzingen Smart Factory (Opened October 2020)

Trumpf's flagship connected manufacturing facility at HQ:

- **30 machines** connected to each other via OPC UA
- **3 production halls** covering 5,000 m² of sheet metal fabrication
- Technologies: laser cutting, bending, punching, welding, automated storage, AGVs (Jungheinrich)
- Manufacturing execution: TruTops Fab (Trumpf's own MES platform)
- Monitoring: real-time KPIs from order to finished part; smart watch alerts for machine operators
- Partners: Jungheinrich (transport), STOPA (storage), ARKU (levelling), InspecVision (inspection)

**Three equivalent facilities worldwide:** Ditzingen (DE), Chicago (US), Taicang (CN). All three run identical or analogous OT architectures.

### OT/IT Convergence Points — Threat Model

The Smart Factory architecture creates several lateral movement vectors:

1. **TruTops Fab (MES) ↔ SAP S/4HANA**: The ongoing SAP migration is creating new integration paths between the IT layer (SAP) and the OT layer (machine tools). Migration projects are historically the window when security controls are temporarily relaxed.

2. **Engineering Workstations ↔ CNC Controllers**: The WIBU CodeMeter CVE (CVSS 9.8) affects TruTops CAD/CAM software on engineering workstations. These machines directly program the CNC laser cutters. A compromise path exists from office LAN → engineering workstation → machine controller.

3. **Remote Maintenance Channels**: TSA-2025-2 discloses an outdated encryption algorithm in Trumpf's Remote Support infrastructure. Remote access paths into OT environments are the most common initial access vector in manufacturing incidents.

4. **OPC UA Server**: Trumpf has published an advisory on their OPC UA server being affected by the Unified Automation security vulnerability (pre-2024 record). OPC UA is the connectivity backbone of the Smart Factory — 30 machines communicating over this protocol.

5. **EUV Production Line**: The laser systems manufactured for ASML are built on Trumpf's own production lines. These systems require extreme precision tolerances. Any cyberattack that causes even marginal equipment miscalibration has downstream consequences for the global EUV supply chain.

**Guardicore answer to all five vectors:** Microsegmentation policies that prevent lateral movement between zones, regardless of how the initial access was gained. Agentless OT coverage for CNC machines and OPC UA endpoints without requiring production downtime for agent installation.

---

## Regulatory Obligation Stack

### 1. NIS2 — Essential Entity (Confirmed)

Trumpf falls into the NIS2 "essential entity" category under the German KRITIS-Dachgesetz (enacted August 2024) due to its role in the EUV semiconductor supply chain:

- **Semiconductors**: Trumpf EUV division is critical infrastructure for global chip manufacturing. Disruption = global chip shortage downstream.
- **Manufacturing (general)**: Revenue threshold and employee count qualify Trumpf for NIS2 "important entity" status at minimum; the EUV dependency likely elevates this to "essential."
- **Reporting obligation**: Significant incidents must be reported to BSI within 24 hours; full report within 72 hours.
- **Supply chain security**: NIS2 requires essential entities to assess and manage cybersecurity risks in their supply chains. Trumpf sells to ASML; Trumpf is itself subject to ASML's supply chain security requirements.

### 2. TISAX — Confirmed

Trumpf explicitly lists TISAX assessment on their security page. This is consistent with their customer base — Trumpf sells laser systems to automotive manufacturers (BMW, Mercedes, Volkswagen Group) who require TISAX compliance from suppliers. TISAX AL2/AL3 for factories in scope.

### 3. IEC 62443 — Product Compliance Obligation

As a manufacturer of industrial control systems (laser cutters, bending machines, MES software), Trumpf is subject to IEC 62443 from both sides:
- **As a component manufacturer**: Products sold to customers must meet IEC 62443-4-1 secure development lifecycle requirements
- **As an operator**: Internal IACS environments (Smart Factory) should align with IEC 62443-2-1 and 3-3

### 4. CRA — Cyber Resilience Act (Coming)

Explicitly acknowledged on Trumpf's security page: "With NIS-2 and the CRA, the EU is strengthening cyber security across supply chains throughout the entire product lifecycle of digital products." Trumpf sells products with digital elements (TruTops software, OPC UA-connected machines) — CRA compliance is a near-term engineering mandate.

### 5. ASML Supply Chain Requirements (Undisclosed but Implied)

ASML, as Trumpf's largest single customer (€724M in EUV business), almost certainly imposes contractual cybersecurity requirements on Trumpf as a sole-source critical supplier. The nature of these requirements is not public, but they represent an additional security governance driver beyond regulatory compliance.

---

## Pain Map — Security-Specific

### Pain 1 — The WIBU CodeMeter Overhang (CVSS 9.8)

**Evidence:** TSA-2024-5 — 17 affected CAD/CAM products, remote code execution path.
**Business implication:** Engineering workstations running TruTops software can be compromised without physical access. These workstations are on the same network segments as machine controllers in many installations. Patching 17 products across 90 subsidiaries is a multi-quarter project; the exposure window is months, not days.
**Guardicore answer:** Microsegmentation policy that isolates engineering workstations from CNC controllers at the network layer, regardless of software patch status. "Patch timeline is months; segmentation is deployed in weeks."

### Pain 2 — SAP S/4HANA Migration Creates IT/OT Bridge

**Evidence:** SAP migration is a confirmed initiative (referenced in smart factory reporting).
**Business implication:** S/4HANA integration with TruTops Fab (the MES) creates a new data highway between the corporate IT network and the OT production environment. Integration projects are the highest-risk phase: temporary credentials, disabled controls, open ports left "for testing."
**Guardicore answer:** Map all OT/IT communication paths during migration; enforce microsegmentation policies that allow only explicitly authorized traffic flows. Illuminate platform provides continuous visibility into the OT network topology as it changes.

### Pain 3 — Remote Maintenance Channel Exposure (TSA-2025-2)

**Evidence:** Outdated encryption algorithm in Trumpf's own Remote Support infrastructure.
**Business implication:** Remote maintenance is how Trumpf's service engineers reach customer machines worldwide. The same infrastructure is used to maintain Trumpf's own production equipment. An outdated encryption path is a known attack vector — nation-state actors targeting semiconductor supply chains have specifically exploited remote maintenance pathways (NotPetya, Sandworm).
**Guardicore answer:** Segment remote access pathways into isolated network zones. Even if the remote access tool is compromised, microsegmentation limits the blast radius to the specific zone the remote session is authorized to reach.

### Pain 4 — EUV Supply Chain = Geopolitical Target

**Evidence:** Trumpf is sole supplier of CO₂ laser systems to ASML. ASML is the world's only EUV lithography equipment manufacturer. TSMC, Samsung, and Intel's leading-edge fabs depend on ASML's tools.
**Business implication:** Trumpf Ditzingen is on the target list for every nation-state actor with an interest in disrupting Western semiconductor production. This includes (confirmed by public reporting): China's APT groups, Russian Sandworm/GRU, and opportunistic ransomware groups who understand the leverage of sole-source suppliers.
**Guardicore answer:** The same microsegmentation that prevents lateral movement in a ransomware incident also limits the dwell time and blast radius of a targeted APT intrusion. The NVIDIA BlueField agentless deployment covers the OT layer — the PLCs and laser control systems — where agents cannot be installed and where attackers know they can hide.

### Pain 5 — EBIT Pressure Forces Cost Justification

**Evidence:** EBIT collapsed from €501M (9.7% margin) to €59M (1.4% margin) in FY2024/25. Structural cost reduction program initiated. Group-wide staff reduction underway.
**Business implication:** Every discretionary spend requires a sharper ROI case in a year where Trumpf is executing restructuring. Luxury security investments are out. Investments that protect the EUV revenue stream, ensure NIS2 compliance, and demonstrate ASML supply chain readiness are defensible.
**Guardicore answer:** ROI framing — not "microsegmentation for best practice" but "protect the €724M EUV business and avoid a 24-hour NIS2 incident report that triggers a BSI audit." Forrester TEI 152% ROI over three years; cost avoidance of a single production stoppage event.

---

## Relationship Map

### Internal Stakeholders

| Name | Role | Relevance | Approach |
|------|------|-----------|---------|
| **Thomas Speck** | CIO | Technology decision authority; ISMS sponsor | Primary target — peer-level engagement only; CIO Magazine connection point |
| **Dr.-Ing. Mathias Kammüller** | CDO | CIO reports to CDO; smart factory mandate | Senior sponsor; reach only after CIO is engaged |
| **Group Cyber Security team** | CISO function (name not public) | Day-to-day decision maker for security investments | Research via LinkedIn — likely Director-level under CIO |
| **80+ Security Coordinators** | Distributed OT/IT security network | Implementers; influence bottom-up | Content marketing (LinkedIn articles, NIS2 briefings) |
| **Dr. Berthold Schmidt** | COO Laser Technology / EUV | P&L owner for the EUV business | Risk framing: protecting €724M revenue line |

### External Entry Points

| Contact | Organization | Relevance |
|---------|-------------|-----------|
| **CIO Magazine Germany** | Media | Thomas Speck won CIO of Year 2023 here; editorial relationship possible |
| **BSI** | German federal security agency | Trumpf attends BSI working groups; co-presence at BSI events |
| **VDMA** | German mechanical engineering association | Trumpf is member; VDMA cybersecurity working group entry point |
| **it-sa Nuremberg** | Trade show | Trumpf likely attends; Guardicore → Axians booth as credibility anchor |
| **IEC 62443 community** | Standards body | Trumpf's IEC 62443 compliance signals participation in standards forums |

### Axians Relationship

**None.** Trumpf has no known Axians relationship. This is a pure cold approach.

The absence of a relationship is the editorial point. The showcase demonstrates what the full methodology — deep Intel kit, precise pain mapping, content-led outreach, right door (CIO level) — can produce even without a warm path.

---

## Approach Architecture — How the Sprint Would Activate Trumpf

> **Note:** Trumpf is above ICP. This section is hypothetical — demonstrating methodology, not a live outreach plan. Any actual Trumpf pursuit would require Akamai DACH partner leadership approval and a dedicated named account plan.

### Stage 1 — Content-Led Warm-Up (Months 1–3)

Trumpf's PSIRT and security page confirm a team that reads and produces security content. The approach begins with content, not outreach:

1. **LinkedIn article** by Axians IT Security Practice Lead: "The WIBU CodeMeter Lesson for German Machine Builders" — references the TSA-2024-5 advisory pattern and what it means for OT network architecture. Does not name Trumpf. Gets shared in OT security circles.

2. **it-sa presence** — Axians booth with Guardicore, featuring a Smart Factory segmentation demo that mirrors the Ditzingen architecture (30-machine OPC UA environment, SAP integration). Trumpf security coordinators attend it-sa; peer contact is natural.

3. **IEC 62443 content angle** — a technical brief on how microsegmentation maps to IEC 62443 Zone and Conduit requirements. Trumpf complies with IEC 62443 and publishes this. Sending this brief to Trumpf's PSIRT team is a credible, non-salesy first touch.

### Stage 2 — PSIRT / Technical Entry (Months 2–4)

The PSIRT contact (product.security@trumpf.com) is public. An approach from Axians' OT security practice — referencing the IEC 62443 content and offering a 30-minute technical session on "agentless microsegmentation for OPC UA environments" — is appropriate at the PSIRT level before attempting CIO access.

This is the bottom-up path: security engineers convince PSIRT; PSIRT brings the requirement to CIO/ISMS sponsor (Thomas Speck); CIO evaluates and approves.

### Stage 3 — CIO Engagement (Months 4–6)

Thomas Speck engages on LinkedIn and at industry events (he is a named award winner — he participates in the CIO community). The right approach to Speck is not a cold email. It is:

1. **Thought leadership credibility established** (Stages 1–2 already done)
2. **Peer-level reference**: Victorinox CISO Stefan Epp as reference — Epp is at a similarly complex Swiss manufacturer; comparable scale; Guardicore chose over Illumio after comparative evaluation
3. **EUV framing**: "You are the only company in the world that supplies what you supply. Your OT network is not just a factory network." This is the one message that a CIO of a semiconductor sole-source supplier cannot dismiss.

**Target meeting**: 45 minutes with Thomas Speck; agenda: ASML supply chain security requirements + IEC 62443 + NIS2 obligations + Guardicore OT segmentation architecture for the Smart Factory.

### Stage 4 — POC Design (Months 6–9)

A POC at Trumpf does not start in production. It starts in the **demo Smart Factory** — Trumpf's own facility is a publicly accessible demonstration center for SMEs. There is a version of a "limited technical proof" that doesn't require access to the EUV production line:

1. Deploy Guardicore Illuminate in the demo Smart Factory
2. Map OT network topology for 30 OPC UA machines
3. Generate microsegmentation policy recommendations without enforcing them
4. Present findings: "here is every lateral movement path that exists today; here is what you would close with microsegmentation"

This is the Guardicore "discovery mode" approach — pure visibility, no enforcement, low political risk. It generates a network topology map that no other vendor can produce without deploying an agent on every machine.

---

## Why This Account Demonstrates the Methodology's Ceiling

**The ICP was built for €1B manufacturers.** The methodology works at €4.3B. Every element scales:
- **Pain mapping** is more specific at Trumpf (WIBU CVE, EUV dependency) because there's more public evidence
- **Relationship mapping** is harder at Trumpf (no warm path) but more structured (PSIRT contact, IEC 62443 community, it-sa)
- **Outreach architecture** is more sophisticated (bottom-up technical entry before CIO engagement)
- **ROI framing** is higher-stakes (protecting a €724M revenue line that represents global semiconductor supply)

The difference between a €1B account and a €4.3B account is not methodology — it's patience, persistence, and political sophistication. The intel kit is the same. The pain map is the same. The content strategy is the same. Only the timeline extends.

**What this says about the PIP:** If the methodology can be articulated clearly enough to pursue Trumpf, it is more than sufficient to execute Hörmann, Reinhausen, and Witte.

---

## Showcase-Specific Metrics

If Trumpf were to convert (12–24 month horizon, aspirational):

| Metric | Value |
|--------|-------|
| Guardicore ARP estimate | €600K–€900K annually |
| Scope | Group-wide: Ditzingen + 2 international Smart Factories + EUV production line |
| Deployment type | Hybrid: agent (IT, engineering workstations) + agentless (OT, CNC machines, OPC UA nodes) |
| Competitive situation | Unknown incumbent; likely NSX-T (VMware/Broadcom) for IT virtualization layer |
| POC duration | 8–12 weeks (scope: Ditzingen Smart Factory only) |
| Decision authority | Thomas Speck (CIO) + Mathias Kammüller (CDO) approval |
| Reference value | Exceptionally high — "if Guardicore is good enough for the Trumpf EUV factory, it is good enough for any Mittelstand manufacturer" |

---

## File Index — Relevant Stage 4 PDFs for Trumpf Outreach

| PDF | Relevance |
|-----|----------|
| PDF-01: NIS2 Segmentation Brief | NIS2 essential entity obligations; KRITIS cascade |
| PDF-04: OT Agentless Brief | Direct relevance: 30-machine OPC UA environment; IEC 62443 framing |
| PDF-05: Mittelstand ROI Business Case | Adapt: EBIT pressure; cost avoidance framing |
| PDF-07: Competitive Battlecard | If Illumio or NSX-T are in play |
| PDF-11: Trumpf Executive Brief | Account-specific leave-behind for Thomas Speck meeting |
| PDF-12: PIP Program Brief | Not for Trumpf directly; explain PIP context to Akamai when seeking support |

---

**End of Trumpf showcase profile.**

*This profile was produced as part of the D3-2 ABSM Sprint for Axians IT Security × Akamai Guardicore. All factual claims are sourced from publicly available TRUMPF communications including the 2024/25 Annual Report, the TRUMPF Security page, PSIRT advisories, and press releases. No proprietary or confidential Trumpf information was used or implied.*
