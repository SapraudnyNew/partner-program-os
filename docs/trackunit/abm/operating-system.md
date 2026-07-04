# ABM operating system

The [plays](plays.md) fail without plumbing. A committee map that lives in someone's head, a trigger spotted two weeks late, a thread nobody owns: that is how partner ABM decays into occasional outreach. This page is the minimum system needed to run the motion from week one, written deliberately without naming a CRM. Trackunit's stack is not public, and it does not matter. Everything below is objects, fields, and stage criteria that HubSpot, Salesforce, a purpose-built ABM tool, or a disciplined spreadsheet can implement in a day. The tool is a detail. The definitions are the system.

## Data model

Four objects carry the whole motion: the account, the people inside it, the signals around it, and the plays running against it. Every field below earns its place in a weekly ritual; anything that no ritual reads has been cut. That discipline matters more than the field list itself, because the usual failure of ABM tooling is not missing fields but dead ones, filled in once at setup and never read again.

**Partner Account.** One record per target organization, seeded from the [First Five](../partner-mapping/first-five.md).

| Field | Definition | Example |
|---|---|---|
| Name | Legal or common name of the partner organization | Procore |
| Category | Landscape category from the mapping work | ConTech |
| Score | Consumption potential score carried over from [targeting](targeting.md) | 4.8 / 5 |
| Disposition | Pursue, Deepen, or Monitor | Pursue |
| Layer mix | Which ABM layers are active: to, with, through | To |
| Funnel stage | One of the seven stages in the table below | First contact |
| Owner | The one person accountable for the account | Head of Partnerships |
| Next milestone | The next dated, checkable event | Demo vs. Equipment Telematics API |

**Contact.** One record per mapped committee member. Multithreading is only real if it is recorded.

| Field | Definition | Example |
|---|---|---|
| Name | Person's name, from public sources only at start | (mapped person) |
| Title | Current published title | Director, Partnerships |
| Role type | Economic buyer, technical gatekeeper, champion candidate, blocker risk, user voice | Technical gatekeeper |
| Relationship stage | Cold, aware, engaged, champion | Aware |
| Thread owner | Who on our side runs this thread | Partnerships Product Manager |
| Last touch | Date and channel of the most recent interaction | 2026-06-24, LinkedIn |

**Signal.** One record per observed trigger. A signal without a recorded action is a rumor.

| Field | Definition | Example |
|---|---|---|
| Date | When the signal was observed | 2026-06-30 |
| Type | ma, product, hiring, regulatory, partnership, financial | product |
| Source | Where it was seen, with a link | Procore release notes |
| Action taken | The play step it triggered, or "logged, no action" with a reason | Outreach wave 2 pulled forward |

**Play.** One record per running play instance, tied to an account and a layer.

| Field | Definition | Example |
|---|---|---|
| Account | The Partner Account it runs against | Point of Rental |
| Layer | To, with, or through | With |
| Status | Planned, running, blocked, done, killed | Running |
| Exit criterion | The observable event that ends the play | Activation dashboard agreed with POR product |

### Funnel stages

The funnel stages are the account-level view of the [seven-stage lifecycle](../method/index.md): Research covers Source and Qualify, Scoping through Scaling map onto Scope, Build, Launch, Adopt, and Scale. Criteria are binary. An account is in a stage or it is not, and nobody advances an account on optimism.

| Stage | Entry criterion | Exit criterion | Owner |
|---|---|---|---|
| Research | Account scored and tiered in [targeting](targeting.md) | Committee mapped with 3+ named contacts and an entry point chosen | Head of Partnerships |
| First contact | First outreach sent on at least one thread | A mapped contact replies and agrees to a conversation | Thread owners |
| In conversation | First meeting held | Partner names a counterpart owner and confirms a joint use case | Head of Partnerships |
| Scoping | Both sides commit to scoping in writing | Signed scope with data contracts and a consumption target | Partnerships Product Manager |
| Building | Scope signed, sandbox access granted | Build passes certification review | Platform Engineer |
| Live | Connector in production with a first account | First IrisX credits consumed within 30 days of go-live (reference assumption) | Head of Partnerships |
| Scaling | 5+ active accounts on the connector (reference assumption) | None; ongoing, reviewed via the connector scorecard | Full pod |

## Signal stack

