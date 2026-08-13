#!/usr/bin/env python3
"""Generate BOM.md from the per-subsystem CSVs in src/bom/.

The CSVs are the source of truth. Run this after editing any of them:

    python3 tools/build-bom.py

Use --check to verify BOM.md is up to date without writing (exits 1 on drift).
"""

import csv
import glob
import os
import sys
from collections import Counter, OrderedDict, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEADER = ["subsystem", "category", "item", "part_no", "spec", "qty", "location", "notes"]

# Display order for subsystems and the categories within each.
SUBSYSTEMS = OrderedDict([
    ("wheelbase", "Wheelbase"),
    ("pedals", "Pedals"),
    ("wheel-rim", "Steering Wheel Rim"),
    ("shifter", "Shifter"),
    ("handbrake", "Handbrake"),
    ("chassis", "Rig Chassis"),
])
CATEGORIES = ["electronics", "mechanics", "bearings", "printed",
              "fasteners", "springs", "consumables", "tools"]
CATEGORY_TITLES = {
    "electronics": "Electronics",
    "mechanics": "Mechanics",
    "bearings": "Bearings",
    "printed": "3D printed parts",
    "fasteners": "Fasteners",
    "springs": "Springs",
    "consumables": "Consumables",
    "tools": "Tools",
}
# Categories rolled up into the consolidated shopping list. Grouping is keyed on
# (item, part_no, spec) so an ISO7380 M5x20 is never merged with a DIN7991 M5x20.
ROLLUP = {"fasteners", "bearings", "springs"}


