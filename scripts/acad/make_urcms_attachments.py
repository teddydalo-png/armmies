#!/usr/bin/env python3
"""Generate the Gantt chart, milestone and flow chart PDFs that URCMS asks to be
uploaded (max 1MB each). Regenerate after any schedule change rather than editing
the PDFs by hand.

    python3 scripts/acad/make_urcms_attachments.py
"""
from pathlib import Path

from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas

OUT = Path(__file__).resolve().parents[2] / "docs" / "urcms-attachments"
OUT.mkdir(parents=True, exist_ok=True)

TITLE = ("Fungal and microbial colonisation of tropical educational building exteriors: "
         "molecular characterisation and campus air-quality context at UTS Sibu")
SUB = "Dr Armstrong Ighodalo Omoregie | BERI, School of Built Environment, UTS | UTS Matching Grant, Cycle 1/2027"

INK = HexColor("#1a1a1a")
MUTE = HexColor("#6b6b6b")
RULE = HexColor("#cfcfcf")
BAR = HexColor("#3f6f8f")
BAR2 = HexColor("#7aa6bf")
MARK = HexColor("#b4532a")
BAND = HexColor("#f2f4f6")

# 24 project months, Mar 2027 - Feb 2029
MONTHS = []
for y in (2027, 2028, 2029):
    for mi, mn in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                             "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], start=1):
        MONTHS.append((y, mi, mn))
MONTHS = [m for m in MONTHS if (m[0], m[1]) >= (2027, 3) and (m[0], m[1]) <= (2029, 2)]
assert len(MONTHS) == 24, len(MONTHS)
IDX = {(y, m): i for i, (y, m, _) in enumerate(MONTHS)}

# (label, start, end, style)  style: "bar" | "bar2"
TASKS = [
    ("SBC permit: SORAS application and issue", (2027, 3), (2027, 5), "bar2"),
    ("Building stratification, 36 sampling points", (2027, 3), (2027, 5), "bar"),
    ("Monitoring node fabrication and calibration", (2027, 3), (2027, 7), "bar"),
    ("Dashboard, cloud platform, display unit", (2027, 7), (2027, 9), "bar"),
    ("Continuous air-quality and microclimate record", (2027, 9), (2028, 12), "bar2"),
    ("Sampling rounds R1-R6 (quarterly)", (2027, 6), (2028, 9), "bar"),
    ("Incubation, enumeration, isolation (TROPI, rolling)", (2027, 6), (2028, 12), "bar"),
    ("DNA extraction, PCR, Sanger identification", (2027, 8), (2028, 12), "bar"),
    ("Statistical and community analysis", (2028, 6), (2029, 1), "bar"),
    ("Manuscript 1: facade mycobiota inventory", (2028, 6), (2028, 11), "bar2"),
    ("Manuscript 2: green design and colonisation risk", (2028, 11), (2029, 2), "bar2"),
    ("Maintenance guidance and reporting protocol", (2028, 10), (2029, 2), "bar2"),
    ("Final report and URCMS closure", (2029, 1), (2029, 2), "bar"),
]

# diamonds: (label, (year, month), row index to sit on)
MILES = [
    ("R1", (2027, 6), 5), ("R2", (2027, 9), 5), ("R3", (2027, 12), 5),
    ("R4", (2028, 3), 5), ("R5", (2028, 6), 5), ("R6", (2028, 9), 5),
]


def header(c, w, h, heading):
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(36, h - 34, heading)
    c.setFont("Helvetica", 7.2)
    c.setFillColor(MUTE)
    # wrap title
    words, line, y = TITLE.split(), "", h - 46
    for word in words:
        if c.stringWidth(line + " " + word, "Helvetica", 7.2) > w - 72:
            c.drawString(36, y, line.strip()); y -= 9; line = word
        else:
            line += " " + word
    c.drawString(36, y, line.strip()); y -= 9
    c.drawString(36, y, SUB)
    c.setStrokeColor(RULE); c.setLineWidth(0.6)
    c.line(36, y - 8, w - 36, y - 8)
    return y - 8


