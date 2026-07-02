# Marketplace and developer portal benchmark for IrisX

Benchmark of five ISV marketplaces (Procore, Autodesk, Salesforce, Shopify, Samsara) focused on what makes ISV activation low-touch: self-serve sandboxes, listing flows, revenue mechanics, certification, and co-marketing. Compiled July 2026 from vendor documentation and recent secondary sources.

## Key findings

- The common denominator across all five is a free, self-serve developer environment that requires no sales conversation: Procore Developer Sandbox, Salesforce scratch orgs and Partner Business Org, Shopify development stores, Samsara sandbox with simulated vehicles/drivers/events. ISVs can build and validate end-to-end before any human touchpoint.
- Listing flows are checklist-driven and published openly. Procore and Shopify publish full approval checklists and requirements pages on the developer portal, so ISVs self-qualify before submitting; review then becomes a verification step, not a negotiation.
- Revenue mechanics vary widely and are a growth lever, not just a monetization lever: Autodesk currently takes 0% commission and charges nothing to publish; Shopify lets developers keep 100% of the first 1M USD in gross app revenue (one-time exemption since 2025) then 85%; Salesforce takes 15% of net revenue for ISVforce apps and 25% for OEM (partner guides report a drop to 10%/15% above 20M USD cumulative).
- Certification tiers create a quality ladder that ISVs climb voluntarily because placement and badges convert: Shopify's "Built for Shopify" badge (higher search ranking, prioritized review queue, performance criteria like p95 latency under 500 ms and minimum installs/reviews) and Procore's tiered Technology Partner Program (announced June 2025) both tie visibility to measurable customer value.
- The marketplace itself is a lead engine for ISVs, which is the strongest activation incentive: Salesforce creates lead records in the partner's org when a prospect watches a demo, takes a Test Drive, or installs (once lead collection is enabled on the listing); Autodesk gives publishers an analytics dashboard with downloads, revenue, and sales stats. Samsara, the closest analog to Trackunit (fleet IoT), grew to 350+ integrations (Aug 2025) with one-click installs inside the customer dashboard and an explicit openness stance ("we won't block or remove an app just because it competes with our own products").

## Details

### Comparison table

| Platform | Self-serve sandbox | Listing flow | Rev-share / fees | Certification / tiers | Co-marketing / demand gen |
|---|---|---|---|---|---|
| Procore App Marketplace (539 apps per third-party tracker appmarketplace.com, 2025) | Free Developer Sandbox via Developer Portal; collaborator invites; webhooks, OAuth (auth code + client credentials), DMSA service accounts | Published Marketplace Approval Checklist and Listing Guidelines; app must be installable, production-ready, with onboarding docs and support contact; beta customer strongly encouraged; named contacts (marketplaceqa@, techpartners@) | No public listing fee found; program benefits listed as included | Tiered Technology Partner Program announced June 16, 2025 (recognize/reward, global consistency, clear growth path); post-approval quality bar: at least 1 active customer per rolling 12 months | Case studies, testimonials, Procore logo use, events (Jobsite), API support team access |
| Autodesk App Store / Design and Make Marketplace | APS developer platform; Publisher Center self-serve submission via Publisher Corner | Self-serve publisher signup, submit for approval; supports desktop, web apps, and now MCP servers | Free to publish; currently 0% commission (agreement reserves up to ~30% in future); PayPal as payment processor for paid apps | Product guidelines per product line (AutoCAD, Vault, Forma, etc.) | Publisher analytics dashboard: downloads, revenue, sales stats, 14-language localization |
| Salesforce AppExchange | Free to join partner program; Partner Business Org with 2 free licenses; scratch orgs simulate any edition; Developer Edition orgs; Trailhead training | Publish via listing + mandatory Security Review (999 USD per submission for paid apps, 0 for free apps); annual listing fee approx 150 USD | ISVforce: 15% of net revenue; OEM: 25% (official docs confirm the 15% base rate; the reported drop to 10%/15% after 20M USD cumulative appears in partner guides, not official docs); Checkout via Stripe adds 0.30 USD per credit-card transaction | Security Review is the certification gate; contractual models (ISVforce/OEM) define the tier | Test Drive and Trialforce trials directly from listing; lead capture into partner's License Management Org on demo/test drive/install (enabled via listing lead settings); Partner Community |
| Shopify App Store | Free development stores for build and test; 19 USD one-time partner registration for App Store distribution | Draft > Submitted > Reviewed > Published statuses; public App Store requirements checklist; automated + manual review | Developers keep 100% of first 1M USD gross app revenue (one-time exemption from Jan 2025), then 85%; 2.9% processing fee | "Built for Shopify" badge: min 50 net installs on paid shops, min 5 reviews, rating threshold, 1000+ API requests/28 days with p95 < 500 ms, theme app extensions, minimal storefront speed impact; badge gives higher search rank and prioritized review queue | Badge-driven placement in search; app store is primary demand channel for ~thousands of ISVs |
| Samsara App Marketplace (closest IoT analog) | Partner Developer Portal: draft apps, sandbox with simulated vehicles, drivers, events to validate integrations end-to-end; test OAuth2 flows and scopes safely | Technology Partner application, then App Certification Process; published integration guides incl. a dedicated guide for FMC (fleet management company) partners; private deployment option besides public listing | No public rev-share found for marketplace listings (inference: primarily an ecosystem/stickiness play, not a take-rate play) | App Certification; quality standards enforced with removal rights; explicit openness pledge: competitive apps allowed | 350+ integrations as of Aug 2025; access to 10,000+ customers as the headline partner pitch; one-click installs in customer dashboard (Settings > Apps) |

