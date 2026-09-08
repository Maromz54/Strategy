# fractal_trading 16-18 — LRC, טקסונומיית כלים, ותורת המשחקים

מקור: `L016_Linear_Regression_Channels.json`, `L017_Tool_Types_Chaos_Theory.json`,
`L018_Integration_Basic_Game_Theory.json`

> ⭐⭐ **L017 עונה על החשש שהעליתי בעצמי** לגבי ה-Observer Problem — האם הקצה נשחק
> כשהשיטה מתפרסמת. התשובה מפתיעה לטובה.

---

## L016 — Linear Regression Channel

**מה הוא תופס:** את ה**יציבות הסטטיסטית** של תנועה כאוטית. מערכות כאוטיות = תנועה
א-מחזורית אך **התפלגות יציבה**.

```
Pitchfork  →  הפרשנות ה**פיזיקלית** של תנועת המחיר
LRC        →  הפרשנות ה**מתמטית**
```

**המטרה:** להעריך אם המחיר **מתוח יתר על המידה מבחינה סטטיסטית**.

**סיווג לפי שיעור 10:** `containment` בקווים החיצוניים, `traditional` בקו המרכזי,
`fractal` ו-`sloped` (לעיתים נדירות אופקי).

### ⭐ למה LRC עדיף על Bollinger Bands

> "In an indicator like Bollinger Bands, the window of price calculation is often **grounded
> in places that make no sense**. This problem is **solved in the LRC** because we can ground
> the channel in **places that do make sense**."

זה בדיוק ההבדל בין `numerical` ל-`fractal` barrier משיעור 10: חלון מתגלגל מול עיגון
גיאומטרי. **ובנוסף** — קווי ה-LRC ישרים, מה שמאפשר לראות קווי תדירות בזוויות לא-מובנות
מאליהן (ל-BB יש קווים דינמיים מעוקלים).

### כללי שרטוט

| | |
|---|---|
| **עוגן שמאלי** | קצה מחיר **בולט**, רצוי כזה שמסתדר עם ההקשר הכללי |
| **עוגן ימני** | קצה **פוטנציאלי חדש** שזה עתה נוצר |
| **מתי לצייר** | כשיש **DFB**, fractal candle שמגיב למחסום, תבנית תמרון — כלומר **רק בהקשר** |
| **סטיות תקן** | ברירת מחדל 2; לעיתים 3 נותן תובנה נוספת |

> "**Drawing LRCs in every candle is pointless**, in the same way that drawing pitchforks in
> every price movement is pointless. These tools **must be bounded by context**."

זה בדיוק העיקרון של `reverse engineering` (vol1 L047) — הכלי מאשר, לא מגלה.

**single-vector מול multi-vector:** משנים רק את מיקום העיגון השמאלי.
**שימוש פרקטלי:** משלבים **לפחות שני LRC בגדלים שונים** — הקטן מאשש את הגדול.

### ⭐ והנקודה החשובה

> "these tools are **not widely used**, and they provide **non-obvious angles and lines**. So
> the **self-fulfilling prophecy effect here is very small or nonexistent**."

---

# ⭐⭐ L017 — טקסונומיית הכלים והנבואה המגשימה את עצמה

| סוג | דוגמאות | נבואה מגשימה? |
|---|---|---|
| **Behavioral** | תבניות צ'ארט, קווי תמיכה/התנגדות | ✅ **כן** |
| **Economic** | אינדיקטורים כלכליים, margin debt, money market funds | ✅ **כן** |
| **Mathematical** | **Linear Regression Channel** — גיאומטריה פרקטלית, דינמיקה לא-ליניארית, סטטיסטיקה | ❌ **לא** |
| **Physical** | **Andrews Pitchfork**, קווי action-reaction | ❌ **לא** |
| **Hybrid** | **אזורי היצע/ביקוש** (כלכלי+התנהגותי) · **fractal candles ו-frequency lines** (מתמטי+התנהגותי) | קטן, *"usually not strong enough"* |

## ⭐⭐ ההשלכה — וזו תשובה לחשש שלי

בהערה על vol1 L010 כתבתי שה-Observer Problem מנבא **דעיכת ביצועים** ככל שהשיטה מתפרסמת,
והמלצתי לבדוק את זה בבקטסט. **השיעור הזה מחדד את התמונה:**

הכלים המרכזיים של השיטה — `frequency lines`, `fractal candles`, `LRC`, `pitchforks` —
הם **מתמטיים, פיזיקליים והיברידיים**, ולכן **אינם כפופים לנבואה מגשימה** (או כפופים לה
במידה זניחה). כלומר הם **לא אמורים להישחק** מפרסום.

**מה שכן נשחק** הוא הרובד ההתנהגותי: תמיכה/התנגדות קלאסיות ותבניות צ'ארט — ואלה בדיוק
מה שהשיטה **פוסלת** ממילא.

