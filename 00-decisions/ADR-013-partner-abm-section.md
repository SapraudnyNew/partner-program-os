# ADR-013: Partner ABM as a fifth section of the Trackunit branch

**Date:** 2026-07-04
**Status:** Accepted

## Context

The Akamai part of the site carries an ABSM Sprint as its capstone execution proof (targeting funnel 30 to 10 to 4, per-account kits, CRM and KPI infrastructure). The Trackunit branch had no equivalent, while the user wants the Trackunit application to demonstrate command of account-based marketing applied to partner acquisition and partner relationship development, and to do it better than the Akamai version.

## Decision

1. Partner ABM becomes a fifth top-level section of the Trackunit branch: `docs/trackunit/abm/`, with its own nav tab and sidebar block (converter: `nav_html`, `sidebar_html`, `detect_section`).
2. The conceptual spine is three layers, not one: ABM-to-partner (win the partner organization), ABM-with-partner (joint campaigns into shared customers), ABM-through-partner (partner as channel: marketplace, co-marketing). The layers map onto the lifecycle stages Source/Qualify, Launch/Adopt, and Scale.
3. The targeting funnel reuses the published landscape scoring (37 candidates, six dimensions, dispositions) instead of inventing a parallel selection. The First Five are the Tier 1 ABM accounts.
4. One data source, `docs/trackunit/abm/data.js` (6 accounts, 42 people, 28 signals, compiled from the account plans), feeds all three interactives: Control Tower, Signal Radar, Relationship Heatmap. This prevents the number drift the Akamai ABSM suffered from.
5. Depth pattern: one full showcase (Procore, highest score) plus five standard play cards. Collateral is six print-ready HTML executive briefs (print CSS, no reportlab dependency).
6. The operating spec is stack agnostic (objects, fields, stage criteria for any CRM) because Trackunit's internal stack is unknown.

## Consequences

- The converter sidebar/nav now has five sections; hand-built pages (memo, spider chart, landscape, credit dashboard) were patched manually with the same block.
- Relationship stages and credit figures are labeled as starting-point estimates and assumptions on every surface; only Point of Rental contacts start above cold, justified by the signed 2025 partnership.
- ADR-012 isolation rules apply unchanged: no links out of `docs/trackunit/` except shared assets and linkedin.com contact links.
- No new people research was run for this section; it reuses the 42 verified names from the account plans (ADR session 2026-07-03). The Apify token is not used and appears nowhere in the repo.
