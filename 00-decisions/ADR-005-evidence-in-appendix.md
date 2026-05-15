# ADR-005: Evidence in Appendix

**Date:** 2026-05-14
**Status:** Accepted

## Decision

Evidence (cases, numbers, sources, citations) goes in a dedicated **Appendix** section. Main body stays evidence-light. Inline citations use bracketed references like `[E-12]` that point to appendix entries.

## Context

Three options were considered:

1. **Inline** — weave case studies and stats directly into prose.
2. **Appendix** — main body argues from logic; appendix carries proof.
3. **Hybrid** — light inline (1–2 numbers per claim) + deep appendix.

Inline reads like a McKinsey deck and clutters the main argument. Hybrid is the magazine-article default, but it forces every claim to either show a number or skip the proof — and most claims have proof, so the document bloats.

## Resolution

Pure appendix model with bracketed refs:

```
Main body:
"Channel marketing programs that align with how buyers actually buy outperform
traditional 'random acts of marketing' by 3-5x on pipeline conversion [E-12].
This is the structural shift Akamai needs in DACH."

Appendix entry E-12:
Source: Moore & Thomas, Marketing Multiplied (2018), ch. 3.
Claim: "Modern aligned channel marketing outperforms random tactics by 3-5x"
Strength: Author claim from practitioner data; not independent meta-analysis.
```

### Strength labels (appendix-only)

Every appendix entry carries a strength label:
- **Hard:** Independent research, peer-reviewed, or audited data.
- **Practitioner:** Cited by domain expert from their own experience.
- **Inferred:** Logical extension, not directly sourced.

The hiring manager who wants to challenge a claim can flip to the appendix and see what they're up against. No claim hides behind vague attribution.

## Consequences

- Main body becomes argumentation. Reader experience is closer to a strategic memo than a research report.
- Appendix must be maintained as a real index. `01-method/appendix/evidence-library.md` is the canonical source.
- Number of evidence entries grows over time. Each artifact references the central library, doesn't duplicate.
