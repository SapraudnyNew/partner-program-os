# Akamai Research

> **Two layers.** This file is the initial synthesis from May 2026, written before deep research executed. Useful as a scoping document and for quick-lookup data points (market sizes, regulatory facts, competitive snapshot).
>
> **For production work, use the deep research outputs in `research/outputs/`:**
> - `research/outputs/company/` - 6 files, ~30 pages: corporate fundamentals, DACH regional intelligence, cultural and operational intelligence, channel marketing organization, risks and questions, master summary
> - `research/outputs/partner-program/akamai-partner-program-dach-dossier.md` - 7-section dossier with 50 named DACH partners, displacement targets identified (KAEMI, Navixia, Computacenter), anchor partners (Deutsche Telekom Security, Bechtle, Controlware, InfoGuard), and Mittelstand recruitment candidates (SVA, Cancom, Axians)
>
> When the deep research contradicts this initial synthesis, the deep research wins.

---

## Provenance of this file

This file pre-dates the deep research missions. Written during D2-1 (initial pass) using web search across Akamai partner program documentation, BCG, IDC, Gartner, Mordor Intelligence, Grand View Research, KENSAI, ChannelDive, ChannelE2E, ChannelBuzz. Confidence varies by section.

The deep research missions in `research/outputs/` use Exa search at scale (150+ tool calls per mission) and include explicit confidence markers (✅ Confirmed, ⚠️ Single-sourced, 🧠 Inferred, ❌ Blind spot) per claim.

---

# Akamai DACH Research: Channel, Zero Trust, Competition, Regulation

Research date: May 2026. Sources: Akamai partner program documentation, BCG, IDC, Gartner, Mordor Intelligence, Grand View Research, KENSAI, ChannelDive, ChannelE2E, ChannelBuzz.

---

## 1. Akamai partner program current state

**Program:** Akamai Partner Connect (launched Q3 2025). Unified global program replacing previous fragmented regional structure. First time all partner types integrated under one framework.

**Partner types:** resellers/VARs, distributors, service providers, technology service distributors (TSDs), referral partners, ISVs (new), MSSPs (new).

**Tiers:** Select, Premier, Elite. Region-specific thresholds (EMEA has its own qualification criteria). Qualification based on revenue + certifications + annual Success Plan reviewed quarterly.

**Channel revenue:** 70% of new security business flows through resellers and VARs. Distribution channel growing 56% YoY. GSI channel growing 34% YoY. The company is actively repositioning existing direct customers to partners ("partner-first" initiative).

**Key changes in 2025-2026:**
- Consolidated multiple go-to-market tracks into single platform
- Enhanced gross margin for partners (especially on strategic products)
- Incentives heavily weighted toward new business and strategic products (Guardicore, API Security)
- Global SPIFF platform: rewards in 136 countries, 9 languages, 4 currencies
- Expanded to include ISVs and MSSPs
- Planning North American distributor expansion (major push imminent)
- Localized tiering: EMEA partners measured against EMEA benchmarks, not global

**Certification and enablement:**
- Three training tracks: Account Executive, Solutions Engineer, Solutions Architect
- Solutions Architect track includes GCSE (Guardicore Certified Solutions Engineer) and API Security Architect certifications
- Certified Service Provider programs: GCSP (Guardicore), APISP (API Security), AAP (App & API Protector)
- Certified partners can deliver: project delivery, Day-2 operations, first-line 24/7 support, security incident management, audit and compliance services for Guardicore
- Self-paced + live virtual training, hands-on labs, Ask an Expert, Akamai Test Account
- Enablement tracks specifically built for Guardicore and API Security use cases

**MDF:** proposal-based system. Available at all three tiers. Managed through partner portal Campaign Builder. MDF Guide available at partner portal.

**Partner portal:** enhanced in 2025 with deal registration, pipeline management, marketing Campaign Builder, MDF tools, asset library with in-document search, technical support ticket submission, Akamai Control Center access.

**Key quotes:**
- Paul Joseph (EVP Global Sales): "We are building a partner ecosystem that thrives on shared success." "We've designed localized tiering to be predictable and transparent."
- Dave Allen (VP Geo Sales): "70% of new security business through resellers and VARs." "We are actively positioning existing customers that may historically have done business with Akamai direct."

---

## 2. Akamai Zero Trust product portfolio

**Akamai Guardicore Segmentation:** microsegmentation platform acquired 2021. Purpose-built for Zero Trust enforcement. Gartner-recognized Representative Vendor. Capabilities: real-time east-west traffic visibility, granular workload-level policy enforcement, AI/ML-assisted policy recommendations, lateral movement prevention (ransomware containment), deployment across on-prem, cloud, hybrid, VMs, containers.

**Akamai API Security:** acquired Noname 2024. API discovery, testing, and runtime protection.

**Enterprise Application Access (EAA):** ZTNA solution. Identity-aware application access.

**Key Gartner finding (2025):** by 2027, 25% of enterprises working toward Zero Trust will use microsegmentation (up from <5% in 2025). Microsegmentation is transitioning from optional to mandatory.

**Guardicore partner opportunity:** certified partners deliver the full microsegmentation lifecycle: initial deployment, policy design, ongoing operations (Day-2), first-line support, incident management, compliance auditing. This is a recurring services business, not a one-time implementation.

---

## 3. Zero Trust market: DACH

**DACH cybersecurity market:** €18.7B in 2026, 14.2% YoY growth. Germany €13.8B (15.1% growth), Switzerland €3.2B, Austria €1.7B.

