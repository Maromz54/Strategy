# שיעור 06 — How to Interpret a Candlestick in Isolation

מקור: `transcripts/L006_How_to_Interpret_a_Candlestick_in_Isolation.json` · global 80

## הרעיון

לא לשנן תבניות — **לנתח את שש התכונות זו בהקשר של זו**. הטענה: יש יותר מדי וריאציות
אפשריות של מה שמחיר יכול לעשות מכדי ששינון יעבוד.

> "The ultimate skill of a price action trader is the understanding of how to analyze any
> candle in a logical way without memorizing patterns."

## טבלת המיפוי (מהמסך, 01:28)

זו הטבלה שממפה כל תכונה לשאלה שהיא עונה עליה:

| תכונה | מה היא נותנת |
|---|---|
| `Bias / Sentiment` | **Qualification** — איזה צד |
| `Body Size` | **Quantification** — כמה |
| `Range` | **Volatility** |
| `Shadows` | **Pressure** |
| `Body%` | **Uncertainty** |
| `Shadow Symmetry / Body Position` | **Balance** |

## חוק חדש ומרכזי — עוצמה בינונית = קיימוּת

> "this is a candle that indicates buyers have a **medium** level of power, which is
> characteristic of **sustainable** price action. Candles with too little or too much power
> tend to lead to **ambiguous** or **unsustainable** price action respectively."

```
עוצמה נמוכה מדי  →  price action  ambiguous     (מעורפל)
עוצמה בינונית    →  price action  sustainable   (בר-קיימא)  ← הרצוי
עוצמה גבוהה מדי  →  price action  unsustainable (לא בר-קיימא)
```

**זה חוק לא-מונוטוני, וזו נקודה קריטית לבוט.** האינטואיציה הנאיבית היא "נר חזק יותר =
אות חזק יותר", וכאן נאמר במפורש שזה שגוי בקצה העליון. פונקציית הניקוד חייבת להיות
**קמורה כלפי מטה** — מקסימום באמצע, לא מונוטונית עולה.

## כלל שקלול — מתי תכונה מאבדת ממשקלה

> "Since the body percentage is **very high** in this case, the balance between buying and
> selling pressure given by the symmetry of shadows becomes **less important**."

כלומר: כש-`body%` גבוה מאוד, המשקל של `shadow symmetry` **יורד**. התכונות אינן שוות משקל
תמיד — המשקל של אחת תלוי בערך של אחרת.

## הסכמה מול התנגשות בין תכונות

זו ההבחנה המרכזית בארבע הדוגמאות של השיעור:

**דוגמה 2 — התנגשות.** נר ברי עם גוף קטן, צל תחתון ארוך מאוד, טווח רחב.
- ה-`bias` מהגוף אומר: **המוכרים ניצחו**
- ה-`shadow symmetry` אומר: **הקונים דומיננטיים** (לחץ קנייה עצום בצל התחתון)
- → "an uncertain candle with **two colliding notions of bias**"

**דוגמה 3 — הסכמה.** נר ברי, גוף בינוני, צל עליון בינוני, **אין צל תחתון**, גוף נמוך בטווח.
- ה-`bias` מהגוף וה-`body position` **מסכימים** — שניהם ברי
- **היעדר צל = היעדר לחץ מאותו כיוון.** פרט שמחזק את הפרשנות.

## תלות הקשר של אי-הוודאות בטווח

> "uncertainty in a **low-range** candle simply means **indecision**. Uncertainty in a
> **wide-range** candle means indecision **with a touch of high risk**, which is a more
> challenging situation."

אותו `body%` נמוך אומר דברים שונים לפי `range_class`. עוד דוגמה לכך שהתכונות אינן
אורתוגונליות.

## חוקים ניתנים לקידוד

```python
# 1. עוצמה — פונקציה לא-מונוטונית
def power_regime(body_pct, range_class):
    """low → ambiguous, medium → sustainable, high → unsustainable"""

# 2. משקל דינמי
weight_of_balance = f(body_pct)     # יורד ככל ש-body% עולה

# 3. דגל התנגשות
bias_from_body     = sign(close - open)
bias_from_position = sign(shadow_asym)        # ראה שיעור 4
conflict = bias_from_body != bias_from_position and both != 0

# 4. אי-ודאות בהקשר
uncertainty_flavor = "indecision"            if range_class == "narrow" else \
                     "indecision + high risk" if range_class in ("wide","outlier") else \
                     "indecision (neutral)"
```

**דגל ה-`conflict` הוא כנראה הפלט השימושי ביותר מהשיעור הזה.** הוא מסמן בדיוק את
הרגעים ש"משהו משתנה בצורה לא-מובנת מאליה" — הרגעים שהשיעור הבא מרחיב עליהם.

## פערים פתוחים

- **מהי "עוצמה" מספרית?** החוק low/medium/high power מנוסח איכותית. האם "power" =
  body_size? body% ? שילוב? לא נאמר. → פער מרכזי, לחפש בהמשך.
- הכלל "משקל ה-balance יורד כש-body% גבוה" — בלי פונקציה או סף.
