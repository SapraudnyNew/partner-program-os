# Trackunit: Company Research Digest

Research date: 2026-07-02. Sources are web-public as of this date.

## Key findings

- Trackunit is a Danish construction technology company (SaaS + IoT hardware) headquartered in Aalborg, Denmark, on a mission to "eliminate downtime" in construction. Founded in 2003 per the company's own press release (some databases say 1998; the discrepancy is unresolved).
- Ownership as of mid-2025: Goldman Sachs Alternatives holds a majority stake; Hg reinvested and remains a minority shareholder; GRO Capital exited. The deal was announced 10 Feb 2025 and closed 16 June 2025. Goldman previously owned Trackunit 2015-2021 before selling to Hg, so this is a re-acquisition. Danish media (Boersen, via M&A trackers) reported a valuation of about DKK 10bn.
- Scale: roughly 3.5 million connected assets, 5,000+ customers, and about 400 employees at the Feb 2025 announcement; third-party trackers put headcount at 473 (Apr 2025) to 496 (Mar 2026). The Head of Partnerships job page cites "over 2 million assets connected" and "2 billion daily data points" and "400+ employees" (numbers vary by page and date). Estimated revenue around USD 75M (Apr 2025, third-party estimate), with North America about 50% of revenue.
- Strategy: IrisX, launched August 2024, is positioned as "the operating data platform for construction", an industry cloud platform with a data lakehouse, analytics, Automation Studio, App SDK, marketplace, GraphQL/REST APIs, webhooks, and GenAI/LLM capabilities. The internal "IrisX Acceleration" plan (named in the Head of Partnerships job posting) aims to make IrisX "the platform layer of the global construction industry", with IrisX credit consumption as the primary commercial metric for the partnerships pod.
- Credit-based consumption: the phrase "IrisX credit consumption" appears in Trackunit's own job posting as the primary commercial metric for the partnerships team; however, no public developer-docs or pricing page found in this research describes the credit mechanics publicly (inference: the credit model is commercially significant but not yet publicly documented).
- 2025-2026 momentum: ERA "Rental Technology of the Year" 2025 award, Sunbelt Rentals UK&I expansion to 20,000+ connected assets on an IrisX-built customer portal (Nov 2025), Point of Rental partnership (Jan 2025), IrisX MCP launch connecting fleet data to ChatGPT/Claude/Copilot, Samoter award in Italy, CONEXPO-CON/AGG 2026 showcase with "digital blueprints" and a reality-capture tool, and the virtual event "Trackunit Next 2026" on AI in construction.

## Details

### Ownership timeline

| Period | Majority owner | Notes |
|---|---|---|
| 2015-2021 | Goldman Sachs (with GRO Capital) | First institutional ownership |
| 2021-2025 | Hg | Hg acquired controlling interest from Goldman Sachs and GRO Capital in 2021 |
| Feb-Jun 2025 onward | Goldman Sachs Alternatives (majority) | Hg reinvested as minority; GRO Capital exited; announced 10 Feb 2025, closed 16 Jun 2025; reported valuation ~DKK 10bn (Boersen via mainsights.io) |

### Business and revenue model

- Core model: telematics hardware (IoT units and sensors, including OEM factory-fit and aftermarket) plus recurring SaaS subscriptions to the software platform; described by third parties as SaaS complemented by DaaS. Revenue nearly doubled between 2021 and 2022; ~USD 75M annual revenue estimated as of April 2025 (third-party).
- IrisX adds a platform/ecosystem layer: marketplace apps (built by customers, partners, third-party developers, and Trackunit), APIs (REST, GraphQL, webhooks, Rental API for ERP integration, Data Ingest API), App SDK, and pricing-plan policies in the app manifest (installation.pricingPlanPolicy). The IrisX credit consumption model is referenced in hiring materials as the primary commercial metric but is not publicly documented in developer docs found during this research.
- Customer segments: OEMs, rental companies, contractors, and ecosystem tech partners.

### IrisX and the Acceleration plan

