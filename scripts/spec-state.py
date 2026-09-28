#!/usr/bin/env python3
"""Read SPEC.md and SPEC.ledger.jsonl, print the rung and what is missing.

Usage: spec-state.py path/to/SPEC.md
Exit 0 on Written or higher, 1 on not Written, 2 on a forbidden state (a seat tagged filled with no asked row)."""
import json, re, sys
from pathlib import Path

CHANGE_KINDS = {"build-stopped", "build-changed", "limit-changed", "goal-revised", "intent-dropped"}

def section(text, name):
    m = re.search(rf"^## {name}\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1).strip() if m else ""

def is_blank(body):
    body = re.sub(r"<[^>]*>", "", body).strip()
    return not body

def seats_from(limits):
    rows = []
    for line in limits.splitlines():
        if not line.startswith("|"): continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 3 or cells[0] in ("Cost", "") or set(cells[0]) <= {"-"}: continue
        if cells[1].startswith("<"): continue
        rows.append({"cost": cells[0], "bearer": cells[1], "seat": cells[2].lower()})
    return rows

def main(path):
    spec = Path(path)
    text = spec.read_text()
    ledger_path = spec.with_name(spec.stem + ".ledger.jsonl")
    rows = []
    if ledger_path.exists():
        for n, line in enumerate(ledger_path.read_text().splitlines(), 1):
            if line.strip():
                try: rows.append(json.loads(line))
                except json.JSONDecodeError: print(f"ledger line {n}: not JSON"); return 1
    missing = []
    m = re.search(r"^cost_class:\s*(reversible|irreversible)", text, re.M)
    cost_class = m.group(1) if m else None
    if not cost_class: missing.append("cost_class (reversible | irreversible)")
    for part in ("Intent", "Goal", "Limits"):
        if is_blank(section(text, part)): missing.append(f"{part} section")
    seats = seats_from(section(text, "Limits"))
    if not seats and "Limits section" not in missing: missing.append("at least one cost with a named bearer")
    for s in seats:
        if s["seat"] not in ("filled", "empty"): missing.append(f"seat for '{s['bearer']}' tagged filled or empty (got '{s['seat']}')")
    if not any(r.get("kind") == "written" for r in rows): missing.append("a 'written' row in the ledger")

    asked = {r.get("seat") for r in rows if r.get("kind") == "asked"}
    forbidden = [s["bearer"] for s in seats if s["seat"] == "filled" and s["bearer"] not in asked]
    if forbidden:
        print("FORBIDDEN: seat tagged filled with no 'asked' row: " + ", ".join(forbidden))
        return 2
    if missing:
        print("rung: not Written")
        for x in missing: print("  missing: " + x)
        return 1
    rung = "Written"
    empty = [s["bearer"] for s in seats if s["seat"] == "empty"]
    unasked_irreversible = empty if cost_class == "irreversible" else []
    if not unasked_irreversible: rung = "Closed"
    written_date = max(r["date"] for r in rows if r.get("kind") == "written")
    tested = [r for r in rows if r.get("kind") in CHANGE_KINDS and r.get("date", "") > written_date]
    if rung == "Closed" and tested: rung = "Tested"
    print(f"rung: {rung}   cost_class: {cost_class}   seats: {len(seats)} ({len(empty)} empty)")
    for b in empty: print(f"  empty seat: {b}")
    if rung == "Written":
        print("  to Closed: ask " + ", ".join(unasked_irreversible))
        print("  build: blocked until Closed (irreversible)")
    elif rung == "Closed":
        print("  to Tested: a row that stopped or changed a build")
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2: print(__doc__); sys.exit(1)
    sys.exit(main(sys.argv[1]))
