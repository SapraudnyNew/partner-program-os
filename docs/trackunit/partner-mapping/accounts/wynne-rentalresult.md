# Account Plan: Wynne Systems (RentalMan / RentalResult)

## Account snapshot

Wynne Systems, headquartered in Irvine, California, builds enterprise software for equipment rental: RentalMan, the rental ERP that Wynne says powers the top four global rental companies (United Rentals, Sunbelt Rentals, Herc Rentals, Loxam), and RentalResult, the construction equipment and tool management product acquired with Result Group in December 2015. The company is part of Volaris Group, an operating group of Constellation Software, which acquired Wynne from United Rentals in May 2012. It is small: roughly 100 to 120 employees, with revenue in the low tens of millions (inference from third-party estimates). Clare McCormick was recently promoted to General Manager, and Robert Gray moved to Chief Revenue Officer with a mandate for new markets. Wynne already intersects IrisX today: an official Trackunit integration page covers RentalMan and TMS, and an "ERP Connector - RentalMan" listing exists on the Trackunit Marketplace. The play is to deepen that legacy connector into an IrisX-native, credit-consuming marketplace app, and to attach IrisX to RentalResult as it captures fleets migrating off SAP ETM.

## Why now

- **February 2026 (content refresh):** Wynne runs an active SAP ETM sunset campaign positioning RentalResult as the purpose-built replacement. SAP ETM usage rights in S/4HANA compatibility mode ended in 2025 and maintenance ends in 2027, so contractor equipment fleets are re-platforming on a fixed schedule. The campaign page now redirects to rentalresult.com, suggesting RentalResult is being built out as a distinct contractor-facing brand (inference).
- **January 2025:** Wynne named Foresight Intelligence its "preferred telematics provider" for RentalMan. Not stated as exclusive, but it is a competitive wedge inside Wynne's telematics stack and a reason to move now rather than later.
- **Q3 2025 and spring 2026:** active product cadence. A Q3 2025 RentalMan release shipped IntelliSource, Logistics, Service, RapidCount and MobileLink updates; a Logistics Solution is coming to RentalResult in spring 2026; Re-Rentals Direct now auto-creates RentalMan pickups from RentalResult requisitions, wiring contractors directly to rental suppliers.
- **October 5-7, 2026:** Wynne User Summit in Charlotte, NC. A concrete co-marketing and field-engagement milestone within the first two quarters of the role.
- **July 2026 (hiring board):** only three open roles, none in partnerships, platform or integrations. Integrations sit with the existing product org, so the window to shape the connector roadmap runs through product management and the CRO, not a partner team (inference).

## Org map: key people

| Name | Title | Location | LinkedIn | Owns / why relevant | EMEA |
|---|---|---|---|---|---|
| Clare McCormick | General Manager | Greater Phoenix Area | https://www.linkedin.com/in/clare-mccormick-5901b99b | Runs the business unit; final commercial sign-off on any partnership economics in a Volaris-style P&L (inference) | No |
| Kenneth Kimura | Director of Product Development | Round Rock, Texas, United States | https://www.linkedin.com/in/kenneth-kimura-b897bb80 | Director-level product owner; the roadmap decision on upgrading the RentalMan connector to an IrisX-native app runs through him (inference) | No |
| Steve Kistler | Director Software Development | Glendale, Arizona, United States | https://www.linkedin.com/in/steve-kistler-b972828 | Engineering leadership; scopes and staffs the actual connector build against IrisX APIs | No |
| Tsvety Petrova | Product Manager | Edinburgh, Scotland, United Kingdom | https://www.linkedin.com/in/tsvety-petrova-8aa27569 | EMEA-based product manager; closest longlist match to the RentalResult and SAP ETM migration motion given the product's UK roots (inference); employment at Wynne Systems Edinburgh confirmed, title from LinkedIn scan only, not independently confirmed | Yes |
| Kevin Shaw | Technology Manager | Elland, England, United Kingdom | https://www.linkedin.com/in/kevin-shaw-4999582a | Technology lead at Wynne Systems (UK) Ltd; the technical counterpart for EMEA deployments and integration questions | Yes |
| Ashish Udeshi | Senior Product Manager | Placentia, California, United States | https://www.linkedin.com/in/ashish-udeshi | Senior PM near Irvine HQ; likely hands-on owner of specific RentalMan integration surfaces (inference) | No |
| Steven Tripp | Marketing Director | Washington DC-Baltimore Area | https://www.linkedin.com/in/steventripp | Owns co-marketing and the Wynne User Summit surface, the October 2026 activation milestone | No |

First entry point: Kenneth Kimura, Director of Product Development. Wynne has no partnerships or marketplace owner in the scan, and the web digest confirms the product org handles integrations, so the connector conversation starts with the person who owns product development. Tsvety Petrova in Edinburgh is the parallel EMEA door for the RentalResult and SAP ETM thread, and the preferred first call if the initial motion is European. Clare McCormick comes in second, once there is a concrete connector proposal to price.

