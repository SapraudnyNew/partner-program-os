# Integration Partner Method

A seven-stage operating system for building, measuring, and scaling third-party integrations on a platform: from partner sourcing to marketplace-grade connectors that drive platform consumption.

---

## The problem

Most platform ecosystems stall for the same reason. Integrations are treated as engineering projects instead of a commercial lifecycle. A partner asks for an API key, an engineer builds a connector, the integration ships, and everyone moves on. Twelve months later the executive team asks why the integration catalog is growing but platform consumption is not.

The root cause is structural, not technical. Three specific failures recur:

First, integrations ship but get no adoption. The connector works, the demo is fine, and exactly one customer uses it. Nobody owned the stage between "code complete" and "customers running on it every day." The gap between a shipped integration and a consumed integration is where most platform ecosystems die.

Second, partner demand never converts into platform consumption. Inbound integration requests pile up, partnership teams sign agreements with recognizable logos, and none of it moves the metric that pays for the program: usage. Without a qualification discipline that scores consumption potential before a line of code is written, the team builds integrations for partners who will never bring volume.

Third, integration programs that cannot prove ROI lose executive sponsorship and budget. The economics of maturity are documented. A Forrester study of 454 companies found that high-maturity programs drive company-level revenue growth at nearly 2x the rate of low-maturity programs: 30% versus 16-17%. McKinsey's analysis of 100 incumbent ecosystem initiatives confirmed the difficulty: while 55% gained customer traction, only 10-15% generated more than 5% of total revenue from ecosystem value propositions. The difference between the 55% and the 10-15% is execution maturity, not strategic intent. A program that cannot report consumption per connector on a monthly cadence gets defunded, regardless of its actual contribution.

The cost of inaction compounds. A competing platform with a mature integration ecosystem locks in the ERP, rental, fleet, and application vendors that customers already run. By the time the gap is visible, those partners have embedded themselves in the customer's workflow, and switching costs work against you.

---

## The seven-stage integration lifecycle

Integration partnerships are not projects with a beginning and an end. They are an operating system with seven stages that run continuously. Each stage has a specific job, a specific failure mode, and a specific metric tied to platform economics. Skipping a stage or running one poorly creates debt that compounds downstream.

**Stage 1: Source**

Build a deliberate pipeline of integration partner candidates instead of waiting for inbound requests. The sourcing map covers the categories customers already depend on: ERP, rental and fleet management, industry software, and emerging application vendors. The output is a ranked candidate list built from customer demand signals, market coverage analysis, and competitive gaps. The failure mode is a pipeline made of whoever asked loudest, which produces a catalog shaped by chance. The core metric is qualified candidates per quarter against the annual connector launch target.

**Stage 2: Qualify**

Score every candidate on consumption potential before committing resources. The qualification model weighs shared customer overlap, expected data volume, use-case fit, and the partner's commercial commitment to a joint motion. Not the biggest logos. The candidates most likely to drive usage. The failure mode is signing partners for announcement value: the press release ships, the consumption never arrives. The core metric is the consumption potential score, verified against actual joint-customer counts, not partner claims.

**Stage 3: Scope**

Convert a qualified partner into a signed integration scope: use cases, data contracts, API surface, commercial model, launch plan, and quantified success criteria. Scope is where the commercial deal and the technical design get locked together, so neither side builds on assumptions. The failure mode is build-first enthusiasm: development starts on a vague spec, scope drifts for months, and the integration that ships solves no customer problem precisely. The core metric is time from qualification to signed scope, with a consumption target written into every scope document.

**Stage 4: Build**

The partner builds against the platform with sandbox access, documentation, reference implementations, and a named technical contact. The platform team's job is to make the partner fast, not to write the partner's code. Certification gates verify data quality, security, and error handling before anything reaches a customer. The failure mode is the engineering slog: timelines slip, the platform team quietly absorbs the work, and the partner learns nothing they can reuse. The core metric is time-to-certified-build from scope sign-off.

**Stage 5: Launch**

Move the certified integration into production with real customers: marketplace listing, joint announcement, sales enablement on both sides, and the first accounts live. Launch is a commercial event, not a deployment. The failure mode is the silent launch: the connector appears in a catalog, no one sells it, and it generates zero usage while everyone reports it as done. The core metric is time-to-first-credit: the days from certification to the first production consumption on the platform.

