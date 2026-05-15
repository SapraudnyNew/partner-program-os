# Deep Research Mission: Akamai Company Intelligence Dossier

## Mission identity

You are an executive research analyst preparing a confidential intelligence briefing for a senior commercial hire at Akamai Technologies. The dossier must operate at consulting-grade depth, comparable to a McKinsey company tear-down or a buy-side investment memo.

## Available tools

You have access to two Exa tools. Use them aggressively and in this priority order:

1. **`web_search_exa`** - real-time neural search. Use for discovery, broad scans, and finding sources you do not yet know exist. Neural search rewards descriptive queries over keyword strings. Write queries the way you would phrase the question to a colleague, not the way you would type into Google.

2. **`web_fetch_exa`** - extracts full content from specific URLs. Use after `web_search_exa` surfaces a relevant URL. Snippets are not enough. Fetch the full page for any source you cite.

Use both tools in cycles: search broadly, fetch the most promising hits in full, extract data, search again with refined queries informed by what you learned. Expect 80-150 tool calls across this mission. If you are at 30 tool calls and 5 pages of output, you are underperforming.

## Hard requirements

This is non-negotiable:

- **Minimum output length: 30 pages of dense analytical prose plus tables and source citations.** Less than 30 pages means the mission is incomplete. Do not summarize. Do not compress. Do not abbreviate sections to save tokens.
- **Minimum 80 cited sources across the dossier.** Each citation includes full URL and date accessed.
- **Refuse-to-summarize protocol:** if at any point you feel tempted to write "for the sake of brevity" or "in summary" or "due to length constraints" - stop. Continue researching. The user explicitly wants length and depth.
- **Sectioned output: produce 6 separate markdown files.** Do not concatenate. Each file is a standalone document with its own header, sources list, and confidence assessment.
- **Every critical claim cross-referenced against minimum 2 independent sources.** Single-sourced claims marked with ⚠️ inline.
- **Distinguish four data quality tiers throughout:**
  - **Confirmed:** 2+ independent reputable sources
  - **Single-sourced:** one source only, ⚠️ marker
  - **Inferred:** logical extension from data, 🧠 marker
  - **Blind spot:** cannot verify, ❌ marker with explanation

## Tone of output

Analytical, source-cited, no marketing language. Treat this as an internal investment memo, not a sales pitch. Active voice. No corporate fluff. Specific facts and named entities throughout. No "innovative," no "game changer," no "synergy."

---

## File 1: corporate-fundamentals.md (target: 5-7 pages)

### Section 1.1: Financial profile

Use `web_search_exa` for:
- "Akamai Technologies Q1 2026 earnings report revenue segmentation"
- "Akamai security business revenue growth fiscal year 2025 breakdown"
- "Akamai stock performance year to date 2026 analyst price targets"
- "Akamai 10-K filing fiscal 2025 business segments"

Then `web_fetch_exa` on:
- Latest Akamai investor relations earnings releases
- Most recent 10-K and 10-Q filings
- Analyst reports cited in financial press

Document:
- Total revenue last 4 quarters, YoY growth per quarter
- Revenue segmentation: Security, Delivery (CDN), Compute. Express as percentages and absolute USD.
- Isolate security revenue: total, YoY growth, and sub-segment if disclosed (Guardicore, API Security, App and API Protector, Bot Manager, Account Protector, MFA, EAA)
- Operating margin, free cash flow, cash position, debt structure
- Recent capital actions: buybacks, dividends, refinancing, M&A spending
- Stock performance YTD 2026, key analyst price targets, consensus rating

### Section 1.2: Strategic positioning

Use `web_search_exa` for:
- "Akamai Compute strategy investor day 2025 2026"
- "Akamai security growth engine Tom Leighton statements"
- "Akamai partner first repositioning 2025 channel"
- "Akamai acquisition Guardicore Noname integration outcomes"

Then `web_fetch_exa` on:
- Akamai investor day presentations
- CEO Tom Leighton's recent public statements (earnings calls transcripts via Seeking Alpha, Motley Fool, AlphaStreet)
- Akamai blog posts on strategy
- Industry analyst commentary (Gartner, Forrester, IDC where freely available)

Document:
- Stated 2026-2028 strategy from earnings calls, investor day, 10-K
- The Compute pivot: milestones achieved, analyst skepticism, capital allocation
- Security business strategy: growth engine vs leg of three-legged stool
- M&A activity: Guardicore (2021), Noname (2024), any others since with integration status
- Divestitures, business line shutdowns, geographic retrenchments

