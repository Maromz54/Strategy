# fractal_trading 19-26 — הפעלה, טריגרים, סיכון וגודל פוזיציה

מקור: `L019_Game_Theory_and_Learning_How_to_Trade.json`, `L020_FPARF_Important_Advice.json`,
`L021_Trade_Triggers_Stops_Targets.json`, `L022_Risk_Behavior_Performance.json`,
`L023_Mathematics_of_RiskReward_Ratios.json`, `L024_Technical_Aspect_of_RiskReward_Ratios.json`,
`L025_Integrating_Mathematics_Technique_Psychology.json`, `L026_Position_Sizing.json`

> ⭐⭐⭐ **מודול הביצוע והסיכון המלא.** כאן נמצאת המתמטיקה היחידה בקורס שהיא מדויקת
> ומלאה, בלי פערים.

---

# L020 — F.P.A.R.F.: שני מסלולי ניתוח

| | מאיפה מתחילים | הזרימה |
|---|---|---|
| **Top-down** | אות מ**כוח חיצוני** (פאזה / דיברגנס / מחסום) | → בודקים חפיפה עם שאר הכוחות → נבנה הקשר → מתבוננים במחיר מול מחסום אחד או יותר → **רק אז** תכונות פנימיות, FC ו-DFB → טריגר, סטופ, יעד |
| **Bottom-up** | **DFB** — אות צר וממוקד | → מרחיבים לכוחות החיצוניים כדי לבדוק אם ה-DFB בהקשר מתאים → מצמצמים שוב לתכונות הפנימיות → טריגר, סטופ, יעד |

## ⭐⭐ שתי אמירות שמעצבות את ארכיטקטורת הבוט

**(א) DFB הוא תנאי הכרחי:**
> "**Notice that ALL price reversals include a DFB.** It's a matter of **filtering out the
> unreliable ones** as efficiently as possible."

```
DFB       =  מחולל מועמדים  (necessary, not sufficient)
כל השאר   =  פילטרים
```
**זה בדיוק המבנה שבוט אוהב:** אירוע זול לגילוי שמצמצם את מרחב החיפוש, ואחריו שכבת סינון
יקרה יותר. וזה גם מסביר את האזהרה משיעור 12 — *"don't rely solely on DFB"* — נכון, כי
הוא מחולל ולא מכריע.

**(ב) אסור להתחיל מהנר:**
> "it's a **terrible idea** to start analyzing any chart by the intrinsic properties of a
> candle. There is **too much information**... **analysis paralysis** will occur. The
> intrinsic properties... should be done **only when there is a context**... usually in
> relation to a **price barrier**."

## ⭐ כלל אבחון עצמי — קודד ישירות

> "if the trader **cannot integrate or identify signals**, it's because **there isn't a
> high-quality trade opportunity happening**. When the trader can **easily** identify and
> integrate many signals, it becomes **pretty obvious** that this is a high-quality
> opportunity."

**קושי האינטגרציה הוא עצמו הפילטר.** לבוט: אם ספירת המרכיבים המיושרים נמוכה — אין עסקה.
לא צריך "להחליט" — האות פשוט לא מצטבר.

> "You **cannot trade whenever you feel like it. The market will tell you when it's time.**"
> "Trading price action correctly is **boring**."

---

# ⭐⭐ L021 — טריגרים, סטופים ויעדים

**דרישות מטריגר:** אובייקטיבי · מדויק · תזמון טוב.

> "The trade analysis **starts with a higher level of subjectivity**. As the analysis
> progresses, it becomes **more focused and objective**."

## שני סוגי טריגר

| | מנגנון | קושי | דיוק |
|---|---|---|---|
| **Market trigger** | ממתינים לסגירת נר האות ונכנסים ב**פתיחת הנר הבא**. אותות: `fractal candle`, `DFB`, ולעיתים inside/outside | קל | פחות מדויק |
| **Limit trigger** | `switch / test / retest` תחת ניתוח פרקטלי — מניחים לימיט **על קו ה-DFB** או על מחסום | קשה בהרבה | **R:R גבוה בהרבה** |

### הדוגמה המספרית מהשיעור

```
כניסה ב-market order  →  R:R = 2.10
כניסה ב-limit order   →  R:R = 5.11        ( +143% )
```

**המחיר:** לפעמים המחיר לא חוזר לרמה והעסקה יוצאת בלעדיך.

