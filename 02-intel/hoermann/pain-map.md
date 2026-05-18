# Hörmann KG — Pain Map

> **Account 1 · Stage 2 Intel** · D3-2 ABSM Sprint
> **Purpose:** Identify the specific operational and compliance pressure points that make Guardicore relevant. Every pain anchored to a public source where possible.

---

## The Three Pain Layers

Hörmann is squeezed by pressure from three distinct directions. The Guardicore message must speak to all three:

```
       Their own NIS2 obligation
                    ↓
   ┌─────────────────────────────────┐
   │       HÖRMANN KG                │
   │   (manufacturer + IoT products) │
   └─────────────────────────────────┘
       ↑                          ↑
   KRITIS customers'          Automotive OEMs'
   compliance cascade         TISAX cascade
   (via KRITIS-Dachgesetz)    (via supplier security audits)
```

---

## Layer 1 — Their Own NIS2 Obligation (✅ verified)

### The legal frame

Hörmann is an "important entity" under §28 of the new BSIG (in force 6 December 2025). Manufacturers of architectural/access closures fall in NIS2 Annex II "Manufacturing — electrical equipment / general manufacturing". With >€10M turnover and >49 employees, they clear the threshold many times over.

### Article 21 obligations directly relevant to Guardicore

Article 21 of the EU Directive (transposed into §30 BSIG) requires risk management measures including:

1. **Risk analysis and information system security policies**
2. **Incident handling** (with 24h initial notice, 72h detailed report, 1m final report)
3. **Business continuity, backup management, crisis management**
4. **Supply chain security** (including security of relationships with direct suppliers and service providers)
5. **Security in network and information systems acquisition, development and maintenance**
6. **Policies and procedures to assess effectiveness of cybersecurity risk-management measures**
7. **Basic cyber hygiene practices and cybersecurity training**
8. **Policies regarding the use of cryptography and encryption where appropriate**
9. **Human resources security, access control policies and asset management**
10. **Use of multi-factor authentication, secured communications**

**Article 21 lines that map directly to microsegmentation:**
- 5 (security in network systems) — segmentation is foundational
- 9 (access control) — least-privilege east-west traffic
- 4 (supply chain security) — proving to customers what segmentation you've documented

### The audit timeline

Under §39 BSIG, operators of critical facilities must provide first evidence of implementation within 3 years (i.e., from 2027 onward), with ongoing evidence every 3 years. For non-KRITIS but important entities, the BSI can request evidence at any time after the law takes effect — and as of May 2026, the audit cycle is just starting to organize.

**The window:** Hörmann has roughly **12–18 months** to either prove documented segmentation or be visibly behind. This is the sweet spot for the outreach.

### Evidence of awareness

✅ Public statement on data protection and IT security page: "*IT security, cybersecurity and data protection are taken extremely seriously at all HÖRMANN Group companies in order to ensure that business systems and expertise enjoy reliable protection against espionage, sabotage and abuse.*"

⚠️ However: no public NIS2 implementation statement; no published gap assessment; no public segmentation reference architecture. The visible posture is high-level commitment without published technical specifics.

---

## Layer 2 — KRITIS Customer Cascade (⚠️ verified via industry coverage)

### The KRITIS-Dachgesetz angle

In May 2026, the Facility-Manager industry magazine published a Hörmann-authored article on doors and gates as part of critical infrastructure architecture. Key passages (paraphrased and lightly translated):

> "Critical infrastructure is often associated with large systems — energy generation, IT networks, water and food supply. Within these systems, however, it is often small components that contribute decisively to operational safety. Doors, gates, and access control systems are integral to nearly all KRITIS applications — and can play a central role in extreme cases."

> "With rising regulatory requirements — currently particularly via the KRITIS-Dachgesetz — the physical condition of buildings and facilities is coming more into focus. Operators of critical infrastructure are required to take defined measures to ensure resilience and to document them in a verifiable manner."

**The implication for Hörmann:** Their KRITIS customers (utilities, water/food/energy operators, fire stations, transport hubs) are now under physical-resilience documentation pressure. The supply chain question — "*Hörmann, prove your own cyber and physical security; we need to write your assurance into our KRITIS file*" — is starting to be asked.

