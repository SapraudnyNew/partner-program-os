# Stage 4: Co-sell

## Strategic intent

Generate joint pipeline and pursue deals together. Not referral passing. Not lead dumping. Structured collaboration that produces revenue neither side could generate alone.

Co-sell is where the partner program earns its keep. Stages 1-3 (Recruit, Onboard, Enable) are investment. Stage 4 is where that investment converts to pipeline. The economics are clear: companies that frequently co-sell with partners report 51% higher revenue growth. 68% of companies see higher close rates when partners are involved. Partner-sourced deals convert at rates 10-20 percentage points above direct marketing channels. These numbers are not because partners are better salespeople. They are because partners carry trust, access, and context that cold outreach cannot replicate. [P-05] [P-11]

Co-sell operates at two levels. The first is the regular co-sell motion: deal registration, joint business planning, account mapping, pipeline management, and revenue attribution. Every company with a partner program runs some version of this, usually badly. The second is Account-Based Sales and Marketing (ABSM): a structured, sprint-based approach that targets specific high-value accounts through deep research, personalized outreach, and coordinated multi-stakeholder engagement. ABSM is a separate execution stream that runs in parallel with regular co-sell, not a replacement for it.

This document covers both.

---

## Maturity levels

| Level | Capabilities | KPIs |
|---|---|---|
| Basic | Deal registration exists. At least one joint selling activity in past 12 months. Partner-sourced leads tracked separately in CRM. | Partner-sourced revenue >5%. Deal reg approval <72h. Pipeline coverage >1x. |
| Professional | Account mapping conducted. Joint business plans with top partners. Deal reg SLA (48h) with conflict resolution. MDF allocated with ROI requirements. | Partner-sourced revenue >15%. Deal reg approval <48h. Pipeline coverage >2.5x. MDF ROI >3x. |
| World-class | Co-investment model. Partner-influenced revenue tracked and reported monthly. Multi-partner deals orchestrated. ABSM campaigns running per target account. | Partner-sourced revenue >25%. Deal reg approval <24h. Pipeline coverage >4x. MDF ROI >5x. |

Full checkpoint detail: see [maturity-model/scorecard-template.md](maturity-model/scorecard-template.md), Stage 4.

---

## The co-sell system

### Deal registration

Deal registration is the "first to file" system that protects partner investment in opportunity development. Without it, partners identify opportunities and the manufacturer's direct sales team closes them without attribution. That happens once, the partner stops sourcing. Trust dies.

**Registration mechanics:**

1. Partner submits registration through PRM portal (not email, not phone call).
2. System runs automatic duplicate check against existing registrations and direct pipeline.
3. If no conflict: approval within SLA (target: 24-48 hours). Partner receives protection period, discount tier, and pre-sales resource allocation.
4. If conflict exists: enter conflict resolution workflow. Documentation first (emails, meeting notes, NDAs, POC agreements). Activity timeline second. Registration timestamp third. Default-to-partner policy recommended: if the partner registered properly and has documented proof of relationship, partner wins.
5. Approved registration creates or updates the opportunity in CRM with partner attribution. Opportunity is pipeline-segregated from direct sales.

**Protection period:** typically 90-180 days depending on deal complexity. Renewable if the opportunity is actively progressing. Expires automatically if no activity logged within 30 days.

**Metrics:** registration volume by partner and region, approval rate, average approval time, protection period utilization (registrations that convert to closed deals), conflict frequency and resolution time.

### Joint business planning

Co-sell without a plan is improvisation. Joint business plans (JBPs) formalize the partnership's commercial objectives for a defined period (typically 12 months, reviewed quarterly).

**JBP structure:**

| Section | Content | Owner |
|---|---|---|
| Mutual objectives | 3-5 shared revenue or pipeline targets | Both (agreed jointly) |
| Target account list | Top 10-20 accounts identified through account mapping | Both |
| Joint value proposition | Why the combined solution solves the customer's problem better than either party alone | Manufacturer (content), partner (market context) |
| Roles and responsibilities | Who leads discovery, demo, proposal, negotiation, implementation per deal type | Both (agreed, documented) |
| Campaign plan | Co-marketing activities, MDF allocation, campaign calendar | Manufacturer (marketing), partner (execution) |
| Review cadence | Monthly pipeline review for Tier A partners. Quarterly business review for all. | Both |
| Success metrics | Pipeline created, win rate, revenue closed, customer satisfaction | Both |

