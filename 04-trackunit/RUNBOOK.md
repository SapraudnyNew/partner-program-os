# RUNBOOK: Trackunit Branch of Partner Program OS

> **Purpose:** a self-sufficient instruction set for a server-side agent (Claude Code or similar)
> to build and deploy the Trackunit application project inside this repo using a system of
> parallel subagents. A fresh agent with this file, repo access, and web access must be able
> to reproduce the whole build end to end.

---

## 0. MISSION

Build a job-application leave-behind site for:

- **Candidate:** A. Marushevsky, Amsterdam (see `MASTER_HANDOVER.md` for locked bio decisions)
- **Target role:** Head of Partnerships: Integrations & Applications, Trackunit (Amsterdam / global)
- **Job posting:** https://careers.trackunit.com/jobs/7782454-head-of-partnerships-integrations-applications
- **Platform context:** IrisX: Trackunit's construction operating data platform. The role owns
  third-party integrations (ERP, rental management, fleet, ConTech, AI platforms), a cross-functional
  pod, the integration partner pipeline, and **IrisX credit consumption** as the primary commercial metric.
- **Live URL target:** https://sapraudnynew.github.io/partner-program-os/trackunit/

Deliverables:
1. Site branch at `docs/trackunit/` (Memo + 3 perspectives + interactive artifacts)
2. Reworked CV (`04-trackunit/cv/`) + Google Doc copy
3. Hiring-manager outreach pack (`04-trackunit/outreach/`): email note, LinkedIn note + first message, application-form text
4. System bookkeeping: STATE.md entry, ADR-012, `prompts/prompt-trackunit.md`

## 1. NON-NEGOTIABLE RULES (inherited + branch-specific)

| # | Rule |
|---|---|
| R1 | Name is **A. Marushevsky** everywhere. Never "Alex M." or full first name in site copy. |
| R2 | English only. Direct voice, no corporate buzzwords, zero em-dashes in new copy. |
| R3 | Every research artifact carries the caveat: "first pass from public sources, presented to demonstrate methodology." |
| R4 | **Isolation:** no page under `docs/trackunit/` links to Akamai pages or to the site root. The root `index.html` gets NO link to `/trackunit/`. Top-nav logo inside the branch points to `trackunit/index.html`. |
| R5 | Design system: reuse `docs/assets/css/main.css` + `docs/assets/js/sidebar.js` as-is. No redesign. |
| R6 | Tone toward Trackunit's existing product (marketplace, dev portal): **opportunity map**, not audit. Frame findings as "what is already strong + where the leverage is." Never a defect list. |
| R7 | IrisX credit pricing/mechanics are not public. Any consumption model uses clearly labeled assumptions. |
| R8 | People research (hiring manager, leadership): names, titles, and public facts are written openly in artifacts. Verify every name with a second independent source before publishing. |
| R9 | Positioning stands on four legs: (a) construction insider (Hilti, Boon Edam), (b) P&L commercial operator (24% ROS, 150% budget), (c) builder of partner programs from scratch (+55% YoY), (d) AI-native operator (this site itself is the proof). |
| R10 | Facts about the candidate come from `04-trackunit/cv/` sources and MASTER_HANDOVER. Never invent numbers. |

## 2. REPO LAYOUT FOR THIS BRANCH

```
04-trackunit/                  ← sources (not published)
├── RUNBOOK.md                 ← this file
├── research/outputs/          ← subagent research digests (md)
├── method/                    ← integration lifecycle method (md sources)
├── partner-mapping/           ← landscape + dossiers (md sources)
├── execution/                 ← first-five plan, pod plan, opportunity map (md sources)
├── cv/                        ← reworked CV
└── outreach/                  ← HM note (email / LinkedIn / application form)

docs/trackunit/                ← published site (GitHub Pages serves /docs on main)
├── index.html                 ← Memo (motivation letter)
├── method/                    ← Perspective 1 (+ spider-chart.html)
├── partner-mapping/           ← Perspective 2 (+ landscape.html filterable matrix)
└── execution/                 ← Perspective 3 (+ credit-dashboard.html)
```

Build tool: `tools/md2html_trackunit.py` (a parameterized sibling of `tools/md2html.py`,
scans only `docs/trackunit/**`, emits Trackunit nav/sidebar, uses `../assets/` CSS with
correct depth prefixes).

