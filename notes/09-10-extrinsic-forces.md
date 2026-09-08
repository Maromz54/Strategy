# שיעורים 09-10 — Extrinsic Forces (חלקים 1+2)

מקור: `transcripts/L009_08_1_Extrinsic_Forces_PART_1.json` (global 83),
`transcripts/L010_08_2_Extrinsic_Forces_PART_2.json` (global 84)

## התפקיד

> "the extrinsic forces of the market can **strengthen, weaken, or even change** the
> interpretation we get from the intrinsic properties."

זה מאשש את מה שסימנתי בשיעור 3: הכוחות החיצוניים אינם מסנן שרץ **אחרי** האות — הם
**מודולציה** על הפרשנות עצמה. `interpretation = f(intrinsic, extrinsic)`, לא
`signal AND context_ok`.

ארבעת הכוחות: `Location/Trend Phase`, `Overextension`, `Price Barriers`, `Prior Activity`.

---

# כוח 1 — Location / Trend Phase

איפה ה-price action נמצא בתוך המגמה הכוללת.

> **הדוגמה המכוננת:** נר שמפגין ודאות לצד אחד. **באמצע** מגמה → `continuation`.
> **בסוף** מגמה → `exhaustion`, ומשם היפוך. *אותו נר בדיוק, משמעות הפוכה.*

הקורס **אינו** מלמד את שיטות ניתוח הפאזה — הוא סוקר אותן ומפנה החוצה.

| שיטה | תמצית | הערת המרצה |
|---|---|---|
| **Dow** | HH+HL = עלייה, LH+LL = ירידה. `accumulation` = דשדוש לפני עלייה, `distribution` = לפני ירידה. אות קנייה/מכירה בשבירת swing | לא אומרת **כמה רחוק** המחיר בתוך המגמה |
| **Elliott** | דפוסי 5-3 גלים, חוזרים בתוך עצמם (פרקטליים) | "the best results come from the observation of **obvious** patterns" — בגלל אפקט הנבואה המגשימה את עצמה |
| **Wyckoff** | סוחרים מיודעים מתמרנים לא-מיודעים. `Spring` (בתחתית), `UTAD` (בפסגה) | **ביקורת מפורשת:** מניחה שתמרון קורה רק בתחילת/סוף מגמה, וריבוי הכללים מקשה על יישום |

**כלל אישוש הנפח של Dow (קודד):**
```
HH (או LL) + שיא נפח גבוה יותר   →  המגמה מאוששת
HH (או LL) + שיא נפח נמוך יותר   →  המגמה מאבדת כוח
```

---

# כוח 2 — Overextension

הכוחות שמאחורי המחיר: `velocity`, `acceleration`, `volume`.

> **מקור היתרון:** "the implicit forces behind price action **change before price**."

## הבהרה טרמינולוגית מהמרצה

RSI **אינו** אינדיקטור מומנטום. הוא מודד קצב שינוי מחיר = **מהירות**. בפיזיקה
`momentum = velocity × mass`; אינדיקטור מומנטום אמיתי היה כולל מסה.

## סוגי דיברגנס — קודדים במלואם

### Velocity Reversal Divergence (נגד-מגמתי)
```
מחיר HH  +  RSI LH   →  bearish reversal
מחיר LL  +  RSI HL   →  bullish reversal
```
פוטנציאל רווח גדול יותר, **אבל מסוכן יותר**.

### Velocity Continuation Divergence (עם המגמה)
```
מחיר HL  +  RSI LL   →  bullish continuation
מחיר LH  +  RSI HH   →  bearish continuation
```
מטרתו: **לתפוס את סוף התיקון**. קל יותר מלנחש את הקצה.

### Acceleration Divergence
`acceleration` = הנגזרת השנייה של המחיר = קצב השינוי של המהירות.
מימוש: **RSI על ה-RSI** (ה-RSI הראשון הוא ה-source של השני).

```
acceleration divergence  ⟶ מקדים ⟶  velocity divergence  ⟶ מקדים ⟶  מחיר
```

## שלושת המשתנים שקובעים חוזק אות ⭐

### 1. Signal Alternation
אותות reversal ו-continuation **מתחלפים**. סוחרים נוטים לשים לב רק ל-reversal.

> "a **continuation signal tends to be stronger** since it has the **trend on its side**."

**כלל הכרעה:** כשמתחלפים — **העדף את האות שמסכים עם המגמה**.

### 2. Length Between Extremes
```
מרחק גדול יותר בין האקסטרמים  →  אות חזק יותר
מרחק קצר                      →  נטייה לאותות שווא
```

### 3. Self-Similarity — ומסקנה חדה לגבי fractal candle
> "a **fractal candle** represents a divergence in a lower timeframe. However, a fractal
> candle is a **weak** divergence signal **in isolation** in the home timeframe because of
> the **smallest length possible** between adjacent candle extremes."

