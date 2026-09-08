# vol1 שיעורים 31-40 — תורת הקווים

מקור: `L031_Line_Theory.json`, `L032_Anchoring.json`, `L033_Extension.json`,
`L034_Validation.json`, `L035_Simple_Line_Extrapolation_and_NonEquidistant_Line_Extrapolation.json`,
`L036_Newtonian_Action_Space_Extrapolation_and_Fibonacci_Action_Space_Extrapolation.json`,
`L037_Vector_Space_Extrapolation.json`, `L038_Single_and_Double_Negative_Vector_Extrapolation.json`,
`L039_Vector_Decomposition.json`, `L040_Vector_Addition.json`

> **שכבת הכלים.** אם 18 היסודות הפרקסאולוגיים הם אוצר המילים, תורת הקווים היא הדרך
> לגזור מהם **רמות עתידיות**. הכול כאן גיאומטריה אנליטית טהורה — קודד לחלוטין.

## L031 — תשעת העקרונות

```
Anchoring · Extension · Validation · Extrapolation · Frequency Shifting/Tuning
Convergence · Cross Dimensionality · Vectorization · Reverse Engineering
```

נשען על שישה תחומים: גיאומטריה אוקלידית, אנליטית ופרקטלית; מרחבים וקטוריים מופשטים
(אלגברה); frequency (סטטיסטיקה); מכניקה ניוטונית.

---

## ⭐ L032 — Anchoring: כאן נמצא הקצה

| סוג | על מה מעוגן | מי רואה |
|---|---|---|
| **Real** | קצוות שוק **מובנים מאליהם** — *"you don't need to do any sort of calculation"* | כולם |
| **Abstract** | **תדירויות** או **מרחבים וקטוריים מופשטים** | *"**most people in the market don't see them**"* |

**זה מתחבר ישירות ל-Observer Problem (L010).** עיגון ריאלי גלוי לכולם — ולכן, לפי אותו
היגיון, שחוק. **העיגון המופשט הוא בדיוק המקום שבו הקצה עדיין קיים.**

לבוט זו נקודה מעשית מאוד: קווים שמעוגנים על תדירויות (שדורשות חישוב) עדיפים על קווים
שמעוגנים על שיאים ושפלים גלויים.

## L033 — Extension

חיבור שתי נקודות עיגון או יותר, והארכה קדימה ⟹ מחסום מחיר סביר.
**כל צירוף מותר:** real-real, real-abstract, abstract-abstract.

## ⭐ L034 — Validation: מדד איכות לקו

> "if a line has been **performing well in the recent past**, it tends to perform well in the
> near future. We do that by **analyzing past frequencies interacting with the line**."

**זה מדד כמותי ישיר וקודד:**

```python
def line_quality(line, history):
    """כמה תדירויות עבר נגעו בקו מבלי להפר אותו."""
    return count(freq for freq in past_frequencies if touches(line, freq))
```

וזה פותר בעיה מעשית: אחרי שמייצרים **הרבה** קווים אפשריים (ראה למטה), צריך דירוג —
וזה הדירוג.

---

# עקרון האקסטרפולציה — שלוש תת-משפחות

## 1. Line Extrapolation (L035)

העתקת קו לעוגן אחר **תוך שמירה על אותה זווית בדיוק**.

| סוג | איך |
|---|---|
| **Simple** | מחברים שני קצוות לקבלת זווית → מעתיקים את הקו לקצה ה**נגדי שנמצא ביניהם**. (למשל: שני שפלים ⟹ העתקה לשיא שבאמצע) |
| **Non-Equidistant** | אותה זווית, אך מועתקת ל**מספר** קצוות ⟹ מרווחים לא-שווים בין הקווים |

## 2. Action Space Extrapolation (L036)

**Action space** = המרווח בין שני קווי ה-simple line extrapolation.
אפשר לאקסטרפולט את **המרווח כולו**, לא רק קו:

| סוג | הכלל |
|---|---|
| **Newtonian** | מעתיקים את המרווח למעלה/למטה **באופן שווה-מרחק**, לפי החוק השלישי של ניוטון — *"every action has an equal and opposite reaction"* ⟹ **reaction space** |
| **Fibonacci** | מעתיקים את המרווח לפי **יחס פיבונאצ'י** ⟹ reaction space לא-שווה-מרחק. בדוגמאות: 100% (extension), ו-78.6% / 61.8% (retracement) |

