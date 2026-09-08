# שיעור 12 — Frequencies, DFB & DFS

מקור: `transcripts/L012_Frequencies_DFB_DFS.json` · global 86

> **מנגנון הטריגר של השיטה.** עד כה למדנו לתאר (1-8) ולבחור היכן (11). כאן לומדים
> **מתי בדיוק ללחוץ**.

## מה זו תדירות

```
Fractal Analysis  ∩  Support & Resistance   =   Frequency Lines
```

הגדרה טכנית: **הקצב שבו משהו חוזר על עצמו לאורך זמן**. נובע ישירות מחקר הצללים
במונחים יחסיים (שיעורים 7-8).

> "We want the **precision of lower timeframes** with the **perspective of the home
> timeframe** without the pitfalls of switching timeframes."

זו אותה תמה שחוזרת בקורס בפעם הרביעית.

## חוק בניית קו התדירות ⭐ — קודד במלואו

> "The line that captures the **greatest number of candle shadows** in a set of candles
> **without violating the candle bodies** is the frequency line."

כלומר: המחיר **נוגע אך לא שובר** את הרמה בקצב הגבוה ביותר האפשרי.

```
maximize   |{ צללים שהקו נוגע בהם }|
subject to  הקו אינו חוצה אף גוף נר בקבוצה
```

**הריצה מהשיעור, נר אחר נר:**

| נר | מה קורה |
|---|---|
| 1 | קווים בשיא ובשפל. **בנר בודד אין הבדל בין קו S/R רגיל לקו תדירות** |
| 2 | הקווים **זזים** כדי לגעת בשני הצללים בלי לחתוך גופים |
| 3 | הקו העליון נשאר (הצל הנמוך היה בנר 2); הקו התחתון **עולה** — יש צל שמאפשר להתקרב לגופים בלי להפר |
| 4 (פנימי) | **הקווים לא זזים בכלל** — הזזתם תפר גופים של נרות קודמים |

קווי תדירות יכולים להיות **אופקיים או משופעים**. באלכסון: הזווית שלוכדת את כל הצללים
התחתונים בלי לחתוך אף גוף.

---

## Dynamic Frequency — התדירות בהתפתחות

```
צללים עליונים  →  upper dynamic frequency
צללים תחתונים  →  lower dynamic frequency
```

### טבלת התפקידים ⭐

| כיוון התנועה | upper DF | lower DF |
|---|---|---|
| **עולה** | סימני **המשך** | סימני **היפוך** |
| **יורדת** | סימני **היפוך** | סימני **המשך** |

**ההיגיון:** בתנועה עולה, ה-upper DF נשבר באופן עקבי — זה **נורמלי**, זה כיוון התנועה.
ה-lower DF **אינו נשבר לאורך כל התנועה**. ולכן:

> "so when it does [break], a **new price movement in the other direction is born**."

### שני האירועים

| | מהו | משמעות |
|---|---|---|
| **DFB** — Dynamic Frequency **Breakout** | המחיר **סוגר** מעבר לקו התדירות בפעם הראשונה | **היפוך** |
| **DFS** — Dynamic Frequency **Stop** | התדירות **מפסיקה להתקדם** — נבדקת ולא נשברת, או מתעדכנת אחורה | עצירה; **שבירתו** = **המשך** |

**ניסוח מדויק לפי כיוון:**

```
ווקטור עולה:   DFB ב-lower frequency  →  היפוך
               שבירת DFS ב-upper frequency  →  המשך

ווקטור יורד:   DFB ב-upper frequency  →  היפוך
               שבירת DFS ב-lower frequency  →  המשך
```

### הקריטריון המדויק ל-DFB

מהריצה המפורטת: **"the first time that price CLOSES below the lower dynamic frequency line."**

**סגירה, לא נגיעה.** זה קריטי לקידוד — נגיעה בצל אינה DFB.

```python
dfb_up_vector = close < lower_dynamic_frequency   # ראשונה מסוגה בווקטור
```

### התדירות כפילטר נגד אזעקות שווא ⭐

מהריצה: מופיע נר ברי שנראה כמו תחילת היפוך. אבל:

> "if we look at the behavior of the lower frequency, we will see that it's **respecting**
> the current dynamic frequency line by testing it without violating it."

> "the dynamic frequency line acts as a **filter** a lot of the times. Sometimes price
> **looks** like it's going to reverse, but when we look at the dynamic frequency, we can
> see that it **won't**."

**זו אחת התובנות המעשיות ביותר בקורס.** נר ברי בתוך מגמה עולה אינו אות היפוך כל עוד
הוא מכבד את ה-lower DF. הבוט חייב לבדוק את התדירות **לפני** שהוא מגיב לצורת הנר.

### כלל ההצטלבות (confluence) ⭐

בריצה, הנר השמיני מייצר **בו-זמנית**: DFS בתדירות העליונה **וגם** DFB בתדירות התחתונה.

> "not only did price stop in the upper shadows, but it also broke the frequency in the
> lower shadows, which **adds more strength to the reversal signal**."

### DFS והממד הפרקטלי ⭐

> "Dynamic Frequency Stops usually mean that the **fractal dimension of price is
> increasing**, which is a **warning** because we want the fractal dimension to be as low
> as possible."

> "If we observe **simultaneous DFB and DFS** patterns happening **within a low fractal
> dimension setting** — meaning smooth price action or gradual change in the intrinsic
> properties — we have a **stronger sign of reversal**."

זה מחבר את שיעור 11 לשיעור 12 בצורה ישירה: DFS בפני עצמו הוא אזהרה (הממד עולה), אבל
DFB+DFS יחד **בתוך סביבה חלקה** הם האות החזק.

### אזהרה מפורשת

> "it's **not a good idea to rely solely on this technique** as tempting as it might be,
> because in many occasions **price vectors are too small** to generate enough profit
> potential with a **good risk-reward ratio**."

---

## Real-Time מול Historical Frequencies

| | הגדרה |
|---|---|
| **Real-Time Frequency** | הרמה הפעילה שהמחיר מגיב אליה **כרגע** |
| **Historical Frequency** | תדירויות בולטות מהעבר הקרוב, ששימשו בזמנן כ-real-time |

**החוק:** כשה-DF נשבר והמחיר מתחיל ווקטור חדש בכיוון ההפוך, הווקטור החדש **יגיב לתדירויות
הבולטות של הווקטור הקודם** שכנגדו הוא מתקן.

בנוסף — המחיר מגיב גם ל**רמה שבה ה-DF נשבר או נעצר** בקצה הווקטור. (הקישור לטכניקות
supply & demand zones.)

**DFB ו-DFS כפופים ל-test / switch / retest** ⇒ אפשר להיכנס ב**הוראות לימיט** במקום
לחכות לפתיחת נר.

> "This can **dramatically enhance the risk-reward ratio**, but it's also a **more dangerous
> and difficult** technique."

---

## פערים פתוחים

- **מה "מפר גוף"?** הקו חייב לא לחתוך גוף — אבל האם נגיעה מדויקת בקצה גוף מותרת?
  נדרש epsilon.
- **מה גודל חלון קבוצת הנרות** לחישוב קו תדירות? "a set of candles" — לא נאמר כמה.
- **קו משופע — איך נבחר השיפוע?** רגרסיה? חיבור שני קצוות? אופטימיזציה תחת האילוץ?
  זה פער מימוש ממשי.
- **"too small price vectors"** — אין סף. נדרש מינימום R:R או מינימום גודל ווקטור.