def gantt():
    w, h = landscape(A4)
    c = canvas.Canvas(str(OUT / "gantt-chart.pdf"), pagesize=(w, h))
    top = header(c, w, h, "GANTT CHART - 24 months, 1 March 2027 to 28 February 2029")

    lx, rx = 36, w - 36
    label_w = 252
    cx0 = lx + label_w
    colw = (rx - cx0) / 24.0
    y = top - 26

    # year + month headers
    c.setFont("Helvetica-Bold", 7)
    c.setFillColor(INK)
    for yr, span in (("2027", (0, 10)), ("2028", (10, 22)), ("2029", (22, 24))):
        a, b = span
        c.drawCentredString(cx0 + (a + b) / 2 * colw, y + 12, yr)
    c.setFont("Helvetica", 6.2)
    c.setFillColor(MUTE)
    for i, (_, _, mn) in enumerate(MONTHS):
        c.drawCentredString(cx0 + (i + 0.5) * colw, y + 3, mn)

    rowh = 19.5
    y -= 8
    for r, (label, s, e, style) in enumerate(TASKS):
        ry = y - r * rowh
        if r % 2 == 0:
            c.setFillColor(BAND)
            c.rect(lx, ry - rowh + 5, rx - lx, rowh, stroke=0, fill=1)
        c.setFillColor(INK)
        c.setFont("Helvetica", 7.1)
        c.drawString(lx + 3, ry - 7, label[:62])
        a, b = IDX[s], IDX[e]
        c.setFillColor(BAR if style == "bar" else BAR2)
        c.roundRect(cx0 + a * colw + 1.2, ry - 11.5, (b - a + 1) * colw - 2.4, 8.5,
                    2, stroke=0, fill=1)

    # month gridlines
    c.setStrokeColor(RULE); c.setLineWidth(0.35)
    bot = y - len(TASKS) * rowh + 5
    for i in range(25):
        c.line(cx0 + i * colw, y + 1, cx0 + i * colw, bot)
    c.setStrokeColor(HexColor("#9aa8b4")); c.setLineWidth(0.5)
    c.line(cx0, y + 1, cx0, bot)

    # sampling round diamonds
    for lab, when, row in MILES:
        mx = cx0 + (IDX[when] + 0.5) * colw
        my = y - row * rowh - 7.2
        c.setFillColor(MARK)
        c.saveState(); c.translate(mx, my); c.rotate(45)
        c.rect(-3.1, -3.1, 6.2, 6.2, stroke=0, fill=1); c.restoreState()
        c.setFont("Helvetica-Bold", 5.6); c.setFillColor(MARK)
        c.drawCentredString(mx, my + 6.2, lab)

    # legend / notes
    ny = bot - 16
    c.setFont("Helvetica-Bold", 6.8); c.setFillColor(INK)
    c.drawString(lx, ny, "Diamonds R1-R6: quarterly sampling rounds.")
    c.setFont("Helvetica", 6.8); c.setFillColor(MUTE)
    c.drawString(lx + 168, ny,
                 "R1-R4 = one complete annual seasonal round. R5 and R6 repeat the R1 and R2 "
                 "phases twelve months later.")
    c.drawString(lx, ny - 10,
                 "Sampling closes September 2028 and molecular work December 2028, leaving the "
                 "final months for analysis, writing and closure. Fixed term, no extension.")
    c.drawString(lx, ny - 20,
                 "The SBC permit is applied for on commencement; no sampling or transfer of biological "
                 "material occurs before it is issued.")
    c.showPage(); c.save()


