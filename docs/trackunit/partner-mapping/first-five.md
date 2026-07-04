# The First Five

Out of the full landscape, five candidates get a dossier. They were not picked for size alone. Each one anchors a repeatable play: a whitespace connector on a major platform, a migration-wave capture, a Deepen template for the existing partner base, a two-channels-in-one-deal enterprise motion, and one bold bet on where high-volume data consumption is heading. Together they span ConTech, ERP, rental management and AI platforms, so the first year of the role produces evidence across the whole map, not one category. Every consumption estimate below is reasoning from public facts, labeled as such, and each dossier ends with the risk that would kill it.

### **1. Procore: the whitespace play**

**Why now.** Procore's Equipment Telematics feature lists Caterpillar, John Deere and Samsara as data sources. United Rentals rental-fleet data flows in through a separate Resource Management integration announced February 2026. Trackunit is not there. Meanwhile Procore reported Q4 2025 revenue of $349M, up 16% year over year, guides toward roughly $1.49B for FY2026, counts 1.3M+ users, and is moving to consumption-based AI monetization. The platform where site teams already work has an open telematics socket and the mixed-fleet source is missing.

**The integration.** A Procore-IrisX connector feeding machine location, hours and status into Procore's Equipment Telematics API, so a contractor sees its entire mixed fleet, not just Cat and Deere machines, inside project workflows. Trackunit claims 100+ OEM integrations, which is exactly the normalization Procore's per-OEM source list lacks.

**Consumption logic (assumption).** Contractor project teams check equipment daily, so the pull pattern is frequent snapshots plus location streams across whole fleets. If even a fraction of Procore's contractor base activates the connector, this is a many-tenant, daily-pull consumption profile: the single connector with the largest reach-to-effort ratio on the map. Volume figures require internal data, this is a shape argument, not a number.

**First 30 days.** Confirm Procore's telematics partner requirements, build a demo against the public Equipment Telematics API using IrisX GraphQL and ISO 15143-3 exports, and identify the Procore partnerships owner via existing mutual customers, starting with contractors who run both.

**Main risk.** Procore treats telematics sources as commodity feeds and offers listing without co-marketing. Mitigation: lead with mixed-fleet coverage breadth, which Cat and Deere structurally cannot offer.

[Account plan: Procore →](accounts/procore.html)

### **2. The SAP ETM sunset: a migration-wave play**

**Why now.** SAP ETM, the module contractors used for internal plant and equipment rental, is being sunset: usage rights ended in 2025 in the S/4HANA context, and maintenance ends 2027 in the ERP context, per BearingPoint guidance cited by Wynne's RentalResult. Every ETM customer, including large contractors like BAM Infra which ran ETM with add-ons, must re-platform on a schedule SAP set. The named successors, BearingPoint ETM.next, Wynne RentalResult and STAEDEAN, all need a telematics layer, and none of them makes hardware.

**The integration.** Not one connector but a standard: position IrisX as the governed telematics data layer specified into every ETM migration. Concretely, a reference architecture per successor product, using the IrisX Rental ERP API for two-way contract and asset sync and the AEMP 2.0 export for fleet status. Wynne already publishes a Trackunit integration, so one of three successors starts warm.

**Consumption logic (assumption).** Migrating contractors move whole internal rental fleets at once, and equipment cost allocation runs on meter data, so pulls are recurring and fleet-wide. A migration play front-loads consumption: each closed migration adds a full fleet on day one rather than growing seat by seat. Again a shape argument, volumes need internal validation.

**First 30 days.** Build the ETM migration one-pager mapping each successor to an IrisX reference integration, contact BearingPoint and STAEDEAN partner teams, and extend the existing Wynne relationship to cover RentalResult explicitly. Ask sales for any current Trackunit customers running SAP ETM.

**Main risk.** Timing. Migrations may already be specified without a telematics decision point, and 2027 makes this window finite. Mitigation: target the systems integrators writing the migration blueprints, not the end customers.

Account plans: [BearingPoint ETM.next →](accounts/bearingpoint-etm-next.html) · [Wynne RentalResult →](accounts/wynne-rentalresult.html)

### **3. Point of Rental: the Deepen template**

**Why now.** The formal partnership dates from January 2025: a two-way API between Trackunit and Point of Rental's Expert and Elite products, syncing on-rent and off-rent status, delivery and billing data. Point of Rental brings 5,000+ business locations across 80 countries. The integration exists. What the public record does not show is a marketplace-grade connector, a joint go-to-market plan, or consumption instrumentation. That gap is the whole Deepen thesis: the fastest credits are the ones sitting inside partnerships already signed.

**The integration.** Three upgrades. First, package the two-way API work as a reusable, self-service connector in the Trackunit Marketplace, matching the pattern of the existing RentalMan and Baseplan ERP connectors. Second, extend coverage beyond Expert and Elite toward the full product line. Third, instrument it: per-tenant activation, pull frequency and credit consumption reporting, so the partnership has a dashboard, not an anniversary press release.