- IrisX launched August 2024 as an "Operating Data Platform" / industry cloud platform (CEO Soeren Brogaard framed it against Gartner's Industry Cloud Platform trend). Components: Data Lakehouse, Analytics and Insights, AI and ML (model training, LLM/GenAI), Automation Studio, Apps and Extensions, Marketplace, OEM integrations, connectors to ERPs, CRMs, rental systems, and BI tools. Named partners on the IrisX page include Twilio, Slack, OpenAI, and SAP.
- The "IrisX Acceleration plan" is Trackunit's internal strategy name (from the Head of Partnerships job posting). The posting describes the partnerships role as "one of the most strategically important hires" in the plan, owning third-party integrations across ERP (SAP, Oracle), fleet management, ConTech, and AI platform layers, leading a pod (Partnerships Product Manager, Platform Engineer, Field Marketing Manager, Regional Partnership Managers), with IrisX credit consumption as the primary success metric, reporting to the VP of Platform.
- Positioning language for 2026: Trackunit as "a data partner rather than a software vendor"; advantage comes from making data understandable and actionable, not from having more data; "working prototypes available in minutes"; ready-to-deploy "digital blueprints" for predictive maintenance, smart servicing, inventory forecasting; IrisX MCP exposes equipment intelligence to ChatGPT, Claude, Copilot and other AI agents.

### Scale, HQ and offices

- HQ: Gasvaerksvej 24, Aalborg, Denmark. US office: Trackunit Inc., 1301 West 22nd Street, Suite 705, Oak Brook, Illinois (Chicago area).
- Amsterdam presence confirmed: Zekeringstraat 17 A, 1014 BM Amsterdam, Netherlands (Glassdoor office listing; also Rotterdam listed).
- Other listed locations: Aarhus, Copenhagen, Kolding, Oslo, Stockholm, Berlin, Goslar, Lyon, London (UK), Kitchener and London (Canada), Yokohama, Singapore, Pymble (Australia).
- Headcount: ~400 (company PR, Feb 2025); 473 across 4 continents (Apr 2025, third-party); 496 (Mar 2026, third-party). Job page says "400+ across offices in Denmark, Norway, Germany, France, Sweden, UK, and Benelux".
- Connected assets: 1.25M "assets and counting" (early 2025 press), ~3.5M connected assets (Feb and Jun 2025 investment PRs), "over 2 million" (careers page). (inference: figures likely count different things, e.g. Trackunit devices vs total assets visible on the platform including third-party feeds.)

### Culture and language

- Purpose: "Together we eliminate downtime"; downtime viewed through five lenses: machines, humans, companies, the industry, society. "Eliminate Downtime 2025" movement launched as an industry initiative.
- Culture described as human-centric ("a people approach in everything we do", "human-centric is not restricted to products, it is a way of life"), collaborative, co-creation and design-thinking driven, remote-friendly. Careers tagline: "Come join us with everything you are."

### Partnership announcements (general pattern)

| Partner | Type | When | Note |
|---|---|---|---|
| Sunbelt Rentals UK&I | Rental customer/partner | Nov 2025 | 20,000+ assets, customer portal built on IrisX, part of Sunbelt 4.0 strategy |
| Point of Rental | Rental management software | Jan 2025 | Long-term partnership for rental efficiency |
| United Rentals | Rental fleet telematics | 2018 (ongoing) | Premium telematics across URI fleet |
| SAP, Twilio, Slack, OpenAI | Platform/tech partners | Listed on IrisX page 2025-2026 | Connectors and AI ecosystem |
| Cisco | Infrastructure case study | n.d. | Cisco customer story |

## Sources

- https://trackunit.com/press/trackunit-launch-operating-data-platform-irisx/
- https://trackunit.com/irisx/
- https://trackunit.com/articles/acceleration-through-irisx/
- https://www.forconstructionpros.com/construction-technology/product/22958802/trackunit-trackunit-brings-latest-irisx-innovations-to-conexpoconagg-2026-portfolio
- https://www.prnewswire.com/news-releases/trackunit-announces-investment-from-goldman-sachs-alternatives-302372680.html
- https://trackunit.com/press/trackunit-announces-closing-of-investment/
- https://www.mainsights.io/ma-news/goldman-sachs-re-acquires-majority-stake-in-trackunit-from-hg-capital-and-gro-capital
- https://www.grocapital.dk/news/goldman-sachs-and-gro-capital-announce-the-sale-of-trackunit-a-global-leader-in-off-highway-telematics-solutions-to-hg
- https://hgcapital.com/insights/trackunit-announces-investment-from-goldman-sachs-alternatives
- https://careers.trackunit.com/jobs/7782454-head-of-partnerships-integrations-applications
- https://careers.trackunit.com/pages/locations-4e921a17-f1c2-4f73-9c2c-eb2a8f690196
- https://www.glassdoor.com/Location/All-Trackunit-Office-Locations-E2162305.htm
- https://trackunit.com/about/purpose/
- https://trackunit.com/eliminate-downtime/
- https://trackunit.com/company/press-releases/eliminate-downtime-launch
- https://trackunit.com/press/point-of-rental-partnership/
- https://trackunit.com/press/sunbelt-trackunit-partnership/
- https://trackunit.com/press/trackunit-and-united-rentals-partnership/
- https://trackunit.com/section/press/
- https://developers.trackunit.com/docs/guides/welcome-to-trackunit-irisx/irisx-overview
- https://developers.trackunit.com/docs/marketplace-config
- https://developers.trackunit.com/docs/api-reference/rental-api/rental-api/
- https://help.trackunit.com/en/articles/676615-connect-trackunit-irisx-mcp
- https://vizologi.com/business-strategy-canvas/trackunit-business-model-canvas/
- https://leadiq.com/c/trackunit/5a1d84c024000024005f7612
- https://tracxn.com/d/companies/trackunit/__EB_Lvej5nCT-Yb2upxTw93RhVSjmUOmJ5hi3FyFn23c
- https://www.cisco.com/site/us/en/about/case-studies-customer-stories/trackunit.html

_Verified: cross-checked against primary sources — PRNewswire investment announcement (Goldman Sachs Alternatives majority, Hg minority reinvestment, GRO exit, prior 2015-2021 Goldman ownership; founded 2003, Aalborg HQ, ~400 employees, 5,000+ customers, ~3.5M connected assets), Trackunit closing press release (deal closed 16 June 2025 after 10 Feb 2025 signing), mainsights.io citing Boersen for the ~DKK 10bn valuation, the live Head of Partnerships job posting (IrisX Acceleration, ERP/fleet/ConTech/AI integration scope, pod composition, VP of Platform reporting line, IrisX credit consumption as primary metric — all quoted verbatim), the IrisX launch press release (29 Aug 2024, "Operating Data Platform"/ICP framing), the Sunbelt Rentals UK&I press release (26 Nov 2025, 20,000+ assets, IrisX customer portal), Dutch business registries and Glassdoor confirming the Amsterdam office at Zekeringstraat 17 A, 1014 BM, and International Rental News confirming the ERA 2025 "Rental Technology of the Year" award for IrisX (Dublin). Searches of developers.trackunit.com and the web found no public documentation of IrisX credit mechanics, confirming the negative claim._