MILESTONES = [
    ("Phase 1", "Mar - May 2027", [
        "SORAS application for the SBC permit submitted on commencement; permit issued",
        "Four buildings stratified by facade material, age, design approach and exposure",
        "36 fixed sampling points established, georeferenced and photographed",
        "Facade material and shading inventory, and baseline algal and cyanobacterial cover survey, complete",
        "Monitoring nodes fabricated and calibrated against the rented reference instrument",
        "Sampling, culture and contamination-control protocols agreed with SRDC-TROPI and validated",
    ]),
    ("Phase 2", "Jun 2027 - Sep 2028", [
        "R1 Jun 2027, R2 Sep 2027, R3 Dec 2027, R4 Mar 2028, R5 Jun 2028, R6 Sep 2028",
        "Haze-triggered supplementary rounds as episodes arise",
        "Nodes installed; cloud platform, public dashboard and display unit live by Sep 2027",
        "Algal and cyanobacterial cover plus microclimate covariates recorded at every point, every round",
        "Field, transport and extraction blanks collected each round",
    ]),
    ("Phase 3", "Jun 2027 - Dec 2028", [
        "Rolling cold-chain transfer of inoculated plates to SRDC-TROPI, one round at a time",
        "Incubation, CFU enumeration, morphotyping, isolation and purification at SRDC-TROPI",
        "Interim community profile at twelve months (Jun 2028)",
        "DNA extraction and ITS PCR; Sanger identification of the curated 60-isolate set",
        "Blanks processed and reported alongside each batch; isolate collection curated",
    ]),
    ("Phase 4", "Oct 2028 - Feb 2029", [
        "Full seasonal and year-on-year statistical and community analysis",
        "First indexed manuscript submitted (Nov 2028)",
        "Exterior material selection and maintenance guidance issued",
        "Campus air-quality reporting protocol issued; sequences deposited with accessions",
        "Second indexed manuscript submitted (Feb 2029)",
        "Final project report and grant closure via URCMS by 28 Feb 2029",
    ]),
]


def milestones():
    w, h = A4
    c = canvas.Canvas(str(OUT / "milestones.pdf"), pagesize=(w, h))
    top = header(c, w, h, "PROJECT MILESTONES - 24 months, 1 March 2027 to 28 February 2029")
    y = top - 22
    for phase, window, items in MILESTONES:
        need = 20 + 11.5 * len(items)
        if y - need < 60:
            c.showPage()
            top = header(c, w, h, "PROJECT MILESTONES (continued)")
            y = top - 22
        c.setFillColor(BAND)
        c.rect(36, y - 13, w - 72, 17, stroke=0, fill=1)
        c.setFillColor(INK); c.setFont("Helvetica-Bold", 8.4)
        c.drawString(41, y - 8, phase)
        c.setFont("Helvetica", 8.4); c.setFillColor(HexColor("#44576a"))
        c.drawRightString(w - 41, y - 8, window)
        y -= 24
        c.setFont("Helvetica", 7.6); c.setFillColor(INK)
        for it in items:
            c.setFillColor(BAR)
            c.circle(45, y + 2.4, 1.5, stroke=0, fill=1)
            c.setFillColor(INK)
            line = it
            while c.stringWidth(line, "Helvetica", 7.6) > w - 110:
                line = line[:-2]
            c.drawString(52, y, line if line == it else line + "...")
            y -= 11.5
        y -= 8
    c.setFont("Helvetica-Oblique", 7)
    c.setFillColor(MUTE)
    c.drawString(36, 44, "Fixed 24-month term, no extension. Sampling closes Sep 2028 and molecular "
                         "work Dec 2028 so that the closing months carry only")
    c.drawString(36, 35, "analysis, writing, dissemination and closure. The first sampling round follows "
                         "issue of the SBC permit.")
    c.showPage(); c.save()


