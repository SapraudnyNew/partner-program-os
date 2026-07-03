# Palantir Technologies (Foundry commercial / industrials scope)

Web enrichment digest, researched 2026-07-03. Scope: Foundry/AIP commercial and industrials, construction deployments, partner motions, EMEA.

## Snapshot

- Public company, NASDAQ: PLTR, HQ Denver, Colorado. 4,429 full-time employees as of Dec 31, 2025, 28% outside the US (FY2025 10-K).
- Q1 2026 revenue $1.6B, up 85% YoY. US commercial revenue $595M, up 133% YoY. FY2026 guidance raised to $7.65B (about 71% growth); US commercial guidance above $3.2B (120%+ growth). Trailing 12-month US commercial TCV bookings $4.7B, up 115%.
- Go-to-market is historically direct, built around forward deployed engineers (FDEs) and deployment strategists plus short "bootcamp" engagements (5 days or less, reported conversion around 75%; 2,800+ bootcamps targeted in 2025). Inference: any partnership with Palantir competes for FDE attention, not marketing budget.

## Why now signals

- Construction is now a named Palantir vertical: a "Palantir for Construction" offering page is live on palantir.com.
- Thomas Cavanagh Construction (Ottawa, heavy civil, reported ~$120M contractor) extended its Foundry partnership to an 11-year term through Dec 31, 2035 (announced late May 2026; PLTR stock rose ~17% on the news). Build started January 2025 after a bootcamp on fleet and job costing.
- Cavanagh created a subsidiary, Cavtera, to commercialize its Foundry-built construction solutions and support Palantir implementations across construction in North America "and beyond." This is a client-to-channel transformation: a customer becoming a Palantir seller for the vertical.
- McCarthy Building Companies (major US GC) signed a multi-year, multi-million dollar partnership with Palantir; its AI-native system "Pulse" (field insight, scenario planning, risk analysis) was demoed at AIPCon 10 in June 2026.
- Partner ecosystem is formalizing: Accenture Palantir Business Group (Accenture named preferred global partner, 2025), Databricks product partnership (AIP + Data Intelligence Platform), Google Cloud Marketplace availability with two-way BigQuery-Foundry integrations and Gemini-AIP connectivity (June 2026), and an ISG Provider Lens "Palantir Ecosystem Partners" report due July 2026, which signals a real implementation-partner market forming around Foundry.
- EMEA: heavy defense/government momentum (UK strategic partnership Sept 2025, GBP 240M MoD contract); commercial software in use by private companies in 13 EU countries as of Aug 2025 (Stellantis renewed and expanded for five more years in March 2026, UniCredit, Fedrigoni).

## Hiring signals

From the live Lever board (jobs.lever.co/palantir, 275 postings, July 2026):

- No dedicated partnerships/alliances/channel roles are posted. Inference: partner motions are run by the deployment and business development orgs, and vertical channel plays (Cavtera-style) are struck opportunistically rather than through a partner program team.
- Heavy FDE and Deployment Strategist hiring, including EMEA locations relevant to Trackunit's footprint: Deployment Strategist in Copenhagen, Oslo, Amsterdam, London, Vilnius; Forward Deployed Software Engineer in Stockholm, Amsterdam, London.
- Deployment Strategist "Warp Speed" (NY) confirms continued push into industrials/manufacturing (Warp Speed links ERP, real-time logistics, AI scheduling; six new manufacturing customers announced March 2025).
- Forward Deployed AI Engineer roles (NY, London) point to AIP/agentic delivery capacity.

## Integration-relevant facts

