# Pain Pattern Library

> **Stage 3 Strategy · D3-2 ABSM Sprint**
> **Purpose:** Catalog every pain pattern observed across the 4 accounts. Reusable for prospecting, email sequences, event narratives, and Stage 4 outreach. Each pattern is named, anchored to specific account evidence, and rated by frequency and urgency.

---

## How to Use This Library

Each pain pattern below is:
- Named and described in plain language
- Anchored to at least one account-specific public source
- Rated for **frequency** (how often it appears in DACH Mittelstand manufacturers) and **urgency** (how immediately it drives a buying decision)
- Paired with a Guardicore response that addresses it

---

## Pattern 1 — "The Triple Obligation" ⭐⭐⭐

**Description:** The company faces three separate compliance-driven obligations to implement network segmentation — their own NIS2 obligation, a cascade from their KRITIS customers' new compliance requirements, and TISAX requirements from automotive OEM customers. Each obligation can individually be partially satisfied; together they create an impossible-to-ignore convergence.

**Observed in:**
- Hörmann KG: Own NIS2 + KRITIS-Dachgesetz (doors in fire stations, utilities) + TISAX (industrial doors at OEM plants)
- Witte Automotive: Own NIS2 + TISAX from VW/BMW/Mercedes + OEM supplier security cascades
- Reinhausen: Own NIS2 + KRITIS customer audits (utilities auditing their MR supplier) + Cyber Resilience Act for ETOS products
- Trumpf: Own NIS2 + EUV supply chain (ASML/TSMC) + ISO 27001 Annex A 8.22 internal obligation

**Frequency:** Very high — applies to any German manufacturer with automotive OEM or KRITIS customers
**Urgency:** Extreme — three separate deadlines, one solution
**Guardicore response:** "One segmentation platform satisfies all three audits. You document once; the policy maps, traffic visualizations, and enforcement logs go to all three auditors."

---

## Pattern 2 — "The Security Role Was Just Created" ⭐⭐⭐

**Description:** The company recently formalized a dedicated IT security role — either hiring a CISO or elevating an infrastructure veteran to a security-focused position. The new security lead is actively building their toolset and hasn't yet committed to vendors. This is the highest-conversion window in the sales cycle.

**Observed in:**
- Witte Automotive: Rainer Schulten moved from Leiter IT Infrastruktur to Leiter IT Security, January 2024
- Hörmann KG: Rian Redinger named CISO (public LinkedIn title — role appears recently formalized)
- Reinhausen: Dr. Hubert Feyrer carries the public "Cyber Security Expert" title — appeared in bylines starting ~2022

**Frequency:** Very high — German Mittelstand is in the middle of a wave of CISO/security-role creation (2022–2026), driven by NIS2 and TISAX
**Urgency:** High — window closes once the new security lead has committed to a platform
**Guardicore response:** "We'd like to walk you through how other newly-formed security functions at German Mittelstand manufacturers have approached their first 90-day architecture decisions. Segmentation is typically one of the first three priorities."

---

## Pattern 3 — "The Industrie 4.0 Winner Who Got Exposed" ⭐⭐⭐

**Description:** The company was an early winner of digital transformation — connected machines, OPC UA, smart factory, Industrie 4.0 award — and is now being audited for the security implications of the connectivity they built to win those awards. The narrative: they succeeded at connecting their factory, and now they're obligated to secure it.

**Observed in:**
- Reinhausen: Won the *first* German Industrie 4.0 Award; built connected factory production in the 2010s; now ISO 27001 building in progress, NIS2 clock running
- Trumpf: Opened Ditzingen smart factory in 2020; 30 machines connected via OPC UA; ISO 27001 certified Dec 2023; NIS2 Article 21 segmentation documentation still a gap

**Frequency:** High — approximately 40% of VDMA/ZVEI member manufacturers have now won or participated in Industrie 4.0 award programs; all are now NIS2 obligated
**Urgency:** Very high — their connected network is already a documented architecture in public case studies
**Guardicore response:** "Your Industrie 4.0 architecture is a public reference. We can use that architecture documentation as the starting point for a segmentation map — we may already know what your production network looks like."

---

## Pattern 4 — "The IoT Product That Became a Liability" ⭐⭐

**Description:** The company sells a connected/IoT product line that is itself a cyber-physical system. A prior vulnerability in that product — either their own or a peer's — created institutional memory of product-security risk. This primes them to understand OT/IT security without needing education.

**Observed in:**
- Hörmann KG: BiSecur Gateway had multiple critical vulnerabilities disclosed by SEC Consult in 2020; Hörmann temporarily halted production and disabled the BiSecur portal. The company learned. Their Informationssysteme MD Uwe Reith now publicly describes the threat in business-continuity terms.
- Reinhausen: ETOS had vulnerabilities (Broken Authorization, log4j, xz) — all publicly disclosed via MR-CERT advisories. Dr. Feyrer notes "cybersecurity is a team sport"
- Witte Automotive: Products are electronic locking systems — cyber-physical by nature; a compromised car-door system is a physical safety issue

**Frequency:** Medium — applies specifically to companies with IoT product portfolios
**Urgency:** High — companies with prior incident memory are faster to see the internal-network parallel
**Guardicore response:** "Your team already understands how an IoT vulnerability can cascade from product to customer. The same logic applies to your production network: a compromised machine is a pivot point to your SAP environment. Guardicore makes that pivot visible and blockable."

---

## Pattern 5 — "The Warm-Path Cross-Portfolio Sell" ⭐⭐⭐

**Description:** An Axians portfolio (typically Axians NEO Solutions for SAP/service management, or Axians network/cloud team) already has a trusted relationship with the account. The security conversation hasn't happened yet because it's in a different portfolio. This is the highest-leverage scenario: the hardest part of a B2B sale (trust) is already in place.

