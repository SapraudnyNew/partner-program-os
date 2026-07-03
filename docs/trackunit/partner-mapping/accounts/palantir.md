# Account Plan: Palantir Technologies

## Account snapshot

Palantir Technologies is a public company (NASDAQ: PLTR), headquartered in Denver, Colorado, with 4,429 full-time employees as of December 31, 2025, 28% of them outside the US. Q1 2026 revenue was $1.6B, up 85% year over year, with US commercial revenue of $595M up 133%, and FY2026 guidance raised to about $7.65B. Its go-to-market is direct: forward deployed engineers and deployment strategists land accounts through short bootcamp engagements, and no classic reseller or alliances program exists on the commercial side. Construction is now a named vertical, with a "Palantir for Construction" offering page live and two flagship contractor deployments, Thomas Cavanagh Construction and McCarthy Building Companies. The intersection with IrisX is the data layer: Foundry ontologies for construction run on equipment, GPS and dispatch data, exactly the machine telemetry IrisX normalizes across 100+ OEM integrations. Palantir's pattern of replacing point software is also a displacement risk for app-layer vendors, which makes the upstream data-feed position the defensible one (inference).

## Why now

- **Late May 2026**: Thomas Cavanagh Construction extended its Foundry partnership to an 11-year term through December 31, 2035; PLTR stock rose about 17% on the news. Cavanagh also created a subsidiary, Cavtera, to commercialize its Foundry-built construction apps and support Palantir implementations across construction, a customer turning into a channel.
- **June 2026**: McCarthy Building Companies, a major US general contractor, signed a multi-year, multi-million dollar partnership; its AI-native field system "Pulse" was demoed at AIPCon 10. Construction is getting a second flagship.
- **June 2026**: Foundry became available on Google Cloud Marketplace with two-way BigQuery integrations and Gemini-AIP connectivity, part of a broader ecosystem formalization alongside the Accenture Palantir Business Group and the Databricks product partnership.
- **February 2026**: DevCon2 introduced Embedded Ontologies for offline edge devices, explicitly citing mining and construction sites with unreliable networks, a direct fit for off-highway equipment telemetry.
- **Q1 2026 results**: revenue up 85%, US commercial up 133%, trailing 12-month US commercial TCV bookings of $4.7B up 115%. The commercial engine that would carry a construction data partnership is the fastest-growing part of the company.

## Org map: key people

| Name | Title | Location | LinkedIn | Owns / why relevant | EMEA |
|---|---|---|---|---|---|
| Noah Diskin Kline | VP, Commercial Business Development | New York, New York, United States | https://www.linkedin.com/in/noahdiskin/ | Most senior commercial BD title in the scan; the level that can sponsor an ISV-style data partnership | No |
| Tom Buller | Commercial Business Development EMEA | London, England, United Kingdom | https://www.linkedin.com/in/tom-buller/ | International commercial BD out of London; the closest thing to an EMEA ecosystem door in the scan | Yes |
| Zachary Zlotnick | Global Business Development - FedStart | Los Angeles, California, United States | https://www.linkedin.com/in/zacharyzlotnick/ | FedStart is Palantir's only formal ISV motion; he sits where third-party software meets Palantir GTM | No |
| Martijn Koerts | Head of Sales and Business Development Benelux | Amsterdam, North Holland, Netherlands | https://www.linkedin.com/in/martijn-koerts-18980b5/ | Named country ownership in Benelux, a dense construction and equipment rental market; public records show a government-sector focus | Yes |
| Jørn Henrik Levy Rasmussen | Sales Executive | Copenhagen, Capital Region of Denmark, Denmark | https://www.linkedin.com/in/jorn-henriklevyrasmussen/ | Senior presence in Trackunit's home market; influence mapping for a Nordic-anchored conversation | Yes |
| Thor Snedker Brandt | Business Development | Copenhagen, Capital Region of Denmark, Denmark | https://www.linkedin.com/in/thorsnedkerbrandt/ | Working-level BD in Copenhagen, joined about 3 months ago; the practical local door | Yes |
| Kaan Korkmaz | Deployment Strategist | Munich, Bavaria, Germany | https://www.linkedin.com/in/ACwAAAzxW9gB0rjkySWeEr5gFu0CbQgAhMnp7kk | Industrials deployment in DACH; deployment strategists run the accounts where an IrisX feed would actually land (LinkedIn scan only, not independently confirmed) | Yes |