def flow():
    w, h = A4
    c = canvas.Canvas(str(OUT / "flow-chart.pdf"), pagesize=(w, h))
    top = header(c, w, h, "RESEARCH FLOW CHART")

    def box(x, y, bw, bh, lines, fill=white, bold_first=True, fs=7.2):
        c.setFillColor(fill); c.setStrokeColor(HexColor("#8d9aa6")); c.setLineWidth(0.7)
        c.roundRect(x, y, bw, bh, 3, stroke=1, fill=1)
        ty = y + bh - 11
        for i, ln in enumerate(lines):
            c.setFillColor(INK)
            c.setFont("Helvetica-Bold" if (i == 0 and bold_first) else "Helvetica",
                       fs + (0.4 if i == 0 and bold_first else 0))
            c.drawCentredString(x + bw / 2, ty, ln)
            ty -= 9.4

    def arrow(x1, y1, x2, y2):
        c.setStrokeColor(HexColor("#5a6b7a")); c.setLineWidth(0.9)
        c.line(x1, y1, x2, y2)
        import math
        a = math.atan2(y2 - y1, x2 - x1)
        for s in (2.5, -2.5):
            c.line(x2, y2, x2 - 5 * math.cos(a) + s * math.sin(a),
                   y2 - 5 * math.sin(a) - s * math.cos(a))

    cx = w / 2
    colw, bh = 196, 40
    y = top - 46

    def lane(label, yy):
        c.setFillColor(MUTE); c.setFont("Helvetica-Bold", 6.6)
        c.drawString(36, yy, label.upper())
        c.setStrokeColor(RULE); c.setLineWidth(0.4)
        c.line(36, yy - 4, w - 36, yy - 4)

    lane("UTS Sibu - field", y + 24)
    box(cx - colw / 2, y - bh, colw, bh,
        ["Four buildings, 36 fixed points", "4 orientations x paired colonised/clean",
         "+ roof points; stratified by material,", "age, design approach, exposure"], fill=HexColor("#eef3f7"))
    y -= bh + 20
    arrow(cx, y + 20, cx, y + 4)
    box(cx - colw / 2, y - bh, colw, bh,
        ["Swab 10 x 10 cm template", "3 replicates per point, composited;",
         "settle plates; algal cover scored;", "microclimate covariates recorded"])
    y -= bh + 20

    # controls box to the left
    box(36, y - bh + 6, 150, bh,
        ["Controls each round", "Field blank, transport blank,", "extraction blank, PCR NTC,",
         "positive control, sterility plates"], fill=HexColor("#fdf3ee"), fs=6.6)
    arrow(186, y - bh / 2 + 6, cx - colw / 2 - 2, y - bh / 2 + 6)

    arrow(cx, y + 20, cx, y + 4)
    box(cx - colw / 2, y - bh, colw, bh,
        ["Inoculate SDA / PDA plates on site", "Media and swabs supplied by SRDC-TROPI",
         "Cold-chain transport, triple packaged", "6 quarterly rounds: R1-R6"])
    y -= bh + 38

    lane("SRDC-TROPI, Kota Samarahan", y + 22)
    y -= 4
    arrow(cx, y + 18, cx, y + 2)
    box(cx - colw / 2, y - bh, colw, bh,
        ["Incubate and enumerate", "CFU per unit area (surfaces),",
         "CFU per cubic metre (settle plates)", "216 composited samples"], fill=HexColor("#eef3f7"))
    y -= bh + 20
    arrow(cx, y + 20, cx, y + 4)
    box(cx - colw / 2, y - bh, colw, bh,
        ["Morphotype, purify, select isolates", "Curated 60-isolate set spanning",
         "morphotypes, buildings, materials,", "seasons; collection maintained"])
    y -= bh + 20
    arrow(cx, y + 20, cx, y + 4)
    box(cx - colw / 2, y - bh, colw, bh,
        ["DNA extraction and ITS PCR", "Fungal-specific primers targeting the",
         "internal transcribed spacer region"])
    y -= bh + 22

    lane("Commercial provider", y + 18)
    y -= 6
    arrow(cx, y + 14, cx, y - 2)
    box(cx - colw / 2, y - 30, colw, 30,
        ["Sanger sequencing of amplicons", "80 reactions, funded VOT 29000"], fill=HexColor("#f4f0f7"))
    y -= 30 + 22

    lane("Joint analysis and outputs", y + 18)
    y -= 4
    arrow(cx, y + 14, cx, y - 2)

    # air quality side feed
    box(36, y - 34, 150, 34,
        ["Air-quality context", "PM2.5/PM10, CO, NOx, O3, CO2,", "T and RH; dashboard and display"],
        fill=HexColor("#f1f6f1"), fs=6.6)
    arrow(186, y - 17, cx - colw / 2 - 2, y - 17)

    box(cx - colw / 2, y - 34, colw, 34,
        ["Taxonomic assignment and analysis", "GLMM on CFU; PERMANOVA on composition;",
         "blanks reported; decontamination applied"])
    y -= 34 + 20
    arrow(cx, y + 20, cx, y + 4)
    box(cx - colw / 2 - 30, y - 48, colw + 60, 48,
        ["Outputs", "Two indexed publications | isolate collection and deposited sequences",
         "Exterior material and maintenance guidance | air-quality reporting protocol",
         "Trained student researchers | open campus dataset"], fill=HexColor("#eef3f7"))

    c.showPage(); c.save()


