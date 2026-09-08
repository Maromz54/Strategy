# vol1 שיעורים 13-18 — קצוות, תדירויות ואזורי היצע/ביקוש

מקור: `L013_Extremes.json`, `L014_Midpoints.json`, `L015_Frequencies.json`,
`L016_Inward_Frequency.json`, `L017_Outward_Frequency.json`,
`L018_Precise_Supply_and_Demand_Zones.json`

> ⭐ **הבלוק הזה סוגר את מנגנון אזורי ההיצע/ביקוש במלואו** ומחדד את הגדרת קו התדירות
> הרבה מעבר למה שהופיע ב-`fractal_trading` L012.

---

## L013 — Extremes

> "Extremes are points in the chart where the **supply and demand balance got extremely
> tilted** to one side of the spectrum, and therefore, price **had no alternative but to
> reverse** direction."

ההגדרה **פרקסאולוגית, לא גיאומטרית**. זה מסביר *למה* קצה הוא קצה, אבל **עדיין לא נותן
כלל מכני** לזיהוי "recognizable high" בסדרת OHLC.

> ⚠️ הפער שסימנתי נשאר פתוח, ועכשיו ברור שהוא לא ייסגר בשיעור הזה. אצטרך כלל משלי
> (fractal pivot בחלון n, או swing לפי סף אחוזי), ולסמן אותו כתוספת שלי ולא כחלק מהשיטה.

## L014 — Midpoints

> "Midpoints are the **exact middle** between two extremes, and they represent the
> **equilibrium** between supply and demand."

ההיגיון: קצה = חוסר איזון קיצוני. אמצע = איזון. ולכן:

> "There's **no such thing** as a price vector that starts at a supply and demand
> disequilibrium and then reverses at equilibrium. **Price only reverses at extremely
> unbalanced points.**"

זו טענה חזקה עם השלכה מעשית: **אין היפוכים ב-midpoint**. אם המחיר "מתהפך" באמצע ווקטור —
או שהזיהוי של הווקטור שגוי, או שזה לא היפוך.

---

## L015 — Frequencies ⭐ ההגדרה המדויקת

> "In statistics, frequency is **how many times a data point occurs**. In price, a frequency
> line shows a **common path between a given number of wicks**."

### שני כללי הבנייה

```
1. הקו חייב לגעת במקסימום wicks
2. הקו לא יכול להפר גוף נר — "It can only occur at the wicks"
```

### ⭐ כלל ההכרעה שחסר לי קודם

האזור שבו לכל ה-wicks יש מסלול משותף הוא **טווח**, ובתוכו יש **אינסוף קווים אפשריים**.
לכן חייבים לבחור אחד:

```
בשיא:  קו התדירות = הגבול ה**עליון**  של הטווח   (ה"outward" ביותר)
בשפל:  קו התדירות = הגבול ה**תחתון**  של הטווח   (ה"outward" ביותר)
```

**הנימוק:** *"the outward frequency shows the most extreme frequency line, which is better
for **both entries and exits in terms of precision**."*

> זה בדיוק מה שהיה חסר ב-`fractal_trading` L012, שם נאמר רק "הקו שלוכד הכי הרבה צללים
> בלי להפר גופים" — בלי לומר איזה קו לבחור מתוך הטווח.

### קווים משופעים

עובדים **בדיוק אותו דבר**. בדוגמה: התדירות ה-outward בין שני שפלים **חוזה** את השפל השלישי.

### ⭐ Overthrow — טיפול בספייקים

> "Frequencies can also have an **overthrow**, which is simply a **range determined by a price
> spike**."

התרחיש: המחיר **מכבד** את קו התדירות (סוגר מעליו) אבל יוצר **ספייק** מתחתיו.

```
לוקחים את קו התדירות המקורי
מזיזים אותו — באותה זווית בדיוק — עד לקצה הספייק
מקבלים קו "overthrow" מקביל
```

בדוגמה מהשיעור, קו ה-overthrow **תופס במדויק** את השפל השלישי. כלומר: ספייק אינו רעש
שיש להתעלם ממנו — הוא מייצר **קו מקביל תקף**.

**זו תשובה חלקית לשאלת ה-epsilon** שהעליתי ב-`fractal_trading` L012: במקום להחליט כמה
חדירה "נסלחת", מחזיקים **שני קווים** — המקורי וה-overthrow — ומתייחסים אליהם כאל טווח.

---

## L016-L017 — Inward ו-Outward Frequency ⭐

מוגדרים על **נקודת הפיתול בין שני וקטורים** (inflection point).