**Stage 6: Adopt**

Drive usage across the joint customer base until the integration is a habit, not a pilot. Adoption requires a named owner, a target account list built from customer overlap, and instrumentation that shows which accounts are active, dormant, or stuck. The failure mode is the lighthouse trap: one flagship customer works, the case study gets written, and the motion to the next twenty accounts never starts. The core metric is active accounts using the connector, with consumption per account as the depth check.

**Stage 7: Scale**

Turn a working integration into a reusable, marketplace-grade connector and a repeatable playbook. Scale means the connector deploys to a new account without custom work, the partner sells it independently, and the program can run the same lifecycle for the next partner faster. This is where individual integrations become an ecosystem and platform consumption compounds. The failure mode is permanent bespoke mode: every deployment is a project, so growth is capped by the team's own hours. The core metric is credit run-rate per connector and the share of platform consumption flowing through partner integrations.

---

## The maturity model

Knowing the seven stages is not enough. Leadership needs to know where the program stands today, what good looks like, and what it takes to get there. Every stage is scored at one of three levels:

**Basic.** The stage exists but runs on ad hoc effort. Integrations happen when an engineer has time. Results depend on individual heroism, and consumption data is partial or absent.

**Professional.** The stage runs on documented process with clear ownership. Consumption potential is scored, certification gates are enforced, and adoption is tracked per connector on a regular cadence. Outcomes are predictable within reasonable variance.

**World-class.** The stage runs with high automation and partner autonomy. Partners self-serve through the developer platform, connectors deploy without custom work, and consumption data flows both directions in real time. The program sets the benchmark competitors measure against.

The 7x3 matrix:

| Stage | Basic | Professional | World-class |
|---|---|---|---|
| Source | Inbound requests only | Category map with ranked candidates | Demand-signal-driven sourcing from customer data |
| Qualify | Logo-driven selection | Consumption potential scoring model | Overlap-verified scoring with predictive usage estimates |
| Scope | Verbal agreements, vague specs | Signed scope with data contracts and success criteria | Templated scoping with consumption targets in every contract |
| Build | Platform team writes the code | Partner builds with sandbox, docs, certification gates | Self-service developer platform with automated certification |
| Launch | Ships to a catalog, no motion | Joint launch plan with first accounts committed | Marketplace launch engine with sales enablement both sides |
| Adopt | One pilot customer | Named owner, target accounts, usage instrumentation | Automated adoption plays triggered by usage signals |
| Scale | Every deployment is bespoke | Reusable connector, documented playbook | Partner-led selling, compounding consumption per connector |

Each cell expands into capability checkpoints and KPIs with quantified thresholds in the full scorecard. The checkpoints are binary: present or absent, no partial credit. That clarity eliminates the ambiguity that lets underperforming programs hide behind "we're working on it."

---

## The diagnostic process

The maturity model becomes actionable through a structured diagnostic in four steps:

**Step 1: intake.** A short questionnaire establishes current state: integration catalog, partner mix, consumption share by connector, pain points, and 12-month ambition.

**Step 2: scoring.** Each of the seven stages receives a maturity level based on capability evidence, not self-reported perception. A program either has a consumption potential scoring model or it does not. The working grid is in the [scorecard](scorecard.html).

**Step 3: gap map.** Current scores are plotted against a target state on a seven-axis [spider chart](spider-chart.html). Seven axes, three concentric rings. The gap is visible in one second, and any executive can read it without explanation.

**Step 4: roadmap.** The gap map converts to a sequenced 90-day action plan. A program with a strong build pipeline but no adoption motion has a different priority than one with eager partners and no qualification discipline. The roadmap selects the 3-5 interventions with the highest consumption impact.

---

## Application context

This method is written generically because the lifecycle is portable across any platform that monetizes through usage. The application context here is a construction operating-data platform where the commercial unit is credit consumption: every stage metric above rolls up to one number, credits consumed through partner integrations. Time-to-first-credit, active accounts per connector, and credit run-rate are the platform-economy translation of pipeline, activation, and revenue.

---

*Framework illustration. Maturity thresholds are reference targets, not Trackunit scores.*
