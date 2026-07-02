# Integration partner candidates, part 2: ConTech, fleet/equipment software, AI platforms

Research date: 2026-07-02. Scope: candidates for Trackunit IrisX integrations owned by Head of Partnerships - Integrations & Applications. Success metric context: IrisX credit consumption grows when partner apps read/write IrisX data via APIs, so each candidate is assessed for data pull/push volume potential.

## Key findings

- Trackunit already claims 1,200+ integrations via IrisX and exposes REST, GraphQL, Time Series and Rental ERP APIs; named connectors are mostly generic SaaS (ERP, BI, CRM), so deep native ConTech and AI integrations are the open frontier (inference on the last clause).
- Trackunit launched an MCP Server at IRE 2026 (April 2026) connecting IrisX fleet data to ChatGPT, Claude, Gemini and Microsoft Copilot, plus IrisX Blueprints (reusable datasets + code + workflow blocks) and a conversational assistant in Trackunit Manager expected summer 2026. AI assistants are now a first-class integration channel, and every agent query is a credit-consumption event (inference on the last clause).
- Procore's Equipment Telematics feature currently lists Caterpillar, John Deere and Samsara as data sources; United Rentals rental-fleet telematics flows into Procore via a separate Resource Management integration announced February 2026. Trackunit is absent, which makes a Procore-IrisX telematics connector the single most obvious whitespace in this category (inference).
- The fleet-software field consolidated hard in 2025-2026: John Deere acquired Tenna (closed Feb 2026), Thoma Bravo agreed to combine HCSS with Nemetschek's Build & Construct segment (ENR: $2.4B), and Trimble agreed to acquire Document Crunch (April 2026). Independent, OEM-neutral integration partners are becoming scarce; Trackunit's neutrality is a selling point but partner M&A is a pipeline risk (inference).
- Hilti is already a strategic Trackunit partner: ON!Track assets appear in Trackunit and vice versa, and the ON!Track Unite open-API marketplace lists Trackunit alongside Fieldwire and Procore. This is the template to replicate with other ConTech platforms (inference on the last clause).
- Palantir Foundry has a proven construction deployment (Thomas Cavanagh Construction runs dispatch, trucking and site ops on Foundry, with 97% daily employee usage), showing demand for ontology-level operational platforms that would consume telematics feeds at high volume.

## Details

### Group A: ConTech / jobsite platforms

| Player | What it is / market presence | Telematics / IrisX relevance | Value of IrisX integration |
|---|---|---|---|
| Procore | Leading construction management platform; Q4 2025 revenue $349M (+16% YoY), FY2026 guidance ~$1.49B, 1.3M+ users, 52% of ARR from customers on 6+ products; moving to consumption-based AI monetization | Equipment Telematics feature with open API; integrates Cat, Deere, Samsara (plus United Rentals rental telematics via a separate Resource Management integration); no Trackunit integration found | High: machine location/hours inside Procore project workflows; large contractor install base pulling IrisX data daily (inference) |
| Autodesk Construction Cloud | 275+ integration partners; part of Autodesk AECO ecosystem (Forma 400+ integrations) | Partner ecosystem open; Propeller covers machine telematics + drone data angle; no Trackunit connector found in sources | Medium-high: equipment data in ACC cost/schedule workflows; brand halo for developer ecosystem (inference) |
| Hilti ON!Track | Tool tracking and asset management; ON!Track Unite open API marketplace | Existing strategic partnership: ON!Track tools visible in Trackunit, Trackunit-connected machines visible in ON!Track; Unite marketplace lists Trackunit, Fieldwire, Procore | Already live; deepen to two-way workflows and joint go-to-market; reference case for other platforms (inference) |
| Fieldwire by Hilti | Jobsite/task management; 2M+ projects worldwide (some sources: 4M+ deployments), ~343 employees; named 2025 Jobsite Management Solution of the Year; drives Hilti software growth above 15% | In ON!Track Unite marketplace; no direct telematics integration found | Medium: equipment status and location in field tasks; low-friction via existing Hilti relationship (inference) |
| PlanRadar | Vienna-based construction/real estate documentation platform; 14,500+ customers, used across 60-75 markets; $69M Series B, total raised $103-127M | No telematics integration found | Medium: strong EMEA/MENA footprint complements Trackunit's European base (inference) |
| Buildots | AI progress tracking (computer vision on helmet cameras); $45M Series D (May 2025), $166M total, 230+ employees; acquired Genda (workforce/safety) | No telematics integration found | Medium: combine visual progress with machine activity data for productivity analytics (inference) |
| OpenSpace | Visual intelligence / 360 reality capture; $102M Series D at $902M valuation (2022); 275k+ users, 94 countries, 43B+ sq ft captured, 1,000+ data center projects; acquired Disperse (progress tracking AI) | No telematics integration found | Medium: site imagery + equipment telemetry for jobsite intelligence, esp. data center construction boom (inference) |

