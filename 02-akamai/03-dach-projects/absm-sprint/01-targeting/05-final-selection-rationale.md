# 05 · Final Selection Rationale — The 3 + Trumpf

> **Stage 1 deliverable** · D3-2 ABSM Sprint
> **Purpose:** The 3 deep-dive accounts plus the named showcase. With written defense of why these four and not others.

---

## The Final Four

| Role | Company | Why this one |
|------|---------|--------------|
| **Showcase** | **Trumpf GmbH + Co. KG** | Named, publicly visible, demonstrates the methodology at the highest level of polish |
| **Account 1** | **Hörmann KG** | Existing Axians customer + perfect ICP fit — proves the warm-path motion |
| **Account 2** | **Maschinenfabrik Reinhausen (MR)** | Highest matrix score (86); Industrie 4.0 award winner; NIS2-essential electrical equipment |
| **Account 3** | **Witte Automotive** | Tier 1/2 automotive supplier; different sector + different region; TISAX × NIS2 double-pressure narrative |

Together these four cover four geographies (BW, NRW × 2, BY), four sub-sectors (machine tools, building hardware, electrical/transformer, automotive supplier), and four distinct strategic angles.

---

## The Reconsideration: Why Hörmann Replaced Beckhoff

After completing the matrix scoring, I checked Axians' public customer references on axians.de. **Hörmann KG appears** in their published reference gallery. This is a material discovery the longlist research missed because I didn't cross-reference Axians' customer list against my candidate pool early enough.

Re-scoring Hörmann with the matrix:

| Criterion | Score | Justification |
|-----------|-------|---------------|
| C1 — NIS2 obligation | 4 | "Important entity" — building hardware manufacturer, >€10M turnover, >49 employees |
| C2 — OT/IT convergence | 5 | Heavy OT: 30+ production locations globally, automated door/gate manufacturing, connected products (Hörmann Smart Home, BiSecur radio system) |
| C3 — Revenue band fit | 4 | €1.5B / 6,000 emp — at the upper edge but still in band |
| C4 — Axians reachability | 5 | **Existing Axians customer** — appears on axians.de Referenzen gallery |
| C5 — Security posture | 3 | Public IoT footprint creates attack surface; no public negative signal |

**Total: (4×0.25 + 5×0.25 + 4×0.20 + 5×0.15 + 3×0.15) × 20 = 85**

That score puts Hörmann at #2 in the universe, behind only Reinhausen (86). And critically, its Criterion 4 score of 5 is essentially uncontested — no other candidate has confirmed Axians-customer status.

**Lesson:** When the partner-led motion is the point, the most valuable single signal is "is this already an Axians customer?" That signal trumps minor differences in technical fit elsewhere on the matrix. I should have queried Axians' reference page first, before building the longlist.

---

## Why these four, account by account

### Trumpf GmbH + Co. KG — the showcase

**Profile:** ~€5.4B revenue, ~20,000 employees, family-owned (Berthold Leibinger family), HQ in Ditzingen, Baden-Württemberg. World leader in laser cutting machines and laser processing. Major positions in machine tools, electronics, and EUV laser sources (only TRUMPF makes the lasers ASML uses for chip lithography).

**Why showcase, not regular account:**
- ABOVE the partner-led band (revenue >€2B, employees >10,000) — formally Akamai-direct territory
- BUT: a publicly named, recognizable German manufacturer, perfect for demonstrating depth
- Family-owned, headquartered in Ditzingen, exemplifies the Mittelstand spirit even at scale
- High public visibility → "they've done their homework" effect for the portfolio reader

**Why Guardicore fits Trumpf specifically:**
- Trumpf machines run on TCP/IP and connect into customer factory floors via Industry 4.0 platforms (TruConnect)
- The company's own production network has the same OT/IT convergence pain as smaller Mittelstand
- A factory floor incident at Trumpf has cascade risk through the EUV/laser supply chain → very high public interest
- The NVIDIA BlueField agentless OT solution (GA Q2 2026) is purpose-built for exactly Trumpf's "un-agentable industrial equipment" situation

**Why naming it publicly is safe:**
- All data used is from public annual reports, press releases, and product documentation
- No proprietary information; no confidential intelligence; no inferred competitive positioning beyond what Trumpf itself has publicly stated
- The treatment will be marked clearly as a worked example, not an active sales engagement

---

### Account 1 — Hörmann KG (Steinhagen, NRW)

