# Pain Pattern Library

Recurring pain patterns identified across German Mittelstand manufacturing through public research (incident reports, NIS2 guidance documents, industry association publications).

---

## Pattern 1: The NIS2 Audit Problem

**The pain:** "My auditor is asking for evidence of network segmentation. I don't know what I have."

**Who feels it:** CISO, compliance manager  
**Urgency:** High — NIS2 enforcement started Q4 2024 in Germany  
**What they're currently doing:** Asking their SI (Axians) to help them figure out what "segmentation" means in practice

**Guardicore answer:** Visibility first (network map), then segmentation policy enforcement. Auditor-ready reporting built in.

---

## Pattern 2: The OT/IT Convergence Risk

**The pain:** "We connected our factory floor to the corporate network for Industry 4.0. Now our security team is terrified. We can't put firewalls between PLCs and the corporate network without stopping production."

**Who feels it:** IT Director, OT Engineer, Production Manager  
**Urgency:** Medium-high — no incident yet, but awareness is high  
**What they're currently doing:** Separate VLAN + "air gap by convention" (which is not real segmentation)

**Guardicore answer:** Agentless deployment — no software on PLCs, no firewall reconfiguration. Works at the network layer, maps OT traffic, applies policies without touching production configuration.

---

## Pattern 3: The Post-Incident Urgency

**The pain:** "We got hit. We paid the ransom. We have budget now. We need to make sure it doesn't happen again."

**Who feels it:** CEO, CISO, board  
**Urgency:** Immediate — post-incident window typically 3–6 months before urgency fades  
**What they're currently doing:** Buying EDR, SIEM, backups. Missing lateral movement prevention.

**Guardicore answer:** Lateral movement prevention is the core value proposition. If Ryuk or similar ransomware enters via email, Guardicore contains it to the initial endpoint rather than letting it spread to ERP and backup systems.

---

## Pattern 4: The TISAX Burden

**The pain:** "Our OEM just told us our TISAX Level 3 assessment is next quarter. We need to show information security controls including network segmentation."

**Who feels it:** IT Security Lead, Quality Manager (in automotive)  
**Urgency:** Hard deadline — TISAX audit is date-specific  
**What they're currently doing:** Scrambling. TISAX requirements are specific and auditor-verified.

**Guardicore answer:** Maps directly to TISAX IS domains covering network separation and monitoring. Deployment timeline (4–8 weeks) is compatible with pre-audit sprint.

---

## Pattern 5: The SAP Migration Gap

**The pain:** "We're migrating to S/4HANA. Our consultant says we should segment the SAP environment from the rest of the network, but nobody knows how."

**Who feels it:** CIO, SAP project lead, security architect  
**Urgency:** Project-driven — depends on migration timeline  
**What they're currently doing:** Discussing with SAP consultants who are not security specialists

**Guardicore answer:** SAP-specific segmentation policies are pre-built. Guardicore can isolate the S/4HANA environment during and after migration with policy templates.

---

*Pain patterns from public sources: BSI reports, NIS2 guidance, TISAX documentation, VDI conference proceedings. May 2026.*
