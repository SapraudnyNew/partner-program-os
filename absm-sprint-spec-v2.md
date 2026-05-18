# D3-2 ABSM Sprint — Master Specification v2.0

> **Version:** 2.0 — Post-discussion, all decisions locked
> **Date:** 2026-05-18
> **Status:** Ready for execution

---

## Mission

Execute the D3-2 ABSM Sprint for the Akamai DACH Partner Project. Full Account-Based Selling Motion (ABSM) sprint — 6 stages, real company names, production-quality artifacts.

**Primary audience:** Portfolio showcase for job application. Secondary: usable as a real deliverable if opportunity arises.

---

## Parameters (locked)

| Parameter | Value |
|-----------|-------|
| Partner | Axians (formerly Fernao) — first mention uses full form, thereafter "Axians" |
| Vertical | German Mittelstand manufacturing — NIS2 essential and important entities |
| Product | Akamai Guardicore Segmentation (Zero Trust microsegmentation) |
| Territory | Germany only |
| Target band | €100M–€2B revenue, 1,000–10,000 employees |
| Hard filter | Below Akamai direct sales coverage threshold (no DAX 40, limited MDAX) |
| Showcase account | Trumpf GmbH (Ditzingen, Baden-Württemberg) — publicly named, full treatment |
| Language | **All English** — including emails, showcase, all customer-facing materials |
| Design identity | **Axians-branded** — colors, style, tone derived from brand research |

---

## Naming Convention

- **First mention in any document:** "Axians (formerly Fernao)"
- **All subsequent mentions:** "Axians"
- **Exception:** When referencing a historical Fernao case study or pre-rebrand event, use "Fernao (now Axians)" for accuracy

---

## Context: Axians (formerly Fernao)

- Revenue: €685M (2024 DE) + €260M ex-Fernao = ~€945M combined
- Employees: ~3,225 + ~770 ex-Fernao = ~4,000 post-integration
- Parent: VINCI Energies
- Primary security contact: Alain de Pauw, Division Leader IT Security Services DE + CH
- Known Mittelstand customers: Hochland SE (food manufacturing, Managed SOC), IAV GmbH (automotive engineering, network segmentation), Flughafen München (KRITIS), fischerwerke GmbH (manufacturing, security awareness), anonymous Autoteile-Zulieferer (automotive OT segmentation in progress)
- Fernao integration: rebranding underway since it-sa October 2025, not complete — portfolio window open
- No Illumio, no Akamai currently in stack
- ISG Leader DE 2025 in 4 cyber categories including Next-Gen SOC/MDR and OT Security

## Context: Trumpf GmbH (showcase account)

- HQ: Ditzingen, Baden-Württemberg
- Revenue: ~€5.4B (FY2024)
- Employees: ~20,000 globally
- Sector: Machine tools, laser technology, electronics, additive manufacturing
- NIS2 status: Important entity (manufacturing, digital infrastructure in products)
- IT/OT relevance: High — Trumpf machines run on TCP/IP, factory floor highly networked, connected laser systems = critical OT infrastructure
- Why Guardicore fits: Trumpf needs to segment production network from corporate IT; lateral movement through shop floor = production shutdown risk
- Public information: Annual report available, strong digital manufacturing position, TruConnect (IoT platform) = additional attack surface

---

## Intent-Enabled Partner Selling Integration

This sprint operates under a **hypothesis overlay**: target accounts are selected as if both Akamai 1st-party signals and 6sense 3rd-party intent data indicated buying activity. This models the **Partner Intelligence Program (PIP)** concept — a two-layer Channel ABM initiative:

**Layer 1 — Partner Intent Routing:** Akamai shares curated high-intent DACH account lists with Axians based on territory and specialization. Signals aggregated at account level (company + buying stage + topic cluster), GDPR-safe.

**Layer 2 — Account-Based Enablement (ABE):** For each flagged account, pre-built sales kits containing account research, personalized outreach templates, case studies, and talking-point cards.

**In this sprint:** The scoring matrix in Stage 1 does NOT include intent signals as a weighted criterion (since we cannot verify actual intent). Instead, the intent concept is **explained at the top of the targeting section** as the operational context, and account selection is based on firmographic and public data criteria only. Intent is marked as **🧠 hypothesis** throughout.

---

## Stage 0: Context Architect

**Output:** `00-context.md`

**Contents:**
1. Partner brief (Axians profile summary)
2. Market brief (German Mittelstand manufacturing + NIS2 landscape)
3. Product brief (Guardicore Segmentation — core use cases for manufacturing OT/IT)
4. **Guardicore content library** — Guardicore-specific only: datasheets, case studies, OT whitepapers, manufacturing references. Collected via web research. These become the personalization fuel for Stages 3–4.
5. **Axians brand guidelines** — Researched from actual public assets (website, PDFs, social media, event materials). Codified as: primary/secondary colors (hex), typography, tone of voice, logo usage observations, visual style notes. Used in all Stage 4 PDF design.
6. Sprint scope and constraints

---

## Stage 1: Target Account Selector

**Output:** `01-targeting/`

**Intent context (top of section):**
- Explain the PIP hypothesis: in production, these accounts would be surfaced by 6sense intent signals + Akamai 1st-party data
- Mark as 🧠 hypothesis — scoring proceeds on firmographic criteria only

**ICP definition:** German Mittelstand manufacturing, €100M–€2B, NIS2-obligated, high IT/OT convergence, not already Akamai direct

