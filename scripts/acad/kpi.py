#!/usr/bin/env python3
"""Score a UTS academic KPI ledger against a rubric, and show where marks are
actually available.

The point of this tool is not addition. It is the caps. Most sections convert raw
points to marks with a ceiling, so past that ceiling further output earns nothing
toward KPI. `marginal` prints the real mark value of one more unit of each
activity, which is the number that should drive how you spend a semester.

Offline, no dependencies beyond pyyaml.

  kpi.py score    --ledger profile/kpi-ledger.yml
  kpi.py marginal --ledger profile/kpi-ledger.yml
  kpi.py gaps     --ledger profile/kpi-ledger.yml
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("pyyaml required:  pip install pyyaml")

REPO = Path(__file__).resolve().parents[2]


def load(p: Path):
    if not p.exists():
        sys.exit(f"missing file: {p}\nCopy the .example file next to it and fill it in.")
    return yaml.safe_load(p.read_text())


def band_marks(bands, value, key="marks"):
    """Pick the marks for a value from banded thresholds. Bands may omit max."""
    if value is None:
        return None
    for b in bands:
        lo = b.get("min", float("-inf"))
        hi = b.get("max", float("inf"))
        if lo <= value <= hi:
            return b[key]
    return 0


def section_by_id(rubric, sid):
    for s in rubric["sections"]:
        if s["id"] == sid:
            return s
    raise KeyError(sid)


def raw_to_marks(section, raw, band):
    """Apply the section's conversion rule. Returns (marks, wasted_raw)."""
    cap = section["max_marks"][band]
    rule = section.get("raw_to_marks", "cap")
    if rule == "direct":
        return min(raw, cap), max(0.0, raw - cap)
    if rule == "cap":
        return min(raw, cap), max(0.0, raw - cap)
    if rule == "scale":
        factor = section["scale_factor"]
        raw_cap = section.get("raw_cap", cap / factor)
        effective = min(raw, raw_cap)
        return min(effective * factor, cap), max(0.0, raw - raw_cap)
    raise ValueError(f"unknown raw_to_marks: {rule}")


def score_teaching(section, ledger, band, column):
    """Teaching is itemised and banded rather than a point pool."""
    t = ledger.get("teaching", {}) or {}
    rows = []
    for item in section["items"]:
        avail = item["marks"].get(column, 0)
        iid = item["id"]
        got, note = None, ""

        if iid == "teaching_performance":
            key = "ucil_marks" if column == "E" else "marks"
            got = band_marks(item["bands"], t.get("set_score"), key)
            note = f"SET {t.get('set_score')}" if t.get("set_score") is not None else "SET score not recorded"
        elif iid == "teaching_hours":
            got = band_marks(item["bands"], t.get("credit_hours"))
            note = f"{t.get('credit_hours')} credit hrs" if t.get("credit_hours") is not None else "credit hours not recorded"
        elif iid == "supervision":
            main = t.get("fyp_main_supervisees")
            co = t.get("fyp_co_supervisees")
            m = band_marks(item["bands"], main) or 0
            c = band_marks(item.get("co_supervisor_bands", []), co) or 0
            got = m + c if (main is not None or co is not None) else None
            note = f"{main or 0} main, {co or 0} co"
        elif iid == "supervision_postgrad":
            main = t.get("pg_main_supervisees")
            co = t.get("pg_co_supervisees")
            m = band_marks(item["bands"], main) or 0
            c = band_marks(item.get("co_supervisor_bands", []), co) or 0
            got = m + c if (main is not None or co is not None) else None
            note = f"{main or 0} main, {co or 0} co"
        elif iid == "teaching_module":
            got = band_marks(item["bands"], t.get("course_files"))
            note = f"{t.get('course_files')} course files" if t.get("course_files") is not None else "course files not recorded"

        capped = min(got, avail) if got is not None else None
        rows.append({
            "id": iid, "name": item["name"], "available": avail,
            "earned": capped, "uncapped": got, "note": note,
        })
    return rows