### Patterns worth noting

1. Openness as positioning. Samsara markets "the world's largest and most open marketplace for operations technology" and commits not to block competitive apps. In machine-data ecosystems where OEMs and ISVs fear platform capture, this pledge lowers the trust barrier to building (relevant to construction OEM dynamics; inference).
2. Two app archetypes. Procore formalizes "data connection apps" (backend integration) vs "embedded apps" (full-screen or side panel inside Procore's UI). This lets simple ERP/rental-system connectors ship fast while richer ConTech apps live inside the primary UI. Trackunit's App SDK already targets the embedded pattern inside Trackunit Manager.
3. Anti-extraction guardrails. Procore explicitly prohibits bulk data export beyond core functionality and use of customer data for AI/LLM training. This protects the platform's data moat while keeping APIs open, directly relevant for a credit-metered platform (inference).
4. Certification pays for itself when tied to distribution. Shopify's badge criteria are operational metrics (latency, installs, ratings), not paperwork; partners self-optimize because the reward is search ranking. Salesforce's paid Security Review works because AppExchange demand justifies the 999 USD cost.
5. Leads are the currency of ISV loyalty. Salesforce's lead routing on listing interactions (demo views, Test Drives, installs, trials) is a frequently cited activation benefit in partner guides; Autodesk's usage/revenue dashboard is a lighter version of the same idea.
6. Quality hygiene is continuous, not one-time. Procore requires at least one active customer per rolling 12 months and removes stale or broken listings, keeping the catalog credible.

### Levers applicable to IrisX

1. Free self-serve sandbox with simulated construction data (machines, sites, operating hours, faults), Samsara-style, so an ISV can validate an integration end-to-end before any partnership conversation.
2. Published, self-qualifying approval checklist and listing guidelines on developers.trackunit.com (Procore/Shopify pattern) so review becomes verification, not negotiation.
3. Two-lane app model: lightweight "data connection" lane for ERP/rental/fleet connectors and an embedded App SDK lane for ConTech and AI apps, with different review depth per lane.
4. Zero fee to publish, at least in the growth phase (Autodesk pattern), because the primary metric is credit consumption: every third-party app that reads or writes IrisX data drives credits, so ISV volume is the monetization (inference tied to the credit model).
5. Consumption-aligned incentives: credit rebates or free credit allowances for certified partners during their first year, an analog of Shopify's first-1M exemption translated to a consumption model (inference).
6. Certification badge tied to operational metrics (uptime, API error rates, active installs, customer rating) that buys marketplace search placement and a prioritized review queue (Built for Shopify pattern).
7. Lead capture and partner analytics: route listing views, demo requests, and installs to the ISV as leads, plus a dashboard with installs and credit consumption per app (AppExchange + Autodesk pattern).
8. One-click install inside Trackunit Manager with OAuth scopes and admin approval (Samsara Settings > Apps pattern) to collapse time-to-first-value for customers.
9. Anti-extraction policy published openly (no bulk export beyond app purpose, no training AI models on customer data without consent), Procore-style, to protect OEM and customer trust while keeping APIs open.
10. Tiered technology partner program with clear criteria and escalating co-marketing (logo, case studies, event presence at bauma/CONEXPO, launch posts), following Procore's June 2025 tiering announcement and its "clear benefits and growth path" framing.

_Verified: Cross-checked against primary sources — Shopify dev docs confirm the lifetime (one-time) 0% share on the first 1M USD gross app revenue from Jan 1, 2025, then 15% share, the 19 USD one-time registration fee, and the 2.9% processing fee; Built for Shopify requirements page confirms 50 net installs from active paid shops, 5 reviews, a minimum rating threshold, 1000+ API requests over 28 days with p95 under 500 ms, and the overview confirms higher search ranking plus a BFS-only prioritized review queue. Salesforce developer docs confirm the 15% Checkout revenue share, the 0.30 USD Stripe fee, the 999 USD per-submission Security Review fee for paid apps (0 for free apps), and the approx 150 USD annual listing fee; the 20M-cumulative tier drop is reported only in partner guides and is hedged accordingly; AppExchange lead creation (demo, Test Drive, install, trial) is confirmed but is enabled via listing lead settings, so "automatic" was softened. The Autodesk publisher FAQ (primary PDF) confirms no publishing fee, 0% current commission with the agreement reserving up to 30% in the future, and PayPal as payment vendor. Samsara's blog (Aug 18, 2025) confirms 350+ integrations, and official Samsara docs confirm the sandbox "contains simulated vehicles, drivers, and events," the App Certification Process, and the pledge not to block or remove competitive apps. Procore's marketplace requirements confirm production-ready/installable apps, the bulk-extraction and AI/ML-training prohibitions, and the one-active-customer-per-rolling-12-months rule; the tiered Technology Partner Program blog is dated June 16, 2025 ("launched" adjusted to "announced"). The 539-app Procore count is a third-party tracker figure and is labeled as such._

## Sources

- https://developers.procore.com/documentation/listing-your-app
- https://procore.github.io/documentation/marketplace-requirements
- https://procore.github.io/documentation/partner-overview
- https://developers.procore.com/documentation/marketplace-checklist
- https://developers.procore.com/partner
- https://www.procore.com/blog/building-stronger-together-new-tiered-technology-partner-program
- https://appmarketplace.com/marketplaces/procore-app-marketplace/
- https://aps.autodesk.com/app-store/publisher-center
- https://damassets.autodesk.net/content/dam/autodesk/www/adn/pdf/frequently-asked-questions.pdf
- https://apps.autodesk.com/Content/pdf/Publisher.pdf
- https://aps.autodesk.com/blog/new-app-usage-insights-dashboard-appstore-publishers
- https://developer.salesforce.com/docs/atlas.en-us.packagingGuide.meta/packagingGuide/appexchange_checkout_rev_share.htm
- https://appnigma.ai/blogs/salesforce-appexchange-listing-guide-2026/
- https://appnigma.ai/blogs/salesforce-isv-partner-program-guide-2026/
- https://blog.beyondthecloud.dev/blog/salesforce-org-types-for-appexchange-partners
- https://blog.beyondthecloud.dev/blog/appexchange-lead-management
- https://shopify.dev/docs/apps/launch/distribution/revenue-share
- https://betakit.com/shopify-app-developers-will-no-longer-be-exempt-from-sharing-their-first-1-million-usd-in-revenue-every-year/
- https://shopify.dev/docs/apps/launch/app-store-review/review-process
- https://shopify.dev/docs/apps/launch/built-for-shopify/requirements
- https://www.shopify.com/partners/blog/built-for-shopify-updates
- https://developers.samsara.com/docs/technology-partner-program
- https://developers.samsara.com/docs/partner-developer-portal
- https://developers.samsara.com/docs/sandboxes
- https://www.samsara.com/blog/samsara-partner-ecosystem-350-integrations
- https://www.samsara.com/products/app-marketplace
- https://developers.trackunit.com/docs/overview
- https://trackunit.com/press/trackunit-launch-operating-data-platform-irisx/
