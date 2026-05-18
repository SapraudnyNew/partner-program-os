# Hörmann KG — Company Brief

> **Account 1 · Stage 2 Intel** · D3-2 ABSM Sprint
> **Last researched:** 2026-05-18
> **Primary sources:** axians.de, hoermann.de, hoermann-gruppe.com, en.wikipedia.org, sec-consult.com, telekom-mms.com, LinkedIn

---

## At a Glance

| Field | Value | Confidence |
|-------|-------|------------|
| Legal entity | Hörmann KG (Hörmann Group) | ✅ |
| HQ | Steinhagen, North Rhine-Westphalia (East Westphalia, near Bielefeld) | ✅ |
| Founded | 1935 (August Hörmann) | ✅ |
| Ownership | Family-owned (3rd generation: Thomas J., Martin J., Christoph Hörmann) | ✅ |
| Revenue | "Over €1 billion" (per Wikipedia, no precise published figure) | ⚠️ — privately held, only consolidated narrative |
| Employees | >6,000 worldwide | ✅ |
| Production sites | 40+ specialized factories | ✅ |
| Sales locations | 100+ in 40+ countries; partner-represented in 50+ more | ✅ |
| Service technicians | 800+ globally | ✅ |
| Market position | **Europe's largest door manufacturer; 4th globally** | ✅ |
| Industries served | Construction, logistics, agriculture, fire/emergency, automotive, KRITIS-adjacent | ✅ |
| Stock listing | Privately held — no public market data | ✅ |

---

## What Hörmann Makes

A diversified manufacturer of **architectural and industrial closures and access systems**, organized across product families:

| Product family | Examples | Scale |
|----------------|----------|-------|
| Garage doors | Sectional, up-and-over, roller garage doors | Millions of units; primary residential business |
| Industrial doors | Sectional industrial doors (Baureihe 60), high-speed doors, rolling shutters | Logistics centers, factories, warehouses |
| Loading systems | Loading ramps, dock shelters, loading houses | Logistics + transport hubs |
| Entrance/internal doors | Fire-rated, smoke-tight, security, multi-function doors (steel, aluminum, timber) | Commercial + KRITIS |
| Door operators (Antriebe) | SupraMatic, ProMatic, industrial door operators | Sold both standalone and integrated |
| Smart Home | Hörmann homee, BiSecur Gateway, WLAN-Gateway, BlueControl app | IoT integration with Apple Home, Alexa, Google |
| Storage systems | Hörmann Berry series | Newer product line |
| Perimeter protection | Pilomat (Italian subsidiary) — bollards, access control | Recent additions |

The product strategy unifies physical access (mechanical) with digital control (IoT, cloud, smartphone) — making Hörmann itself a connected-products manufacturer with cyber-physical risk in its own portfolio.

---

## Group Structure (the relevant entities)

The Hörmann Group consists of multiple entities with separate roles:

| Entity | Role | Relevance to sprint |
|--------|------|---------------------|
| **Hörmann KG (Holding)** | Family-owned holding company | Top-level decision authority |
| **Hörmann KG VKG** | Vertriebs- und Kunden-Gesellschaft (sales + service entity) | Customer-facing; **the Axians contract is here** |
| **HÖRMANN Informationssysteme GmbH** | Internal IT subsidiary | Operates infrastructure + software systems; MD: Uwe Reith |
| **HÖRMANN Digital GmbH** | Internal digital subsidiary | Software product solutions and enhancements |
| **ALUKON KG** | Subsidiary in Konradsreuth | Roller shutters, garage doors |
| **HUGA Hubert Gaisendrees** | Gütersloh subsidiary | Timber internal doors |
| **Schörghuber Spezialtüren KG** | Ampfing subsidiary | Construction project timber doors |
| **Pilomat s.r.l.** | Italy subsidiary | Access control / power supply stations |
| **Northwest Door, Hörmann Flexon, Hörmann LLC** | US subsidiaries | Sectional, high-speed, garage doors |
| **Hörmann Beijing / Tianjin** | China subsidiaries | Industrial sectional doors, high-speed, fire doors |
| **Shakti Hörmann** | India joint venture | Industrial doors, loading systems |

**Critical for the sprint:**
- The **Axians relationship is with Hörmann KG VKG** (sales + service entity), via Axians NEO Solutions & Technology
- The **CISO (Rian Redinger) sits at the Hörmann Deutschland group level** — broader scope than VKG
- **HÖRMANN Informationssysteme GmbH (Uwe Reith)** is the internal IT operator — the buyer for infrastructure security
- **HÖRMANN Digital GmbH** owns software product development — they understand cyber-physical security from the product side

