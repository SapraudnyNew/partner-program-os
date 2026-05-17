# Akamai HVO — Context

> **Role:** Senior Channel Marketing Manager
> **Location:** DACH region
> **Product focus:** Zero Trust security solutions
> **Posting:** https://jobs.akamai.com/en/sites/CX_1/job/2855

## Entry path

**Warm referral.** Mark Shelepov (Principal Lead Architect at Akamai, US, Rhode Island, 2nd-degree LinkedIn connection) sends Alex internal referral. Akamai sends Alex application invitation email. Alex does NOT apply directly through the job posting. The referrer's credibility is on the line (see ADR-006).

**Referrer constraint:** Mark is on the technical track. He vouches for judgment and execution at a generalized level. He cannot vouch for the specific DACH channel marketing competency the role requires. The HVO bundle must close that function-fit gap on its own (rationale for ADR-009).

## Reader stack

1. **Mark Shelepov (referrer)** — reads the HVO bundle before passing it on. Must feel comfortable championing it. Forwards a portfolio, not a memo.
2. **Hiring manager** — Senior Manager level, owner of the DACH channel marketing P&L for Zero Trust. Reads to decide whether to schedule the call and what to talk about.
3. **VP Channel Marketing EMEA (skip-level)** — does not receive the document directly. May read the 1-page executive summary if the hiring manager forwards it. Document must withstand executive scrutiny.

## Why this role makes strategic sense for Alex

The role is below Alex's career altitude on paper. Three factors make it the right door:

1. **Domain entry, not domain demotion.** DACH cybersecurity channel marketing is a domain Alex has not formally held. Senior Manager is the right rank for a domain-entry move. Director-level entry would require Akamai to take a bet they have no reason to take.
2. **The role is closer to P&L than the title suggests.** Channel marketing managers at Akamai own MDF allocation, partner co-marketing budgets, pipeline contribution targets. Small-P&L work where Alex's 20+ years of P&L thinking compounds quickly.
3. **DACH market access.** A senior role at Akamai in DACH puts Alex inside the European cybersecurity ecosystem with one of the strongest channel programs in the industry. Lateral and upward moves become available from there that don't exist from outside.

## Strategic frame for the HVO

The HVO's central claim: **Most channel marketers know channel marketing. Few think in P&L. I do both.**

This frame:
- Positions Alex at the right level for the job (channel marketing competence is the table stakes).
- Distinguishes from the typical Senior Manager candidate (they don't have P&L muscle).
- Reads upward to the VP (they think in P&L; they recognize the language).
- Does not threaten the hiring manager (P&L thinking presented as a service to the channel function, not a power move).

## Akamai-specific research status

Per the research mission prompts in `research/prompts/` and outputs in `research/outputs/`:

- [x] Akamai's current DACH channel structure (top partners, tiers, MDF model) - covered in `research/outputs/partner-program/akamai-partner-program-dach-dossier.md` File 1 + File 2
- [x] Zero Trust security buyer journey in DACH (CISO + buying committee dynamics) - covered in `research/outputs/company/02-dach-regional-intelligence.md`
- [x] Akamai's main channel competition in DACH (Cloudflare, Zscaler, Cisco, Microsoft, Illumio partners) - covered in `research/outputs/partner-program/akamai-partner-program-dach-dossier.md` File 3
- [x] Akamai's recent channel marketing campaigns and playbook - covered in `research/outputs/company/04-channel-marketing-organization.md` and `akamai-research.md`
- [x] DACH-specific regulatory pressure on Zero Trust (NIS2, DORA implications) - covered in `research/outputs/company/02-dach-regional-intelligence.md`
- [x] Recent Akamai leadership changes affecting channel - covered in `research/outputs/company/01-corporate-fundamentals.md`
- [x] Referrer relationship confirmed - Mark Shelepov, Principal Lead Architect, technical track, NOT in channel marketing reporting line

Research outputs total: 60+ pages, 50 named DACH partners, displacement targets identified (KAEMI, Navixia, Computacenter), anchor partners identified (Deutsche Telekom Security, Bechtle, Controlware, InfoGuard).

## HVO bundle structure (per ADR-009)

The Akamai deliverable is NOT a single memo. It is a bundle:

1. **Page 0:** 1-page executive summary. Standalone. Skip-level readable. For VP Channel Marketing EMEA forwarding path. (file: `00-page-zero-executive-summary.md`)
2. **Pages 1-3.5:** main memo. Method overview, Akamai diagnosis, top 3 gaps, 90-day plan, fit. (file: `01-leave-behind-memo.md`)
3. **Linked:** ABM/TAS DACH partner package. 30 candidates scored, 10 longlisted with full IPP + 9-box + one-page profile. (location: `03-dach-projects/abm-tas-partners/`)
4. **Linked:** ABSM DACH sprint package. 32-artifact methodology for German Mittelstand Zero Trust, 3 accounts deep + 1 publicly-named showcase. (location: `03-dach-projects/absm-sprint/`)
5. **Linked:** Interactive spider chart (web-hosted) + PDF static export. (file: `05-akamai-spider.html`)
6. **Optional:** HVO direct approach version for VP/Director-level fallback frame. (file: `02-hvo-direct-approach.md`)

The memo is the entry point. The DACH projects carry the proof of execution. The 1-page summary lets the document travel up the org without requiring the reader to consume the full bundle.

## Documents in this folder

- `00-context.md` — this file
- `00-page-zero-executive-summary.md` — 1pp standalone executive summary (TO BE WRITTEN)
- `01-leave-behind-memo.md` — main 3.5pp memo (skeleton, awaits D2-3)
- `02-talking-points.md` — discussion structure for the warm intro call (drafted)
- `02-hvo-direct-approach.md` — VP/Director-level fallback (TO BE WRITTEN)
- `03-diagnosis-scorecard.md` — Akamai scored on maturity model (TO BE WRITTEN, D2-2)
- `04-talking-points.md` — same as 02 (legacy, may consolidate)
- `05-akamai-spider.html` — interactive spider chart (TO BE BUILT)
- `akamai-research.md` — initial research synthesis, pointer to deep research outputs
- `research/prompts/` — the two v2 research mission prompts (done)
- `research/outputs/` — full research outputs (60+ pages, done)

## Next action

Per STATE.md day-by-day status, the next D-block is **D2-2: Akamai diagnosis scorecard.** Apply `01-method/maturity-model/scorecard-template.md` to Akamai using the research outputs. Score each of the 7 stages at Basic/Professional/World-class. Output: filled scorecard in `02-akamai/03-diagnosis-scorecard.md`, top 3 gaps with revenue impact, spider chart input data (current state coordinates vs world-class).

After D2-2 settles, D3-1 (ABM/TAS) and D3-2 (ABSM) run in parallel.

The main memo (D2-3) drafts AFTER D2-2 scorecard is in place and at least one DACH project has a framing draft. The 1-page executive summary (D2-3a) writes LAST, after the memo settles.
