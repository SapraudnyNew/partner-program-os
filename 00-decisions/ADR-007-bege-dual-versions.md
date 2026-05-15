# ADR-007: BEGE Rollout Map — Dual Versions

**Date:** 2026-05-14
**Status:** Accepted

## Decision

The Boon Edam rollout map exists in **two versions** from day one:

- **Internal version** (`03-boon-edam/02-rollout-map-internal.md`): full, BEGE-specific, with partner names, financial numbers, real risks, internal politics.
- **Public/portfolio version** (`03-boon-edam/01-rollout-map-public.md` and `/docs/case-study-bege.md`): sanitized. Company name abstracted to "European premium B2B equipment manufacturer". Partner names removed or pseudonymized. Numbers either rounded into ranges or removed entirely.

## Context

The artifact has two equally real purposes:

1. **Internal execution document.** Alex genuinely intends to roll out the partner program changes at Boon Edam. The document is a working plan.
2. **External portfolio piece.** The same intellectual work is the strongest single proof point for Alex's RJSM positioning. It's what makes recruiters and CEO-targets take him seriously.

Mixing these into one document produces either:
- A working plan too sanitized for internal use, or
- A portfolio piece too company-confidential to share

Both fail.

## Resolution

### Sanitization rules for the public version

Strip:
- Company name "Boon Edam" → "European premium B2B equipment manufacturer"
- Specific partner names → generic descriptors ("a Tier-1 systems integrator in DACH")
- Specific financial numbers → ranges or removed ("AR aging > 30 days impacted ~X% of receivables")
- Internal names and email addresses → roles only
- Specific tooling and ERP names → generic ("the partner portal")
- Internal political dynamics → removed entirely

Keep:
- The 7-stage lifecycle structure
- The diagnostic framework
- The intervention logic
- The phased rollout sequence (with timing in weeks, not dates)
- The success metrics framework

### Sync discipline

When the internal version updates, the public version updates the same day or the public version is taken down. No public version that lags reality.

The `/docs/` GitHub Pages publish job pulls from the public version only. A pre-commit check should fail if `01-rollout-map-public.md` contains the string "Boon Edam" or known partner names.

## Consequences

- Double the writing for the rollout map specifically. Mitigated by writing the public version first (forces clarity), then specializing for internal use.
- The public version becomes citable in conversations: "Here's the rollout framework I've been applying at my current employer — happy to walk through it." Real, credible, no NDA breach.
