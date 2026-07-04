# Procore showcase: partner ABM at full depth

Every partner account in the [landscape](../partner-mapping/index.html) gets a score. Procore got the highest one, 4.8, disposition Pursue, and this page shows why it also gets the deepest treatment. Partner ABM is not one motion. It is three layers that share an account: win the partner itself (ABM to partner), sell jointly into shared customers (ABM with partner), and use the partner's marketplace as a channel (ABM through partner). Procore is the one account on the map where all three layers apply at full strength, so it is the showcase.

## Why Procore is the showcase

Three reasons. First, the score: Procore combines a $1.499B to $1.53B FY2026 revenue guide, 1.3M+ users, a formal tiered Technology Partner Program launched June 2025, and an EMEA expansion into the region where Trackunit is strongest. Second, the whitespace: Procore's Equipment Telematics feature is an open API that today ingests Caterpillar, John Deere, Samsara, and United Rentals, with no Trackunit connection listed. IrisX normalizes 100+ OEM feeds, which is exactly what a per-OEM source list cannot give a contractor running a mixed fleet. Third, the layer test: Procore has a named buying committee to win, a large base of contractors who plausibly also run Trackunit hardware, and a marketplace of roughly 539 apps that works as a distribution channel. One account, three ABM layers, one root metric: IrisX credit consumption.

The timing case is unusually dense. In February 2026 Procore announced its first telematics-centered strategic partnership, with United Rentals rental-fleet data syncing into Resource Management, proof that Procore takes third-party fleet data natively. In January 2026 it completed the Datagrid acquisition and put Datagrid's CEO in charge of AI and data strategy, and at Groundbreak 2025 it launched Helix and Agent Builder, with attendees building 1,000+ custom agents at the event. Agents built on equipment data need a mixed-fleet source behind them (inference). Add the June 2025 tiered Technology Partner Program as a formal on-ramp and the Dublin-anchored EMEA expansion, and the window is open now, not eventually.

Full account context lives in the [Procore account plan](../partner-mapping/accounts/procore.html) and the [first five dossier](../partner-mapping/first-five.html); the execution timeline is in the [first five plan](../execution/first-five-plan.html).

## Layer 1: ABM to partner, winning Procore

### The buying committee

The org map in the account plan names seven people from a 68-profile employee scan. Here they are as a buying committee, each with a role in the decision and a thread owner on our side. Roles are working hypotheses from public data, marked where the account plan marks them as inference.

| Name | Title | LinkedIn | Role in the decision | Thread owner |
|---|---|---|---|---|
| Samira Jabbar | VP Partnerships | https://www.linkedin.com/in/ACwAAABi7t8ByRO3fQ8KpXoyPURGXT5nQkpc6QI | Economic buyer for the partner motion (inference); 2 months in role and still forming her agenda, so a well-prepared inbound is an early win for her | Me |
| Tony Harbour | Director of Partnerships, EMEA | https://www.linkedin.com/in/tony-harbour-2a51bb23/ | Champion candidate and first entry point; a Denmark-headquartered partner is a regional win he can sponsor | Me |
| Brittany Schramm | Senior Director, Cloud Partnerships & Business Development | https://www.linkedin.com/in/brittschramm/ | Operating layer where a new alliance gets qualified and staffed (inference); blocker risk if the connector stalls in qualification | Me |
| Meg Baldini | VP, Corporate Development and Partnerships | https://www.linkedin.com/in/meganbaldini/ | Deal-structure counterpart if the connector grows into a strategic partnership like United Rentals | Exec sponsor |
| Lee Miles | SVP General Manager EMEA | https://www.linkedin.com/in/lemiles/ | Regional executive influence target once the partnerships track is live | Exec sponsor |
| Raechele Kuskie | Senior Product Manager, Platform Services | https://www.linkedin.com/in/raechele/ | Technical counterpart for connector scoping against the developer platform (inference) | SE |
| Stephen Perkins | Product Design Lead, Resource Management | https://www.linkedin.com/in/perkinsstephen/ | Closest named route to the Equipment tool product surface; blocker risk if product deprioritizes new telematics sources | SE |

Two names the scan could not produce: the Equipment Telematics product manager and the App Marketplace program owner. The cadence below is built to extract both from the conversations themselves.

### The 12-week cadence

Grounded in the account plan's entry path and first 30 days. Every step has an owner and an exit criterion, because a cadence without exits is a calendar, not a plan.

| Weeks | Action | Owner | Exit criterion |
|---|---|---|---|
| 1 to 2 | Research: capture Procore's telematics partner requirements from public developer docs and what the four existing sources had to provide; ask Trackunit sales for mutual customers running both platforms | Me | Requirements documented; named mutual-customer list in hand |
| 3 to 4 | Warm intro to Tony Harbour, opened with the mutual-customer evidence; SE starts the demo feed against the Equipment Telematics open API using IrisX GraphQL | Me, SE | Harbour meeting booked; demo build underway in the Procore Developer Sandbox |
| 5 to 6 | Harbour meeting held; in the same fortnight, formal intake into the tiered Technology Partner Program toward Samira Jabbar's organization | Me | Harbour signals regional sponsorship; intake acknowledged |
| 7 to 8 | Show the sandbox demo: one mixed fleet, Cat plus non-Cat machines, in a single Procore view; qualification conversation with Brittany Schramm | SE, me | Demo delivered to at least two committee members; qualification criteria known |
| 9 to 10 | Technical scoping with Raechele Kuskie against the public developer platform; ask every thread for the Equipment Telematics PM and the Marketplace program owner by name | SE, me | Connector scope drafted; at least one of the two missing names produced |
| 11 to 12 | Product alignment via Stephen Perkins toward the Resource Management roadmap; exec sponsor letter toward Lee Miles framing the EMEA angle; consumption instrumentation defined (per-tenant activation, pull frequency, credits per active project) | Me, exec sponsor | Scoping agreement: connector spec, program tier path, and a named beta customer candidate |