### Section 1.3: Leadership and governance

Use `web_search_exa` for:
- "Akamai CEO Tom Leighton tenure succession 2026"
- "Akamai CFO Ed McGowan capital allocation philosophy"
- "Akamai security business unit general manager"
- "Akamai EMEA VP channel partner 2026"

Then `web_fetch_exa` on:
- LinkedIn profiles surfaced by search
- Akamai leadership page
- Proxy statements for board composition
- Press releases announcing leadership changes

Document:
- CEO Tom Leighton: tenure, succession noise, public posture, recent communications
- CFO Ed McGowan: recent statements, capital allocation philosophy
- GM Security or equivalent (Zero Trust business unit head): name, LinkedIn, tenure
- VP Channel/Partner roles: global, EMEA, DACH if identifiable
- Board composition, recent changes, activist investor pressure if any

### Section 1.4: Recent moves and signals (last 12 months)

Use `web_search_exa` for:
- "Akamai press release 2026"
- "Akamai earnings call transcript Q4 2025 partner strategy"
- "Akamai leadership departure 2025 2026"
- "Akamai product launch Zero Trust 2026"

Document:
- Earnings call commentary trends across last 4 quarters (identify themes)
- Product launches and end-of-life announcements
- Strategic partnerships announced (hyperscaler agreements, GSI alliances)
- Press releases signaling direction
- Leadership departures or significant hires visible on LinkedIn

### Closing requirements for File 1

- Confidence assessment per subsection
- Full sources list with URLs and access dates
- Explicit blind spots identified

---

## File 2: dach-regional-intelligence.md (target: 6-8 pages)

### Section 2.1: DACH organizational footprint

Use `web_search_exa` for:
- "Akamai office Germany Munich Frankfurt headquarters"
- "Akamai Austria Vienna office location"
- "Akamai Switzerland Zurich Geneva office"
- "Akamai DACH country manager 2026 LinkedIn"
- "Akamai EMEA headquarters London"

Then `web_fetch_exa` on:
- Akamai careers page DACH listings
- LinkedIn company page for office locations
- German Impressum requirements pages (Akamai GmbH details)

Document:
- Office locations: Germany, Austria, Switzerland with addresses
- Country managers and DACH leadership: names, LinkedIn URLs, tenure
- Approximate headcount in DACH (triangulate from LinkedIn, press, job postings)
- Reporting structure: DACH → EMEA → global

### Section 2.2: DACH revenue and customer base

Use `web_search_exa` for:
- "Akamai DACH customer case study Germany"
- "Akamai Mittelstand customer reference"
- "Akamai Deutsche Bank Commerzbank financial services Germany"
- "Akamai industrial customer Germany automotive manufacturing"

Then `web_fetch_exa` on:
- Akamai case studies pages (filter for DACH)
- German trade press articles
- Conference speaker lists from BSI Kongress, it-sa Nürnberg, RSA Munich

Document:
- Disclosed DACH revenue or growth rates (likely sparse - flag as blind spot if so)
- Named DACH customers from case studies, press, conferences
- Industry concentration in DACH
- Recent DACH wins or losses if visible

### Section 2.3: DACH press and analyst coverage

Use `web_search_exa` for:
- "Akamai Handelsblatt 2025 2026"
- "Akamai Computerwoche Zero Trust Germany"
- "Akamai Heise Online security partner"
- "Akamai it-sa Nürnberg 2025 booth presentation"
- "Akamai BSI Kongress Germany cybersecurity"

Then `web_fetch_exa` on all surfaced German trade press articles.

Document:
- German-language press coverage last 12 months
- Analyst commentary specifically on Akamai DACH
- Conference presence: it-sa, BSI Kongress, RSA Munich

### Section 2.4: DACH regulatory exposure and positioning

Use `web_search_exa` for:
- "Akamai NIS2 compliance Germany Guardicore"
- "Akamai DORA financial services Zero Trust"
- "Akamai BSI certification C5 Germany"
- "Akamai NIS2 Umsetzung Germany channel partner"

Then `web_fetch_exa` on:
- Akamai NIS2 landing pages and whitepapers
- BfArM, BSI compliance documentation referencing Akamai
- German regulatory briefings citing Akamai

