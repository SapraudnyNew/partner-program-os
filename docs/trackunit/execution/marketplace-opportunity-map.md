# Marketplace Opportunity Map

This map answers one question: given what Trackunit has already built, which marketplace mechanics from best-in-class ecosystems would convert that foundation into the steepest possible IrisX credit-consumption curve? It reads the platform against a benchmark of five ISV marketplaces (Procore, Autodesk, Salesforce, Shopify, Samsara) and proposes seven moves. All consumption effects are directional and labeled as assumptions.

## What is already strong

Trackunit enters this game with assets most industrial platforms lack.

**Connector breadth.** The IrisX integrations page claims more than 1,200 prebuilt connectors and integrations, a catalog depth that took horizontal SaaS players years to reach.

**A premium API surface built for partners.** GraphQL for tailored data-lake access, a Time Series API on Prometheus standards with PromQL so partners reuse tooling they already know, a purpose-built Rental ERP API for two-way contract sync, and webhooks. This is a differentiated surface, not a generic REST wrapper.

**A working app pipeline.** The Iris App SDK ships apps into Trackunit Manager with a CLI submission flow straight to the marketplace, where Trackunit-built ERP connectors (RentalMan, Baseplan, B2W, Integrated Rental) already sit alongside partner apps.

**Brand and reach.** Works With Trackunit claims 7,000+ trusted construction partners across OEMs, System Integrators, Integrations and Digital Experience Partners: a distribution asset that new entrants cannot buy.

**An AI head start.** The Trackunit MCP Server connects IrisX to ChatGPT, Claude, Gemini and Microsoft Copilot on standard OAuth 2.1. Most industrial platforms have nothing comparable live; Trackunit shipped it at IRE.

**Reusable building blocks.** IrisX Blueprints package datasets, code patterns and workflows for distribution through the marketplace, which is exactly the compounding mechanism a partner program needs.

## The benchmark: what best-in-class marketplaces do

Six mechanics recur across the five benchmarked ecosystems.

1. **Free self-serve sandbox before any sales conversation.** Procore's Developer Sandbox, Salesforce scratch orgs, Shopify development stores, and Samsara's sandbox with simulated vehicles, drivers and events all let an ISV build and validate end-to-end before a human touchpoint.
2. **Published approval checklists so ISVs self-qualify.** Procore and Shopify publish full requirements on the developer portal; review becomes verification, not negotiation.
3. **Revenue mechanics as a growth lever.** Autodesk charges 0 percent commission and nothing to publish; Shopify lets developers keep 100 percent of their first 1M USD in gross app revenue. Generous early economics buy ISV volume.
4. **Certification ladders that convert visibility into quality.** The Built for Shopify badge ties operational metrics (p95 latency under 500 ms, minimum installs and reviews) to higher search ranking and a prioritized review queue; Procore announced tiered technology partnership in June 2025 with the same logic.
5. **The marketplace as a lead engine for ISVs.** Salesforce creates lead records in the partner's org when a prospect watches a demo, takes a Test Drive or installs; Autodesk gives publishers an analytics dashboard with downloads and revenue. Leads are the strongest activation incentive an ISV can receive.
6. **The closest fleet-IoT analog validates the path.** Samsara reached 350+ integrations by August 2025 with one-click installs inside the customer dashboard and an explicit openness stance, including a pledge not to block competing apps.

## Seven leverage moves for IrisX

1. **Public self-serve sandbox with simulated fleet data.** Extend the developer hub with a free environment containing simulated machines, sites, operating hours and fault codes, so an ISV validates a connector end-to-end before any partnership conversation. Borrows: Samsara's simulated-entity sandbox. Consumption effect: widens the top of the funnel that every other move feeds; more ISVs building means more apps consuming (assumption: sandbox-originated ISVs convert to live listings at meaningfully higher rates, to be measured). Effort: L.
2. **Published listing checklist and guidelines.** Put the full marketplace approval checklist on developers.trackunit.com so ISVs self-qualify and submissions arrive review-ready. Borrows: Procore's Marketplace Approval Checklist and Shopify's requirements pages. Consumption effect: shortens scoped-to-live cycle time, pulling each connector's first credits forward by weeks (assumption). Effort: S.
3. **A "Built on IrisX" certification badge tied to placement.** Define operational criteria (uptime, API error rates, active installs, customer rating) and reward certified apps with marketplace search placement and a prioritized review queue. Borrows: Built for Shopify and Procore's June 2025 tiers. Consumption effect: partners self-optimize toward reliability and active usage, and active usage is credits (assumption). Effort: M.
4. **Lead-gen instrumentation on listings.** Route listing views, demo requests and installs to the ISV as leads, and give every publisher a dashboard showing installs and credit consumption per app. Borrows: Salesforce lead records and Autodesk's publisher analytics. Consumption effect: leads make the marketplace the ISV's favorite channel, so their best engineering flows here first, and each new app version deepens data usage (assumption). Effort: M.
5. **Connector templates for the top three RMS patterns.** Package the recurring rental integration shapes (two-way contract sync, usage-based billing meters, service triggers) as IrisX Blueprints so the next ten RMS connectors start at 80 percent done (assumption on the fraction). Borrows: Trackunit's own Blueprints mechanism, applied to the partner catalog. Consumption effect: multiplies connector count per engineering quarter, and every live connector is a recurring credit stream. Effort: M.
6. **An AI-agent listing category around the MCP Server.** Create a dedicated marketplace category for agent integrations and MCP-ready apps, and publish a certification path for agent developers. Borrows: Autodesk's App Store, which now accepts MCP servers, with Trackunit already ahead of most industrial platforms on the protocol itself. Consumption effect: every agent query is a metered event, so distribution of the MCP channel converts directly into credits (assumption on volume). Effort: S.
7. **Published partner economics.** State the commercial terms openly: publishing is free, and certified partners receive a first-year credit allowance (assumption, an analog of Shopify's first-1M exemption translated to a consumption model). Borrows: Autodesk's 0 percent commission and Shopify's first-1M exemption. Consumption effect: removes the pricing unknown that stalls ISV business cases, and the allowance seeds usage habits that convert to paid consumption in year two (assumption). Effort: S for publication, M with the allowance mechanics.

## Sequencing

Three moves come first. Move 2 (published checklist) ships in weeks and immediately compresses time-to-first-credit for every integration already in flight, including the first five. Move 6 (AI-agent category) rides momentum the MCP Server launch already created; it is the cheapest way to open a second consumption channel while the market attention is fresh. Move 1 (self-serve sandbox) starts now despite being the largest, because it gates the scale phase: once the checklist and the agent category raise inbound ISV interest, the sandbox is what lets the pod serve that interest without linear headcount. Together the three cover the full funnel: more builders in (sandbox), faster to live (checklist), and a second metered channel (agents), each terminating in the same place, IrisX credits consumed. Moves 3, 4, 5 and 7 then convert that funnel into a compounding catalog through certification, leads, templates and published economics.

*First pass from public sources. Presented to demonstrate methodology, to be validated with internal data.*