### Group B: Fleet / equipment management software

| Player | What it is / market presence | Telematics / IrisX relevance | Value of IrisX integration |
|---|---|---|---|
| Tenna | Construction asset management platform (heavy iron to tools); acquired by John Deere (announced Dec 22, 2025, closed mid-Feb 2026, operates under Tenna name) | Ingests AEMP/ISO 15143-3 feeds from Cat, Deere, Komatsu, Volvo; integrates ERPs, fuel, Gearflow | Medium: IrisX as mixed-fleet feed into Tenna; Deere ownership complicates neutrality (inference) |
| HCSS | Heavy civil construction software (HeavyBid, HeavyJob, Equipment360, Telematics); 4,000+ companies in US/Canada; Thoma Bravo agreed to combine HCSS with Nemetschek Build & Construct segment (ENR: $2.4B deal) | HCSS Telematics aggregates machine data from a dozen+ OEMs; Equipment360 feeds ERPs like Viewpoint Spectrum; VisionLink API feed integrated | High: IrisX as a single normalized mixed-fleet feed replacing per-OEM plumbing for HCSS customers (inference) |
| Trimble B2W (Maintain) | Heavy civil estimating/ops/maintenance suite inside Trimble | B2W Maintain consumes AEMP-compliant telematics for preventive maintenance triggers; Trimble also owns VisionLink heritage | Medium-high: maintenance triggers from IrisX fault codes/hours; Trimble is simultaneously partner and competitor (inference) |
| Fleetio | Fleet maintenance SaaS with construction/heavy equipment offering; integrates Cat VisionLink and John Deere Operations Center, fuel cards, open API | Telematics integration directory exists; no Trackunit connector found in sources | Medium: engine hours and fault codes from IrisX driving PM schedules for mixed fleets (inference) |
| Gearflow | AI-powered parts procurement (Parts Hub Pro); ~4,000 North American users; ~$10-13.9M raised (Brick & Mortar Ventures led); HCSS partnership | Sits downstream of fault codes and maintenance events | Medium-low volume, high strategic fit: fault code to parts order automation is a clean credit-consuming workflow (inference) |

### Group C: AI platforms and agents

| Player | What it is / market presence | Telematics / IrisX relevance | Value of IrisX integration |
|---|---|---|---|
| OpenAI (ChatGPT), Anthropic (Claude), Google (Gemini), Microsoft Copilot | Hyperscaler/frontier AI assistants | Already connected: Trackunit MCP Server (IRE 2026) lets these agents query assets, update records, set alerts in natural language | Very high: every agent call is API/credit consumption; partnership work shifts to distribution, connector directories and enterprise agent stores (inference) |
| Palantir Foundry / AIP | Ontology-based operational platform; construction proof point: Thomas Cavanagh Construction runs dispatch, trucking, Site 360 on Foundry ("TOM"), 97% daily employee usage; telematics + maintenance + demand signals connected to cut idle time | Foundry ingests IoT/streaming/geospatial data natively | High for large contractors/owners: IrisX as certified telematics source into Foundry ontologies; large recurring data pulls (inference) |
| Trunk Tools | Agentic AI over construction documents; $40M Series B (Jul 2025, Insight Partners), $70M total | Document/schedule focus today; no telematics found | Medium: extend agents from documents to machine data via IrisX MCP (inference) |
| Document Crunch | AI contract/risk intelligence; 400+ customers, $350B+ construction volume; Trimble agreed to acquire (Apr 2, 2026, closing Q2 2026) | None found; risk workflows could consume usage/compliance data | Low-medium; acquisition routes it into Trimble ecosystem (inference) |
| nPlan | Probabilistic schedule risk forecasting trained on thousands of projects | None found | Medium: actual machine activity as ground truth for schedule forecasts (inference) |
| Buildots / OpenSpace (also Group A) | Construction AI computer vision | See Group A | See Group A |

Market context: AI in construction is projected at $6.02B in 2026 growing ~24.8% CAGR to $35.5B by 2034; construction AI VC funding rose 75% YoY in early 2025.

### Prioritization takeaway (inference)

Highest credit-consumption leverage: (1) hyperscaler AI agents via the already-launched MCP Server (distribution partnerships), (2) Procore Equipment Telematics connector (large gap, huge install base), (3) HCSS/Nemetschek as normalized mixed-fleet feed, (4) deepen the Hilti template. M&A watch: Deere-Tenna, Trimble-Document Crunch and Nemetschek-HCSS all pulled potential partners toward competing ecosystems within eight months.