def collect_pool(section, ledger):
    """Sum raw points for a point-pool section from itemised entries."""
    acts = section.get("activities", {})
    raw = 0.0
    detail = []
    for e in ledger.get("entries", []) or []:
        a = e.get("activity")
        if a not in acts:
            continue
        role = e.get("role", "lead")
        count = e.get("count", 1)
        per = acts[a].get(role if role in ("lead", "co") else "lead", 0)
        pts = per * count
        raw += pts
        detail.append({"activity": a, "name": acts[a]["name"], "role": role,
                       "count": count, "per": per, "points": pts,
                       "ref": e.get("ref", ""), "proof": e.get("proof", "")})
    declared = (ledger.get("declared_raw") or {}).get(section["id"])
    if declared is not None:
        if detail:
            raw += float(declared.get("raw", 0)) if isinstance(declared, dict) else float(declared)
        else:
            raw = float(declared.get("raw", 0)) if isinstance(declared, dict) else float(declared)
    return raw, detail


def full_score(rubric, ledger):
    band = ledger["meta"]["grade_band"]
    column = ledger["meta"]["teaching_column"]
    out = {"band": band, "column": column, "sections": [], "total": 0.0}

    for section in rubric["sections"]:
        sid = section["id"]
        cap = section["max_marks"][band]
        if sid == "teaching":
            rows = score_teaching(section, ledger, band, column)
            known = [r["earned"] for r in rows if r["earned"] is not None]
            raw = sum(known)
            declared = (ledger.get("declared_raw") or {}).get(sid)
            if not known and declared is not None:
                # Nothing itemised, but the submitted form carried a total. Trust it
                # and say so, rather than reporting a zero we know to be wrong.
                raw = float(declared.get("raw", 0) if isinstance(declared, dict) else declared)
            marks, wasted = raw_to_marks(section, raw, band)
            unknown = [r for r in rows if r["earned"] is None]
            out["sections"].append({
                "id": sid, "name": section["name"], "cap": cap, "raw": raw,
                "marks": marks, "wasted": wasted, "rows": rows,
                "unrecorded": [r["name"] for r in unknown],
            })
        else:
            raw, detail = collect_pool(section, ledger)
            marks, wasted = raw_to_marks(section, raw, band)
            out["sections"].append({
                "id": sid, "name": section["name"], "cap": cap, "raw": raw,
                "marks": marks, "wasted": wasted, "detail": detail,
                "unrecorded": [],
            })
        out["total"] += out["sections"][-1]["marks"]
    return out


def cmd_score(rubric, ledger, args):
    s = full_score(rubric, ledger)
    print(f"KPI score — {ledger['meta'].get('name','(unnamed)')}, "
          f"year {ledger['meta'].get('year')}, grade band {s['band']}, "
          f"teaching column {s['column']}\n")
    print(f"{'Section':<48}{'Marks':>12}{'Cap':>6}{'Raw':>8}{'Wasted':>9}")
    print("-" * 83)
    for sec in s["sections"]:
        wasted = f"{sec['wasted']:.1f}" if sec["wasted"] else "-"
        print(f"{sec['name'][:47]:<48}{sec['marks']:>9.1f}   {sec['cap']:>5}{sec['raw']:>8.1f}{wasted:>9}")
    print("-" * 83)
    print(f"{'TOTAL':<48}{s['total']:>9.1f}   {100:>5}")

    waste = [x for x in s["sections"] if x["wasted"]]
    if waste:
        print("\nRaw points earning zero marks (section already at its cap):")
        for x in waste:
            print(f"  {x['name']}: {x['wasted']:.1f} raw points above the {x['cap']} cap")
    unrec = [(x["name"], x["unrecorded"]) for x in s["sections"] if x["unrecorded"]]
    if unrec:
        print("\nNot scored because the ledger has no value (these may be free marks):")
        for name, items in unrec:
            for i in items:
                print(f"  {name} -> {i}")
    return s


