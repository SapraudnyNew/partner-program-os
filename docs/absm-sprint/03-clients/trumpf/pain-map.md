# Trumpf SE + Co. KG — Pain Map

> **Showcase Account · Stage 2 Intel** · D3-2 ABSM Sprint
> **Note:** As the showcase, this pain map is written at maximum analytical depth — to demonstrate what the ABSM methodology produces for a reference-class flagship at the top of Mittelstand maturity.

---

## Strategic Framing — The Mature-Account Paradox

Trumpf presents an unusual pain-map challenge: **more mature security than any other account in this sprint**, yet still exposed at specific architectural points where Guardicore adds genuine value. The outreach narrative is not "your security is poor." It's:

> "You've built an extraordinary security posture. The remaining architectural gap — production network microsegmentation at the machine level — is now exactly what NIS2 auditors and your own insurance underwriters examine."

For Trumpf, this is a peer-level technical conversation, not a remediation conversation.

---

## Pain Layer 1 — Production Network Complexity Has Outgrown the Perimeter (✅ verified)

### The architecture

Trumpf's Ditzingen smart factory (opened October 2020) has **30 connected machines** in 5,000 m² — laser cutters, bending machines, AGVs, storage systems, and control systems all communicating via **OPC UA** under the TruConnect platform. Add Chicago + Taicang smart factories, plus 90 subsidiaries in 11+ production countries.

### The gap

ISO 27001 Annex A control A.8.22 ("Segregation in networks") requires documented network segmentation. An ISO 27001 certified company has *scoped* this requirement. The question is implementation depth at the machine-to-machine and zone-to-zone level.

**Verified through Trumpf's own OT security guidance to customers** (their April 2026 Cyber Security PDF):
> "*Ensure availability through network segmentation and reduction of the attack surface. Use firewalls to protect. Use Network Access Control (NAC) to control and secure access to your network.*"

They publish this guidance to their customers. **The same recommendation applies to themselves.** Guardicore is the platform that delivers it at the granularity OPC UA environments need — identity-aware, east-west, without rearchitecting the network.

### Why perimeter isn't enough

TruConnect connects machines to MES (TruTops Fab), MES to ERP, ERP to cloud services, cloud to customer data. Each link is a potential lateral-movement path. A compromised endpoint (even a phishing click on a technician's laptop) that can reach OPC UA can reach machine controllers. **Microsegmentation interrupts this chain before it reaches production.**

---

## Pain Layer 2 — EUV Division Creates Systemic Supply-Chain Criticality (✅ verified)

### The strategic uniqueness

Trumpf is the **sole global supplier** of EUV laser sources to ASML. ASML's EUV scanners are the only tools that can manufacture <7nm chips (TSMC, Samsung, Intel). This creates a unique NIS2 dynamic:

- ASML's supply chain audits will include Trumpf's production infrastructure
- The semiconductor supply chain is under direct focus from BSI (Germany), NCSC (Netherlands), and CISA (US)
- A Trumpf production disruption would have geopolitical implications
- **This places Trumpf in the intersection of NIS2 "essential entity" + strategic industrial asset**

### Where Guardicore lands

The EUV production environment involves highly specialized, extremely high-value tooling — laser resonators, precision optics, clean-room assembly lines. These are the epitome of OT environments that need:
- Absolute east-west isolation between sub-systems
- Agentless monitoring (you cannot install agents on laser pump optics)
- Auditability for NIS2 + supply chain compliance

**NVIDIA BlueField agentless OT solution (GA Q2 2026)** was specifically designed for environments where traditional agents are not deployable. The EUV floor is the most extreme version of that use case.

---

## Pain Layer 3 — NIS2 + CRA Convergence (✅ documented by Trumpf themselves)

### What Trumpf publishes

From their April 2026 Cyber Security PDF (paraphrased):
> "With NIS-2 and the CRA, the EU is strengthening cyber security across supply chains throughout the entire product lifecycle of digital products. For many industrial companies, this means: higher requirements for security levels and responsiveness, including reporting and verification obligations; greater focus on products with digital elements; increased relevance of security updates and vulnerability management."

Trumpf has anticipated this publicly. **They're communicating it to customers** — meaning their own compliance team is actively working the same problem internally.

### The CRA angle (unique to Trumpf)

Trumpf's machine tools and lasers have embedded software, remote connectivity, OTA updates — all of which put them in **CRA Annex I Class 2** (critical default) or Class 1. The CRA's requirements for secure development environment, SBOM, vulnerability handling, and supply chain transparency all benefit from a documented microsegmentation architecture around the development and production infrastructure.

### Caleta's own public statement

Tomislav Caleta's recent LinkedIn post (paraphrased):
> "Information security is for us not a one-time project, but a permanent promise. We invest continuously in strong internal capabilities, modern systems, and regular, independent reviews."

The phrasing "modern systems" and "regular, independent reviews" is an opening for a Guardicore conversation framed as the next-generation platform for ISMS audit evidence.

---

## Pain Layer 4 — Scale of Restructuring Creates Transient Vulnerabilities (✅ verified)

### The restructuring context (FY2024/25)

Trumpf is executing a significant structural reduction:
- 430 positions cut at Ditzingen + Gerlingen + Hettingen + Höfingen
- 1,000 positions cut globally
- "Restrictive replacement policy" applied to natural attrition
- External services and new investments paused

### Why restructuring is a cyber risk moment

Three specific risks during workforce and organizational change:
1. **Departing employees with privileged access** — during large layoffs, access revocation sometimes lags; microsegmentation limits the blast radius even if access isn't perfectly revoked
2. **Contracted external services being cut** — when external IT support is reduced, visibility decreases; Guardicore's monitoring layer maintains it
3. **Systems operated with smaller teams** — reduced security operations headcount means automated enforcement (which Guardicore provides) becomes more valuable, not less

**Conversation hook:** "Your restructuring program is delivering €350M in savings. One side effect: the internal security operations workload per person has increased. Guardicore's automation reduces analyst burden while maintaining coverage."

---

## Pain Layer 5 — CDO Mathias Kammüller's Industrie 4.0 Ambition = Expanding OT/IT Boundary (✅ verified)

### Kammüller's digital vision

Kammüller's 2020 statement: "*Comprehensive digital connectivity could boost our productivity by 30 percent.*"

His CDO role owns TruConnect, TruTops Fab, and the entire Smart Factory roadmap. As Trumpf recovers from the FY24/25 cycle, the CDO's next investment priorities include (per Leibinger-Kammüller's October 2025 press conference, paraphrased):
- Electromobility
- Semiconductors and electronics
- Smart factories and services in machine tools
- Networked manufacturing and AI