No paid intent tools are assumed. The triggers that matter for partner accounts are public: funding and M&A news, job postings (a partner hiring integration engineers is telling you something), product release notes and changelogs, marketplace listing changes, LinkedIn activity of mapped committee members, and conference agendas where target people speak. Each source gets a named checker and a weekly slot, fifteen minutes of scanning per person at most. The SAP ETM sunset, the Procore telematics gap, and the Copilot timeline in the First Five were all found this way, from documents anyone can read.

The ritual is a 30-minute signal review each week. Every signal captured since the last review gets one of two outcomes: it triggers a play step, recorded on the Play object, or it is logged with a reason for no action. Nothing sits in an inbox and nothing is discussed without being written down first. Logged non-actions are not waste; three logged hiring signals from the same partner in a quarter is itself a trigger, and the log is what makes the pattern visible. The current signal set per account is visualized in the [signal radar](signal-radar.html).

## Cadence

The ABM cadence rides on the pod rituals from the operating plan rather than competing with them. Same rule applies: every session starts from its artifact, ends with decisions logged in it, and gets shortened or killed if it stops producing updates.

**Weekly.** The 30-minute signal review, plus a thread review per Tier-1 account: every mapped contact checked for last touch, stalled threads reassigned or explicitly parked.

**Biweekly.** A partner ABM pipeline deep dive, run inside every other session of the pod's pipeline review from the [pod operating plan](../execution/pod-operating-plan.md): stage moves argued against the criteria table, kill decisions taken, next milestones dated.

**Quarterly.** Re-score the full landscape, promote and demote tiers using the filter logic in [targeting](targeting.md), and retire accounts that produced no stage movement in two quarters. Promotion needs a reason recorded as a Signal; demotion needs one too. The quarter review is also where Monitor accounts like Palantir get their upgrade triggers checked against what actually happened.

## 12-week launch checklist

Twelve weeks is roughly the Q1 window in the [first five execution plan](../execution/first-five-plan.md), so the milestones below align with its sequencing: Procore sandbox work in weeks 1 to 6 and a beta customer around week 10, the Point of Rental re-scope and the first ETM successor conversations inside the same quarter. All dates are reference assumptions.

| Weeks | Milestone |
|---|---|
| 1 to 2 | CRM objects and fields above live; First Five committees imported with relationship stages |
| 3 to 4 | Signal stack running with named checkers; first outreach wave to Procore and Point of Rental threads |
| 5 to 6 | Procore sandbox demo underway per the execution plan; POR re-scope conversation opened |
| 7 to 8 | RentalResult and STAEDEAN partner contacts made for the ETM play; Sycor conversation opened for the D365 lane |
| 9 to 10 | First "in conversation" exits: at least two accounts with a named counterpart owner; Procore beta customer identified |
| 11 to 12 | First scoping agreement signed; [control tower](control-tower.html) reviewed with leadership as the standing dashboard |

## Roles

Decision rights come straight from the [pod operating plan](../execution/pod-operating-plan.md) and nothing here overrides them. The Head of Partnerships owns account selection, stage-move approval, and every commercial conversation; nobody else commits terms or engineering time to a partner, in a play step or anywhere else. The Partnerships Product Manager owns scoping threads and the technical-gatekeeper relationships, because the person who writes the spec should be the one talking to the people who will review it. The Platform Engineer owns Building-stage criteria and certification calls, including blocking a move to Live, and runs the demo assets that plays like Procore and Palantir depend on. The Field Marketing Manager owns outreach assets, launch moments, and the co-marketing steps inside with-layer and through-layer plays. Regional Partnership Managers, as they arrive, take thread ownership for regional contacts but escalate anything touching roadmap or pricing. In practice most contacts have a natural thread owner by role type: commercial threads to the Head, technical threads to the PPM or the engineer, marketing counterparts to Field Marketing.

## Measurement

The [control tower](control-tower.html) is the operating view: stage, owner, next action, and signal status for all five accounts on one screen. Behind it sits the same KPI tree as the pod plan, and it ends where everything in this program ends: IrisX credit consumption attributable to pod-delivered integrations. Stage counts, thread coverage, and signal-to-action rates are leading indicators only. All numbers in this system are assumptions until replaced with internal data, and the system is built so that replacing them takes an edit, not a redesign.

*Demonstration artifact built from public sources. Stage thresholds and dates are reference assumptions to be validated inside Trackunit.*
