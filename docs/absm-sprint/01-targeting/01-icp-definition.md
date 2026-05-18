# 01 · ICP Definition

> **Stage 1 deliverable** · D3-2 ABSM Sprint
> **Purpose:** Define exactly which companies belong in the target universe before scoring begins.

---

## Operational Frame: How This ICP Plugs Into the Partner Intelligence Program 🧠

This sprint operates under a **hypothesis overlay**. In a production deployment of the proposed Partner Intelligence Program (PIP), the funnel would be:

```
Akamai 6sense intent + 1st-party telemetry
            ↓
   [Filter: matches ICP criteria below]
            ↓
   "Hot 20 DACH Accounts" — monthly curated list
            ↓
   Axians receives via HubSpot deal-stage import
            ↓
   Pre-built sales kit attached per account
            ↓
   Axians executes outreach
```

**For this sprint**, since we cannot verify actual 6sense signals on specific accounts, the ICP defined below is used to **pre-qualify the universe** of accounts that would be worth flagging when intent fires. Targeting in Stage 1 uses firmographic and public-data criteria only. Intent is marked 🧠 hypothesis throughout downstream artifacts.

---

## ICP — The Target Account Profile

A company belongs in the target universe if it meets **all** of the following:

### 1. Firmographic fit

| Attribute | Criterion |
|-----------|-----------|
| Headquarters | Germany |
| Revenue | €100M–€2B (FY2024 or most recent reported) |
| Employees | 1,000–10,000 |
| Ownership type | Family-owned, Mittelstand, Stiftung (foundation-owned), or private equity portfolio — **excluding** DAX 40 and most MDAX listed |
| Sector | Manufacturing — mechanical engineering, automotive supply (Tier 1/2), machine tools, industrial components, electrical equipment, industrial process, instruments/sensors |

### 2. NIS2 status

The company must qualify as either an **"essential" or "important" entity** under the new BSIG (German NIS2 Implementation Act, in force 6 December 2025). For Mittelstand manufacturers, this typically means:

- Revenue >€10M **OR** >49 employees (almost all targets clear this)
- Sector explicitly listed in NIS2 Annex I or II: mechanical engineering, motor vehicles, medical devices, electrical equipment, or chemicals
- OR: supplier to a critical infrastructure operator (KRITIS contractor relationship)

### 3. OT/IT convergence

The company must have **real operational technology** in its operating model — not just office IT:
- Physical manufacturing or assembly operations
- Connected machinery, robots, PLCs, HMIs, SCADA, or industrial control systems
- IoT or Industry 4.0 initiatives publicly visible (digital twin, smart factory, predictive maintenance, machine-as-a-service)
- Production network distinct from corporate IT, with at least some interconnection between them

**Exclusion:** Pure-software companies, IT services firms, and B2B SaaS — even if they have a German manufacturing customer base — don't qualify. The motion is for companies *that run factories*.

### 4. Below Akamai direct sales coverage

Akamai's direct sales team in DACH typically focuses on:
- DAX 40 constituents
- Large MDAX constituents (>€2B revenue)
- KRITIS operators with their own SOC and dedicated security budget >€10M

Target accounts for this sprint sit **below** that threshold. The implicit ICP message: "If Akamai's named-account team isn't calling you, but you still need enterprise-grade microsegmentation, Axians is the way you get it."

**Exception for the showcase:** Trumpf GmbH (~€5.4B revenue, ~20,000 employees) is **above** this threshold but is included as the named public showcase — a way to demonstrate the methodology against a recognizable manufacturing brand. The remaining 3 accounts will sit firmly in the Mittelstand band.

### 5. Axians reachability (preference, not hard filter)

Bonus weight in scoring is given to companies showing one of:
- Existing Axians or VINCI Energies relationship (publicly disclosed customer, joint event, joint case study)
- Sister-brand connection (Actemium, Omexom, VINCI Facilities engagement)
- Geographic proximity to an Axians office (65 German locations) or to an Axians SOC (Hamburg, Ulm)
- Public co-attendance at industry events (Hannover Messe, it-sa, IFAT)

This isn't a filter that rejects companies — it's a tilt that elevates accounts where the "first phone call" already has a warm bridge.

---

## What We Exclude (negative ICP)

The motion is **not** for:

| Type | Why excluded |
|------|--------------|
| DAX 40 / large MDAX | Already Akamai-direct accounts |
| <€100M revenue | Too small for the deal economics |
| >€2B revenue (except Trumpf showcase) | Above partner-led threshold |
| <1,000 employees | OT footprint typically too small to justify Guardicore commercial |
| Pure software / IT services / SaaS | No physical OT to segment |
| Banking, insurance, professional services | Different motion, different vendor positioning |
| Pharma manufacturing (NIS2 highly regulated already) | Often have mature segmentation; different sales motion |
| Energy / utilities (KRITIS regulated already, IT-SiG 2.0) | Akamai-direct or already advanced |
| Healthcare providers | Different vertical motion |
| Existing Illumio or Akamai customers | Already covered |
| Companies with publicly disclosed mature Zero Trust deployment | Late stage, low convertibility |

---

## Sweet Spot Profile (the "ideal target")

The platonic ideal of this ICP — a company that would score very high on every dimension:

- **A €500M–€1.5B German mechanical engineering or automotive-supply company**, family-owned or Stiftung-owned
- **3,000–6,000 employees**, headquartered in Baden-Württemberg, Bavaria, or NRW
- **Recently launched a digital transformation initiative** (Industrie 4.0, smart factory, IoT) → flat-but-now-connected OT network
- **NIS2 "important entity"** under the new BSIG → fines exposure but not in the "highest-attention" critical bucket
- **No public Illumio or Akamai relationship**, no large internal SOC
- **Geographic proximity** to an Axians office or visible at Hannover Messe / industry events
- **Cybersecurity is publicly on the agenda** — recent annual report mention, a security-related job posting, or a public incident in the sector

---

## What Each Stage 2 Intel File Will Verify

For each shortlisted account, the Stage 2 intel files will confirm or invalidate:

1. **Company brief** — exact revenue/employees/sector codes, parent/owner, key digital transformation initiatives
2. **Pain map** — concrete OT/IT convergence pressure points, any public incidents in the company or peer set, insurance signals, NIS2 statements
3. **Relationship map** — CISO, CTO, OT security lead, plant directors (LinkedIn-verified contacts only)
4. **Axians connection** — concrete evidence of relationship (or absence thereof), warmest realistic entry path

---

**End of Stage 1.1.** Scoring matrix next.