JBPs exist for Tier A (top 20%) partners. Tier B and C partners operate on standard co-sell processes without individualized plans. [P-41]

### Account mapping

Account mapping is the act of comparing the manufacturer's target account list with the partner's customer base to identify three types of accounts:

- Overlap accounts: both parties have an existing relationship. Highest co-sell probability.
- Whitespace accounts: the partner has a relationship, the manufacturer does not. Partner-sourced opportunity.
- Competitive displacement: the partner's customer uses a competitor's product. Replacement opportunity.

The Account Mapping Matrix is the base artifact of ecosystem-led co-selling. It does not require raw customer list exchange. Modern ecosystem platforms map overlap using privacy-preserving matching: both sides upload hashed account data, the platform identifies matches without exposing raw lists. [P-05] [P-43]

Account mapping runs quarterly at minimum. For Tier A partners, monthly. Output feeds the JBP target account list and the ABSM campaign targeting.

### Pipeline management

Co-sell pipeline is managed separately from direct pipeline, with its own forecast, its own review cadence, and its own attribution rules.

**Pipeline architecture:**

| Pipeline element | Definition |
|---|---|
| Partner-sourced | Partner originated the opportunity. Partner registered before any manufacturer touch. 100% creation credit to partner. |
| Partner-influenced | Manufacturer originated the opportunity. Partner materially advanced it (co-sell meeting, technical validation, POC support, procurement access). Influence event logged with evidence. |
| Co-sold | Both parties actively involved in the sales cycle. Roles defined per JBP. Revenue attributed per pre-agreed split. |

**Attribution rules:**

- Partner-sourced: first-touch creation credit. Partner registered the deal before the manufacturer's SDR/AE contacted the account.
- Partner-influenced: logged influence events with timestamps and evidence (meeting notes, solution architecture, POC sign-off, executive intro). Each event must cause a stage change or satisfy a gating requirement. No evidence, no influence credit.
- Multi-partner deals: role-weighted split stored on a junction object. Standard starting weights: lead partner 50%, supporting partners split remaining 50% by contribution.

**Review cadence:**

- Weekly: pipeline hygiene check (stale opportunities, unregistered partner deals, missing attribution).
- Monthly: co-sell pipeline review with Tier A partners. Shared visibility into deal health, blockers, and next actions.
- Quarterly: QBR with all active co-sell partners. Performance against JBP targets. Pipeline coverage assessment. Reforecast.

---

## ABSM skill: Account-Based Sales and Marketing

ABSM is a separate execution stream within the co-sell stage. Where regular co-sell manages the pipeline in aggregate, ABSM targets individual high-value accounts with deep research, personalized outreach, and coordinated multi-stakeholder engagement.

ABSM runs as a sprint: a time-bounded campaign (typically 8-12 weeks) focused on a defined scope. One territory. One product. One vertical. Three target accounts.

**Execution model:** joint. The manufacturer owns strategy, research, content creation, and campaign orchestration. The partner owns customer relationships, last-mile delivery, and local market intelligence. Both contribute to account selection and stakeholder mapping.

The ABSM pipeline has six stages. Each stage produces specific deliverables that feed the next.

### ABSM Stage 0: Context Architect

**Purpose:** establish the strategic foundation for the campaign. Product positioning, market context, buyer personas, ecosystem map, and ICP criteria.

**Deliverables:**

| # | Deliverable | Content |
|---|---|---|
| 0.1 | Product DNA and positioning | Value proposition, business model, pricing model, competitive differentiation, tone of voice rules |
| 0.2 | Market and competitive landscape | PESTEL analysis of the target vertical, competitive positioning map (direct and indirect competitors), market sizing for the target territory |
| 0.3 | Buyer persona profiles | 3-5 roles in the buying committee (e.g., CISO, CTO, CFO, VP Engineering, Procurement). For each: KPIs, jobs-to-be-done, primary pain points, information sources, decision criteria |
| 0.4 | Ecosystem map | Industry events (min 3), trade associations (min 2), opinion leaders (min 5), complementary technology vendors, regulatory bodies |
| 0.5 | ICP criteria synthesis | Target verticals, company size thresholds, geography, technology signals, trigger events (M&A, regulatory deadlines, leadership changes), disqualification criteria |

**Owner:** manufacturer (strategy and research), partner (local market validation and ecosystem input).

