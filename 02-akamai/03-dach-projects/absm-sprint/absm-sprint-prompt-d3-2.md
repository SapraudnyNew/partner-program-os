# D3-2 ABSM Sprint — New Chat Prompt

## Mission

You are executing the D3-2 ABSM Sprint for the Akamai DACH Partner Project. This is a full Account-Based Selling Motion (ABSM) sprint — 6 stages, real company names, production-quality artifacts.

## Parameters (locked, do not change)

| Parameter | Value |
|-----------|-------|
| Partner | Axians/Fernao (Axians Deutschland GmbH, post-Fernao integration) |
| Vertical | German Mittelstand manufacturing — NIS2 essential and important entities |
| Product | Akamai Guardicore Segmentation (Zero Trust microsegmentation) |
| Territory | Germany only |
| Target band | €100M–€2B revenue, 1,000–10,000 employees |
| Hard filter | Below Akamai direct sales coverage threshold (no DAX 40, limited MDAX) |
| Showcase account | Trumpf GmbH (Ditzingen, Baden-Württemberg) — publicly named, full treatment |

## Context on Axians/Fernao (already researched — use this, do not re-research)

- Revenue: €685M (2024 DE) + €260M ex-Fernao = ~€945M combined
- Employees: ~3,225 + ~770 ex-Fernao = ~4,000 post-integration
- Parent: VINCI Energies
- Primary security contact: Alain de Pauw, Division Leader IT Security Services DE + CH
- Known Mittelstand customers: Hochland SE (food manufacturing, Managed SOC), IAV GmbH (automotive engineering, network segmentation), Flughafen München (KRITIS), fischerwerke GmbH (manufacturing, security awareness), anonymous Autoteile-Zulieferer (automotive OT segmentation in progress)
- Fernao integration: rebranding underway since it-sa October 2025, not complete — portfolio window open
- No Illumio, no Akamai currently in stack
- ISG Leader DE 2025 in 4 cyber categories including Next-Gen SOC/MDR and OT Security

## Context on Trumpf GmbH (showcase account)

- HQ: Ditzingen, Baden-Württemberg
- Revenue: ~€5.4B (FY2024)
- Employees: ~20,000 globally
- Sector: Machine tools, laser technology, electronics, additive manufacturing
- NIS2 status: Important entity (manufacturing, digital infrastructure in products)
- IT/OT relevance: High — Trumpf machines run on TCP/IP, factory floor highly networked, connected laser systems = critical OT infrastructure
- Why Guardicore fits: Trumpf needs to segment production network from corporate IT; lateral movement through shop floor = production shutdown risk
- Public information: Annual report available, strong digital manufacturing position, TruConnect (IoT platform) = additional attack surface

## ABSM Sprint — 6-stage methodology

### Stage 0: Context Architect
Output: `00-context.md`
- Partner brief (Axians/Fernao profile summary)
- Market brief (German Mittelstand manufacturing + NIS2 landscape)
- Product brief (Guardicore Segmentation — core use cases for manufacturing OT/IT)
- Sprint scope and constraints

### Stage 1: Target Account Selector
Output: `01-targeting/`
- ICP definition: German Mittelstand manufacturing, €100M–€2B, NIS2-obligated, high IT/OT convergence, not already Akamai direct
- Scoring matrix: 5 criteria weighted (NIS2 obligation, OT/IT convergence, revenue band, Axians/Fernao reachability via existing relationship, public cyber incident history)
- 30-candidate longlist (use Exa to research real German manufacturing Mittelstand companies)
- 10-company scored shortlist (apply matrix)
- Final 3 deep accounts + Trumpf as named showcase (total 4)
- Selection rationale document

Real companies required. Examples to consider (research and score):
Festo SE, Krones AG, Rational AG, Bürkert Fluid Control, Dorma+Kaba, Hella GmbH, Wacker Chemie, Dürr AG, Knorr-Bremse, Schaeffler AG, Voith GmbH, Grenzebach Group, CLAAS KGaA, Sick AG, Weinig Group — plus others you discover via Exa research.