### ⭐ ניואנס שמתקן את ההערה שלי על שיעור 13

> "this is a **high volatility DFB, which would eliminate the butterfly effect**, but the
> **limit order trigger can make this entry reliable again**."

כלומר: DFB שנפסל בפילטר ה-2σ **אינו בהכרח אבוד** — כניסת לימיט על קו ה-DFB יכולה להחזיר
אותו למשחק, כי היא משפרת את הגיאומטריה של העסקה. בהערה על שיעור 13 כתבתי שהפילטר פוסל;
מדויק יותר לומר ש**הוא פוסל כניסת שוק**.

## ⭐ חוק הסטופ — ניסוח מבצעי

> "In this method, we **always get near newly formed and potential market extremes**. The
> stop must **always be above or below a newly formed and potential high or low**."

תואם לחלוטין ל-vol1 L023/L048 (מאחורי מבנה **מוצק**), וכאן בניסוח תפעולי ישיר.

> "you can find fractal candles and DFBs in **many places**. That **doesn't mean you should
> trigger trades every time you see them**."

---

# L022 — איכות תשואה מול כמות

> "the outcome of your trades is **probabilistic**, but the risk management is
> **deterministic**."

ניסוח מצוין: אי אפשר לשלוט אם עסקה תנצח — אפשר לשלוט **כמה מפסידים בה**.

**יחידות תשואה ליחידת סיכון:**

| | תשואה | סיכון | יחידות |
|---|---|---|---|
| סוחר A | 10% | 1% | **10** |
| סוחר B | 10% | 5% | 2 |
| סוחר A' | **5%** | 1% | **5** |
| סוחר B' | **10%** | 5% | 2 |

> "**a higher return is not necessarily a better return**"

A' מייצר **חצי** מהתשואה של B' — ובכל זאת איכותו **פי 2.5**.

**לבוט:** פונקציית המטרה בבקטסט אינה תשואה. היא תשואה **ליחידת סיכון**.

---

# ⭐⭐ L023 — מתמטיקת ה-R:R

```python
minimum_win_rate = 1 / (1 + R)
margin_of_error  = 1 - minimum_win_rate
```

| R | שיעור זכייה מינימלי | מרווח טעות |
|---|---|---|
| 0.25 | 80% | 20% |
| 1 | 50% | 50% |
| 3 | 25% | 75% |
| 4 | 20% | 80% |
| 10 | 9.1% | 90.9% |

## ⭐ הקשר האקספוננציאלי ההפוך

> "as ratios increase **linearly**, the change in margin of error **decays exponentially**."

```
0.25 → 1     (מרחק 0.75)  :  +30.00%  במרווח הטעות
1    → 1.75  (מרחק 0.75)  :  +13.64%  בלבד
```

**מסקנה מפורשת:** *"it's **not reasonable to aim for the highest ratio possible**."*
ובנוסף — יעד רחוק יותר גם **קשה יותר לפגוע בו**. שני הכוחות פועלים באותו כיוון.

## ⭐⭐ אין קצה ב-R:R לבדו

> "different risk-reward ratios provide **no mathematical edge when trades are opened
> randomly**... If you open 1,000 random trades using a specific ratio, the **win rate will be
> very close to the minimum win rate** associated with the ratio."

יחסים לא-נוחים ⟹ שיעור זכייה **גבוה** מטבעם. יחסים נוחים ⟹ שיעור זכייה **נמוך** מטבעם.

**ולכן:**
> "**win rate by itself is misleading.** It must be judged in the context of the minimum win
> rate associated with each ratio. A **35% win rate is sometimes better than a 70%** win rate."

**זה קריטי לבקטסט:** מדד ההצלחה אינו win rate אלא `win_rate − minimum_win_rate(R)`.
בוט שמדווח "68% הצלחה" בלי לציין את ה-R שלו אינו מדווח כלום.

---

# ⭐⭐ L024 — ההיבט הטכני: היכן הקצה כן נמצא

> "if a trader can open a trade **near a reversal point** and place his stop in a **strategic
> place**, the opposite happens. **The target becomes more likely to be hit**, even while
> being a few times farther from the entry."

כלומר: הקצה אינו ב-R:R — הוא ב**מיקום ובתזמון**. ה-R:R רק **ממנף** אותו.