**Guardrails:** no unsourced facts. Missing data marked as blind spot. Hypotheses marked explicitly. Minimum 2 sources per critical claim.

### ABSM Stage 1: Target Account Selector

**Purpose:** score and rank target accounts to select the top 3 for deep pursuit.

**Deliverables:**

| # | Deliverable | Content |
|---|---|---|
| 1.1 | ICP scoring model | 2 hard filters (MUST HAVE criteria) + GE/McKinsey matrix with two axes (account attractiveness 1-5, strategic position strength 1-5) |
| 1.2 | Account long list | 8-10 companies in the target vertical and territory, each with basic firmographic data (revenue, headcount, domain, industry classification) |
| 1.3 | Account scoring matrix | Each account scored on attractiveness and strength dimensions. Scores of 3 or 5 require evidence (exact quote + source URL). No evidence = forced score of 1. |
| 1.4 | Top 3 selection | Ranked accounts with total ABSM score. Selection rationale documented. |

**Scoring formula:** Total = (Attractiveness average + Strength average) / 2 x 20. Maximum 100.

**Owner:** manufacturer (scoring model and research), partner (local market intelligence, relationship assessment).

### ABSM Stage 2: Deep Intel Profiler

**Purpose:** build deep intelligence dossiers on each of the 3 target accounts using MEDDPICC framework.

**For each of the 3 accounts, produce 4 deliverables:**

| # | Deliverable | Content |
|---|---|---|
| 2.1 | Company research (MEDDPICC) | Strategic initiatives, financial indicators, technology stack signals, talent signals (hiring patterns = operational priorities), competitive threats. Classification of each pain: C-level priority vs local issue. Cost of inaction estimated. Executive summary on first page. |
| 2.2 | Stakeholder mapping | 3-5 real people mapped to buying committee roles: Economic Buyer, Champion, Technical Buyer, User Buyer, Coach. Name, title, division, MEDDPICC role. No fabricated contacts: if data unavailable, mark as blind spot. |
| 2.3 | Contact sheet | Name, title, buying role, LinkedIn URL, email (if publicly available). Sources: corporate website, LinkedIn, industry event speaker lists. |
| 2.4 | Account plan | Point of view (why this account needs the solution now), compelling event with deadline, 3 key threats (competitor, internal solution, competing budget priority), 2 prioritized opportunities, influence architecture, decision criteria map. |

**Owner:** manufacturer (research execution), partner (relationship intelligence, stakeholder access validation).

**Partial success protocol:** if primary sources are unavailable, fall back to secondary sources. Campaign does not stop for missing data.

### ABSM Stage 3: Strategy Master

**Purpose:** identify pain patterns across the 3 accounts, select the campaign theme (Sweet Spot), and build the content matrix.

**Deliverables:**

| # | Deliverable | Content |
|---|---|---|
| 3.1 | Pain pattern analysis | Cross-account comparison. Common pains (appearing in 2/3 or 3/3 accounts), unique pains. Categorization: operational, financial, strategic, technological, talent. Intersection table: account x pain x persona. |
| 3.2 | Sweet Spot selection | Campaign theme with: name (3-5 words), thesis, target persona champion, anchor pain, 2-3 proof points from intel, risks, account coverage (2/3 or 3/3). Selection criterion: highest coverage + lowest risk. |
| 3.3 | Content matrix | Persona x funnel stage x content type. 3-5 personas x 3 stages (Interest, Consideration, Decision). Email sequence specification: 3 primary personas x 4 touches = 12 emails per account. |

**Owner:** manufacturer (pattern analysis and strategy), partner (validation of pain relevance in local market).

### ABSM Stage 4: Execution Arsenal

**Purpose:** produce the personalized outreach assets for each of the 3 target accounts.

**For each account, produce 4 deliverables:**

| # | Deliverable | Content |
|---|---|---|
| 4.1 | One-page business case | Status quo with numbers from intel, cost of inaction (quantified), ROI model, implementation timeline. Written for the Economic Buyer. |
| 4.2 | Email sequence (12 per account) | 3 personas x 4 touches. Touch 1: cold outreach via insight from intel. Touch 2: value-add content. Touch 3: social proof (case study from similar company). Touch 4: break-up (final touch). Each email: subject line (<50 chars), personalized hook, one pain mapped to one argument mapped to one proof point, specific CTA. |
| 4.3 | Mutual Action Plan | Joint objectives, 8-12 week phased timeline, named owners (real people from stakeholder mapping), milestones, resources required, risk register. |
| 4.4 | Personalized landing page or leave-behind | Product positioning filtered through the account's specific pain points. Structure: hero (the account's problem), proof (how the solution addresses it), how (implementation approach), CTA (next step). Personalized with account name, industry context, and relevant metrics. |