**Consumption logic (assumption).** Rental workflows are inherently high-frequency: contract status changes, meter reads for billing, location for logistics. Reasoning from the location count, even modest per-location activation across 5,000+ locations compounds into a steady consumption base, and two-way sync doubles the API surface per contract event.

**First 30 days.** Joint review with Point of Rental product leadership on activation numbers, agree one co-marketing motion into their user base, and scope the marketplace connector build. This dossier doubles as the template for inspHire, MCS, Texada and Wynne.

**Main risk.** Point of Rental offers its own Hapn telematics bundle, so deepening competes with an in-house revenue line. Mitigation: position IrisX for mixed OEM fleets Hapn hardware does not cover.

[Account plan: Point of Rental →](accounts/point-of-rental.html)

### **4. Microsoft Dynamics 365 plus Copilot: two channels, one conversation**

**Why now.** Dynamics 365 is already named on the IrisX integrations page, and Trackunit's MCP Server, launched at IRE 2026, connects IrisX fleet data to Microsoft Copilot (listed as coming soon in Trackunit's own support material). That means one Microsoft-facing motion covers two channels at once: the ERP backbone where rental and service transactions live, and the AI agent channel where natural-language fleet queries will run. No other candidate offers two consumption surfaces for one partner conversation.

**The integration.** On the ERP side, work through the Dynamics rental ISV layer, STAEDEAN, Sycor and HSO, embedding IrisX feeds into rental invoicing and maintenance workflows; Sycor already markets telematics-driven ERP processes, so the pitch lands on prepared ground. On the AI side, finish and certify the Copilot connection of the MCP Server and pursue placement in Microsoft's enterprise agent distribution. The strategic prize, marked as inference, is co-sell status through Microsoft's construction and field-service verticals.

**Consumption logic (assumption).** ERP consumption is steady and transaction-driven: invoicing and service events pull meter data on schedule. Agent consumption is additive and behavioral: every Copilot question about a machine is an API call that did not exist before. The reasoning is that agent channels grow consumption without any new connector build, one MCP endpoint serves every Copilot tenant.

**First 30 days.** Confirm the Copilot connector timeline internally, book conversations with STAEDEAN and Sycor partner leads, and define what a certified AppSource listing requires.

**Main risk.** Microsoft's scale means slow motion and generic partner treatment. Mitigation: enter through the ISVs, who are small enough to move quarterly, and let the Copilot channel ride the MCP Server that already exists.

[Account plan: Microsoft →](accounts/microsoft.html)

### **5. Palantir Foundry: the bold bet**

**Why now.** This is the clearly labeled bet of the five. Palantir has a proven construction deployment: Thomas Cavanagh Construction runs dispatch, trucking and site operations on Foundry, with 97% daily employee usage, connecting telematics, maintenance and demand signals to cut idle time. That case shows large contractors will run daily operations on an ontology platform, and an ontology platform is only as good as its data feeds. Foundry ingests IoT, streaming and geospatial data natively; nobody normalizes off-highway machine data across 100+ OEM integrations the way IrisX does.

**The integration.** IrisX as a certified telematics source for Foundry construction ontologies: time series, location and fault data flowing into the machine objects that dispatch and scheduling logic runs on, delivered through the IrisX Time Series and GraphQL APIs and the AEMP 2.0 export.

**Consumption logic (assumption).** Ontology platforms do not sample, they synchronize. Reasoning from the Cavanagh pattern, a Foundry deployment would pull continuously across an entire fleet to keep dispatch models current, making a single enterprise deployment a durable, high-throughput credit consumer, plausibly worth many conventional connectors. This is the least validated claim in the whole mapping and is presented as exactly that.

**First 30 days.** Identify shared prospect accounts, large contractors and equipment owners evaluating Foundry, and build one demonstration ontology object fed by IrisX data. One named joint prospect decides whether this stays on the list.

**Main risk.** Deal count. Palantir deployments are few, large and slow, and construction may stay a niche vertical for them. Mitigation: cap effort until a joint prospect exists, and treat the demo asset as reusable for other AI platform conversations.

[Account plan: Palantir →](accounts/palantir.html)

## Summary

| Partner | Category | Disposition | Primary consumption driver | First milestone |
|---|---|---|---|---|
| Procore | ConTech | Pursue | Daily mixed-fleet pulls by project teams (assumption) | Demo against Equipment Telematics API |
| SAP ETM successors | ERP | Pursue | Fleet-wide meter and contract sync per migration (assumption) | Reference architecture per successor, BearingPoint and STAEDEAN contact |
| Point of Rental | Rental management | Deepen | Two-way contract, billing and meter sync (assumption) | Marketplace-grade connector scoped, activation dashboard |
| Microsoft Dynamics 365 + Copilot | ERP | Pursue | ERP transactions plus per-query agent calls via MCP (assumption) | ISV conversations opened, Copilot connector timeline confirmed |
| Palantir Foundry | AI | Monitor | Continuous fleet sync into ontology objects (assumption) | One named joint prospect, upgrade on trigger |

*First pass from public sources. Presented to demonstrate methodology, to be validated with internal data.*
