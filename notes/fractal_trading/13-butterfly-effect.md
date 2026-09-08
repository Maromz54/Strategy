# שיעור 13 — Butterfly Effect

מקור: `transcripts/L013_Butterfly_Effect.json` · global 87 · שיעור קצר, השלכה גדולה

## ההנחה שמתחת לכל השיטה

> "financial markets are **chaotic and fractal**. Meaning that the market is **not random**,
> but a higher degree of order that **seems** to be random, but that has a **simple and
> deterministic mechanism** in its origin."

המנגנון: היגיון היצע וביקוש. מה שהופך אותו לכאוטי הוא שיש שחקנים רבים בעלי עוצמה שונה,
שפועלים מסיבות שונות ובאופקי זמן שונים.

**זו הבחנה מהותית ולא סמנטית:** *כאוטי* ≠ *אקראי*. מערכת אקראית אינה ניתנת לניצול;
מערכת כאוטית — כן, אם מזהים את המבנה.

## אפקט הפרפר = Sensitive Dependence on Initial Conditions

שינויים **קטנים ולכאורה חסרי חשיבות** מובילים לשינויים **גדולים וחשובים**.

## עקרון הכניסה ⭐⭐

> "We want to enter trades that are signaled by **small changes** so that the **large changes
> happen to our advantage when we are already in the market**."

**ומה קורה אחרת:**

> "If we enter trades that are signaled by **large changes**, the entry point will usually
> be **too far away from the logical stop loss**, and the trade becomes unreliable."

> "If we enter the trade **in the middle of the hurricane**, the only direction it can go is
> to **calm down**."

**זו הצדקה מכנית, לא פילוסופית:** אות גדול = הכניסה רחוקה מהסטופ ההגיוני = R:R גרוע.
לכן העדפת אות קטן אינה עניין של טעם — היא נגזרת ישירות מגיאומטריית העסקה.

זה מאשש ומחדד את מה שסימנתי בשיעור 10: *"the candle that breaks the dynamic frequency is
not too dramatic."* **חיפוש נרות דרמטיים כטריגר סותר את השיטה מיסודה.**

---

## הפילטר האובייקטיבי ל-DFB ⭐⭐ — הכי קודד בקורס עד כה

> "the more reliable dynamic frequency breakouts happen with **low to medium volatility**.
> We can measure that objectively with the **ATR(1) represented as columns**, and with the
> **modified Bollinger Bands** indicator plotted on top of it."

**זה בדיוק האינדיקטור משיעור 4.** הסיווג שבנינו שם מקבל כאן את שימושו הראשון:

```python
# מסיווג הטווח של שיעור 4
if range_class in ("narrow", "medium"):    # מתחת ל-2σ
    dfb_valid = True                       # ← "reliable"
elif range_class in ("wide", "outlier"):   # מעל 2σ
    dfb_valid = False                      # ← "unreliable"
```

השיעור נוקב במפורש בסף: **"volatility above the two sigma level"** = לא אמין.

### הטענה החזקה ⭐

> "the **unreliable DFBs tend to lead to the OPPOSITE price vector that they signal**."

**זו לא רק חולשה — זו היפוך.** DFB בתנודתיות גבוהה לא סתם נכשל; הוא נוטה להוביל לכיוון
ההפוך מזה שהוא מסמן. אם זה נכון, יש כאן שני מסקנות אפשריות לבוט:
1. **מינימום:** לפסול DFB שנוצר מעל 2σ.
2. **אגרסיבי:** לשקול אותו כאות **הפוך**.

אני **לא** אקדד את (2) בלי בקטסט — טענה כזו חייבת אימות סטטיסטי לפני שסומכים עליה. אבל
היא בהחלט שווה בדיקה, וזו בדיקה זולה.

### קריטריון נוסף

> "this dynamic frequency breakout is confirmed **too far away from the origin of the price
> vector**."

כלומר DFB שמתאשש רחוק מדי מנקודת ההתחלה של הווקטור — לא אמין. צריך מדד מרחק מהמקור.

## דוגמאות מהשיעור

- DFB אחד קטן ולכאורה חסר חשיבות → ממנו נולדת תנועה עולה **גדולה מאוד**. הפרפר = ה-DFB;
  ההוריקן = התנועה.
- **סייג הכרחי מהמרצה עצמו:** "**not every** small DFB generates a result like this,
  otherwise we would not need the rest of this course."

## סיכום — שרשרת הכניסה כפי שהיא מצטיירת כרגע

```
1. אזור בעל ממד פרקטלי נמוך            (שיעור 11 — היכן בכלל להסתכל)
2. הקשר: flows מיושרים / כוחות חיצוניים (שיעורים 9-11)
3. DFB בתדירות הנגדית                  (שיעור 12 — הטריגר)
4. פילטר: הנר מתחת ל-2σ                (שיעור 13 — האימות)  ← קטן, לא דרמטי
5. חיזוק: DFB+DFS בו-זמנית בסביבה חלקה  (שיעור 12)
```

עדיין חסרים: **סטופ, יעד וגודל פוזיציה** → שיעורים 21, 23, 24, 26.
