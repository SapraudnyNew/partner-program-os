# Partner Program Maturity Framework

A three-level scoring system for diagnosing where a partner program stands today, where it needs to go, and what closes the gap.

---

## Why maturity matters

Partner programs fail gradually, not suddenly. A company recruits partners, signs contracts, and builds a portal. Revenue trickles in. Leadership asks for ROI justification. The channel team produces activity metrics: partners recruited, MDF spent, portal logins. None of these answer the question the CEO is actually asking: is this program generating revenue efficiently, and will it compound over time?

The maturity model replaces feelings with evidence. It scores each lifecycle stage against observable capabilities and measurable outcomes. The score reveals which stages drag the program down and which are ready to scale. A company at Basic in Enable but Professional in Co-sell has a specific problem: partners cannot sell independently, so every co-sell deal requires manufacturer hand-holding that does not scale. The intervention is clear. The investment case writes itself. [P-36] [P-40]

---

## Three levels

Every stage of the partner lifecycle operates at one of three maturity levels. The levels are cumulative: Professional includes everything in Basic, World-class includes everything in Professional.

**Basic**

The stage exists but depends on individual effort. Processes are informal or undocumented. Results vary by person, by partner, and by quarter. The company reacts to partner needs instead of anticipating them. Data is partial, late, or trapped in spreadsheets. Most partner programs operate at Basic across most stages. This is not failure. It is the starting point. But staying here past the first 12-18 months signals a structural problem.

Characteristics: manual execution, heroism-dependent, inconsistent outcomes, no SLAs, limited measurement.

**Professional**

The stage runs on documented process with defined ownership. SLAs exist and are enforced. Metrics are tracked and reviewed on a regular cadence. Outcomes are predictable within reasonable variance. The work does not collapse when a key person leaves. Getting from Basic to Professional is primarily a systems and governance investment: documenting the process, assigning RACI, building the dashboards, and enforcing the SLAs. Most companies can reach Professional in 6-12 months per stage with focused effort. [P-40]

Characteristics: documented process, clear RACI, enforced SLAs, regular reporting, repeatable outcomes.

**World-class**

The stage runs with minimal friction, high automation, and continuous optimization. Partners operate with significant autonomy. Data flows bidirectionally in real time. The company sets the benchmark that competitors and industry analysts reference. Getting from Professional to World-class requires technology investment, cultural shift toward ecosystem thinking, and sustained executive commitment. Few companies reach World-class across all seven stages. The goal is not perfection across the board. The goal is World-class in the stages that drive the most revenue and Professional everywhere else. [P-01]

Characteristics: automated workflows, partner autonomy, bidirectional data, predictive analytics, continuous improvement, industry benchmark status.

**The economic case for progression**

The difference between levels is not theoretical. Forrester's study of 454 companies quantified it: high-maturity programs drive company-level revenue growth at 30% compared to 16-17% for low-maturity programs. High-maturity companies receive 28% of total revenue from partnerships compared to 18% for low-maturity companies. For the average company in the sample ($1.55B revenue), the gap represents $162M annually in partner-channel revenue alone.

McKinsey found that while 55% of incumbents gain traction with ecosystem initiatives, only 10-15% generate more than 5% of total revenue from them. The drop-off maps directly to maturity: traction comes from Basic-level effort (launching, recruiting, signing). Revenue comes from Professional and World-class execution (enabling, co-selling, delivering, renewing).

The transition from Basic to Professional in a single stage typically requires 6-12 months and is primarily a systems and governance investment. The transition from Professional to World-class requires 12-24 months, technology spend, and cultural change. The compounding effect across all seven stages means that a company reaching Professional across the board operates on fundamentally different economics than one stuck at Basic. The Forrester data shows this is not a linear improvement. It is a multiplier.

---

## Scoring methodology

Each stage is scored using two instruments: capability checkpoints and performance KPIs.

**Capability checkpoints** answer the question: what do you have?

Each maturity level has 3-5 checkpoints per stage. Each checkpoint is binary: present or absent. There is no partial credit. A company either has an ideal partner profile with a scoring matrix (Professional checkpoint in Recruit) or it does not. A company either has automated AR suspension for overdue partner accounts (World-class checkpoint in Deliver) or it does not. Binary clarity eliminates the ambiguity that lets underperforming programs hide behind "we're working on it." [P-36]

A stage earns a maturity level when all checkpoints for that level (and all levels below it) are present. If a company has 4 of 5 Professional checkpoints in Enable, the score is Basic. The missing checkpoint is the gap. The gap is the roadmap.

**Performance KPIs** answer the question: how well does it work?

