# Boon Edam Rollout Map — Context

> **Audience:** Two versions (ADR-007). Internal: BEGE leadership. Public/portfolio: external readers, sanitized.

## What is being rolled out

The Boon Edam Partner Program redesign across seven lifecycle stages. The PDP Summary spreadsheet is the master tracking document; this rollout map is the execution plan for moving from current state to designed state.

## Current state (from session 1 discovery)

| Dimension | Reality |
|---|---|
| Product type | Configurable B2B equipment (revolving doors, security entrances) with installation and recurring service. |
| Sales cycle | 9+ months from first contact to shipment. |
| End customer | Mix of developers, GCs, FMs, SI partners — no single dominant type. |
| Partner channel | Mixed — varies by market between distributors, installers, system integrators. |
| Partner count in Alex's portfolio | 10–30 active. |
| Order placement | Through portal/ERP. |
| Operational pain | All four areas simultaneously: spec errors, logistics delays, AR overdue, site readiness misses. |
| Handover | Document signed but not standardized. |
| Partner PM tools | None — partners work manually and by phone. |
| Project types | Mixed: offices, airports, retail, critical infrastructure. |
| Typical order | €20–80k net revenue to BEGE (excluding partner install margin). |
| Installation | Partner's own crew. |
| Partner margin source | Bundled project margin (product + install + service). |
| Storage risk | Partner takes after pickup, but BEGE rarely enforces storage SLA on delay. |
| AR pain | 15–30 day delays, "manageable" but pattern is hardening. |
| Alex's market | CEE / Baltics. |
| Market variation impact | Moderate — logistics and legal differ, but core process can be unified. |
| Global Accounts | 20–40% of revenue. |

## Three diagnostic conclusions

1. **The cycle is leaking value in multiple places simultaneously.** This isn't a single-stage fix. It's a coordinated multi-stage rollout, not a project.
2. **Portal exists but discipline doesn't.** The transactional infrastructure is in place; what's missing is enforcement of the gates and SLAs that the portal should make automatic.
3. **Partner technological maturity is the binding constraint.** Partners work by phone. Any rollout that assumes Fieldwire-style PM tools at the partner level will fail. Solutions must work with where partners actually are.

## Rollout shape (to be detailed)

The rollout map specifies, by phase:
- Sequence of changes (which stage first, why)
- Pilot vs full rollout decisions per change
- Partner segmentation by readiness (Silver / Gold / Platinum)
- Internal capability builds required
- Risks and mitigation
- Gates between phases

## Why dual versions

Two equally real purposes (ADR-007):
- **Internal version** — what Alex actually executes at Boon Edam.
- **Public version** — sanitized portfolio piece referenced in HVO conversations.

## Documents in this folder

- `00-context.md` — this file
- `01-rollout-map-public.md` — sanitized portfolio version (to be drafted)
- `02-rollout-map-internal.md` — BEGE-specific execution plan (to be drafted)
- `artifacts/` — supporting documents and outputs from sessions

## Next action

Draft `02-rollout-map-internal.md` first. Get it complete and accurate. Then derive `01-rollout-map-public.md` by applying sanitization rules from ADR-007.
