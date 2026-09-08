# שיעור 11 — Fractal Price Action Properties

מקור: `transcripts/L011_Fractal_Price_Action_Properties.json` · global 85

> **זה השיעור החשוב ביותר עד כה.** כאן מופיע לראשונה **קריטריון הבחירה** של האסטרטגיה —
> מה הופך פיסת מחיר לראויה למסחר. עד עכשיו למדנו לתאר; כאן לומדים **לבחור**.

---

## הרעיון המרכזי — Fractal Dimension

המחיר הוא מבנה פרקטלי, ולכן יש לו **ממד עצמי (self-similarity dimension)** שנע בין 1 ל-2:

```
ממד → 1    המחיר קרוב ל**קו**
ממד → 2    המחיר קרוב ל**משטח**
```

> "price action is always **more than a line and less than a surface**."

### החוק המרכזי ⭐⭐

> "price movements with a **lower fractal dimension are more predictable**."

**זה הקריטריון.** כל השאר בקורס משרת אותו. הבוט לא אמור לחפש "אות" — הוא אמור לחפש
**אזורים בעלי ממד פרקטלי נמוך**, ורק שם לחפש כניסה.

---

## Coastline Paradox — למה הממד גם אובייקטיבי וגם סובייקטיבי

אורך של קו חוף אינו מוגדר היטב, כי הוא תלוי בגודל הסרגל שמודד אותו:

| סרגל | אורך חוף בריטניה |
|---|---|
| 100 ק"מ | 2,800 ק"מ |
| 50 ק"מ | 3,400 ק"מ |
| 100 מ' | 17,820 ק"מ |

ככל שהסרגל קטן יותר, כך הגרנולריות גדולה יותר והאורך הנמדד **גדל**.

**הדגמה על מחיר** (מהשיעור): תנועת מחיר אחת נמדדת כ-1,402 פיקסלים כקו יחיד, אך 2,375
פיקסלים כשמסכמים את התנועות הקטנות שבתוכה. הגדלת גרנולריות תגדיל עוד.

> "Once you choose a ruler size, you can reach an **objective** measurement, but the choice
> of the ruler size is **subjective**, and there is an **infinite set of valid ruler sizes**."

**המשמעות לבוט — קריטית:** אין "הממד הפרקטלי" של המחיר. יש ממד **ביחס לסרגל שבחרנו**.
כלומר קנה המידה של המדידה הוא **פרמטר מפורש** של המערכת, לא קבוע טבע. כל מימוש חייב
לחשוף אותו כפרמטר, ובקטסט חייב לבדוק רגישות אליו.

---

## Roughness — הגשר בין הממד לתכונות הפנימיות ⭐

זו החוליה שמחברת את כל מה שלמדנו קודם אל הממד הפרקטלי:

| | הגדרה | ממד פרקטלי |
|---|---|---|
| **Rough** | התכונות הפנימיות מתפתחות **בפתאומיות** (abruptly) | **גבוה** |
| **Smooth** | התכונות הפנימיות מתפתחות **בהדרגה** (gradually) | **נמוך** |

**זה קודד ישירות!** "roughness" = מדד לתנודתיות של הדלתאות של התכונות הפנימיות. כלומר:

```python
# חלקות ≈ יציבות של השינויים בתכונות הפנימיות לאורך הווקטור
roughness = aggregate(volatility_of(Δbias, Δbody_size, Δrange,
                                    Δbody_pct, Δshadow_asym))
```

ההגדרה **fuzzy במפורש** — ספקטרום, לא בינארי:

```
Extremely Smooth — Very Smooth — Slightly Smooth — Slightly Rough — Very Rough — Extremely Rough
                   └──────────────────────────┘
                     Optimal Price Action to Trade   ← החץ הירוק בשקף
```

> ⚠️ **סתירה קלה בין המקורות שכדאי לשים לב אליה:** התמלול אומר שהאופטימום הוא "the
> **greatest** degree of smoothness", כלומר הקצה. אבל השקף (05:17) ממקם את החץ הירוק על
> **Very Smooth / Slightly Smooth** — ולא על `Extremely Smooth`. השקף עקבי עם החוק
> הלא-מונוטוני משיעור 6 (יותר מדי כוח = unsustainable). **אני נוטה לשקף**, ומסמן את זה
> כפער לאימות מול שיעורים 30/32 שעוסקים ישירות ב-fractal dimension.

---

## ממד פרקטלי וטווח זמן — כלל בחירת TF ⭐

