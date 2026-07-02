# Partner Mapping: The IrisX Integration Ecosystem

The role owns one number: IrisX credit consumption. Credits are consumed when partner applications read and write IrisX data. So the mapping question is not "who could we partner with" but "which integrations, once live, pull data every day at scale." To answer it, I mapped the integration ecosystem across six categories: ERP, rental management systems, fleet and equipment management software, ConTech and jobsite platforms, AI platforms and agents, and OEM data ecosystems. I scored every candidate on six dimensions, assigned each one of four dispositions, and selected five for full dossiers.

## The six scoring dimensions

The scoring model is an adapted Integration Partner Profile. Each dimension is scored from public evidence, with inferences marked as such.

**Strategic Fit.** Does the partner's product sit in a workflow where live machine data changes decisions: rental contracts, billing, dispatch, maintenance, project schedules? A BI dashboard that shows telematics is nice. A rental ERP that bills off engine hours is structural.

**Market Reach.** Install base, geography, and segment. Point of Rental serves 5,000+ business locations in 80 countries. Procore reports 1.3M+ users. Reach converts one connector build into thousands of consuming tenants.

**Technical Readiness.** Does the partner already speak the right protocols: open APIs, webhook support, and ISO 15143-3 (AEMP 2.0), the standard payload for position, hours, fuel and machine status that Cat, Volvo CE, John Deere and Trackunit itself all expose? A partner already consuming AEMP feeds can swap in a normalized IrisX feed with low engineering cost.

**Commercial Model Fit.** Can the partner's pricing carry a consumption-based data layer underneath it? Partners with marketplace economics, per-seat SaaS with usage add-ons, or their own move to consumption pricing (Procore is shifting to consumption-based AI monetization) align naturally with IrisX credits.

**Consumption Potential.** The expected IrisX credit volume, which is the primary metric. Scored on data pull frequency, breadth (assets covered), and depth (time series versus snapshots). All volume estimates in this work are labeled assumptions: Trackunit does not publish credit pricing mechanics, so relative ranking is what the public record supports.

**Recruitability.** Existing commitments and M&A gravity. The fleet software field consolidated hard in 2025 and 2026: John Deere acquired Tenna, Trimble agreed to acquire Document Crunch, and Thoma Bravo agreed to combine HCSS with Nemetschek's Build and Construct segment. Candidates are being pulled into competing ecosystems, so an otherwise strong candidate may already be spoken for, and independence itself is becoming scarce.

## Disposition taxonomy

- **Pursue.** No integration exists, the scoring case is strong, open recruitment now.
- **Deepen.** An integration or partnership already exists; the work is expansion and instrumentation. This covers Point of Rental, Hilti ON!Track, Wynne Systems, MCS, inspHire, Texada and Baseplan, among others.
- **Monitor.** Real potential blocked by timing, M&A movement, or unproven fit; revisit on a trigger.
- **Deprioritize.** Low consumption ceiling or structural conflict; no active effort.

## What the landscape shows

**The ERP and rental base is already broad, but shallow in instrumentation.** The IrisX integrations page claims 1,200+ prebuilt connectors, and names NetSuite, Microsoft Dynamics 365, Acumatica, Baseplan, inspHire and MCS. Point of Rental has a formal two-way partnership, Wynne publishes a Trackunit integration, and Texada lists Trackunit as a partner. The base exists. What the public record does not show is consumption instrumentation on top of it, which is where a Deepen program earns its keep.

**Procore is the clearest whitespace.** Procore's Equipment Telematics feature lists Caterpillar, John Deere and Samsara as sources, and United Rentals rental telematics arrives through a separate Resource Management integration announced February 2026. Trackunit is absent from the largest construction management platform. That is the single most visible gap in the map.

**A migration wave is coming off SAP ETM.** Usage rights ended in 2025 in the S/4HANA context and maintenance ends 2027, per BearingPoint guidance cited by Wynne's RentalResult. Every migration to ETM.next, RentalResult or STAEDEAN needs a telematics layer. Time-bound demand, already scheduled by SAP.

**AI agents are now a consumption channel, not a demo.** Trackunit launched an MCP Server at IRE 2026 connecting IrisX to ChatGPT, Claude, Gemini and Microsoft Copilot. Every agent query against fleet data is an API event, and by inference every agent query is a credit event. Partnership work here shifts from connector building to distribution.

## Where to go next

The full scored matrix with filters by category, disposition and dimension is at [landscape.html](landscape.html). The five priority dossiers, each with a first-30-days plan and a named risk, are at [first-five.html](first-five.html).

*First pass from public sources. Presented to demonstrate methodology, to be validated with internal data.*
