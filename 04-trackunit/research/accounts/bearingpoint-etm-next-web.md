# BearingPoint / ETM.next - Web Digest (July 2026)

## Snapshot
- BearingPoint is an independent management and technology consultancy, partner-owned (partnership model, parent BearingPoint Europe Holdings B.V.), headquartered in Amsterdam, Netherlands.
- FY2025: revenue EUR 1.026 billion (about USD 1.16 billion), third consecutive year above EUR 1 billion; bookings near EUR 1.3 billion; 2,200+ projects in 26 countries; roughly 6,200 employees; 1,000+ new hires in 2025 incl. 16 new Partners (press release, 5 March 2026).
- Alliances: ABeam (Asia; new North America JV "BearingPoint North America" launched with ABeam), Arcwide JV with IFS (gross revenue +14% in 2025).
- ETM.next is BearingPoint's productized SaaS: equipment and tools management (fleet, rental, tools, logistics, billing) for construction and other asset-heavy industries. Sold via SAP Store, run by BearingPoint Business Services B.V. Won SAP Pinnacle Award 2021, SAP Endorsed App since April 2022, and more recently an SAP Spotlight+ designation on SAP Store (date not stated on the news page).

## Why now signals
- Burning platform: SAP Equipment and Tools Management for EC&O (legacy SAP ETM) usage rights in S/4HANA compatibility mode ended in 2025; maintenance in the ERP context ends 2027. ETM.next is SAP's endorsed industry cloud successor, co-innovated with SAP's EC&O Industry Business Unit and existing ETM customers. Every remaining SAP ETM contractor must migrate now (inference: 2026-2027 is the peak migration window).
- BearingPoint exhibited ETM.next at bauma 2025 in Munich (7-13 April 2025, Hall A2 Booth N); earlier presence at bauma China. Trackunit also exhibits at bauma (inference: shared event circuit).
- Customer momentum: SACDE (leading Argentine contractor) went live with ETM.next ahead of its S/4HANA go-live (news posted on the ETM.next site, undated but recent); earlier adopters include Graham Construction (Canada, 2021), Eiffage (France), Hitachi Energy, Fluxys, Jean Bratengeier (DE); SAP itself is listed as a user.
- Blog series through 2025-2026 ("From isolated tools to ETM.next", parts 1-4) plus an insight arguing that rebuilding custom ECC/ETM code in S/4HANA is a costly mistake: active demand-gen against the 2027 deadline.
- Competitive pressure: Wynne Systems (RentalResult) and others run "SAP ETM sunset" campaigns targeting the same install base, so the migration market is contested.
- North America expansion (ABeam JV) plus US ETM.next delivery hiring (below) signal a push beyond the European base.

## Hiring signals
- US job listings (Indeed/Glassdoor aggregation): "SaaS Implementation Manager/Consultant - ETM.next" (Chicago, USD 135-170K) and "Solution Implementation Consultant - ETM.next" (Chicago, USD 82-110K), plus SAP CO consultants. Inference: building a dedicated US ETM.next implementation bench to serve North American contractors, consistent with the Graham Construction reference and the new North America JV.
- BearingPoint Romania advertises a "Cloud Support Lead" role connected to product/cloud operations (Teamtailor listing). Inference: Romania is a nearshore support hub for the product business.
- No public postings found for ETM.next partnerships/alliances or telematics-specific roles; the product team is reached through the IP Assets unit (Donald Wachs, Management Committee member globally responsible for IP Assets) and Christoph Kühne, Business Development Manager, named as contact in the SACDE story.

## Integration-relevant facts
- Architecture: ETM.next runs on SAP BTP as a side-by-side extension to SAP ERP/S/4HANA (on-prem, private and public cloud), connected via SAP cloud connectors; SaaS subscription; standard 2-3 month fast-track implementation.
- Telematics: the official FAQ states ETM.next "employs RESTful OData APIs to connect with the OEM telematic platform according to international standards such as AEMP 2.0 or ISO 15413-3" (their typo; the standard is ISO 15143-3). Marketing lists IoT integration, geo-fencing, asset track and trace, and "open interfaces with the proprietary ETM platforms of major OEMs."
- That is exactly the interface Trackunit exposes: Trackunit publishes an ISO 15143-3 (AEMP 2.0) export API on its developer hub, with metadata extensions for system integration. No public evidence of an existing ETM.next-Trackunit integration was found (searched July 2026). Inference: a natural partnership gap; ETM.next needs mixed-fleet telematics feeds (hours, position, fuel, status) for utilization, idle-time and billing logic, and Trackunit/IrisX could be the aggregation layer instead of per-OEM connections, driving IrisX credit consumption per connected asset.
- ETM.next also pushes data to SAP Analytics Cloud, has Fiori apps, a web shop, planning board, and native iOS/Android apps.
- Who runs SAP ETM today: publicly documented ETM.next adopters were SAP ETM or equipment-management legacy users (Graham, Eiffage, Hitachi Energy, SACDE). A named list of remaining SAP ETM contractors was not found in public sources; SAP ETM was historically strong among large German-speaking and French contractors (inference from the EC&O install base; verify via BearingPoint or SAP references).
- Implementation partners around ETM.next: Dimensys (NL/BE, published an SAP ETM vs ETM.next comparison), Iquant (delivered SACDE in Argentina). Inference: a small SI ecosystem exists that Trackunit could also enable.

## Sources
- https://bearingpoint.services/etm/en/
- https://bearingpoint.services/etm/en/faq/
- https://bearingpoint.services/etm/en/news/
- https://bearingpoint.services/etm/en/news/customer-success-story-sacde-argentina/
- https://bearingpoint.services/etm/en/news/our-partner-dimensys-to-compare-sap-etm-vs-etmnext/
- https://bearingpoint.services/etm/en/events/bauma-april-2025-in-munich/
- https://www.bearingpoint.com/en-us/about-us/news-and-media/press-releases/etmnext-by-bearingpoint-now-an-sap-endorsed-app/
- https://www.bearingpoint.com/en/about-us/news-and-media/press-releases/bearingpoint-delivers-over-1billion-in-revenue-third-year-running/
- https://en.wikipedia.org/wiki/BearingPoint
- https://store.sap.com/dcp/en/product/display-2001011301_live_v1/etm.next/
- https://www.sap.com/products/scm/partners/bearingpoint-business-services-bv-etmnext.html
- https://news.sap.com/2021/03/graham-construction-etmnext-equipment-tools-management/
- https://developers.trackunit.com/reference/export-iso-15143-3-aemp-20-api-intro
- https://wynnesystems.com/sap-etm-sunset/
- https://www.glassdoor.com/Jobs/BearingPoint-Jobs-E11516.htm (ETM.next Chicago roles)
- https://bearingpointromania.teamtailor.com/jobs/7851730-cloud-support-lead
