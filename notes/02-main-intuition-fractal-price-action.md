# שיעור 02 — Main Intuition for Fractal Price Action

מקור: `transcripts/L002_Main_Intuition_for_Fractal_Price_Action.json` · global 76

## תקציר

הרעיון המרכזי של כל השיטה, ומכאן הכול נגזר.

## מונחים

| מונח | הגדרה |
|---|---|
| `fractal` | תבנית **self-similar** — תבנית שחוזרת על עצמה בתוך עצמה ומחוץ לעצמה על פני סקאלות מרובות |
| `broad extreme` | שיא/שפל רחב, כזה שמופרד משכניו ב**הרבה** נרות. נראה כשמסתכלים על הצ'ארט מרחוק |
| `adjacent extreme` | שיא/שפל שנוצר משני נרות **סמוכים**. נראה כשמסתכלים "עם זכוכית מגדלת" |

הבסיס התיאורטי מגיע מתורת הכאוס: `fractals`, `butterfly effect`,
`attractors & repellers`, `statistical stability`.

## החוק המרכזי — שקילות סקאלות

> "the adjacent extremes in the candlestick level in a **higher** timeframe are the broader
> market extremes in a **lower** timeframe."

**כיוון החוק קריטי ולא אינטואיטיבי.** המבחן בודק אותו במפורש (שיעור 2, שאלה 3), והניסוח
ההפוך — "adjacent על TF נמוך = broad על TF גבוה" — מסומן כ**שגוי**.

```
adjacent extreme  @ timeframe גבוה   ≡   broad extreme  @ timeframe נמוך
```

הדגמה מהשיעור: בצ'ארט שעה מסומנים שני שיאים בנרות סמוכים (`adjacent`). מעבר ל-10 דקות —
אותם שני שיאים בדיוק הופכים לשיאי סווינג רחבים (`broad`).

## המסקנה המעשית

מכיוון שהמבנה זהה בכל הסקאלות, אפשר **לראות מספר טווחי זמן בתוך צ'ארט אחד**:

> "Instead of switching timeframes, we switch our perception."

הנימוק: מעבר בין טווחי זמן יוצר בלבול ושיתוק אנליטי (`analysis paralysis`). שינוי תפיסה
נותן את אותו רווח בלי החיסרון.

## חוקים ניתנים לקידוד

1. **סיווג אקסטרם לפי מרחק בנרות** — ההבחנה בין `broad` ל-`adjacent` היא מספר הנרות
   שמפרידים בין האקסטרם לשכניו. `adjacent` = שני נרות סמוכים; `broad` = הרבה נרות.
   (המבחן, שיעור 2 שאלה 2, מאשר במפורש: "Broad price extremes are separated by many
   candlesticks while adjacent price extremes are not.")

2. **ניתוח רב-סקאלתי מסדרה אחת** — זו נקודה חזקה לבוט: אין צורך למשוך OHLC של כמה
   טווחי זמן. מבנה הסקאלות הנמוכות יותר נגזר מהמבנה המקומי של סדרה בודדת. חוסך גם
   סנכרון נתונים וגם באגים של יישור זמנים.

## פערים פתוחים

- **מה היחס המספרי בין הסקאלות?** בדוגמה 1H ↔ 10min, כלומר 6:1. לא נאמר אם זה כלל,
  המלצה, או סתם דוגמה. לקידוד `adjacent ≡ broad` צריך להגדיר את היחס.
- **כמה זה "many candlesticks"?** הסף בין `broad` ל-`adjacent` מוגדר מילולית בלבד.
  צריך מספר. → לבדוק בשיעורים 11-12 (`Fractal Price Action Properties`, `Frequencies`).
