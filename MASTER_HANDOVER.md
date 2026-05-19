# MASTER HANDOVER — Partner Program OS
> **This file lives permanently in repo root.**  
> Every new Claude session starts by reading this file, then reading STATE.md for current status.  
> Never rewrite this file. Update STATE.md instead.

---

## HOW TO START ANY NEW SESSION

You are reading this because the user said:  
*"Read the master handover prompt in repo"*

**Do this immediately, in order:**
1. Read this file top to bottom — it is the locked context
2. Read `STATE.md` — it is the current build log (append-only, newest at bottom)
3. Say: "Read. [one sentence summary of where we left off from STATE.md]. Ready."
4. Wait for user instruction — do not propose work unprompted

---

## THE PROJECT

A GitHub Pages mini-site that is Alex's motivation letter with proof-of-work artifacts for a specific job application. Not a portfolio. Not a generic site. One target, one referrer, one shot.

**Repo:** https://github.com/SapraudnyNew/partner-program-os (PRIVATE)
**Live site:** https://sapraudnynew.github.io/partner-program-os/ (PUBLIC)
**Source:** `docs/` directory on branch `main` → GitHub Pages
**Hosting:** GitHub Pro ($4/mo) — private repo, public Pages

---

## ALEX (the candidate)

- **Name:** A. Marushevsky — based in Amsterdam
- **Current:** Boon Edam — global physical security (revolving doors, security portals)
- **Built:** Partner program Eastern Europe from scratch, full P&L ownership
- **Results:** 150% budget delivery, ROS 24%, COGS -10.5pp over 3 years
- **Earlier (2018-2022):** Consultant. ABM programs for partner ecosystems of Cisco, NetApp, SAP, Dassault Systemes
- **Also:** Hilti (+128% facade growth, best profitability in Eastern Europe) — available if needed
- **Target role:** Senior Channel Marketing Manager, Akamai DACH, Zero Trust
- **Path:** Warm referral via **Mark Shelepov** (Principal Lead Architect, Akamai US, Rhode Island)
- **Narrative:** Physical security channel → cybersecurity channel. Same system, different product.

**Mark receives:** CV (separate file) + 1 printed PDF of homepage + link to this site

---

## THE SITE STRUCTURE

```
docs/
├── index.html                    ← Homepage = Memo (motivation letter)
├── assets/
│   ├── css/main.css              ← Shared design system (v2, 313 lines)
│   └── js/sidebar.js             ← Collapsible sidebar component
├── method/
│   ├── index.html                ← Perspective 1: 7-stage lifecycle + maturity model
│   ├── spider-chart.html         ← Interactive radar (framework, no Akamai scores)
│   └── scorecard-template.html   ← Full 7x3 scorecard
├── partner-mapping/
│   ├── index.html                ← Perspective 2: IPP, 6 dims, research overview
│   ├── dach-landscape.html       ← 33-partner matrix, filterable
│   ├── pursue-five/
│   │   ├── index.html            ← 5 partner profiles with hooks
│   │   ├── *.html                ← Individual partner profiles (from MD)
│   │   └── all-five-profiles.html
│   └── entanglement/
│       └── *.html                ← Entanglement matrix, deep profiles, etc. (from MD)
├── absm-sprint/
│   ├── index.html                ← Perspective 3: full ABSM program
│   ├── 01-targeting/*.html       ← ICP, scoring, longlist, shortlist, final selection
│   ├── 02-strategy/*.html        ← Sweet-spot, pain patterns, content matrix, competitive
│   ├── 03-clients/               ← Hoermann, Reinhausen, Witte, Trumpf (4 files each)
│   ├── 04-collateral/*.pdf       ← 12 branded execution PDFs
│   └── 05-infrastructure/
│       ├── kpi-dashboard.html    ← Interactive KPI dashboard
│       └── *.html                ← CRM spec, MDF spec, launch checklist
└── (54 MD-generated HTML pages total)
```

---

## LOCKED DECISIONS — DO NOT RELITIGATE

