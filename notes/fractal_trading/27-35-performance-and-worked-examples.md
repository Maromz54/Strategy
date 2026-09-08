# fractal_trading 27-35 — הערכת ביצועים ודוגמאות מעשיות

מקור: `L027_Basic_Performance_Appraisal.json`,
`L028_Reversal_Mechanics_of_Price_Action_in_Low_Fractal_Dimension.json`,
`L029_Velocity_Acceleration_Hyper_Integration.json`,
`L030_Fractal_Dimension_Filter_Temptations_of_a_Stochastic_Game.json`,
`L031_Self_Similar_Manipulation_in_Higher_Fractal_Dimension.json`,
`L032_Unsustainable_Price_Feigenforks_Low_Fractal_Dimension.json`,
`L033_When_Low_Fractal_Dimension_Fails_and_what_to_do_about_it.json`,
`L034_Integration_as_an_Ambiguity_Reduction_Mechanism.json`,
`L035_Confronting_Opposing_Trade_Ideas.json`

> משיעור 28 ואילך הקורס עובר ל**דוגמאות מעשיות**. הן אינן מציגות מנגנונים חדשים אלא
> מדגימות את המסגרת — אבל מכילות פרטי הפעלה שלא נאמרו בתיאוריה. אלה מרוכזים כאן.

---

# ⭐⭐ L027 — הערכת ביצועים: איך למדוד את הבוט

## consistent אינו sustainable

> "short-term consistency **doesn't necessarily imply** long-term sustainability, and
> long-term sustainability **doesn't imply the absence of drawdowns**."

בסימולציה בשיעור (3 שנים, 756 ימי מסחר, תנועה בראונית עם דריפט): במבט כולל — יתרון ברור.
במבט על מקטעים קצרים — *"sometimes the trader loses consecutively for **more than 30
days**"*, ולעיתים **חודשים** להתאושש מרצף הפסדים.

> "During periods where the trader rises consistently, he thinks his edge is on point.
> During losing streaks, he thinks he has lost his edge. However, it's clear that he **has**
> an edge in the long term."

## כללי מדידה — ישימים ישירות לבקטסט

| כלל | מקור |
|---|---|
| למדוד ב**תשואות חודשיות** — *"daily returns have **too much noise**"* | הנוהג המקצועי |
| **סיכון = תנודתיות = סטיית תקן של התשואות** | הגדרה פיננסית |
| להשוות שתי עקומות הון לפי **עומק הדרודאון**, לא לפי התשואה | הדוגמה בשיעור |
| לצפות ל**רצפי הפסד של 30+ ימים** גם באסטרטגיה מנצחת | הסימולציה |

## ⭐⭐ אזהרה שחייבת להיאמר במפורש

> "**in the same way you find an edge, you can lose it.** That happens because the market is
> dynamic, and the **probabilities associated with patterns and techniques vary over time**."

> "**You can never PROVE that you are consistently profitable. You can only demonstrate that
> you HAVE BEEN in the past**, and if you do, that doesn't mean it will continue."

> "Extreme market conditions such as **black swan** events render every type of market
> approach useless."

**זו האזהרה שיש להעביר למשתמש כפי שהיא.** בקטסט מוצלח אינו הוכחה — הוא תיעוד של העבר.
זו הרחבה של ה-`unknown probability` מ-L018 וה-Observer Problem מ-vol1 L010.

---

# פרטי הפעלה מהדוגמאות

## ⭐ הממד הפרקטלי — הפער נשאר פתוח, ועכשיו סופית

L030 נקרא `Fractal Dimension Filter`, וסימנתי אותו כמקום הסביר לנוסחה. **אין בו נוסחה.**
המדידה מודגמת **ויזואלית בלבד**: מחברים את השיאים והשפלים של קטע המחיר ומתבוננים אם
הצורה דומה יותר לקו או למשטח.

**המסקנה:** אין בשום מקום בחומר נוסחה לממד. ההגדרה האופרטיבית היחידה נשארת זו
מ-vol1 L006 ומ-FT L011 — **"חספוס = כמה בפתאומיות משתנות התכונות הפנימיות"** — וזו
כן ניתנת לחישוב. **המדד יהיה תוספת שלי**, ואסמן אותו ככזה.

## ⭐ ממד פרקטלי ותנודתיות הם **צירים נפרדים**

> L030: "a situation where fractal dimension is **higher** and volatility is **lower** is
> **preferable** to a situation where fractal dimension is higher [with high volatility]."

> L032: "a **high volatility** movement like this **automatically creates a LOW fractal
> dimension**."

**נפילה חדה ואלימה היא קווית — ולכן ממד נמוך — אבל תנודתיות גבוהה.** אלה שני מדדים
בלתי-תלויים, וצריך את שניהם בנפרד. טעות נפוצה תהיה לזהות ביניהם.

**המצב הרצוי:** ממד נמוך **וגם** תנודתיות נמוכה. ממד נמוך עם תנודתיות גבוהה = הפרפר
כבר עף.

## ⭐ Range dynamics כפילטר ל-fractal candle