**Owner:** manufacturer (content creation), partner (relationship-based delivery, email sending, meeting scheduling).

**Total sprint output per campaign:** 4 context documents + 1 scoring matrix + 12 intel files (4 per account) + 3 strategy documents + 12 execution files (4 per account) = 32 artifacts.

### ABSM Stage 5: Infrastructure and Launch

**Purpose:** set up measurement, reporting, CRM integration, and campaign launch operations.

**Deliverables:**

| # | Deliverable | Content |
|---|---|---|
| 5.1 | Measurement system | Campaign KPIs: emails sent, open rate, reply rate, meetings booked. Pipeline velocity formula. Account engagement score (composite of email engagement, meeting attendance, content interaction, stakeholder involvement). |
| 5.2 | Campaign dashboard | Visual reporting: tactical (email performance), operational (funnel by account), strategic (engagement heatmap: accounts x personas), revenue (pipeline velocity, weighted pipeline). |
| 5.3 | CRM integration | Account records with ABSM score field and engagement score field. Contact records with buying role field. Opportunity records linked to ABSM campaign. Pipeline stages: new account, awareness, nurturing, MQA-ready, consideration, validation, closed-won. |
| 5.4 | Campaign budget | Cost of research tools, content production, platform fees, personnel time. Planned vs actual tracking. |

**Owner:** manufacturer (system setup, dashboard), partner (CRM hygiene on their side, reporting on outreach activity).

### ABSM universal campaign template

The template below defines a single ABSM sprint. Fill in the bracketed fields per campaign instance.

| Parameter | Value |
|---|---|
| Territory | [e.g., DACH] |
| Product | [e.g., Zero Trust Network Access] |
| Vertical | [e.g., Financial services under NIS2/DORA regulation] |
| Campaign duration | 8-12 weeks |
| Target accounts | 3 (selected through Stage 1 scoring) |
| Personas per account | 3-5 (from Stage 0 buyer persona profiles) |
| Emails per account | 12 (3 personas x 4 touches) |
| Total sprint deliverables | 32 artifacts across 6 stages |
| Measurement | Email open/reply rates, meetings booked, pipeline created, engagement score per account |
| CRM pipeline | ABSM-specific pipeline with 7 stages |
| Budget | Research + content + tools + personnel time |

**Akamai HVO application:** the first ABSM campaign instance is documented in [02-akamai/](../02-akamai/) with territory = DACH, product = Zero Trust (Guardicore/EAA), vertical = financial services. The universal template above produces the structure. The Akamai instance fills it with company-specific research and personalized assets.

---

## Common failure modes

**Referral passing disguised as co-selling.** The partner sends a name over the fence. The manufacturer's sales team takes it from there. The partner has no visibility into deal progress, no involvement in the sales cycle, and no influence credit. This is a referral program, not co-selling. It produces low conversion because the partner's trust and context are lost at handoff.

**Deal registration as bureaucracy.** Approval takes a week. The form asks for 15 fields the partner does not have yet. Conflict resolution is opaque. Partners stop registering. Unregistered deals mean invisible pipeline and broken attribution. The fix: 5 required fields maximum on first registration. 24-hour approval SLA. Transparent conflict resolution with default-to-partner policy.

**Account mapping as a one-time exercise.** The team runs one account mapping session, produces a spreadsheet, and never revisits it. Accounts change. Contacts change. Competitive landscape changes. Account mapping is a recurring activity (quarterly minimum) with a living output, not a project with a deliverable.

**No separation of sourced vs influenced.** All partner-touched revenue goes into one bucket. Finance cannot disaggregate. The result: the partner program gets credit for influenced revenue it did not earn (inflating the number) and misses credit for sourced revenue it did earn (undervaluing the most expensive motion). Separate pipelines, separate attribution, separate reporting.

**ABSM without commitment.** A company launches an ABSM campaign with the right templates but does not commit the research time, the personalization effort, or the follow-up discipline. The emails are generic. The business cases are templates with names swapped. The stakeholder mapping is guesswork. ABSM at half effort produces worse results than no ABSM at all because it burns the target account list.

