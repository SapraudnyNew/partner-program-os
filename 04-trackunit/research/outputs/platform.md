# Trackunit IrisX Platform and Developer Surface (research digest, July 2026)

## Key findings

- IrisX is Trackunit's "Construction Industry Specific Cloud Platform" built on top of the existing Iris APIs. Its stated backbone is a Data Lake that normalizes telematics data for use in Apps, Analytics, AI and Automation. IrisX Analytics is "a customer-facing analytics platform powered by Databricks."
- Scale claims (IRE 2026 press release): 6 million connected assets (the same release elsewhere says Trackunit "connects more than 6.5 million assets across the off-highway sector"), more than 2 trillion data points processed, over 3 billion new data points ingested daily. Databricks case study adds "5x faster time-to-market" for IrisX customers versus building in-house.
- Developer surface at developers.trackunit.com covers: Iris APIs (REST plus GraphQL, webhooks), IrisX-only premium APIs (GraphQL API, Time Series API with PromQL, Rental ERP API, webhooks), an Iris App SDK with marketplace publishing, a Design System, and ISO feed (AEMP 2.0 / ISO 15143-3) integrations for mixed OEM fleets.
- Integration count claims vary by source: the launch-era coverage says "more than 100 standardized integrations to external IT systems"; the current trackunit.com/irisx/integrations page claims "more than 1,200 prebuilt connectors and integrations" (the larger number appears to include generic low-code connectors to tools like Slack, Power BI, HubSpot, AWS; inference).
- AI direction is concrete and recent: Trackunit launched a Trackunit MCP Server (Model Context Protocol) at IRE 2026 connecting IrisX to ChatGPT, Claude, Gemini and Microsoft Copilot (endpoint https://mcp.trackunit.ai/mcp, OAuth 2.1 with dynamic client registration). A conversational AI assistant inside Trackunit Manager is expected "later this summer" 2026. IrisX Analytics exposes SQL and Databricks Genie spaces through the MCP.
- The marketplace lists Trackunit-built ERP connectors (RentalMan, Baseplan, B2W, Integrated Rental, a generic ERP connector) plus partner apps; IrisX "Blueprints" (reusable datasets plus code patterns plus workflows) were announced for CONEXPO-CON/AGG 2026 and distributed via the marketplace.
- "Works With Trackunit" is the partner program (OEMs, System Integrators, Integrations, Digital Experience Partners; "7,000+ trusted construction partners" claimed; example: Irdeto/Imperto, April 2025). Public pages do not describe formal tiers.
- The job posting for Head of Partnerships confirms "IrisX credit consumption" as the primary commercial metric, but no public documentation of the credit/consumption pricing mechanics was found on trackunit.com or the developer hub.

## Details

### API surface

| API | Protocol | Purpose | Availability |
|---|---|---|---|
| Iris APIs (Asset, Sites, Groups, Users, Custom Fields, Alerts, Service Mgmt, Access Mgmt/Operators, Emissions Reporting, Location) | REST, OAuth 2.0 | Core CRUD and fleet operations | Iris customers (API access via Trackunit Manager, Administration tab) |
| ISO Export (AEMP 2.0 / ISO 15143-3) | REST (XML/JSON) | Standardized snapshot and time-series fleet data; metadata extension via addMetadata=true | Iris customers |
| GraphQL API | GraphQL | "Tailored data access into the IrisX data lake," efficient client-defined queries; GraphQL Explorer and Visualizer on the dev hub | "Only available to customers on IrisX" |
| Time Series API | REST following Prometheus standards, PromQL query language, instant and range queries | Machine insights and advanced sensor metrics over time ranges with aggregation | "Only available to customers on IrisX" |
| Rental (ERP) API | REST, two-way sync | "Facilitates two-way integrations between IrisX and various Rental Management Systems"; core objects: contracts, contract items linking assets to customers | "Only available to customers on IrisX" |
| Webhooks | HTTP callbacks, event catalog in Manager | Real-time asset events to customer endpoints | "Only available to IrisX customers" |
| Trackunit MCP Server | Model Context Protocol, OAuth 2.1 dynamic client registration, mcp.trackunit.ai/mcp | AI agents query assets/sites/customers/operators/alerts/services/telematics, run SQL against IrisX Analytics and Genie spaces, update records, configure alerts | Active IrisX subscription; ChatGPT live, Claude via custom connector (native "coming soon"), Copilot "coming soon" |

### App SDK and marketplace

- Apps are containers bundling "extensions" deployed into Trackunit Manager; the manifest handles marketplace appearance (logo, screenshots, descriptions) and an installation.pricingPlanPolicy attribute controls install behavior by pricing plan.
- Dev flow uses nx tooling; submission is `nx run [app]:submitApp` with version bump in package.json, acceptance of developer terms, and browser-based identity authentication. Apps can run privately ("in your private browser for internal use") or be deployed to the marketplace to reach "hundreds ... or thousands of other users."
- Marketplace positioning: "the gateway for new services to the industry provided by customers themselves, partners and 3rd party software developers - as well as Trackunit." Confirmed listings include Trackunit-built ERP connectors: RentalMan, Baseplan, B2W, Integrated Rental, generic ERP connector.
- IrisX Blueprints (announced for CONEXPO 2026): Smart Servicing, Out-of-Contract Usage detection, Custom Reporting, Site Optimization, Data-Driven Product Design; distributed via the marketplace.
- App tokens: Manager issues scoped tokens per the app manifest; on-behalf-of-user OAuth flow (client ID/secret) for async API calls.

### Works With Trackunit

- Partner types on trackunit.com/become-a-partner: OEMs, System Integrators (ERP, BI, CRM), Integrations (APIs and apps), Digital Experience Partners (custom-branded insights in Trackunit Manager). Benefits: "Works With" branding, co-marketing, global reach. Claim: "7,000+ trusted construction partners." No public tier structure found.
- Example: Irdeto (digital platform security) integrated its Imperto equipment pooling solution with IrisX and Trackunit Access Management (press release, Aalborg, April 7, 2025).

### AI direction

- IrisX overview: users can apply "ML, LLMs and GenAI, to analyze data, identify patterns, and generate predictive insights" with "strict data privacy."
- MCP Server (IRE 2026): "lets users query assets, update records, and configure alerts through natural language, with no custom integrations required"; framed as "embedding AI into the platform rather than as a separate layer." Databricks direction includes Genie and "upcoming agentic capabilities (Agent Bricks)."
- Conversational AI assistant in Trackunit Manager expected summer 2026.

### Strengths and friction points for a new ISV (facts, neutral)

Strong: dedicated developer hub with GraphQL Explorer/Visualizer, App SDK with CLI submission path, standardized ERP surface (Rental API), Prometheus/PromQL compatibility reusing existing tooling, MCP server with standard OAuth 2.1, Databricks-powered analytics, ISO 15143-3 standard support.

Friction (facts): premium APIs (GraphQL, Time Series, Rental, Webhooks) require an IrisX customer subscription; API keys and webhooks are configured inside a Trackunit Manager account, and no public self-serve sandbox signup was found on the developer hub; several developer-hub doc URLs return 404 and the docs GitHub repo (Trackunit/developer-hub) was archived October 16, 2025 (docs likely migrated; inference); the marketplace web app does not render without JavaScript/login, limiting public discoverability of listings; no public documentation of the credit/consumption pricing model was found. The job posting itself lists improving "sandbox environments, API documentation, and self-serve onboarding for ISVs" as a responsibility, consistent with these gaps.

## Sources

- https://developers.trackunit.com/
- https://developers.trackunit.com/docs/guides/welcome-to-trackunit-irisx/irisx-overview
- https://developers.trackunit.com/reference/rental-erp-api-intro
- https://developers.trackunit.com/reference/time-series-introduction
- https://developers.trackunit.com/reference/export-iso-15143-3-aemp-20-api-intro
- https://developers.trackunit.com/docs/webhooks-overview
- https://developers.trackunit.com/docs/iris-app-publish
- https://developers.trackunit.com/docs/marketplace-config
- https://developers.trackunit.com/docs/app-tokens
- https://help.trackunit.com/en/articles/149690-iris-apis-101
- https://help.trackunit.com/en/articles/676615-connect-trackunit-irisx-mcp
- https://trackunit.com/irisx/integrations/
- https://trackunit.com/become-a-partner/
- https://trackunit.com/press/irdeto-enters-works-with-trackunit-partnership-to-scale-up-equipment-pooling-solution/
- https://trackunit.com/press/trackunit-launch-operating-data-platform-irisx/
- https://trackunit.com/press/trackunit-introduces-ai-driven-fleet-intelligence/
- https://www.internationalrentalnews.com/news/embargo-do-not-use-trackunit-updates-data-platform-with-generative-ai/8038821.article
- https://www.databricks.com/customers/trackunit
- https://new.manager.trackunit.com/marketplace/@trackunit/erp-connector-rental-man (and sibling listings: erp-connector-baseplan, erp-connector-b2w, erp-connector-integrated-rental, erp-connector-generic)
- https://github.com/Trackunit/developer-hub
- https://careers.trackunit.com/jobs/7782454-head-of-partnerships-integrations-applications

_Verified: All eight load-bearing claims cross-checked against primary sources. Confirmed directly: MCP OAuth 2.1 / dynamic client registration / mcp.trackunit.ai/mcp endpoint and per-client support status (help.trackunit.com); IRE 2026 Maastricht press release scale figures and summer conversational-assistant timeline (with the 6M vs 6.5M asset-count discrepancy inside the release noted above); Time Series API Prometheus/PromQL wording and "only available to customers on IrisX" for Time Series, GraphQL, and Rental APIs (live developer-hub pages after following redirects); the "more than 1,200 prebuilt connectors" quote on trackunit.com/irisx/integrations and the launch-era ">100 standardized integrations" figure; Databricks case-study quotes (customer-facing IrisX, Genie, Agent Bricks, 5x time-to-market); become-a-partner page (7,000+ partners, four partner types, no tier structure) and Irdeto/Imperto press release dateline (Aalborg, April 7, 2025); the nx submitApp flow with version bump and browser ID authentication; RentalMan/Baseplan/B2W/Integrated Rental marketplace listings (via indexed listing pages — the SPA itself does not render without JS); and the Trackunit/developer-hub repo archive banner (Oct 16, 2025) plus live 404s on old /reference/ doc URLs. No claims were refuted._