ROUNDS = [
    ("R1", "June 2027", "Southwest monsoon", ""),
    ("R2", "September 2027", "Southwest monsoon, late phase", ""),
    ("R3", "December 2027", "Northeast monsoon", ""),
    ("R4", "March 2028", "Northeast monsoon, late phase", ""),
    ("R5", "June 2028", "Southwest monsoon", "twelve-month repeat of R1"),
    ("R6", "September 2028", "Southwest monsoon, late phase", "twelve-month repeat of R2"),
]


def schedule():
    w, h = A4
    c = canvas.Canvas(str(OUT / "sampling-schedule.pdf"), pagesize=(w, h))
    top = header(c, w, h, "SAMPLING ROUND SCHEDULE")
    y = top - 30
    c.setFont("Helvetica-Bold", 8); c.setFillColor(INK)
    for x, lab in ((40, "Round"), (95, "Month"), (190, "Seasonal phase"), (430, "Note")):
        c.drawString(x, y, lab)
    c.setStrokeColor(RULE); c.setLineWidth(0.6); c.line(36, y - 5, w - 36, y - 5)
    y -= 20
    for i, (r, m, phase, note) in enumerate(ROUNDS):
        if i % 2 == 0:
            c.setFillColor(BAND); c.rect(36, y - 6, w - 72, 18, stroke=0, fill=1)
        c.setFillColor(INK); c.setFont("Helvetica-Bold", 8); c.drawString(40, y, r)
        c.setFont("Helvetica", 8)
        c.drawString(95, y, m); c.drawString(190, y, phase)
        c.setFillColor(MARK); c.setFont("Helvetica-Oblique", 7.4)
        c.drawString(430, y, note)
        y -= 18
    y -= 14
    c.setFillColor(INK); c.setFont("Helvetica", 8)
    for ln in [
        "Rounds 1 to 4 constitute a complete annual seasonal round covering both monsoon phases. Rounds 5",
        "and 6 resample the Round 1 and Round 2 phases exactly twelve months later, giving paired",
        "year-on-year observations for two of those phases.",
        "",
        "Up to two additional rounds are triggered opportunistically during regional haze episodes.",
        "",
        "At each round, 36 fixed points are sampled: 4 buildings x 4 orientations x paired colonised and clean",
        "surfaces, giving 32 wall points, plus 4 roof points. Three replicate swabs per point are composited,",
        "giving 36 samples per round and 216 composited samples across the six rounds.",
        "",
        "The first round falls three months after commencement so that the SBC permit can be applied for",
        "and issued first. Sampling closes in September 2028 so that the remaining molecular work,",
        "analysis, both manuscripts and grant closure complete within the term ending 28 February 2029.",
    ]:
        c.drawString(40, y, ln); y -= 12
    c.showPage(); c.save()