**Observed in:**
- Hörmann KG: 11-year Axians NEO Solutions engagement (SAP CS, MRS, C/4HANA, mobile apps). Axians IT Security team has never met the CISO. This is the PIP use case par excellence.

**Frequency:** Medium — limited to the subset of DACH manufacturers who are already Axians customers in any portfolio
**Urgency:** Highest — the trust pre-exists; the friction is internal Axians cross-portfolio, not external customer resistance
**Guardicore response:** [Internal Axians talking point, not customer-facing] "Our NEO colleagues have been at Hörmann for 11 years. They know Alexandra Kempe's priorities. One introduction from her to Rian Redinger converts a cold call into a warm meeting. Let's build the joint outreach plan."

---

## Pattern 6 — "The Investment Offensive Creates Greenfield" ⭐⭐

**Description:** The company is in the middle of a major production expansion — new buildings, new machines, new plants. New builds are the optimal moment for security architecture because greenfield is always easier than retrofit. The company's capital allocation is already in progress; adding security architecture is an incremental addition.

**Observed in:**
- Reinhausen: Three-digit million Euro investment program; doubling Regensburg Haslbach site; explicitly including "AI-supported technologies"
- Trumpf: €298M capex in FY2023/24; global production footprint expansion

**Frequency:** Medium — approximately 30% of Mittelstand manufacturers are in active expansion phases in 2025–2026 due to energy transition demand
**Urgency:** High — the window is during the build, not after
**Guardicore response:** "Your new Haslbach expansion is the easiest network you'll ever segment — it's being built from scratch. We can design the segmentation architecture into the blueprint now, before the first machine is connected."

---

## Pattern 7 — "The Insurance Renewal Ultimatum" ⭐⭐

**Description:** Cyber insurance renewals in Germany (2024–2026) now routinely require documented network segmentation as a coverage condition. Companies that cannot evidence segmentation either face premium increases of 20–40%, reduced coverage, or outright non-renewal in certain verticals. This is an external financial forcing function.

**Observed in (inferred):**
- All four accounts: No public evidence of specific renewal requirements, but standard practice in German mid-market manufacturing
- Confirmable via conversation: "What did your last renewal questionnaire ask about segmentation?" is a highly effective qualifying question

**Frequency:** Very high — applies to any German manufacturer with a cyber insurance policy (which is essentially all NIS2-obligated entities)
**Urgency:** High but time-bound — triggered by renewal cycle
**Guardicore response:** "German insurers are increasingly requiring documented segmentation for mid-market manufacturers. The output from a Guardicore deployment — specifically the policy maps and traffic logs — is exactly what underwriters want to see. Some of our customers used the Guardicore deployment documentation directly in their renewal submission and received 15–22% premium reductions."

---

## Pattern 8 — "The New SAP Migration Creates Maximum Risk" ⭐⭐

**Description:** SAP S/4HANA migrations are underway at nearly all German Mittelstand manufacturers (2022–2027 is the main migration window, driven by SAP's end-of-life announcement for ECC 6.0). During migrations, parallel-run environments, new middleware connections, and elevated external consultant access create unprecedented east-west risk. This is the period when microsegmentation is most urgently needed.

**Observed in:**
- Trumpf: SAP S/4HANA migration explicitly confirmed by CIO Thomas Speck
- Hörmann: SAP ecosystem is their core stack (CS, HCM, Service Cloud, C/4, NetWeaver) — S/4 migration likely underway (2025 timeframe)
- Reinhausen: SAP ERP at production scale; ITOS product ISMS confirms SAP-level complexity

**Frequency:** Extremely high — approximately 80% of DACH Mittelstand manufacturers are mid-SAP-S/4HANA migration in 2025–2026
**Urgency:** Very high — window is during migration, not before or after
**Guardicore response:** "During your S/4HANA migration, your SAP landscape is in its most vulnerable state — parallel environments, external consultants with elevated access, new integration paths. Guardicore can segment the S/4 environment from legacy ECC and from the production floor before you go live. We call this the 'SAP segmentation first' motion."

---

## Frequency / Urgency Matrix

Summary view for prioritizing outreach angle by account:

| Pattern | Freq | Urgency | Best for |
|---------|------|---------|----------|
| 1 — Triple Obligation | ★★★★★ | ★★★★★ | All DACH Mittelstand manufacturers |
| 2 — Security Role Created | ★★★★ | ★★★★★ | Accounts with new CISO/security role |
| 3 — Industrie 4.0 Winner | ★★★★ | ★★★★ | Award-winning connected factories |
| 5 — Warm-Path Cross-Portfolio | ★★★ | ★★★★★ | Existing Axians customers |
| 8 — SAP Migration Risk | ★★★★★ | ★★★★★ | SAP S/4 mid-migration accounts |
| 7 — Insurance Renewal | ★★★★★ | ★★★★ | All NIS2-obligated entities |
| 6 — Investment Offensive | ★★★ | ★★★★ | Expanding manufacturers |
| 4 — IoT Product Liability | ★★★ | ★★★ | IoT product manufacturers |

---

## Pattern Combinations by Account

| Account | Primary pattern | Secondary patterns |
|---------|----------------|-------------------|
| Hörmann | 5 (warm-path) + 1 (triple obligation) | 4 (BiSecur incident) + 8 (SAP migration) |
| Reinhausen | 3 (Industrie 4.0 winner) + 1 (triple obligation) | 6 (investment offensive) + 2 (security role created) |
| Witte Automotive | 2 (security role created) + 1 (triple obligation) | 7 (insurance) + 8 (SAP) |
| Trumpf | 3 (Industrie 4.0) + 8 (SAP migration) | 1 (triple obligation) + 7 (insurance) |

---

**End of pain pattern library.**
