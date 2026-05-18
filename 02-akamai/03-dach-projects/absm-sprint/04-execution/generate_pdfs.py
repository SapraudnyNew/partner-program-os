"""
ABSM Sprint – Stage 4 Execution Arsenal
Generates all 12 Axians-branded PDFs.
Axians brand: #0068B6 (primary blue), #AC006D (magenta), white, dark grey
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm, cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether, PageBreak
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfgen import canvas as canvasm

# ─── Brand colours ───────────────────────────────────────────────────────────
AXIANS_BLUE   = colors.HexColor("#0068B6")
AXIANS_MAG    = colors.HexColor("#AC006D")
DARK_GREY     = colors.HexColor("#333333")
MID_GREY      = colors.HexColor("#666666")
LIGHT_GREY    = colors.HexColor("#F0F4F8")
WHITE         = colors.white
BLACK         = colors.black

OUTPUT_DIR = "/home/claude/04-execution"
os.makedirs(OUTPUT_DIR, exist_ok=True)

W, H = A4   # 595 × 842 pt

# ─── Reusable styles ─────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

def S(name, **kw):
    """Create or clone a paragraph style."""
    base = styles.get(name, styles["Normal"])
    return ParagraphStyle(name + str(id(kw)), parent=base, **kw)

TITLE_STYLE  = S("Normal", fontSize=22, textColor=WHITE,    leading=26, fontName="Helvetica-Bold")
H1_STYLE     = S("Normal", fontSize=14, textColor=AXIANS_BLUE, leading=18, fontName="Helvetica-Bold", spaceAfter=4)
H2_STYLE     = S("Normal", fontSize=11, textColor=AXIANS_MAG,  leading=14, fontName="Helvetica-Bold", spaceAfter=3)
BODY_STYLE   = S("Normal", fontSize=9,  textColor=DARK_GREY,   leading=13, spaceAfter=4)
SMALL_STYLE  = S("Normal", fontSize=8,  textColor=MID_GREY,    leading=11)
BOLD_STYLE   = S("Normal", fontSize=9,  textColor=DARK_GREY,   leading=13, fontName="Helvetica-Bold")
WHITE_STYLE  = S("Normal", fontSize=9,  textColor=WHITE,       leading=13)
FOOT_STYLE   = S("Normal", fontSize=7,  textColor=MID_GREY,    leading=10)
BULLET_STYLE = S("Normal", fontSize=9,  textColor=DARK_GREY,   leading=13, leftIndent=12, spaceAfter=3,
                 bulletIndent=0, bulletText="•")

def bullet(text):
    return Paragraph(f"<bullet>&bull;</bullet> {text}", BULLET_STYLE)

def h1(text):  return Paragraph(text, H1_STYLE)
def h2(text):  return Paragraph(text, H2_STYLE)
def body(text):return Paragraph(text, BODY_STYLE)
def bold(text):return Paragraph(text, BOLD_STYLE)
def sp(h=6):   return Spacer(1, h)
def hr(col=AXIANS_BLUE, w=0.5): return HRFlowable(width="100%", thickness=w, color=col, spaceAfter=4)

def tag_cell(text, bg=AXIANS_BLUE, fg=WHITE):
    """Small coloured tag for tables."""
    return Paragraph(f"<font color='#{bg.hexval()[2:] if hasattr(bg,'hexval') else '0068B6'}'>{text}</font>",
                     S("Normal", fontSize=8, textColor=bg, fontName="Helvetica-Bold"))

# ─── Page-template helpers ────────────────────────────────────────────────────

def make_header_footer(title_text, subtitle_text, filename):
    """Return an onPage / onLaterPages callable pair for a document."""

    def _first(c, doc):
        c.saveState()
        # Blue header bar
        c.setFillColor(AXIANS_BLUE)
        c.rect(0, H - 70, W, 70, fill=1, stroke=0)
        # Magenta accent stripe
        c.setFillColor(AXIANS_MAG)
        c.rect(0, H - 75, W, 5, fill=1, stroke=0)
        # Title
        c.setFont("Helvetica-Bold", 18)
        c.setFillColor(WHITE)
        c.drawString(20*mm, H - 45, title_text)
        # Subtitle
        c.setFont("Helvetica", 10)
        c.drawString(20*mm, H - 62, subtitle_text)
        # Axians wordmark (text approximation)
        c.setFont("Helvetica-Bold", 14)
        c.drawRightString(W - 20*mm, H - 48, "axians")
        c.setFont("Helvetica", 8)
        c.setFillColor(AXIANS_MAG)
        c.drawRightString(W - 20*mm, H - 62, "part of VINCI Energies")
        # Footer
        _footer(c, doc)
        c.restoreState()

    def _footer(c, doc):
        c.setFillColor(LIGHT_GREY)
        c.rect(0, 0, W, 22, fill=1, stroke=0)
        c.setFillColor(AXIANS_BLUE)
        c.rect(0, 20, W, 2, fill=1, stroke=0)
        c.setFont("Helvetica", 7)
        c.setFillColor(MID_GREY)
        c.drawString(20*mm, 8, "Axians Deutschland · axians.de · IT Security Services · confidential")
        c.drawRightString(W - 20*mm, 8, f"Page {doc.page}")

    def _later(c, doc):
        c.saveState()
        # Slim header for subsequent pages
        c.setFillColor(AXIANS_BLUE)
        c.rect(0, H - 25, W, 25, fill=1, stroke=0)
        c.setFillColor(AXIANS_MAG)
        c.rect(0, H - 27, W, 2, fill=1, stroke=0)
        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(WHITE)
        c.drawString(20*mm, H - 18, title_text)
        c.setFont("Helvetica-Bold", 9)
        c.drawRightString(W - 20*mm, H - 18, "axians")
        _footer(c, doc)
        c.restoreState()

    return _first, _later


def build_pdf(filename, title, subtitle, story_fn):
    path = os.path.join(OUTPUT_DIR, filename)
    first_page, later_pages = make_header_footer(title, subtitle, filename)
    doc = SimpleDocTemplate(
        path, pagesize=A4,
        topMargin=85, bottomMargin=30,
        leftMargin=20*mm, rightMargin=20*mm
    )
    story = story_fn()
    doc.build(story, onFirstPage=first_page, onLaterPages=later_pages)
    print(f"  ✓  {filename}")
    return path


# ═══════════════════════════════════════════════════════════════════════════════
# 1. NIS2 ARTICLE 21 SEGMENTATION BRIEF
# ═══════════════════════════════════════════════════════════════════════════════
def pdf_01():
    def story():
        s = []
        s += [h1("NIS2 Obligates Network Segmentation — Here Is What That Means"), hr(), sp()]
        s += [body("The German NIS2 Implementation Act (BSIG) entered into force on 6 December 2025. "
                   "Registration deadlines passed on 6 March 2026. For manufacturers classified as "
                   "<b>important or essential entities</b>, §30 BSIG requires documented risk-management measures "
                   "including explicit network segmentation controls."), sp()]
        s += [h2("What Article 21 Requires (§30 BSIG)")]
        reqs = [
            ("21.5", "Security in network and information systems — acquisition, development, maintenance",
             "Segmentation policies per environment (OT, corporate IT, cloud)"),
            ("21.9", "Access control, asset management, multi-factor authentication",
             "Least-privilege east-west enforcement; documented workload inventory"),
            ("21.4", "Supply chain security — direct suppliers and service providers",
             "Proof that third-party access is segmented from production"),
            ("21.2", "Incident handling — 24h / 72h / 1-month reporting cascade",
             "Network flow logs for forensic reconstruction of incidents"),
        ]
        tdata = [["Article", "Obligation", "Segmentation evidence required"]]
        for ref, ob, ev in reqs:
            tdata.append([ref, ob, ev])
        t = Table(tdata, colWidths=[25*mm, 75*mm, 65*mm])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), AXIANS_BLUE),
            ("TEXTCOLOR",  (0,0), (-1,0), WHITE),
            ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
            ("FONTSIZE",   (0,0), (-1,-1), 8),
            ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT_GREY]),
            ("GRID", (0,0), (-1,-1), 0.4, colors.HexColor("#DDDDDD")),
            ("VALIGN", (0,0), (-1,-1), "TOP"),
            ("TOPPADDING", (0,0), (-1,-1), 4),
            ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ]))
        s += [t, sp(10)]
        s += [h2("The Triple Obligation Pattern")]
        s += [body("German Mittelstand manufacturers typically face NIS2 compliance pressure from <b>three simultaneous directions</b>:")]
        triple = [
            ("Own NIS2 obligation", "Manufacturer is directly obligated as important entity (§28 BSIG)"),
            ("KRITIS customer cascade", "KRITIS operators audit suppliers under KRITIS-Dachgesetz (2025)"),
            ("TISAX / OEM cascade", "Automotive OEM customers require network segmentation evidence per TISAX 6.0"),
        ]
        tdata2 = [["Layer", "Source", "What is demanded"]]
        for l, src in triple:
            tdata2.append(["", l, src])
        tdata2[1][0] = "1"
        tdata2[2][0] = "2"
        tdata2[3][0] = "3"
        t2 = Table(tdata2, colWidths=[12*mm, 60*mm, 93*mm])
        t2.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), AXIANS_MAG),
            ("TEXTCOLOR",  (0,0), (-1,0), WHITE),
            ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
            ("FONTSIZE",   (0,0), (-1,-1), 8),
            ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT_GREY]),
            ("GRID", (0,0), (-1,-1), 0.4, colors.HexColor("#DDDDDD")),
            ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
            ("ALIGN", (0,0), (0,-1), "CENTER"),
            ("FONTNAME", (0,1), (0,-1), "Helvetica-Bold"),
            ("TEXTCOLOR", (0,1), (0,-1), AXIANS_MAG),
        ]))
        s += [t2, sp(10)]
        s += [h2("How Guardicore Satisfies All Three Audits from One Platform")]
        s += [bullet("Automated flow maps per environment — exportable for NIS2 auditor, TISAX assessor, and KRITIS inspector")]
        s += [bullet("Traffic logs with process-level granularity — forensic-ready for 24h/72h incident reporting")]
        s += [bullet("Policy enforcement with change history — demonstrates ongoing control, not a point-in-time screenshot")]
        s += [bullet("Agentless OT coverage via NVIDIA BlueField DPU (GA Q2 2026) — PLCs, KUKA robots, HMIs included without disruption")]
        s += [sp(10), hr(AXIANS_MAG)]
        s += [body("<b>Axians IT Security Services</b> · NIS2 readiness assessments · Guardicore deployment · Managed microsegmentation · "
                   "Contact: info@axians.de · <link href='https://axians.de/cybersecurity'>axians.de/cybersecurity</link>")]
        return s
    return build_pdf("01-nis2-segmentation-brief.pdf",
                     "NIS2 & Network Segmentation",
                     "Article 21 obligations for German manufacturers — May 2026", story)


# ═══════════════════════════════════════════════════════════════════════════════
# 2. TRIPLE OBLIGATION POSTER
# ═══════════════════════════════════════════════════════════════════════════════
def pdf_02():
    def story():
        s = []
        s += [sp(10)]
        # Big visual table showing the three layers
        layers = [
            ("LAYER 1", "Own NIS2 Obligation",
             "§30 BSIG — direct obligation\nas important or essential entity",
             "Deadline: BSI audit from 2026",
             AXIANS_BLUE),
            ("LAYER 2", "KRITIS Customer Cascade",
             "KRITIS-Dachgesetz (2025) —\nsupplier security audits by KRITIS operators",
             "Doors in fire stations. Valves in water plants.\nSoftware in substations.",
             AXIANS_MAG),
            ("LAYER 3", "OEM / TISAX Cascade",
             "TISAX 6.0 (May 2024) —\nautomotive OEM supplier security requirements",
             "VW, BMW, Mercedes, Stellantis\nrequire documented segmentation",
             colors.HexColor("#005A9E")),
        ]
        for tag, title_t, desc, example, col in layers:
            row = [[
                Paragraph(f"<font color='white'><b>{tag}</b></font>",
                          S("Normal", fontSize=11, textColor=WHITE, fontName="Helvetica-Bold", alignment=TA_CENTER)),
                Paragraph(f"<b>{title_t}</b>", S("Normal", fontSize=12, textColor=col, fontName="Helvetica-Bold")),
            ]]
            t = Table(row, colWidths=[28*mm, 137*mm])
            t.setStyle(TableStyle([
                ("BACKGROUND", (0,0), (0,0), col),
                ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                ("TOPPADDING", (0,0), (-1,-1), 8),
                ("BOTTOMPADDING", (0,0), (-1,-1), 8),
                ("LEFTPADDING", (0,0), (0,0), 6),
                ("ROWBACKGROUNDS", (1,0), (1,0), [LIGHT_GREY]),
            ]))
            s.append(t)
            s.append(Paragraph(f"   {desc}", BODY_STYLE))
            s.append(Paragraph(f"   <i>Example: {example}</i>", SMALL_STYLE))
            s.append(sp(8))

        s += [hr(), sp(6)]
        s += [h1("One Platform. Three Audits Satisfied.")]
        s += [body("Akamai Guardicore Segmentation, delivered by Axians IT Security Services, produces the "
                   "segmentation maps, enforcement logs, and compliance documentation that satisfies all "
                   "three audit tracks simultaneously.")]
        s += [sp(8)]
        kpi = [
            ["152%", "ROI", "Forrester TEI for comparable manufacturer"],
            ["6 months", "Payback", "From deployment to positive return"],
            ["€9.6M", "3-year benefit", "Composite €1B/5,000-emp manufacturer"],
            ["€0", "Production disruption", "Agentless OT deployment"],
        ]
        t2 = Table(kpi, colWidths=[35*mm, 35*mm, 95*mm])
        t2.setStyle(TableStyle([
            ("FONTNAME", (0,0), (1,-1), "Helvetica-Bold"),
            ("FONTSIZE", (0,0), (0,-1), 16),
            ("FONTSIZE", (1,0), (1,-1), 9),
            ("FONTSIZE", (2,0), (2,-1), 9),
            ("TEXTCOLOR", (0,0), (0,-1), AXIANS_BLUE),
            ("TEXTCOLOR", (1,0), (1,-1), MID_GREY),
            ("ROWBACKGROUNDS", (0,0), (-1,-1), [WHITE, LIGHT_GREY]),
            ("GRID", (0,0), (-1,-1), 0.3, colors.HexColor("#DDDDDD")),
            ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
            ("TOPPADDING", (0,0), (-1,-1), 6),
            ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ]))
        s.append(t2)
        return s
    return build_pdf("02-triple-obligation-poster.pdf",
                     "The Triple Obligation",
                     "NIS2 + KRITIS-Dachgesetz + TISAX — one segmentation answer", story)


# ═══════════════════════════════════════════════════════════════════════════════
# 3. TISAX 6.0 SEGMENTATION BRIEF
# ═══════════════════════════════════════════════════════════════════════════════
def pdf_03():
    def story():
        s = []
        s += [h1("TISAX 6.0 and Network Segmentation — What Tier 1 Suppliers Need to Show"), hr(), sp()]
        s += [body("TISAX (Trusted Information Security Assessment Exchange) is the automotive industry's "
                   "standard for supplier information security. Version 6.0 (published May 2024) significantly "
                   "raised the bar for network architecture requirements — specifically for suppliers handling "
                   "prototype data or production technology (Assessment Levels 2 and 3)."), sp()]
        s += [h2("What TISAX 6.0 Requires for Network Segmentation")]
        reqs = [
            ("IS-07", "Network segmentation", "Production networks must be separated from corporate IT. VLANs alone are insufficient without documented policy enforcement."),
            ("IS-08", "Remote access control", "Remote maintenance access must traverse a documented, segmented boundary. All sessions logged."),
            ("IS-11", "Supplier/partner access", "Third-party access to systems (ERP, CAD, test environments) must be bounded and auditable."),
            ("IS-19", "IT/OT boundary", "For manufacturers with production systems: documented segmentation between office IT and shop floor OT."),
            ("IS-22", "Asset inventory", "All network-connected assets inventoried with security classification. Dynamic discovery preferred."),
        ]
        tdata = [["Control", "Topic", "What TISAX auditors check"]]
        for ctrl, topic, what in reqs:
            tdata.append([ctrl, topic, what])
        t = Table(tdata, colWidths=[20*mm, 45*mm, 100*mm])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), AXIANS_BLUE),
            ("TEXTCOLOR",  (0,0), (-1,0), WHITE),
            ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
            ("FONTSIZE",   (0,0), (-1,-1), 8),
            ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT_GREY]),
            ("GRID", (0,0), (-1,-1), 0.4, colors.HexColor("#DDDDDD")),
            ("VALIGN", (0,0), (-1,-1), "TOP"),
            ("TOPPADDING", (0,0), (-1,-1), 5),
            ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ]))
        s += [t, sp(10)]
        s += [h2("The Witte Automotive Scenario")]
        s += [body("A Tier 1 automotive supplier with mechatronic locking systems for VW, BMW, and Mercedes "
                   "faces simultaneous TISAX audits from multiple OEMs. Each OEM's audit questionnaire (since "
                   "Q4 2024) includes a mandatory section on: <i>IS your production network documented and "
                   "separated from corporate IT?</i>")]
        s += [bullet("VW: 'Provide evidence of network segmentation between corporate and production environments'")]
        s += [bullet("BMW: 'Document all production-adjacent system connections and access controls'")]
        s += [bullet("Mercedes: 'Show network architecture with segmentation policy in effect'")]
        s += [sp(8)]
        s += [h2("How Guardicore Generates TISAX Evidence")]
        steps = [
            ("Week 1–2", "Discovery", "Guardicore maps every workload, connection, and flow in the production network. No enforcement, no disruption."),
            ("Week 3", "Visualization", "Complete network map with process-level labels. Your team sees the network as it actually is."),
            ("Week 4–5", "Policy generation", "AI-assisted policy draft: what should be allowed, what blocked. Your team reviews and approves."),
            ("Week 6+", "Enforcement", "Policy enforced. Traffic logs begin. Audit-ready documentation generated."),
            ("Ongoing", "Evidence export", "TISAX evidence package exportable: network map PDF + policy document + traffic log summary."),
        ]
        tdata2 = [["Phase", "Step", "TISAX output"]]
        for phase, step, output in steps:
            tdata2.append([phase, step, output])
        t2 = Table(tdata2, colWidths=[22*mm, 35*mm, 108*mm])
        t2.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), AXIANS_MAG),
            ("TEXTCOLOR",  (0,0), (-1,0), WHITE),
            ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
            ("FONTSIZE",   (0,0), (-1,-1), 8),
            ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT_GREY]),
            ("GRID", (0,0), (-1,-1), 0.4, colors.HexColor("#DDDDDD")),
            ("VALIGN", (0,0), (-1,-1), "TOP"),
            ("TOPPADDING", (0,0), (-1,-1), 5),
            ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ]))
        s += [t2]
        return s
    return build_pdf("03-tisax-segmentation-brief.pdf",
                     "TISAX 6.0 & Network Segmentation",
                     "What automotive Tier 1 suppliers must document — 2026", story)


# ═══════════════════════════════════════════════════════════════════════════════
# 4. OT AGENTLESS BRIEF (NVIDIA BLUEFIELD)
# ═══════════════════════════════════════════════════════════════════════════════
def pdf_04():
    def story():
        s = []
        s += [h1("Segmenting OT Assets That Cannot Run Agents"), hr(), sp()]
        s += [body("The most common objection to network microsegmentation in manufacturing: "
                   "<i>'Our PLCs, CNC machines, and industrial robots run proprietary firmware. "
                   "We cannot install agents. We cannot disrupt production.'</i>"), sp()]
        s += [body("Akamai Guardicore Segmentation, now with NVIDIA BlueField DPU integration "
                   "(GA Q2 2026), eliminates this objection entirely."), sp(10)]
        s += [h2("The Problem: Un-Agentable OT Assets in Every Production Floor")]
        unagentable = [
            "Siemens SIMATIC PLCs and S7 controllers",
            "KUKA industrial robots and their controllers",
            "Fanuc / Mitsubishi CNC machine controllers",
            "HMI panels (Windows CE / embedded Linux, vendor-locked)",
            "Legacy SCADA systems on Windows XP / 2003",
            "Embedded sensors and IoT gateways",
            "Automated Guided Vehicles (AGVs)",
        ]
        for item in unagentable:
            s.append(bullet(item))
        s += [sp(10)]
        s += [h2("The Akamai + NVIDIA BlueField Solution (GA Q2 2026)")]
        s += [body("The NVIDIA BlueField DPU (Data Processing Unit) is a SmartNIC that handles "
                   "network policy enforcement at the hardware layer — below the operating system, "
                   "without any software on the end device.")]
        s += [sp(6)]
        how = [
            ["BlueField DPU installed on server adjacent to OT network switch", "Hardware layer — no OT device touch"],
            ["Guardicore agent on the BlueField DPU (not on OT devices)", "All enforcement in the SmartNIC"],
            ["Guardicore discovers all OT flows via passive network observation", "Complete visibility of all machines"],
            ["Segmentation policy applied without touching any production device", "Zero downtime; zero vendor approval needed"],
            ["All logs and flow data reported to central Guardicore console", "Unified IT + OT visibility dashboard"],
        ]
        tdata = [["How it works", "Benefit"]]
        for step, benefit in how:
            tdata.append([step, benefit])
        t = Table(tdata, colWidths=[110*mm, 55*mm])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), AXIANS_BLUE),
            ("TEXTCOLOR",  (0,0), (-1,0), WHITE),
            ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
            ("FONTSIZE",   (0,0), (-1,-1), 8),
            ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT_GREY]),
            ("GRID", (0,0), (-1,-1), 0.4, colors.HexColor("#DDDDDD")),
            ("VALIGN", (0,0), (-1,-1), "TOP"),
            ("TOPPADDING", (0,0), (-1,-1), 5),
            ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ]))
        s += [t, sp(10)]
        s += [h2("Why This Matters for NIS2 and TISAX")]
        s += [body("NIS2 Article 21 and TISAX 6.0 IS-19 both require documented segmentation "
                   "of IT/OT boundaries — without exception for legacy equipment. The BlueField "
                   "solution enables manufacturers to satisfy these requirements on 100% of their "
                   "production floor, including assets that have been exempt from previous "
                   "segmentation projects due to agent constraints.")]
        s += [sp(6)]
        s += [body("<b>Contact Axians IT Security Services</b> for a BlueField-enabled OT "
                   "segmentation assessment: info@axians.de")]
        return s
    return build_pdf("04-ot-agentless-brief.pdf",
                     "OT Segmentation Without Agents",
                     "Akamai Guardicore + NVIDIA BlueField DPU — GA Q2 2026", story)


# ═══════════════════════════════════════════════════════════════════════════════
# 5. MITTELSTAND ROI BUSINESS CASE
# ═══════════════════════════════════════════════════════════════════════════════
def pdf_05():
    def story():
        s = []
        s += [h1("The Business Case for Microsegmentation — German Mittelstand Edition"), hr(), sp()]
        s += [body("This brief summarises the Forrester Total Economic Impact (TEI) study commissioned "
                   "by Akamai for Guardicore Segmentation, localized for a German Mittelstand "
                   "manufacturer profile."), sp()]
        s += [h2("Composite Profile (Forrester Reference Manufacturer)")]
        profile = [
            ["Revenue", "Approximately €1 billion"],
            ["Employees", "~5,000 worldwide"],
            ["Industry", "Manufacturing — discrete production"],
            ["IT environment", "Hybrid: on-premises data center + cloud + OT production network"],
            ["Pre-Guardicore security", "Traditional firewall-based perimeter; no microsegmentation"],
        ]
        t = Table(profile, colWidths=[55*mm, 110*mm])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (0,-1), LIGHT_GREY),
            ("FONTNAME", (0,0), (0,-1), "Helvetica-Bold"),
            ("FONTSIZE", (0,0), (-1,-1), 9),
            ("GRID", (0,0), (-1,-1), 0.3, colors.HexColor("#DDDDDD")),
            ("TOPPADDING", (0,0), (-1,-1), 5),
            ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ]))
        s += [t, sp(10)]
        s += [h2("3-Year Financial Results (Forrester TEI)")]
        results = [
            ["Total benefit (3 years)", "€9.6 million", "Net present value across 4 benefit categories"],
            ["Total cost (3 years)", "€3.8 million", "Licensing + implementation + operations"],
            ["Net present value", "€5.8 million", "After costs; positive from month 6"],
            ["ROI", "152%", "Industry benchmark for security tools is 30–80%"],
            ["Payback period", "6 months", "From go-live to positive return"],
        ]
        tdata = [["Metric", "Value", "Context"]]
        for m, v, c in results:
            tdata.append([m, v, c])
        t2 = Table(tdata, colWidths=[65*mm, 35*mm, 65*mm])
        t2.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), AXIANS_BLUE),
            ("TEXTCOLOR",  (0,0), (-1,0), WHITE),
            ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
            ("FONTNAME",   (1,1), (1,-1), "Helvetica-Bold"),
            ("TEXTCOLOR",  (1,1), (1,-1), AXIANS_BLUE),
            ("FONTSIZE",   (0,0), (-1,-1), 9),
            ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT_GREY]),
            ("GRID", (0,0), (-1,-1), 0.4, colors.HexColor("#DDDDDD")),
            ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
            ("TOPPADDING", (0,0), (-1,-1), 6),
            ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ]))
        s += [t2, sp(10)]
        s += [h2("Benefit Breakdown — The Four Value Drivers")]
        drivers = [
            ("Ransomware attack prevention", "€4.1M", "Based on avoided recovery cost of €1.3M per incident prevented; probability-weighted over 3 years"),
            ("Operational cost reduction", "€2.8M", "Reduced manual network-documentation labour; faster security audits; automated policy management"),
            ("Data breach risk reduction", "€1.5M", "Lateral movement containment limits blast radius; insurance premium reduction modeled"),
            ("Compliance acceleration", "€1.2M", "NIS2 / TISAX / KRITIS audit cost reduction; documentation automation"),
        ]
        tdata3 = [["Value driver", "3-year benefit", "How it is calculated"]]
        for d, v, c in drivers:
            tdata3.append([d, v, c])
        t3 = Table(tdata3, colWidths=[55*mm, 30*mm, 80*mm])
        t3.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), AXIANS_MAG),
            ("TEXTCOLOR",  (0,0), (-1,0), WHITE),
            ("FONTNAME",   (0,0), (-1,0), "Helvetica-Bold"),
            ("FONTNAME",   (1,1), (1,-1), "Helvetica-Bold"),
            ("TEXTCOLOR",  (1,1), (1,-1), AXIANS_MAG),
            ("FONTSIZE",   (0,0), (-1,-1), 8),
            ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT_GREY]),
            ("GRID", (0,0), (-1,-1), 0.4, colors.HexColor("#DDDDDD")),
            ("VALIGN", (0,0), (-1,-1), "TOP"),
            ("TOPPADDING", (0,0), (-1,-1), 5),
            ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ]))
        s += [t3, sp(8)]
        s += [body("<i>Source: Forrester Total Economic Impact of Akamai Guardicore Segmentation. "
                   "Actual results vary by organisation. German regulatory multipliers applied by Axians. "
                   "Full study available on request.</i>")]
        return s
    return build_pdf("05-mittelstand-roi-business-case.pdf",
                     "Business Case: Microsegmentation",
                     "Forrester TEI for German Mittelstand manufacturers — 152% ROI", story)


# ═══════════════════════════════════════════════════════════════════════════════
# 6. AXIANS × AKAMAI JOINT CAPABILITIES
# ═══════════════════════════════════════════════════════════════════════════════
def pdf_06():
    def story():
        s = []
        s += [h1("Axians IT Security × Akamai Guardicore — Joint Capabilities"), hr(), sp()]
        s += [body("For German Mittelstand manufacturers evaluating network microsegmentation, "
                   "the Axians–Akamai partnership provides the only offer combining "
                   "world-class technology, local German service delivery, and manufacturing sector expertise."), sp(10)]
        s += [h2("Axians IT Security Services — Credentials")]
        creds = [
            ("Market recognition", "ISG Benchmark Leader 2025 in 4 cybersecurity categories"),
            ("Geographic footprint", "65 offices across Germany; SOCs in Hamburg and Ulm"),
            ("Team", ">400 cybersecurity specialists in Germany; language: German"),
            ("Certifications", "ISO 27001 and ISO 9001 for both SOCs; BSI-recognized processes"),
            ("Partner ecosystem", "Part of VINCI Energies — global industrial group; Actemium OT delivery"),
            ("Manufacturing focus", "References in mechanical engineering, automotive supply, electronics manufacturing"),
        ]
        for label, val in creds:
            row_data = [[Paragraph(f"<b>{label}</b>", BODY_STYLE), Paragraph(val, BODY_STYLE)]]
            t = Table(row_data, colWidths=[55*mm, 110*mm])
            t.setStyle(TableStyle([
                ("BACKGROUND", (0,0), (0,0), LIGHT_GREY),
                ("GRID", (0,0), (-1,-1), 0.3, colors.HexColor("#DDDDDD")),
                ("TOPPADDING", (0,0), (-1,-1), 5),
                ("BOTTOMPADDING", (0,0), (-1,-1), 5),
                ("VALIGN", (0,0), (-1,-1), "TOP"),
            ]))
            s.append(t)
        s += [sp(10)]
        s += [h2("Akamai Guardicore Segmentation — Product Credentials")]
        akamai_creds = [
            ("Analyst recognition", "Forrester Wave — Microsegmentation Solutions; Gartner Peer Insights 4.8/5"),
            ("Global telemetry", "Largest commercial network; trillions of daily observations"),
            ("OT capability", "Only enterprise segmentation with agentless OT via NVIDIA BlueField DPU (GA Q2 2026)"),
            ("Threat detection", "Built-in breach detection, deception, and AI anomaly detection"),
            ("ROI", "Forrester TEI: 152% ROI, 6-month payback for composite €1B manufacturer"),
            ("Reference win", "Victorinox: chose Guardicore over Illumio following comparative evaluation"),
        ]
        for label, val in akamai_creds:
            row_data = [[Paragraph(f"<b>{label}</b>", BODY_STYLE), Paragraph(val, BODY_STYLE)]]
            t = Table(row_data, colWidths=[55*mm, 110*mm])
            t.setStyle(TableStyle([
                ("BACKGROUND", (0,0), (0,0), LIGHT_GREY),
                ("GRID", (0,0), (-1,-1), 0.3, colors.HexColor("#DDDDDD")),
                ("TOPPADDING", (0,0), (-1,-1), 5),
                ("BOTTOMPADDING", (0,0), (-1,-1), 5),
                ("VALIGN", (0,0), (-1,-1), "TOP"),
            ]))
            s.append(t)
        s += [sp(10)]
        s += [h2("The Joint Engagement Model")]
        s += [body("Axians manages the customer relationship and service delivery. Akamai provides "
                   "the technology platform, global threat intelligence, and product roadmap. "
                   "Together, we offer:")]
        s += [bullet("NIS2 readiness assessment (Axians-led, Guardicore-powered) — scopes the segmentation gap")]
        s += [bullet("30-day proof of value (discover only; no enforcement; full OT visibility)")]
        s += [bullet("Architecture workshop — production network segmentation design with your IT/OT team")]
        s += [bullet("Full deployment and managed microsegmentation service via Axians SOC Hamburg or Ulm")]
        s += [bullet("Ongoing compliance evidence generation for NIS2, TISAX, KRITIS auditors")]
        return s
    return build_pdf("06-axians-akamai-capabilities.pdf",
                     "Axians IT Security × Akamai",
                     "Joint capabilities brief — German Mittelstand manufacturing", story)


# ═══════════════════════════════════════════════════════════════════════════════
# 7. COMPETITIVE BATTLECARD — GUARDICORE VS ILLUMIO
# ═══════════════════════════════════════════════════════════════════════════════
def pdf_07():
    def story():
        s = []
        s += [h1("Guardicore vs. Illumio — Competitive Battlecard"), hr(), sp()]
        s += [body("<i>For Axians IT Security AEs — internal use. Respectful, data-based positioning.</i>"), sp(8)]
        s += [h2("Market Context")]
        s += [body("Both Akamai Guardicore and Illumio are credible, market-leading microsegmentation platforms "
                   "rated 4.8/5 on Gartner Peer Insights. Illumio is the 'original specialist'; Guardicore was "
                   "acquired by Akamai in 2021 and benefits from Akamai's security network. "
                   "For <b>German manufacturing OT environments</b>, Guardicore has clear technical superiority."), sp(8)]
        s += [h2("The Five Key Dimensions")]
        dims = [
            ("OT / Agentless capability",
             "GUARDICORE WINS",
             "NVIDIA BlueField DPU (GA Q2 2026) enables agentless policy enforcement on PLCs, robots, HMIs. No software on OT devices required.",
             "VEN agents required on each workload. Agentless options exist but are secondary. Acknowledged weakness: 'improve agent performance in OT environments' (PeerSpot).",
             AXIANS_BLUE),
            ("Built-in threat detection",
             "GUARDICORE WINS",
             "Breach detection, network deception (Akamai Hunt), AI anomaly detection on east-west traffic — all built in.",
             "Pure segmentation platform. No native threat detection. Customer must integrate separately with SIEM/XDR.",
             AXIANS_BLUE),
            ("Network intelligence",
             "GUARDICORE WINS",
             "Akamai operates the world's largest commercial network. Trillions of daily observations feed threat intelligence.",
             "Standalone company. Strong product but no network telemetry advantage.",
             AXIANS_BLUE),
            ("Policy granularity",
             "GUARDICORE WINS (complex envs)",
             "Flow + process + user-level visibility. AI-assisted policy creation with templates.",
             "Workload-level L3/L4 policy. Human-readable labels make simple environments easy.",
             AXIANS_BLUE),
            ("Commercial / total cost",
             "ILLUMIO ADVANTAGE",
             "List price higher than Illumio. Competitive when OT coverage and integrated detection are factored in.",
             "More cost-effective for simpler, pure-IT, all-agent-capable environments.",
             AXIANS_MAG),
        ]
        for dim, winner, guard_text, illumio_text, col in dims:
            s += [Paragraph(f"<b>{dim}</b>  —  <font color='#0068B6'>{winner}</font>", BODY_STYLE)]
            row = [[
                Paragraph(f"<b>Guardicore</b>\n{guard_text}", S("Normal", fontSize=8, textColor=DARK_GREY, leading=12)),
                Paragraph(f"<b>Illumio</b>\n{illumio_text}", S("Normal", fontSize=8, textColor=MID_GREY, leading=12)),
            ]]
            t = Table(row, colWidths=[82*mm, 83*mm])
            t.setStyle(TableStyle([
                ("BACKGROUND", (0,0), (0,0), colors.HexColor("#EBF4FB")),
                ("BACKGROUND", (1,0), (1,0), LIGHT_GREY),
                ("GRID", (0,0), (-1,-1), 0.3, colors.HexColor("#DDDDDD")),
                ("TOPPADDING", (0,0), (-1,-1), 6),
                ("BOTTOMPADDING", (0,0), (-1,-1), 6),
                ("VALIGN", (0,0), (-1,-1), "TOP"),
            ]))
            s += [t, sp(6)]
        s += [sp(4), hr(AXIANS_MAG)]
        s += [h2("The Three Lines — Use These in Every Competitive Call")]
        s += [body("<b>1.</b> 'If you have PLCs or industrial robots that cannot run software agents, "
                   "Guardicore is the only enterprise-grade option — with NVIDIA BlueField now GA.'")]
        s += [body("<b>2.</b> 'Forrester TEI: Guardicore 152% ROI vs. Illumio 111%. We are both better than "
                   "doing nothing — Guardicore delivers more for manufacturing environments.'")]
        s += [body("<b>3.</b> 'Stefan Epp at Victorinox ran both platforms in a real evaluation and chose "
                   "Guardicore. Happy to arrange a reference call.'")]
        return s
    return build_pdf("07-competitive-battlecard.pdf",
                     "Guardicore vs. Illumio",
                     "Competitive battlecard for Axians IT Security AEs — confidential", story)


# ═══════════════════════════════════════════════════════════════════════════════
# 8–10. ACCOUNT EXECUTIVE BRIEFS (Hörmann, Reinhausen, Witte)
# ═══════════════════════════════════════════════════════════════════════════════

def pdf_account_brief(filename, title, subtitle, company, hq, revenue, employees,
                      axians_status, contact_name, contact_title,
                      pain_points, narrative, ask):
    def story():
        s = []
        # Company snapshot table
        snap = [
            ["Company", company],
            ["HQ", hq],
            ["Revenue", revenue],
            ["Employees", employees],
            ["Axians relationship", axians_status],
        ]
        t = Table(snap, colWidths=[45*mm, 120*mm])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (0,-1), LIGHT_GREY),
            ("FONTNAME", (0,0), (0,-1), "Helvetica-Bold"),
            ("FONTSIZE", (0,0), (-1,-1), 9),
            ("GRID", (0,0), (-1,-1), 0.3, colors.HexColor("#DDDDDD")),
            ("TOPPADDING", (0,0), (-1,-1), 5),
            ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ]))
        s += [t, sp(10)]
        s += [h2("Why This Account. Why Now.")]
        for pp in pain_points:
            s.append(bullet(pp))
        s += [sp(10)]
        s += [h2("The Narrative")]
        s += [body(narrative), sp(10)]
        s += [h2("Primary Contact")]
        contact_data = [
            ["Name", contact_name],
            ["Title", contact_title],
        ]
        tc = Table(contact_data, colWidths=[35*mm, 130*mm])
        tc.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (0,-1), LIGHT_GREY),
            ("FONTNAME", (0,0), (0,-1), "Helvetica-Bold"),
            ("FONTSIZE", (0,0), (-1,-1), 9),
            ("GRID", (0,0), (-1,-1), 0.3, colors.HexColor("#DDDDDD")),
            ("TOPPADDING", (0,0), (-1,-1), 4),
            ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ]))
        s += [tc, sp(10)]
        s += [h2("The Ask")]
        s += [body(ask)]
        s += [sp(10), hr(AXIANS_MAG)]
        s += [body("Prepared by Axians IT Security Services in partnership with Akamai. "
                   "All intelligence from public sources. For internal use only.")]
        return s
    return build_pdf(filename, title, subtitle, story)


def pdf_08():
    return pdf_account_brief(
        "08-hoermann-executive-brief.pdf",
        "Account Brief: Hörmann KG",
        "Existing Axians customer — cross-portfolio opportunity",
        "Hörmann KG (Steinhagen, NRW)",
        "Steinhagen, North Rhine-Westphalia (near Bielefeld)",
        ">€1 billion (privately held, family-owned, 4th generation)",
        ">6,000 worldwide; 40+ specialized factories",
        "Active since 2014 — Axians NEO Solutions & Technology (SAP service management, C/4HANA, mobile apps). "
        "First IT Security engagement: not yet initiated.",
        "Rian Redinger",
        "Chief Information Security Officer, Hörmann Deutschland (Steinhagen)",
        [
            "NIS2 own obligation + KRITIS-Dachgesetz (doors in fire stations, utilities) + TISAX (automotive OEM plants) — triple obligation",
            "2020 BiSecur Gateway critical IoT vulnerability disclosure — SEC Consult; production halted, portal disabled. Institutional memory of cyber risk.",
            "KUKA robotics in tech stack + 40+ factories = flat-but-now-connected OT network",
            "SAP S/4HANA migration underway = highest-risk window for lateral movement",
            "Axians already trusted at group level (11+ years) — cross-portfolio introduction is the fastest possible path",
        ],
        "Axians has been helping Hörmann's service operations run smoothly since 2014. "
        "The SAP, mobile suite, and cloud projects give us trust that no vendor can buy. "
        "Now, as NIS2 activates and their CISO has a mandate to document network segmentation, "
        "an introduction from Alexandra Kempe (Hörmann VKG) to Rian Redinger (CISO) is the "
        "fastest-closing deal in the DACH Guardicore pipeline.",
        "Identify the Axians NEO account manager who owns the Hörmann VKG relationship. "
        "Arrange a 15-minute internal Axians cross-portfolio brief with Alain de Pauw's IT Security team. "
        "Request a joint introduction call — Axians NEO + Axians IT Security — with Alexandra Kempe as the bridge. "
        "Goal: a 60-minute NIS2 segmentation scoping session with Rian Redinger within 6 weeks."
    )


def pdf_09():
    return pdf_account_brief(
        "09-reinhausen-executive-brief.pdf",
        "Account Brief: Maschinenfabrik Reinhausen",
        "First Industrie 4.0 Award winner — NIS2 essential entity",
        "Maschinenfabrik Reinhausen GmbH (Regensburg, Bavaria)",
        "Regensburg, Bavaria",
        "€1.2 billion (Scheubeck Holding, 6th generation family-owned)",
        "~5,400 worldwide; 60 locations in 28 countries",
        "No known Axians relationship — cold account",
        "Dr. Hubert Feyrer",
        "Cyber Security Expert, Maschinenfabrik Reinhausen GmbH",
        [
            "Won the first German Industrie 4.0 Award — connected factory is real and documented",
            "Products regulate 50% of global electricity — NIS2 essential entity + KRITIS supply chain pressure from utility customers",
            "ISO 27001 ISMS under construction, scoped to ETOS product only — group-wide segmentation gap exists",
            "Three-digit million Euro investment offensive: doubling Regensburg Haslbach site — greenfield segmentation opportunity",
            "ProductCERT publishes vulnerability advisories recommending customers use network segmentation — does MR's own production network match that standard?",
        ],
        "Reinhausen's MR-CERT publishes advisories that explicitly tell utility operators: "
        "'Use mechanisms for vertical and horizontal network segmentation at all transition points.' "
        "The outreach narrative: <i>Your customers' auditors are going to ask whether their OLTC supplier holds their own production network to the same standard you recommend to them.</i> "
        "With the Haslbach expansion underway, the greenfield segmentation window is now.",
        "Cold LinkedIn connection (Dr. Hubert Feyrer) with a NIS2 + BDEW Whitepaper angle. "
        "Reference their own published advisory language. "
        "Ask: 'Would a 30-day production network discovery, with your team retaining full control, "
        "be useful as an input to the ISO 27001 ISMS build you are currently undertaking for ETOS?'"
    )


def pdf_10():
    return pdf_account_brief(
        "10-witte-automotive-executive-brief.pdf",
        "Account Brief: Witte Automotive",
        "Automotive Tier 1 — TISAX × NIS2 double pressure",
        "WITTE Automotive GmbH (Velbert, NRW)",
        "Velbert, North Rhine-Westphalia",
        ">€1 billion (Vast Automotive Group; 4th-generation family-owned)",
        "~6,000 worldwide; 9 countries",
        "No known Axians relationship — cold account. NRW regional proximity is an advantage.",
        "Rainer Schulten",
        "Leiter IT Security, WITTE Automotive (LinkedIn verified — role created January 2024)",
        [
            "Leiter IT Security role created January 2024 — same month TISAX 6.0 was published and NIS2 preparation was peaking",
            "Tier 1 automotive supplier to VW, BMW, Mercedes, Stellantis — OEM auditors require documented production network segmentation",
            "Mechatronic locking systems = cyber-physical products; production floor = OT/IT convergent environment",
            "CTO Christian Kaczmarczyk left July 2025 — technology leadership in transition; 'assess everything' mode",
            "No known Illumio or other segmentation vendor — first-mover opportunity",
        ],
        "Rainer Schulten spent 25 years building Witte's IT infrastructure. He knows every gap. "
        "In January 2024, he accepted the security mandate — which means he's now accountable for "
        "the segmentation that TISAX 6.0 and NIS2 both require. "
        "The first call is about what VW's last supplier security questionnaire said about network segmentation — "
        "not about Guardicore.",
        "LinkedIn connection to Rainer Schulten via Axians IT Security NRW AE. "
        "Message angle: what OEM auditors are requiring in 2026 for production network segmentation documentation. "
        "Goal: a 30-minute discovery call on current TISAX compliance challenges. "
        "Follow-up ask: 30-day production network discovery at one Velbert plant."
    )


# ═══════════════════════════════════════════════════════════════════════════════
# 11. TRUMPF SHOWCASE BRIEF
# ═══════════════════════════════════════════════════════════════════════════════
def pdf_11():
    def story():
        s = []
        s += [h1("Showcase Account: Trumpf GmbH + Co. KG"), hr(), sp()]
        s += [body("<i>This brief demonstrates the ABSM methodology applied to a high-profile, recognizable "
                   "German manufacturer — above the standard ICP band but included for portfolio credibility.</i>"), sp(8)]
        snap = [
            ["Company", "TRUMPF GmbH + Co. KG, Ditzingen (near Stuttgart), Baden-Württemberg"],
            ["Revenue FY2024/25", "€4.3 billion (down 16% — belt-tightening year)"],
            ["Employees", "18,303 worldwide; 9,337 in Germany"],
            ["Market position", "World leader in machine tools + industrial lasers; sole EUV laser supplier to ASML"],
            ["ISO 27001", "Certified December 2023 — all core TRUMPF entities"],
            ["CIO", "Thomas Speck (since 2021); 190 IT staff; CIO of Year 'Transformation of Work Award' 2023"],
            ["Axians status", "No known relationship — cold account; BW geographic proximity"],
        ]
        t = Table(snap, colWidths=[45*mm, 120*mm])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (0,-1), LIGHT_GREY),
            ("FONTNAME", (0,0), (0,-1), "Helvetica-Bold"),
            ("FONTSIZE", (0,0), (-1,-1), 9),
            ("GRID", (0,0), (-1,-1), 0.3, colors.HexColor("#DDDDDD")),
            ("TOPPADDING", (0,0), (-1,-1), 5),
            ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ]))
        s += [t, sp(10)]
        s += [h2("Why Trumpf, Despite Being Above the ICP Band")]
        s += [body("Trumpf's production network complexity exceeds that of every other account in this sprint. "
                   "30 machines connected via OPC UA in the Ditzingen smart factory. SAP S/4HANA migration underway. "
                   "EUV production (sole supplier to ASML) is the most KRITIS-adjacent manufacturing "
                   "environment in Germany. ISO 27001 certification mandates segmentation controls "
                   "that the production network architecture must now satisfy."), sp(6)]
        s += [h2("The Three Pain Patterns")]
        s += [bullet("ISO 27001 Annex A 8.22 — documented network segmentation control — directly requires what Guardicore delivers")]
        s += [bullet("SAP S/4HANA migration in flight — highest lateral movement risk in the company's digital transformation")]
        s += [bullet("EUV supply chain criticality — ASML and semiconductor customers will audit Trumpf's production security")]
        s += [sp(8)]
        s += [h2("The Narrative")]
        s += [body("Thomas Speck won CIO of the Year for transforming Trumpf's IT systematically. "
                   "The transformation created a cloud-first, IIoT-connected, SAP-migrating infrastructure. "
                   "The next chapter is securing what the transformation connected — specifically the production floor, "
                   "where 30 OPC UA machines communicate freely in an architecture that predates modern "
                   "microsegmentation policy tools."), sp(8)]
        s += [h2("The Ask")]
        s += [body("Request through Axians BW regional team: a 60-minute executive briefing with Thomas Speck on "
                   "'NIS2 segmentation requirements for connected manufacturing — peer benchmark from "
                   "the BW Mittelstand.' "
                   "Frame as information sharing, not vendor pitch. Guardicore emerges in the second meeting.")]
        s += [sp(8), hr(AXIANS_MAG)]
        s += [body("Prepared by Axians IT Security Services in partnership with Akamai. "
                   "All intelligence from public sources. For internal use only.")]
        return s
    return build_pdf("11-trumpf-showcase-brief.pdf",
                     "Showcase Account: TRUMPF",
                     "Methodology demonstration — above ICP band, maximum depth", story)


# ═══════════════════════════════════════════════════════════════════════════════
# 12. PIP PROGRAM BRIEF (INTERNAL AXIANS)
# ═══════════════════════════════════════════════════════════════════════════════
def pdf_12():
    def story():
        s = []
        s += [h1("Partner Intelligence Program (PIP) — Axians IT Security Brief"), hr(), sp()]
        s += [body("The Partner Intelligence Program is a strategic initiative proposed by Akamai to "
                   "systematically route high-intent DACH accounts to Axians IT Security Services, "
                   "pre-loaded with account intelligence and ready-to-use sales kits. "
                   "This brief explains the program mechanics and Axians' role."), sp(10)]
        s += [h2("The Problem This Solves")]
        s += [body("Without the PIP, Axians IT Security finds accounts through: (a) cold outreach, "
                   "(b) industry events, (c) occasional internal referral from other Axians portfolio teams. "
                   "This produces a fragmented, effort-intensive pipeline with long sales cycles. "
                   "Warm-path accounts — like Hörmann, where Axians NEO has an 11-year relationship — "
                   "are never routed to IT Security because there is no systematic cross-portfolio mechanism."), sp(10)]
        s += [h2("How the PIP Works")]
        steps = [
            ("Layer 1", "Intent Routing",
             "Akamai uses 6sense intent signals + 1st-party telemetry to identify DACH manufacturers "
             "showing in-market signals for OT security, NIS2 compliance, and microsegmentation. "
             "Monthly curated 'Hot 20 DACH Accounts' list delivered to Axians via HubSpot."),
            ("Layer 2", "Account Intelligence",
             "For each account, a pre-built intel kit is delivered: company brief, pain map, "
             "relationship map, Axians connection analysis, and outreach sequence. "
             "Axians AE receives a ready-to-use dossier, not raw data."),
            ("Layer 3", "Content Arsenal",
             "Account-specific PDF briefings (like the 11 other files in this package) are "
             "attached to each HubSpot deal record. AE knows which asset to send, to which "
             "contact, at which stage of the buying journey."),
            ("Layer 4", "Cross-Portfolio Routing",
             "When the intent-routed account is already an Axians customer in another portfolio "
             "(SAP, network, cloud), a cross-portfolio referral mechanism routes the Guardicore "
             "opportunity to IT Security with the existing AE's warm introduction."),
        ]
        for layer, name, desc in steps:
            row = [[
                Paragraph(f"<b>{layer}</b>", S("Normal", fontSize=10, textColor=WHITE, fontName="Helvetica-Bold", alignment=TA_CENTER)),
                Paragraph(f"<b>{name}</b><br/>{desc}", S("Normal", fontSize=9, textColor=DARK_GREY, leading=13)),
            ]]
            t = Table(row, colWidths=[22*mm, 143*mm])
            bg = AXIANS_BLUE if layer in ("Layer 1","Layer 3") else AXIANS_MAG
            t.setStyle(TableStyle([
                ("BACKGROUND", (0,0), (0,0), bg),
                ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                ("TOPPADDING", (0,0), (-1,-1), 8),
                ("BOTTOMPADDING", (0,0), (-1,-1), 8),
                ("ROWBACKGROUNDS", (1,0), (1,0), [LIGHT_GREY]),
                ("GRID", (0,0), (-1,-1), 0.3, colors.HexColor("#DDDDDD")),
            ]))
            s += [t, sp(4)]
        s += [sp(8)]
        s += [h2("Metrics — What the PIP Targets in Year 1")]
        metrics = [
            ["20 accounts/month", "Monthly 'Hot 20' list delivered to Axians"],
            ["5 qualified opportunities", "Target from 20 accounts per month"],
            ["2 POC closures/quarter", "30-day proof-of-value engagements"],
            ["1 deal closure/quarter", "Full deployment win from POC pipeline"],
            ["€150K–€400K ARR/deal", "Typical German Mittelstand Guardicore deployment"],
        ]
        t = Table(metrics, colWidths=[60*mm, 105*mm])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (0,-1), LIGHT_GREY),
            ("FONTNAME", (0,0), (0,-1), "Helvetica-Bold"),
            ("FONTSIZE", (0,0), (-1,-1), 9),
            ("GRID", (0,0), (-1,-1), 0.3, colors.HexColor("#DDDDDD")),
            ("TOPPADDING", (0,0), (-1,-1), 5),
            ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ]))
        s += [t, sp(8)]
        s += [h2("Hörmann as the PIP Proof of Concept")]
        s += [body("The ABSM Sprint deliverables in this package constitute a working demonstration "
                   "of the PIP at full capability: 4 accounts researched, 16 intel files produced, "
                   "4 strategy documents, and 12 execution PDFs — all without CRM access or "
                   "internal Axians data. A live PIP with Akamai 6sense signals and Axians "
                   "HubSpot access would be more targeted, faster, and richer. "
                   "Hörmann is the proof-of-concept account: existing relationship + Guardicore gap = "
                   "the model deal the PIP was designed to close.")]
        return s
    return build_pdf("12-pip-program-brief.pdf",
                     "Partner Intelligence Program",
                     "How Akamai and Axians systematically route and close DACH Guardicore accounts", story)


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("Generating 12 Axians-branded PDFs...")
    pdf_01()   # NIS2 segmentation brief
    pdf_02()   # Triple obligation poster
    pdf_03()   # TISAX brief
    pdf_04()   # OT agentless
    pdf_05()   # Mittelstand ROI
    pdf_06()   # Axians × Akamai capabilities
    pdf_07()   # Competitive battlecard
    pdf_08()   # Hörmann executive brief
    pdf_09()   # Reinhausen executive brief
    pdf_10()   # Witte executive brief
    pdf_11()   # Trumpf showcase brief
    pdf_12()   # PIP program brief
    print(f"\nAll 12 PDFs written to {OUTPUT_DIR}")
    import os
    files = sorted(os.listdir(OUTPUT_DIR))
    for f in files:
        if f.endswith(".pdf"):
            size = os.path.getsize(os.path.join(OUTPUT_DIR, f))
            print(f"  {f} — {size:,} bytes")
