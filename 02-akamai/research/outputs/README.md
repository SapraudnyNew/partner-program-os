# Research Outputs

Deep research outputs for the Akamai HVO bundle. Three research missions, executed via dedicated chats per `02-akamai/research/prompts/`.

## Structure

```
outputs/
├── company/                  # Akamai as a company (research-prompt-akamai-company-v2.md)
│   ├── 01-corporate-fundamentals.md          (~10pp: finances, strategy, leadership, M&A)
│   ├── 02-dach-regional-intelligence.md      (~8pp: DACH footprint, customers, NIS2/DORA, regulatory)
│   ├── 03-cultural-and-operational-intelligence.md  (~5pp: culture, ops norms, hiring signals)
│   ├── 04-channel-marketing-organization.md  (~5pp: channel marketing org, leaders, programs, MDF)
│   ├── 05-risks-and-questions.md             (~4pp: blind spots, interview questions, risks)
│   └── 06-master-summary.md                  (~7pp: synthesis + cross-file index + recommendations)
├── partner-program/          # Akamai partner program + DACH partner network (research-prompt-akamai-partner-program-v2.md)
│   └── akamai-partner-program-dach-dossier.md  (~30pp, 7 sections, 50 named DACH partners)
└── entanglement/             # D2-RC Recruitability + dispositions (research-prompt-akamai-entanglement-v1.md)
    ├── 01-entanglement-matrix.md             (33-partner matrix: L1/L2/L3/L4 signals, Recruitability, disposition)
    ├── 02-deep-profiles.md                   (12 partner deep dossiers)
    ├── 03-recruitability-scoring-framework.md (6-sub-criterion rubric, ADR-011 operationalisation)
    └── 04-recommended-dispositions.md        (Pursue/Contain/Monitor/Drop plus 90-day execution plan)
```

## How to use this material

For diagnosis scorecard (D2-2):
- Start with `company/06-master-summary.md` for company synthesis
- Cross-reference `partner-program/akamai-partner-program-dach-dossier.md` File 6 (questions and blind spots) and File 7 (master summary)
- For Gap 2 dispositions: `entanglement/04-recommended-dispositions.md` Section 1 (disposition summary)
- Score Akamai on each of the 7 lifecycle stages (Basic / Professional / World-class) per `01-method/maturity-model/scorecard-template.md`

For ABM/TAS DACH Partner Project (D3-1):
- Primary input: `partner-program/akamai-partner-program-dach-dossier.md` File 2 (DACH partner network, 50 named partners) and File 4 (displacement and recruitment targets)
- Disposition input: `entanglement/01-entanglement-matrix.md` (33-partner matrix with Recruitability scores) and `entanglement/04-recommended-dispositions.md` (full Pursue/Contain/Monitor/Drop list with 90-day plan)
- Scoring rubric: `entanglement/03-recruitability-scoring-framework.md` (6 sub-criteria, weights, aggregation logic, recalibration cadence)
- **Pursue priority five (next 90 days):** Axians/Fernao (DE), SVA (DE), ACP (AT), AVANTEC (CH), InfoGuard (CH)
- **Pursue disciplined:** Nomios DE, Deutsche Telekom Security (Guardicore-only), suresecure, Kudelski Security
- **Pursue distributor lift:** Infinigate, Arrow ECS Switzerland
- **Contain (work residual product gaps):** Computacenter, Bechtle, Cancom, K-Businesscom, Controlware, NTT Data DE, Indevis, Navixia, NTS AG, Deutsche Telekom Security (SASE/ZTNA)
- **Drop:** KAEMI, Open Systems, genua, Exclusive Networks DE, Westcon-Comstor

For ABSM DACH Sprint (D3-2):
- Primary input: `company/02-dach-regional-intelligence.md` (NIS2/DORA section, Germany Mittelstand context)
- Cross-reference `partner-program/akamai-partner-program-dach-dossier.md` File 4 (Mittelstand systemhauser recommendations) plus `entanglement/04-recommended-dispositions.md` (priority Pursue list) to identify the partner that fronts the showcase account
- Axians/Fernao + SVA are the highest-recruitability Mittelstand fronts

For HVO main memo (D2-3):
- Section "What I see today" cites from `company/04-channel-marketing-organization.md` and `partner-program/akamai-partner-program-dach-dossier.md` File 2 / File 6
- Section "Where the largest moves are" cites the diagnosis scorecard (D2-2 output) and dispositions from `entanglement/04-recommended-dispositions.md`
- Section "What I'd own in 90 days" references the linked DACH project bundles at `02-akamai/03-dach-projects/`

## Confidence markers

The dossier uses these markers throughout:
- ✅ Confirmed (2+ sources)
- ⚠️ Single-sourced
- 🧠 Inferred (logical extension)
- ❌ Blind spot (no public source, requires inside intelligence)

Treat ❌ items as questions for the hiring manager interview. Do not present them as facts in the HVO.

## Source corpus

All three research missions used Exa search and fetch at scale (150+ tool calls per mission). Sources include: Akamai corporate site, Akamai partner blog, Akamai University, PR Newswire releases, Channel Futures, Channel Buzz, ChannelE2E, ARN/IDG, partner websites (50+), Crunchbase, Northdata, Bundesanzeiger filings, LinkedIn company pages, Gartner, IDC, Mordor Intelligence, BCG, KENSAI, Illumio blog, PANW partner pages, Zscaler partner news, Cisco partner award lists.

Full source lists at the end of each file. Master deduplicated source lists in `partner-program/akamai-partner-program-dach-dossier.md` File 7 (company + program research) and inside each entanglement file (D2-RC).

## Provenance

- Company research: executed 2026-05-16, output 6 files
- Partner program research: executed 2026-05-16, output as single multi-section dossier
- Entanglement research (D2-RC): executed 2026-05-18, output 4 files. ADR-011 amendment 2026-05-18 retracts the "Computacenter as Illumio investor" claim based on entanglement file 1 section 5 (Illumio funding records).

All three missions referenced the prompts in `02-akamai/research/prompts/`.

The synthesis layer `02-akamai/akamai-research.md` lives one level up. It predates this deep research and remains useful as an initial scope-setting document; for production work, use the deep research files in this directory.
