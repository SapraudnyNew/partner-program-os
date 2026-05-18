# Akamai Leave-Behind Memo

> **Status:** Skeleton awaiting content. Drafts in D2-3 after D2-2 diagnosis scorecard is in place and at least one DACH project has a framing draft.
> **Reader:** Hiring manager (DACH channel marketing Senior Manager) and skip-level (VP Channel Marketing EMEA).
> **Path:** Forwarded internally by Mark Shelepov as part of the HVO bundle (per ADR-009).

## Format

- Length: 3.5 pages. Opens cold with diagnosis. Referrer NOT named in cover.
- Format: PDF for handover. Markdown source canonical.
- Sits inside the HVO bundle alongside the 1-page executive summary (separate file: `00-page-zero-executive-summary.md`) and links to the DACH project bundles.

## Bundle position

The memo is the doorway. It frames the diagnosis, names the top 3 gaps, sketches the 90-day plan, and points to the linked artifacts for proof of execution. The DACH projects (ABM/TAS partner project + ABSM Mittelstand sprint) carry the operating-evidence burden that Mark Shelepov cannot vouch for from a technical-track position.

## Skeleton

```
[Cover paragraph — one-line value claim]
  Cold open. Diagnosis-led. Example pattern:
  "Akamai's DACH partner ecosystem shows Professional-grade structure
  on paper and Basic-grade operating depth in the data. The gap is
  channel marketing execution, not channel program design. This memo
  proposes how to close it in 90 days."
  Do NOT name Mark Shelepov here. The referral is the channel, not the pitch.

[Section 1: What I see in Akamai's DACH channel today]
  Outside-in view, grounded in research outputs.
  Three observations, each pinned to specific evidence from:
    - research/outputs/company/04-channel-marketing-organization.md
    - research/outputs/partner-program/akamai-partner-program-dach-dossier.md
  Specific. Not flattering. Not aggressive. Diagnostic.

[Section 2: Where the largest moves are]
  Three priorities mapped to 7-stage lifecycle but not labeled as such.
  Each priority gets one paragraph with one concrete first action.
  Sources: 03-diagnosis-scorecard.md (D2-2 output) plus the 50-partner dossier.
  Priority candidates (to be confirmed by D2-2 scorecard):
    - Displacement campaign at Illumio DACH partners (KAEMI, Navixia, Computacenter)
    - Tier upgrade of Computacenter Select -> Premier
    - Mittelstand systemhaus recruitment (SVA, Cancom, Axians) for Guardicore

[Section 3: What I would own in the first 90 days]
  Specific deliverables, not abstract themes.
  3-5 items, each measurable. Reference the ABM/TAS and ABSM bundles as
  proof of method, not as the plan itself.

[Section 4: Why this fit]
  Brief. Two paragraphs.
  Central claim: "Most channel marketers know channel marketing.
  Few think in P&L. I do both."
  Boon Edam reference allowed as brief credibility anchor (per ADR-009).
  Do not lean on Boon Edam metrics; the DACH projects do the proof work.

[Closing]
  No "I'd love to chat." Mark handles scheduling.
  Pointer to the linked artifacts:
    - ABM/TAS DACH partner package (full bundle in repo)
    - ABSM DACH sprint (full 32-artifact methodology in repo)
    - Interactive spider chart at [URL after D2-5a hosting decision]
  Sign-off: "Glad to take this further with [hiring manager name]
  when timing works."
```

## Specialization rules

Pull from the universal method (`01-method/`) but:

- **Reframe the language** for cybersecurity, not B2B equipment. Zero Trust, secure access, partner-led security adoption.
- **Reframe the scale** for Akamai's channel reality per the dossier. Partner Connect launched Q3 2025. DACH roster is thin and top-heavy (Deutsche Telekom Security, Bechtle, Controlware, InfoGuard, Computacenter at lowest tier). Operations focus is campaign-to-pipeline, not order-to-handover.
- **Lead with marketing**, not operations. The job is channel marketing.
- **Cite from the evidence library** sparingly. One or two `[E-NN]` refs in the main body maximum. The DACH projects carry detailed citations and named-entity density.
- **Reference research outputs** for specific data points, not the universal method.

## Draft trigger

This file gets filled when:
1. D2-2 (diagnosis scorecard) is complete and signed off.
2. At least one of D3-1 (ABM/TAS) or D3-2 (ABSM) has a framing draft so the memo can reference real outputs.
3. Mark Shelepov has confirmed the bundle structure is acceptable to forward.

## Linked artifacts in the bundle

- `00-page-zero-executive-summary.md` — 1pp standalone, skip-level readable
- `02-hvo-direct-approach.md` — VP/Director-level fallback frame
- `03-diagnosis-scorecard.md` — Akamai maturity scorecard
- `05-akamai-spider.html` — interactive spider chart (current vs world-class vs 90-day target)
- `03-dach-projects/abm-tas-partners/` — full ABM/TAS bundle (sibling under 02-akamai/)
- `03-dach-projects/absm-sprint/` — full ABSM 32-artifact sprint (sibling under 02-akamai/)