| | היכן | הגדרה |
|---|---|---|
| **Inward** | על ה**פנים** שבין שני הווקטורים | בשיא (עולה→יורד): התדירות ה**גבוהה ביותר** שנמצאת בפנים — כלומר על ה-wicks ה**תחתונים** של נרות השיא |
| | | בשפל (יורד→עולה): התדירות ה**נמוכה ביותר** בפנים — על ה-wicks ה**עליונים** של נרות השפל |
| **Outward** | על ה**חוץ** | בשיא: על ה-wicks ה**עליונים** ביותר |
| | | בשפל: על ה-wicks ה**תחתונים** ביותר |

**המשמעות:**
- `inward` = *"the **inside line** of buyers or sellers of a solid structure"*
- `outward` = *"the **outer line** of sellers"* (בדוגמת השיא)

**ולמה צריך את שניהם:** בדוגמה אחת המחיר נגע ב-inward והתהפך ממנו. באחרת הוא נגע ב-inward
אך **נכשל להגיע ל-outward**. כלומר הם **שתי רמות שונות** ולא כפילות.

---

## L018 — Precise Supply and Demand Zones ⭐⭐

> "The supply and demand zone is determined by the **inward and outward frequencies** found on
> the **inflection point between two price vectors**."

```
אזור היצע (בשיא):   גבול עליון = outward   |   גבול תחתון = inward
אזור ביקוש (בשפל):  גבול עליון = inward    |   גבול תחתון = outward
```

האזור **מוקרן קדימה** ומייצר תחזית מדויקת מאוד לאזור היפוך.

> "Some people believe that supply and demand zones is a **loose** concept, and it is **if you
> don't know** about inward and outward frequencies. However, when you do know... you can
> draw **precise** supply and demand zones... that takes some of the **guesswork** out."

**באיזה מהשניים המחיר יתהפך?** לא נקבע מראש — *"you need other elements in the analysis,
like more complex line work"*. כלומר האזור הוא הפלט; ההכרעה בתוכו דורשת שכבה נוספת.

### ⭐ סגירת מעגל עם L006

בשיעור 6 נאמר שה-`near-extremes` הם *"a **range between the inward and outward frequencies**
that happened near the extremes"*, ושם *"supply and demand zones live"*.

**עכשיו זה מתחבר לגמרי:**

```
near-extreme  ≡  אזור היצע/ביקוש  ≡  הרצועה [inward, outward]
```

וזה גם מסביר את האמירה מ-L006 שהמחיר **לא מאיץ בקצה עצמו אלא ב-near-extreme** — ההאצה
מתחילה כשנכנסים לרצועה הזו, לא בנקודת הקיצון.

---

## מפרט קידוד

```python
def frequency_line(candles, side):
    """side='high' → הגבול העליון של טווח המסלול המשותף; 'low' → התחתון."""
    # 1. אזור מותר: לא חוצה אף גוף
    #    בשיא:  [max(body_top), min(high)]
    #    בשפל:  [max(low),      min(body_bottom)]
    # 2. בוחרים את הקצה ה-outward של האזור

def supply_demand_zone(v1, v2):
    """על נקודת הפיתול בין שני וקטורים."""
    if inflection == "peak":                    # עולה → יורד
        return (outward_high_wicks, inward_low_wicks)      # (עליון, תחתון)
    else:                                       # יורד → עולה
        return (inward_high_wicks, outward_low_wicks)

def overthrow(freq_line, spike_extreme):
    """הזזה מקבילה — אותה זווית — עד קצה הספייק."""
    return shift_parallel(freq_line, to=spike_extreme)
```

## מה נסגר ומה נשאר

### ✅ נסגר
- **בחירת קו התדירות מתוך הטווח** — תמיד ה-outward
- **אזור היצע/ביקוש מדויק** — [inward, outward] בנקודת הפיתול
- **`near-extreme` = אזור היצע/ביקוש** — סגירת מעגל עם L006
- **טיפול בספייקים** — קו overthrow מקביל, לא התעלמות

### ⚠️ נשאר
- **זיהוי מכני של קצה** — מוגדר פרקסאולוגית בלבד. **זה הפער הבסיסי ביותר שנותר**, כי
  וקטורים, זרימות, תדירויות ואזורים — כולם נבנים עליו.
- ההכרעה בין inward ל-outward בתוך האזור — נדחית ל"line work" מתקדם (L031+)
- כמה wicks נדרשים למינימום קו תדירות? "a given number" — לא נקבע
