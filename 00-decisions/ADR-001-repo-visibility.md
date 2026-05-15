# ADR-001: Repo Visibility and Publishing

**Date:** 2026-05-14
**Status:** Accepted

## Decision

Repo is **private**. A curated subset publishes to **GitHub Pages** via `/docs`.

## Context

This repo holds three artifacts:
- A reusable methodology (universal template)
- An application targeting a specific employer (Akamai)
- An application referring to a current employer (Boon Edam) with internal data

Public-by-default is wrong because:
- Boon Edam-specific content includes internal numbers, partner names, AR risk patterns, and operational state. None of this can be public.
- Akamai HVO references a warm referrer; making that public burns the referrer.

Private-only is wrong because:
- The methodology layer (universal template) is portfolio-grade. Hiding it loses the credibility asset.
- A public artifact at `username.github.io/partner-program-os/` is a stronger signal than a CV bullet.

## Resolution

Two-track publishing:

**Private (default):**
- All content in `01-method/`, `02-akamai/`, `03-boon-edam/`, `00-decisions/`, `prompts/`.

**Public via `/docs` → GitHub Pages:**
- Sanitized universal template (no client names, no Akamai-specific tactics)
- One or two case studies framed generically ("European premium B2B equipment manufacturer")
- Index page with one-paragraph positioning

`/docs` is regenerated from canonical sources in `01-method/` after every major update. Diffs reviewed before publish.

## Consequences

- Every artifact must be written twice if it goes public: full version (private) + sanitized version (`/docs`).
- The "sanitize" step is a real workflow, not a hand-wave. ADR-007 specifies what gets stripped.