## Sources

- https://trackunit.com/irisx/integrations/
- https://trackunit.com/press/trackunit-introduces-ai-driven-fleet-intelligence/
- https://www.forconstructionpros.com/construction-technology/equipment-monitoring-logistics/product/22966222/trackunit-trackunit-expands-ai-capabilities-for-fleet-data
- https://www.procore.com/whats-new/unlock-efficiency-with-equipment-telematics-integration
- https://www.procore.com/press/procore-announces-fourth-quarter-and-full-year-2025-financial-results
- https://construction.autodesk.com/partners/integrate-with-autodesk-construction-cloud/
- https://unite.ontrack3.hilti.com/marketplace/telematics
- https://www.prnewswire.com/news-releases/hilti-opens-up-its-ontrack-tool-tracking-app-to-help-enable-contractors-to-manage-more-than-jobsite-assets-301567923.html
- https://www.fieldwire.com/blog/2025-jobsite-solution-of-the-year/
- https://www.planradar.com/about-us/
- https://www.prnewswire.com/news-releases/planradar-raises-69m-to-digitize-global-construction-and-real-estate-industry-301464878.html
- https://techcrunch.com/2025/05/29/buildots-raises-45m-to-help-companies-track-construction-progress/
- https://www.constructiondive.com/news/openspace-acquires-disperse-contech-merger/804410/
- https://www.prnewswire.com/news-releases/openspace-surpasses-1-000-data-center-projects-defining-the-construction-intelligence-standard-for-ai-infrastructure-302786566.html
- https://www.tenna.com/integrated-construction-software/oem-telematics-aemp-integrations/
- https://www.heavyequipmentguide.ca/article/35109/tenna-integrates-telematics-from-multiple-manufacturers-into-one-platform
- https://www.hcss.com/products/oem-telematics/
- https://www.hcss.com/press/nemetschek-set-to-acquire-hcss-creates-next-global-construction-technology-leader/
- https://www.enr.com/articles/62828-nemetschek-to-buy-hcss-for-24b-expanding-reach-into-heavy-civil-contractor-software
- https://www.trimble.com/en/products/b2w-software/maintain-equipment-maintenance
- https://www.fleetio.com/industries/construction-equipment-management-software
- https://gearflow.com/ and https://www.enr.com/articles/55134-parts-matching-platform-gearflow-receives-55m-led-by-brick-mortar
- https://www.hcss.com/news/partnership-gearflow/
- https://blog.palantir.com/revolutionizing-construction-e37cba735796
- https://trunktools.com/resources/company-updates/trunk-tools-closes-40m-series-b-construction-ai-transformation/
- https://news.trimble.com/2026-04-02-Trimble-to-Acquire-Document-Crunch-to-Add-AI-Powered-Risk-Management-and-Document-Compliance-to-Trimble-Construction-One-Project-Delivery-Ecosystem
- https://www.constructionplacements.com/best-ai-tools-construction-project-teams/
- https://www.procore.com/press/united-rentals-announces-telematics-integration-with-procore-to-expand

_Verified: adversarially cross-checked against primary sources — Trackunit MCP Server press release (IRE launch, ChatGPT/Claude/Gemini/Copilot, summer conversational assistant, IrisX Blueprints) confirmed on trackunit.com; IrisX integrations page confirms 1,200+ prebuilt connectors and REST/GraphQL/Time Series/Rental ERP APIs; Procore Q4 revenue $349M (+16% YoY per press release, corrected from 15.6%), FY guidance $1,489-1,494M and 1.3M+ users (procore.com/what-is-procore) confirmed; Procore Equipment Telematics page lists only Deere/CAT/Samsara with no Trackunit — United Rentals telematics is a separate Resource Management integration (Businesswire/Procore press), wording corrected; Hilti-Trackunit two-way ON!Track visibility confirmed via Trackunit/Hilti press releases and International Rental News, Unite marketplace listing (Trackunit, Fieldwire, Procore) confirmed via PR Newswire; Deere-Tenna (announced Dec 22, completed Feb 18, independent under Tenna tradename) confirmed via deere.com and ENR; Thoma Bravo/Nemetschek-HCSS $2.4B (ENR headline, ~72/28 structure, 4,000+ companies) confirmed; Trimble-Document Crunch (Apr 2 announcement, Q2 close, 400+ customers, $350B+ volume per Construction Dive/Ironspring) confirmed; Buildots $45M Series D/$166M total (TechCrunch), OpenSpace-Disperse (Construction Dive), Palantir-Cavanagh 97% daily Foundry usage (Palantir blog quote), and Trunk Tools $40M Series B led by Insight Partners/$70M total (company release) all confirmed._
