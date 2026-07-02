# Trackunit OEM Ecosystem Digest (research as of July 2026)

## Key findings

- Trackunit claims 100+ OEM integrations on its OEM integrations page and 7,000+ "trusted construction partners" under the Works With Trackunit program; its press stated 1.25M connected assets in April 2024 and a separate press release announces passing 1.4M+ connected assets.
- The OEM layer has three distinct motions: (1) "powered by Trackunit" white-label telematics for OEMs (Skyjack Elevate, Niftylift Niftylink, SCHWING), (2) component and engine maker partnerships feeding data into IrisX (Cummins, Bosch Rexroth, Danfoss, Perkins, Hilti), and (3) self-service OEM data feeds in the Trackunit Marketplace that pull competitor and mixed-fleet OEM data (Caterpillar, Komatsu KOMTRAX, Volvo CE, John Deere, JLG ClearSky, Manitou) into Trackunit Manager without Trackunit hardware.
- ISO 15143-3 (AEMP 2.0) is the lingua franca in both directions: Trackunit exposes an outbound AEMP 2.0 export API on Iris (OAuth 2.0, snapshot endpoints for all customers, time series gated to higher subscription packages), and the Marketplace "ISO feed self-service" apps ingest OEM feeds that OEM ecosystems (Cat VisionLink/Cat Digital, Komatsu, Deere JDLink) publish under the same standard.
- Works With Trackunit is a branded compatibility and ecosystem program: OEMs get "Works With" branding, custom-branded presence in Trackunit Manager, access to Trackunit technology, and global reach; system integrators, component makers, and app developers are also covered partner types.
- Genie is a notable non-partner: Genie Lift Connect is built with ZTR Control Systems, but exposes a standard ISO 15143-3 API, making it an integration counterpart rather than a "powered by" OEM. No confirmed Hiab-Trackunit partnership was found (Hiab HiConnect launched 2017; sources found do not name Trackunit as supplier).

## Details

### OEM and component partnerships (verified entries)

