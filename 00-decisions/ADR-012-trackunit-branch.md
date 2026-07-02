# ADR-012: Second Campaign (Trackunit) as Isolated Branch Inside One Repo

**Date:** 2026-07-02
**Status:** Accepted

## Decision

The repo hosts a second job-application campaign: **Head of Partnerships - Integrations & Applications at Trackunit** (IrisX platform). It lives as an isolated branch of the same site rather than a new repo.

Layout:

| Layer | Path |
|---|---|
| Sources, research, CV, outreach | `04-trackunit/` |
| Published site | `docs/trackunit/` → https://sapraudnynew.github.io/partner-program-os/trackunit/ |
| Build tool | `tools/md2html_trackunit.py` (sibling of `md2html.py`, scoped to the branch) |
| Agent runbook | `04-trackunit/RUNBOOK.md` (subagent system: research, content, build, deploy) |

Isolation rules:

1. No page under `docs/trackunit/` links to Akamai pages or to the site root. The only shared references are `../assets/css/main.css` and `../assets/js/sidebar.js`.
2. The root `index.html` gets no link to `/trackunit/`. A Trackunit reader lands on the branch URL directly and stays inside the branch.
3. The Akamai campaign content is frozen: nothing under `docs/` outside `docs/trackunit/` changes.

Reuse rules:

1. Design system v2 (`docs/assets/css/main.css`, sidebar.js) is reused unchanged.
2. The universal 7-stage method is adapted, not copied: stages renamed to the integration partner lifecycle (Source → Qualify → Scope → Build → Launch → Adopt → Scale) with a maturity model reworded for a platform integrations program.
3. Site formula repeats the Akamai pattern: Memo homepage + three perspectives (Method / Partner Mapping / Execution) + interactive artifacts (spider chart, filterable landscape, credit consumption dashboard).

## Context

The Akamai campaign shipped and the link is in circulation, so its URLs must not change. Renting a second repo would split the toolchain (converter, design system, session continuity files) for no reader-visible benefit: the Trackunit reader gets a clean branch URL either way. The user chose one repo with isolation over a new repo.

Campaign-specific decisions: application goes through both the careers form and direct hiring-manager outreach (likely addressee: VP of Platform, identified via people research; fallback: ranked 2-3 addressees). The primary commercial metric of the target role is IrisX credit consumption, so the execution perspective centers on it. Tone toward Trackunit's existing marketplace and developer portal is an opportunity map, not an audit (constructive framing only). Names and titles of real people found in public sources are written openly in artifacts after two-source verification.

## Consequences

- Future campaigns can repeat this pattern: `0N-<company>/` sources + `docs/<company>/` branch + a scoped converter, at the cost of one more nav variant per branch.
- `md2html.py` (Akamai-scoped) and `md2html_trackunit.py` drift independently by design; a shared template refactor is deliberately postponed until a third campaign proves the pattern.
- The public-sources caveat and "A. Marushevsky" naming carry over as repo-wide invariants (see MASTER_HANDOVER).
