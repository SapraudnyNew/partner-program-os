# Partner Growth Method OS: Architecture and Sprint Plan


**Client:** Alex M.
**Date:** May 15, 2026
**Sprint:** 2 days (May 15-16)
**Status:** Architecture frozen. Execution begins immediately.
**Definition of done:** Method complete + Akamai HVO ready to send.


---


## Decision Log (7 rounds, 21 answers)


### Round 1: Scope and boundary


| # | Decision | Answer |
|---|----------|--------|
| 1 | Sprint scope | Method + Akamai HVO only. BEGE frozen. CrewAI discarded as deliverable. |
| 2 | ABSM positioning | Execution skill inside Stage 1 (Recruit) and Stage 4 (Co-sell) only. |
| 3 | Primary reader | CEO / GM (strategic altitude, not operational process maps). |


### Round 2: Method architecture


| # | Decision | Answer |
|---|----------|--------|
| 4 | Document structure | Hub and spoke + layered. One overview doc (CEO altitude) + 7 standalone stage docs (Head of Channel depth), each layered internally. |
| 5 | Diagnostic tool | Maturity model (3 levels) where level 3 = gold standard. Binary clarity inside each level. Gap = roadmap. |
| 6 | Evidence base | Books (8-book corpus) + deep research agent. Agent runs two missions: (a) enhance method per stage with latest developments, (b) company-specific research per HVO target. |


### Round 3: ABM and company intake


| # | Decision | Answer |
|---|----------|--------|
| 7 | ABM artifact in Stage 1 | Full TAS: Ideal Partner Profile + scoring matrix + GE/McKinsey 9-box prioritization. |
| 8 | Company intake questionnaire | Modular: 10-question strategic core + optional deep modules (PESTEL, competitive, value chain). |
| 9 | Research execution model | Fully automated: research agent scrapes, fills, produces draft report with confidence scores. Human validates. (Sprint delivers spec + output template. Agent build = week 2.) |


### Round 4: Akamai HVO


| # | Decision | Answer |
|---|----------|--------|
| 10 | Target role | Both paths documented: warm referral (ADR-006, Senior Manager entry) + direct approach (VP/Director level) as fallback. |
| 11 | HVO hook | Partner program diagnosis: current maturity score vs gold standard, gap report. |
| 12 | Method reveal | Method overview (1 page) + Akamai diagnosis (2 pages) + proof metrics (half page). Full method stays behind the curtain. |


### Round 5: Maturity model


| # | Decision | Answer |
|---|----------|--------|
| 13 | Granularity | 3 levels per stage: basic, professional, world-class. |
| 14 | Level definition | Dual: capabilities define the level (what you have), KPIs measure performance at that level (how well it works). |
| 15 | Output format | Dual: scorecard table (working tool) + spider/radar chart (executive visual). |


### Round 6: Deliverable packaging


| # | Decision | Answer |
|---|----------|--------|
| 16 | Vendor/tool coverage | Category map + evaluation criteria per stage. Vendor-neutral. No named tool recommendations. |
| 17 | Delivery format | Markdown as source of truth in repo. PDF as leave-behind format. |
| 18 | Spider chart | Static in PDF + interactive HTML as follow-up demo artifact. |


### Round 7: Execution plan


| # | Decision | Answer |
|---|----------|--------|
| 19 | Day 1 priority | Method first, all 7 stages to depth, then Akamai. |
| 20 | Work mode | Forge produces full drafts. Alex reviews async. One revision pass at the end. |
| 21 | Definition of done | End of Day 2: method complete + Akamai HVO ready to send (done-done). |


---


## Architecture


### Three-layer model


Layer 3: HVO Wrapper - Applies Layer 1 + Layer 2 output to produce an executive value letter for a specific employer. Akamai is the first instance. Format: method overview (1pg) + diagnosis (2pg) + proof (½pg)


Layer 2: Playbook Engine - Skills that instantiate the method per target company. ABM/TAS skill (Stage 1 + Stage 4), research agent spec, intake questionnaire, diagnostic scorecard, spider chart.


Layer 1: The Method - 7 lifecycle stages, vendor-agnostic, book-sourced. Maturity model (3 levels × 7 stages). Tool landscape (category map + evaluation criteria).


### Updated repo structure


partner-program-os/
- 00-decisions/ (ADR-001 through ADR-007 existing + ADR-008 new)
- 01-method/
  - 00-method-overview.md (CEO-level hub)
  - 01-recruit.md (with ABM/TAS skill)
  - 02-onboard.md
  - 03-enable.md
  - 04-cosell.md (with ABM partner campaign skill)
  - 05-deliver.md (EXISTS)
  - 06-renew.md
  - 07-expand.md
  - maturity-model/ (framework + scorecard + spider chart)
  - tool-landscape/ (category map + evaluation criteria)
  - intake/ (core questionnaire + deep modules)
  - research-agent/ (spec + output template)
  - appendix/ (evidence library EXISTS)