def load():
    rows = []
    for path in sorted(glob.glob(os.path.join(ROOT, "src", "bom", "bom-*.csv"))):
        with open(path, newline="", encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            if reader.fieldnames != HEADER:
                sys.exit("%s: unexpected header %s" % (path, reader.fieldnames))
            rows.extend(reader)
    return rows


def cell(value):
    """Escape a value for use inside a Markdown table cell."""
    return (value or "").replace("|", "\\|").strip() or "—"


def render(rows):
    by_sub = defaultdict(list)
    for row in rows:
        by_sub[row["subsystem"]].append(row)

    order = list(SUBSYSTEMS)
    flagged = sorted(
        [r for r in rows if r["notes"].startswith(("TODO:", "VERIFY:"))
         or " TODO:" in r["notes"] or " VERIFY:" in r["notes"]],
        key=lambda r: order.index(r["subsystem"]))

    out = []
    w = out.append
    w("# Bill of Materials")
    w("")
    w("Compiled parts lists for every subsystem in this repo. This is a compilation of")
    w("**other people's open-source projects** — see [Credits](./README.md#credits) for")
    w("who designed what.")
    w("")
    w("> [!IMPORTANT]")
    w("> **This file is generated.** The CSVs in [`src/bom/`](./src/bom) are the source of")
    w("> truth — edit those, then run `python3 tools/build-bom.py`.")
    w("")
    w("**Conventions**")
    w("")
    w("- **No purchase links.** The upstream sources were full of Amazon/AliExpress")
    w("  affiliate shortlinks that rot quickly and cannot be verified. Manufacturer and")
    w("  standard part numbers (`DIN7991`, `6800-ZZ`, `JKK60-5-C-150-A1-F4-M`) are kept —")
    w("  those are the durable sourcing information.")
    w("- **Blank quantity** means the upstream source genuinely did not state one. Nothing")
    w("  here is guessed.")
    w("- **`TODO:`** marks a part the source references but never specifies.")
    w("  **`VERIFY:`** marks a contradiction in the source. Both are listed in")
    w("  [Known gaps](#known-gaps).")
    w("- **`ALTERNATIVE n of m`** means pick one — those quantities are *not* additive.")
    w("")
    w("## Contents")
    w("")
    for key, title in SUBSYSTEMS.items():
        n = len(by_sub.get(key, []))
        w("- [%s](#%s) — %d line item%s" % (title, key, n, "" if n == 1 else "s"))
    w("- [Consolidated hardware list](#consolidated-hardware-list)")
    w("- [Known gaps](#known-gaps)")
    w("")

    for key, title in SUBSYSTEMS.items():
        sub_rows = by_sub.get(key, [])
        w('<a id="%s"></a>' % key)
        w("")
        w("## %s" % title)
        w("")
        if not sub_rows:
            w("_No parts recorded yet._")
            w("")
            continue
        for cat in CATEGORIES:
            cat_rows = [r for r in sub_rows if r["category"] == cat]
            if not cat_rows:
                continue
            w("### %s" % CATEGORY_TITLES[cat])
            w("")
            w("| Item | Part no. | Spec | Qty | Location | Notes |")
            w("|---|---|---|---|---|---|")
            for r in cat_rows:
                w("| %s | %s | %s | %s | %s | %s |" % (
                    cell(r["item"]), cell(r["part_no"]), cell(r["spec"]),
                    cell(r["qty"]), cell(r["location"]), cell(r["notes"])))
            w("")

    # --- Consolidated hardware list -------------------------------------------------
    w('<a id="consolidated-hardware-list"></a>')
    w("")
    w("## Consolidated hardware list")
    w("")
    w("Fasteners, bearings and springs summed across **every** subsystem and every")
    w("assembly step, so repeated parts are ordered once. Grouped on item + part number +")
    w("spec, so a countersunk `DIN7991 M5x20` is never merged with a button-head")
    w("`ISO7380 M5x20`.")
    w("")
    for cat in ["fasteners", "bearings", "springs"]:
        totals = Counter()
        where = defaultdict(Counter)
        partial = set()
        for r in [x for x in rows if x["category"] == cat]:
            k = (r["item"], r["part_no"], r["spec"])
            if r["qty"]:
                totals[k] += int(r["qty"])
            else:
                totals[k] += 0
                partial.add(k)
            where[k][SUBSYSTEMS[r["subsystem"]]] += 1
        if not totals:
            continue
        w("### %s" % CATEGORY_TITLES[cat])
        w("")
        w("| Item | Part no. | Spec | Total qty | Used in |")
        w("|---|---|---|---|---|")
        for k in sorted(totals, key=lambda k: (k[1], k[2], k[0])):
            qty = str(totals[k]) if totals[k] else "—"
            if k in partial:
                qty += " +?" if totals[k] else ""
            w("| %s | %s | %s | **%s** | %s |" % (
                cell(k[0]), cell(k[1]), cell(k[2]), qty,
                ", ".join("%s (%d)" % (s, n) for s, n in sorted(where[k].items()))))
        w("")
    w("`+?` means at least one contributing line item had no stated quantity.")
    w("")

    # --- Known gaps -----------------------------------------------------------------
    w('<a id="known-gaps"></a>')
    w("")
    w("## Known gaps")
    w("")
    w("%d line items carry a `TODO:` or `VERIFY:` flag. These are faults in the upstream" % len(flagged))
    w("sources that were preserved rather than papered over — resolve them before ordering.")
    w("")
    w("| Subsystem | Item | Flag |")
    w("|---|---|---|")
    for r in flagged:
        flag = "VERIFY" if "VERIFY:" in r["notes"] else "TODO"
        w("| %s | %s | **%s** — %s |" % (
            SUBSYSTEMS[r["subsystem"]], cell(r["item"]), flag,
            cell(r["notes"].split("VERIFY:")[-1].split("TODO:")[-1])))
    w("")
    return "\n".join(out) + "\n"


def main():
    text = render(load())
    target = os.path.join(ROOT, "BOM.md")
    if "--check" in sys.argv:
        current = open(target, encoding="utf-8").read() if os.path.exists(target) else ""
        if current != text:
            sys.exit("BOM.md is out of date — run: python3 tools/build-bom.py")
        print("BOM.md is up to date")
        return
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(text)
    print("wrote %s" % target)


if __name__ == "__main__":
    main()
