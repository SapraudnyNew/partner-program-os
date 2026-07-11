# PLAN-bege-rollout-maps

> **Rank: 2 of 5.** Do after `PLAN-newcalling-sprint1-conveyor` (in the `new-calling` repo).
> Why: ADR-007 calls the BEGE rollout map "the strongest single proof point for Alex's RJSM
> positioning" — it is simultaneously a working plan for his current employer (Boon Edam) and
> the portfolio artifact that makes recruiters/CEO-targets take him seriously. All inputs exist
> in this repo; it is the declared next action (`03-boon-edam/00-context.md`, STATE.md). Nothing
> else blocks on it, but it directly serves the top career goal.

## ⚠️ Critical fact discovered during exploration — read before anything else

**This repository became PUBLIC on 2026-07-02** (STATE.md session `repo-going-public`; Pages
would not deploy privately). ADR-007 was written on 2026-05-14 when the repo was PRIVATE and
assumes the internal rollout map (real partner names, EUR figures, internal politics) can live
in git. **It no longer can.** Committing `02-rollout-map-internal.md` with real content to this
repo would publish Boon Edam confidential information to the open internet.

Consequence for this plan: the internal version is written to disk but **gitignored**; only the
sanitized public version is committed. This supersedes the letter (not the intent) of ADR-007's
file layout and must be recorded in a new ADR (Step 8).

## Goal

Produce both BEGE rollout map versions per ADR-007:

1. `03-boon-edam/02-rollout-map-internal.md` — full, BEGE-specific (LOCAL ONLY, gitignored).
2. `03-boon-edam/01-rollout-map-public.md` — sanitized, portfolio-grade (committed).

Plus: a sanitization gate script, the md2html.py template fix, and repo-hygiene corrections
(stale "PRIVATE" claim in MASTER_HANDOVER, missing ADR-014 pointer).

## Read these files FIRST (in this order)

1. `MASTER_HANDOVER.md` (locked context: who Alex is, results to cite, design rules)
2. `STATE.md` — last 6 session entries (append-only log; note `repo-going-public`)
3. `00-decisions/ADR-007-bege-dual-versions.md` (sanitization rules — the contract)
4. `prompts/prompt-bege-rollout.md` (the drafting brief: section structure 1–7 for internal,
   derivation rules for public)
5. `03-boon-edam/00-context.md` (session-1 discovery: current-state table, 3 diagnostic
   conclusions, rollout shape)
6. `03-boon-edam/artifacts/session-1-operations-rows.md` (Stage 5 / Deliver raw material)
7. `01-method/05-deliver.md` and `01-method/00-method-overview.md` (7-stage lifecycle lens)
8. `01-method/appendix/evidence-library.md` (50 principles — cite principles by name in the maps)

## Exact files to touch

| File | Action |
|---|---|
| `.gitignore` | **CREATE or APPEND** — ignore internal map + local banlist |
| `03-boon-edam/02-rollout-map-internal.md` | **CREATE (local only, never committed)** |
| `03-boon-edam/01-rollout-map-public.md` | **CREATE (committed)** |
| `03-boon-edam/banlist.local.txt` | **CREATE (local only, never committed)** |
| `tools/check_bege_public.py` | **CREATE** — sanitization gate |
| `tools/md2html.py` | **EDIT** — one-line hamburger SVG fix |
| `00-decisions/ADR-014-trackunit-moved-and-adr015-internal-artifacts.md` | **CREATE** (see Step 8) |
| `MASTER_HANDOVER.md` | **EDIT** — additive visibility-warning block only |
| `STATE.md` | **EDIT** — append one session entry at the very bottom |