> "**Rough** price vectors in one timeframe are **smooth** price vectors in a **higher**
> timeframe. Notice that you can **find the optimal timeframe to trade** based on the
> fractal dimension and roughness of a price vector."

זהו חוק שיעור 2 שוב, בגלגול שלישי — וכאן הוא הופך ל**מנגנון בחירת טווח זמן**:

```
אם הווקטור מחוספס מדי בטווח הזמן הנוכחי
    →  עלה טווח זמן עד שהוא נעשה חלק
    →  שם נמצא ה-TF האופטימלי למסחר בתנועה הזו
```

**זה שימושי מאוד לבוט** — במקום TF קבוע מראש, ה-TF נבחר **דינמית** לפי חספוס התנועה.

---

## Fractal Flows — וכאן מגיע חוק כניסה אמיתי ⭐⭐

בכל צ'ארט אפשר לזהות:
- **minor flow** — קבוצת שיאים ושפלים קטנים
- **major flow** — קבוצה גדולה יותר

> "It's not uncommon to find **more than two** flows simultaneously."

### החוק

> "price action **reverses significantly when both flows align in direction**."

**הדוגמה המפורטת מהשיעור:**
1. ה-major flow עולה (HH + HL)
2. בתוך התיקון של ה-major, ה-**minor** flow מראה מגמת **ירידה** — כלומר השניים **מנוגדים**
3. **המחיר מתהפך משמעותית כלפי מעלה ברגע שה-minor מתחיל להראות סימני מגמת עלייה שוב** —
   כלומר ברגע שה-minor **מתיישר מחדש** עם ה-major

```
major = UP,  minor = DOWN   →  אנחנו בתיקון. מחכים.
major = UP,  minor מתהפך ל-UP →  ⚡ טריגר — היפוך משמעותי כלפי מעלה
```

**זה החוק הראשון בקורס שהוא ממש כלל כניסה**, והוא ניתן לקידוד ישירות ברגע שמגדירים
איך מזהים flow (רצף HH/HL מול LH/LL בשתי סקאלות).

וכמובן — ה-minor flow הוא ה-major flow של טווח זמן נמוך יותר. עקבי עם כל השיטה.

### הביקורת על Elliott

> "Elliott made the mistake of trying to **impose** too many rules of how the market is
> **supposed to** work, instead of outlining a framework that **describes** what the market
> does."

זה בדיוק הציר descriptive/normative משיעור 1. `fractal flows` מוצג כתיקון של Elliott.
עם זאת — הפרסום של Elliott יוצר אפקט נבואה מגשימה את עצמה, ולכן יש לו ערך מעשי גם אם
ההסבר המתמטי שלו שגוי.

---

## Variability — הממד משתנה כל הזמן

הממד הפרקטלי **משתנה ברציפות**, ובדוגמה שהוצגה — **מחזורית**:

```
שוק דשדוש / קוצני   →  ממד גבוה   (לא למסחר)
מגמה ברורה וחזקה    →  ממד נמוך   (למסחר)
```

זה מתחבר להערה משיעור 4 על כך שה-`range` מתנהג מחזורית, ולהערה משיעור 8 על כך שאסור
לנתח כל נר. **כאן מתקבלת התשובה למה שחסר שם:** הטריגר להפעלת הניתוח העמוק הוא
**כניסה לאזור בעל ממד פרקטלי נמוך**.

---

## מה זה סוגר ומה נשאר

✅ **`price vector` — נסגר בפועל.** השיעור משתמש ב"price vectors **or** price movements in
isolation" כמילים נרדפות. ווקטור = קטע תנועה כיווני יחיד. (עדיין אין הגדרה פורמלית של
היכן ווקטור מתחיל ונגמר — זה יידרש לקוד.)

### פערים פתוחים

- **איך מודדים את הממד הפרקטלי בפועל?** השיעור מסביר את המושג יפה אבל **לא נותן נוסחה**.
  אין אזכור ל-box counting, Higuchi, Katz, או אינדיקטור מוכן. → שיעור 30 נקרא
  "Fractal Dimension **Filter**" — כנראה שם.
- **איפה בדיוק ווקטור מתחיל ונגמר?** בלי זה אי אפשר לחשב "ממד של ווקטור".
- **איך מגדירים flow אופרטיבית?** כמה נרות? איזו סקאלה מפרידה major מ-minor?
- הסתירה בין התמלול לשקף לגבי `Extremely Smooth` (ראה למעלה).
