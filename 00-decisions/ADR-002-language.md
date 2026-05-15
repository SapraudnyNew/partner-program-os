# ADR-002: Language

**Date:** 2026-05-14
**Status:** Accepted

## Decision

All artifacts in **English**. Internal notes and `00-decisions/` may use English-only; no Russian fork.

## Context

Alex's reverse job search targets European (DACH, Benelux, EMEA) executive market. Working language is English at every level above country-manager. Hiring managers, recruiters, peer-recommenders all read English.

A bilingual repo creates drift: the Russian version becomes the "real" one and the English version becomes the marketing skin. Drift kills credibility.

## Resolution

- Canonical content: English.
- No Russian translations stored in the repo.
- Chat conversations during build can continue in Russian for speed. Output gets translated to English before commit.

## Consequences

- Cost: Alex loses some nuance in Russian. Mitigation: critical concept naming is decided in chat first (in either language), then English version is committed.
- Benefit: zero ambiguity about which version is authoritative.