**DO NOT touch:** anything under `docs/` (the live GitHub Pages site is a curated Akamai
application artifact — publishing a BEGE case-study page there is Alex's call, not yours),
`02-akamai/**`, `01-method/**` content, `prompts/**`.

## Implementation order

### Step 1 — gitignore BEFORE writing anything sensitive
Create/append `.gitignore` at repo root:
```
# BEGE internal artifacts — repo is PUBLIC since 2026-07-02, internal versions never in git
03-boon-edam/02-rollout-map-internal.md
03-boon-edam/banlist.local.txt
```
Verify: `git check-ignore -v 03-boon-edam/02-rollout-map-internal.md` prints the rule.
Commit the `.gitignore` change immediately, before Step 3.

### Step 2 — fix `tools/md2html.py`
Line ~87: hamburger SVG has hardcoded `stroke="#fff"`; the shipped site uses
`stroke="currentColor"` (v2 redesign, STATE 2026-05-19-c). Change the template string to
`currentColor`. Do NOT regenerate existing pages (that would churn 54 files for nothing) —
template fix only.

### Step 3 — write the INTERNAL map (`02-rollout-map-internal.md`)
Follow `prompts/prompt-bege-rollout.md` section plan exactly:
1. **Current state** — synthesize the 20-row table in `00-context.md` into prose (cycle 9+ mo,
   mixed channel, portal-without-discipline, all four ops pains, €20–80k orders, CEE/Baltics).
2. **Diagnostic conclusions** — start from the three in `00-context.md`; extend to 5 max, each
   tied to a lifecycle stage and an evidence-library principle.
3. **Rollout phases 30/60/90/180** with explicit go/no-go gates between phases. Sequence by
   impact × dependency, NOT stage order. Given the diagnostics, the defensible sequence is:
   30d = Deliver-stage discipline (handover standard, storage SLA enforcement, AR cadence —
   uses `session-1-operations-rows.md`); 60d = portal gate enforcement + spec-error kill loop;
   90d = partner segmentation (Silver/Gold/Platinum readiness tiers) + enablement; 180d =
   co-sell/expand motions on the stabilized base.
4. **Per-phase changes by lifecycle stage** with RACI (roles: Partner Manager, Sales Ops,
   Finance/AR, Service Lead, Regional Director) and 1–2 KPIs per change.
5. **Risks and mitigation** (min 6, incl. partner tech immaturity — phone-first reality from
   conclusion 3; global-accounts channel conflict at 20–40% of revenue).
6. **Internal capability builds.**
7. **Partner segmentation + communication plan.**

At the very top of the internal file add this box verbatim:
```
> ВНИМАНИЕ / PENDING ALEX INPUT: the drafting prompt requires asking Alex which phase carries
> the most political risk inside Boon Edam before locking the sequence. This draft sequences by
> impact×dependency. When Alex answers, re-order the affected phase and delete this box.
> LOCAL FILE — gitignored. Repo is public; this file must never be committed or pasted into
> issues/PRs.
```
Where a real number/name is needed but unknown, write `[FILL: …]` — never invent partner names
or figures beyond what `00-context.md` states.

### Step 4 — build the local banlist
`03-boon-edam/banlist.local.txt`: one term per line — `Boon Edam`, `BEGE`, every partner/person
name and every exact EUR figure you used in the internal map. (The banlist itself is gitignored
because it would leak the very names it guards.)

### Step 5 — derive the PUBLIC map (`01-rollout-map-public.md`)
Apply ADR-007 rules mechanically: company → "a European premium B2B equipment manufacturer";
partners → generic descriptors; figures → ranges or removed; names/emails → roles; ERP/tools →
"the partner portal"; politics → removed; dates → week numbers. KEEP: 7-stage structure,
diagnostic framework, intervention logic, phased sequence, KPI framework. Byline:
`A. Marushevsky` (repo convention — never "Alex M.").

### Step 6 — sanitization gate
`tools/check_bege_public.py` (stdlib only): reads `03-boon-edam/banlist.local.txt` (if missing:
falls back to built-ins `["Boon Edam", "BEGE"]` and warns), scans ONLY
`03-boon-edam/01-rollout-map-public.md`, case-insensitive; exit 1 with line numbers on any hit,
exit 0 otherwise. Self-test: running it against the INTERNAL file must exit 1 (prove the gate
works), against the public file must exit 0.

### Step 7 — repo hygiene corrections
- `MASTER_HANDOVER.md`: the file forbids rewriting itself, so make an ADDITIVE correction —
  insert directly under the title a short dated block:
  `> ⚠️ CORRECTION 2026-07-11: repo is PUBLIC since 2026-07-02 (see STATE.md session
  repo-going-public; supersedes ADR-001 and the "(PRIVATE)" note below). Never commit
  internal/confidential BEGE material. Homepage PDF exists: docs/memo-alex-m.pdf.`
  Change nothing else in the file.
- `00-decisions/ADR-014-trackunit-moved-and-adr015-internal-artifacts.md`: STATE.md references
  "ADR-014" for the Trackunit removal but no such file exists in this repo (it lives in the
  private hosting repo). Write a 15-line pointer ADR: (a) records that ADR-014 = Trackunit
  campaign moved to private hosting 2026-07-09, content removed in commit `9301491`, history
  intentionally not rewritten; (b) adds the new rule from Step 1: internal-only artifacts are
  gitignored, public repo carries sanitized versions only.

### Step 8 — STATE.md session entry
Append AT THE BOTTOM of the file (append-only convention, newest last):
`## SESSION 2026-07-11 · bege-rollout-maps` — what was written, the gitignore decision and why
(public repo), gate script usage, the open political-risk question for Alex, next action
(Alex reviews internal map → answers political-risk question → optional publication of the
public version to docs/ as a separate decision).

## Edge cases a weaker model would miss

- **E1. The repo is public.** The single most dangerous mistake is committing the internal map
  or the banlist. Gitignore FIRST (Step 1), verify with `git check-ignore`, and re-verify with
  `git status --porcelain` before every commit.
- **E2. `00-context.md` is already committed and public** and contains moderately sensitive BEGE
  discovery data (AR delays, order values, partner counts). Do NOT copy those specifics into the
  public map with more precision than `00-context.md` already exposes; flag this file's
  public status to Alex in your final report (removal/sanitization is HIS decision — it has been
  public since 2026-07-02, so do not unilaterally delete it).
- **E3. The drafting prompt says "ask Alex first" (political risk).** You are running
  autonomously — do not stall: draft with the dependency-based sequence, carry the PENDING box
  (Step 3), and surface the question in STATE + final report.
- **E4. ADR-007 mentions a third target (`/docs/case-study-bege.md`).** Do NOT create it. The
  docs/ site is the live Akamai application; adding BEGE content there changes an
  outward-facing career artifact and needs Alex's go.
- **E5. Style rules from this repo, not intakto:** no em/en dashes in new copy (`—`/`–` — the
  repo's verified convention, see STATE sessions "zero em/en dashes"); name always
  `A. Marushevsky`; English prose (repo language per ADR-002); no Cyrillic in the PUBLIC file
  (the internal file may use RU where quoting Alex).
- **E6. STATE.md is append-only, newest at bottom** — despite the misleading
  `<!-- ADD NEW SESSIONS BELOW THIS LINE -->` comment sitting after the first session, every
  later session was appended at EOF. Append at EOF.
- **E7. MASTER_HANDOVER.md says "never rewrite this file"** — the visibility correction must be
  a clearly-dated additive block, not edits to existing lines.
- **E8. Don't run `tools/md2html.py` over the repo** after fixing it — regeneration would diff
  54 published HTML pages and risk visual regressions on the live site.

## Acceptance criteria (verify each)

1. `git check-ignore 03-boon-edam/02-rollout-map-internal.md` and
   `git check-ignore 03-boon-edam/banlist.local.txt` both succeed.
2. `03-boon-edam/02-rollout-map-internal.md` exists locally with all 7 sections non-empty and
   the PENDING ALEX INPUT box at top; `git log --all --oneline -- 03-boon-edam/02-rollout-map-internal.md`
   is EMPTY (never committed).
3. `03-boon-edam/01-rollout-map-public.md` is committed; contains all 7 sections; contains the
   string "European premium B2B equipment manufacturer"; `python tools/check_bege_public.py`
   exits 0 on it and exits 1 when pointed at the internal file (gate self-test).
4. `grep -P "[—–]" 03-boon-edam/01-rollout-map-public.md` → no matches;
   `grep -c "Alex M\." 03-boon-edam/01-rollout-map-public.md` → 0.
5. `grep -n "currentColor" tools/md2html.py` shows the hamburger template fixed;
   `git diff --stat` shows zero changes under `docs/`.
6. MASTER_HANDOVER.md contains the dated CORRECTION block; ADR-014 pointer file exists;
   STATE.md's last section is `## SESSION 2026-07-11 · bege-rollout-maps`.
7. Final report to Alex lists: (a) the political-risk question, (b) the `00-context.md`
   public-exposure flag, (c) publication of the public map to docs/ as a pending decision.
