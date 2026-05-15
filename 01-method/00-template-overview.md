# HVO Universal Template — Overview

**Purpose:** A reusable framework for High-Value Offer (HVO) artifacts targeting any partner program leadership role. Specializes per target company by filling stage-level content.

**Structure:** 7-stage partner lifecycle (ADR-003). Three-reader model (ADR-004). Evidence in appendix (ADR-005).

---

## Document anatomy

Every HVO built on this template has the same skeleton:

```
[Cover page — 1 paragraph]
  One-line value claim. Target company named. Reader-facing positioning.

[Executive Summary — 1 page]
  Strategic frame. Three to five core moves. Business case.

[Stage 1: Recruit — 0.5 to 1 page]
  Diagnosis of current state. Proposed intervention. KPIs.

[Stage 2: Onboard — 0.5 to 1 page]
  Same pattern.

[Stage 3: Enable — 0.5 to 1 page]
  Same pattern.

[Stage 4: Co-sell — 0.5 to 1 page]
  Same pattern.

[Stage 5: Deliver — 0.5 to 1 page]
  Same pattern.

[Stage 6: Renew — 0.5 to 1 page]
  Same pattern.

[Stage 7: Expand — 0.5 to 1 page]
  Same pattern.

[Closing — half page]
  90-day priorities. What I would own in the first quarter.

[Appendix — as needed]
  Evidence library. Frameworks source map. Glossary.
```

Total length: 6 to 10 pages depending on application depth.

---

## Stage-level content pattern

Each of the seven stage files (`01-recruit.md` through `07-expand.md`) follows this internal pattern:

```markdown
# Stage N: [Name]

## What this stage is

Plain-language definition. Two to three sentences.

## What "good" looks like

Three to five characteristics of a high-performing partner program at this stage.

## Common failure modes

What goes wrong. Specific patterns, not abstractions.

## Diagnostic questions

Five to ten questions that surface state of this stage at a target company.

## Intervention library

Concrete plays. Each play has:
- Name
- One-paragraph description
- Source [evidence ref]
- Applicability conditions
- Lead time to impact

## KPIs

Three to seven metrics that measure this stage. With formulas, not just names.

## RACI within the stage

Who does what — at the company, in the partner organization, at the end customer.
```

This pattern is identical across all seven stages. Predictability is the feature.

---

## How to specialize for a target company

To produce a target-company HVO from this template:

1. Read the seven stage files in order.
2. For each stage, choose 2–3 interventions from the library that fit the target's situation.
3. Write the cover and Executive Summary last, after stage selection.
4. Strip anything not chosen. The final HVO is 6–10 pages, not 30.

The Akamai HVO (`02-akamai/`) is the first application.
The BEGE Rollout Map (`03-boon-edam/`) is a different shape — it's a rollout plan, not an HVO — but draws from the same stage library.

---

## What this template is NOT

- Not a partner program audit framework. Different work product.
- Not a partner program operations manual. Too high-level.
- Not a CV or cover letter. HVO is its own genre.
- Not industry-specific. Industry context goes in the specialization layer.
