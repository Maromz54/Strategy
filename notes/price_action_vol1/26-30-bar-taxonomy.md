# vol1 שיעורים 26-30 — טקסונומיית הנרות

מקור: `L026_Fractal_Bar.json`, `L027_Inside_Bar.json`, `L028_Outside_Bar.json`,
`L029_Pressure_Bar.json`, `L030_Hybrid_Bar.json`

---

## ⭐ L026 — Fractal Bar = המקור של ה-Fractal Candle

```
Bearish Fractal Bar:  שיא גבוה יותר מהנר הקודם  +  גוף ברי
Bullish Fractal Bar:  שפל נמוך יותר מהנר הקודם  +  גוף בולי
```

> "These **two conditions must occur**... **both conditions are necessary**."

**זהה מילה במילה ל-`fractal candle` ב-`fractal_trading` L015.** כלומר המושג נולד כאן,
בקורס התיאורטי, והקורס המאוחר רק הרחיב אותו (RFC/CFC, וריאציות, האינטגרציה בת 10 המרכיבים).

### המקור הרעיוני

> "The fractal bar was born by observing how **reversal divergences happen within
> themselves**, which is what I call **fractal divergence**."

> "A fractal bar is a pattern that implies a **reversal divergence in a lower timeframe**."

וחשוב: *"This is a **pure price action** course, so we are not going to plot an RSI on the
chart... there is a way of seeing a fractal bar **just by looking at price**."*

**זו נקודה משמעותית לבוט:** ה-fractal bar הוא **תחליף מחירי טהור לדיברגנס**. אין צורך
ב-RSI כדי לזהות אותו — הוא הדיברגנס עצמו, נצפה בסקאלה אחת למטה.

---

## L027-L030 — ארבעת הסוגים ודירוג החוזק שלהם ⭐

| נר | הגדרה | מה זה אומר | חוזק |
|---|---|---|---|
| **Inside Bar** | מוכל **במלואו** בטווח הנר הקודם | עצירה רגעית של המחיר | 🔻 **חלש** |
| **Outside Bar** | **בולע במלואו** את הנר הקודם | פרץ תנודתיות פתאומי | 🔻 **חלש** |
| **Pressure Bar** | צל אחד או שניים **גדולים באופן חריג** | עליון = לחץ מכירה · תחתון = לחץ קנייה · שניהם = "קרב לחץ גבוה" | 🔹 **חזק יותר** |
| **Fractal Bar** | ראה למעלה | היפוך (דיברגנס בסקאלה נמוכה) | 🔹 חזק |
| **Hybrid Bar** | **שניים או יותר** מהסוגים בנר אחד | צירוף הפרשנויות | ⭐ **החזק ביותר** |

### הדירוג נאמר במפורש, וזה חשוב

> **Inside bar:** "considered to be a **weak signal** because they **can happen all over the
> place**... inside bars happen in some sort of **random** way."

> **Outside bar:** "also considered to be **weak signals**... they happen in a sort of
> **random** way across time."

> **Pressure bar:** "pressure bars tend to appear in **reversal points**, so they are
> considered to be **stronger signals than inside and outside bars**."

**המסקנה לבוט חדה:** inside/outside bar **אינם אות בפני עצמם**. השימוש היחיד בהם הוא
*"when they appear in **hybrid bars**, and/or in combination with other powerful elements
like **supply and demand zones** or **complex line work**"*.

זה חוסך טעות נפוצה — engulfing ו-inside bar הם מהתבניות הפופולריות ביותר במסחר קמעונאי,
וכאן נאמר מפורשות שהן רועשות.

### Pressure Bar מייצר גם רמה

> "the **most important** thing about pressure bars is that they show a **level** where there
> is a lot of buying or selling pressure."

כלומר pressure bar אינו רק אות רגעי — הוא מוליד רמה, בדיוק כמו `wick expansion` ו-`pressure
zone` מ-L020-L021. **שלושתם מייצרים אזורים.**

---

## ⭐ L030 — Hybrid Bar = הזרע של ה-Integrated Fractal Candle

> "A hybrid bar is a **combination of two or more bar types** in one single bar. The
> interpretation is a **combination of the individual interpretations** of all bar patterns
> contained in the bar."

הדוגמאות מהשיעור:

```
Outside + Fractal Bar                      →  היפוך  +  פרץ תנודתיות
Fractal Bar + Buy Pressure + Outside Bar   →  "signaling the market will go up,
                                               which it does quite dramatically right after"
Fractal Bar + Buy & Sell Pressure          →  היפוך + קרב לחץ דו-צדדי
Inside Bar + Buy Pressure                  →  עצירה + לחץ קנייה
```

**זהו בדיוק העיקרון של ה-`Integrated Fractal Candle`** מ-`fractal_trading` L015, בצורתו
המוקדמת והפשוטה: **יותר מרכיבים בנר אחד = אות חזק יותר**. הקורס המאוחר רק הרחיב את רשימת
המרכיבים מ-4 סוגי נרות ל-10 מרכיבים שכוללים גם כוחות חיצוניים.

```
vol1   L030:  hybrid bar              — 4 סוגי נרות, צירוף
FT     L015:  integrated fractal candle — 10 מרכיבים, צירוף משוקלל
```

---

## מפרט קידוד — כל הטקסונומיה

```python
def bar_types(o, h, l, c, po, ph, pl, pc):
    """כל סוגי הנרות של הנר הנוכחי ביחס לקודם. p = previous."""
    t = set()
    if h > ph and c < o: t.add("bearish_fractal")     # ⭐ חזק
    if l < pl and c > o: t.add("bullish_fractal")     # ⭐ חזק
    if h <= ph and l >= pl: t.add("inside")           # 🔻 חלש בפני עצמו
    if h >  ph and l <  pl: t.add("outside")          # 🔻 חלש בפני עצמו
    up, lo = h - max(o, c), min(o, c) - l
    if up > SHADOW_T: t.add("sell_pressure")          # סף — ראה פערים
    if lo > SHADOW_T: t.add("buy_pressure")
    return t                                          # |t| >= 2  ⟹  hybrid bar

# חוזק האות עולה עם |t|, אך inside/outside לבדם אינם אות
```

## פערים

- **"unusually large wick"** — אין סף ל-pressure bar. כנראה מול חלון סטטיסטי, כמו
  סיווג הטווח ב-`fractal_trading` L004. אכייל בבקטסט.
- **inside bar** — האם ההכלה כוללת שוויון (`h <= ph`) או דורשת אי-שוויון חד? לא נאמר.
- אין משקלים לצירופים ב-hybrid bar — אותו פער כמו ב-Integrated FC.
