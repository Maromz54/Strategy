#!/usr/bin/env python3
"""בונה notes/COVERAGE.md — איזה שיעור עובד לכדי הערות ואיזה לא.

שיעור נחשב מכוסה אם קובץ הערות כלשהו מזכיר את שם קובץ התמלול שלו.
זה מודד כיסוי בפועל ולא הצהרת כוונות.
"""
import glob, os, re, json
from collections import defaultdict

ROOT  = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
ORDER = ["price_action_vol1", "price_action_vol2", "price_action_vol3", "fractal_trading"]

notes_text = ""
for n in glob.glob(os.path.join(ROOT, "notes", "**", "*.md"), recursive=True):
    if os.path.basename(n) in ("COVERAGE.md", "README.md"): continue
    notes_text += open(n).read()

courses, totals = defaultdict(list), defaultdict(lambda: [0, 0])
for course in sorted(os.listdir(os.path.join(ROOT, "transcripts"))):
    cdir = os.path.join(ROOT, "transcripts", course)
    if not os.path.isdir(cdir): continue
    for f in sorted(glob.glob(os.path.join(cdir, "L*.json"))):
        base = os.path.basename(f)
        d = json.load(open(f))
        done = base in notes_text
        courses[course].append((int(base[1:4]), d.get("displayTitle"), done,
                                len(d["content"]["fullText"])))
        totals[course][0] += done; totals[course][1] += 1

done_all = sum(v[0] for v in totals.values()); all_all = sum(v[1] for v in totals.values())
with open(os.path.join(ROOT, "notes", "COVERAGE.md"), "w") as o:
    o.write("# מעקב כיסוי\n\n")
    o.write("נוצר על ידי `tools/coverage.py`. שיעור מסומן ✅ רק אם קובץ הערות מזכיר את\n")
    o.write("קובץ התמלול שלו בשמו — כלומר זה מודד כיסוי בפועל, לא הצהרה.\n\n")
    o.write(f"## סה\"כ: {done_all} / {all_all} שיעורים ({100*done_all//all_all}%)\n\n")
    o.write("| קורס | מכוסה | סה\"כ |\n|---|---|---|\n")
    for c in sorted(totals, key=lambda c: (ORDER.index(c) if c in ORDER else 99, c)):
        d_, t_ = totals[c]
        o.write(f"| `{c}` | {d_} | {t_} |\n")
    for c in sorted(courses, key=lambda c: (ORDER.index(c) if c in ORDER else 99, c)):
        o.write(f"\n### {c}\n\n| # | שיעור | chars | |\n|---|---|---|---|\n")
        for n, t, done, ch in courses[c]:
            o.write(f"| {n:02d} | {t} | {ch} | {'✅' if done else '⬜'} |\n")
print(f"כיסוי: {done_all}/{all_all} ({100*done_all//all_all}%)")
for c in sorted(totals, key=lambda c: (ORDER.index(c) if c in ORDER else 99, c)):
    d_, t_ = totals[c]
    bar = "█" * (20*d_//t_) + "░" * (20 - 20*d_//t_)
    print(f"  {c:20s} {bar} {d_:3d}/{t_}")