**מסקנה מפורשת: אסור להשתמש ב-fractal candle כאות דיברגנס בפני עצמו.** לפי כלל 2 הוא
בהכרח האות החלש ביותר שקיים.

אבל אותות יכולים **לקנן זה בתוך זה**, ואז הם **מחזקים** זה את זה — ההפך מ-alternation.
הדוגמה מהשיעור: continuation גדול ⊃ reversal קטן ⊃ fractal candle. שרשרת מאששת.

## דיברגנס נפח

**בסיסי:** התקדמות שיאים/שפלים במחיר מול **שיאים נמוכים יותר** בהיסטוגרמת הנפח.
(עולים → משווים שיאי מחיר; יורדים → משווים שפלי מחיר לשיאי נפח.) ההיסטוגרמה חד-כיוונית
(חיובית בלבד) ולכן מתנהגת מעט אחרת.

**CVD — Cumulative Volume Delta.** נפח מחולק לבולי וברי; `delta` = ההפרש; ה-CVD מצטבר
לאורך זמן. נראה כמו אוסילטור אבל הוא **אינדיקטור נפח טהור**.

| דפוס | מחיר | CVD | מסקנה |
|---|---|---|---|
| **Buying Exhaustion** | HH | לא HH | הקונים מתישים אנרגיה → היפוך ברי |
| **Selling Exhaustion** | LL | לא LL | המוכרים מתישים אנרגיה → היפוך בולי |
| **Selling Absorption** | נכשל ב-LL (עושה HL) | **כן** LL | נפח מכירה גדול אך הקונים סופגים → בולי |
| **Buying Absorption** | נכשל ב-HH (עושה LH) | **כן** HH | נפח קנייה גדול אך המוכרים סופגים → ברי |

**הסימטריה שכדאי לזכור:** `exhaustion` = המחיר מתקדם וה-CVD לא. `absorption` = ה-CVD
מתקדם והמחיר לא.

שלושת המשתנים (alternation, length, self-similarity) חלים גם על CVD. יש "fractal volume".
> "you **should** combine velocity, acceleration, and CVD divergences to increase reliability."

---

# כוח 3 — Price Barriers

**הגדרה:** מכשול להתקדמות המחיר. אם יש מחסום בדרך, הסיכוי להיפוך גבוה יותר.

## שלושה צירי סיווג — נערמים זה על זה

| ציר | ערכים | הבחנה |
|---|---|---|
| **תפקוד** | `Traditional` / `Containment` / שניהם | traditional כפוף ל-**test/switch/retest**; containment **לא** — נועד לסמן overextension ולהחזיק את המחיר |
| **מקור** | `Geometric` / `Numerical` / `Fractal` | גיאומטרי = מגיאומטריית העבר (קווים, תעלות). נומרי = נוסחה על **חלון מתגלגל**. פרקטלי = נוסחה מתמטית ש**מעוגנת בגיאומטריית העבר** במקום בחלון מתגלגל |
| **התנהגות** | `Horizontal` / `Sloped` / `Dynamic` | אופקי/משופע לא משנים כיוון (מגיעים מגיאומטרי); דינמי משנה כיוון (מגיע מנומרי או פרקטלי) |

**דוגמאות מהשיעור:**
- `Bollinger Bands`: הקו **האמצעי** = traditional (test/switch/retest). הרצועות **החיצוניות** = containment. *אותו אינדיקטור, שני תפקידים שונים.*
- `Andrews Pitchfork` = traditional + geometric + sloped
- `Anchored VWAP` = fractal + dynamic — מעוגן בשפל משמעותי (גיאומטריה), מחושב בנוסחה
- `Linear Regression Channel` = fractal + sloped — הרוחב והשיפוע מחושבים נומרית, אך העיגון גיאומטרי

> "Combining barriers of **different kinds** increases the likelihood of detecting a market edge."

## הדינמיקה: לפני / ב / אחרי המחסום

### לפני — שלושה משטרים ⭐

**זהו החוק של שיעור 6 בניסוח גיאומטרי, וכאן הוא הופך לקודד:**

| משטר | גיאומטריה | אנרגיה |
|---|---|---|
| **Sustainable** | תנועה **לינארית** — לא מהר מדי, לא לאט מדי | מתיש וצובר אנרגיה במאוזן |
| **Unsustainable** | תנועה **לא-לינארית מאיצה** (עקומה פרבולית) | מתיש אנרגיה מהר יותר משהוא מסוגל להתאושש |
| **Ambiguous** | תנועה **לא-לינארית מאטה** | **או** מאבד כוח (→היפוך) **או** צובר מחדש (→המשך). לא ניתן להכריע |

```
d²(price)/dt² ≈ 0   →  sustainable
d²(price)/dt² > 0   →  unsustainable   (מאיץ בכיוון המגמה)
d²(price)/dt² < 0   →  ambiguous       (מאט)
```