| # | Decision |
|---|---|
| TONE | "Three Perspectives" — NOT "your program has gaps." Framework, not diagnosis. |
| NAME | **A. Marushevsky** everywhere. Not "Alex M.", not "Alex Marushevsky." |
| BIO | Cisco/NetApp/SAP/Dassault = consulting clients (2018-2022), NOT employer. |
| MATURITY | Framework illustration only. No concrete Akamai scores anywhere on site. |
| SCORECARD | `03-diagnosis-scorecard-v1.3.md` has real Akamai scores — reference only, NOT published. |
| CAVEAT | All partner research: "first pass from public sources" caveat on every artifact. |
| DESIGN | Akamai-inspired minimalism. DM Sans only (no serif). White nav, dark footer. Blue accents. |
| SPIDER CHART | 7 axes, 3 rings (Basic/Professional/World-class), draggable dots. No named company scores. |
| PURSUE FIVE | Axians+Fernao, AVANTEC, SVA Wiesbaden, ACP Gruppe, InfoGuard |
| INFOGUARD | Deepen existing relationship (already Akamai partner) — not cold recruit |
| ABSM TERRITORY | Germany only. Four targets: Hoermann, Reinhausen, Witte, Trumpf |
| AI ANGLE | Dedicated callout in ABSM page: "6 to 8 weeks per partner gets done in days" |
| URL | `partner-mapping/` (not `partners/`) |
| PDF | Homepage generates to `docs/memo-alex-m.pdf` for Mark |
| REPO | Private (GitHub Pro). GitHub Pages public from /docs/ branch main. |
| EM-DASHES | Zero in new copy. Colons, periods, or removed. |

---

## DESIGN SYSTEM v2 — Akamai-Inspired

### CSS: `docs/assets/css/main.css` (313 lines)

```css
/* Key variables */
--ak-blue: #009FDB;            /* Akamai primary — links, accents, hover */
--ak-blue-dark: #0077B5;       /* Hover state */
--ak-navy: #0D2137;            /* Footer only */
--ink: #1B2733;                /* Headings */
--ink-light: #4A5568;          /* Body text */
--ink-muted: #718096;          /* Captions, metadata */
--surface: #FFFFFF;            /* Page background */
--surface-alt: #F7FAFC;        /* Alt sections */
--border: #E2E8F0;             /* Borders */
--border-accent: rgba(0,159,219,0.2); /* Blue borders */
--font-sans: 'DM Sans', sans-serif;
--font-mono: 'JetBrains Mono', monospace;
--sidebar-width: 240px;
--nav-height: 52px;
```

### Nav structure (white, not dark)
```html
<nav class="top-nav">
  <button class="hamburger" aria-label="Toggle navigation">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">
      <line x1="3" y1="6" x2="21" y2="6"/>
      <line x1="3" y1="12" x2="21" y2="12"/>
      <line x1="3" y1="18" x2="21" y2="18"/>
    </svg>
  </button>
  <a href="[prefix]index.html" class="top-nav__logo">Partner Program <span>OS</span></a>
  <ul class="top-nav__links">
    <li><a href="[prefix]index.html">Memo</a></li>
    <li><a href="[prefix]method/index.html" class="active">Method</a></li>
    <li><a href="[prefix]partner-mapping/index.html">Partners</a></li>
    <li><a href="[prefix]absm-sprint/index.html">ABSM</a></li>
  </ul>
</nav>
```

### Footer (dark navy)
```html
<footer class="site-footer">
  <p>A. Marushevsky &middot; Amsterdam &middot; All partner research is a first pass from public sources.</p>
</footer>
```

### Sidebar
Copy from any of the 4 main pages. Adjust `href` paths for directory depth. JS: `sidebar.js`.

---

## SOURCE FILES IN REPO (where to find content)

| Content needed | Source in repo |
|---|---|
| Method overview | `01-method/00-method-overview.md` |
| 7 stage details | `01-method/01-recruit.md` through `07-expand.md` |
| Maturity framework | `01-method/maturity-model/00-maturity-framework.md` |
| Scorecard template | `01-method/maturity-model/scorecard-template.md` |
| Entanglement research | `02-akamai/research/outputs/entanglement/` (4 files) |
| Pursue Five profiles | `02-akamai/research/outputs/d3-1/d3-1-pursue-priority-five.md` |
| DACH dossier | `02-akamai/research/outputs/partner-program/akamai-partner-program-dach-dossier.md` |
| ABSM sprint files | `02-akamai/03-dach-projects/absm-sprint/` (44 files) |
| 12 execution PDFs | `02-akamai/03-dach-projects/absm-sprint/04-execution/*.pdf` |
| **Do NOT use** | `02-akamai/03-diagnosis-scorecard.md` (has Akamai scores — reference only) |

---

## WHAT "DONE" LOOKS LIKE

The site ships when:
1. All HTML pages render correctly on GitHub Pages ✅
2. All MD stub files converted to HTML with sidebar ✅
3. PDF collateral accessible at `04-collateral/` links (needs verification)
4. `kpi-dashboard.html` built and linked ✅
5. Homepage generates clean PDF: `docs/memo-alex-m.pdf` ← STILL OPEN
6. All navigation links work without 404s (needs verification)

Check STATE.md for current completion status.
