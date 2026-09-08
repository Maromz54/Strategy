# vol1 שיעורים 01-06 — יסודות התיאוריה

מקור: `transcripts/price_action_vol1/L001..L006` (שיעור 5 "The Level Zero" טרם נקרא)

> **החומר הזה סוגר שלושה פערים מרכזיים שסימנתי בקורס השני.** הוא הבסיס שאליו
> `fractal_trading` מפנה במפורש.

---

## הגדרת התחום (L001)

> "Price action analysis is the use of **logic** to interpret a price chart in order to find
> **interconnected patterns** that **might** shed light into the future of price."

ארבע הנחות מפורשות: (1) לוגיקה היא העדשה; (2) כל המידע הדרוש נמצא בצ'ארט; (3) הדפוסים
**מקושרים** בצורת נרטיב; (4) זה **לא מדע מדויק**, כי הצ'ארט הוא ייצוג פשטני של מנגנון מורכב.

### ארבעת האקסיומות

1. יש דפוסים **חוזרים** בצ'ארט שמאפשרים להשליך מהעבר הקרוב על העתיד המיידי
2. כל הדפוסים הרלוונטיים נמצאים ב-**raw price action** — *"no indicators like moving
   averages or Bollinger Bands"*
3. נדרשים **סוגי קווים** שונים ומשלימים. קווים הם *"the ultimate leading tools"*
4. יש שתי שכבות: **concrete** (מה שכולם רואים) ו-**abstract** (רק עם הכלים הנכונים)

> ⚠️ **סתירה בין הקורסים שכדאי לשים לב אליה.** אקסיומה 2 פוסלת אינדיקטורים במפורש ונוקבת
> ב-Bollinger Bands בשם. אבל `fractal_trading` **משתמש** ב-ATR(1)+Bollinger לסיווג טווח,
> ב-RSI לדיברגנס, וב-CVD לנפח. או שהמתודולוגיה התפתחה, או שהכוונה היא "לא כתחליף לקריאת
> מחיר גולמי, אלא ככלי מדידה עזר". **אני נוקט בפרשנות השנייה** — האינדיקטורים בקורס השני
> תמיד מכמתים תכונה של המחיר עצמו (טווח, קצב שינוי, דלתא), ואף פעם לא מייצרים אות בעצמם.

---

## שתי הדימנסיות של המחיר (L002)

| שכבה | מה היא |
|---|---|
| **Praxeological** | הלוגיקה של פעולה אנושית — היא ש**מניעה** את המחיר (היצע/ביקוש, פסיכולוגיה, היוריסטיקות) |
| **Logical** | מתמטיקה, פיזיקה, סטטיסטיקה — הן ש**מגבילות** את התנועה ומתארות אותה |

פרקסאולוגיה ⊂ חוקי הפיזיקה (מעגלים קונצנטריים). *"our actions are not entirely logical, but
they are bounded by a logical universe."*

## ⭐ Metaphysical Verification — מבחן הקוהרנטיות

זהו הרעיון שהכי קשה לקודד ואולי החשוב ביותר במתודולוגיה.

**הבעיה:** יש לנו יכולת להסיק דפוסים מנתונים דלילים — ברכה וקללה. הקללה:

> "**Setups are just a combination of disconnected facts** about price, which creates a
> powerful illusion. They look like they make sense on the surface, but they are
> **disconnected at the core**."

> "The illusion here is that **connected and disconnected facts in the chart look exactly
> the same**."

**הפתרון שמוצע:** ארבע הסיבות של אריסטו כמבחן שמראה איך סיבות ותוצאות מתפשטות בין
עובדות הצ'ארט, באופן ליניארי ולא-ליניארי.

```
לא מצליחים להרכיב נרטיב תחת ארבע הסיבות  →  העובדות מנותקות  →  אין עסקה
מצליחים                                   →  "temporary suspension of the Brownian
                                              motion" → יש הזדמנות
```

**המשמעות לבוט:** זה **לא** פילטר נוסף — זו הגדרת ה-go/no-go. וזה בדיוק מה שמפריד את
המתודולוגיה הזו מ"setup". → שיעור 9 (`Metaphysics and Narrative`) אמור לפרט. **עד שאקרא
אותו, זה הפער הגדול ביותר בקידוד.**

## Trader's Paradox (L002)

אנחנו גרועים בניתוח השוק שאנחנו עצמנו יוצרים. קאנט: אי אפשר לחלץ מנתוני החושים את המבנה
הקוגניטיבי שמאפשר להבין אותם. הפתרון המוצע: מדע כשופט חיצוני, ופיתוח "impartial spectator".