First entry point: Tom Buller. There is no partnerships or marketplace owner anywhere in the scan, so the entry has to run through commercial business development, and Buller combines the international commercial remit with a London seat close to Trackunit's EMEA footprint. The Copenhagen pair, Rasmussen for seniority and Brandt for working-level contact, is the parallel local path, with Noah Diskin Kline as the US sponsor once a joint prospect exists.

## What the employee scan shows

The scan covers 44 unique people surfaced by business development and industrials queries.

- Two functions dominate and nothing else appears: business development (about half the list) and deployment strategists (the other half). Not a single title contains partnerships, alliances, channel or marketplace, which matches the job-board finding that no such roles are posted. BD and deployment people do the partner-shaped work at Palantir (inference).
- Tenures are strikingly short. Over half the list shows 5 months or less at the company, and 11 people show 1 to 2 months. Palantir is building out both the BD and deployment benches right now, consistent with the 85% revenue growth (inference).
- Geography splits into a US core (New York and Washington DC clusters, plus Denver and LA) and a real EMEA bench: London is the largest non-US cluster, with two people in Copenhagen, plus Amsterdam, Paris, Madrid, Munich, Dubai and Abu Dhabi. The Copenhagen presence sits in Trackunit's home market.
- Title patterns reveal a geographic ownership model, not a functional one: Head of BD and Sales Benelux, Sales Director Japan, International BD Commercial, Australian Commercial. Only one VP-level BD title appears in the whole scan, so decision paths above that level are outside this data (assumption).
- Every deployment strategist is an individual-contributor title with no named vertical lead for construction or industrials, which suggests vertical plays like Cavanagh are account-driven rather than run by a construction team (inference).

## Integration angle and entry path

The play, labeled a bold bet in the First Five, is IrisX as a certified telematics source for Foundry construction ontologies, following the Cavanagh pattern where dispatch, trucking and site operations run on equipment, GPS and truck-scale data. Ontology platforms synchronize rather than sample, so a single Foundry deployment pulling continuously across a whole fleet is plausibly a high-throughput, durable IrisX credit consumer (assumption). The mapping to IrisX surfaces: the Time Series API feeds hours, fuel, location and fault streams into Foundry machine objects; GraphQL serves the asset and fleet structure those objects hang on; the MCP Server becomes relevant later for AIP agents querying live fleet state; the Rental ERP API is secondary here, useful only if the joint account is a rental company. Because Palantir has no partner program to apply to, the sequence runs by role: first a commercial BD conversation (international or EMEA BD) to surface one shared prospect, a large contractor or equipment owner evaluating Foundry; then the deployment strategist on that account, since deployment teams decide what data enters the ontology; then, if the pattern repeats, a FedStart-style hosting or listing conversation with the global commercial BD level. The longlist contains no partnerships, alliances or marketplace owner and no named construction vertical lead, so those conversations cannot be booked from this data; the BD-first path above is the honest substitute. Per the First Five trigger, effort stays capped until one named joint prospect exists.

## First 30 days and main risk

- Ask Trackunit sales and customer success for any customer or prospect that has run or booked a Palantir bootcamp, or that mentions Foundry in RFPs. One named joint prospect is the go/no-go trigger.
- Build one demonstration ontology object, a machine object fed by IrisX Time Series and GraphQL data, reusable for other AI platform conversations regardless of the Palantir outcome.
- Watch Cavtera: as a construction-focused Foundry implementer it needs telematics feeds for every future customer, and it may be a faster door than Palantir itself (inference).
- Open the EMEA BD conversation (London, then Copenhagen) only after the demo asset exists, so the first meeting shows data in an ontology rather than a slide.
- Read the ISG "Palantir Ecosystem Partners" report due July 2026 to see whether a formal partner tier is emerging worth applying to.
- Main risk: deal count. Palantir deployments are few, large and slow, construction may stay a niche vertical for them, and there is no partner program to institutionalize the relationship. Mitigation: cap effort until the joint prospect exists, keep the demo asset platform-neutral, and treat Cavtera and McCarthy-style contractors as alternate routes to the same consumption.

Sources: palantir.com/offerings/construction, blog.palantir.com (Cavanagh case, FedStart), investors.palantir.com (Q1 2026), sec.gov (FY2025 10-K), newswire.ca and palantirbullets.com (Cavanagh extension, Cavtera), stocktitan.net and constructiondive.com (McCarthy), businesswire.com (Google Cloud Marketplace, ISG, Warp Speed, Stellantis, AIPCon 10), jobs.lever.co/palantir.

*Built from public LinkedIn and web data. First pass, presented to demonstrate account-based methodology. People data as of July 2026.*