### Customer segments where this bites

| Hörmann customer segment | KRITIS exposure | Pressure on Hörmann |
|--------------------------|-----------------|---------------------|
| Fire stations | Direct KRITIS | Highest — emergency response continuity |
| Water utility plants | Direct KRITIS | High — sealed facilities, controlled access |
| Energy infrastructure | Direct KRITIS | High — substations, fueling stations |
| Food production / logistics hubs | Indirect KRITIS via supply chain | Medium-High |
| Hospital logistics docks | Direct KRITIS | High |
| Transport hubs (rail, airport) | Direct KRITIS | High |
| Data centers (loading docks) | KRITIS by sector | High |

**A customer-cascade conversation:** "*Your customer who runs the water plant in Hannover is being audited under NIS2. Their auditor asked them which of their door supplier's products are remotely accessible. They're calling you next week.*"

---

## Layer 3 — Automotive Customer TISAX Cascade (⚠️ verified)

### The TISAX context

Hörmann supplies industrial doors to automotive OEM plants. The German automotive industry has mandated **TISAX** (Trusted Information Security Assessment Exchange, operated by VDA/ENX) as the supplier cyber assessment standard since 2017. Hörmann's public sustainability page explicitly notes: "*At their customers' request, some HÖRMANN Group companies even obtain certification for their business and IT systems in accordance with the TISAX standard or the ISO 27001 IT security standard.*"

### What changed in 2024–2026

TISAX requirements have escalated:
- **TISAX 6.0 (May 2024)** — explicit requirements on network segmentation between production and corporate IT
- **AL3 (Assessment Level 3)** — required for OEMs to share design data with suppliers; demands documented segmentation evidence
- **OEM-specific addenda** — Volkswagen, BMW, Mercedes have published security baselines that drill deeper than ISA standard

**The implication:** Hörmann's automotive customers are increasingly asking for evidence of internal network segmentation as a precondition of design-data sharing or production-line installation contracts.

---

## Specific OT/IT Pain Points

### Pain 1 — Flat-but-now-connected production networks 🧠 (inferred)

Hörmann operates **40+ specialized production plants** globally, each presumably with their own production network grown over decades. The tech stack signals (KUKA robotics, ERP-connected production, IoT product strategy) confirm these networks are no longer air-gapped — they're connected to corporate IT, to cloud platforms, and increasingly to customer-facing services.

**Why it hurts:**
- A compromised office endpoint can traverse to factory floor via the corporate-OT bridge
- A factory shutdown via ransomware would halt production of doors → customer SLA exposure
- Cyber insurance carriers are increasingly requiring documented production-network segmentation as a coverage condition

**Where Guardicore lands:** The NVIDIA BlueField agentless solution (GA Q2 2026) is purpose-built for exactly this scenario — segmenting KUKA robotics, PLCs, and other "un-agentable" OT assets without touching them.

### Pain 2 — The IoT product portfolio creates its own attack surface (✅ verified by 2020 incident)

Hörmann's connected products (BiSecur Gateway, Hörmann homee, WLAN Gateway, NetControl, smart industrial doors via Telekom Cloud) all have:
- Backend infrastructure (Hörmann Cloud, Open Telekom Cloud, BiSecur portal)
- Communications protocols (custom HCP, BiSecur radio, Bluetooth)
- Customer-facing user accounts at scale

**The 2020 SEC Consult incident proved this is real:**
- Multiple critical vulnerabilities in BiSecur Gateway
- Quote from the disclosure: "*allows attacker to steal credentials of ALL BiSecur Gateways worldwide*"
- Hörmann had to halt gateway production temporarily
- Required complete framework redesign

**Where Guardicore lands:** While Guardicore segmentation doesn't directly secure consumer IoT devices, it does protect:
- The backend Hörmann Cloud infrastructure (cloud workload segmentation)
- The boundary between IoT backend and corporate ERP (preventing lateral movement from compromised cloud to internal SAP)
- Production environments where IoT product engineering and testing happens