**Scoring matrix:** 5 criteria weighted:
1. NIS2 obligation strength
2. OT/IT convergence level
3. Revenue band fit
4. Axians reachability (existing relationship evidence)
5. Public cyber incident history / security posture signals

**Deliverables:**
- `01-icp-definition.md`
- `02-scoring-matrix.md`
- `03-longlist-30.md` — 30 real German manufacturers, researched via Exa
- `04-shortlist-10-scored.md` — top 10 scored
- `05-final-selection-rationale.md` — final 3 + Trumpf with rationale

**⏸️ CHECKPOINT 1:** Present shortlist for approval before proceeding.

---

## Stage 2: Deep Intel Profiler

**Output:** `02-intel/` — 4 files × 4 accounts = 16 files

Per account:
- `[account]-company-brief.md` — firmographics, tech stack, NIS2 exposure, recent news
- `[account]-pain-map.md` — OT/IT pain points, known incidents, compliance pressure
- `[account]-relationship-map.md` — IT/OT security decision makers, LinkedIn-verified contacts
- `[account]-axians-connection.md` — existing Axians relationship evidence

---

## Stage 3: Strategy Master

**Output:** `03-strategy/`

- `01-sweet-spot.md` — three-way overlap: Axians relationship + NIS2 OT-segmentation need + Guardicore differentiation
- `02-pain-pattern-library.md` — 3 recurring pain patterns across all 4 accounts
- `03-content-matrix.md` — per pain pattern: content/case study/proof point for Axians to use
- `04-competitive-angle-guardicore-vs-illumio.md` — why Guardicore for Mittelstand manufacturing

---

## Stage 4: Execution Arsenal

**Output:** `04-execution/` — 3 items × 4 accounts = 12 files

**Format:** PDF — Axians-branded design (colors, typography, visual identity from Stage 0 brand research)

Per account:
- `[account]-email-sequence.pdf` — 3-email sequence, **English language**, personalized to account pain, Axians brand voice
- `[account]-business-case.pdf` — one-page ROI/risk frame for CISO/CTO
- `[account]-map.pdf` — Mutual Action Plan: 5-step path to POC approval

**Design standard:** Top-notch. These are the portfolio hero pieces.

**⏸️ CHECKPOINT 2:** Present execution materials for approval before proceeding.

---

## Stage 5: Infrastructure and Launch

**Output:** `05-infrastructure/`

- `01-measurement-kpis.html` — **Interactive HTML dashboard** showing KPI framework
- `02-crm-integration-spec.md` — Based on **actual CRM Axians uses** (research via job postings, website HTML scripts, OSINT)
- `03-mdf-request-spec.md` — MDF request from Akamai
- `04-launch-checklist.md` — prerequisites before first outreach

---

## Showcase: Trumpf GmbH — Full Treatment

**Output:** `showcase/trumpf-full-profile.md`

**Language:** English only

Complete consolidation:
- All Stage 2 intel files
- Stage 3 strategy applied to Trumpf
- Stage 4 execution: email sequence, business case, MAP
- Narrative: why Trumpf + Axians + Guardicore = the right combination

---

## Output Folder Structure

```
02-akamai/03-dach-projects/absm-sprint/
├── 00-context.md
├── 01-targeting/
│   ├── 01-icp-definition.md
│   ├── 02-scoring-matrix.md
│   ├── 03-longlist-30.md
│   ├── 04-shortlist-10-scored.md
│   └── 05-final-selection-rationale.md
├── 02-intel/
│   ├── [account1]-company-brief.md
│   ├── [account1]-pain-map.md
│   ├── [account1]-relationship-map.md
│   ├── [account1]-axians-connection.md
│   └── [... ×4 accounts including trumpf]
├── 03-strategy/
│   ├── 01-sweet-spot.md
│   ├── 02-pain-pattern-library.md
│   ├── 03-content-matrix.md
│   └── 04-competitive-angle-guardicore-vs-illumio.md
├── 04-execution/
│   ├── [account1]-email-sequence.pdf
│   ├── [account1]-business-case.pdf
│   ├── [account1]-map.pdf
│   └── [... ×4 accounts including trumpf]
├── 05-infrastructure/
│   ├── 01-measurement-kpis.html
│   ├── 02-crm-integration-spec.md
│   ├── 03-mdf-request-spec.md
│   └── 04-launch-checklist.md
└── showcase/
    └── trumpf-full-profile.md
```

---

## Execution Rules

1. Use Exa/web search aggressively — real company names, real contacts, real public data
2. **All content in English** — emails, business cases, MAPs, showcase, everything
3. Confidence markers throughout: ✅ confirmed · ⚠️ single-sourced · 🧠 inferred · ❌ blind spot
4. Every contact name must be verified via LinkedIn or corporate website — no invented names
5. Every pain point must be anchored to a public source
6. Stage 4 PDFs use Axians brand identity (researched in Stage 0)
7. Intent-enabled partner selling concept explained as hypothesis overlay, not baked into scoring
8. Two checkpoints: after Stage 1, after Stage 4

---

## Confidence Marker Legend

| Marker | Meaning | Usage |
|--------|---------|-------|
| ✅ | Confirmed | Multiple independent public sources |
| ⚠️ | Single-sourced | One public source only |
| 🧠 | Inferred | Logical deduction from available data, not directly confirmed |
| ❌ | Blind spot | No data found, flagged for manual research |