> **הערה שלי:** זהו למעשה **טיעון בעד אוטומציה**. בוט אינו סובל מהפרדוקס הזה — אין לו
> הטיה קוגניטיבית, אין לו הצורך "להתאהב ביצירה של עצמו". זה אולי הנימוק החזק ביותר
> להעביר את השיטה הזו לקוד דווקא.

---

## Econophysics (L003) ו-Reflexivity (L004)

L003: פעולה אנושית כפופה לחוקי הפיזיקה (העיקרון האנתרופי). לכן לגיטימי להחיל מתמטיקה
ופיזיקה על מחיר.

L004 — **וזה משמעותי לבוט:** תיאוריית ה-Reflexivity של סורוס — לולאת משוב דו-כיוונית בין
אנשים לשוק.

> "In chaos theory, this is just called a **chaotic system of second order** because the
> **predictions about the system change the state of the system itself**."

**זו אזהרה תפעולית אמיתית:** אסטרטגיה שנעשית מוכרת מספיק מְשַׁנה את השוק ומשחיקה את עצמה.
זה גם מסביר למה הקורס אומר ש-Elliott "עובד" חלקית דרך נבואה מגשימה את עצמה. לבוט:
**לצפות לדעיכת ביצועים לאורך זמן, ולנטר אותה** — לא להניח שהקצה יציב.

---

# ⭐⭐ The Level One (L006) — כאן נסגרים הפערים

## 1. Price Vector — ההגדרה הפורמלית ✅

> "The price vector is the **distance between recognizable highs and lows** in the chart."

```
וקטור עולה:  מתחיל בשפל, נגמר בשיא
וקטור יורד:  מתחיל בשיא, נגמר בשפל
```

### ארבע התכונות

| תכונה | הגדרה |
|---|---|
| **Extremes** | שני הקצוות. הם ש**מחברים** וקטור לוקטור |
| **Midpoint** | האמצע המדויק בין הקצוות |
| **Near-Extremes** | **לא נקודה אלא טווח** — בין התדירות הפנימית לחיצונית שקרו ליד הקצה |
| **Inside / Outside** | ראה למטה |

### ההיגיון של היצע/ביקוש

- **בשיא:** יותר מדי היצע, כמעט אין ביקוש ⟹ למחיר אין ברירה אלא לרדת
- **בשפל:** יותר מדי ביקוש, כמעט אין היצע ⟹ למחיר אין ברירה אלא לעלות
- **ב-midpoint:** היצע וביקוש **מאוזנים**

> "the whole trajectory of a price vector is like a **seesaw** between supply and demand that
> swings from extreme unbalance → perfect balance → extreme unbalance again."

### Near-Extremes — למה זה חשוב

> "Price doesn't really accelerate at full power **at** the extremes. It starts to accelerate
> to the other side **in the near-extremes**. Just like a car doesn't go from 0 to 60
> instantly."

**שם חיים אזורי ההיצע והביקוש האמיתיים.** כלומר: לא לצייר supply/demand zone על הקצה
עצמו, אלא על הטווח שלפניו. זה משפיע ישירות על מיקום סטופ ויעד.

### ⭐ Inside / Outside — ומדוע זה מסביר את DFB/DFS

| | בווקטור עולה | תפקיד |
|---|---|---|
| **Inside** | ה**שפלים** של הנרות | הצד ה**פעיל, הדומיננטי** — לחץ קנייה דוחף שפלים למעלה **ומצליח** |
| **Outside** | ה**שיאים** של הנרות | הצד ה**מגיב, פסאודו-דומיננטי** — לחץ מכירה דוחף שיאים למטה **ונכשל** |

**וכאן ההתאמה המושלמת לשיעור 12 של הקורס השני:**

```
inside  (השפלים בווקטור עולה)  ≡  lower dynamic frequency  — זו שלא נשברת, ושבירתה = היפוך
outside (השיאים בווקטור עולה)  ≡  upper dynamic frequency  — זו שנשברת שוב ושוב כרגיל
```

**זה מסביר *למה* ה-DFB עובד**, ולא רק מה הוא. עד עכשיו זה היה כלל; עכשיו זה נגזר ממבנה.

> "in the vector extreme, there is a moment where the **inside of an upward vector turns
> into the outside of a downward vector**... the moment market players shift positions."

## 2. Market Flow — ההגדרה האופרטיבית ✅

> "A combination of vectors that have **roughly the same magnitude** compose what we call a
> **market flow**, because the alternating price vectors are formed by **traders that have
> roughly the same size**."

**זה בדיוק מה שחסר לי בשיעור 11 של הקורס השני.** `major flow` מול `minor flow` = **מחלקות
גודל שונות של וקטורים**. לקידוד: לחלץ וקטורים, לקבץ לפי מגניטודה, וכל אשכול הוא flow.

וההיגיון מאחורי זה יפה — הגודל של הווקטור משקף את **גודל השחקנים** שיצרו אותו.