This multi-entity structure means an outreach needs two angles: VKG (where Axians already has a relationship) and Informationssysteme/Digital (where the cyber-buying authority sits).

---

## Tech Stack Signals

Inferred from public job postings, case studies, and Exa-extracted profile data. ⚠️ Confidence varies by signal type — job postings are strong, profile aggregators less so.

### Confirmed (✅)
- **SAP ecosystem:** SAP ERP, SAP HCM, SAP Service Cloud, SAP Customer Service (CS), SAP MRS (Multiresource Scheduling), SAP Sales Cloud, SAP S/4 (likely migrating), SAP Successfactors, SAP NetWeaver, SAP Basis, C/4HANA Customer Cloud — *core ERP and CRM stack*
- **KUKA robotics** — industrial automation on factory floors (high-value Guardicore signal — OT robotics on production network)
- **SUSE Linux** as primary OS (also Microsoft Windows ecosystem)
- **Microsoft 365** and OneDrive
- **DevOps tooling:** GitLab, Ansible, Terraform, Docker, Kubernetes (modern containerized cloud)
- **Open Telekom Cloud** (M2M / IoT platform for industrial doors via Telekom MMS)
- **SoSafe** — security awareness training partner (confirmed in their public sustainability page)

### Inferred (🧠)
- **Active Directory + Azure AD** (typical for SAP + Microsoft 365 footprint)
- **VPN-centric remote access** with mobile devices (Panasonic Toughbook 19 mentioned in service tech setup)
- **Bluetooth/BLE** for service tooling (BlueControl app)
- **WLAN-centric production floors** (mentions of WiFi gateways in product lines)

### Security-related signals
- **TISAX certification** — public statement that "some HÖRMANN Group companies obtain certification in accordance with the TISAX standard" — typically required by their automotive customers (Hörmann supplies industrial doors to OEM plants)
- **ISO 27001** — partial, "some Group companies"
- **No public EDR/XDR vendor** named
- **No public SIEM** named
- **No public microsegmentation vendor** — the white space Guardicore fills

---

## NIS2 Exposure

Hörmann is an **important entity** under the German NIS2 Implementation Act, in force since 6 December 2025:

| NIS2 criterion | Hörmann situation |
|----------------|-------------------|
| Sectoral coverage | ✅ Manufacturing of mechanical/electrical equipment, specifically architectural closures and access control — Annex II "important entity" |
| Size threshold | ✅ Clearly above >€10M turnover and >49 employees |
| Registration deadline | March 6, 2026 — **status unknown, no public statement** |
| KRITIS adjacency | ⚠️ Their *products* are deployed in KRITIS facilities (fire stations, water utilities, energy infrastructure). The new **KRITIS-Dachgesetz** (KRITIS umbrella law) creates compliance pressure indirectly through Hörmann's customers |
| Article 21 obligations | Network segmentation, supply-chain security, incident reporting (24/72h/1m windows) all apply |

**The compliance squeeze:**
- Hörmann's own organization is NIS2-obligated as a manufacturer
- Hörmann's products are part of KRITIS facilities → their customers' KRITIS audits will increasingly ask about supplier cybersecurity
- Hörmann's automotive customer base (industrial doors at OEM plants) drives TISAX requirements that include network segmentation evidence

**The triple obligation:** NIS2 (own scope) + KRITIS-Dachgesetz (customer cascade) + TISAX (automotive customer cascade). All three demand documented network segmentation, all three are activating in 2025–2027.

---

## Recent News (last 12 months — May 2025 to May 2026)

✅ Verified from primary sources:

**February 2026:**
- *Facility-Manager article* (May 2026): Hörmann publishes detailed positioning on **KRITIS-Dachgesetz** compliance for door/gate operations — explicit acknowledgment that their products are part of critical infrastructure architecture
- New **NetControl Gateway** product launched: monitors industrial doors via BUS interface, integrates to local network → Hörmann's own connected-product strategy

**2024–2025:**
- Multiple Smart Home product launches: WLAN Gateway for voice-controlled gates (Alexa, Google Home, Apple Home), Hörmann homee Brain integration
- 70th anniversary (2025)
- Continued expansion of Berry storage series

**Open job postings (2026, Steinhagen + remote):**
- Product Owner SAP CX Cloud
- Product Owner Field Service Applikationen
- Solution Architekt CPQ
- BIM Manager Digitale Produktdaten
- Spezialist HR-IT-Systeme