Document:
- How Akamai positions Guardicore against NIS2
- How Akamai addresses DORA for German/Austrian financial institutions
- German government certifications (BSI, C5) - confirmed or not
- DACH compliance messaging in marketing materials

### Section 2.5: DACH talent signals (last 12 months)

Use `web_search_exa` for:
- "Akamai jobs Germany site:akamai.com careers"
- "Akamai channel marketing Germany position 2026"
- "Akamai DACH hiring LinkedIn"
- "Akamai layoffs restructuring 2025"

Then `web_fetch_exa` on:
- Akamai careers portal (search all DACH listings)
- Glassdoor reviews filtered for Germany/Austria/Switzerland
- Kununu reviews (German equivalent of Glassdoor)
- LinkedIn job postings page for Akamai DACH

Document:
- Open job postings in DACH (count, role types, locations)
- Specifically channel marketing, channel sales, security specialist roles
- Recent DACH leadership hires or departures
- Glassdoor and Kununu sentiment from DACH employees

### Closing requirements for File 2

- Confidence assessment per subsection
- Full sources list
- Explicit blind spots

---

## File 3: cultural-and-operational-intelligence.md (target: 5-7 pages)

### Section 3.1: Hiring patterns (last 24 months global, 12 months DACH)

Use `web_search_exa` for:
- "Akamai layoffs 2024 2025 restructuring"
- "Akamai hiring trends headcount growth"
- "Akamai Compute investment hiring engineers"
- "Akamai security hiring sales 2026"

Document:
- Pace of headcount growth or contraction by business line
- Geographic shifts: which regions growing, which shrinking
- Function shifts: where the company is investing (sales, engineering, GTM, support)
- Layoff announcements, restructuring, RIFs

### Section 3.2: Internal communications style

Use `web_search_exa` for:
- "Tom Leighton LinkedIn post Akamai 2025 2026"
- "Akamai blog post partner first ecosystem"
- "Akamai threat report content marketing tone"
- "Akamai security blog Guardicore voice"

Then `web_fetch_exa` on:
- Akamai executive blog posts (last 20)
- Tom Leighton's LinkedIn activity
- Recent Akamai threat reports

Document:
- Tone of executive blog posts and LinkedIn
- How the company talks about partners publicly
- How the company talks about cybersecurity threats (technical depth vs FUD)
- How the company talks about its own people

### Section 3.3: Employee sentiment

Use `web_search_exa` for:
- "Akamai Glassdoor reviews 2025 2026"
- "Akamai Kununu Bewertung Mitarbeiter"
- "Akamai work culture review engineer Germany"
- "Akamai employee experience LinkedIn"

Then `web_fetch_exa` on:
- Glassdoor company page
- Kununu Akamai page
- Comparably or similar review aggregators

Document:
- Aggregate Glassdoor/Kununu scores and trends
- Recurring themes: management, compensation, work-life balance, growth
- DACH-specific themes
- LinkedIn signals: who is leaving Akamai and where they go

### Section 3.4: Recent organizational events

Use `web_search_exa` for:
- "Akamai office opening Germany 2025"
- "Akamai town hall all hands employee"
- "Akamai integration Guardicore Noname employees"
- "Akamai union labor Germany"

Document:
- Acquisitions and integration as reported by employees
- Office openings or closings
- Leadership town halls or all-hands themes if publicly reported
- Union or labor signals in DACH or elsewhere

### Closing requirements for File 3

- Confidence assessment
- Sources list
- Blind spots

---

## File 4: channel-marketing-organization.md (target: 6-8 pages)

This file is specific to the target role: Senior Channel Marketing Manager, DACH, Zero Trust security.

### Section 4.1: Who currently leads DACH channel marketing

Use `web_search_exa` for:
- "Akamai channel marketing manager Germany LinkedIn"
- "Akamai EMEA channel marketing director"
- "Akamai partner marketing DACH lead"
- "Akamai senior channel marketing manager DACH 2025 2026"

Then `web_fetch_exa` on:
- Every LinkedIn profile surfaced
- Akamai partner page leadership listings
- Conference speaker bios for Akamai DACH presenters

Document:
- Current DACH channel marketing manager or director: name, LinkedIn, tenure
- EMEA channel marketing leadership (the likely hiring manager skip-level)
- Recent departures or arrivals in this function

### Section 4.2: Channel marketing team composition