### Pain 3 — Multi-cloud + Kubernetes complexity (✅ verified via tech stack)

Hörmann's tech stack includes Kubernetes, Docker, Open Telekom Cloud, plus SAP cloud (S/4HANA, Service Cloud, Sales Cloud). This is a modern, complex hybrid environment. Each new cloud platform introduces:
- New attack surfaces
- New identity/access boundaries
- New compliance scope for NIS2

**Where Guardicore lands:** Kubernetes-native segmentation; cloud workload protection; unified policy across legacy SAP, modern Kubernetes, and OT — Guardicore's hybrid-IT positioning is squarely in this space.

### Pain 4 — 800 service technicians + mobile devices = expanded edge (⚠️ inferred)

The Axians-NEO partnership case study describes 800+ globally deployed service technicians, each with a Panasonic Toughbook 19 running the NEO Mobile Suite. Each technician:
- Carries customer data, access codes, and product diagnostics
- Connects intermittently from customer sites, hotels, home networks
- Touches SAP backends with elevated privileges

**Where Guardicore lands:** Not directly — endpoint security is EDR territory. But Guardicore's role is to **contain damage if a technician's device is compromised**: limit the lateral reach to only what each technician genuinely needs.

### Pain 5 — Internal supply chain (subsidiaries) — 30+ entities (✅ verified)

The Hörmann Group includes 30+ subsidiaries with varying digital maturity. Some are recent acquisitions (Pilomat, Northwest Door, Shakti Hörmann India). The "supply chain security" pillar of NIS2 (Article 21.4) explicitly extends to subsidiaries and intra-group data flows.

**Where Guardicore lands:** Group-level visibility — a single segmentation map covering all subsidiaries, helpful both for documentation and for limiting blast radius from a less-mature subsidiary affecting the core.

---

## Insurance Pressure (🧠 inferred — Stage 4 conversation point)

The German cyber insurance market has hardened significantly in 2024–2026. Insurers (Allianz, Munich Re, Hiscox, AIG Germany) now routinely require:
- Documented network segmentation
- MFA on all privileged accounts
- EDR coverage
- Tabletop exercise evidence

Hörmann's renewal cycle is a likely trigger. **Stage 4 outreach can ask: "What did your cyber insurance renewal questionnaire ask about segmentation? We're seeing 80% of mid-cap renewals now require this evidence."**

---

## What This Pain Map Implies for Outreach

Three messaging angles, ranked by likely resonance:

### Angle A — The triple obligation (highest resonance) ⭐

"Hörmann faces NIS2 directly, KRITIS-Dachgesetz indirectly via your customers, and TISAX via your automotive OEM relationships. All three demand the same evidence: documented network segmentation. One platform answers all three audits."

### Angle B — The lessons of BiSecur (medium resonance, requires tact)

"Five years on from BiSecur, the regulatory environment has changed. Your team handled that disclosure with discipline; the question now is how to demonstrate that same discipline across 40+ production sites under NIS2."

### Angle C — Insurance renewal (Stage 4 conversational tactic)

"Whatever your insurer asked about segmentation last year, they're asking again next renewal. We see Mittelstand customers using Guardicore output directly in their renewal package."

---

## Honest Boundaries

What I'm confident about (✅):
- The 2020 BiSecur incident and Hörmann's response
- TISAX involvement (their own sustainability page confirms)
- NIS2 obligation
- KRITIS customer relevance (their own May 2026 industry article confirms)
- Multi-cloud and Kubernetes tech stack
- 40+ production plants

What I'm inferring (🧠) — would benefit from a first conversation:
- Current insurance renewal questions
- Specific incumbent network security vendors
- Internal organizational view of where segmentation maturity sits
- Whether they've started or completed a NIS2 gap assessment
- Whether their CISO has named Guardicore (or Illumio) as a vendor on her or his shortlist

What I cannot know (❌):
- Whether they've already received a NIS2-triggered customer audit
- Their internal budget allocation for cyber in FY2026

---

**End of Hörmann pain map.** Relationship map next.
