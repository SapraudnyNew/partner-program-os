# REDESIGN BRIEF — Partner Program OS v2

> **Created:** 2026-05-19
> **Source:** 12 design decisions from elicitation session
> **Repo:** https://github.com/SapraudnyNew/partner-program-os
> **Live:** https://sapraudnynew.github.io/partner-program-os/
> **Workflow:** Chat 1 (Opus 4.7) → copywriting · Chat 2 (Opus 4.6) → HTML/CSS implementation · OpenClaw → merge

---

## WHAT CHANGED (problems with current site)

1. Homepage text is generic AI slop. Needs human voice, storytelling arc, short sentences.
2. Name wrong everywhere. **A. Marushevsky** (not "Alex M.")
3. No reading guide — visitor doesn't know the site has 78 files of depth
4. No executive summaries at top of perspective pages — McKinsey always does this
5. Raw .md files unreadable in browser (entanglement, pursue-five, targeting, strategy, etc.)
6. No sidebar navigation — can't see site tree
7. No back-navigation UX
8. CSS doesn't reference Akamai's visual language at all
9. Too much "I" / "me" in text — reads as self-promotional

---

## 12 LOCKED DECISIONS

| # | Decision | Answer |
|---|----------|--------|
| 1 | CSS direction | Show 2 variants (Akamai-inspired), pick best. Target: Akamai color palette + our clean spacing |
| 2 | MD rendering | Every .md → full .html with nav, styles, back-button |
| 3 | Sitemap/TOC | Collapsible sidebar on every page |
| 4 | Back navigation | Sidebar is sufficient (no separate breadcrumbs or back buttons) |
| 5 | Exec summary format | Bullet-list with anchor links at top of each perspective (McKinsey style) |
| 6 | MD content language | Keep as-is — German files stay German, English stays English |
| 7 | Sidebar behavior | Visible on desktop, hamburger on mobile (2026 standard) |
| 8 | Reading guide | Short block on homepage: 3 sentences explaining site depth |
| 9 | Workflow | This brief → Opus 4.7 (copy) → Opus 4.6 (code) → OpenClaw merge |
| 10 | Copywriting scope | Homepage + 3 perspective landing pages (4 pages total) |
| 11 | Name format | A. Marushevsky (short, professional) |
| 12 | Timeline | Ship today |

---

## DESIGN SYSTEM v2 — Akamai-Inspired Minimalism

### Color palette (derived from akamai.com)

```css
:root {
  /* Akamai core */
  --ak-blue: #009FDB;           /* Akamai primary — links, accents */
  --ak-blue-dark: #0077B5;      /* Hover state */
  --ak-navy: #0D2137;           /* Dark sections, nav, footer */
  --ak-navy-light: #132C46;     /* Card backgrounds in dark mode */
  
  /* Neutral palette */
  --ink: #1B2733;               /* Primary text */
  --ink-light: #4A5568;         /* Body paragraphs */
  --ink-muted: #718096;         /* Captions, metadata */
  --surface: #FFFFFF;           /* Page background */
  --surface-alt: #F7FAFC;       /* Alternating sections, card bg */
  --border: #E2E8F0;            /* Borders, dividers */
  --border-accent: rgba(0,159,219,0.2); /* Subtle blue borders */
  
  /* Semantic */
  --green: #38A169;             /* Success, warm-path */
  --amber: #D69E2E;             /* Warning, showcase */
  --red: #E53E3E;               /* Alert */
  
  /* Typography */
  --font-sans: 'DM Sans', -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  
  /* Spacing */
  --sidebar-width: 260px;
  --content-max: 820px;
  --page-max: 1200px;
}
```

### Typography rules

- **Headings:** DM Sans 700. No serif on headings (Akamai uses sans).
- **Body:** DM Sans 400, 16px/1.7, color: --ink-light
- **Code/data:** JetBrains Mono 400, 13px
- **No Source Serif 4** — dropping the serif. Akamai is entirely sans-serif. Cleaner.
- **Link style:** --ak-blue, no underline, underline on hover

### Layout principles