> **הסתייגות שלי:** זו טענה תיאורטית, לא מדידה. גם אם הכלי לא נשען על אמונה קולקטיבית,
> **התנהגות המרקט מייקרס עשויה להשתנות** אם מספיק סוחרים משתמשים בכלים האלה. הבדיקה
> בבקטסט לאורך זמן נשארת רלוונטית — אבל עכשיו יש **היפותזה מנוגדת** לבדוק מולה, וזה טוב.

## כאוס מסדר ראשון מול שני

```
מסדר ראשון:  המערכת **אינה** מגיבה לתחזיות על עצמה   —  מזג אוויר
מסדר שני:    המערכת **כן** מגיבה                      —  שווקים, פוליטיקה
```

נבואה מגשימה אפשרית **רק** במערכות מסדר שני. וזו הסיבה שהיא קיימת בשווקים בכלל.

**דוגמה קיצונית מהשיעור:** אם מספיק אנשים יאמינו ש"השוק יעלה אם יורד גשם ביום רביעי" —
הוא **יעלה**, כי הם יקנו. אבל אז *"traders will start **preempting one another**, and that
will render this pattern **useless**."* — כלומר גם דפוסים חסרי היגיון עובדים זמנית,
ואז מתים.

## שני סוגי נבואה מגשימה

| | לולאה | דינמיקה | אנלוגיה |
|---|---|---|---|
| **Self-correcting** | משוב שלילי | **יציבה** — חוזרת למקומה | כדור בתוך קערה = **attractor** |
| **Self-reinforcing** | משוב חיובי | **לא יציבה** — נדנוד קטן מאיץ | כדור על קערה הפוכה = **repeller** |

> "a **small nudge produces an increasingly large effect**, alluding to the **butterfly
> effect**."

**כאן מתחבר אפקט הפרפר לתורת המשחקים:** מה שאנחנו מחפשים הוא **repeller** — מצב לא יציב
שבו נדנוד קטן (DFB עדין) מוליד תנועה גדולה.

---

# ⭐⭐ L018 — Integration ותורת המשחקים

## הגדרת המשחק

> "trading is a **stochastic game of incomplete and asymmetric information, unknown and
> variable probabilities**."

| מאפיין | מה זה אומר |
|---|---|
| **Stochastic** | התוצאה = מיומנות **וגם** מזל |
| **Incomplete information** | אף אחד לא יודע את כל המשתנים |
| **Asymmetric information** | לשחקנים שונים גישה ויכולת שונות |
| **Unknown probability** | ⚠️ *"there is **no way to measure the quantitative probability of a pattern in the future**, only in the past"* |
| **Variable probability** | ההסתברות **משתנה לאורך זמן** לפי תרחיש השוק |

## ⚠️⚠️ אזהרה ישירה לגבי בקטסט

שתי התכונות האחרונות הן אזהרה מפורשת נגד אמון עיוור בבקטסט:

> "you **cannot fully trust the feedback you get from the system to learn**, unlike in games
> of pure skill where the feedback is the main learning tool. **If you ignore the role of
> chance, you'll end up reinforcing the wrong types of behaviors without noticing it.**"

**זו האזהרה החשובה ביותר בקורס עבור הפרויקט הזה.** בקטסט הוא בדיוק "משוב מהמערכת".
המסקנות המעשיות:
1. **הסתברות היסטורית אינה הסתברות עתידית** — במפורש.
2. אופטימיזציה על תוצאות עבר = *"reinforcing the wrong behaviors"* = overfit.
3. לכן: מעט פרמטרים, walk-forward, ובחינת **יציבות** על פני תקופות — לא מקסום תשואה.

## שלוש רמות אינטגרציה

| רמה | הגדרה |
|---|---|
| **Vertical** | כלים מ**שיטה אחת** (למשל רק טכניקות נפח) |
| **Horizontal** | טכניקה אחת מ**לפחות שתי** שיטות שונות |
| **Hyper** | כמה שיותר טכניקות מכמה שיותר שיטות |

> "The **higher the integration, the more reliable** a trade tends to be. However, the higher
> the integration, the **lower the frequency** of trades."

**אותו trade-off בדיוק** כמו ב-Integrated Fractal Candle וב-Hybrid Bar. שלוש הופעות של
אותו עיקרון, וההנמקה שלו נמצאת ב-vol1 L009 (הגברת הסתברות הפרמיסות).

## מגבלות האינטגרציה — כנות שכדאי לרשום

> "integration can increase the odds, but it **cannot guarantee** that a trade will be
> successful."

> "A **hyper-integrated trade cannot overcome** the power of market players acting for a
> strong **macroeconomic force**."

> "integrated price action trading **works better when the markets are relatively stable**."

**לבוט:** צריך מנגנון שמכבה או מקטין חשיפה באירועים מאקרו-כלכליים. אין תועלת באות
מושלם ביום של הכרזת ריבית.

## היכן המיומנות נמצאת באמת

> "in games of incomplete and asymmetric information, [the critical aspect] dwells in
> **information**... This information is **not exactly included in price nor in the trader**.
> It's contained in **the means of observation** that the trader uses to observe price."

זו טענה מעניינת: היתרון אינו בנתונים ואינו בכישרון — הוא ב**כלי התצפית**. וזה בדיוק מה
שאנחנו בונים.
