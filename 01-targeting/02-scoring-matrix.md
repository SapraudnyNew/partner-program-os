# 02 · Scoring Matrix

> **Stage 1 deliverable** · D3-2 ABSM Sprint
> **Purpose:** Translate ICP into a numerical scoring system. Apply to longlist → produce shortlist.

---

## Scoring Philosophy

Five criteria, each scored **0–5**, with explicit weights. Maximum raw score: 100 points.

**Design principles:**
1. Weights reflect business value to Axians + Akamai, not just data availability
2. NIS2 obligation strength is the strongest signal (highest weight) — it's both regulatory pressure and budget-unlocking
3. OT/IT convergence is the second-strongest — it's the actual technical fit for Guardicore
4. Axians reachability is meaningful but not dispositive — a perfect-fit account with no Axians relationship is still worth pursuing
5. Public cyber incident history is weighted carefully — too high and we punish quiet competence

---

## The Five Criteria

### Criterion 1 — NIS2 Obligation Strength **(weight: 25%)**

How clearly is this company an obligated entity under the German NIS2 Implementation Act, and how much regulatory pressure are they under right now?

| Score | Definition |
|-------|------------|
| 5 | Clearly an **essential entity** (large company, mechanical engineering, motor vehicle, medical device, or electrical equipment manufacturer); explicit public NIS2 statements or registration confirmed |
| 4 | Almost certainly **important entity**; sector explicitly in scope, size threshold cleared; some public NIS2 discussion |
| 3 | Likely in scope (sector match, size cleared); no public NIS2 statements yet |
| 2 | Probably in scope but boundary case (sector adjacent, size near threshold) |
| 1 | Marginal applicability (e.g. small subsidiary of foreign parent) |
| 0 | Not in NIS2 scope |

### Criterion 2 — OT/IT Convergence Level **(weight: 25%)**

How real is the operational technology footprint, and how exposed is it to lateral movement from the corporate network?

| Score | Definition |
|-------|------------|
| 5 | Heavy OT footprint (multiple plants, connected machinery, public Industrie 4.0 strategy, IoT platform, smart factory initiative); known IT/OT integration projects |
| 4 | Significant OT footprint (1+ plant, connected production, machine-to-cloud telemetry); digital-transformation projects visible |
| 3 | Standard manufacturing OT (PLCs, SCADA in plant, but limited cloud integration); minimal public Industrie 4.0 narrative |
| 2 | Light OT (assembly only, mostly office IT environment) |
| 1 | Very light (light assembly or distribution only) |
| 0 | No OT footprint |

### Criterion 3 — Revenue Band Fit **(weight: 20%)**

How well does the company sit in the €100M–€2B, 1K–10K employee sweet spot for partner-led motion?

| Score | Definition |
|-------|------------|
| 5 | €300M–€1B revenue, 2,000–6,000 employees — the platonic sweet spot |
| 4 | €100M–€300M or €1B–€1.5B; 1,500–8,000 employees — solid fit |
| 3 | At the edges of the band (€100M–€150M or €1.5B–€2B) |
| 2 | Just outside the band but compelling (€2B–€2.5B and strong other signals, or €80M–€100M and strong other signals) |
| 1 | Outside the band, included only for showcase or special reason |
| 0 | Far outside band, not viable |

### Criterion 4 — Axians Reachability **(weight: 15%)**

How warm is the path from Axians' first call to a meaningful conversation?

| Score | Definition |
|-------|------------|
| 5 | Existing public Axians or VINCI Energies customer relationship (Axians.de reference, joint case study, joint event with leadership visibility) |
| 4 | Sister-brand relationship (Actemium, Omexom, VINCI Facilities) or close geographic proximity to an Axians office + plant in same Bundesland |
| 3 | Public co-attendance at industry events with Axians (Hannover Messe, it-sa); LinkedIn second-degree connections likely |
| 2 | No known relationship but geographic match (plant near Axians office) |
| 1 | No known signal but reachable via cold outreach |
| 0 | Hostile signal — known competitor relationship, prior Axians escalation, public preference for other ICT integrator |