## What the employee scan shows

The scan covered 30 unique current employees, consistent with a company of roughly 116 people where LinkedIn coverage is partial.

- **No partnerships function exists.** Zero titles containing partnerships, alliances or business development. Product management and the executive layer absorb integrations and partner relationships, which changes who you call first.
- **Sales is the heaviest function.** Two Enterprise Account Managers, two Enterprise Sales Managers, a Sales Engineer, an Inside Sales Representative and a Revenue Operations Manager. Wynne grows by selling deeper into enterprise accounts, matching the digest's read of the hiring board.
- **Product is small but deliberately distributed.** One Director of Product Development (Texas), one Senior PM (California, near HQ), and two PMs in Toronto and Edinburgh. The Edinburgh seat is notable: product presence where RentalResult's UK roots are (inference).
- **EMEA is thin: two people.** Kevin Shaw (Technology Manager, UK, 1 month in role) and Tsvety Petrova (PM, Edinburgh). Combined with the open UK Enterprise Account Manager role, this reads as an early-stage European enterprise push (inference).
- **Tenure and titles hint at renewal and AI interest.** Most captured tenures are under a year, which likely reflects recent role changes or scrape limits rather than mass hiring (assumption). A Senior AI Developer (8 months) is a concrete signal that even a 116-person Constellation company is staffing AI work.

## Integration angle and entry path

The play has two legs. Leg one, Deepen: the existing RentalMan connector on the Trackunit Marketplace is legacy-grade, and the January 2025 Foresight designation shows the default telematics slot in RentalMan is contested. The counter is an IrisX-native connector that does what a preferred-provider feed does not: off-rent triggers and two-way contract sync through the IrisX Rental ERP API, utilization and meter data for billing through the Time Series API, and fleet and asset queries through GraphQL, all metered in IrisX credits across RentalMan tenants at United Rentals, Sunbelt, Herc and Loxam scale (inference on volumes). Leg two, Pursue: pair RentalResult with IrisX as the equipment data layer for the SAP ETM migration cohort, where every closed migration lands a full contractor fleet on day one. The MCP surface is a later add, once connector data flows exist to expose to agents (assumption). Sequence of first conversations by role: Director of Product Development first, to scope the connector upgrade; the EMEA Product Manager in parallel, to open the RentalResult and ETM thread; then the General Manager, to frame commercial terms; the Marketing Director next, to lock a Wynne User Summit slot; Director of Software Development last, once scope is agreed. One gap to name honestly: the longlist contains no CRO and no named RentalMan or RentalResult product line managers, although the web digest identifies Robert Gray, Jim Rosinke and Craig Richmond in those roles, so those introductions must come through the product development door or through shared customers rather than from this scan.

## First 30 days and main risk

- Pull internal IrisX data on the existing RentalMan ERP connector: active tenants, pull frequency, credit consumption baseline. This is the before picture the whole Deepen case is measured against.
- Identify who inside Trackunit currently owns the Wynne relationship and what the Foresight announcement changed in practice.
- Request a scoping call with Wynne product development leadership: one page on the IrisX-native connector (Rental ERP API for contract sync and off-rent triggers, Time Series for utilization billing, GraphQL for fleet queries).
- Open the RentalResult thread with the EMEA product manager: a reference architecture for SAP ETM migrations with IrisX as the telematics layer, reusable across the BearingPoint and STAEDEAN plays.
- Ask Trackunit sales for shared customers running RentalMan or RentalResult, starting with the top four rental accounts, to anchor the conversation in live fleets.
- Reserve a presence at the Wynne User Summit, October 5-7, 2026, Charlotte, as the activation deadline for a demonstrable connector.

**Main risk:** the Foresight Intelligence "preferred telematics provider" position hardens into a default, and Trackunit becomes one checkbox among many in RentalMan telematics. Mitigation: anchor in the shared enterprise customers, since the top four rental companies run RentalMan and operate mixed fleets at a scale where Trackunit's 100+ OEM normalization is the differentiator Foresight cannot match (inference), and make the marketplace-grade connector, with instrumented consumption reporting, the proof Wynne's product team can see.

Sources: wynnesystems.com/integrations/trackunit/, wynnesystems.com/rentalresult/, rentalresult.com/sap-etm-sunset-a-critical-opportunity-to-consolidate-and-modernize-equipment-management/, rermag.com (Foresight announcement), volarisgroup.com press room, volarisgroup.wd3.myworkdayjobs.com/WynneNA, new.manager.trackunit.com/marketplace/@trackunit/erp-connector-rental-man.

*Built from public LinkedIn and web data. First pass, presented to demonstrate account-based methodology. People data as of July 2026.*