**Profile:** Family-owned (3rd generation, Hörmann family), ~€1.5B revenue, ~6,000 employees, 30+ production locations globally, HQ in Steinhagen near Bielefeld in North Rhine-Westphalia. World market leader in residential and industrial doors, gates, and access systems. Significant IoT footprint via BiSecur radio system and Hörmann Smart Home platform.

**Why this account:**
- **Already an Axians customer** (axians.de Referenzen gallery, confirmed) — gives the strongest possible Criterion 4 score and the warmest realistic outreach path
- **Perfect ICP fit on band, sector, and family-ownership criteria** — exactly the Mittelstand profile the sprint targets
- NRW location → different region from Trumpf (BW), strengthening geographic narrative
- **IoT-heavy product line** → creates a unique angle: their *products* (smart gates, IoT openers) are themselves potential attack surfaces, raising consciousness about microsegmentation in their own production environment
- Strong public Industrie 4.0 narrative; multiple smart-factory press releases

**Why this gives the sprint a unique story:**
Hörmann represents the partner-cross-sell motion in its purest form. Axians already has a relationship; Akamai needs to find a way to enter via Axians. The motion isn't "find a new account" but "deepen an existing account with a new technology line." This is exactly the PIP architecture — except instead of intent signals routing a *new* account to Axians, the value is in identifying that an *existing* account has a Guardicore-shaped problem.

**Hypothesis (🧠) flagged for Stage 2 verification:**
- The exact services Axians provides Hörmann (Network? Cloud? SOC?) — verify in Stage 2 intel
- Whether Hörmann has a security incident in their public record or in industry peer-set
- Whether their current Axians account manager is in the cybersecurity org or another portfolio area

---

### Account 2 — Maschinenfabrik Reinhausen (MR), Regensburg, BY

**Profile:** Privately held (Geier family + foundation structure), €630M revenue, 2,700 employees. World leader in on-load tap-changers for power transformers — equipment that lets transformers adjust voltage under load, critical to every modern electrical grid. **First German company to receive the German Industrie 4.0 Award.** Headquartered in Regensburg, Bavaria.

**Why this account:**
- **Highest matrix score** (86) of any in-band company
- **Classic NIS2 essential entity** — electrical equipment for grids; their products are deployed in KRITIS infrastructure operated by their customers
- The Industrie 4.0 award is publicly cited — they've publicly committed to data-driven manufacturing, which means their production network is connected (and exposed)
- Bavaria location → geographic complement to Trumpf (BW) and Hörmann (NRW)
- Their customers are utility companies → MR's own supply-chain compliance with NIS2 directly affects whether their utility customers can stay compliant — they're under regulatory pressure twice over
- ~3,000 employees, family-owned: textbook Mittelstand profile

**The narrative hook:**
"You won the Industrie 4.0 award for connecting your factory floor to the cloud. Now you have to prove to the BSI and to your utility customers that you can keep it segmented under NIS2."

This is the cleanest example in the sprint of an account that *succeeded* at digital transformation and now needs to *secure* what they connected.

---

### Account 3 — Witte Automotive, Velbert, NRW

**Profile:** Privately held (Gölz family + management), €664M revenue, 4,179 employees. Tier 1/2 automotive supplier specializing in mechatronic locking systems for car doors, tailgates, interiors, and seats. Operates outside Europe as Vast Automotive Group. Headquartered in Velbert, North Rhine-Westphalia.

**Why this account:**
- **Pure automotive supplier perspective** — different from Trumpf (machine tools to industry), Hörmann (consumer building hardware), and Reinhausen (electrical equipment)
- **Double regulatory pressure**: NIS2 ("motor vehicle manufacturer") + TISAX (German automotive industry cyber standard) + OEM customer cyber requirements cascading down the supply chain
- **Mechatronics manufacturer = inherent IT/OT convergence**: their products are themselves cyber-physical systems (electronic locking, body electronics)
- 4,179 employees, family-controlled, NRW location
- Automotive supply chain is publicly under cybersecurity scrutiny — multiple high-profile German supplier ransomware events in 2023–2025

**The narrative hook:**
"Your OEM customers' TISAX audits now demand documented network segmentation from suppliers. NIS2 requires the same thing from a different angle. Guardicore lets you prove both with one platform."

This account demonstrates the supply-chain compliance angle — accounts where the buying motivation isn't only their own risk, but their customers' compliance requirements pushing down.

---

## Why these three together, not other combinations

The combinations I evaluated:

**Option A (chosen):** Hörmann + MR + Witte
- Geographic spread: NRW + BY + NRW ✓
- Sub-sector spread: Building hardware / Electrical / Automotive ✓✓
- Narrative spread: Existing customer cross-sell + Industrie 4.0 success + Supply chain cascade ✓✓
- Axians warm path: 1 confirmed, 2 cold ✓ (realistic)
- Score range: 82-86 ✓ (all tier 1)

**Option B:** Schunk + Wittenstein + Beckhoff
- All Tier 1 scorers (84, 84, 82), but...
- All in components/automation → narrative overlap
- All family-owned-ish but no Axians-customer angle
- Lower compelling differentiation
- Rejected

**Option C:** MR + Pilz + Harro Höfliger
- Scores 86, 80, 78 — all tier 1
- BY + BW + BW → too concentrated geographically
- Pharma packaging is interesting (dual-regulation) but Pilz and Harro both BW → no NRW representation
- Rejected

**Option D:** MR + Witte + Beckhoff
- Pure top scorers
- BY + NRW + NRW
- Beckhoff is an automation vendor selling TO manufacturers — its own production may be more advanced than typical Mittelstand; story is harder to tell
- Rejected in favor of A's Hörmann warm-path

---

## What the four together demonstrate (the narrative arc)

When read in sequence, the four accounts demonstrate the full ABSM motion:

1. **Trumpf** (showcase): "Here's how we'd treat the visible flagship — methodology at maximum polish"
2. **Hörmann** (warm-path): "Here's how we use an existing Axians relationship to introduce Guardicore"
3. **Reinhausen** (cold-but-bullseye): "Here's how we target a perfect-fit account where Axians has no current presence"
4. **Witte Automotive** (compliance cascade): "Here's how the regulatory environment pulls Guardicore into accounts that wouldn't have asked"

Each represents a different play in the partner-led motion playbook. Together they form a coherent argument that the PIP architecture is worth building.

---

## What Stage 2 will verify or invalidate

For each of the four:

**Trumpf:**
- Verify the public CISO/IT-security leadership (likely identifiable on LinkedIn)
- Confirm 2024 financials and current production-network architecture statements
- Identify any Akamai-Trumpf historical engagement (very low probability of direct customer)

**Hörmann:**
- Verify exactly what Axians delivers to Hörmann today (Stage 2 priority research)
- Identify the Axians account manager (likely findable via LinkedIn)
- Confirm current security tooling on the Hörmann side

**Maschinenfabrik Reinhausen:**
- Verify 2024 revenue and headcount (the €630M figure is from 2015–2018; could have grown or shrunk)
- Identify IT/security leadership at Reinhausen
- Confirm the Industrie 4.0 connected-factory architecture; specifically what cloud and what production-network design

**Witte Automotive:**
- Confirm 2024 revenue (the €664M is 2022)
- Identify TISAX status and current OEM customer security audits
- Locate IT and OT security decision-makers

---

## What we lose by not picking other strong candidates

The honest cost of choosing these three:

- **Schunk Group** (score 84) — would have been perfect, but no Axians angle and similar profile to Wittenstein
- **Wittenstein SE** (score 84) — strong mechatronics story, but overlaps with Witte's mechatronic angle
- **Beckhoff Automation** (score 82) — they ARE automation; their own factory floor is probably already best-in-class
- **Lenze SE** (score 80) — drives is a strong segment but no differentiated story vs. the others
- **Pilz GmbH** (score 80) — would have given the "safety vendor securing themselves" irony, but too similar in size profile to Reinhausen

If any of the top three for some reason becomes unfeasible in Stage 2 (e.g., Hörmann turns out not to be a current Axians customer, or has a recently announced competitor relationship), the backup order is: **Pilz → Schunk → Wittenstein → Lenze.**

---

## Checkpoint summary

| Account | Score | Why included | What Stage 2 will deepen |
|---------|-------|--------------|--------------------------|
| **Trumpf** (showcase) | n/a — editorial inclusion | Recognized public name, perfect for portfolio depth | Public leadership, NIS2 statements, Industrie 4.0 platform |
| **Hörmann KG** | 85 | Existing Axians customer + ICP fit | Exact Axians services delivered, AM relationship, IoT footprint |
| **Maschinenfabrik Reinhausen** | 86 | Highest scorer; Industrie 4.0 award winner | Current financials, IT/OT leadership, NIS2 status |
| **Witte Automotive** | 82 | Auto supplier angle; TISAX × NIS2 double-pressure | TISAX status, OEM cascade pressure, security org |

**End of Stage 1.** Awaiting your approval to proceed to Stage 2 intel (16 deep-dive files, 4 per account).
