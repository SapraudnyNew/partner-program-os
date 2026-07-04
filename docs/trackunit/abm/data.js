// Single data source for control-tower, signal-radar, relationship-heatmap. Compiled from partner-mapping/accounts/*.md. Public data, July 2026.

const ABM_DATA = {
  meta: {
    asOf: "July 2026",
    source: "Public LinkedIn and web data, account plans first pass",
    note: "Relationship stages are starting-point estimates, not CRM data. Credit figures are assumptions."
  },

  accounts: [
    {
      id: "procore",
      name: "Procore Technologies",
      shortName: "Procore",
      category: "ConTech",
      score: 4.8,
      disposition: "Pursue",
      layerMix: { to: 2, with: 2, through: 3 },
      creditDriver: "Daily mixed-fleet pulls by project teams (assumption)",
      entryPoint: "Tony Harbour",
      funnelStage: "First contact planned"
    },
    {
      id: "bearingpoint-etm-next",
      name: "BearingPoint (ETM.next)",
      shortName: "BearingPoint",
      category: "ERP",
      score: 4.3,
      disposition: "Pursue",
      layerMix: { to: 1, with: 2, through: 3 },
      creditDriver: "Fleet-wide meter and contract sync per migration (assumption)",
      entryPoint: "Ernest de Weert",
      funnelStage: "First contact planned"
    },
    {
      id: "wynne-rentalresult",
      name: "Wynne Systems (RentalMan / RentalResult)",
      shortName: "Wynne",
      category: "Rental",
      score: 4.3,
      disposition: "Deepen / Pursue",
      layerMix: { to: 2, with: 2, through: 3 },
      creditDriver: "Two-way contract sync and utilization pulls across RentalMan tenants, plus fleet-wide sync per SAP ETM migration via RentalResult (assumption)",
      entryPoint: "Kenneth Kimura",
      funnelStage: "Active partner"
    },
    {
      id: "point-of-rental",
      name: "Point of Rental Software",
      shortName: "Point of Rental",
      category: "Rental",
      score: 4.5,
      disposition: "Deepen",
      layerMix: { to: 1, with: 3, through: 3 },
      creditDriver: "Two-way contract, billing and meter sync (assumption)",
      entryPoint: "Cal Grant",
      funnelStage: "Active partner"
    },
    {
      id: "microsoft",
      name: "Microsoft",
      shortName: "Microsoft",
      category: "ERP + AI",
      score: 4.5,
      disposition: "Pursue / Deepen",
      layerMix: { to: 1, with: 3, through: 3 },
      creditDriver: "ERP transactions plus per-query agent calls via MCP (assumption)",
      entryPoint: "Kristian Ridley Schou",
      funnelStage: "First contact planned"
    },
    {
      id: "palantir",
      name: "Palantir Technologies",
      shortName: "Palantir",
      category: "AI / ops platform",
      score: 4.2,
      disposition: "Monitor, upgrade on trigger",
      layerMix: { to: 2, with: 2, through: 1 },
      creditDriver: "Continuous fleet sync into ontology objects (assumption)",
      entryPoint: "Tom Buller",
      funnelStage: "Research"
    }
  ],

  people: [
    // Procore
    {
      name: "Samira Jabbar",
      title: "VP Partnerships",
      account: "procore",
      location: "Austin, Texas, United States",
      linkedin: "https://www.linkedin.com/in/ACwAAABi7t8ByRO3fQ8KpXoyPURGXT5nQkpc6QI",
      owns: "Most senior person in the scan with a pure partnerships title; likely owner or executive sponsor of the technology partner motion (inference); 2 months in role, still forming her agenda",
      emea: false,
      role: "partnerships",
      stage: "cold",
      confirmed: false
    },
    {
      name: "Meg Baldini",
      title: "VP, Corporate Development and Partnerships",
      account: "procore",
      location: "Austin, Texas, United States",
      linkedin: "https://www.linkedin.com/in/meganbaldini/",
      owns: "Corporate development plus partnerships in one seat; the deal-structure counterpart if the connector grows into a strategic partnership like United Rentals",
      emea: false,
      role: "partnerships",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Brittany Schramm",
      title: "Senior Director, Cloud Partnerships & Business Development",
      account: "procore",
      location: "San Diego, California, United States",
      linkedin: "https://www.linkedin.com/in/brittschramm/",
      owns: "Cloud partnerships and business development, currently driving the AWS partnership; the operating layer where a new technology alliance gets qualified and staffed (inference)",
      emea: false,
      role: "partnerships",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Tony Harbour",
      title: "Director of Partnerships, EMEA",
      account: "procore",
      location: "City Of London, England, United Kingdom",
      linkedin: "https://www.linkedin.com/in/tony-harbour-2a51bb23/",
      owns: "Owns partnerships for the region where Trackunit is headquartered and where Procore is expanding; the natural regional sponsor",
      emea: true,
      role: "partnerships",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Lee Miles",
      title: "SVP General Manager EMEA",
      account: "procore",
      location: "United Kingdom",
      linkedin: "https://www.linkedin.com/in/lemiles/",
      owns: "Runs the EMEA business; influence target for regional executive sponsorship once the partnerships track is live",
      emea: true,
      role: "leadership",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Raechele Kuskie",
      title: "Senior Product Manager, Platform Services",
      account: "procore",
      location: "Austin, Texas, United States",
      linkedin: "https://www.linkedin.com/in/raechele/",
      owns: "Product owner in Platform Services, the layer the developer platform and marketplace integrations run on (inference); the technical counterpart for connector scoping",
      emea: false,
      role: "product",
      stage: "cold",
      confirmed: false
    },
    {
      name: "Stephen Perkins",
      title: "Product Design Lead, Resource Management",
      account: "procore",
      location: "United States",
      linkedin: "https://www.linkedin.com/in/perkinsstephen/",
      owns: "Closest named person to the Resource Management product surface where Equipment Telematics data lands; a route to the Equipment tool product owner",
      emea: false,
      role: "product",
      stage: "cold",
      confirmed: false
    },

    // BearingPoint (ETM.next)
    {
      name: "Donald Wachs",
      title: "Member of Management Committee - Products",
      account: "bearingpoint-etm-next",
      location: "Berlin Metropolitan Area",
      linkedin: "https://www.linkedin.com/in/donald-wachs-b827608b/",
      owns: "Partner and global leader of the BearingPoint Products unit, the product business ETM.next sits in (confirmed via bearingpoint.com people page and The Org); the executive sponsor any partnership needs",
      emea: true,
      role: "leadership",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Frank Zeidler",
      title: "Director of Product Management",
      account: "bearingpoint-etm-next",
      location: "Greater Hamburg Area",
      linkedin: "https://www.linkedin.com/in/frank-zeidler-a0446215/",
      owns: "Director Product Management in the BearingPoint Products unit; publicly listed on the Assets & Funding Management product team, not ETM.next (corrected after verification); a products-unit route rather than a confirmed ETM.next roadmap owner",
      emea: true,
      role: "product",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Ernest de Weert",
      title: "Business Development Sr Manager",
      account: "bearingpoint-etm-next",
      location: "Eindhoven, North Brabant, Netherlands",
      linkedin: "https://www.linkedin.com/in/ernestdeweert/",
      owns: "BD in the BearingPoint Products unit; publicly tied to the Lease & Rent product, a sibling of ETM.next, not to ETM.next itself (corrected after verification); still the closest partnerships-facing route in the scan",
      emea: true,
      role: "partnerships",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Dr. Uta Deppe",
      title: "Business Development Manager | Expert for Salesforce & SAP Platform Services",
      account: "bearingpoint-etm-next",
      location: "Hamburg, Hamburg, Germany",
      linkedin: "https://www.linkedin.com/in/dr-uta-deppe-978b98169/",
      owns: "BD Manager in BearingPoint Products (confirmed via The Org); named contact for Salesforce Platform Services; a route into how BearingPoint packages third-party services around its products (inference)",
      emea: true,
      role: "partnerships",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Helmut Ritter",
      title: "Partner, Head of SAP Austria",
      account: "bearingpoint-etm-next",
      location: "Vienna, Vienna, Austria",
      linkedin: "https://www.linkedin.com/in/helmut-ritter/",
      owns: "Partner and Head of SAP Austria (confirmed via bearingpoint.com people page); leads SAP enterprise transformation in the DACH region, where the legacy SAP ETM install base is historically concentrated; his teams write the migration blueprints (inference)",
      emea: true,
      role: "field",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Nicu Zaharia",
      title: "Partner | SAP Practice Lead BearingPoint Romania, Czech Republic, Portugal, India",
      account: "bearingpoint-etm-next",
      location: "Bucharest, Bucharest, Romania",
      linkedin: "https://www.linkedin.com/in/nicuzaharia/",
      owns: "Promoted to Partner July 2025, BearingPoint's second Partner in Romania (confirmed via press release); leads the SAP practice across the nearshore delivery hubs, including Romania, which also hosts product cloud support; delivery capacity for migrations runs through him (inference)",
      emea: true,
      role: "field",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Roope Kreula",
      title: "Director, Head of SAP Finland",
      account: "bearingpoint-etm-next",
      location: "Helsinki, Uusimaa, Finland",
      linkedin: "https://www.linkedin.com/in/roope-kreula-8683b",
      owns: "Heads SAP in Finland (confirmed via bearingpoint.com Finland pages); the Nordic SAP practice is the natural bridge to Trackunit's Nordic home base and Nordic contractor accounts (inference)",
      emea: true,
      role: "field",
      stage: "cold",
      confirmed: true
    },

    // Wynne Systems (RentalMan / RentalResult)
    {
      name: "Clare McCormick",
      title: "General Manager",
      account: "wynne-rentalresult",
      location: "Greater Phoenix Area",
      linkedin: "https://www.linkedin.com/in/clare-mccormick-5901b99b",
      owns: "Runs the business unit; final commercial sign-off on any partnership economics in a Volaris-style P&L (inference)",
      emea: false,
      role: "leadership",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Kenneth Kimura",
      title: "Director of Product Development",
      account: "wynne-rentalresult",
      location: "Round Rock, Texas, United States",
      linkedin: "https://www.linkedin.com/in/kenneth-kimura-b897bb80",
      owns: "Director-level product owner; the roadmap decision on upgrading the RentalMan connector to an IrisX-native app runs through him (inference)",
      emea: false,
      role: "product",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Steve Kistler",
      title: "Director Software Development",
      account: "wynne-rentalresult",
      location: "Glendale, Arizona, United States",
      linkedin: "https://www.linkedin.com/in/steve-kistler-b972828",
      owns: "Engineering leadership; scopes and staffs the actual connector build against IrisX APIs",
      emea: false,
      role: "product",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Tsvety Petrova",
      title: "Product Manager",
      account: "wynne-rentalresult",
      location: "Edinburgh, Scotland, United Kingdom",
      linkedin: "https://www.linkedin.com/in/tsvety-petrova-8aa27569",
      owns: "EMEA-based product manager; closest longlist match to the RentalResult and SAP ETM migration motion given the product's UK roots (inference); employment at Wynne Systems Edinburgh confirmed, title from LinkedIn scan only",
      emea: true,
      role: "product",
      stage: "cold",
      confirmed: false
    },
    {
      name: "Kevin Shaw",
      title: "Technology Manager",
      account: "wynne-rentalresult",
      location: "Elland, England, United Kingdom",
      linkedin: "https://www.linkedin.com/in/kevin-shaw-4999582a",
      owns: "Technology lead at Wynne Systems (UK) Ltd; the technical counterpart for EMEA deployments and integration questions",
      emea: true,
      role: "product",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Ashish Udeshi",
      title: "Senior Product Manager",
      account: "wynne-rentalresult",
      location: "Placentia, California, United States",
      linkedin: "https://www.linkedin.com/in/ashish-udeshi",
      owns: "Senior PM near Irvine HQ; likely hands-on owner of specific RentalMan integration surfaces (inference)",
      emea: false,
      role: "product",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Steven Tripp",
      title: "Marketing Director",
      account: "wynne-rentalresult",
      location: "Washington DC-Baltimore Area",
      linkedin: "https://www.linkedin.com/in/steventripp",
      owns: "Owns co-marketing and the Wynne User Summit surface, the October 2026 activation milestone",
      emea: false,
      role: "field",
      stage: "cold",
      confirmed: true
    },

    // Point of Rental Software
    {
      name: "Cal Grant",
      title: "Vice President, Payments & Ecosystem",
      account: "point-of-rental",
      location: "Denver Metropolitan Area",
      linkedin: "https://www.linkedin.com/in/calgrant/",
      owns: "Closest title to a partnerships owner: \"Ecosystem\" covers third-party connections, the natural counterpart for a marketplace-grade connector and joint GTM",
      emea: false,
      role: "partnerships",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Emad Georgy",
      title: "Chief Technology Officer",
      account: "point-of-rental",
      location: "Los Angeles Metropolitan Area",
      linkedin: "https://www.linkedin.com/in/emad-georgy/",
      owns: "First-ever CTO (Jan 2025), owns the technical architecture the two-way API and any deeper IrisX feed run through; AI background aligns with the data-platform pivot",
      emea: false,
      role: "leadership",
      stage: "aware",
      confirmed: true
    },
    {
      name: "Collin Pike",
      title: "Vice President, Cloud & Innovation",
      account: "point-of-rental",
      location: "Dallas-Fort Worth Metroplex",
      linkedin: "https://www.linkedin.com/in/pikecollin/",
      owns: "Cloud and platform ownership, named alongside the CEO in the Rental Intelligence Suite launch; the suite consumes exactly the fleet and asset performance data IrisX can supply",
      emea: false,
      role: "product",
      stage: "cold",
      confirmed: true
    },
    {
      name: "James Morley",
      title: "Senior Vice President, Global Product Management",
      account: "point-of-rental",
      location: "Houston, Texas, United States",
      linkedin: "https://www.linkedin.com/in/ACwAAAFq7loBR-GlFHc7Kid8SuNa-Q22Japr3x0",
      owns: "Top of the product organization; decides whether the connector extends beyond Expert and Elite across the product line",
      emea: false,
      role: "product",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Matthew Gaffin",
      title: "Head of AI",
      account: "point-of-rental",
      location: "Irving, Texas, United States",
      linkedin: "https://www.linkedin.com/in/mattgaffin",
      owns: "Owns the AI agenda the Rental Intelligence Suite sits on; telematics-grade machine data via IrisX is a direct input to those models",
      emea: false,
      role: "product",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Mark Goodrum",
      title: "Managing Director, EMEA",
      account: "point-of-rental",
      location: "Reading, England, United Kingdom",
      linkedin: "https://www.linkedin.com/in/mark-goodrum-6a834614",
      owns: "Runs the UK business where the Syrinx 365 ERP Connector is already live in the Trackunit Marketplace; the EMEA path into the account",
      emea: true,
      role: "leadership",
      stage: "aware",
      confirmed: true
    },
    {
      name: "Wayne Harris",
      title: "CEO",
      account: "point-of-rental",
      location: "Grand Prairie, Texas, United States",
      linkedin: "https://www.linkedin.com/in/wayne-harris-por/",
      owns: "Personally quoted in the Jan 2025 partnership announcement; executive sponsor for any expansion of the relationship",
      emea: false,
      role: "leadership",
      stage: "engaged",
      confirmed: true
    },

    // Microsoft
    {
      name: "Kelly Curran",
      title: "Senior Director ISV Strategic Partnerships",
      account: "microsoft",
      location: "Eagle, Idaho, United States",
      linkedin: "https://www.linkedin.com/in/kellycurran/",
      owns: "Senior owner of strategic ISV partnerships, the program lane Trackunit needs for ISV Success and App Accelerate",
      emea: false,
      role: "partnerships",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Carol S. Scott",
      title: "Senior Director, EMEA, Software & Development Platforms- Sales & Customer Success for Partners",
      account: "microsoft",
      location: "London, England, United Kingdom",
      linkedin: "https://www.linkedin.com/in/carolsscott/",
      owns: "Senior EMEA owner for software-company partner sales and success, the regional escalation point for a Danish ISV",
      emea: true,
      role: "partnerships",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Kristian Ridley Schou",
      title: "Sr. Technology Strategist EMEA | ISV Partnerships",
      account: "microsoft",
      location: "Roskilde, Region Zealand, Denmark",
      linkedin: "https://www.linkedin.com/in/kristianridley/",
      owns: "EMEA ISV technology strategist sitting in Denmark, Trackunit's home market; natural first technical counterpart for MCP and marketplace architecture",
      emea: true,
      role: "partnerships",
      stage: "cold",
      confirmed: false
    },
    {
      name: "Zehra SyedaSarwat",
      title: "Senior Director Global ISV Partnerships, Data & AI",
      account: "microsoft",
      location: "Libertyville, Illinois, United States",
      linkedin: "https://www.linkedin.com/in/zehra-syedasarwat-7127a211/",
      owns: "Global ISV partnerships for Data & AI, the specialization that covers an MCP-based agent data play",
      emea: false,
      role: "partnerships",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Bradley Davis",
      title: "Director, Business Planning (Commercial Portfolio & Marketplace Strategy )",
      account: "microsoft",
      location: "Redmond, Washington, United States",
      linkedin: "https://www.linkedin.com/in/bradley-davis-24241894/",
      owns: "Marketplace strategy planning; relevant once a transactable, MACC-eligible listing and Copilot Credits billing are on the table",
      emea: false,
      role: "partnerships",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Dina Habib OMara",
      title: "Global, Industry Partner Strategy, GTM Co-Sell Lead",
      account: "microsoft",
      location: "Greater Seattle Area",
      linkedin: "https://www.linkedin.com/in/ACwAAAGsL8oBjwQmdDJRPLJ7yAQUOTY5583_JDE",
      owns: "Global industry partner co-sell lead, the bridge from an ISV listing to Manufacturing & Mobility co-sell motions",
      emea: false,
      role: "partnerships",
      stage: "cold",
      confirmed: false
    },
    {
      name: "Reetu Chopra",
      title: "Senior Product Manager - Dynamics 365, AI ERP",
      account: "microsoft",
      location: "India",
      linkedin: "https://www.linkedin.com/in/ACwAAANSPiYBK21Ced3vZulE2c2q4ctwyBA6wtU",
      owns: "Product side of D365 AI ERP, where the 2026 rental-business-model features land; useful for validating the ERP connector shape",
      emea: false,
      role: "product",
      stage: "cold",
      confirmed: false
    },

    // Palantir Technologies
    {
      name: "Noah Diskin Kline",
      title: "VP, Commercial Business Development",
      account: "palantir",
      location: "New York, New York, United States",
      linkedin: "https://www.linkedin.com/in/noahdiskin/",
      owns: "Most senior commercial BD title in the scan; the level that can sponsor an ISV-style data partnership",
      emea: false,
      role: "partnerships",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Tom Buller",
      title: "Commercial Business Development EMEA",
      account: "palantir",
      location: "London, England, United Kingdom",
      linkedin: "https://www.linkedin.com/in/tom-buller/",
      owns: "International commercial BD out of London; the closest thing to an EMEA ecosystem door in the scan",
      emea: true,
      role: "partnerships",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Zachary Zlotnick",
      title: "Global Business Development - FedStart",
      account: "palantir",
      location: "Los Angeles, California, United States",
      linkedin: "https://www.linkedin.com/in/zacharyzlotnick/",
      owns: "FedStart is Palantir's only formal ISV motion; he sits where third-party software meets Palantir GTM",
      emea: false,
      role: "partnerships",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Martijn Koerts",
      title: "Head of Sales and Business Development Benelux",
      account: "palantir",
      location: "Amsterdam, North Holland, Netherlands",
      linkedin: "https://www.linkedin.com/in/martijn-koerts-18980b5/",
      owns: "Named country ownership in Benelux, a dense construction and equipment rental market; public records show a government-sector focus",
      emea: true,
      role: "field",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Jørn Henrik Levy Rasmussen",
      title: "Sales Executive",
      account: "palantir",
      location: "Copenhagen, Capital Region of Denmark, Denmark",
      linkedin: "https://www.linkedin.com/in/jorn-henriklevyrasmussen/",
      owns: "Senior presence in Trackunit's home market; influence mapping for a Nordic-anchored conversation",
      emea: true,
      role: "field",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Thor Snedker Brandt",
      title: "Business Development",
      account: "palantir",
      location: "Copenhagen, Capital Region of Denmark, Denmark",
      linkedin: "https://www.linkedin.com/in/thorsnedkerbrandt/",
      owns: "Working-level BD in Copenhagen, joined about 3 months ago; the practical local door",
      emea: true,
      role: "partnerships",
      stage: "cold",
      confirmed: true
    },
    {
      name: "Kaan Korkmaz",
      title: "Deployment Strategist",
      account: "palantir",
      location: "Munich, Bavaria, Germany",
      linkedin: "https://www.linkedin.com/in/ACwAAAzxW9gB0rjkySWeEr5gFu0CbQgAhMnp7kk",
      owns: "Industrials deployment in DACH; deployment strategists run the accounts where an IrisX feed would actually land",
      emea: true,
      role: "field",
      stage: "cold",
      confirmed: false
    }
  ],

  signals: [
    // Procore
    {
      date: "2026-02",
      account: "procore",
      type: "partnership",
      title: "United Rentals strategic partnership",
      detail: "Procore's first telematics-centered partnership (Feb 26, 2026): rental equipment data and telematics sync directly into Resource Management with AI-driven recommendations. Proof that Procore takes third-party fleet data natively, not just OEM feeds."
    },
    {
      date: "2026-01",
      account: "procore",
      type: "ma",
      title: "Datagrid acquisition completed",
      detail: "Agentic AI platform that connects data across ERPs, document repositories and project platforms (Jan 20, 2026); Datagrid CEO Thiago da Costa now leads AI and data strategy at Procore. Equipment telematics is an obvious next data silo for agents to consume (inference)."
    },
    {
      date: "2025",
      account: "procore",
      type: "product",
      title: "Procore Helix and Agent Builder launched at Groundbreak 2025",
      detail: "Attendees built 1,000+ custom agents at the event. Agents built on equipment data need a mixed-fleet source behind them (inference)."
    },
    {
      date: "2025-06",
      account: "procore",
      type: "partnership",
      title: "Tiered Technology Partner Program announced",
      detail: "Announced June 16, 2025, rewarding partners on joint customer value with a globally consistent structure, owned under Ryan Butler, SVP Corporate Strategy and Operations. A formal on-ramp now exists."
    },
    {
      date: "2025",
      account: "procore",
      type: "hiring",
      title: "EMEA expansion",
      detail: "2025-2026: new Dublin hub with hundreds of planned hires, UK Data Zone live, EU Data Zone planned for fall 2026. Procore is building the region where Trackunit is strongest."
    },

    // BearingPoint (ETM.next)
    {
      date: "2025",
      account: "bearingpoint-etm-next",
      type: "product",
      title: "SAP ETM usage rights ended in S/4HANA compatibility mode",
      detail: "Usage rights for legacy SAP Equipment and Tools Management ended in 2025; maintenance in the ERP context ends 2027. Every remaining SAP ETM contractor must re-platform, and 2026-2027 is the peak migration window (inference)."
    },
    {
      date: "2025-04",
      account: "bearingpoint-etm-next",
      type: "product",
      title: "ETM.next exhibited at bauma in Munich",
      detail: "BearingPoint exhibited ETM.next at bauma April 7-13, 2025 (Hall A2 Booth N), after earlier presence at bauma China. Trackunit exhibits on the same event circuit (inference: shared floor, shared audience)."
    },
    {
      date: "2025",
      account: "bearingpoint-etm-next",
      type: "product",
      title: "Active ETM.next demand generation and SACDE win",
      detail: "2025-2026: active demand generation against the 2027 deadline, including the four-part blog series \"From isolated tools to ETM.next\" and an insight arguing that rebuilding custom ECC/ETM code in S/4HANA is a costly mistake. Recent customer win: SACDE, a leading Argentine contractor, went live ahead of its S/4HANA go-live."
    },
    {
      date: "2026-03",
      account: "bearingpoint-etm-next",
      type: "financial",
      title: "FY2025 results and North America JV with ABeam",
      detail: "Announced March 5, 2026: third consecutive year above EUR 1 billion, 1,000+ new hires including 16 new Partners, and a new North America JV with ABeam (\"BearingPoint North America\"), matched by Chicago-based ETM.next implementation hiring."
    },

    // Wynne Systems (RentalMan / RentalResult)
    {
      date: "2026-02",
      account: "wynne-rentalresult",
      type: "product",
      title: "SAP ETM sunset campaign content refresh",
      detail: "Wynne runs an active SAP ETM sunset campaign positioning RentalResult as the purpose-built replacement. SAP ETM usage rights in S/4HANA compatibility mode ended in 2025 and maintenance ends in 2027. The campaign page now redirects to rentalresult.com, suggesting RentalResult is being built out as a distinct contractor-facing brand (inference)."
    },
    {
      date: "2025-01",
      account: "wynne-rentalresult",
      type: "partnership",
      title: "Foresight Intelligence named preferred telematics provider for RentalMan",
      detail: "Not stated as exclusive, but a competitive wedge inside Wynne's telematics stack and a reason to move now rather than later."
    },
    {
      date: "2025",
      account: "wynne-rentalresult",
      type: "product",
      title: "Active product cadence across RentalMan and RentalResult",
      detail: "Q3 2025 RentalMan release shipped IntelliSource, Logistics, Service, RapidCount and MobileLink updates; a Logistics Solution comes to RentalResult in spring 2026; Re-Rentals Direct now auto-creates RentalMan pickups from RentalResult requisitions, wiring contractors directly to rental suppliers."
    },
    {
      date: "2026-10",
      account: "wynne-rentalresult",
      type: "partnership",
      title: "Wynne User Summit in Charlotte, NC",
      detail: "October 5-7, 2026. A concrete co-marketing and field-engagement milestone within the first two quarters of the role."
    },
    {
      date: "2026-07",
      account: "wynne-rentalresult",
      type: "hiring",
      title: "Hiring board shows no partnerships or integrations roles",
      detail: "July 2026: only three open roles, none in partnerships, platform or integrations. Integrations sit with the existing product org, so the window to shape the connector roadmap runs through product management and the CRO, not a partner team (inference)."
    },

    // Point of Rental Software
    {
      date: "2025-01",
      account: "point-of-rental",
      type: "partnership",
      title: "Long-term Trackunit partnership announced",
      detail: "A bidirectional API between Point of Rental Expert and Elite and Trackunit Manager plus the Trackunit Go app, syncing on-rent and off-rent status, delivery events and billing data. CEO Wayne Harris framed it as taking IoT to the next level with Trackunit."
    },
    {
      date: "2025-01",
      account: "point-of-rental",
      type: "hiring",
      title: "First-ever CTO hired, Emad Georgy",
      detail: "CTO with an AI background, following the company's first CFO in August 2024. Inference from the web digest: PE-backed professionalization of the executive layer and a pivot from record-keeping software toward an AI and data platform, which raises the value of machine-data feeds like Trackunit's."
    },
    {
      date: "2026-03",
      account: "point-of-rental",
      type: "ma",
      title: "Acquired The Owl, a rental data insights platform",
      detail: "March 1, 2026, its most recent deal per PitchBook, with the analytics folded into the Rental Intelligence Suite."
    },
    {
      date: "2026-03",
      account: "point-of-rental",
      type: "product",
      title: "Rental Intelligence Suite launched at the ARA Show",
      detail: "March 2, 2026, Orlando: described as the first agentic intelligence layer built for rental operations with natural-language dashboards, utilization and ROI analytics, cross-fleet benchmarks, nightly AI insights and background agents, trained on de-identified data from thousands of rental companies. An AI-powered Intelligent Phone Agent launched the same day."
    },

    // Microsoft
    {
      date: "2025-09",
      account: "microsoft",
      type: "product",
      title: "Azure Marketplace and AppSource merged into a single Microsoft Marketplace",
      detail: "One Partner Center listing flow and 6M+ monthly unique visitors; a dedicated AI Apps category launched in 2026."
    },
    {
      date: "2025-11",
      account: "microsoft",
      type: "partnership",
      title: "App Accelerate announced at Ignite",
      detail: "Launching 2026: unifies ISV Success, Marketplace Rewards and co-sell resources into one pathway, and early co-sell access is no longer gated only by the $100K revenue threshold. Lower barriers for a first-time Microsoft ISV like Trackunit."
    },
    {
      date: "2026-04",
      account: "microsoft",
      type: "product",
      title: "Dynamics 365 release wave 1 is explicitly agentic, adds rental business models",
      detail: "April to September 2026: D365 Finance adds support for rental-based business models, tracking rental assets, revenue and related processes, landing directly on Trackunit's rental-company customer base (inference on the fit, fact on the release plan). Field Service gets a Scheduling Operations Agent and deeper ties to Finance & Operations."
    },
    {
      date: "2025-10",
      account: "microsoft",
      type: "product",
      title: "Legacy Field Service IoT integrations deprecated",
      detail: "After October 30, 2025: several legacy Field Service IoT integrations were deprecated, while Field Service continues to support custom IoT providers. The deprecations create whitespace for a construction telematics platform to become the equipment-data provider into Field Service work orders (inference)."
    },
    {
      date: "2026",
      account: "microsoft",
      type: "product",
      title: "MCP support GA in Copilot Studio; Copilot monetization shifts to consumption",
      detail: "Through 2026: MCP support went GA in Copilot Studio and for declarative agents in M365 Copilot, and Copilot monetization shifted to consumption via Copilot Credits, with ISV agents distributed through the Agent Store and published via Partner Center."
    },

    // Palantir Technologies
    {
      date: "2026-05",
      account: "palantir",
      type: "partnership",
      title: "Cavanagh extends Foundry partnership to 11 years, creates Cavtera",
      detail: "Late May 2026: Thomas Cavanagh Construction extended its Foundry partnership through December 31, 2035; PLTR stock rose about 17% on the news. Cavanagh also created a subsidiary, Cavtera, to commercialize its Foundry-built construction apps and support Palantir implementations across construction, a customer turning into a channel."
    },
    {
      date: "2026-06",
      account: "palantir",
      type: "partnership",
      title: "McCarthy Building Companies signs multi-year partnership",
      detail: "A major US general contractor signed a multi-year, multi-million dollar partnership; its AI-native field system \"Pulse\" was demoed at AIPCon 10. Construction is getting a second flagship."
    },
    {
      date: "2026-06",
      account: "palantir",
      type: "partnership",
      title: "Foundry available on Google Cloud Marketplace",
      detail: "Two-way BigQuery integrations and Gemini-AIP connectivity, part of a broader ecosystem formalization alongside the Accenture Palantir Business Group and the Databricks product partnership."
    },
    {
      date: "2026-02",
      account: "palantir",
      type: "product",
      title: "DevCon2 introduces Embedded Ontologies for offline edge devices",
      detail: "Explicitly citing mining and construction sites with unreliable networks, a direct fit for off-highway equipment telemetry."
    },
    {
      date: "2026",
      account: "palantir",
      type: "financial",
      title: "Q1 2026 results: revenue up 85%, US commercial up 133%",
      detail: "Trailing 12-month US commercial TCV bookings of $4.7B, up 115%. The commercial engine that would carry a construction data partnership is the fastest-growing part of the company."
    }
  ]
};