def cmd_marginal(rubric, ledger, args):
    """The number that matters: marks gained from one more unit of each activity."""
    base = full_score(rubric, ledger)
    band = base["band"]
    print("Marginal KPI value of ONE more of each activity, at your current totals.")
    print("Zero means the section is capped and the work earns no KPI mark.\n")
    print(f"{'Activity':<52}{'Raw pts':>8}{'KPI marks':>11}")
    print("-" * 71)
    rows = []
    for section in rubric["sections"]:
        if section["id"] == "teaching":
            continue
        sid = section["id"]
        cur = next(x for x in base["sections"] if x["id"] == sid)
        for aid, a in (section.get("activities") or {}).items():
            per = a.get("lead", 0)
            m_now, _ = raw_to_marks(section, cur["raw"], band)
            m_next, _ = raw_to_marks(section, cur["raw"] + per, band)
            rows.append((a["name"], per, m_next - m_now, sid))
    rows.sort(key=lambda r: (-r[2], -r[1]))
    for name, per, gain, sid in rows:
        flag = "" if gain > 0 else "  <- capped, no KPI gain"
        print(f"{name[:51]:<52}{per:>8.1f}{gain:>11.2f}{flag}")

    tsec = section_by_id(rubric, "teaching")
    trows = score_teaching(tsec, ledger, band, base["column"])
    head = [r for r in trows if r["earned"] is not None and r["earned"] < r["available"]]
    missing = [r for r in trows if r["earned"] is None and r["available"]]
    if head or missing:
        print("\nTeaching and supervision — marks still on the table here:")
        for r in head:
            print(f"  {r['name']}: {r['earned']:.0f}/{r['available']} ({r['note']}) "
                  f"-> {r['available'] - r['earned']:.0f} available")
        for r in missing:
            print(f"  {r['name']}: not recorded, up to {r['available']} available")


def cmd_gaps(rubric, ledger, args):
    s = full_score(rubric, ledger)
    print("Where your marks are, and are not.\n")
    short = [x for x in s["sections"] if x["marks"] < x["cap"] - 1e-9]
    full_ = [x for x in s["sections"] if x["marks"] >= x["cap"] - 1e-9]
    if short:
        print("BELOW CAP — every mark here is real:")
        for x in short:
            print(f"  {x['name']}: {x['marks']:.1f}/{x['cap']}  "
                  f"({x['cap'] - x['marks']:.1f} marks available)")
    if full_:
        print("\nAT CAP — further work here scores nothing on this form:")
        for x in full_:
            extra = f", {x['wasted']:.0f} raw points already wasted" if x["wasted"] else ""
            print(f"  {x['name']}: {x['marks']:.1f}/{x['cap']}{extra}")
    print(f"\nTotal {s['total']:.1f}/100. "
          f"Headroom {100 - s['total']:.1f} marks, all of it in the sections listed above.")
    if short:
        print("\nNote: KPI headroom is not the same as promotion merit. Work that is")
        print("capped here may still count toward promotion, which uses a different")
        print("rubric. Check promotion.criteria_source in profile/researcher.yml.")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["score", "marginal", "gaps"])
    ap.add_argument("--ledger", default="profile/kpi-ledger.yml")
    ap.add_argument("--rubric", default="profile/kpi-rubric.2026.yml")
    args = ap.parse_args()

    rubric = load(Path(args.rubric) if Path(args.rubric).is_absolute() else REPO / args.rubric)
    ledger = load(Path(args.ledger) if Path(args.ledger).is_absolute() else REPO / args.ledger)
    {"score": cmd_score, "marginal": cmd_marginal, "gaps": cmd_gaps}[args.command](rubric, ledger, args)


if __name__ == "__main__":
    main()