---

## Diagnostic questions

1. Do you have a deal registration process? What is the average approval time? What percentage of partner deals are registered?
2. Do you have joint business plans with your top partners? How often are they reviewed?
3. When was the last time you ran account mapping with a partner? What did you do with the output?
4. Can you separate partner-sourced revenue from partner-influenced revenue in your CRM today?
5. What is the win rate on co-sold deals versus direct-only deals? Do you track this?
6. How do you resolve deal conflicts between partners and direct sales?
7. Have you ever run an account-based campaign jointly with a partner? What was the scope and result?
8. Do your direct sales reps receive commission credit on partner-influenced deals?
9. How do you decide which accounts to co-sell versus which to leave to the partner?
10. What is your pipeline coverage ratio on partner-sourced opportunities?

---

## Intervention library

### Play: deal registration overhaul

- **Applicability:** companies with no registration process or a process that takes >48 hours. Foundation for any co-sell motion.
- **Description:** implement PRM-based deal registration with 5 required fields (account name, contact name, estimated value, expected close date, partner company). Automatic duplicate check. 24-hour approval SLA. Default-to-partner conflict resolution. CRM integration creating partner-attributed opportunities on approval. Track registration volume, approval time, and conversion rate from Day 1.
- **Source:** Rework 2026 guide: high registration-to-close rates correlate with partner trust and program health.
- **Lead time:** 2-4 weeks for PRM configuration. Impact on pipeline visibility immediate.

### Play: account mapping activation

- **Applicability:** companies that have never conducted formal account mapping or did it once and stopped.
- **Description:** select top 5 partners by revenue. Run account mapping using privacy-preserving overlap matching. Identify overlap, whitespace, and competitive displacement accounts. Build shared target account list. Feed into JBP. Repeat quarterly. [P-05] [P-43]
- **Source:** Bob Moore (Ecosystem-Led Growth): Account Mapping Matrix is the base artifact. Crossbeam architecture for privacy-preserving matching.
- **Lead time:** 2 weeks per partner for first mapping. Quarterly thereafter.

### Play: attribution model implementation

- **Applicability:** companies that cannot separate partner-sourced from partner-influenced revenue. The play that makes the partner program financially visible.
- **Description:** define taxonomy (partner type, motion, influence role, influence event). Instrument CRM with required fields and picklists. Enforce evidence-based influence logging. Implement automated sourced attribution from deal registration. Build reporting dashboard: pipeline, win rate, ACV, cycle time by partner, motion, and type. Run weekly unattributed opportunity audit.
- **Source:** Pedowitz Group: SaaS client increased partner-sourced pipeline by 38% and reduced credit disputes by 72% in 90 days after implementing structured attribution.
- **Lead time:** 4-6 weeks for system implementation. First clean data within one quarter.

### Play: ABSM sprint launch

- **Applicability:** companies at Professional maturity with co-sell infrastructure in place (deal registration, account mapping, attribution), looking to pursue high-value accounts with surgical precision. ABSM is not a replacement for regular co-sell. It is an additional stream for strategic accounts.
- **Description:** run the full 6-stage ABSM pipeline described in this document. Scope: 1 territory, 1 product, 1 vertical, 3 target accounts. Joint execution with one partner. Sprint duration: 8-12 weeks. Total output: 32 artifacts. Requires dedicated resource commitment from both manufacturer and partner for the sprint duration.
- **Source:** ABSM pipeline methodology. MEDDPICC framework for deep intel. GE/McKinsey matrix for account prioritization.
- **Lead time:** 2 weeks for Stage 0 (context). 2 weeks for Stages 1-2 (targeting and intel). 2 weeks for Stages 3-4 (strategy and execution). 2 weeks for Stage 5 (infrastructure and launch). 8 weeks total.

### Play: co-sell incentive alignment

- **Applicability:** companies where direct sales reps view partners as commission competition.
- **Description:** restructure compensation to include partner-influenced deals. Direct reps receive full commission on deals where a partner provided sourcing or material influence. Partner influence is logged through the attribution system. This eliminates the zero-sum dynamic. The cost is higher commission payout on some deals. The benefit is higher win rates, shorter cycles, and larger deal sizes on co-sold opportunities. Net positive. [P-06] [P-11]
- **Source:** Bob Moore: Bombora dedicated reps for channel partners, Procore internal accountability.
- **Lead time:** 90 days (requires sales leadership sign-off and comp plan revision).