Twelve weeks ends at a scoping agreement, not a signed partnership, on purpose. The execution plan takes it from there: sandbox build, beta customer, marketplace listing, first production credits within 30 days of listing (target, assumption).

### Content matrix

Each persona gets content matched to their stage. One asset is already built: the [Procore exec brief](briefs/procore.html).

| Persona | Aware | Engaged | Committed |
|---|---|---|---|
| Partnerships leadership (Jabbar, Schramm, Baldini) | One-pager: the mixed-fleet whitespace in Equipment Telematics | Joint-customer analysis: named contractors running both platforms | [Exec brief](briefs/procore.html): tier placement, consumption dashboard, United Rentals pattern |
| EMEA (Harbour, Miles) | One-pager with the EMEA angle: Dublin hub, UK Data Zone, Trackunit's home region | Integration demo staged around a European mixed-fleet contractor | Exec brief variant: regional win narrative for the EMEA business review |
| Product and platform (Kuskie, Perkins) | One-pager: IrisX API surfaces mapped to the Equipment Telematics open API | Integration demo: live GraphQL feed in the Developer Sandbox | Connector spec plus Helix and agent roadmap fit, where broader data coverage improves Procore's own AI features |

## Layer 2: ABM with partner, joint ABM into shared customers

Once the connector is live, the account flips from target to co-seller. The move: pull the overlap list from the GTM interlock and pick 10 to 20 shared accounts, contractors and rental companies that run Procore for projects and Trackunit hardware on their fleets. These are not cold accounts; both vendors already have a relationship, a rep, and usage data.

The joint value message is one sentence: your equipment data, from every OEM you own, inside the Procore workflows your site teams already use. No new screen, no swivel chair, the mixed fleet appears where schedules, cost tracking, and jobsite views live.

The co-run campaign has three motions. A joint webinar with one live customer showing the connector in a real project. One-to-one exec briefs for the top five shared accounts, co-presented by the Trackunit enterprise seller and the Procore account team. Field-sales alignment so Procore's Resource Management sellers, a staffed motion of at least eight people per the employee scan, carry the connector as a differentiator rather than discovering it by accident.

Metrics for this layer, all assumptions until internal data replaces them: shared-account meetings held (target 15 of 20 accounts in the first quarter of the campaign), integrations activated on shared tenants (target 10 in the first two quarters), and credits consumed by those tenants, following the reference case of 100 assets pulled daily per account.

## Layer 3: ABM through partner, the marketplace as channel

The third layer treats Procore's App Marketplace, roughly 539 apps, as a distribution channel in its own right. The mechanics are mapped in the [marketplace opportunity map](../execution/marketplace-opportunity-map.html): Procore publishes its Marketplace Approval Checklist, offers a free Developer Sandbox, and runs the June 2025 tier system that rewards partners on joint customer value.

Three things matter here. Category placement: the listing must sit where contractors searching for telematics or equipment find it, and the tier level determines visibility, so the Layer 1 relationship work directly buys Layer 3 distribution. Listing conversion: views to installs to activated tenants, each step instrumented. Partner-sourced installs: every self-serve install from the marketplace is a tenant Trackunit never had to sell, pulling IrisX data on a recurring schedule. The assumption set: a listed connector in the right category converts a low single-digit percentage of category traffic into installs, and each activated install follows the same daily-pull consumption profile as a sold one. The point of the layer is that the marginal cost of the next tenant approaches zero while the credit stream does not.

The three layers are sequential in dependency but overlapping in time. Layer 1 produces the connector and the tier placement. Layer 2 turns the first shared customers into references that raise listing conversion. Layer 3 returns partner-sourced installs that strengthen the joint-value case Procore's own sellers carry. Each layer feeds the next, and all three report into the same root metric.

## The KPI tree

One compact rollup from activity to the root metric. Every figure is an assumption from public sources, stated to show how targets get set, not as commitments.

| Level | Metric | Reference target (assumption) |
|---|---|---|
| Activity | Committee threads active (of 7 named) | 5+ by week 8 |
| Activity | Shared-account meetings | 15 in first campaign quarter |
| Engagement | Committee members who saw the live demo | 3+ by week 12 |
| Commitment | Scoping agreement signed | Week 12 |
| Build | Scoped to live | Under 90 days median |
| Adoption | Joint accounts activated, year one | 50 |
| Channel | Marketplace installs activating | Low single-digit share of category traffic |
| Root | IrisX credits: time to first credit | Under 30 days from listing go-live |
| Root | IrisX credits: steady state | 50 accounts x 100 assets x daily pulls as the reference consumption case |

## Risks

**Commodity-feed risk (from the account plan).** Procore treats telematics sources as commodity feeds and offers a directory listing without co-marketing, which caps activation and therefore credit consumption. Mitigation: lead with mixed-fleet coverage breadth that Cat and Deere structurally cannot offer, and tie the pitch to the Helix and agent roadmap, where broader data coverage makes Procore's own AI features better.

**Single-threading risk (ABM-specific).** The natural pull is to run everything through Tony Harbour, because he is the warm entry and the easiest yes. If he changes roles or deprioritizes the deal, the account resets to zero. Mitigation is built into the cadence: the global thread to Samira Jabbar opens in the same fortnight as the Harbour meeting, the SE owns an independent technical thread through Raechele Kuskie, and the exit criterion at week 8 requires the demo in front of at least two committee members, not one.

---

*Built from public LinkedIn and web data as of July 2026. All stage assignments, targets, and credit figures are assumptions from public sources, presented to demonstrate methodology and to be validated with internal data.*