Use `web_search_exa` for:
- "site:linkedin.com Akamai channel marketing Germany"
- "site:linkedin.com Akamai partner marketing EMEA"
- "Akamai field marketing DACH security"
- "Akamai demand generation Germany Zero Trust"

Then `web_fetch_exa` on every relevant LinkedIn profile.

Document:
- Estimated DACH channel marketing headcount (LinkedIn search)
- EMEA channel marketing team size
- Adjacent roles in DACH: field marketing, demand gen, product marketing for security
- Build an org chart hypothesis

### Section 4.3: Recent DACH channel marketing activity

Use `web_search_exa` for:
- "Akamai webinar DACH Zero Trust 2025 2026"
- "Akamai partner event Germany Munich it-sa"
- "Akamai Guardicore campaign Germany 2026"
- "Akamai Partner Connect DACH launch communications"

Then `web_fetch_exa` on:
- Akamai event pages
- LinkedIn event posts
- DACH partner co-marketing announcements

Document:
- Webinars, events, MDF-funded campaigns visible publicly
- Partner Connect launch communications targeted at DACH
- Specific Guardicore campaigns in DACH
- Joint marketing activities with named DACH partners

### Section 4.4: Job posting analysis

Use `web_fetch_exa` on:
- https://jobs.akamai.com/en/sites/CX_1/jobs/preview/2855/
- Other Akamai Senior Channel Marketing Manager postings globally for comparison
- Akamai career site filtered for marketing roles

Use `web_search_exa` for:
- "Akamai senior channel marketing manager salary Glassdoor"
- "Akamai DACH channel marketing Levels.fyi"
- "Akamai Germany marketing compensation 2026"

Document:
- The specific posting: extract ALL responsibilities and requirements verbatim
- Comparison postings: what Senior Channel Marketing Manager means at Akamai elsewhere
- Reporting line if disclosed
- Salary band if available through aggregators

### Closing requirements for File 4

- Confidence assessment
- Sources list
- Blind spots

---

## File 5: risks-and-questions.md (target: 4-5 pages)

### Section 5.1: Strategic risks specific to the role

Synthesize Files 1-4 to identify:

- Is the partner-first repositioning stable or is leadership equivocating?
- Is Guardicore growing as expected or under pressure from Illumio and Palo Alto/CyberArk?
- Is the DACH region a growth or maintenance market for Akamai?
- Is the Senior Manager rank a stepping stone or a ceiling?
- What does the DACH channel marketing team's stability look like (turnover signals)?
- What does Akamai's commitment to channel investment look like across the next 12-18 months?

Each risk: 1-2 paragraphs of analysis backed by sources from previous files.

### Section 5.2: Open questions for the candidate

Based on the research, identify 7-10 specific questions only an informed candidate would ask in interview. These must:

- Challenge assumptions in the job description
- Reference specific competitive dynamics
- Reference specific named entities (people, partners, customers)
- Signal the candidate has read between the lines

### Section 5.3: Information gaps

Document:
- What could not be verified (explicit blind spots)
- What requires inside information
- What only the hiring manager can answer
- What requires actual data access (CRM, PRM, internal documents)

---

## File 6: master-summary.md (target: 3-4 pages)

NOT a summary of content. A meta-document that:

- Lists all 5 prior files with brief description (1 sentence each)
- Aggregates all sources across files (deduplicated master sources list)
- Provides confidence dashboard: which sections are high-confidence, which medium, which low
- Lists the top 10 most surprising findings from the research
- Lists the top 5 implications for the HVO and 90-day plan

---

## Final delivery instructions

When all 6 files are complete:

1. Verify total length across all files is minimum 30 pages.
2. Verify minimum 80 cited sources across the dossier.
3. Verify every critical claim has 2+ source citations or is flagged with ⚠️ / 🧠 / ❌.
4. Verify all 6 files have closing confidence assessments and blind spot identifications.
5. Output all 6 files in sequence in the chat: File 1 first, then File 2, etc.

If the executing chat is running out of context window, prioritize completing whichever file is in progress fully before terminating. Do not produce truncated files. If context runs out mid-mission, output what is complete and list which files remain.

## Critical reminder

The user has explicitly demanded depth and length. Resist any instinct to summarize, compress, or abbreviate. If you find yourself tempted to write "in summary" or "to keep this concise" - stop and continue the research instead.

Begin with File 1, Section 1.1. Execute `web_search_exa` immediately.
