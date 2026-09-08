# שיעור 15 — Advanced Fractal Candles

מקור: `transcripts/L015_Advanced_Fractal_Candles.json` · global 89

> **⭐ השיעור המרכזי של הקורס.** כאן מתכנסים כל השיעורים הקודמים לכדי **אות כניסה יחיד**,
> ובמבנה שהוא כמעט **מודל ניקוד מוכן לקידוד**.

---

## הגדרת Fractal Candle — קודדת במלואה

```
Bias  ∩  Shadow Changes   =   Fractal Candle
```

```python
bullish_fc = (close[t] > open[t]) and (low[t]  < low[t-1])   # הטיה בולית + שפל נמוך יותר
bearish_fc = (close[t] < open[t]) and (high[t] > high[t-1])  # הטיה ברית  + שיא גבוה יותר
```

**כלל הזיהוי:** אם הנר הנוכחי בולי — בודקים את שינוי הצל **התחתון**. אם ברי — את שינוי
הצל **העליון**.

> "**The bias of the previous candle is not important.**"

### למה זה משמעותי — הדיסוננס

> "the Fractal Candle implies a **contradiction or dissonance** in terms of intrinsic
> properties (bias and shadows)."

| | ההטיה | הצללים |
|---|---|---|
| **Bullish FC** | כלפי **מעלה** | הצללים התחתונים נעים כלפי **מטה** |
| **Bearish FC** | כלפי **מטה** | הצללים העליונים נעים כלפי **מעלה** |

זה בדיוק דגל ה-`conflict` שזיהיתי בשיעור 6, וכאן הוא מקבל שם ומעמד. **הידע בתכונות
הפנימיות הוא שמאפשר לראות את הסתירה הזו — היא אינה גלויה לעין.**

---

## RFC מול CFC — סיווג לפי Prior Activity

| | תנאי | נוסחה מהשקף |
|---|---|---|
| **RFC** (Reversal) | ההטיה **חולקת** על ה-prior activity | בולי + שפל נמוך + **תנועה יורדת** |
| | | ברי + שיא גבוה + **תנועה עולה** |
| **CFC** (Continuation) | ההטיה **מסכימה** עם ה-prior activity | בולי + שפל נמוך + **תנועה עולה** |
| | | ברי + שיא גבוה + **תנועה יורדת** |

זה השימוש הראשון והישיר בכוח החיצוני הרביעי (שיעור 10). ה-`prior_activity` הוא בדיוק
המשתנה שמכריע כאן.

---

## FC מול Fractal Manipulation — יחס הכלה

> "**All** fractal candles imply a fractal manipulation, but **not all** fractal manipulations
> are fractal candles. That's because a fractal trap is only related to the **candle
> shadows** and doesn't take the **bias** into account."

```
{ Fractal Candles }  ⊂  { Fractal Manipulations }
```

ההיגיון: ב-bullish FC המחיר **דוקר מתחת לשפל הקודם אך סוגר גבוה יותר** — כלומר מדיח
מוכרים כלפי מטה ואז סוגר למעלה. זו בדיוק מלכודת דובים פרקטלית, פלוס תנאי ההטיה.

---

## Fractal Butterfly ⭐ — הרעיון היפה בשיעור

`Expanding FC` + `high body%` ⟹ hybrid fractal manipulation (מלכודת ואז raid בטווח נמוך).

> "The expansion fractal candle is a **window to a lower timeframe where volatility already
> picked up**, but in the home timeframe, **volatility is still low**."

**זה בדיוק מה שאנחנו רוצים לפי שיעור 13:** להיכנס כשהתנודתיות עדיין נמוכה אצלנו, בזמן
שהיא כבר התפרצה בסקאלה שמתחת. הפרפר כבר הניף כנפיים — ההוריקן עדיין לא הגיע אלינו.

---

## Fractal Signal Alternation — למה expansion חזק מ-progression ⭐

| וריאציה | הצד התחתון | הצד העליון | תוצאה |
|---|---|---|---|
| FC כ-**downward progression** | bullish **reversal** divergence | bearish **continuation** divergence | **דיסוננס** → FC **חלש** |
| FC כ-**expansion** | bullish **reversal** divergence | **בסנכרון** עם האוסילטור (convergence) | הדיסוננס נעלם → FC **חזק** |

זה מיישם את כלל ה-`signal alternation` משיעור 9 ברמת הנר הבודד, ונותן **דירוג אובייקטיבי
בין וריאציות של FC**:

```
expansion  >  expansion חד-צדדי  >  progression
```

---

# ⭐⭐ Integrated Fractal Candle — עשרת המרכיבים

זהו **צ'ק-ליסט הכניסה של האסטרטגיה**. השיעור מציג אותו כרשימה ממוספרת:

| # | מרכיב | מה בדיוק, ולמה זה מחזק |
|---|---|---|
| 1 | **Expanding Range Dynamics** | המחיר הלך לכיוון אחד ואז התהפך משמעותית לצד שמסכים עם ההטיה. *"as if sellers opened the door and found strong buyers on their way"* |
| 2 | **High Body%** | ודאות. FC חיצוני עם body% גבוה חזק מאחד עם body% נמוך — צל עליון גדול ב-FC בולי **סותר** את האות |
| 3 | **DFB & DFS** | ה-FC שובר את התדירות הדינמית של הווקטור הנוכחי. **מרמז אוטומטית על DFS בצד הנגדי ל-DFB** |
| 4 | **Butterfly Effect** | תנודתיות נמוכה/בינונית בזמן האות, שעולה **אחרי** הכניסה |
| 5 | **Low Fractal Dimension** | price action חלק → התנהגות צפויה ומסודרת יותר |
| 6 | **Overextension** | דיברגנס במהירות / תאוצה / נפח — הכוחות מאחורי המחיר לא מסונכרנים איתו |
| 7 | **Final Trend Phase** | בשלבים הסופיים של המגמה (Elliott: אחרי 3 או 5 גלים ברורים) |
| 8 | **Reaction Without Penetration of Barrier** | המחיר **מגיב** למחסום **בלי לדקור אותו כלל** |
| 9 | **Fractal Manipulations** | **חדירה ללא הפרה** — הצל דוקר רמה קודמת אך לא סוגר מעבר לה |
| 10 | **Unsustainable Motion** | תנועה מאיצה **שמובילה אל** ה-FC ⟹ היפוך קרב, כי המחיר מתיש כוח מהר מכפי שהוא צובר |

### ⚠️ ההבחנה העדינה בין 8 ל-9 — קל לבלבל

השיעור מדגיש אותה במפורש:

```
מרכיב 9 (מניפולציה):  הצל  דוקר  את הרמה, אך אין סגירה מעבר לה   →  penetration without violation
מרכיב 8 (מחסום):      הצל  אינו דוקר את הרמה כלל                  →  reaction without penetration
```

**אלה שני מצבים גיאומטריים שונים ושניהם מחזקים** — צריך שני תנאים נפרדים בקוד.

### מדד כמותי למרכיב 4 ⭐

> "the **smaller the vertical distance between the DFB and the DFS**, the **greater the
> butterfly effect**."

```python
butterfly_strength = 1 / abs(dfb_level - dfs_level)     # ככל שקטן יותר — חזק יותר
```

זה אחד המדדים הכמותיים הבודדים שהקורס נותן במפורש. שווה זהב לניקוד.

### מה שהופך את זה למודל ניקוד ⭐

> "an integrated fractal candle **must not have all** of these elements to be valid, but the
> **more elements there are, the better the signal**."

> "the **more elements** integrated in the fractal candle, the **less frequently it appears**.
> This is the **trade-off between frequency and integration**."

**זו הצהרה מפורשת שהאות הוא רציף, לא בינארי.** המבנה המתבקש:

```python
def integrated_fc_score(bar, ctx):
    elements = {
        "expanding_range":   ...,   # 1
        "high_body_pct":     ...,   # 2
        "dfb_and_dfs":       ...,   # 3
        "butterfly":         ...,   # 4  — משוקלל לפי המרחק DFB↔DFS
        "low_fractal_dim":   ...,   # 5
        "overextension":     ...,   # 6
        "final_trend_phase": ...,   # 7
        "barrier_no_pierce": ...,   # 8
        "manipulation":      ...,   # 9
        "unsustainable":     ...,   # 10
    }
    return weighted_sum(elements)
```

**וה-trade-off הוא פרמטר תפעולי ישיר:** סף הניקוד קובע את תדירות המסחר. סף גבוה = מעט
עסקאות איכותיות; סף נמוך = יותר עסקאות חלשות יותר. זה בדיוק מה שבקטסט אמור לכייל.

**מה שהשיעור לא נותן: משקלים.** כל עשרת המרכיבים מוצגים כשווי-ערך. סביר שאינם.
→ פער לכיול אמפירי.

---

## סייג חשוב לסיום

> "**Not all price reversals occur with fractal candles.** Often, there is a transition of
> market direction **without** the indication of fractal candles or fractal manipulations."

כלומר ה-FC אינו מנגנון ההיפוך היחיד — הוא מנגנון **אחד** שניתן לזהות בביטחון. בוט שמחכה
רק ל-FC יפספס היפוכים אמיתיים. זה מקובל (עדיף לפספס מלטעות), אבל צריך להיאמר.

## פערים פתוחים

- **משקלים לעשרת המרכיבים** — לא ניתנו.
- **מרכיב 7 (`final trend phase`) דורש ניתוח פאזה** שהקורס לא מלמד. זהו המרכיב היחיד
  שאין לי דרך לקודד מהחומר שנלמד. → יידרש פתרון חיצוני, או להריץ בלעדיו.
- מרכיב 1: מה נחשב "התהפכות **משמעותית**"? ללא סף.
- מרכיב 2: מהו "high body%"? עדיין אין סף מספרי (פער פתוח משיעור 4).
