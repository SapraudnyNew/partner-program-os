# Maschinenfabrik Reinhausen (MR) — Pain Map

> **Account 2 · Stage 2 Intel** · D3-2 ABSM Sprint
> **Purpose:** Identify the concrete pressure points that make Guardicore relevant. Reinhausen's case is different from Hörmann's: they have *more* cyber maturity, not less. The pain pattern is **adjacent strength, not deficiency**.

---

## Strategic Framing — Reinhausen Is Different

Most ABSM accounts have a security maturity gap that Guardicore plugs. Reinhausen does not have an obvious deficit — they have a mature product security program (MR-CERT, BDEW compliance, ETOS ISMS in progress). The Guardicore conversation here is **complementary, not corrective**:

> "You've built world-class product security around what your transformers do *out there* in customer substations. NIS2 now asks the same engineering rigor of what happens *in here* — corporate IT, manufacturing OT, and the cloud links between them."

This is a more sophisticated, peer-to-peer technical conversation, not a wake-up-call. The buying motion will be **specification-led** (Dr. Feyrer's team will rigorously evaluate technical fit) rather than **threat-led**.

---

## The Three Pain Layers

```
        Their own NIS2 obligation
        (essential entity, Annex I)
                    ↓
   ┌────────────────────────────────────────────┐
   │       MASCHINENFABRIK REINHAUSEN           │
   │   (KRITIS supply chain at universal scale) │
   └────────────────────────────────────────────┘
       ↑                          ↑
   Utility customer            S/4HANA + investment
   KRITIS audits ask           offensive expanded
   about MR supply             the IT/OT attack
   chain compliance            surface massively
```

---

## Layer 1 — NIS2 Essential Entity Obligation (✅ verified)

### Why MR is an essential entity, not just important

MR is unambiguously **essential** under §28 BSIG Annex I. Their products are manufacturer-of-record equipment for the energy distribution sector. The size threshold (>250 employees, >€50M revenue) is met by orders of magnitude (~5,400 employees, €1.2B revenue).

Essential entity status means:
- BSI direct supervision authority
- Audits at any time, with prior notice; on-site permitted
- Highest fine band: **up to €10M or 2% of global turnover** — for MR, the cap would be ~€24M
- Mandatory incident reporting with the tightest 24/72/30-day cascade
- C-level personal liability (§38 BSIG) — Dr. Maier-Scheubeck and his board are personally exposed

### Article 21 measures with direct segmentation relevance

| Article 21 measure | What it asks of MR | Guardicore relevance |
|--------------------|---------------------|----------------------|
| §21(2)(a) Risk management policies | Documented risk register including segmentation gaps | Guardicore visualization = the document |
| §21(2)(d) Supply chain security | Evidence that MR's *suppliers* and the integration with their *customers* is secured | Microsegmentation between SAP, partner clouds, and customer-facing TESSA platforms |
| §21(2)(e) Security in network systems | The literal requirement — segmented networks, controlled east-west | Guardicore native scope |
| §21(2)(h) Cryptography | TLS, encrypted east-west tunnels | Layered with segmentation |
| §21(2)(i) HR security + access control | Least-privilege enforced via network policy | Identity-aware segmentation |
| §21(2)(j) MFA + secured communications | Application-level | Foundation underneath |

### The audit window

§39 BSIG requires **first evidence of implementation within 3 years** for essential entities (so by ~December 2028). But the BSI has explicit authority to request evidence *at any time* once the law is in force. **Practically:** MR's first real audit interaction is likely 2026–2027. The window to have documented segmentation in the audit dossier is now.

---

## Layer 2 — KRITIS Supply Chain Cascade (✅ verified)

### Every MR customer is KRITIS

This is the unique feature of Reinhausen's position. Whereas Hörmann's customers are *sometimes* KRITIS, **Reinhausen's customers are essentially always KRITIS:**

- Transmission System Operators (TSOs): TenneT, 50Hertz, Amprion, TransnetBW (all KRITIS in DE)
- Distribution System Operators (DSOs): every utility serving >500,000 households (KRITIS threshold)
- Transformer manufacturers: themselves KRITIS suppliers (Siemens Energy, Hitachi Energy, GE Vernova, Hyundai)
- Industrial grid operators: large industrial sites with private grids (chemical parks, steelworks, automotive plants — KRITIS-adjacent or directly KRITIS)

This is verified by Jürgen Ach (Director of Automation) in his Power Systems Technology interview: he describes a TenneT project where MR is wiring up a substation with their ETOS system, connected to SCADA on one side and asset-management cloud on the other.

### What KRITIS audits now ask about suppliers

Since the 2023 amendments to the IT-SiG and the 2025 KRITIS-Dachgesetz, KRITIS operator audits explicitly require:
- Documented supplier risk assessment
- Supplier breach notification SLAs
- Evidence that critical equipment vendors have demonstrable cyber controls
- Specifically for SCADA-connected equipment: evidence of network-level controls between vendor cloud and operator network

**MR's exposure:** Every time a TSO or DSO renews or expands an MR contract, the procurement process now includes a supplier-cyber questionnaire. The answers must satisfy the operator's own BSI auditor.

> "The KRITIS auditor at our utility customer asked about the cloud architecture between ETOS in our substation and your TESSA cloud. We need documented segmentation evidence to close their finding." — *a likely Stage 4 conversation opener*

---

## Layer 3 — Internal Expansion Created New Attack Surface (✅ verified)

### Two simultaneous expansions

In 2024–2025 MR is executing **two parallel expansion programs** that materially change their IT/OT footprint:

**1. SAP S/4HANA migration** *(completed via All for One + SNP, January 2026)*
- 3,600 active SAP users on the new system (up from R/3)
- Planned 2026 expansion: SAP Fiori per process, Enterprise Search, SAP Business Technology Platform, SAP Joule (AI)
- New cloud and on-premise integration points
- New API surfaces (Fiori apps, BTP integrations)

**2. Investment offensive (three-digit-million-euro, 4-year horizon)**
- Doubling Regensburg Haslbach site → ~1,800 employees at single site
- US OLTC production expansion
- Glocalization — local value creation in regions previously centralized
- AI-supported production technologies
- New OT environments at scale

**Combined effect:** the production-network attack surface is doubling at the same time the corporate-IT integration is becoming richer. The OT/IT boundary is busier than it has ever been at MR.

### The unmeasured dimension

🧠 inferred — verifiable via Stage 4 conversation:

Internal IT segmentation tends to be a **legacy artifact** in companies that have grown through acquisition (MR has 39 associated companies in 28 countries). Segmentation policies that worked in 2010 often don't match 2025 reality. Every cross-acquisition data flow is a potential lateral path.

The investment offensive is also creating **greenfield OT environments** that would benefit from segmentation designed-in from day one — exactly the use case Guardicore + NVIDIA BlueField was built for.

---

## Specific Pain Points (concrete)

### Pain 1 — SAP S/4HANA is now the crown jewel; segmentation is the moat (✅ recent event)

The migration to S/4HANA just landed (January 2026 case study published). 3,600 users, all production data, the entire business runs through it. The platform is supported through 2040. **This is the highest-value workload to segment.** Guardicore's identity-aware microsegmentation around SAP is a textbook use case.

**Specific conversation:** "All for One brought you home on Bluefield. Who's protecting Bluefield now that the migration is complete?"

### Pain 2 — TESSA APM cloud is the bridge between MR and every utility customer (✅ verified)

TESSA APM, MR's asset performance management software (Siemens Xcelerator platform), creates a persistent data link between MR cloud infrastructure and customer (utility) IT environments. Every utility customer's KRITIS auditor will eventually ask: "What controls separate MR's tenant in TESSA from other tenants? What controls separate TESSA cloud from MR corporate IT?"

**Specific conversation:** "Segmentation between TESSA and corporate IT — and between TESSA tenants — is your customer's audit question for the next 5 years."

### Pain 3 — Industrial robotics on production floor (🧠 inferred)

MR doesn't publicly disclose robotic automation specifics, but doubling Regensburg production at scale requires modern automated manufacturing — likely KUKA, ABB, FANUC, or local German vendors (e.g. Reinhausen-area suppliers). These devices are typically un-agentable.

**Specific conversation:** Akamai + NVIDIA BlueField agentless OT solution (GA Q2 2026) is purpose-built for exactly this.

### Pain 4 — Distributed production now means distributed OT (✅ verified)

"Glocalization" — Holger Michalka's term for partial localization of value-creation steps along the supply chain. Translating: MR is moving production stages into regional facilities (US expansion is named; others likely in Brazil, China, India, UAE). Each new regional site is a new OT environment with new connectivity into central systems.

**Specific conversation:** "How do you plan to segment your new Brazilian/US/Indian production sites from each other and from Regensburg? The pattern we see in Mittelstand multinationals is that the first site gets perimeter, the second gets some segmentation, the fifth needs centrally-managed policy."

### Pain 5 — Cyber Resilience Act preparation (✅ partially verified)

Dr. Feyrer has publicly stated MR is preparing for the EU Cyber Resilience Act (CRA, in force December 2027). The CRA imposes requirements on **manufacturers of products with digital elements** — ETOS, TESSA, ISM, TAPCON all fall in scope. Compliance evidence will include:
- SBOM management
- Vulnerability handling processes
- Security update delivery
- And — increasingly — evidence of secure development infrastructure

**Specific conversation:** "Your CRA dossier will benefit from being able to show that the *infrastructure that builds ETOS* is itself segmented. Otherwise the CRA auditor will keep asking until they find a control gap."

---

## Insurance + Customer-Demand Pressure (🧠 Stage 4 hooks)

Two additional pressure points that won't appear in public reporting but are likely real:

1. **Cyber insurance renewal questions** — same as every Mittelstand at MR's scale; insurers increasingly require documented segmentation
2. **OEM customer audit cycles** — Siemens Energy, Hitachi Energy, GE Vernova, Hyundai run their own supplier cyber audits; MR is presumably in those programs

---

## What This Pain Map Implies for Outreach

Three messaging angles, ranked by likely resonance with Dr. Feyrer's team:

### Angle A — Adjacent extension of existing strength ⭐⭐

"Your ProductCERT and BDEW Whitepaper 2.0 compliance are reference-class. NIS2 + KRITIS-Dachgesetz now ask the same engineering discipline of what's between your factory floor and your cloud — east-west, not just north-south. Microsegmentation is the next-natural step in the maturity arc you've already established."

### Angle B — Timing triple-trigger ⭐

"You have three simultaneous triggers active right now: (1) S/4HANA just landed and needs hardening; (2) Regensburg is doubling at Haslbach; (3) CRA dossier preparation. Each one drives toward the same control. Doing it once for all three saves quarters of work later."

### Angle C — Customer audit cascade ⭐

"Your TSO and DSO customers' KRITIS auditors are asking about TESSA. The next contract renewal cycle is when this stops being a polite question."

---

## Honest Boundaries

What I'm confident about (✅):
- The verified investment offensive and S/4HANA migration are real, recent, and material
- The ProductCERT publications and BDEW compliance are verified
- Dr. Feyrer's identity and role as cyber security expert
- The 50%-of-global-electricity-routes-through-MR figure (MR's own public claim)

What I'm inferring (🧠):
- Specific OT robotics vendors at MR's plants
- The internal segmentation maturity at corporate IT (vs. product side)
- Whether KRITIS customer audits have already produced supplier-cyber findings against MR
- Whether MR has previously evaluated Illumio

What I cannot know (❌):
- MR's current segmentation budget for FY2026
- Internal cyber team headcount
- Specific incumbent vendors

For Stage 4 outreach, the first technical conversation question to Dr. Feyrer (in a high-quality first meeting): *"How does the segmentation story between your corporate IT, your factory OT, and your customer-facing TESSA tenants look today? Where would you draw the architecture diagram?"* Answer reveals immediately whether the white space is real.

---

**End of Reinhausen pain map.** Relationship map next.