BUDGET = [
    ("11000", "Salary and Wages",
     "<b>Y1 (RM 1,500):</b> Undergraduate research assistant allowance (RM 7.00/hour x 4 hours/day x approx. 18 days = RM 500.00/month x 3 active months) for sampling rounds R1 to R3 and monitoring node assembly. <b>Y2 (RM 1,500):</b> RA allowance (RM 500.00/month x 3 active months) for rounds R4 to R6, plate inoculation and cold-chain packing. Rate complies with Guideline Section 7(a); total within the RM 3,000 ceiling.",
     "1,500.00", "1,500.00", "3,000.00"),
    ("21000", "Travel and Transport",
     "<b>Y1 (RM 850):</b> Cold-chain transport of swabs, media and inoculated plates between UTS Sibu and SRDC-TROPI, Kota Samarahan (5 legs x RM 150.00 = RM 750.00); inbound delivery of sensor modules and field consumables (2 x RM 50.00 = RM 100.00). <b>Y2 (RM 2,150):</b> Cold-chain transport (4 legs x RM 150.00 = RM 600.00); delivery (RM 50.00); attendance at one national conference to present project findings (RM 1,500.00 covering return airfare RM 700.00, accommodation RM 250.00/night x 3 nights, ground transport RM 50.00). <i>(Note: Conference registration fee is claimed under VOT 29000. Local Sibu fieldwork travel excluded, as all four sampled buildings are on campus. Within RM 3,000 SET ceiling, Guideline Section 7(b).)</i>",
     "850.00", "2,150.00", "3,000.00"),
    ("24000", "Rental",
     "<b>Y1 (RM 1,200):</b> Rental of a reference-grade air quality analyser for co-location calibration of the monitoring nodes (RM 600.00/week x 2 weeks): one pre-deployment campaign and one post-installation verification. <b>Y2 (RM 0):</b> No further rental required. <i>(Note: Rental rather than purchase, as the instrument is required for two short campaigns only. Placed in VOT 24000 per Guideline Section 7(c).)</i>",
     "1,200.00", "0.00", "1,200.00"),
    ("26000", "Research Materials and Supplies",
     "<b>Y1 (RM 9,300):</b> Monitoring node components for four campus nodes plus spares (RM 8,040) comprising multi-parameter air-quality modules for CO2, PM2.5, PM10, temperature and humidity (RM 2,600); discrete temperature and humidity sensors (RM 200); metal oxide gas sensor sets (RM 1,120); microcontroller boards (RM 540); LoRa gateway and transmitter set (RM 900); IP65 enclosures and mounting (RM 880); power supply, solar panel, battery and cabling (RM 1,200); PCB fabrication and prototyping consumables (RM 600). Field sampling consumables (RM 1,260) comprising sterile sampling templates (RM 600), cold-chain coolers and gel packs (RM 360), and PPE for rounds R1 to R3 (RM 300). <b>Y2 (RM 2,500):</b> Additional cold-chain coolers (RM 360); PPE and field consumables for rounds R4 to R6 (RM 400); ethanol, sample bags, labels and markers (RM 540); culture consumable contingency (RM 1,200) for SDA and PDA media, sterile swabs and Petri dishes. <i>(Note: Node configuration is already validated in deployed service, removing design risk. Culture media and swabs are supplied by SRDC-TROPI as in-kind matched expenditure; the contingency covers control plates and repeat sampling only. Sulphur dioxide sensing excluded.)</i>",
     "9,300.00", "2,500.00", "11,800.00"),
    ("29000", "Professional Services",
     "<b>Y1 (RM 1,300):</b> Sanger sequencing of ITS amplicons, 32 reactions at RM 25.00 (RM 800.00) for isolates from rounds R1 to R3; SORAS application and Sarawak Biodiversity Council permit fees (RM 500.00). <b>Y2 (RM 1,700):</b> Sanger sequencing, 48 reactions at RM 25.00 (RM 1,200.00) for isolates from rounds R4 to R6; registration fee for one national conference (RM 500.00). <i>(Note: DNA extraction and PCR are performed by SRDC-TROPI as an in-kind matched contribution, so only the sequencing service is charged to this grant. Journal article processing charges excluded; non-APC journals targeted. Within RM 3,000 SET ceiling, Guideline Section 7(f).)</i>",
     "1,300.00", "1,700.00", "3,000.00"),
    ("35000", "Accessories and Small Appliances",
     "<b>Y1 (RM 3,000):</b> Outdoor-rated display panel for live campus air-quality readings at a high-traffic location (RM 2,200.00); weatherproof housing, mounting bracket and installation hardware (RM 800.00). <b>Y2 (RM 0):</b> No accessories required. <i>(Note: Cloud hosting and data plan excluded as utilities, provided instead as a UTS in-kind contribution. Assets remain UTS property. Total is 12% of grant, within the 40% ceiling, Guideline Section 7(g).)</i>",
     "3,000.00", "0.00", "3,000.00"),
]