Capabilities without performance are infrastructure without revenue. Each maturity level has 2-3 KPIs per stage with quantified thresholds. The thresholds are calibrated from industry benchmarks (Forrester, McKinsey, Omdia partner ecosystem research) and operational experience. A company that has all Professional checkpoints but misses the KPI thresholds is classified as Basic-with-infrastructure: the system is built but not yet producing results. This distinction matters because it changes the intervention from "build the system" to "optimize the system."

**Scoring rules:**

1. Score capabilities first, then KPIs.
2. A stage scores at the highest level where all capability checkpoints are present AND KPI thresholds are met.
3. If capabilities are present but KPIs fall short, the score stays at the level below. Tag it "infrastructure ahead of performance" in the gap report. The intervention is optimization, not construction.
4. If KPIs are met but capabilities are absent, investigate data quality. Results without process are usually unsustainable or misattributed. Tag it "fragile performance" in the gap report.
5. Each stage scores independently. A company can be World-class in Deliver and Basic in Recruit. This is common in companies that grew through direct sales and bolted on a channel later.
6. Numeric conversion for spider chart: Basic = 1, Professional = 2, World-class = 3. A company scoring Basic across all seven stages has a spider area of 7 (the minimum). A company at World-class across all seven has 21 (the maximum). The total score is less useful than the shape: a lopsided spider reveals which stages constrain the others.

---

## The diagnostic output

The scoring produces three artifacts:

**The scorecard.** A 7x3 matrix showing the maturity level for each stage, with capability checkpoints marked present/absent and KPI actuals versus thresholds. This is the working document. The Head of Channel uses it to plan interventions. See [scorecard-template.md](scorecard-template.md).

**The spider chart.** A seven-axis radar visualization. Current state plotted as one shape, target state as another. The gap between the two shapes is visible in one second. Any executive can read it without explanation. Basic = inner ring (score 1), Professional = middle ring (score 2), World-class = outer ring (score 3). See [spider-chart.html](spider-chart.html).

**The gap report.** A prioritized list of gaps ordered by business impact. Each gap identifies the stage, the missing checkpoints or underperforming KPIs, the estimated cost of the gap (in revenue leakage, partner churn, or competitive displacement), and the recommended intervention from the stage's intervention library. The gap report is the bridge between diagnosis and action.

---

## How gaps become roadmaps

Not all gaps are equal. A gap in Recruit limits the total size of the partner portfolio. A gap in Enable limits every partner's productivity. A gap in Deliver destroys trust and creates partner churn that undermines everything upstream. The sequencing of gap closure follows three principles:

**Principle 1: downstream gaps first.** A company that recruits partners into a broken Deliver stage is recruiting partners into churn. Fix the stages that retain and monetize partners before investing in the stages that add more partners. The exception: if the company has fewer than 10 active partners, Recruit takes priority because there is no portfolio to optimize.

**Principle 2: highest revenue impact per stage.** Each gap report estimates the revenue at risk from each stage's current score. A company losing 15% of partner-sourced deals to attribution disputes (Co-sell gap) has a different priority than one losing partners in the first 90 days because onboarding is a PDF and a webinar (Onboard gap). Revenue impact determines sequence, not the stage number.

**Principle 3: 90-day sprints.** Moving a single stage from Basic to Professional takes 6-12 months of sustained effort. But the first intervention in each stage can show measurable improvement in 90 days. The roadmap selects 3-5 interventions across the highest-impact gaps, executes them in a 90-day sprint, re-scores, and adjusts. This creates a visible feedback loop that sustains executive sponsorship.

---

## Relationship to the lifecycle stages

The maturity framework is the measurement layer. The seven lifecycle stages are the execution layer. They connect through the scorecard:

Each stage document (01-recruit.md through 07-expand.md) contains:
- Capability checkpoints for Basic, Professional, and World-class
- KPIs with tiered thresholds
- An intervention library: the specific plays that close gaps at each level

The framework document you are reading defines how to score. The scorecard template provides the working grid. The stage documents provide the content that fills the grid for any specific company.

See: [scorecard-template.md](scorecard-template.md) for the full 7x3 matrix with checkpoints and KPIs.

---

## Source mapping

Principles from `appendix/evidence-library.md` that primarily apply to the maturity framework:
- P-36 (80% of failed ecosystems = governance issues; RACI must be explicit per stage)
- P-40 (alliance capability is institutional, not personal; documented method beats heroism)
- P-01 (partnership is ecosystem orchestration, not channel management)
- P-09 (strategy precedes structure; tier definitions follow commercial purpose)
- P-04 (partner ecosystem is a data source)
- P-41 (performance management is a two-way conversation; bidirectional scorecard at QBR)
