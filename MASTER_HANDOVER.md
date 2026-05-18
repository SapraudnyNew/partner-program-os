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

**Repo:** https://github.com/SapraudnyNew/partner-program-os  
**Live site:** https://sapraudnynew.github.io/partner-program-os/  
**Source:** `docs/` directory → GitHub Pages

---

## ALEX (the candidate)

- **Name:** Alex M. — based in Amsterdam
- **Current:** Boon Edam — global physical security (revolving doors, security portals)
- **Built:** Partner program Eastern Europe from scratch, full P&L ownership
- **Results:** 150% budget delivery · ROS 24% · COGS −10.5pp over 3 years
- **Earlier:** ABM implementation for Cisco partners in Russia — passwordless authentication, partner portal playbooks
- **Target role:** Senior Channel Marketing Manager, Akamai DACH, Zero Trust
- **Path:** Warm referral via **Mark Shelepov** (Principal Lead Architect, Akamai US, Rhode Island)
- **Narrative:** Physical security channel → cybersecurity channel. Same system, different product.

**Mark receives:** CV (separate file) + 1 printed PDF of homepage + link to this site

---

## THE SITE STRUCTURE

```
docs/
├── index.html                    ← Homepage = Memo (motivation letter)
├── assets/css/main.css           ← Shared design system
├── method/
│   ├── index.html                ← Perspective 1: 7-stage lifecycle + maturity model
│   ├── spider-chart.html         ← Interactive radar (framework, no Akamai scores)
│   └── scorecard-template.html   ← Full 7×3 scorecard
├── partner-mapping/
│   ├── index.html                ← Perspective 2: IPP, 6 dims, research overview
│   ├── dach-landscape.html       ← 33-partner matrix, filterable
│   ├── pursue-five/
│   │   ├── index.html            ← 5 partner profiles with hooks
│   │   └── *.md                  ← Individual partner profiles
│   └── entanglement/
│       └── *.md                  ← Entanglement matrix, deep profiles, etc.
└── absm-sprint/
    ├── index.html                ← Perspective 3: full ABSM program
    ├── 01-targeting/*.md
    ├── 02-strategy/*.md
    ├── 03-clients/hoermann|reinhausen|witte|trumpf/*.md
    ├── 04-collateral/*.pdf
    └── 05-infrastructure/
        ├── kpi-dashboard.html    ← Build: interactive KPI dashboard
        └── *.md
```

---

## LOCKED DECISIONS — DO NOT RELITIGATE

| # | Decision |
|---|---|
| TONE | "Three Perspectives" — NOT "your program has gaps." Framework, not diagnosis. |
| MATURITY | Framework illustration only. No concrete Akamai scores anywhere on site. |
| SCORECARD | `03-diagnosis-scorecard-v1.3.md` has real Akamai scores — reference only, NOT published. |
| CAVEAT | All partner research: "first pass from public sources" caveat on every artifact. |
| DESIGN | consulting-minimal · Source Serif 4 serif + DM Sans sans · warm neutrals · print-ready |
| SPIDER CHART | 7 axes, 3 rings (Basic/Professional/World-class), draggable dots · No named company scores |
| PURSUE FIVE | Axians+Fernao · AVANTEC · SVA Wiesbaden · ACP Gruppe · InfoGuard |
| INFOGUARD | Deepen existing relationship (already Akamai partner) — not cold recruit |
| ABSM TERRITORY | Germany only · Four targets: Hörmann · Reinhausen · Witte · Trumpf |
| AI ANGLE | Dedicated callout in ABSM page: personalization at scale through AI agents |
| URL | `partner-mapping/` (not `partners/`) |
| PDF | Homepage generates to `docs/memo-alex-m.pdf` for Mark |
| REPO | Private until ready. GitHub Pages from /docs/ branch main. |

---

## DESIGN TOKENS (use in all new HTML pages)

```css
/* Import path — adjust for directory depth */
<link rel="stylesheet" href="../assets/css/main.css">  /* 1 level deep */
<link rel="stylesheet" href="../../assets/css/main.css"> /* 2 levels deep */

/* Key variables */
--accent: #2c5545;          /* green — links, kickers, badges */
--ink: #1a1a1a;             /* headings */
--ink-light: #4a4a4a;       /* body paragraphs */
--ink-muted: #7a7a7a;       /* metadata, captions */
--surface: #fafaf8;         /* page bg */
--surface-alt: #f2f1ed;     /* caveat bg, alt rows */
--border: #e0ddd6;          /* card borders */
--font-serif: 'Source Serif 4', Georgia, serif;
--font-sans: 'DM Sans', sans-serif;
--font-mono: 'JetBrains Mono', monospace;
```

**Nav structure** — copy exactly:
```html
<nav class="site-nav">
  <div class="site-nav__inner">
    <a href="../" class="site-nav__brand">Partner Program OS</a>
    <ul class="site-nav__links">
      <li><a href="../">Memo</a></li>
      <li><a href="../method/">Method</a></li>
      <li><a href="../partner-mapping/">Partners</a></li>
      <li><a href="../absm-sprint/">ABSM</a></li>
    </ul>
  </div>
</nav>
```
Add `class="active"` to current section's link.

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
1. All 8 HTML pages render correctly on GitHub Pages
2. All MD stub files have real content (or are removed if not needed)
3. PDF collateral is accessible at `04-collateral/` links
4. `kpi-dashboard.html` is built and linked
5. Homepage generates clean PDF: `docs/memo-alex-m.pdf`
6. All navigation links work without 404s

Check STATE.md for current completion status.
