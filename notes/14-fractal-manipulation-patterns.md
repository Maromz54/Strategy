# שיעור 14 — Fractal Manipulation Patterns

מקור: `transcripts/L014_Fractal_Manipulation_Patterns.json` · global 88

## שני דפוסי התמרון הבסיסיים

לאורך ההיסטוריה של הניתוח הטכני היו **שני** דפוסי תמרון בלבד, תחת שמות רבים.

### Trap (מלכודת)

| | היכן | המנגנון |
|---|---|---|
| **Bull Trap** | ברמת **שיא קודם** | מעל שיאים יושבות הוראות **buy stop**. קונים מאמינים שחציית השיא = המשך עלייה. סוחרים גדולים **סופגים את הביקוש הזה** ונכנסים בכיוון ההפוך |
| **Bear Trap** | ברמת **שפל קודם** | מתחת לשפלים יושבות הוראות **sell stop**. סוחרים גדולים סופגים את ההיצע ונכנסים כלפי מעלה |

**ההיגיון קונקרטי, לא מיסטי:** המלכודת עובדת כי יש שם **נזילות ידועה מראש** בצורת
הוראות סטופ. זה ניתן לחיזוי ולכן ניתן לניצול.

### Raid (פשיטה)

סוחרים גדולים קונים/מוכרים **אגרסיבית** כדי לדחוף את המחיר ולגרור סוחרים קטנים —
**לולאת משוב חיובית**. שלוש מטרות אפשריות:
1. להוביל סוחרים קטנים לנקודה שבה תתרחש **מלכודת**
2. להתרחש **אחרי** מלכודת, כדי להכניס את הפוזיציה של הגדולים לרווח
3. **בבידוד**

> "**Not all** price action movements that look like this are manipulation maneuvers
> necessarily. It depends on the **context**."

### ביקורת מפורשת על Wyckoff

Wyckoff קורא לדפוסים האלה `Spring` ו-`UTAD` ומניח שהם מתרחשים משמעותית **רק** בתחילת או
בסוף מגמה.

> "However, this basic pattern can occur in **any place** in the chart, and in **various
> scales**."

זו לא הערת אגב — זו ההצדקה לכל השיעור. אם התמרון פרקטלי, הוא קיים בכל סקאלה ובכל מקום.

---

## Fractal Manipulations — אותו היגיון על נרות סמוכים ⭐

```
תמרון רחב      →  broad highs & lows
תמרון פרקטלי   →  adjacent candle highs & lows
```

### ההגדרות — קודדות במלואן

> "The fractal bull trap occurs when the current candle **pierces the previous candle high
> without closing above it**."

```python
fractal_bull_trap = (high[t] > high[t-1]) and (close[t] <= high[t-1])
fractal_bear_trap = (low[t]  < low[t-1])  and (close[t] >= low[t-1])
```

**זו התבנית הנקייה ביותר בקורס כולו** — שני תנאים, בלי פרמטרים חופשיים.

> "There are **many forms** in which a fractal trap can occur in terms of the intrinsic
> properties. The **important feature** here is the **piercing** of the previous candle
> **without breaking** above or below it."

כלומר: התכונות הפנימיות של הנר יכולות להיות כל דבר. הגדרת התבנית תלויה **רק** בגיאומטריה
מול הנר הקודם.

### Double / Triple Fractal Traps

הדפוס חוזר על עצמו לנר או שניים נוספים ⇒ המחיר נדחף שוב ושוב בעוד הגדולים סופגים.

### אין fractal raid בבידוד

> "There is **no fractal raid in isolation** because it's usually a **one-candle pattern**."

לכן raid ברמה הפרקטלית מופיע רק כחלק מהיברידי.

---

## Hybrid Fractal Manipulations (HFM)

```
Fractal Analysis  ∩  Traps  ∩  Raids   =   HFM
```

ארבע הצורות שהוצגו:

| | |
|---|---|
| Fractal **Bear Trap → Bull Raid** | Fractal **Bull Trap → Bear Raid** |
| Fractal **Bull Raid → Bull Trap** | Fractal **Bear Raid → Bear Trap** |

### חוק הסיווג ⭐

> "When there is a **mixture of both bull and bear** signals, the fractal manipulation can be
> a **reversal or a continuation** signal. When there are **two bullish** signals or **two
> bearish** signals, it's usually a **reversal or a dynamic frequency stop**."

```
מעורב (בולי + ברי)        →  RHF (Reversal Hybrid Fractal)  או  CHF (Continuation Hybrid Fractal)
חד-כיווני (בולי + בולי)   →  היפוך  או  DFS
חד-כיווני (ברי + ברי)     →  היפוך  או  DFS
```

**שים לב שבשני המקרים ההכרעה אינה חד-משמעית.** הדפוס לבדו **אינו מספיק** — הוא מצמצם
לשתי אפשרויות, וההקשר (כוחות חיצוניים, מיקום, תדירות) מכריע ביניהן. זה עקבי לחלוטין עם
הארכיטקטורה משיעור 3.

### התמרון והממד הפרקטלי

> "Notice how the manipulations **increase the fractal dimension of the vector for a brief
> moment**."

מתחבר לשיעור 12: DFS = הממד עולה. תמרון = הממד עולה לרגע. שניהם קפיצות זמניות בחספוס.

---

## Self-Similar Manipulations

תמרון **פרקטלי** שמתרחש **בתוך** תמרון **רחב**. הדוגמה: bull trap רחב, שבו נר החדירה
עצמו מכיל bull trap פרקטלי קטן בתוכו.

> "It's **pointless to memorize all the variations**. It's better to **understand the
> elements** that compose them."

---

## שתי מסקנות הסיום — שתיהן חשובות ⭐

### 1. תמרון מייצר קו תדירות אוטומטית

> "manipulations — broad, fractal, or self-similar — **always generate some kind of frequency
> line**."

זה מקשר את שיעור 14 ישירות ל-12. **כל תמרון שמזוהה הוא גם רמה חדשה שנולדה.** כלומר
זיהוי מלכודת אינו רק אות — הוא גם מייצר את הרמה שממנה יימדד הסטופ בהמשך.

### 2. יישוב הסתירה עם אפקט הפרפר ⭐

הייתה כאן לכאורה סתירה: raid הוא במהותו תנועה **אגרסיבית**, ואילו שיעור 13 דורש אותות
**קטנים** מתחת ל-2σ. השיעור פותר אותה במפורש:

> "A raid **in the home timeframe** has **high volatility**, but when it happens in the
> context of **fractal manipulation patterns**, the raid is a **low to medium volatility**
> candle in the home timeframe, which aligns with the idea of the **Butterfly Effect**."

כלומר: ה-raid ה**פרקטלי** הוא raid של טווח זמן **נמוך יותר**, ולכן בטווח הבית הוא נראה
כנר צנוע. **הוא עובר את פילטר ה-2σ.** אין סתירה — יש עקביות סקאלתית.

## פערים פתוחים

- **מהו "raid" ברמה הפרקטלית, מספרית?** המלכודת הוגדרה בדיוק; ה-raid לא. מהשקפים הוא
  "נר גדול בעל גוף ארוך וצללים קטנים" — כלומר `body%` גבוה + `body_size` גדול יחסית.
  אבל **אין סף**. פער מימוש ממשי ב-HFM.
- **"pierces" — בכמה?** האם חדירה של טיק אחד נחשבת? נדרש מינימום, אחרת רעש ייספר כמלכודת.
- ההכרעה בין RHF ל-CHF, ובין היפוך ל-DFS, נשארת להקשר — בלי כלל מפורש.