## ⭐ היחס תלוי-פאזה

```
עסקה נגד-מגמתית          →  יחס  קטן יותר
עסקה בתחילת מגמה         →  יחס  גבוה בהרבה
תמיד                     →  נוח (reward > risk)
```

## ⭐ מה מעלה את שיעור הזכייה מעל המינימום

> "And the answer is simple: **integration**. The higher the level of integration in a trade,
> the more likely it is to be a winner."

זו החוליה שסוגרת את הלולאה:
```
אינטגרציה ↑  →  שיעור זכייה ↑  →  win_rate − MWR(R) > 0  →  ציפייה חיובית
```
**וזו ההצדקה המתמטית לכל מודל הניקוד** של ה-Integrated Fractal Candle.

## תנודתיות ו-repellers

> "you want to enter trades when the market has **low volatility** with the expectation that
> volatility will **increase to the desired side**... you want to enter near potential
> **repellers**, moments where the integration produces a **self-reinforcing cycle**."

זה מחבר את אפקט הפרפר (L013) לדינמיקה הלא-ליניארית (L017) ולמתמטיקת ה-R:R — **תנודתיות
נמוכה בכניסה היא מה שהופך יעד רחוק לבר-השגה**.

---

# L025 — הסינתזה

> "risk-reward ratios should be **phase-dependent and favorably bounded**."

| תכונה | פירוש |
|---|---|
| **Phase-dependent** | הגודל הנכון תלוי בפאזת השוק |
| **Favorable** | תמיד reward > risk — כדי לקזז loss aversion |
| **Bounded** | לא לשאוף ליחס אינסופי — הדעיכה האקספוננציאלית |

---

# ⭐ L026 — גודל פוזיציה

```
סיכון 1%  לעסקה  →  צריך 100 הפסדים רצופים כדי להתאפס
סיכון 10% לעסקה  →  מספיקים 10
```

> "**sustainability is inversely proportional to percentage risk**" — סיכון גבוה ⟹ סטיית
> תקן גבוהה של התשואות ⟹ קיימוּת נמוכה.

**הנחיה:** 1% הוא הכלל הרווח, אבל — *"use a percentage risk that makes you **completely
forget** about risk. That will certainly be **equal or less than 1%**."*

> ⭐ **ואמירה נגד-אינטואיטיבית:** *"The **higher** your predictive power and risk management
> skills, the **lower** your percentage risk needs to be."*

## שלושת מודלי הגודל

| מודל | בסיס | אפקט |
|---|---|---|
| **Linear** | אחוז מההון **ההתחלתי** | איטי ובטוח, **בלי** ריבית דריבית |
| **Geometric** | אחוז מההון **הנוכחי** | מרכיב רווחים — **ומרכיב גם הפסדים** |
| **Geolinear** | מעדכנים את האחוז ברמות הון מוגדרות מראש (למשל כל ±25%) | *"seems to be the **optimal choice** while being practical"* |

**לבוט: geolinear.** קל לממש (סף בדיד), נהנה מריבית דריבית חלקית, ומגביל את קצב
הגידול בסיכון.

---

# L019 — מה שכדאי לדעת על למידה מהתוצאות

אנלוגיה: זירה שבה משוחקות **וריאציות שונות של שחמט בו-זמנית**, ומהלכים במשחק אחד משפיעים
על משחקים אחרים.

> "Doing the right thing **doesn't always yield a good result**, and doing the wrong thing
> sometimes yields an **illusory good result**."

> "there are **right ways of losing and wrong ways of winning**."

> "The **outcome** is not entirely up to you. But the **process** is mostly up to you."

> "you need to learn how to **reward good behavior instead of rewarding performance**."

**לבוט — וזו נקודה מעשית:** אסור להעריך את האסטרטגיה לפי תוצאת עסקה בודדת, ואסור לכייל
פרמטרים לפי מקטעים קצרים. זו הרחבה ישירה של אזהרת ה-`unknown probability` מ-L018.

## אזהרה שכדאי להעביר הלאה

> "it's a **mistake to attempt trading for a living as a retail trader**. Retail traders can
> only rely on performance. They don't have a salary."

המרצה מסביר שקרנות משלמות **שכר + בונוס** דווקא כי ביצועי מסחר לבדם אינם יכולים לספק
יציבות פיננסית לצרכים שוטפים.