**Germany Zero Trust market:** $2.47B in 2024, projected $5.6B by 2030 (14.7% CAGR). Network security is the fastest-growing segment.

**Global Zero Trust market:** $51B in 2026 (16-19% CAGR). Projected $90B by 2030.

**Global microsegmentation market:** $21.58B in 2025, projected $62.3B by 2030 (23.62% CAGR). This is the specific market for Guardicore.

---

## 4. Regulatory pressure: NIS2 and DORA

**NIS2 (Network and Information Security Directive 2):**
- Germany: NIS2UmsuCG affects estimated 29,000 organizations (up from ~2,000 under NIS1)
- Mandates "state-of-the-art" security implementation for critical infrastructure
- Zero Trust is best practice for compliance
- Organizations allocating 15-25% more budget to cybersecurity in 2026
- Managed security services growing 40% as organizations outsource compliance
- Automated security testing: fastest-growing segment at 45% YoY

**DORA (Digital Operational Resilience Act):**
- Applies to EU financial institutions
- Mandates resilient access controls (Zero Trust is the architecture of choice)
- Explicitly references network segmentation as a technical control
- Financial entities must evidence operational resilience through technical controls

**Compliance-driven buying behavior:** NIS2 and DORA create non-discretionary budget. Organizations must buy microsegmentation, not because they want to, but because they legally must. This changes the sales conversation from "why do you need this?" to "how will you comply?"

---

## 5. Competition in DACH Zero Trust

**Tier 1 competitors (major platform players):**

| Vendor | Zero Trust approach | DACH presence | Estimated global ZT market share |
|---|---|---|---|
| Palo Alto Networks | Prisma Access (SASE + ZTNA). Acquired CyberArk ($25B, 2025) for identity-fused segmentation. | Strong. Major enterprise presence in Germany. | ~18% |
| Zscaler | ZPA/ZIA. Cloud-native SASE pure-play. | Strong in DACH financial services and large enterprise. | ~15% |
| Cisco | Secure Access (ZTNA + Umbrella + Duo). | Dominant installed base in DACH enterprise networking. | ~14% |
| Fortinet | FortiSASE (ZTNA + SD-WAN + FWaaS). | Growing, especially mid-market. | ~10% |

**Tier 2 competitors (specialized/adjacent):**

| Vendor | Relevance | Notes |
|---|---|---|
| Illumio | Direct microsegmentation competitor to Guardicore | Ranked high in IDC microsegmentation market shares 2024 |
| Cloudflare | Edge-native Zero Trust, 310+ PoPs | Growing in DACH mid-market, very aggressive pricing |
| CrowdStrike | Falcon Zero Trust Assessment (endpoint-integrated) | Strong brand, but microsegmentation is not their core |
| Microsoft | Azure AD + Defender, leveraging M365 footprint | Ubiquitous in DACH, but Zero Trust is one of many plays |

**Competitive dynamics for Guardicore specifically:**
- Primary competitor: Illumio (dedicated microsegmentation vendor)
- Structural advantage: Akamai's broader security portfolio (CDN + DDoS + WAF + API Security + Guardicore) enables cross-sell that pure-play cannot match
- Risk: Palo Alto's CyberArk acquisition signals platform convergence: identity + segmentation under one vendor
- DACH opportunity: regulatory pressure (NIS2/DORA) creates a buying trigger that favors vendors with compliance-ready reporting and audit features

---

## 6. DACH channel landscape for Akamai

**Current state (hypothesis, confidence: medium):**
- Akamai's DACH channel historically CDN-centric. Security and cloud channel is newer and growing.
- The Partner Connect restructure is designed to attract security-focused partners (MSSPs, SIs)
- EMEA has localized tiering, meaning DACH partners are measured against DACH benchmarks
- Guardicore and API Security are the priority product lines for channel growth
- The Senior Channel Marketing Manager role for DACH sits at the intersection of: partner enablement, demand generation through partners, MDF execution, and certification program promotion

**DACH-specific challenges:**
- 137,000 unfilled cybersecurity positions across DACH (talent shortage)
- Average enterprise uses 47 security tools (vendor fragmentation/fatigue)
- Many organizations still at early Zero Trust maturity despite regulatory pressure
- Partner channel marketing in DACH requires German-language content, compliance messaging, and regulatory context

**The gap for the HVO:** Akamai has the product (Guardicore recognized by Gartner), the regulatory tailwind (NIS2/DORA creating non-discretionary budget), and a freshly restructured partner program (Partner Connect). What they need is the execution layer in DACH: someone who can run the four marketing motions through partners, build the certification pipeline, execute MDF-funded demand generation, and create the co-marketing programs that convert regulatory urgency into partner-sourced pipeline. That is the role.

---

## 7. Key data points for HVO

For use in the diagnosis and leave-behind memo:

- 70% of new security business through channel (Akamai data)
- €18.7B DACH cybersecurity market, 14.2% growth
- 29,000 organizations affected by NIS2 in Germany
- Microsegmentation market: $21.58B growing to $62.3B (23.62% CAGR)
- Gartner: 25% of Zero Trust enterprises will use microsegmentation by 2027 (up from <5%)
- Germany Zero Trust market: $2.47B to $5.6B by 2030
- Partner Connect launched Q3 2025: first unified global program
- GCSP certification enables partners to deliver full microsegmentation lifecycle
- DACH talent gap: 137,000 unfilled cybersecurity positions
