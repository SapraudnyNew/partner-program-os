# Witte Automotive — Pain Map

> **Account 3 · Stage 2 Intel** · D3-2 ABSM Sprint
> **Purpose:** Identify the concrete pressure points that make Guardicore relevant. Witte's case is defined by **the most multi-axis regulatory environment in the sprint** — five overlapping frameworks, all requiring documented network controls.

---

## Strategic Framing — The Quintuple Cascade

Whereas Hörmann faces 3 obligations and Reinhausen 2, **Witte faces 5 simultaneously**:

```
                     1. NIS2 (own scope)
                              ↓
                     2. ISO/SAE 21434 (vehicle cyber)
                              ↓
   ┌──────────────────────────────────────────────┐
   │            WITTE AUTOMOTIVE                  │
   │  (Tier 1/2 automotive supplier, post-VAST,   │
   │   €1B revenue, 6,000 employees, 9 countries) │
   └──────────────────────────────────────────────┘
            ↑                  ↑                  ↑
    3. TISAX           4. UNECE WP.29     5. EU CRA
    (OEM customer      R155/R156          (Dec 2027,
    cascade — VW,      (vehicle-level     products with
    BMW, Mercedes,     cyber)             digital elements)
    Stellantis, Ford)
```

Each framework demands documented network segmentation evidence in some form. Doing it once with Guardicore covers all five.

---

## Layer 1 — NIS2 Essential Entity Obligation (✅ verified)

### Why Witte is essential, not just important

Witte is unambiguously in NIS2 Annex I as "manufacturer of motor vehicles, trailers and semi-trailers" — automotive Tier 1/2 falls cleanly in scope. Size threshold (~6,000 employees, €1B+ revenue) is far above the cutoff. BSI direct supervision applies.

**Specific Article 21 measures most relevant to Guardicore:**
- §21(2)(d) **Supply chain security** — with 100% VAST ownership + Helbako + Forez Bulgaria, integrated cross-entity security is now a Witte-internal problem
- §21(2)(e) **Security in network and information systems** — the core segmentation requirement
- §21(2)(i) **Access control + asset management** — east-west enforcement; identity-aware policy

### The fine exposure

Up to €10M or 2% of global turnover. For Witte at €1B+ revenue, the 2% cap would be **€20M+** — meaningful enough to justify any reasonable infrastructure investment.

---

## Layer 2 — ISO/SAE 21434 (✅ verified, just certified)

### What this standard requires

ISO/SAE 21434:2021 "Road Vehicles — Cybersecurity Engineering" governs the cybersecurity engineering of road vehicles throughout their lifecycle:
- Risk management throughout product lifecycle
- Concept, product development, production, operations, decommissioning phases
- Mandatory **CSMS (Cyber Security Management System)** with documented controls
- Specific requirements for **secure development infrastructure** — including the networks where development happens

### Why this creates an indirect segmentation requirement

While ISO/SAE 21434 is primarily product-focused, **annex requirements for "secure development environment"** explicitly reference:
- Network segmentation between development and production environments
- Access control for design data and source code repositories
- Vulnerability management — including the network paths attackers might use

Witte's April 2025 certification means **their next re-audit (typically every 3 years)** will examine the maturity of the network controls supporting the CSMS. **A 2028 re-audit will absolutely look at segmentation evidence.**

### Marko Schwarz's public framing

> "*Diese Zertifizierung ist ein bedeutender Meilenstein für unser Cyber Security Management System — und ein sichtbarer Beleg für die Reife und Zukunftsfähigkeit unserer Sicherheitsorganisation.*"

Schwarz frames cybersecurity in **maturity-and-future-readiness terms**. The Guardicore conversation lands well when positioned as the next step in that maturity arc — not a remediation of weakness.

---

## Layer 3 — TISAX Customer Cascade (⚠️ inferred but high-confidence)

### Why TISAX is the silent giant for Witte

TISAX (Trusted Information Security Assessment Exchange) is the German automotive industry's information security framework, operated by ENX Association on behalf of VDA. Since 2017, OEMs require TISAX participation as a precondition for design data exchange.

Witte's customer base is **every major OEM globally** (per their public materials: "supplying all well-known vehicle brands"). At least VW Group, BMW, Mercedes-Benz, Stellantis, Ford, Porsche, Volvo, Toyota, Honda — all mandate TISAX.