| # | Partner | Type | What it is | Date / source |
|---|---------|------|-----------|---------------|
| 1 | Skyjack | AWP OEM, "powered by Trackunit" | Skyjack Elevate telematics is powered by Trackunit; partnership announced at ALH Conference, Miami; included a data-only package supporting rental company ERP systems plus a standalone end-to-end solution | Oct 12, 2017; skyjack.com, machinerytrader.com, rermag.com |
| 2 | Niftylift | AWP OEM, factory install | Niftylink, powered by Trackunit; Trackunit is factory install partner; built on Trackunit Manager and Trackunit Go | niftylift.com |
| 3 | SCHWING Group | Concrete machinery OEM, Works With Trackunit | German concrete pump maker fits Trackunit IoT devices on truck-mounted pumps; deal closed late 2023, launched at Intermat Paris; PR cites 1.25M connected assets | Apr 22, 2024; trackunit.com/press |
| 4 | Cummins | Engine maker | Collaboration to surface advanced engine insights in Trackunit to eliminate downtime | Feb 2022 (Cummins PR dated Feb 2, 2023 on cummins.com; Trackunit PR Feb 9, 2022, Aalborg); dates differ across sources |
| 5 | Hilti | Tool OEM | Strategic partnership Jan 31, 2022: ON!Track tools visible in Trackunit and Trackunit-equipped machinery in ON!Track; Hilti later added 500,000+ tags to the Trackunit platform; joint van inventory and heavy equipment solution launched Nov 2023 | trackunit.com/press, hilti.group |
| 6 | Bosch Rexroth | Component / OTA | Strategic partnership embedding Rexroth BODAS Connect OTA update platform into IrisX for secure machine updates; positioned around the EU Cyber Resilience Act | Apr 4, 2025; trackunit.com/press |
| 7 | Danfoss | Component | Danfoss component data surfaced in Trackunit Manager; Trackunit Raw data accessible in Danfoss Plus+1 service tool | Apr 2, 2025; trackunit.com/press |
| 8 | Perkins | Engine maker | Perkins diagnostics app launched on the Trackunit Marketplace to tackle unplanned downtime | trackunit.com/press-releases (undated on listing page) |
| 9 | JLG | AWP OEM, data feed | "JLG ClearSky" ISO feed self-service app in Trackunit Marketplace standardizes JLG data into Trackunit Manager via the Iris ecosystem; ClearSky Smart Fleet (JLG's in-house next-gen IoT platform) rolled out from July 2023; historically ClearSky was built with ORBCOMM | new.manager.trackunit.com marketplace, jlg.com |
| 10 | Manitou | Telehandler OEM, data feed | Manitou OEM app listed in Trackunit Marketplace (oem-apps-manitou); Manitou also markets its own Connected Solutions telematics, so this is a feed integration, not confirmed "powered by" (inference) | new.manager.trackunit.com marketplace |
| 11 | Caterpillar, Komatsu, Volvo CE, John Deere | Major OEM ecosystems, data feeds | Self-service ISO feed apps in the Marketplace (cat-iso-feed, komatsu-iso-feed for KOMTRAX, volvo-iso-feed, johndeere-iso-feed); Trackunit's Data Feeds article: pick feed in Marketplace, complete verification, data flows into Trackunit Manager, no hardware needed | trackunit.com/articles, marketplace listings |
| 12 | Genie (Terex) | Non-partner counterpart | Genie Lift Connect telematics developed with ZTR Control Systems; subscription includes data consumption via portal and/or standard ISO 15143-3 API, so Trackunit-side ingestion is standards-based (inference on ingestion path) | rermag.com, genielift.com |

### What "Works With Trackunit" means for OEMs

Per trackunit.com/become-a-partner: partner categories are OEMs (product differentiation through digitalization), system integrators (ERP, BI, CRM), component makers and tech providers (validated compatibility), and app developers (Marketplace integrations). OEMs get access to Trackunit technologies, global reach, "Works With" ecosystem branding, and custom-branded presence in Trackunit Manager with machine visuals and insights. The page claims 7,000+ construction partners; logos shown include JCB, Hilti, CAT, Volvo, Komatsu. The Marketplace is the integration hub and IrisX is the underlying operating data platform.

The OEM integrations page (trackunit.com/oem-integrations) claims 100+ OEM integrations and displays 70+ logos including Caterpillar, Volvo, John Deere, Komatsu, Liebherr, Hitachi, Doosan, Kobelco, Sany, Yanmar, JLG, Genie, Snorkel, Haulotte, Niftylift, Skyjack, Bobcat, JCB, Wacker Neuson, Kubota, Manitou, Vermeer, Bomag, Terex and others. (Logo presence signals a data feed exists, not necessarily a commercial partnership; inference.)

### ISO 15143-3 (AEMP 2.0) role

- Outbound: Trackunit's developer portal documents an "Export ISO 15143-3 (AEMP 2.0)" REST API (XML or JSON) at iris.trackunit.com/public/api/aemp/v2/15143/-3/ with OAuth 2.0 shared across Iris APIs, pagination at 100 records per page, optional addMetadata=true extension, snapshot endpoints for all customers, and time series endpoints only on Evolve & Expand or Link, Lift & Leap packages. A legacy AEMP 1.2 API carries a deprecation warning.
- Inbound: the Marketplace ISO feed self-service apps consume OEM-published ISO 15143-3 feeds; on the OEM side, Cat Digital Marketplace publishes an ISO 15143-3 (AEMP 2.0) developer guide and a third-party API integrations tool for VisionLink, and Genie exposes the same standard API. This makes AEMP 2.0 the default contract for cross-ecosystem integrations with Cat VisionLink, Deere JDLink/Operations Center, and Komatsu (KOMTRAX), even where no bilateral partnership exists (inference on strategic framing).
- Counterpart note: John Deere Operations Center runs its own partner ecosystem (Razor Tracking, Fleetio, Samsara integrations found); Trackunit today ingests Deere data via the ISO feed rather than a two-way Operations Center listing, based on sources found (inference).

### Gaps and negatives worth knowing

- Hiab: no source found tying HiConnect to Trackunit; HiConnect launched Sept/Oct 2017 (Cargotec PR) without naming Trackunit. Treat "Hiab is a Trackunit OEM partner" as unverified.
- Genie: confirmed ZTR, not Trackunit.
- Rental-side anchor: Sunbelt Rentals UK & Ireland extended its Trackunit partnership in Nov 2025 (fleet connectivity, Sunbelt 4.0 strategy), useful as the demand-side pull for OEM feeds.

## Sources

- https://trackunit.com/oem-integrations/
- https://trackunit.com/become-a-partner/
- https://trackunit.com/press/german-oem-schwing-group-agrees-works-with-trackunit-partnership/
- https://www.skyjack.com/node/568
- https://www.machinerytrader.com/blog/construction-equipment-news/2017/12/aerial-work-platform-provider-skyjack-partners-with-trackunit-on-telematics-solution
- https://www.niftylift.com/uk/about-us/blog/news/introducing-niftylink
- https://trackunit.com/press/partnership-leveraging-advanced-insights/
- https://www.cummins.com/news/releases/2023/02/02/cummins-and-trackunit-announce-collaboration-gain-advanced-insights-and
- https://trackunit.com/press/hilti-and-trackunit-announce-strategic-partnership/
- https://trackunit.com/press/hilti-trackunit-strengthen-partners/
- https://trackunit.com/press/trackunit-bosch-rexroth-partnership-construction-industry/
- https://trackunit.com/press/trackunit-danfoss-partnership-eliminate-downtime/
- https://trackunit.com/press-releases/
- https://trackunit.com/press/sunbelt-trackunit-partnership/
- https://new.manager.trackunit.com/marketplace/@trackunit/jlg-iso-feed-self-service
- https://new.manager.trackunit.com/marketplace/@trackunit/oem-apps-manitou
- https://new.manager.trackunit.com/marketplace/@trackunit/cat-iso-feed-self-service
- https://new.manager.trackunit.com/marketplace/@trackunit/komatsu-iso-feed-self-service
- https://new.manager.trackunit.com/marketplace/@trackunit/volvo-iso-feed-self-service
- https://new.manager.trackunit.com/marketplace/@trackunit/johndeere-iso-feed-self-service
- https://trackunit.com/articles/trackunit-fleet-data-feeds/
- https://developers.trackunit.com/reference/export-iso-15143-3-aemp-20-api-intro
- https://digital.cat.com/knowledge-hub/articles/iso-15143-3-aemp-20-api-developer-guide
- https://www.rermag.com/business-technology/article/20953457/genie-partners-with-ztr-to-develop-genie-lift-connect-telematics-system
- https://www.genielift.com/docs/default-source/default-document-library/en/api-flyer-na-2020-en-lowres.pdf
- https://www.cargotec.com/en/nasdaq/press-release-hiab/2017/hiab-presents-the-pioneering-hiconnecttm---a-connected-solution-for-load-handling/
- https://trackunit.com/press/connecting-1-4m-assets/
- https://www.jlg.com/en/technology-innovation/clearsky-smart-fleet

_Verified: adversarial cross-check of 12 load-bearing claims against primary sources (trackunit.com press releases and product pages, developers.trackunit.com, niftylift.com, become-a-partner and oem-integrations pages) and independent coverage (RER Magazine for Skyjack and Genie/ZTR, web-indexed Trackunit Marketplace listings for the JLG/John Deere/Manitou ISO feed apps). All 12 claims confirmed: Skyjack-Trackunit (Oct 12, 2017, ALH Miami, data-only ERP package per RER), Niftylink powered by Trackunit (factory install, Trackunit Manager + Go), SCHWING Works With Trackunit (PR Apr 22, 2024, Intermat launchpad, 1.25M assets, agreement "effectively agreed towards the end of 2023"), Bosch Rexroth BODAS Connect OTA into IrisX with EU Cyber Resilience Act framing (PR Apr 4, 2025), Danfoss Plus+1 two-way data (PR Apr 2, 2025), Hilti strategic partnership (dateline 31.01.2022, Aalborg; 500,000+ ON!Track tags per follow-up PR), Marketplace self-service ISO feeds (Cat/Komatsu/Volvo named in Trackunit's data-feeds article as hardware-free; JLG ClearSky, John Deere, Manitou listings confirmed via indexed marketplace pages), 100+ integrations (oem-integrations page, wording "100+ integrations") and 7,000+ trusted construction partners (become-a-partner page), AEMP 2.0 export API with OAuth 2.0 (Iris access-token docs) and snapshot-for-all vs time-series-on-Evolve & Expand/Link, Lift & Leap gating, Genie Lift Connect built with ZTR exposing standard ISO 15143-3 API (RER + Genie FAQ), Cummins date discrepancy real (Trackunit PR dateline Feb 09, 2022, Aalborg vs Cummins release URL dated Feb 2, 2023), and no source ties Hiab HiConnect to Trackunit (search of Hiab/Cargotec materials and telematics coverage found Assured Telematics/Geotab integrations instead). Machinerytrader.com was unreachable (403) but the Skyjack claim was independently confirmed via RER Magazine and multiple trade outlets._