- 02-akamai/
  - 00-context.md (EXISTS)
  - 01-hvo-warm-referral.md
  - 02-hvo-direct-approach.md
  - 03-diagnosis-scorecard.md
  - 04-talking-points.md (EXISTS)
  - 05-akamai-spider.html
- 03-boon-edam/ (FROZEN)
- prompts/
- docs/ (GitHub Pages, Phase 4)


### Method overview document (00-method-overview.md)


The CEO-level hub. One document that frames the entire system. Structure:


1. The partner growth problem (why most partner programs stall at basic)
2. The 7-stage lifecycle (one paragraph per stage, each links to standalone doc)
3. The maturity model (3 levels explained, visual of the scorecard)
4. The diagnostic process (how a company gets scored and receives its roadmap)
5. Proof (Boon Edam metrics, compressed)
6. Tool landscape summary (categories, not products)


Writing register: strategic. No process detail. Every sentence answers the CEO question: why should I care.


### Stage document template (01 through 07)


Each standalone stage doc follows this internal layered structure:


Stage N: [Name]
- Strategic intent: why this stage exists, what it solves
- Maturity levels: Basic / Professional / World-class with capabilities and KPIs
- The system: detailed operational content, process, roles, deliverables
- Tool requirements: category map for this stage, evaluation criteria, vendor-neutral
- Evidence: [P-NN] and [E-NN] references to appendix
- Research refresh layer: space for deep research agent output


### Maturity model: the 7x3 matrix


Basic / Professional / World-Class per stage:
- Recruit: ad hoc / systematic / ecosystem-led
- Onboard: manual / standardized / automated + personalized
- Enable: reactive / programmatic / self-service + certified
- Co-sell: opportunistic / structured / data-driven + co-invested
- Deliver: inconsistent / quality-assured / partner-autonomous
- Renew: passive / managed / predictive
- Expand: none / account-planned / portfolio-orchestrated


Each cell: 3-5 capability checkpoints + 2-3 KPIs with thresholds.


### ABM/TAS skill (Stage 1: Recruit)


1. Ideal Partner Profile template
2. Scoring matrix (weighted criteria, 1-5 scale)
3. GE/McKinsey 9-box prioritization
4. Target Account List output


### ABM partner campaign skill (Stage 4: Co-sell)


1. Campaign brief template
2. Folder structure: TAS / Partner Account Plans / Strategy / Campaign / Execution
3. Joint pipeline management framework
4. Campaign measurement dashboard spec


### Company intake: 10-question strategic core


1. What is your company's core value proposition?
2. What products/services do you sell through partners today?
3. How many active partners do you have and in which categories?
4. What percentage of revenue comes through partner channels?
5. What is your current partner onboarding process?
6. How do you enable partners to sell (training, content, tools)?
7. What co-selling or co-marketing do you do with partners?
8. How do you measure partner performance today?
9. What is your biggest partner program pain point?
10. Where do you want the partner program to be in 12 months?


Optional deep modules: PESTEL, Competitive landscape, Value chain, Tech stack, Financial model.


### Tool landscape: category map


PRM, Ecosystem ops/data mapping, CRM, Marketing automation, LMS, Deal registration/CPQ, Analytics/BI, Collaboration - each with evaluation criteria and relevant lifecycle stages.


### Akamai HVO structure (3.5 pages)


Page 1: method overview. Pages 2-3: Akamai diagnosis (maturity scores, spider chart, top 3 gaps). Page 3.5: proof metrics (Boon Edam results + CTA).


Warm referral version: Senior Channel Marketing Manager framing.
Direct approach version: VP/Director Partnerships EMEA framing.


---


## Frozen 2-day sprint plan


### Day 1: the method


D1-1 (90 min): 00-method-overview.md
D1-2 (60 min): maturity framework + scorecard
D1-3 (90 min): 01-recruit.md (with ABM/TAS)
D1-4 (60 min): 02-onboard.md
D1-5 (60 min): 03-enable.md
D1-6 (90 min): 04-cosell.md (with ABM campaigns)
D1-7 (45 min): 06-renew.md
D1-8 (45 min): 07-expand.md


Day 1 total: ~8.5 hours.


### Day 2: Akamai HVO + packaging


D2-1 (90 min): Akamai research
D2-2 (60 min): Diagnosis scorecard
D2-3 (90 min): HVO warm referral
D2-4 (45 min): HVO direct approach
D2-5 (60 min): Spider chart (interactive + static)
D2-6 (45 min): PDF export
D2-7 (60 min): Revision pass


Day 2 total: ~8.5 hours.


### Week 2 backlog


- Company intake questionnaire
- Research agent spec and build
- Tool landscape standalone document
- BEGE rollout map
- GitHub Pages publish
- Interactive React dashboard
- PDF pipeline automation


---


## Success criteria


1. CEO reads overview and sees a system
2. Maturity model creates urgency
3. Akamai HVO makes a specific diagnosis
4. Spider chart makes the gap visible in one second
5. Proof metrics are concrete and verifiable
6. Package creates deal debt
7. Alex adapts HVO for new target in under 2 hours


Rate target: 8+ on Forge scale before deployment.


Architecture frozen. ADR-008. No structural changes during sprint.