> L030: "a bearish fractal candle happening within an **upward progression**... at the same
> time that there is a bearish reversal divergence at the candle highs, there's a bullish
> continuation at the candle lows. **That's how you use range dynamics to filter out bad
> fractal candles.**"

> "the next one is also bearish, but now it's an **expansion**, which **removes the
> contradiction**."

מאשש במלואו את הדירוג שרשמתי בהערה על L015: `expansion > progression`.

## ⭐ הגדרה קודדת ל-Unsustainable

> L032: "for price to go in the same direction for long periods, there must be a **balance
> between how much price advances in the y-axis and the x-axis** of the chart."

```
sustainable    ≈  Δprice / Δtime  יציב
unsustainable  ≈  Δprice / Δtime  גדל  (האצה)
```

> "The acceleration of price gives the impression that price is **gaining power**, but in
> reality, price is **exhausting its power too quickly**."

## ⭐ תמרון בשתי סקאלות בו-זמנית

> L035: המחיר שבר שיא קודם וחזר למטה באלימות = **bull trap** בסקאלה הרחבה.
> ובמקביל, ה-fractal candle שובר את שיא הנר הקודם וסוגר למטה = **bear raid** במיקרו.

זו ההמחשה הישירה של `self-similar manipulation` (L014) — אותה תבנית בשתי רמות.

## ⭐ אינטגרציה כמנגנון להסרת עמימות (L034)

Wyckoff יכול לקרוא את אותו דשדוש **גם** כ-distribution (ירידה) **וגם** כ-reaccumulation
(עלייה). עמימות מובנית.

> "We can **remove the ambiguity by integrating the different types of phase analysis
> methods**... we can eliminate the ambiguity by looking at the **intersection between the
> phase methods**."

**כלל קודד:** כשלשיטה אחת יש שתי קריאות מנוגדות — **החיתוך עם שיטה עצמאית אחרת מכריע**.

## ⭐ חובה לחפש אותות **נגד**

> L031: "it's easy to keep focusing on the signals that **agree** with the trade idea and
> ignore the ones that **go against** it, but **you must try to find signals that go against
> you**."

לבוט זה פשוט: לספור גם את המרכיבים ה**מנוגדים**, ולא רק את התומכים. הניקוד צריך להיות
`תומכים − מנוגדים`, לא `תומכים` בלבד.

## היפוך רעיון העסקה (L033)

בממד פרקטלי **נמוך**, אות סותר **אינו רעש**:

> "Recall that we are in low fractal dimension, so a sign like this **cannot be considered
> noise**."

שתי אפשרויות: להחזיק את הרעיון המקורי ולפתוח גם את הנגדי, או לצאת מהראשון ולהיכנס לשני.

> "you should **not increase risk** when a perfect situation appears, as some traders will
> definitely do."

## Fibonacci — סיווג כן

> L032: "the **161.8 ratio is very common**... this could be a case where the fib ratio would
> work due to the **self-fulfilling prophecy effect**, and **not because of its capacity to
> capture some fundamental aspect** of the market."

למרות המראה המתמטי, פיבונאצ'י מסווג כ**התנהגותי** — ולכן **כן** כפוף לשחיקה. שווה לזכור
מול טקסונומיית הכלים ב-L017.

## שתי טכניקות קווים חדשות (L029)

**היפוך זווית תדירות:** מציירים קו שלוכד תדירויות בזווית של, למשל, ‎−7°, ואז **הופכים
ל-‎+7°** ומעגנים על שפל משמעותי.

> ⚠️ **פרט מימוש קריטי:** *"you have to **lock the price-to-bar ratio** of the chart since
> the angles would change if you zoom in and out."* — כל טכניקה מבוססת-זווית מחייבת
> **סקאלת מחיר/זמן קבועה ומפורשת**. בקוד זה חייב להיות פרמטר, לא משתמע.

**AR Lines (Action-Reaction), על שם Roger Babson** — החוק השלישי של ניוטון על מחיר:
*"As above, so below."* מעגנים על שפל משמעותי, הזווית נקבעת מתדירויות השיאים האחרונים,
משכפלים את הזווית לשיא חשוב ליצירת תעלה, מודדים את המרווח האנכי, ומשכפלים אותו **מתחת**
לקו המקורי.

> "this line is **not obvious to most traders**, so the self-fulfilling prophecy effect is
> **not present** to a significant degree."

## ⭐ אקצלרציה מקדימה — הודגם בפועל (L029)

> "the **velocity RSI is in sync** with price to the upside, but the **acceleration RSI is
> showing a bullish continuation divergence already**."

> "there is **divergence between divergence signals**. Contradictions in divergence signals
> show that **something about price is changing**."

`acceleration → velocity → price` — שרשרת ההקדמה מ-L009 מודגמת על צ'ארט אמיתי.

## אזהרה מפני נבירה בעבר (L028)

> "It's a **mistake to keep going to the past of price until you find some barrier** that
> might interact with the current price. The problem is that you will increase the amount of
> information to an **overwhelming** degree."

עקבי עם חלון ה-250/100-200 נרות מ-vol1.