זה מחבר ישירות ל-`acceleration divergence` מכוח 2 — אותה נגזרת שנייה, שני שימושים.

### ב — שלושה דברים לבחון

1. **התכונות הפנימיות** של הנרות שנוגעים במחסום
2. **דינמיקת test / switch / retest**
3. **מיקום הנר ביחס למחסום** ⭐

> "The candle on the left lands **below** the barrier, so it gives the impression that it's
> being **held** by the resistance. On the right, **the same candle** crosses the barrier
> giving the impression of a **breakout**."

זו הדוגמה הנקייה ביותר בקורס לכך שכוח חיצוני **משנה** את פרשנות התכונות הפנימיות.

**סימן שהמחסום חזק:** המחיר מגיב אליו **בלי להפר אותו**, ויוצר רושם של לחץ קנייה/מכירה.
**אזהרה:** "A barrier might seem strong for a few candles only to be broken right after."

### אחרי — עד מתי המחיר "שבוי"

> "**Until** price action displays signs that it is getting away from the barrier, it's
> susceptible to testing, switching, and retesting **at any point in time**."

הסימן הטוב ביותר לכך שהמחיר משתחרר: **Dynamic Frequency Breakout (DFB)**, כשהוא ממוקם
בהקשר של התכונות הפנימיות ושל אפקט הפרפר. (מוגדר בשיעור 12.)

**הדוגמה מלמדת תזמון:** תמיכה נבדקת, אחריה שני retests. ה-retest הראשון הוא `fractal candle`
עם `expanding range dynamics` וצל תחתון בולט — מאשש לחץ קנייה. **אבל ה-DFB מגיע רק שני
נרות אחר כך.** עד לרגע ההוא, המחיר היה יכול לשבור את התמיכה כלפי מטה למרות כל סימני
לחץ הקנייה.

> "the candle that breaks the dynamic frequency is **not too dramatic**, which is in
> alignment with the idea of the **butterfly effect**."

**זו נקודה עדינה וחשובה לבוט:** אות הכניסה הוא **לא** הנר הדרמטי. חיפוש נרות גדולים
כטריגר סותר את השיטה.

---

# כוח 4 — Prior Activity

**הגדרה:** האם הנר הנבחן נמצא ב-price vector **עולה** או **יורד**.

> אותו נר ברי: ב-price vector **יורד** → `continuation` או `exhaustion`.
> ב-price vector **עולה** → `correction` או `reversal`.

## ההבחנה מ-Trend Phase ⭐

> "Prior activity is location in a **micro** scale, and trend phase is location in a **macro**
> scale."

בתרשים ון: `Phase` (הגדול) מכיל את `Prior Activity` (הקטן).

**הדוגמה המכריעה:** במגמת עלייה לפי Elliott, גל 1 וגל 5 שניהם price vectors עולים —
**זהים לחלוטין** מנקודת המבט של prior activity. אבל גל 1 בתחילת המגמה וגל 5 בסופה —
**שונים לגמרי** מנקודת המבט של trend phase.

לכן שני הכוחות אינם מיותרים זה לצד זה, וחייבים להיות שני שדות נפרדים במודל.

---

## מפרט קידוד מרוכז

```python
extrinsic = {
  "trend_phase":   {...},          # Dow / Elliott / Wyckoff — מאקרו
  "overextension": {
      "velocity_div":     "reversal_bull|reversal_bear|cont_bull|cont_bear|none",
      "accel_div":        ...,      # RSI(RSI) — מקדים את velocity
      "cvd_pattern":      "buy_exh|sell_exh|buy_abs|sell_abs|none",
      "length":           int,      # ↑ = חזק יותר
      "agrees_with_trend": bool,    # continuation > reversal
      "nested_chain":     int,      # מספר אותות מקוננים = חיזוק
  },
  "barriers": [ {"function":..., "origin":..., "behavior":...,
                 "regime_before": "sustainable|unsustainable|ambiguous",
                 "candle_side":   "below|above|crossing"} ],
  "prior_activity": "upward_vector|downward_vector",   # מיקרו
}
```

## פערים פתוחים

- **`price vector` עדיין לא הוגדר פורמלית**, ועכשיו הוא כבר נושא משקל אמיתי — כוח 4
  מוגדר עליו לגמרי. → שיעור 11.
- **`fractal candle` בשימוש לפני הגדרה** (השיעור אומר "don't worry, we'll dive into it
  later"). → שיעור 15.
- **`Dynamic Frequency Breakout` בשימוש לפני הגדרה.** → שיעור 12.
- הקורס **אינו** מלמד Dow/Elliott/Wyckoff. אם `trend_phase` נדרש לבוט — זה פער חיצוני
  שנצטרך לסגור בעצמנו, וזו עבודה לא קטנה.
- אין ספים מספריים ל: מהו "length" גדול, מהי לינאריות מספקת ל-sustainable, מהו "reacts
  without violating".