### Criterion 5 — Security Posture Signals **(weight: 15%)**

Are there public signals that the company is *aware* and *willing* — not necessarily that they've already been breached?

| Score | Definition |
|-------|------------|
| 5 | Multiple recent signals: CISO hiring posts, cybersecurity job postings, public statements on NIS2/Zero Trust/OT security, recent supplier or peer breach disclosure |
| 4 | One or two strong signals (recent CISO hire, public OT security commentary, NIS2 ISMS project) |
| 3 | General digital-transformation signals + sector peer pressure, but nothing security-specific |
| 2 | Quiet on security topics publicly |
| 1 | Very quiet, no public signals at all (still viable but harder to time) |
| 0 | Public statements of "we have it covered" or recent vendor commitment to a competitor |

**Note on this criterion:** Companies that have *suffered* a public breach are not penalized — they're sometimes the highest-converting prospects post-incident. But the cost is awkward outreach. We let the intel stage (Stage 2) decide how to handle.

---

## The Math

```
Total Score = (C1 × 0.25) + (C2 × 0.25) + (C3 × 0.20) + (C4 × 0.15) + (C5 × 0.15)
            × 20    [to express as percentage]
```

**Maximum possible:** 100 (every criterion at 5)
**Strong shortlist threshold:** ≥ 70
**Final 3 cutoff:** typically ≥ 75 with positive Stage 2 verification

---

## Cross-Cutting Tiebreakers

When two accounts tie on total score, prefer the one that:
1. Has stronger NIS2-obligation pressure (more time-sensitive deal)
2. Has clearer Axians warm-path (faster execution)
3. Has more accessible identifiable CISO/CTO (more actionable outreach)
4. Is geographically closer to an Axians SOC (Hamburg, Ulm) — easier service delivery
5. Has a Bundesland match with VINCI Energies branch density

---

## What This Matrix Does Not Score

By design, this scoring system **does not** include:

- **Intent signals** — explicitly excluded per Decision D-03 (intent is a separate hypothesis overlay, not a scoring dimension)
- **Deal size estimates** — handled in Stage 4 business cases
- **Competitive incumbency depth** — handled in Stage 2 tech-stack intel
- **Buying committee complexity** — handled in Stage 2 relationship map

Keeping the matrix to five criteria makes it readable, defensible, and easy to audit. More criteria would create the illusion of precision without adding signal.

---

## Validation Check (sanity examples)

To verify the matrix discriminates well, here's how three reference profiles would score:

### Example A — Strong fit
- "€800M family-owned automotive supplier, 5,000 employees, NRW; smart factory press releases; recent CISO LinkedIn post; uses Actemium for automation"
- C1: 5 (clear NIS2), C2: 5 (heavy OT), C3: 5 (sweet spot), C4: 4 (Actemium link), C5: 5 (strong signals)
- **Score: (5×0.25 + 5×0.25 + 5×0.20 + 4×0.15 + 5×0.15) × 20 = 96**

### Example B — Borderline
- "€200M instrumentation maker, 1,500 employees, BW; very quiet publicly; no known Axians relationship"
- C1: 3, C2: 3, C3: 4, C4: 1, C5: 1
- **Score: (3×0.25 + 3×0.25 + 4×0.20 + 1×0.15 + 1×0.15) × 20 = 52**

### Example C — Showcase (Trumpf-like)
- "€5.4B family-owned machine tools, 20,000 employees, BW; Industrie 4.0 leader; CISO publicly identified; no Axians relationship"
- C1: 5, C2: 5, C3: 2 (above band), C4: 1, C5: 4
- **Score: (5×0.25 + 5×0.25 + 2×0.20 + 1×0.15 + 4×0.15) × 20 = 73**

The matrix correctly identifies Example A as the strongest fit, Example B as borderline, and Example C (Trumpf-like) as score-eligible but flagged by the revenue-band criterion as out-of-standard for partner-led motion. This is the intended behavior — Trumpf is included by **editorial decision** as the showcase, not by matrix-forced ranking.

---

**End of Stage 1.2.** Longlist research next.