## 3. PHASE PLAN (execute in order; parallelize inside phases)

### Phase 1: Research (parallel subagents, ~6 streams)

Every stream writes a markdown digest to `04-trackunit/research/outputs/<stream>.md`
with a Sources list of URLs. Streams:

| Stream | Prompt core | Output file |
|---|---|---|
| company | Trackunit strategy, IrisX Acceleration, business model, credits, investors (Goldman Sachs Asset Mgmt, GRO, Hg), scale, offices, culture ("eliminate downtime", human-centric) | `company.md` |
| platform | developers.trackunit.com deep dive: IrisX APIs (GraphQL, Rental API, Time Series/PromQL), connectors, marketplace, "Works With Trackunit" program, sandbox, AI-agent direction | `platform.md` |
| eco-erp-rental | ERP (SAP, Oracle, MS Dynamics, IFS) + rental management systems (Point of Rental, MCS, inspHire, Wynne/RentalMan, Baseplan, Systematix...): candidates for the landscape with integration-relevant facts | `eco-erp-rental.md` |
| eco-contech-ai | ConTech (Procore, Autodesk Construction Cloud, Hilti ON!Track, Fieldwire, PlanRadar...), fleet mgmt, AI platforms/agents in construction: same format | `eco-contech-ai.md` |
| eco-oem | OEM layer: existing Trackunit OEM relationships (e.g. via press: Manitou, JLG, Hiab, Skyjack...) and OEM software ecosystems | `eco-oem.md` |
| people | Hiring manager hunt: VP of Platform at Trackunit (role reports there), plus adjacent leaders (CPTO/CTO, Head of Partnerships, VP Product). Use LinkedIn-capable people search (Apify actor if available; otherwise Exa `category:people`). Deliver 2-3 most-likely addressees with evidence and confidence levels | `people.md` |
| marketplace-bench | Marketplace/dev-portal best practice benchmark: Procore App Marketplace, Autodesk App Store, Salesforce AppExchange, Shopify: what makes ISV activation low-touch; distill levers applicable to IrisX | `marketplace-bench.md` |

**Verification pass (mandatory):** after streams return, run 2-3 verifier subagents that
adversarially re-check: (a) every person name+title, (b) every claimed Trackunit partnership,
(c) every product/API claim used later in copy. Anything unverified gets softened or cut.

### Phase 2: Content (markdown, parallel writers after research)

1. `method/`: adapt the universal 7-stage method (`01-method/`) to the **integration partner
   lifecycle**: Source → Qualify → Scope → Build → Launch → Adopt → Scale. Keep the 3-level
   maturity model (21 checkpoints) re-worded for a platform/integrations program.
2. `partner-mapping/`: landscape of 30-40 players across 6 categories (ERP, rental, fleet,
   ConTech, AI, OEM), scored on 6 dimensions (adapt IPP: Strategic Fit, Market Reach,
   Technical Readiness, Commercial Model Fit, Consumption Potential, Recruitability).
   Disposition per player: Pursue / Contain / Monitor / Drop. Then **First Five** dossiers
   (deep profiles with hooks) for the top Pursue candidates.
3. `execution/`: three artifacts:
   - **First Five Integrations plan:** per partner: why, scoping summary, commercial model,
     path from first call to live integration and credit consumption, 90-day milestones.
   - **Pod operating plan (90 days):** weekly cadence, interlocks with P&E and GTM,
     roles (PM, Platform Engineer, Field Marketing, Regional Managers), decision rights, KPI tree
     rooted in credit consumption.
   - **Marketplace opportunity map:** what is already strong on developers.trackunit.com and
     the marketplace + 5-7 leverage moves for low-touch ISV activation (constructive frame, R6).
4. `index` memo: the motivation letter. Hook: builder's bridge (Hilti construction sites,
   Boon Edam entrances → the machines on the same sites, now the data platform above them).
   Three perspectives + 30/60/90 + the AI-speed angle. Under 1 page of screen reading.

### Phase 3: Site build

