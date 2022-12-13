---
title: "Check if column name from one dataframe matches with index value of another dataframe and populate value into a new column"
site: stackoverflow
question_id: 74790102
answer_id: 74790801
url: https://stackoverflow.com/a/74790801
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-13T20:58:52Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74790801/revisions
accepted: false
score: 0
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5eeb81496779adea0ed4411dec8d67391b4eef6437d3159f44d76b2300fb3bb2
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-13

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74790801>, 2022-12-13; score 0. Text as retrieved 2026-10-12.

You could define a function to get the profits at corresponding tiemstamps:

```python
# import dateutil.parser
# from datetime import timedelta

def getProfit_atDelay(delayMins, startTime, profitDF):
    try: 
        startTime = dateutil.parser.parse(str(startTime))
        dTime = startTime - timedelta(minutes=int(str(delayMins)))
        return profitDF['Profit'].loc[dTime]
    except: return None
```

(I'm assuming that `df_profit` index contains datetime datatype; otherwise, edit code to convert `dTime` to the matching datatype.)

---

And to get all the values for the new column:

```python
def profits_for_rates(ratesDF, profitDF):
    rStart, rMins = ratesDF.columns[1], ratesDF['Mins before time']
    return [getProfit_atDelay(t, rStart, profitDF) for t in rMins]
```

---

If you use it like 

```python
df_rates['New_column'] = profits_for_rates(df_rates, df_profit)
```

then `df_rates` will look like

```python
   Mins before time  2012-03-31 23:45:00  New_column
0                 0               113.10    3504.664
1                 5               112.10         NaN
2                10               113.10         NaN
3                15               113.17    1215.760
4                20               103.17         NaN
5                25               133.17         NaN
6                30               101.39     -21.480
```
