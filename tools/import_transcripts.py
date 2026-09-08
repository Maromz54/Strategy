#!/usr/bin/env python3
"""מייבא תמלולי שיעורים מתיקיית ההעלאות אל transcripts/<course>/, ובונה אינדקסים.

אידמפוטנטי — אפשר להריץ שוב בכל פעם שמגיעים קבצים חדשים.

מספור: אף אחד משדות המקור אינו אמין לבדו —
  * `course.lessonNumber` שגוי בחלק מהקבצים (למשל fractal_trading 28, vol1 "The Level One").
  * קידומת שם קובץ הווידאו כוללת כפילויות ("07 - Pt1"/"07 - Pt2") ודילוגים.
  * שם קובץ ההעלאה שגוי בחלק מקבצי vol2.
לכן: דה-דופליקציה לפי `id`, מיון לפי קידומת הווידאו כמספר עשרוני (כך ש-08.1
נופל בין 08 ל-09), ואז מספור רץ. הקידומת המקורית נשמרת באינדקס למעקב.
"""
import json, glob, os, re, shutil, sys
from collections import defaultdict

UPLOADS = sys.argv[1] if len(sys.argv) > 1 else \
    "/root/.claude/uploads/f26e8a4c-e6f6-5f89-91e9-052d8808e9c1"
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     "..", "transcripts"))
TITLES = {
    "price_action_vol1": "Price Action Trading Course, Vol. 1 — התיאוריה",
    "price_action_vol2": "Price Action Trading Course, Vol. 2 — יישום מעשי",
    "price_action_vol3": "Price Action Trading Course, Vol. 3 — יישום מעשי",
    "fractal_trading":   "Fractal Trading: Mastering Price Action & Beyond",
}
ORDER = ["price_action_vol1", "price_action_vol2", "price_action_vol3", "fractal_trading"]

slugify = lambda s: re.sub(r'[^A-Za-z0-9]+', '_', s or "untitled").strip('_')

def sort_key(d, src):
    """קידומת שם קובץ הווידאו כמספר עשרוני; נפילה אחורה לשם ההעלאה."""
    m = re.match(r'^(\d+(?:\.\d+)?)', d.get("fileName", "").strip())
    if m: return float(m.group(1))
    m = re.search(r'_L0*(\d+)_', os.path.basename(src))
    return float(m.group(1)) if m else 0.0

seen, courses = {}, defaultdict(list)
for src in sorted(glob.glob(os.path.join(UPLOADS, "*.json"))):
    try: d = json.load(open(src))
    except Exception as e: print(f"  דילוג {os.path.basename(src)}: {e}"); continue
    course = d.get("course", {}).get("name")
    if not course or "content" not in d: continue
    uid = d.get("id") or d.get("fileName")
    if uid in seen:                                  # אותו שיעור הועלה פעמיים
        print(f"  כפילות — מדלג: {os.path.basename(src)[:56]}")
        continue
    seen[uid] = True
    courses[course].append((sort_key(d, src), d, src))

for course in sorted(courses, key=lambda c: (ORDER.index(c) if c in ORDER else 99, c)):
    # שובר שוויון: שם קובץ הווידאו המלא — שמות ההעלאה מתחילים בהאש אקראי
    items = sorted(courses[course], key=lambda x: (x[0], x[1].get("fileName", "")))
    dest_dir = os.path.join(ROOT, course); os.makedirs(dest_dir, exist_ok=True)
    for stale in glob.glob(os.path.join(dest_dir, "L*.json")): os.remove(stale)
    rows = []
    for n, (key, d, src) in enumerate(items, 1):
        fname = f"L{n:03d}_{slugify(d.get('displayTitle'))}.json"
        shutil.copy(src, os.path.join(dest_dir, fname))
        os.chmod(os.path.join(dest_dir, fname), 0o644)
        rows.append((n, d.get("displayTitle"), len(d["content"]["fullText"]),
                     len(d.get("timeline", {}).get("keyEvents", [])), fname,
                     d.get("fileName", "")))
    with open(os.path.join(dest_dir, "INDEX.md"), "w") as o:
        o.write(f"# {TITLES.get(course, course)}\n\n{len(rows)} שיעורים.\n\n")
        o.write("`video` = קידומת שם קובץ הווידאו המקורי, לצורך מעקב.\n\n")
        o.write("| # | שיעור | chars | events | video |\n|---|---|---|---|---|\n")
        for n, t, c, e, fn, vid in rows:
            o.write(f"| {n:02d} | [{t}]({fn}) | {c} | {e} | `{vid[:14]}` |\n")
        o.write(f"\n**סה\"כ:** {sum(r[2] for r in rows):,} תווי תמלול · "
                f"{sum(r[3] for r in rows)} תיאורי מסך\n")
    print(f"{course:20s} {len(rows):3d} שיעורים · {sum(r[2] for r in rows):>7,} תווים")
