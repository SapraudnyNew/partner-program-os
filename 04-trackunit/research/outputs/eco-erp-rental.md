# Ecosystem research, part 1: ERP and rental management software (integration partner candidates for Trackunit IrisX)

Research date: 2026-07-02. Focus: ERP systems used in construction/equipment rental and dedicated rental management systems (RMS), their market presence, existing Trackunit/telematics integrations, IrisX value logic, and typical decision maker roles.

## Key findings

- Trackunit already has a substantial ERP/RMS connector footprint: the IrisX integrations page claims "1,200+ prebuilt connectors" plus REST, GraphQL, Time Series and Rental ERP APIs, webhooks, and two-way ERP integrations. Named systems include NetSuite, Microsoft Dynamics 365, Acumatica, Baseplan, inspHire, MCS Rental Software and more (https://trackunit.com/irisx/integrations/).
- Named ERP connectors visible in the Trackunit Marketplace include RentalMan (Wynne Systems) and Integrated Rental (new.manager.trackunit.com marketplace URLs). Trackunit also has a formal, publicized partnership with Point of Rental (two-way API with Expert and Elite products) (https://trackunit.com/press/point-of-rental-partnership/).
- ISO 15143-3 (AEMP 2.0) is the standard interoperability layer: a common JSON/XML payload for position, hours, fuel and machine status across OEM portals and third-party systems; rental businesses use it for mixed-fleet visibility. Cat, Volvo CE, John Deere and others expose ISO 15143-3 APIs; Trackunit publishes its own explainer on the standard (https://trackunit.com/articles/benefits-from-iso-15143-4/).
- A concrete near-term ERP opening: SAP ETM (Equipment and Tools Management), long used by contractors for internal plant/equipment rental, is being sunset (usage rights ended 2025 in S/4HANA context, end of maintenance 2027 in ERP context per BearingPoint guidance cited by Wynne's RentalResult). Successors (BearingPoint ETM.next, Wynne RentalResult, STAEDEAN) all need telematics data, which favors a governed IrisX feed (https://rentalresult.com/sap-etm-sunset-a-critical-opportunity-to-consolidate-and-modernize-equipment-management/).
- The RMS market is consolidated into a few groups with global reach: Point of Rental (5,000+ business locations, customers in 80 countries), inspHire (owned by Kerridge Commercial Systems, ~10,000 users, offices UK/US/AU/NL), MCS (UK-based, multi-provider Telematics Hub including Trackunit), Wynne Systems (RentalMan, enterprise tier incl. large rental majors), Texada (North America + Australia, listed Trackunit partner), Baseplan (Australia-origin, 30+ years, named on Trackunit integrations page).
- Value logic for the role: every RMS/ERP integration that pulls live telematics (hours, location, status, faults) into rental contracts, billing, service scheduling and dispatch is a recurring driver of IrisX API calls, i.e. credit consumption. Two-way integrations (on-rent/off-rent status pushed back into Trackunit) deepen lock-in. (inference)

## Details

### ERP platforms

| Player | What it is / rental relevance | Telematics / Trackunit status | IrisX value angle |
|---|---|---|---|
| SAP S/4HANA (+ ETM) | Global enterprise ERP; ETM module served construction internal equipment rental (e.g. BAM Infra ran ETM with add-ons); leasing/rental also via Contract & Lease Mgmt and partner solutions (BearingPoint Lease&Rent on SAP BTP with telematics integration) | No public native Trackunit connector found; ETM sunset (rights ended 2025 in S/4HANA, maintenance to 2027) forces migrations | Position IrisX as the telematics data layer for ETM successors (ETM.next, RentalResult) and for large contractors re-platforming; note: the vacancy text mentions "SAP ECTR"; the construction-rental module is ETM, ECTR is SAP's engineering control center (inference on intent) |
| Oracle NetSuite | Cloud ERP popular with mid-market rental firms; rental handled via SuiteApps (NetScore, SuiteWorks, Sererra, KPI Rentegrate) | NetSuite named on Trackunit IrisX integrations page as a connector | Certified SuiteApp-level connector or partnership with the leading rental SuiteApps to make Trackunit the default telematics source |
| Microsoft Dynamics 365 F&SCM | Enterprise/mid-market ERP; strong rental ISV layer: STAEDEAN (ex To-Increase DynaRent), Sycor.Rental, HSO rental practice | D365 named on Trackunit integrations page; Sycor markets telematics-driven ERP processes (predictive maintenance, rental invoicing) | Partner with ISVs (STAEDEAN, Sycor, HSO) rather than Microsoft directly; embed IrisX feeds into their rental workflows |
| IFS | ERP/EAM vendor with construction and engineering focus (publishes EAM-for-construction content); European HQ | No public Trackunit integration found | EAM/service use cases: fault codes and usage hours feeding IFS maintenance objects (inference) |
| Infor (M3 / CloudSuite Equipment) | CloudSuite Equipment is a rental/dealer ERP built on M3 (rental orders, re-rent, rent-to-buy, parts, service); used by large equipment dealers (e.g. Zahid Tractor) | No public Trackunit connector found in this research | Dealer-heavy install base; telematics into service and rental billing; strong Nordics/Europe M3 heritage (inference on geography) |
| Acumatica | Cloud ERP for SMB/mid-market incl. construction edition | Named on Trackunit IrisX integrations page | Lightweight connector for smaller rental/contractor firms |

### Rental management systems (RMS)

| Player | Ownership / presence | Trackunit / telematics status | IrisX value angle |
|---|---|---|---|
| Point of Rental | US HQ; offices US, UK, AU, CA, ZA; 5,000+ business locations, 80 countries; also offers Hapn telematics bundle | Formal Trackunit partnership: two-way API with Expert and Elite (on/off-rent status, delivery, billing data, customer portal) | Expand from Expert/Elite to full product line; move partnership onto IrisX credits |
| Wynne Systems (RentalMan, RentalResult) | Volaris-era enterprise rental ERP; RentalMan used by very large rental companies; RentalResult targets contractors and ex-SAP-ETM users; also distributed via InTempo | Trackunit integration page on wynnesystems.com; RentalMan ERP connector listed in Trackunit Marketplace | Enterprise accounts with big mixed fleets; deepen from asset feed to workflow-level (service, dispatch) integration |
| inspHire | Owned by Kerridge Commercial Systems (acquired 2016); ~10,000 users; offices UK, US, AU, NL | Dedicated Trackunit integration (live location, status, contract info, 7-day usage, meter readings inside inspHire Asset Tracker); named on IrisX integrations page | KCS group-level deal could cover inspHire plus sister products (Current RMS); strong UK/EU hire market reach |
| MCS Rental Software | UK-based, independent; global sales incl. US, ZA | MCS Telematics Hub aggregates many providers (Trackunit, JCB LiveLink, Enigma, Teletrac, Eroad, etc.) | Risk: hub commoditizes telematics; opportunity: premium two-way IrisX connector with richer data than generic feeds (inference) |
| Texada | Canada (Mississauga) + Australia (Queensland); "Equipment Growth Platform" for dealers and rental; ISO 27001, SOC 2 | Trackunit listed as partner; integration into Texada Rental Management and Service Management | Dealer segment (sales+rental+service) fits Trackunit OEM/dealer strategy |
| Baseplan | Australia-origin equipment hire/rental ERP, 30+ years, US presence | Named on Trackunit IrisX integrations page | APAC rental market entry vehicle (inference) |
| Sycor (Sycor.Rental) | German-American Microsoft partner; Sycor.Rental on D365 F&SCM for SMB/mid-market rental in North America and DACH | Markets telematics-to-ERP process automation; no explicit Trackunit reference found | Co-sell with Microsoft ecosystem; telematics-triggered ERP workflows |
| Systematix | Named in the role scope alongside Sycor as a Dynamics rental route; not independently verified in this research (inference, verify) | Unknown | Same D365 ISV logic |
| Rouse Services | Part of RB Global; rental rate and utilization benchmarking from 400+ companies, $115B+ fleet value tracked; also appraisals; integrates with RMS vendors (Point of Rental, Fame, Quipli) | No public Trackunit integration found | Different shape of partner: data-for-benchmarking; IrisX utilization data could enrich Rouse benchmarks, Rouse insights could ship as an IrisX marketplace app; note pending antitrust scrutiny reporting around its benchmarking model (The Capitol Forum) |
| Integrated Rental | US rental software for heavy equipment dealers, ERP/DMS-connected | ERP connector listed in Trackunit Marketplace | Dealer rental ops; already a marketplace asset to grow |
| InTempo Software | US rental ERP provider; also provides RentalMan to part of the market | Not verified in this research | Mid-market US rental reach (inference) |

### Decision makers (role types, all inference from B2B software norms)

- RMS/ISV side: VP/Head of Product, Director of Partnerships/Alliances, CTO (connector roadmap and API commercial terms); at group level (KCS, Volaris/Wynne, RB Global) corporate development or portfolio GM.
- ERP vendor side: industry solution leads (construction/equipment verticals), ISV/technology partner program managers (SAP PartnerEdge, Microsoft AppSource, Oracle SuiteCloud), rarely core product.
- Joint customer side (rental companies, dealers): CIO/IT Director, Head of Fleet/Asset Management, COO; commercial sponsor is usually the fleet or operations owner who feels downtime and billing leakage.

## Sources

- https://trackunit.com/irisx/integrations/
- https://trackunit.com/marketplace/
- https://trackunit.com/press/point-of-rental-partnership/
- https://new.manager.trackunit.com/marketplace/@trackunit/erp-connector-rental-man
- https://new.manager.trackunit.com/marketplace/@trackunit/erp-connector-integrated-rental
- https://trackunit.com/articles/benefits-from-iso-15143-4/
- https://www.autopi.io/blog/what-is-aemp-telematics-standard/
- https://digital.cat.com/knowledge-hub/articles/iso-15143-3-aemp-20-api-developer-guide
- https://www.volvoce.com/europe/en/volvo-services/machine-data-api/
- https://developer.deere.com/dev-docs/aemp
- https://wynnesystems.com/integrations/trackunit/
- https://wynnesystems.com/rentalman/
- https://www.intemposoftware.com/blog/rentalman-software-provided-by-intempo
- https://rentalresult.com/sap-etm-sunset-a-critical-opportunity-to-consolidate-and-modernize-equipment-management/
- https://bearingpoint.services/etm/en/
- https://bearingpoint.services/lease-and-rent/en/
- https://www.emixa.com/cases/bam-infra-sap-s4hana
- https://www.insphire.com/page/integrations/trackunit
- https://www.rermag.com/news-analysis/international-news/article/20953149/kerridge-commercial-systems-acquires-uk-software-provider-insphire
- https://www.mcsrentalsoftware.com/us/rental-software-solutions/telematics/
- https://www.mcsrentalsoftware.com/za/resources/news-and-events/mcs-rental-software-expands-telematics-portfolio-with-industry-leading-integrations/
- https://www.point-of-rental.com/company/about-us/
- https://www.point-of-rental.com/press-release/trackunit-point-rental-partner-empower-rental-customers/
- https://texadasoftware.com/partners/trackunit/
- https://baseplan.com/heavy-equipment-hire-rental-software/
- https://staedean.com/rental/staedean-rental-management-microsoft-dynamics-365
- https://sycor-group.com/us-en/microsoft/solutions/dynamics-365-industry/rental.html
- https://sycor-group.com/us-en/microsoft/blog/microsoft/implement-and-manage-telematics-for-equipment-rental.html
- https://www.infor.com/products/cloudsuite-equipment
- https://www.infor.com/news/zahid-tractor-infor-m3-equipment
- https://blog.ifs.com/top-7-eam-platforms-for-construction-and-engineering-in-2026/
- https://www.netsuite.com/portal/resource/articles/erp/from-mobility-to-asset-tracking-here-are-4-ways-netsuite-helps-construction-equipment-rental-companies.shtml
- https://kpi.co/equipment-rental-erp-rentegrate-netsuite
- https://integratedrental.com/
- https://www.rouseservices.com/solutions/rental-insights/
- https://rbglobal.com/insights/rouse-rental-insights/
- https://thecapitolforum.com/rb-globals-rouse-services-could-face-antitrust-scrutiny-over-information-sharing/
- https://loxam.com/en/