def budget():
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.lib import colors as rc

    w, h = landscape(A4)
    doc = SimpleDocTemplate(str(OUT / "budget-table.pdf"), pagesize=(w, h),
                            leftMargin=12 * mm, rightMargin=12 * mm,
                            topMargin=12 * mm, bottomMargin=12 * mm,
                            title="Proposed Budget", author="Dr Armstrong Ighodalo Omoregie")
    body = ParagraphStyle("body", fontName="Helvetica", fontSize=6.2, leading=7.6, textColor=INK)
    head = ParagraphStyle("head", fontName="Helvetica-Bold", fontSize=6.8, leading=8.4, textColor=white)
    cat = ParagraphStyle("cat", fontName="Helvetica-Bold", fontSize=6.4, leading=8, textColor=INK)
    num = ParagraphStyle("num", fontName="Helvetica", fontSize=6.6, leading=8,
                         alignment=2, textColor=INK)
    title = ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=INK)
    sub = ParagraphStyle("sub", fontName="Helvetica", fontSize=7, leading=9, textColor=MUTE)

    rows = [[Paragraph(x, head) for x in
             ["VOT", "Category", "Justification and detailed breakdown (Year 1 and Year 2)",
              "Year 1 (RM)", "Year 2 (RM)", "Total (RM)"]]]
    for v, c, j, y1, y2, tot in BUDGET:
        rows.append([Paragraph(v, cat), Paragraph(c, cat), Paragraph(j, body),
                     Paragraph(y1, num), Paragraph(y2, num), Paragraph(tot, num)])
    rows.append([Paragraph("", cat), Paragraph("TOTAL", cat), Paragraph("", body),
                 Paragraph("<b>17,150.00</b>", num), Paragraph("<b>7,850.00</b>", num),
                 Paragraph("<b>25,000.00</b>", num)])

    colw = [14 * mm, 28 * mm, 157 * mm, 20 * mm, 20 * mm, 20 * mm]
    tbl = Table(rows, colWidths=colw, repeatRows=1)
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BAR),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.4, RULE),
        ("BACKGROUND", (0, -1), (-1, -1), BAND),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))

    story = [
        Paragraph("PROPOSED BUDGET", title),
        Paragraph("Fungal and microbial colonisation of tropical educational building exteriors: "
                  "molecular characterisation and campus air-quality context at UTS Sibu", sub),
        Paragraph("Dr Armstrong Ighodalo Omoregie | BERI, School of Built Environment, UTS | "
                  "UTS Matching Grant, Cycle 1/2027 | Year 1: Mar 2027 to Feb 2028, "
                  "Year 2: Mar 2028 to Feb 2029", sub),
        Spacer(1, 6), tbl, Spacer(1, 6),
        Paragraph("VOT 23000 and VOT 28000 are not used. Virement may be exercised only once during the "
                  "project and requires the approval of the Director, Centre for Research and Development. "
                  "Supplier unit costs are planning figures pending current quotations, except the Sanger "
                  "sequencing rate of RM25.00 per reaction, which is quoted.", sub),
    ]
    doc.build(story)


if __name__ == "__main__":
    gantt(); milestones(); flow(); schedule(); budget()
    for f in sorted(OUT.glob("*.pdf")):
        print(f"{f.name:22s} {f.stat().st_size/1024:7.1f} KB")