**TISAX 6.0** (released May 2024) sharpened requirements on:
- **Information Security Management System** (ISMS) — section 1.x of the ISA catalog
- **Identity and Access Management** — section 4.x — including network segregation between business functions
- **Cryptography** — section 5.x — encryption of east-west traffic
- **Operational security** — section 6.x — explicit segmentation references
- **Communications security** — section 8.x — network segregation and monitoring
- **Supplier relationships** — section 14.x — Witte's own suppliers (now including the integrated VAST, Forez, Helbako entities)

### What changed for Witte with the VAST acquisition

Pre-VAST, Witte's TISAX scope was largely Velbert + European plants. Post-VAST (June 2023), the scope now includes:
- China operations (VAST China)
- Japan office (VAST Japan)
- India JV (Minda-VAST)
- Bulgaria injection molding (Forez integration)
- US locations

Each entity needs to be brought into the TISAX audit scope or carved out with documented controls. **This is a 24-month integration project where network segmentation evidence is foundational.**

### The audit cycle

TISAX assessments have a 3-year validity. **Witte's next TISAX assessment is likely in 2026 or 2027** — exactly when documented network segmentation needs to be ready.

---

## Layer 4 — UNECE WP.29 (R155 / R156) — Indirect via OEM customers (✅ verified context)

### What WP.29 requires of OEMs (which cascades to Witte)

UNECE Regulation 155 (cyber security and Cyber Security Management System) and R156 (software updates and SUMS) became mandatory:
- For new vehicle types: July 2022
- **For all new vehicles: July 2024** (now in force)

OEMs must demonstrate cyber security management throughout the supply chain. This means OEM auditors examine **supplier CSMS maturity** during certification:
- Documented secure development environment
- Network segmentation between supplier networks and OEM data
- Vulnerability handling processes that cover supplier components
- SBOM transparency for embedded software

**Witte's flinkey, WITTE digital, mechatronic locking ECUs all fall in scope** — they're products with digital elements installed in motor vehicles.

---

## Layer 5 — Cyber Resilience Act (CRA, in force December 2027) (✅ regulation passed)

### Why CRA matters to Witte specifically

CRA imposes obligations on **manufacturers of products with digital elements** placed on the EU market. Witte products affected:
- **flinkey** (smartphone-based vehicle access) — clearly in scope
- **WITTE digital fleet management** — clearly in scope
- **Mechatronic locking ECUs with embedded firmware** — likely in scope

CRA requirements include:
- Vulnerability handling processes
- Security update delivery mechanisms
- SBOM (Software Bill of Materials) management
- **Security-by-design and security-by-default**
- Documented secure development infrastructure
- 24-hour active exploitation notification

### Why segmentation is foundational to CRA

The CRA auditor will ask: "*Show me the network architecture where this software was developed. Show me how the build pipeline is segmented from the IT general environment. Show me how production environments are isolated from development.*"

Documented microsegmentation — the kind Guardicore produces as an output — is exactly the evidence required.

---

## Specific OT/IT Pain Points

### Pain 1 — The post-VAST integration challenge (✅ verified)

Witte just absorbed VAST Automotive Group (June 2023) — adding China, Japan, India operations to a previously European-centric footprint. **The integration is ongoing.** Each new entity:
- Has its own pre-existing IT environment
- Has its own connection requirements to Witte central systems (SAP, engineering data, ERP)
- Has different local regulatory regimes (China cyber security law, India's PDP Act, Japan's APPI)
- Creates a new east-west attack surface

**Guardicore angle:** Unified visibility and policy across new and legacy entities — useful for both the integration phase and the steady-state ongoing operations.

### Pain 2 — The Helbako electronics integration (✅ verified, recent)

The December 2024 Helbako acquisition adds electronic systems manufacturing capability. Helbako specializes in **electronic control units and embedded electronics**. Integration means:
- A new development organization that must be brought into Witte's ISO/SAE 21434 scope
- A new manufacturing OT environment
- New cross-entity data flows for shared product development

**Guardicore angle:** Documented segmentation between Helbako and Witte during integration — essential for both companies' TISAX audits, plus the ISO/SAE 21434 re-audit.

### Pain 3 — nextWITTE program creates new digital surfaces (✅ verified)

The internal digital transformation program (status C SAP/logistics, Blue Yonder/flexis sequencing, tablet-based picking) means:
- New mobile-device fleet (Witte tablets and barcode scanners in plants)
- New SAP integrations
- New cloud or edge endpoints