### Stage 2: Deep Intel Profiler
Output: `02-intel/` — 4 files per account (4 accounts × 4 files = 16 files)
Per account:
- `[account]-company-brief.md` — firmographics, tech stack, NIS2 exposure, recent news
- `[account]-pain-map.md` — OT/IT pain points, known incidents, compliance pressure points
- `[account]-relationship-map.md` — who owns IT/OT security decisions, LinkedIn-verified contacts
- `[account]-axians-connection.md` — does Axians/Fernao already have a relationship? Any public evidence?

### Stage 3: Strategy Master
Output: `03-strategy/`
- Sweet Spot definition: the exact overlap of Axians/Fernao's existing customer relationship + Trumpf/accounts' NIS2 OT-segmentation need + Guardicore's differentiation vs Illumio (confirmed vs inferred)
- Pain pattern library: 3 recurring pain patterns across all 4 accounts (e.g., "flat OT network post-digital-transformation", "NIS2 Article 21 gap: network segmentation not documented", "insurance requiring segmentation proof")
- Content matrix: for each pain pattern, what content/case study/proof point does Axians use in the conversation
- Competitive angle: why Guardicore over Illumio specifically for Mittelstand manufacturing (simpler deployment, agentless option, OT-native policy templates)

### Stage 4: Execution Arsenal
Output: `04-execution/` — 3 items per account (4 accounts × 3 items = 12 files)
Per account:
- `[account]-email-sequence.md` — 3-email sequence (German language), personalized to account pain, referencing specific Axians relationship or known public trigger
- `[account]-business-case.md` — one-page ROI/risk framing for CISO/CTO: cost of OT downtime, NIS2 fine exposure, Guardicore deployment timeline
- `[account]-map.md` — Mutual Action Plan: 5-step path from first conversation to POC approval

### Stage 5: Infrastructure and Launch
Output: `05-infrastructure/`
- Measurement system: KPIs for this sprint (meetings booked, POCs initiated, pipeline created)
- CRM integration spec: how Axians logs these accounts, tracks interactions, reports to Akamai
- MDF request spec: what Axians requests from Akamai MDF to fund the outreach (event, workshop, co-branded content)
- Launch checklist: what Axians needs from Akamai before first outreach (Guardicore demo access, case study approval, deal registration confirmed)

### Showcase: Trumpf GmbH — full treatment
Output: `showcase/trumpf-full-profile.md`
This is the public-facing, named account that makes the hiring manager say "they've done their homework." Full treatment:
- All Stage 2 Intel files (company brief, pain map, relationship map, Axians connection)
- Stage 3 strategy applied to Trumpf specifically
- Stage 4 execution: personalized 3-email sequence, business case, MAP
- Why Trumpf + Axians + Guardicore = the right combination

## Output folder structure

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
│   └── [... same for accounts 2, 3, and trumpf]
├── 03-strategy/
│   ├── 01-sweet-spot.md
│   ├── 02-pain-pattern-library.md
│   ├── 03-content-matrix.md
│   └── 04-competitive-angle-guardicore-vs-illumio.md
├── 04-execution/
│   ├── [account1]-email-sequence.md
│   ├── [account1]-business-case.md
│   ├── [account1]-map.md
│   └── [... same for accounts 2, 3, and trumpf]
├── 05-infrastructure/
│   ├── 01-measurement-kpis.md
│   ├── 02-crm-integration-spec.md
│   ├── 03-mdf-request-spec.md
│   └── 04-launch-checklist.md
└── showcase/
    └── trumpf-full-profile.md
```

## Execution rules

1. Use Exa web search aggressively — real company names, real contacts, real public data
2. German language for all email sequences and customer-facing materials
3. English for all internal strategy documents
4. Confidence markers throughout: ✅ confirmed · ⚠️ single-sourced · 🧠 inferred · ❌ blind spot
5. Every contact name must be verified via LinkedIn or corporate website — no invented names
6. Every pain point must be anchored to a public source (NIS2 legislation, Axians case study, company press release, industry report)
7. Start with Stage 0 + Stage 1 (targeting). Present the shortlist of 10 and final 3+1 selection before proceeding to Stage 2. This is the checkpoint — confirm before going deep.

## First task

Start now. Execute Stage 0 (context brief) and Stage 1 (30-candidate longlist + scoring + shortlist). Use Exa to research German Mittelstand manufacturing companies. Present the final 3 + Trumpf selection with rationale before proceeding to Stage 2 intel.

When done with all stages, output all files in sequence for copy/commit to repo.
