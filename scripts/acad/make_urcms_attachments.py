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
    ("SBC permit: variation and renewal", (2027, 3), (2027, 7), "bar2"),
    ("Building stratification, 36 sampling points", (2027, 3), (2027, 5), "bar"),
    ("Monitoring node fabrication and calibration", (2027, 3), (2027, 8), "bar"),
    ("Dashboard, cloud platform, display unit", (2027, 7), (2027, 9), "bar"),
    ("Continuous air-quality and microclimate record", (2027, 9), (2028, 12), "bar2"),
    ("Sampling rounds R1-R6 (quarterly)", (2027, 4), (2028, 7), "bar"),
    ("Incubation, enumeration, isolation (TROPI, rolling)", (2027, 4), (2028, 10), "bar"),
    ("DNA extraction, PCR, Sanger identification", (2027, 6), (2028, 10), "bar"),
    ("Statistical and community analysis", (2028, 4), (2029, 1), "bar"),
    ("Manuscript 1: facade mycobiota inventory", (2028, 4), (2028, 10), "bar2"),
    ("Manuscript 2: green design and colonisation risk", (2028, 10), (2029, 1), "bar2"),
    ("Maintenance guidance and reporting protocol", (2028, 9), (2029, 2), "bar2"),
    ("Final report and URCMS closure", (2029, 1), (2029, 2), "bar"),
]

# diamonds: (label, (year, month), row index to sit on)
MILES = [
    ("R1", (2027, 4), 5), ("R2", (2027, 7), 5), ("R3", (2027, 10), 5),
    ("R4", (2028, 1), 5), ("R5", (2028, 4), 5), ("R6", (2028, 7), 5),
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
                 "Sampling closes July 2028 and molecular work October 2028, leaving the final "
                 "four months for analysis, writing and closure. Fixed term, no extension.")
    c.drawString(lx, ny - 20,
                 "Preparatory steps before 1 March 2027 (SORAS variation, MoA addendum, quotations) "
                 "are outside the funded term per MoA Clause 5.2.")
    c.showPage(); c.save()


MILESTONES = [
    ("Preparatory", "before 1 Mar 2027", [
        "SORAS application for SBC Permit variation and renewal submitted",
        "MoA Clause 21 addendum executed: title, Commencement Date and term, Schedule A A5 team, Schedule B Part 1 budget",
        "SRDC-TROPI written confirmation of matched expenditure re-issued against revised dates",
        "Consumable supply split confirmed with SRDC-TROPI; supplier quotations refreshed",
        "No sampling, biological transfer or expenditure before the Commencement Date (MoA Clause 5.2)",
    ]),
    ("Phase 1", "Mar - May 2027", [
        "Four buildings stratified by facade material, age, design approach and exposure",
        "36 fixed sampling points established, georeferenced and photographed",
        "Facade material and shading inventory complete",
        "Monitoring hardware procured; node fabrication begun",
        "Sampling, culture and contamination-control protocols agreed with SRDC-TROPI and validated",
    ]),
    ("Phase 2", "Apr 2027 - Jul 2028", [
        "R1 Apr 2027, R2 Jul 2027, R3 Oct 2027, R4 Jan 2028, R5 Apr 2028, R6 Jul 2028",
        "Haze-triggered supplementary rounds as episodes arise",
        "Nodes calibrated against rented reference instrument and installed; dashboard and display live by Sep 2027",
        "Algal and cyanobacterial cover plus microclimate covariates recorded at every point, every round",
        "Field, transport and extraction blanks collected each round",
    ]),
    ("Phase 3", "Apr 2027 - Oct 2028", [
        "Rolling cold-chain transfer of inoculated plates to SRDC-TROPI, one round at a time",
        "Incubation, CFU enumeration, morphotyping, isolation and purification at SRDC-TROPI",
        "Interim community profile at twelve months (Apr 2028)",
        "DNA extraction and ITS PCR; Sanger identification of the curated 100-isolate set",
        "Blanks processed and reported alongside each batch; isolate collection curated",
    ]),
    ("Phase 4", "Aug 2028 - Feb 2029", [
        "Full seasonal and year-on-year statistical and community analysis",
        "First indexed manuscript submitted (Oct 2028)",
        "Exterior material selection and maintenance guidance issued",
        "Campus air-quality reporting protocol issued; sequences deposited with accessions",
        "Second indexed manuscript submitted (Jan 2029)",
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
    c.drawString(36, 44, "Fixed 24-month term, no extension. Sampling closes Jul 2028 and molecular "
                         "work Oct 2028 so that the final four months carry only")
    c.drawString(36, 35, "analysis, writing, dissemination and closure. No deliverable depends on "
                         "activity after Oct 2028 other than writing.")
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
        ["Morphotype, purify, select isolates", "Curated 100-isolate set spanning",
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
        ["Sanger sequencing of amplicons", "~100 reactions, funded VOT 29000"], fill=HexColor("#f4f0f7"))
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


if __name__ == "__main__":
    gantt(); milestones(); flow()
    for f in sorted(OUT.glob("*.pdf")):
        print(f"{f.name:22s} {f.stat().st_size/1024:7.1f} KB")