1. Write `tools/md2html_trackunit.py`: same template pattern as `md2html.py`, but:
   nav = Memo / Method / Partners / Execution (all inside `trackunit/`); sidebar mirrors the
   Trackunit tree only; CSS prefix accounts for the extra `trackunit/` directory level;
   logo href = branch index. Footer keeps the public-sources caveat.
2. Interactive artifacts (adapt existing ones):
   - `method/spider-chart.html` ← from `docs/method/spider-chart.html` (7 axes renamed to the
     integration lifecycle stages; no company scores).
   - `partner-mapping/landscape.html` ← from `docs/partner-mapping/dach-landscape.html`
     (filterable by category and disposition).
   - `execution/credit-dashboard.html` ← from `docs/absm-sprint/05-infrastructure/kpi-dashboard.html`
     (funnel: pipeline → scoped → live integrations → active accounts → credit consumption; labeled assumptions).
3. Run the converter, then **link-check**: no `href` under `docs/trackunit/` may resolve outside
   `docs/trackunit/` except `../assets/...` (CSS/JS only). Root index must not reference trackunit.

### Phase 4: CV + outreach

- `cv/CV_Trackunit.md`: deep rework of the master CV toward the JD language (ecosystem,
  integrations, platform consumption, marketplace, cross-functional pod leadership). Same facts,
  platform frame. Headline: partnerships/ecosystem leader, not channel marketer.
- `outreach/hm-note.md`: email note in the Akamai-note style (short, hook, three perspectives,
  links, CV attached separately). Addressee per `people.md` findings.
- `outreach/linkedin.md`: 300-char connection note + first message after connect.
- `outreach/application-form.md`: short text for the careers-site free-text field
  (Trackunit says "don't waste time on cover letters": 5-7 sentences, link as the hook).
- Create Google Docs copies of CV and HM note in the user's Drive (if Drive tooling is available).

### Phase 5: Bookkeeping

- Append a session entry to `STATE.md` (format: `## SESSION YYYY-MM-DD · trackunit-branch`).
- Write `00-decisions/adr-012-trackunit-branch.md`: second campaign inside one repo, isolation
  rules, reuse of design system, runbook-driven build.
- Write `prompts/prompt-trackunit.md`: continuation prompt for future sessions (style of existing prompts).

### Phase 6: Deploy + verify

1. Commit on the working branch, push with retries (2s/4s/8s/16s backoff).
2. Open PR to `main`, merge (Pages serves `/docs` from main). Merge permission for this build
   was granted explicitly by the user on 2026-07-02.
3. Wait for Pages build, then verify over HTTP: `/trackunit/`, one page per section, all three
   interactive artifacts → HTTP 200 and correct render.
4. Re-run the isolation check against the live site.
5. Report: live links, PR link, Google Doc links, HM addressees found.

## 4. QUALITY CHECKLIST (before merge)

- [ ] **Anti-slop pass over every new md/html file (mandatory, dedicated agent):**
      remove AI-tell phrasing (delve, leverage, seamless, robust, holistic, game-changer,
      "isn't just X, it's Y", "in today's fast-paced world", empty rule-of-three chains,
      hype adjectives), kill every em-dash and en-dash in copy, confirm 100% of published
      text is English, prefer concrete verbs and numbers over adjectives
- [ ] Every page renders with sidebar + nav, no 404 links inside the branch
- [ ] No link from `/trackunit/**` to Akamai content or root (except shared `/assets/`)
- [ ] Root index unchanged except none; no `/trackunit/` link added
- [ ] Names/titles of real people verified by 2+ independent sources
- [ ] Public-sources caveat present on memo + all research-derived pages
- [ ] No em-dashes in new copy; name always "A. Marushevsky"
- [ ] Credit model assumptions explicitly labeled
- [ ] Opportunity map contains zero defect-list phrasing
- [ ] CV facts identical to master CV facts (frame changes, numbers do not)

## 5. FAILURE MODES

- **LinkedIn tooling (Apify) unavailable** → fall back to Exa people search + press releases; lower confidence, mark it.
- **Google Drive MCP down** → keep markdown in repo, tell the user to copy manually.
- **Pages build slow** → poll up to ~10 min before declaring failure; check Actions "pages build and deployment".
- **Fact unverifiable** → cut or soften to "reportedly"; never ship a shaky claim about a named person.