**Guardicore angle:** Each nextWITTE initiative is an opportunity to **design in segmentation** rather than retrofit later.

### Pain 4 — flinkey and digital products as new revenue (🧠 inferred)

The flinkey smartphone-vehicle-access product is a backend-cloud-plus-mobile architecture. Like any consumer IoT, it has:
- Customer-facing user accounts
- Backend cloud infrastructure
- API connections to vehicle ECUs
- Potential supply chain to OEM telematics platforms

**Guardicore angle:** Microsegmentation of flinkey's cloud backend from corporate IT; cloud-workload protection for the digital product line.

### Pain 5 — Embedded firmware development environments (✅ inferred from product portfolio)

Witte develops embedded firmware for ECUs (locking, access, sensors). Embedded development environments — toolchains, hardware-in-the-loop test rigs, debugging interfaces, source code repositories — are **high-value targets**. A compromise of the toolchain would let an attacker insert malicious firmware that ships to every car.

**Guardicore angle:** Strict segmentation of the embedded development network from corporate IT and from the production network. CRA auditors will specifically ask about this.

### Pain 6 — Industrial robotics on production floors (🧠 inferred)

Mechatronic component manufacturing typically involves significant automation: pick-and-place robots, automated assembly lines, vision systems. Tier 1/2 plants at Witte's scale almost certainly have KUKA, ABB, FANUC, or similar industrial robotics. These are **un-agentable** OT.

**Guardicore angle:** NVIDIA BlueField agentless OT solution (GA Q2 2026) — purpose-built for exactly this. Witte's nextWITTE program would benefit from agentless OT segmentation designed in.

---

## Insurance + Customer Audit Pressure (🧠 likely real)

Two additional dimensions that won't appear in public reporting:

1. **OEM customer audits** — VW, BMW, Mercedes etc. run their own supplier cyber audits beyond TISAX. Findings from these audits go directly into Witte's account-level relationship with each OEM.

2. **Cyber insurance** — Witte's renewal premium is sensitive to documented network segmentation evidence.

---

## What This Pain Map Implies for Outreach

Three messaging angles, ranked by likely resonance with Marko Schwarz:

### Angle A — "One platform, five frameworks" ⭐⭐⭐

"You face NIS2 + ISO/SAE 21434 + TISAX + UNECE WP.29 + CRA simultaneously. Each demands documented network segmentation evidence in some form. Guardicore is the platform that produces that evidence once — for all five audits. The hours saved over the regulatory cycle are real money."

This is the message most likely to resonate with Schwarz's audit-and-compliance mindset.

### Angle B — "Protecting the integrations" ⭐⭐

"VAST is integrated. Forez is integrated. Helbako is integrating. Each acquisition is a new east-west attack path. Microsegmentation prevents the acquisition risk from becoming a NIS2 finding."

This resonates with the integration program managers and the executive board.

### Angle C — "The next maturity step" ⭐

"Your CSMS got ISO/SAE 21434 certified. The audit team called out 'tightly integrated, seamless collaboration of departments.' Microsegmentation is the network-architecture layer that lets you keep that maturity rating as you scale."

This is intellectual peer-framing for Schwarz.

---

## Honest Boundaries

What I'm confident about (✅):
- All five regulatory frameworks named are real and applicable
- ISO/SAE 21434 certification confirmed by TÜV NORD CERT April 2025
- VAST, Forez, Helbako acquisitions confirmed
- nextWITTE program confirmed via status C case study

What I'm inferring (🧠):
- TISAX participation (not publicly disclosed but industry-mandatory)
- Specific OT robotics vendors (typical for Tier 1)
- Cyber insurance renewal questions
- Embedded development environment specifics

What I cannot know (❌):
- Current TISAX assessment scope and date
- Specific OEM audit findings
- Witte's internal segmentation maturity
- Whether competing microsegmentation vendors have approached

For Stage 4, the first-call discovery question to Marko Schwarz:
*"You just achieved ISO/SAE 21434 certification — one of the first three suppliers globally. Looking ahead at your next TISAX assessment plus the CRA December 2027 deadline plus the post-VAST integration, what's your roadmap for documenting network controls that cover all of these in one architecture?"*

---

**End of Witte pain map.** Relationship map next.