These postings cluster around **digital service transformation** and **product information management** — the same areas Axians is already supporting via NEO Solutions.

---

## Historical Incident — The 2020 BiSecur Disclosure ⚡

In October 2020, **SEC Consult publicly disclosed multiple critical vulnerabilities** in Hörmann's BiSecur Gateway product (remote garage door control over WiFi/internet). The vulnerabilities included:

- Hardware: Unprotected flash memory storing user credentials and SSL keys in plain text; unprotected debug interface allowing firmware extraction
- Local network: Custom protocol prone to MITM; default hardcoded credentials; buffer overflow in user creation; guessable session numbers
- Server: Backend allowing impersonation of arbitrary devices — "*an attacker can steal credentials of ALL BiSecur Gateways worldwide*"
- Recommendation: "*Complete framework redesign including hardware, protocol, server functionality*"

**Hörmann's response was prompt:**
- Immediately disabled registration on the BiSecur portal
- **Temporarily suspended production** of BiSecur Gateways
- Highest-priority remediation by product engineering

**Why this matters for the sprint:**
1. Hörmann has direct, painful, public memory of an IoT/cyber incident
2. The incident was disclosed responsibly but it cost them a product line interruption
3. They now know their connected-products attack surface is real
4. **This is a conversation opener** — not an attack on their security maturity, but a reference point showing their team takes cyber risk seriously
5. Their subsequent investments (HÖRMANN Digital GmbH, Informationssysteme, CISO hire, SoSafe partnership) suggest organizational learning

**Stage 4 narrative use:** "Five years on from BiSecur. NIS2 changes the threshold." (Not as an accusation, but as a marker of how the regulatory environment has evolved since their team last had to think this hard about cyber.)

---

## Industrie 4.0 / Smart Factory Footprint

Hörmann has invested significantly in production digitalization:

| Initiative | Description | Source |
|------------|-------------|--------|
| HÖRMANN Digital GmbH | Internal subsidiary for software-based product enhancements | Annual report context |
| Smart Home product line | BiSecur radio + cloud, homee integration, WLAN Gateway | hoermann.de |
| Telekom MMS IoT platform | M2M Smart Module for industrial door monitoring; Open Telekom Cloud; DSGVO-compliant | telekom-mms.com |
| KUKA robotics | Factory automation (presence in tech stack) | Exa profile |
| 40+ specialized production plants | Each likely with distinct OT environments | Wikipedia |
| Predictive maintenance | NetControl Gateway → real-time data on door cycles, error states | hoermann.de |

The Industrie 4.0 footprint creates exactly the OT/IT convergence pattern Guardicore is built to address: dozens of factories, each with their own production network, increasingly interconnected to centralized cloud and ERP, with security architecture that has grown organically.

---

## What Stage 2 Could Not Verify

Honest documentation of blind spots (❌):

- Exact 2024/2025 revenue (privately held; "over €1B" is the closest public number)
- Whether Hörmann has registered with the BSI under NIS2 (registration list is not public)
- Specific incumbent security vendors (firewall, EDR, SIEM)
- Whether Akamai has any prior engagement with Hörmann (very low probability)
- The internal Axians cross-portfolio routing process (how does an Axians NEO account manager hand off to Axians IT Security Services?)
- Exact split of revenue across business units
- Internal CISO budget, headcount in HÖRMANN Informationssysteme

These gaps would be filled by a first conversation, not by further public research.

---

## Why This Account Belongs in the Final 3

Cross-reference against the ICP and scoring matrix:

| Criterion | Score | Justification |
|-----------|-------|---------------|
| C1 — NIS2 obligation | 5 | Triple obligation: NIS2 + KRITIS-Dachgesetz cascade + TISAX cascade |
| C2 — OT/IT convergence | 5 | 40+ factories, KUKA robotics, IoT product platform, multi-cloud, public BiSecur incident history |
| C3 — Revenue band fit | 4 | €1B+ at upper edge — slightly above sweet spot but acceptable |
| C4 — Axians reachability | 5 | Confirmed customer since 2014 via Axians NEO Solutions; multiple ongoing projects |
| C5 — Security signals | 4 | Public CISO (Rian Redinger), public sustainability page on IT security, SoSafe partnership, past incident disclosure handled openly |

**Revised total: (5×0.25 + 5×0.25 + 4×0.20 + 5×0.15 + 4×0.15) × 20 = 91**

Hörmann moves from initial score 85 → revised 91 once the multiple obligation cascade and tech-stack richness are properly factored.

---

**End of Hörmann company brief.** Pain map next.