- Cavanagh deployment specifics: Foundry acts as the company operating system ("Total Operations Management"). Apps built: Dispatch, Trucking, Site 360, Cavanagh Connect. 97% of employees use Foundry daily. Ontology unifies HR data, truck scale systems, GPS feeds, dispatch workflows and planning. Core ontology domains: Contracts, Labor, Equipment, Materials. ERP is being reduced to a financial ledger. COO quote: "In just one year, we have replaced multiple software platforms," rebuilding workflows in Foundry rather than via "complex API integrations."
- Relevance to Trackunit (inference): Cavanagh-style ontologies need machine/fleet data (GPS feeds, equipment domain are already in scope). A telematics/data platform like IrisX is a natural upstream feed into Foundry ontologies for any contractor going this route; conversely, Palantir's pattern of replacing point software is a displacement risk for app-layer vendors.
- Developer/ecosystem surface: Ontology SDK (OSDK), Developer Console with Marketplace integration for packaging/deploying OSDK apps across stacks, AIP Agents publishable as Functions, AIP community registry on GitHub. DevCon2 (Feb 2026, Palo Alto) introduced Embedded Ontologies for offline edge devices, explicitly citing mining and construction sites with unreliable networks.
- Partner programs that exist today: Palantir FedStart (US federal accreditation hosting for ISVs, FedRAMP High / IL5; participants include Unstructured.io 2025, Oligo Security June 2026), Foundry for Builders (startups), bootcamps as the standard land motion, and hyperscaler marketplace listings (Google Cloud June 2026). Inference: the ISV-hosting pattern (FedStart) and the customer-as-reseller pattern (Cavtera) are the two most realistic templates for a Trackunit-Palantir motion, since a classic reseller/SI program for commercial does not visibly exist.
- No public evidence found of any existing Palantir-Trackunit relationship or of Palantir consuming construction OEM telematics feeds beyond customer-side integrations like Cavanagh's GPS/truck-scale data.

## Sources

- https://blog.palantir.com/revolutionizing-construction-e37cba735796 (Cavanagh case: TOM, Dispatch/Trucking/Site 360, 97% daily usage, FDEs, timeline)
- https://www.newswire.ca/news-releases/thomas-cavanagh-construction-limited-extends-strategic-partnership-with-palantir-technologies-through-december-31-2035-863207801.html
- https://www.palantirbullets.com/p/11-year-construction-deal-palantir (Cavtera, client-to-seller)
- https://finance.yahoo.com/markets/stocks/articles/why-palantir-technologies-pltr-17-080722290.html
- https://www.stocktitan.net/news/PLTR/mc-carthy-and-palantir-announce-strategic-partnership-to-bring-ai-to-5bgdl1wg9b7k.html and https://www.constructiondive.com/news/mccarthy-palantir-artificial-intelligence-ai-partnership/822517/
- https://investors.palantir.com/news-details/2026/Palantir-Reports-Q1-2026-U-S--Revenue-Growth-of-104-YY-and-Revenue-Growth-of-85-YY-Raises-FY-2026-Revenue-Guidance-to-71-YY-Growth-and-U-S--Comm-Revenue-Guidance-to-120-YY-Crushing-Consensus-Expectations/
- https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000011/pltr-20251231.htm (FY2025 10-K, headcount)
- https://jobs.lever.co/palantir via api.lever.co (275 postings, retrieved 2026-07-03)
- https://newsroom.accenture.com/news/2025/accenture-and-palantir-expand-global-strategic-partnership-to-drive-ai-reinvention
- https://www.databricks.com/company/newsroom/press-releases/palantir-and-databricks-announce-strategic-product-partnership
- https://www.businesswire.com/news/home/20260604907574/en/ (Google Cloud Marketplace, BigQuery/Gemini integrations)
- https://www.businesswire.com/news/home/20260220605851/en/ISG-to-Assess-Palantir-Ecosystem-Partners
- https://blog.palantir.com/introducing-palantir-fedstart-cd5995d0dfaa and https://www.businesswire.com/news/home/20260618553571/en/ (FedStart, Oligo)
- https://www.businesswire.com/news/home/20250313062266/en/ (Warp Speed manufacturing customers)
- https://dorians.medium.com/palantir-devcon2-recap-eae9797ee102 and https://www.palantir.com/developers/ (OSDK, Embedded Ontologies, Marketplace)
- https://www.businesswire.com/news/home/20260330921521/en/ (Stellantis renewal)
- https://www.businesswire.com/news/home/20260604590081/en/ (AIPCon 10)
- https://www.palantir.com/offerings/construction/