---

## RACI within the stage

| Activity | Channel / partner ops | Partner manager | Sales leadership | Partner |
|---|---|---|---|---|
| Deal registration system management | R, A | I | I | R (submits registrations) |
| Conflict resolution | R, A | C | A (escalation) | I (receives decision) |
| Joint business plan creation | C (template) | R, A | C (targets) | R (co-creates) |
| Account mapping execution | R, A (data platform) | R (partner coordination) | I | R (provides account data) |
| Pipeline review (monthly) | C (reporting) | R, A | C | R (participates) |
| QBR (quarterly) | C (data) | R, A | R (executive sponsor) | R (executive participation) |
| Attribution reporting | R, A | I | I (consumer) | I |
| ABSM sprint: Stages 0-3 | R, A (research and strategy) | C (partner coordination) | I | C (local intel, validation) |
| ABSM sprint: Stage 4 | R, A (content creation) | C | I | R (delivery, outreach) |
| ABSM sprint: Stage 5 | R, A (infrastructure) | C | I | R (CRM hygiene, reporting) |

**RACI variant: companies without dedicated partner operations**

In pre-scale companies, the partner manager absorbs operations responsibilities. Account mapping runs on spreadsheets. Deal registration runs through a shared form. ABSM is not feasible without dedicated research and content capacity. Regular co-sell (deal registration, JBP, monthly pipeline review) is achievable with one person. ABSM requires either a second resource or external support.

---

## Tool requirements

| Category | Requirement for Co-sell | Evaluation criteria |
|---|---|---|
| PRM | Deal registration with automated duplicate check, approval workflow, conflict resolution, and CRM sync | Registration-to-opportunity automation, SLA tracking, conflict audit trail, partner portal self-service |
| Ecosystem ops / data mapping | Privacy-preserving account mapping. Overlap, whitespace, and competitive displacement identification. | Matching accuracy, data security, CRM integration, ability to run recurring mapping on schedule [P-43] |
| CRM | Partner-attributed opportunity tracking. Separate pipeline for partner-sourced, influenced, and co-sold deals. Attribution fields and influence event logging. | Partner object, deal registration object, influence event subtype, role-weighted split on junction objects, reporting parity with direct pipeline |
| Analytics / BI | Co-sell dashboard: pipeline by partner, win rate comparison (co-sold vs direct), ACV and cycle time by motion, MDF ROI, ABSM campaign performance | Real-time updates, partner-facing dashboard option, finance-ready reporting format |
| Marketing automation | ABSM email sequence delivery, personalized landing page hosting, campaign performance tracking | Personalization depth, deliverability, A/B testing, integration with CRM for attribution |

---

## Evidence

Principles from `appendix/evidence-library.md` that primarily apply to this stage:
- P-05 (Account Mapping Matrix is the base artifact of ecosystem-led growth)
- P-06 (partner data must pierce the veil and reach every customer-facing role)
- P-07 (partner is a strategic counterparty with multi-level touchpoints)
- P-11 (joint value: both earn more together than separately)
- P-35 (no random acts of marketing: every co-sell dollar tied to measurable outcome)
- P-41 (performance management is bidirectional: QBR as two-way conversation)
- P-43 (Venn-diagram transparency without raw list exchange)
- P-47 (trust > contract: deal registration protects trust)

---

## Research refresh layer

Space for deep research agent output when available:

- Latest developments in co-selling (2024-2026): AI-powered account matching, automated mutual action plans, multi-partner deal orchestration, ecosystem marketplaces as co-sell infrastructure
- Best practices: top 3 companies executing Co-sell at World-class level. Candidates: Bombora (3.5x higher close rate through channel co-sell, 2.5x lower churn), Procore (internal accountability driving partner involvement in forecasting), AWS (partner connections enabling multi-partner co-sell at scale)
- ABSM evolution: AI-driven research automation, predictive account scoring, real-time intent signals, personalization engines
- Future outlook: where co-selling is heading in 2-3 years (ecosystem-first GTM, multi-cloud partner co-sell, AI agents as ABSM researchers)
- Confidence score per data point (high/medium/low based on source quality)

Agent output will be appended here when Mission 1 executes. See [research-agent/00-agent-spec.md](../research-agent/00-agent-spec.md).
