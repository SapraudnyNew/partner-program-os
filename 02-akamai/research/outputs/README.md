# Research Outputs

Deep research outputs for the Akamai HVO bundle. Two parallel research missions, executed via dedicated chats per `02-akamai/research/prompts/`.

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
└── partner-program/          # Akamai partner program + DACH partner network
    └── akamai-partner-program-dach-dossier.md  (~30pp, 7 sections, 50 named DACH partners)
```

## How to use this material

For diagnosis scorecard (D2-2):
- Start with `company/06-master-summary.md` for synthesis
- Cross-reference `partner-program/akamai-partner-program-dach-dossier.md` File 6 (questions and blind spots) and File 7 (master summary)
- Score Akamai on each of the 7 lifecycle stages (Basic / Professional / World-class) per `01-method/maturity-model/scorecard-template.md`

For ABM/TAS DACH Partner Project (D3-1):
- Primary input: `partner-program/akamai-partner-program-dach-dossier.md` File 2 (DACH partner network, 50 named partners) and File 4 (displacement and recruitment targets)
- Top displacement candidates: KAEMI GmbH (Berlin, Illumio EMEA Partner of the Year), Navixia SA (CH, first EMEA Illumio ZTS Professional)
- Top tier-upgrade candidate: Computacenter (dual partner Akamai+Illumio, Select today)
- Top recruitment candidates: SVA, Cancom, Axians (Mittelstand systemhauser, currently outside Akamai program)
- Anchor partners to deepen: Deutsche Telekom Security, Bechtle AG / Bechtle Schweiz, Controlware, InfoGuard (CH)

For ABSM DACH Sprint (D3-2):
- Primary input: `company/02-dach-regional-intelligence.md` (NIS2/DORA section, Germany Mittelstand context)
- Cross-reference `partner-program/akamai-partner-program-dach-dossier.md` File 4 (Mittelstand systemhauser recommendations) to identify the partner that fronts the showcase account

For HVO main memo (D2-3):
- Section "What I see today" cites from `company/04-channel-marketing-organization.md` and `partner-program/akamai-partner-program-dach-dossier.md` File 2 / File 6
- Section "Where the largest moves are" cites the diagnosis scorecard (D2-2 output)
- Section "What I'd own in 90 days" references the linked DACH project bundles

## Confidence markers

The dossier uses these markers throughout:
- ✅ Confirmed (2+ sources)
- ⚠️ Single-sourced
- 🧠 Inferred (logical extension)
- ❌ Blind spot (no public source, requires inside intelligence)

Treat ❌ items as questions for the hiring manager interview. Do not present them as facts in the HVO.

## Source corpus

Both research missions used Exa search and fetch over 150+ tool calls each. Sources include: Akamai corporate site, Akamai partner blog, Akamai University, PR Newswire releases, Channel Futures, Channel Buzz, ChannelE2E, ARN/IDG, partner websites (50+), Crunchbase, Northdata, Bundesanzeiger filings, LinkedIn company pages, Gartner, IDC, Mordor Intelligence, BCG, KENSAI.

Full source lists are at the end of each file. Master deduplicated source list lives in `partner-program/akamai-partner-program-dach-dossier.md` File 7.

## Provenance

- Company research: executed 2026-05-16, output 6 files
- Partner program research: executed 2026-05-16, output as single multi-section dossier
- Both missions referenced the prompts in `02-akamai/research/prompts/` (v2 versions)

The synthesis layer `02-akamai/akamai-research.md` lives one level up. It predates this deep research and remains useful as an initial scope-setting document; for production work, use the deep research files in this directory.
