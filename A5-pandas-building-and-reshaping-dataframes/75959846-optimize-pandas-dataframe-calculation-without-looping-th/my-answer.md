---
title: "Optimize pandas dataframe calculation without looping through rows"
site: stackoverflow
question_id: 75959846
answer_id: 75962227
url: https://stackoverflow.com/a/75962227
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-07T21:59:46Z
last_edited: 2023-04-09T09:12:52Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75962227/revisions
accepted: false
score: 0
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8317f3de2ae42167ad20a72ade187742472a6358baec8a3a4714d685b5529418
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-07

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75962227>, 2023-04-07, last edited 2023-04-09; score 0. Text as retrieved 2026-10-12.

You could define a function with a row input [and output] and [`.apply`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html) it (instead of using the `for` loop) across columns like <kbd>`df_trades = df_trades.apply(calculate_capital, axis=1, from_df=df_trades)`</kbd> where `calculate_capital` is defined as

```py
def calculate_capital(row, from_df):
    if row.name==0: return row
    prev_row = from_df.loc[row.name-1]
    if row['TRADE'] != -1: # BUY order: set POSITION for buy order
        row['POSITION'] = row['CAPITAL']//row['<Open>']
        row['GAIN'] = 0
        row['GAIN_C'] = prev_row['GAIN_C']
    if row['TRADE'] == -1: # SELL order: recalculate Capital, gain, gain_c
        row['POSITION'] = 0
        row['DIFF'] = row['<Close>'] - prev_row['<Open>']            
        row['GAIN'] = row['DIFF'] * prev_row['POSITION']
        row['GAIN_C'] = prev_row['GAIN_C'] + row['GAIN']
        row['CAPITAL'] = prev_row['CAPITAL'] + row['GAIN']
    return row
```

---

**Example**: If I recreate your sample data as `df_trades` with

```py
df_trades = pd.DataFrame([l.split() for l in '''
  7.17   1.0  100000.00   13947.0      0.00      0.00   NaN
  7.20  -1.0  100418.41       0.0    418.41    418.41  0.03
  7.19   1.0  100418.41   13966.0      0.00    418.41   NaN
  8.96  -1.0  125138.23       0.0  24719.82  25138.23  1.77
  8.99   1.0  125138.23   13919.0      0.00  25138.23   NaN
'''.splitlines() if l.strip()], columns='''
  <Open> TRADE    CAPITAL  POSITION      GAIN    GAIN_C  DIFF
'''.split())
df_trades = df_trades.assign(**{'<Close>': 8})[[
    '<Open>','<Close>', 'TRADE','CAPITAL','POSITION', 'GAIN','GAIN_C','DIFF'
]].applymap(float)
```

<sup>**(I added and filled `<Close>` with `8`s since your loop snippet indicated there should be such a column.)**</sup>

The changes in the results below are highlighted in green.

> [![opdfs][1]][1]

---
---

In retrospect, I think it might be faster to apply this function:

```py
def calculate_new_row(row):
    if row.name==0: return row
    if row['TRADE'] != -1: # BUY order: set POSITION for buy order
        row['POSITION'] = row['CAPITAL']//row['<Open>']
        row['GAIN'] = 0
        row['GAIN_C'] = row['GAIN_C_prev']
    if row['TRADE'] == -1: # SELL order: recalculate Capital, gain, gain_c
        row['POSITION'] = 0
        row['DIFF'] = row['<Close>'] - row['<Open>_prev']            
        row['GAIN'] = row['DIFF'] * row['POSITION_prev']
        row['GAIN_C'] = row['GAIN_C_prev'] + row['GAIN']
        row['CAPITAL'] = row['CAPITAL_prev'] + row['GAIN']
    return row
```

but after joining (with [`.join`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html)) `df_trades` to a shifted version (via [`.shift`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shift.html))<sup>([view example][2])</sup>

```py
df_trades = df_trades.join(
    df_trades.shift(), rsuffix='_prev').apply(
        calculate_new_row, axis=1)[df_trades.columns]
```


  [1]: https://i.sstatic.net/pWNJX.png
  [2]: https://i.sstatic.net/nzdxj.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[bong kem](https://stackoverflow.com/users/21589998)** (2023-04-08): thanks a lot, i have an impression that the apply method don't go row by row to calculate each Capital  but rather try to do the calculation all at once, right? I try to write the code as you suggest and it generated a bunch of Nan (and do no calculation) for Capital, Gain, Gain_c after row 1.
- **me** (2023-04-09): @bongkem I wouldn't be able to figure out why that's happening without being able to reproduce your `df_trades` more exactly (like if you add a snippet with the output from `df_trades.to_dict('tight')` to your post), but I've added in a screenshot of what I got with a df generated from parsing your sample snippet, as well as another method which I think would be faster
- **[bong kem](https://stackoverflow.com/users/21589998)** (2023-04-09): that's amazing, i'll try the shifted join approach to optimize the run time, thanks a lot !!!
