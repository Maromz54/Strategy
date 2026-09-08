#!/usr/bin/env python3
"""מדפיס שיעורים בפורמט דחוס לקריאה: תמלול + תיאורי מסך, בלי ה-chunks הכפולים.
שימוש: dump.py <course> <n> [n...]   |   dump.py <course> 13-22
"""
import json, glob, sys, os
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
course = sys.argv[1]
nums = []
for a in sys.argv[2:]:
    if "-" in a: lo, hi = a.split("-"); nums += list(range(int(lo), int(hi) + 1))
    else: nums.append(int(a))
for n in nums:
    hits = glob.glob(os.path.join(ROOT, "transcripts", course, f"L{n:03d}_*.json"))
    if not hits: print(f"\n!! אין שיעור {n} ב-{course}"); continue
    d = json.load(open(hits[0]))
    print(f"\n{'='*70}\n{course} L{n:03d} — {d['displayTitle']}\n{'='*70}")
    print(d["content"]["fullText"])
    ev = d.get("timeline", {}).get("keyEvents", [])
    if ev:
        print("\n--- ON SCREEN ---")
        for e in ev: print(f"[{e['timestamp']}] {e['description']}")
