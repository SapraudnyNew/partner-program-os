# Pod Operating Plan: The First 90 Days

How I would run the Integrations & Applications pod at Trackunit: a dedicated Partnerships Product Manager, a Platform Engineer, a Field Marketing Manager, and Regional Partnership Managers as the function scales, with structured interlocks into Product & Engineering (P&E) and GTM leadership. The plan below covers principles, decision rights, cadence, the KPI tree rooted in IrisX credit consumption, and 30/60/90 milestones.

## 1. Operating principles

1. **The pod ships integrations, not slideware.** Every week ends with something a partner or customer can touch: a scoped spec, a working endpoint, a live marketplace listing. Decks are inputs, never outputs.
2. **Credit consumption is the only success metric that counts at quarter end.** Launches, signatures, and press are leading noise unless they convert into IrisX credits consumed. Every activity in the pod traces to that number or gets cut.
3. **Partner demand enters the P&E roadmap through one door.** All integration requests, from partners, sales, or customers, flow through the pod's qualification framework and the Platform Partnerships Lead. No side channels, no hallway commitments.
4. **Every integration compounds into a reusable marketplace connector.** One-off custom work is a cost center. We build once, list on the marketplace, and sell many times. If it cannot be productized, it needs an explicit exception with a commercial reason.
5. **Engineering time is the scarcest resource, so we spend it against scored demand.** The qualification framework ranks demand by projected credit consumption, account coverage, and reuse potential. The score decides sequence, not who shouted loudest.
6. **Say no early and in writing.** A fast, documented no to a low-fit partner protects the roadmap and the relationship. Ambiguity is the expensive answer.

## 2. Roles and decision rights

| Role | Owns | Decides alone | Escalates |
|---|---|---|---|
| **Head of Partnerships, I&A (this role)** | Pod strategy, portfolio prioritization, partner commercial terms, credit consumption target | Partner selection and sequencing, qualification framework changes, resource allocation inside the pod | Deals with non-standard commercial or legal terms; conflicts with P&E roadmap that the interlock cannot resolve |
| **Partnerships Product Manager** | Integration specs, qualification scoring, connector backlog, partner-facing documentation | Scope of individual integrations within an approved partner engagement; spec trade-offs that do not move dates | Scope changes that move a live date or require additional P&E capacity |
| **Platform Engineer** | Technical feasibility, reference implementations, developer portal quality, connector review before marketplace listing | Technical design within a spec; blocking a listing that fails quality or security review | Platform gaps that require core IrisX engineering work |
| **Field Marketing Manager** | Launch plans, co-marketing with partners, adoption campaigns per connector, marketplace merchandising | Campaign channel and content choices within budget; launch timing within an agreed window | Budget overruns; launches lacking an adoption plan tied to credit targets |
| **Regional Partnership Managers (as we scale)** | Regional partner pipeline, local enablement, first-line partner relationships | Which regional prospects enter qualification; regional event participation | Any commitment on roadmap, pricing, or exclusivity; anything promising engineering time |
| **Platform Partnerships Lead (embedded in Product, interface not report)** | Representing integration demand inside the P&E roadmap and prioritization process | How pod demand is packaged and sequenced into P&E planning artifacts | Back to this role when P&E capacity cannot cover committed partner dates |

One rule binds the table: nobody outside this role commits engineering time or commercial terms to a partner. Everything else is delegated deliberately.

## 3. The weekly cadence

| Ritual | Frequency | Duration | Participants | Standing agenda | Artifact updated |
|---|---|---|---|---|---|
| **Pod standup** | Weekly, Monday | 25 min | Full pod | Blockers, this week's ship list, one metric callout | Pod ship list |
| **Pipeline review** | Weekly, Wednesday | 45 min | Head, PPM, RPMs | New demand scored, stage moves, kill decisions, next two scoping slots | Qualified integration pipeline |
| **P&E interlock** | Weekly, Thursday | 30 min | Head, PPM, Platform Engineer, Platform Partnerships Lead | Capacity vs. committed dates, spec handoffs, platform gaps, one decision per session | Integration roadmap |
| **GTM interlock** | Biweekly | 30 min | Head, Field Marketing, GTM leadership rep | Partner-sourced pipeline handoff, launch calendar, account overlap on live connectors | Partner-sourced pipeline log |
| **Marketplace review** | Biweekly | 30 min | PPM, Platform Engineer, Field Marketing | Listing quality, adoption per connector, developer portal friction, credit consumption by connector | Connector scorecard |