- White background, generous whitespace (Akamai uses tons of white space)
- Cards with subtle --border, 8px radius, no shadow (Akamai style — flat, not elevated)
- Section dividers: thin 1px --border lines
- Dark nav bar (--ak-navy) with white text — matches Akamai's top nav
- Footer: --ak-navy background

---

## SIDEBAR SPEC

Every page gets a collapsible sidebar showing the full site tree.

```
📄 Memo (homepage)
📁 Method
  ├── Overview (lifecycle + maturity)
  ├── Spider Chart
  └── Scorecard Template
📁 Partner Mapping
  ├── Overview (IPP + dispositions)
  ├── DACH Landscape (33 partners)
  ├── Pursue Five
  │   ├── Axians + Fernao
  │   ├── SVA Wiesbaden
  │   ├── ACP Gruppe
  │   ├── AVANTEC
  │   └── InfoGuard
  └── Entanglement
      ├── Matrix
      ├── Deep Profiles
      ├── Recruitability
      └── Dispositions
📁 ABSM Sprint
  ├── Overview (program + clients)
  ├── Targeting
  │   ├── ICP Definition
  │   ├── Scoring Matrix
  │   ├── Longlist 30
  │   ├── Shortlist 10
  │   └── Final Selection
  ├── Strategy
  │   ├── Sweet-Spot Profile
  │   ├── Pain Pattern Library
  │   ├── Content Matrix
  │   └── Competitive Angle
  ├── Clients
  │   ├── Hörmann (4 files)
  │   ├── Reinhausen (4 files)
  │   ├── Witte (4 files)
  │   └── Trumpf (4 files)
  ├── Collateral (12 PDFs)
  └── Infrastructure
      ├── CRM Spec (HubSpot)
      ├── KPI Dashboard
      ├── MDF Spec
      └── Launch Checklist
```

**Behavior:**
- Desktop: sidebar always visible, 260px fixed left
- Content area: scrolls independently
- Mobile (<768px): hamburger icon top-left → overlay sidebar
- Current page highlighted in sidebar (bold + --ak-blue left border)
- Sections collapsible (click to toggle children)
- Sidebar sticky (scrolls with own overflow)

---

## MD → HTML CONVERSION SPEC

Every .md file becomes a full .html page with:
1. Shared nav (dark top bar: logo + section links)
2. Sidebar (collapsible tree, current page highlighted)
3. Content area (rendered markdown with site CSS)
4. No separate back button needed — sidebar is navigation

**Template structure:**
```html
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="[depth]/assets/css/main.css">
</head>
<body>
  <nav class="top-nav">...</nav>
  <div class="layout">
    <aside class="sidebar">...</aside>
    <main class="content">
      <!-- rendered markdown content here -->
    </main>
  </div>
</body>
</html>
```

**Approach:** Build one `md-template.html` shell. Use a Python script to:
1. Read each .md file
2. Convert to HTML via `markdown` library
3. Inject into template
4. Write .html next to .md (or replace .md)
5. Sidebar highlights current page via filename match

---

## COPYWRITING BRIEF (for Opus 4.7 chat)

### Voice & style

**Read the two books in project knowledge** — especially:
- Reverse Job Search Method (Whittaker): Value Letter concept, pre-suasion, WIIFM
- Reverse the Search (Mann): Job Shopper mindset, story-driven positioning

**Writing rules:**
- Short sentences. Max 15 words per sentence average.
- No "I built" / "I created" / "I designed" flooding. Use passive or third-person where possible: "The program delivered 150% of budget" not "I delivered 150%."
- When first-person is unavoidable, use it once per paragraph max.
- Proof-first: lead with the number, then the context. "150% budget delivery. Three-year compound. Eastern European partner network built from zero."
- No AI slop: no "leverage," "utilize," "drive synergies," "passionate about." Write like a person talking to a smart colleague.
- Storytelling arc: Physical doors → digital doors. Security you can touch → security you can't see. Same system-building, different product.

### Homepage rewrite spec

**Current:** Generic AI-generated motivation letter. Too long, too "I"-heavy, no hook.

**Target:** 2-page-equivalent memo. Story arc structure:

1. **Hook** (2-3 sentences): The bridge from physical security to cybersecurity. Not "I want this job" — instead: "Revolving doors and firewalls have more in common than you'd think."
2. **The builder's proof** (1 paragraph): Boon Edam numbers. Partner program built from scratch. 150% budget, ROS 24%, COGS −10.5pp. Eastern Europe. Don't explain what a partner program is — prove you can build one.
3. **Three Perspectives** (3 cards/bullets with anchor links to sections):
   - Method: "A 7-stage partner lifecycle framework. Maturity model with 21 checkpoints. Not theory — tested against 4 years of execution."
   - Partner Mapping: "33 DACH security partners scored across 6 dimensions. Five prioritized for recruitment. First-pass research, publicly sourced."
   - ABSM Sprint: "Four German Mittelstand manufacturers researched to account-level depth. 12 branded execution PDFs. CRM spec. Launch checklist. Ready to execute."
4. **Reading guide** (3 sentences): "This site runs deep. The homepage is the summary. Each section links to raw artifacts — scoring matrices, pain maps, battlecards — produced in a single sprint."
5. **30/60/90** (compact): What happens in the first 90 days. Three bullets.
6. **Sign-off:** "A. Marushevsky · Amsterdam" — no long bio, no "sincerely."

### Perspective page rewrite spec (3 pages)

Each perspective page gets:
1. **McKinsey-style exec summary** at top: 4-5 bullet points with anchor links to sections below. "This section covers: [link] ICP definition · [link] Scoring methodology · [link] 30-company longlist · [link] Final four selection"
2. **Rewritten intro paragraph** — same voice rules as homepage. Short, proof-first, no AI slop.
3. **Body content stays** — the existing HTML content (lifecycle table, maturity model, partner matrix, ABSM cards) is good. Just add the exec summary on top and clean up any "Alex M." references.

---

## IMPLEMENTATION PLAN (for Opus 4.6 chat)

### Phase 1: New CSS + Layout
- Replace main.css with Akamai-inspired design system
- Add sidebar component (HTML + CSS + JS toggle)
- Add dark top nav
- Add mobile hamburger

### Phase 2: MD → HTML conversion
- Python script: read all .md in docs/ → convert to .html with template
- Each .html gets sidebar, nav, proper CSS
- Remove or redirect .md links to .html equivalents

### Phase 3: Page rewrites
- Replace homepage content (from Opus 4.7 output)
- Add exec summaries to 3 perspective pages (from Opus 4.7 output)
- Fix all "Alex M." → "A. Marushevsky"

### Phase 4: QA
- All internal links work
- All .md files render as styled HTML
- Sidebar highlights correct page
- Mobile responsive
- PDF links work

---

## FILES TO UPDATE

| File | Action |
|---|---|
| `docs/assets/css/main.css` | **Replace** — new Akamai-inspired design system |
| `docs/index.html` | **Rewrite** — new homepage copy + layout |
| `docs/method/index.html` | **Update** — add exec summary, fix name |
| `docs/partner-mapping/index.html` | **Update** — add exec summary, fix name |
| `docs/absm-sprint/index.html` | **Update** — add exec summary, fix name |
| `docs/**/*.md` (37 files) | **Convert** — each becomes .html with sidebar |
| `docs/absm-sprint/05-infrastructure/kpi-dashboard.html` | **Update** — new CSS tokens |
| ALL html files | **Add** — sidebar component, new nav |

---

## CONTEXT FOR NEW CHAT

**Who is A. Marushevsky:**
- Managing Director / Commercial Architect, Amsterdam
- 20+ years B2B, P&L ownership
- Currently Boon Edam (physical security: revolving doors, security portals)
- Built partner program Eastern Europe from scratch
- Results: 150% budget delivery, ROS 24%, COGS −10.5pp over 3 years
- Earlier: ABM implementation for Cisco partners (Russia, passwordless authentication)

**Target:** Senior Channel Marketing Manager, Akamai DACH, Zero Trust
**Referrer:** Mark Shelepov, Principal Lead Architect, Akamai US (Rhode Island)
**What Mark receives:** CV (separate) + 1 printed PDF of homepage + link to this site

**Tone:** "Three Perspectives" — not diagnosis, not criticism. Framework, not prescription.
**Maturity scores:** Show the framework, never concrete Akamai scores.
**Caveat:** All partner research = "first pass from public sources" on every artifact.