זהו השימוש הראשון בפיבונאצ'י בקורס, והוא **לא** מסורתי: היחס ממקם **מרחב**, לא רמה בודדת.

## 3. Vector Space Extrapolation (L037-L041)

ארבעה סוגים: `negative extrapolation`, `vector decomposition`, `vector addition`,
`circular decomposition`.

### ⭐ Negative Vector Extrapolation (L038)

> "The **negative market theory** claims that the real vectors have a **mirrored image in
> space and time**, and these hidden abstract vectors can unveil interesting anchors and
> angles."

**Single** — לכל וקטור אמיתי יש **שלוש** תמונות ראי:

| מראה | הכלל | התוצאה |
|---|---|---|
| **Spatial** | לשמר את זווית הזמן, **להפוך את זווית המרחב**, לשמר אורך | יורד במרחב, קדימה בזמן |
| **Temporal** | לשמר את זווית המרחב, **להפוך את זווית הזמן** | עולה במרחב, **אחורה בזמן** |
| **Spatio-temporal** | להפוך את **שתיהן** | יורד במרחב, אחורה בזמן |

הקצוות וה-midpoints של שלושת אלה = נקודות עיגון מופשטות חדשות.

**Double** — לוקחים **שני וקטורים סמוכים ומתחלפים** ובונים **מקבילית**: מעתיקים אורך וזווית
של וקטור אחד ומחברים לקצה של הסמוך לו. ניתן לשרשר — מקבילית מווקטורים מופשטים.

### ⭐ Vector Decomposition (L039)

לכל וקטור יש ממד **מרחבי** (y) וממד **זמני** (x). מפרקים:

```
וקטור מרחבי טהור:  משמרים מרחב, מאפסים זמן   →  וקטור אנכי   (כמה המחיר זז, בלי זמן)
וקטור זמני טהור:   משמרים זמן, מאפסים מרחב   →  וקטור אופקי  (כמה זמן ארך, בלי מחיר)
```

הקצוות וה-midpoints שלהם = עוד עוגנים.

### Vector Addition (L040)

מחברים את הווקטורים המפורקים של **שני וקטורים אמיתיים סמוכים ומתחלפים**.

> **כלל קשיח:** *"You can only add **spatial vectors with spatial** vectors, and **temporal
> with temporal**."*

ואז: מחברים את קצה הווקטור המרחבי המחובר לקצה הווקטור הזמני המחובר ⟹ **קו משופע**.

> "it would be **difficult to see this line without knowing** the vector decomposition and
> addition procedures." — שוב, עיגון מופשט = קצה.

---

## ⭐ ההערה החשובה ביותר לגבי קידוד

כל הגיאומטריה הזו **קודדת בקלות** — זו גיאומטריה אנליטית סטנדרטית ברגע שיש וקטורים.
**אבל היא מייצרת מספר עצום של קווים אפשריים.** מכל זוג וקטורים אפשר לגזור:
3 מראות שליליות × קצוות ו-midpoints, וקטורים מפורקים, חיבורים, מקביליות, action spaces
ניוטוניים ופיבונאצ'יים...

**אין בשיעורים האלה כלל שאומר איזה קו לצייר.** וזה מסוכן: מספיק קווים על צ'ארט ותמיד
יימצא אחד שמסביר כל תנועה. זו בדיוק ההיוריסטיקה שמפניה מזהיר L009.

**שני מנגנוני ההגנה שהקורס כן נותן:**
1. **Validation (L034)** — דירוג קו לפי כמה תדירויות עבר כיבדו אותו
2. **Convergence (L043)** — הסיגנל אינו הקו הבודד אלא **המקום שבו רבים נפגשים**

ולכן הגישה הנכונה לבוט: **לייצר את כל הקווים באופן ממצה, לדרג לפי validation, ולחפש
התכנסות** — במקום לנסות "לבחור" קו. זה גם מנטרל את הסכנה, כי קו בודד לעולם אינו אות.

## פערים

- כמה נרות/תדירויות נדרשים כדי ש-validation ייחשב מספק?
- אילו יחסי פיבונאצ'י בדיוק? הדוגמאות: 100%, 78.6%, 61.8% — לא נאמר אם זו רשימה סגורה.
- "overthrow and underthrow lines" מוזכרים ב-L038 כמחזקים — ה-underthrow לא הוגדר בנפרד.
