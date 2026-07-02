# First Five Integrations: Execution Plan

This plan takes the five priority partners from [../partner-mapping/first-five.html](../partner-mapping/first-five.html) through the four lifecycle stages the pod runs: Scope, Build, Launch, Adopt. Each block below states the play, the scoping summary against the IrisX API surface, a commercial sketch, the path to first credit, the adoption motion, and one risk with its mitigation. Every number is a labeled assumption from public sources, stated to show how I set targets, not what Trackunit's targets should be. The pod KPI language matches the operating plan: scoped-to-live under 90 days median, time-to-first-credit under 30 days from go-live, both reference assumptions.

## 1. Procore

**Play.** Fill the most visible ConTech whitespace: Procore's Equipment Telematics feature lists Caterpillar, John Deere and Samsara as data sources, and Trackunit is absent, so we ship the connector that puts 6M+ connected assets inside Procore project workflows.

**Scoping summary.** Use cases: machine location, hours and status in Procore schedules, cost tracking and jobsite views. Data flows: IrisX GraphQL API for asset and site queries, Time Series API for hours and utilization, webhooks pushing status events into Procore's Equipment Telematics open API. Certification: Procore's published Marketplace Approval Checklist, built and validated in the free Procore Developer Sandbox, with one beta customer before submission per Procore's guidelines.

**Commercial model.** Co-sell sourced pipeline, no rev-share: the connector is free, the money is consumption. Assumption: 50 joint contractor accounts in year one, each pulling data for 100 assets daily, is the reference consumption case.

**Path to first credit.** Scope spec and Procore sandbox build in weeks 1 to 6 (assumption), beta with one joint contractor by week 10 (assumption), marketplace listing submission by end of Q1, first production credits within 30 days of listing (target, assumption). Time-to-first-credit: inside Q2.

**Adoption motion.** Target accounts: contractors that run Procore and hold Trackunit-connected fleets, pulled from account overlap in the GTM interlock. Procore-aligned Trackunit enterprise sellers carry it; Field Marketing anchors the moment on the marketplace listing going live, with CONEXPO as the stage if timing aligns.

**Risk and mitigation.** Procore may prefer its incumbent OEM sources. Mitigation: position IrisX as the mixed-fleet normalizer, one feed covering the OEM long tail via ISO 15143-3 rather than a fourth single-brand source.

## 2. SAP ETM sunset play

**Play.** Ride the forced migration wave: SAP ETM usage rights ended in 2025 in the S/4HANA context and maintenance ends 2027, so every successor stack (BearingPoint ETM.next, Wynne RentalResult, STAEDEAN) needs a telematics layer, and IrisX becomes the default feed inside their migration templates.

**Scoping summary.** Use cases: internal plant hire contracts, utilization billing and service scheduling for contractors leaving ETM. Data flows: Rental ERP API for two-way contract and contract-item sync, GraphQL for asset master data, webhooks for on-rent and off-rent events. Certification: none external; the deliverable is a reference connector per successor, reviewed through our own marketplace listing flow.

**Commercial model.** Co-sell sourced pipeline with the three successor ISVs, plus an optional rev-share on the connector where an ISV resells it (assumption: 10 to 15 percent of connector fees as the reference band). Consumption assumption: each migrated contractor syncs 500+ assets into rental workflows daily.

**Path to first credit.** Q1: partnership agreements and a scoped reference spec with one successor (RentalResult first, since Wynne already publishes a Trackunit integration). Q2: connector build and one pilot migration account. Q3: first production credits from a completed migration (assumption: migrations run 6 to 9 months, so we attach early). Time-to-first-credit: within 30 days of the pilot going live (target, assumption).

**Adoption motion.** Target accounts: contractors publicly running ETM today, the BAM Infra archetype, sourced through the successor ISVs' migration pipelines. The ISVs sell the migration; Trackunit sells the data layer. Marketing moment: a joint migration playbook launched at bauma.

**Risk and mitigation.** Migration timelines slip past 2027. Mitigation: embed IrisX in the ISV template so every migration carries us regardless of date, rather than chasing individual accounts.

## 3. Point of Rental

**Play.** Deepen a partnership that already works: the two-way API with POR Expert and Elite has run since January 2025, so we migrate it onto the IrisX Rental ERP API and credits, and extend it across POR's full product line and 5,000+ business locations in 80 countries.

**Scoping summary.** Use cases: on-rent and off-rent status, delivery tracking and billing data already covered; extension targets utilization-based billing and service triggers. Data flows: Rental ERP API two-way sync as the backbone, webhooks for rental status events, Time Series API for usage-based billing meters. Certification: our own listing review, a candidate for the first "Built on IrisX" certified connector.

**Commercial model.** Credit-resale: POR bundles IrisX credits into its telematics offering per location (assumption: bundle priced per active tracked asset per month, POR margin 20 percent as reference). This converts an integration into a distribution channel.

**Path to first credit.** Q1: re-scope the live integration onto IrisX APIs with POR's product team. Q2: migrate existing joint customers, first credits from migrated accounts within 30 days of cutover (target, assumption). Q3: extend to the remaining POR product line. Fastest time-to-first-credit of the five because customers already exist.