Each of these expands the OT/IT boundary — more machines connected, more AI systems interacting with production data, more external service providers accessing machine telemetry. **Every expansion is a new segmentation gap unless policy-as-code is in place.**

---

## OT Security Checklist from Trumpf's Own PDF

In their April 2026 Cyber Security PDF, Trumpf publishes a checklist for their machine tool customers. Reading it self-referentially:

| Their checklist item | Guardicore's role |
|----------------------|-------------------|
| ☐ Separate production network from office IT | Native: microsegmentation between OT and IT zones |
| ☐ Use firewalls at production hall boundary | Guardicore is the enforcement engine behind the firewall policy |
| ☐ Use Network Access Control (NAC) | Identity-aware microsegmentation policy subsumes NAC for east-west |
| ☐ Secure transmission of machine data via encrypted channels | TLS + segmentation = defense in depth |
| ☐ Enable remote maintenance via secure, reliable connections | Guardicore policy controls which external sessions can reach which OT nodes |

**The punch line:** Trumpf wrote this checklist for their customers. Guardicore checks every box. When Tomislav Caleta reads it, he's reading a Guardicore use case brief.

---

## What This Pain Map Implies for Outreach

The Trumpf showcase is not an outreach plan — but if it were:

### Angle A — Mirror the guidance they publish ⭐⭐⭐

"Your April 2026 Cyber Security PDF is excellent guidance for your customers. Guardicore is the platform that implements exactly the controls you're recommending. We'd love to show you what implementation at your scale looks like."

This is self-validating, peer-respecting, and directly grounded in Trumpf's own public work.

### Angle B — EUV supply chain protection ⭐⭐

"ASML's supply chain audit cycle + the semiconductor KRITIS discussion in NCSC + BSI is converging on production network evidence. The EUV floor is the highest-value OT environment in the country. Agentless segmentation documentation is the control that satisfies the audit."

This is unique to Trumpf — not applicable to any other sprint account.

### Angle C — ISMS extension for CRA ⭐

"Your ISO 27001 ISMS covers information security broadly. CRA's requirement for secure development infrastructure documentation is the new extension. Guardicore produces the segmentation evidence that makes the CRA annex defensible."

This is technical-CISO-level content — works with Tomislav Caleta or Oliver Guthier directly.

---

## Honest Boundaries

What I'm confident about (✅): All pain points grounded in Trumpf's own public statements or verified event facts

What I'm inferring (🧠): The specific depth of implementation of each control (ISO 27001 certified, but degree of microsegmentation unknown); the exact EUV facility OT architecture (protected)

What I cannot know (❌): Whether Trumpf has already evaluated Guardicore; their specific cyber vendor spend; internal SOC architecture

For the sprint deliverable: the Trumpf pain map exists to demonstrate **the full analytical methodology** — not to guide a sales call.

---

**End of Trumpf pain map.** Relationship map next.