## 3. ⭐⭐ ארבעת מצבי השוק — מסווג המשטר

מודל: מערך מטוטלות מצומדות (harmonic oscillator). מטוטלת בודדת = flow פשוט, ליניארי וצפוי.
סופרפוזיציה של מטוטלות = מערכת לא-ליניארית. הניסוי מראה **ארבעה** דפוסים:

| flow | תנועה במתנד | השוק | סדר |
|---|---|---|---|
| **Standing** | Standing motion | מגמה **נקייה**, כמעט בלי תנודות | הכי מסודר |
| **Travelling** | Travelling motion | תנודה **חלקה** — *"the market everyone likes to trade"* | מסודר |
| **Beating** | Beating motion | דשדוש **מסודר** | מסודר |
| **Brownian** | Brownian motion | כאוס — שיאים ושפלים מפוזרים ומנותקים | הכי כאוטי |

> "we want to trade the phases where the movement is **orderly** and therefore predictable,
> and we want to **avoid the chaotic movements**, especially the purely Brownian phases."

**זה מסווג המשטר שהבוט צריך**, והוא קונקרטי יותר מ"ממד פרקטלי נמוך" — ארבע מחלקות במקום
ספקטרום. ושלוש מתוך ארבע הן ניתנות למסחר.

**והפרקטליות מוסיפה שכבה:** *"within Brownian flows, there can be standing, travelling, or
beating flows happening in a lower degree. In fact, that happens indefinitely."* — כלומר
Brownian ב-TF אחד אינו פסילה מוחלטת; יש לרדת סקאלה ולבדוק.

> סייג שהמרצה עצמו מציין: המתנד ההרמוני פשוט מהשוק, כי אין לו שכבה פרקסאולוגית. לכן
> **משך** כל משטר בשוק פחות צפוי מאשר בניסוי.

## 4. Hausdorff Dimension — שם המדד ✅

> "The **Hausdorff dimension** is a measure of **roughness** of a structure."

```
לראות וקטורים מושלמים מאחורי נרות מחוספסים   =  הקטנת הממד
לראות את הווקטורים הקטנים שמרכיבים וקטור      =  הגדלת הממד
```

> "the **counterpoint** between price action seen in **different Hausdorff dimensions** is one
> of the most powerful starting points of any analysis."

**וניואנס חשוב:** לא תמיד רוצים להקטין. *"to look at certain details of price, like frequency
along the candle tails, we **don't** want to reduce the Hausdorff dimension. We want to
maintain it as it is, otherwise we lose precious information."*

> ⚠️ עדיין **אין נוסחה** — יש שם. Hausdorff dimension על סדרת מחירים מחושב בפועל
> בקירוב (box-counting / Higuchi / Katz). הקורס לא נוקב בשיטה. הפער צומצם אך לא נסגר.

## 5. ההיררכיה הפרקטלית (Mandelbrot × Mises)

```
transactions → tick → price vectors → flows → larger vectors → larger flows → markets → economy
```

## 6. ארגז הכלים המתמטי שהוכרז

| תחום | מה בדיוק |
|---|---|
| מתמטיקה | Chaos Theory, Euclidean / fractal / analytical geometry, וקטורים, מרחבים וקטוריים |
| סטטיסטיקה | **רק** המושג `frequency` |
| פיזיקה | חוקי ניוטון ומכניקה קלאסית |
| מטאפיזיקה | ארבע הסיבות של אריסטו — כבקרת הטיה |

---

## מה נסגר ומה עדיין פתוח

### ✅ נסגר
- `price vector` — הגדרה פורמלית + ארבע תכונות
- `market flow` — הגדרה אופרטיבית (וקטורים בעלי מגניטודה דומה)
- **הסבר מבני ל-DFB/DFS** דרך inside/outside
- **מסווג משטר שוק** בן ארבע מחלקות
- שם המדד לחספוס: Hausdorff dimension
- מיקום אזורי היצע/ביקוש: ב-near-extremes, לא בקצוות

### ⚠️ נשאר פתוח
- **נוסחה** לממד — יש שם, אין חישוב. (vol1 L015-L019 עוסקים בתדירויות; fractal_trading L030
  נקרא "Fractal Dimension Filter")
- **המבחן המטאפיזי** — הרעיון המרכזי שהכי קשה לקודד. → vol1 L009
- **"recognizable" highs and lows** — מה הופך שיא ל"מזוהה"? בלי זה אי אפשר לחלץ וקטורים
  אוטומטית. זהו כעת **הפער הבסיסי ביותר**, כי הכול בנוי על וקטורים. → vol1 L013 (`Extremes`)
- הסתירה סביב אקסיומה 2 (אינדיקטורים)