**Adoption motion.** Target accounts: existing joint Expert and Elite customers first, then POR's install base without telematics. POR's own sales team sells it inside the bundle; Trackunit supports enablement. Marketing moment: joint launch at IRE, where Trackunit already stages platform news.

**Risk and mitigation.** POR also offers its Hapn telematics bundle. Mitigation: differentiate on off-highway data depth (fault codes, PromQL time series) that generic trackers do not carry, and formalize this in the certified connector.

## 4. Microsoft Dynamics 365 + Copilot

**Play.** Run two lanes into one ecosystem: deepen the D365 connector already named on the IrisX integrations page through rental ISVs (STAEDEAN, Sycor, HSO), and open the AI channel by completing Copilot support on the Trackunit MCP Server.

**Scoping summary.** Use cases: rental order sync, telematics-triggered maintenance and invoicing inside D365 F&SCM, plus natural-language fleet queries in Copilot. Data flows: Rental ERP API and GraphQL for the ERP lane, webhooks for workflow triggers, MCP Server (OAuth 2.1) for the agent lane. Certification: AppSource listing requirements for the ISV lane; Copilot connector validation for the agent lane.

**Commercial model.** Co-sell sourced pipeline through the Microsoft partner ecosystem; no rev-share. Consumption comes twice: steady ERP sync volume plus per-query agent consumption (assumption: agent queries add 10 to 20 percent incremental credits on mature accounts).

**Path to first credit.** Q1: scope with one ISV (Sycor, which already markets telematics-to-ERP automation) and confirm the Copilot timeline. Q2: ISV connector pilot live, first ERP-lane credits. Q3: Copilot lane live once MCP support lands, AppSource listing. Time-to-first-credit: Q2 via the ERP lane (assumption).

**Adoption motion.** Target accounts: mid-market rental firms on D365 F&SCM in North America and DACH, sourced from ISV customer lists. The ISVs sell it inside their rental solutions; Microsoft field co-sell follows the AppSource listing. Marketing moment: the Copilot go-live, staged with the MCP Server story from IRE.

**Risk and mitigation.** Copilot MCP support is "coming soon" and the date is Microsoft's. Mitigation: sequence the ERP lane first so credits flow regardless, and treat the agent lane as upside.

## 5. Palantir Foundry

**Play.** Make IrisX the certified telematics source for ontology-level operations platforms, starting from Foundry's proven construction deployment at Thomas Cavanagh Construction, where dispatch, trucking and site operations run on Foundry with 97 percent daily employee usage.

**Scoping summary.** Use cases: live machine data inside Foundry ontologies for dispatch, idle-time reduction and demand planning at large contractors and owners. Data flows: Time Series API with PromQL for high-frequency metrics, GraphQL for asset and site objects, webhooks for event streams; Foundry ingests streaming and geospatial data natively, so the connector is a data-source template, not an app. Certification: a documented Foundry data-connection template published on both sides.

**Commercial model.** Pure consumption, no rev-share: this is the highest per-account volume of the five (assumption: one Foundry deployment pulls more daily credits than 20 standard connector accounts, given full-fleet high-frequency reads).

**Path to first credit.** Q1: design-partner agreement with one large contractor or owner running both platforms. Q2: data-connection template built and validated on the design partner's fleet, first credits at pilot cutover. Q3: published template and second account. Time-to-first-credit: end of Q2 (assumption); the cycle is long but the volume compounds.

**Adoption motion.** Target accounts: a lighthouse motion, not a volume motion; Trackunit enterprise sellers and Palantir field teams jointly pursue a shortlist of large mixed-fleet owners. Marketing moment: a joint reference case published when the design partner hits measurable idle-time reduction.

**Risk and mitigation.** Few accounts, long enterprise cycles. Mitigation: cap pod investment at one design partner until first credits confirm the volume assumption.

## Combined quarter view

| Partner | Q1 | Q2 | Q3 |
|---|---|---|---|
| Procore | Sandbox build, beta customer, listing submitted | Listing live, first credits, 10 joint accounts (assumption) | 25+ accounts, CONEXPO push (assumption) |
| SAP ETM sunset | RentalResult agreement, reference spec | Connector built, pilot migration starts | First migration credits, bauma playbook |
| Point of Rental | Re-scope onto Rental ERP API | Joint customers migrated, first credits | Full product line, IRE joint launch |
| D365 + Copilot | Sycor scope, Copilot timeline fixed | ISV pilot live, first ERP-lane credits | Copilot lane live, AppSource listing |
| Palantir Foundry | Design-partner agreement | Template validated, first pilot credits | Template published, second account |

## How the five compound

None of these builds stays a one-off. The Procore connector becomes the reusable ConTech telematics-push pattern for Autodesk Construction Cloud and Fieldwire. The Point of Rental migration and the ETM successor work harden the Rental ERP API into connector templates that cover the next ten RMS vendors at a fraction of the cost, packaged as IrisX Blueprints and listed on the marketplace. The D365 work produces both a generic ERP lane and the first agent-channel playbook, which every future Copilot, ChatGPT or Claude distribution deal reuses. Foundry yields a high-volume data-connection template for any ontology or analytics platform. By Q3 the pod operates a catalog where each new partner starts from a proven pattern, which is what turns integration work into a consumption flywheel.

*First pass from public sources. Presented to demonstrate methodology, to be validated with internal data.*