Cadence rules: every ritual has one owner, starts from its artifact, and ends with decisions logged in it. If a meeting produces no update to its artifact twice in a row, we shorten or kill it.

## 4. The KPI tree

Root metric: **IrisX credit consumption attributable to pod-delivered integrations and applications**. All numeric targets below are reference assumptions, stated to show how I set targets, not what Trackunit's targets should be.

| Level | Metric | Reference target (assumption) | Why it leads the root |
|---|---|---|---|
| Root | IrisX credits consumed via pod integrations, per quarter | Baseline in Q1, then +25% QoQ as reference | The commercial metric this role is accountable for |
| Leading | Integration pipeline coverage (scored demand vs. quarterly build capacity) | 3x coverage as reference | No pipeline, no future consumption |
| Leading | Scoped-to-live cycle time per integration | Under 90 days median as reference | Faster cycles compound consumption sooner |
| Leading | Time-to-first-credit per new integration | Under 30 days from go-live as reference | Proves the integration is used, not just launched |
| Leading | Active accounts per connector | 5+ within two quarters of listing as reference | Reuse is what separates connectors from custom work |
| Leading | Partner-sourced pipeline handed to GTM | 2 qualified opportunities per live connector per quarter as reference | Ties the pod to revenue beyond consumption |

Health checks reviewed monthly, not weekly: connector defect rate post-listing, developer portal signup-to-first-call conversion, and partner satisfaction on a simple three-question pulse.

## 5. 30/60/90 milestones

**Days 1 to 30: listen and map.**
- Inventory every current integration: status, owner, consumption contribution, and whether it is a reusable connector or custom work.
- Compile the full partner demand backlog from sales, support, product, and existing partner conversations into one scored list.
- Sit in existing P&E planning and GTM meetings before changing anything; document how integration demand flows today and where it leaks.
- Meet the top partners by consumption and by pipeline potential, plus the Platform Partnerships Lead, weekly from day one.
- Output: a one-page current-state map and a draft qualification framework circulated for feedback.

**Days 31 to 60: stand up the machine.**
- Launch the full weekly cadence from Section 3, with artifacts live from the first session.
- Publish the qualification framework v1 and integration roadmap v1, reviewed with P&E and GTM leadership.
- Run the first two scoping engagements through the new framework end to end, deliberately including one no.
- Agree the credit-attribution method for pod-delivered integrations with Finance and Product analytics.
- Output: cadence running, roadmap published, two engagements in scoping.

**Days 61 to 90: prove the loop.**
- First integration from the new pipeline moving through build with a committed live date.
- Marketplace listing flow tested end to end with a real connector: submission, review, listing, first install.
- Credit-consumption reporting live per connector and per partner, feeding the connector scorecard.
- QBR format shipped and piloted with one strategic partner, anchored on consumption and joint pipeline.
- Output: the full loop demonstrated once, from scored demand to measurable credits, ready to scale.

## 6. Interlocks that fail and how this plan prevents it

Partner functions inside product companies fail in three predictable ways.

**Partner demand bypasses the roadmap.** A senior stakeholder promises a partner an integration in a hallway, and engineering finds out via a signed contract. Prevention here: one door (Principle 3), decision rights that reserve engineering commitments to this role, and a weekly P&E interlock where every commitment is visible in the integration roadmap before it is made externally.

**Engineering treats integrations as distractions.** This happens when demand arrives unscored, unspecced, and urgent. Prevention: the Partnerships Product Manager delivers build-ready specs, the qualification score justifies every request in P&E's own prioritization language via the Platform Partnerships Lead, and the pod's own Platform Engineer absorbs reference implementations so core teams see leverage, not interruptions.

**Marketing celebrates launches nobody adopts.** Prevention: no launch without an adoption plan tied to a time-to-first-credit target, and the marketplace review inspects consumption per connector two weeks after every listing. A launch that produces zero credits is treated as an open incident, not a closed win.

The common thread: every interlock runs on a shared artifact and a shared metric, so disagreements surface in a meeting with a decision log, not in a quarter-end surprise.

*Demonstration artifact built from the public job description. Cadence and targets are reference assumptions to be validated inside Trackunit.*
