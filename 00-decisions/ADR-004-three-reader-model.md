# ADR-004: Three-Reader Model

**Date:** 2026-05-14
**Status:** Accepted

## Decision

Every artifact serves **three readers simultaneously** in one document via a two-layer structure:

- **Top layer (Executive Summary):** CEO / Board / VP-level. Strategic framing, business case, key numbers.
- **Bottom layer (Operational Detail):** Head of Channel / CRO / CMO / Director-level. RACI, KPIs, process flows, decisions.

A third reader is served by the artifact's surface signal: the recruiter or first-screen reviewer who scans for credibility cues without reading deeply.

## Context

Three reader types exist for partner-program work:

1. **C-suite / Board.** Reads only top of document. Asks: "Is this a real growth lever? Can this person operate at the strategic level?"
2. **Operating leader.** Reads in depth. Asks: "Does this person know the work? Can I hand them a quarter and expect execution?"
3. **Screening reader (recruiter, EA, internal HR).** Scans. Asks: "Does this artifact signal seniority? Should I forward it up?"

Writing three separate documents fragments the work and creates version drift. Writing one document for one reader loses the others.

## Resolution

Single document, structured for layered reading:

```
[Cover / one-line value claim] ← screening reader
[Executive Summary, 1 page]    ← C-suite + screening reader
[Detailed sections, 4-8 pages]  ← operating leader
[Appendix: evidence, sources]   ← anyone who wants to verify
```

### Writing rules

- **Executive Summary** must stand alone. If the C-suite reads only this, they have a complete decision.
- **Detailed sections** must not contradict the Executive Summary. Detail expands, never re-decides.
- **Appendix** must let anyone fact-check any claim in 60 seconds.

### Surface signals (for screening reader)

Document name, cover format, one-line value claim, and section titles must read at senior-executive level. No tactical jargon on the cover.

## Consequences

- Every artifact is longer than a one-purpose document but shorter than three documents.
- The discipline of "Executive Summary stands alone" forces clarity. This is a feature.
- Detail and summary must stay in sync — version control needed.
