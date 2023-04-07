---
title: "Optimize pandas dataframe calculation without looping through rows"
site: stackoverflow
question_id: 75959846
url: https://stackoverflow.com/q/75959846
asked: 2023-04-07T15:32:30Z
asked_by: "bong kem"
asked_by_url: https://stackoverflow.com/users/21589998
last_edited: 2023-04-08T04:22:10Z
tags: [python-3.x, pandas, dataframe]
score: -1
views_at_snapshot: 97
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 776a8f3acd9b798f8911a067846e155b60d453dcfefbf9b7b65a47e6a672e883
---

# Optimize pandas dataframe calculation without looping through rows

Asked by [bong kem](https://stackoverflow.com/users/21589998) on Stack Overflow, <https://stackoverflow.com/q/75959846>, 2023-04-07, last edited 2023-04-08. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm using panda to calculate capital after each trade as follow but wonder if there is any other way to calculate this without looping through every row?
Thanks in advance!!!

**Logic:**

```
trade = 1: buy
trade = -1: sell

diff: <Open> price of sell order - <Open> price of buy order, only calculate after each sell
position: capital/<Open> price, resets after each sell
gain = diff * position, only calculate after each sell
gain_c = gain_c + gain
capital = capital + gain
```

**The code I'm using:**

```
for i in range(1, len(df_trades)):
    if df_trades.loc[i, 'TRADE'] != -1: # BUY order: set POSITION for buy order
        df_trades.loc[i, 'POSITION'] = df_trades.loc[i,'CAPITAL']//df_trades.loc[i,'<Open>']
        df_trades.loc[i,'GAIN'] = 0
        df_trades.loc[i,'GAIN_C'] = df_trades.loc[i -1,'GAIN_C']
    if df_trades.loc[i, 'TRADE'] == -1: # SELL order: recalculate Capital, gain, gain_c
        df_trades.loc[i, 'POSITION'] = 0
        df_trades.loc[i,'DIFF'] = df_trades.loc[i,'<Open>'] - df_trades.loc[i-1,'<Open>']            
        df_trades.loc[i,'GAIN'] = df_trades.loc[i,'DIFF'] * df_trades.loc[i-1,'POSITION']
        df_trades.loc[i,'GAIN_C'] = df_trades.loc[i-1,'GAIN_C'] + df_trades.loc[i,'GAIN']
        df_trades.loc[i,'CAPITAL'] = df_trades.loc[i-1,'CAPITAL'] + df_trades.loc[i,'GAIN']
```

**Expected output:**

```
<Open> TRADE    CAPITAL  POSITION      GAIN    GAIN_C  DIFF
  7.17   1.0  100000.00   13947.0      0.00      0.00   NaN
  7.20  -1.0  100418.41       0.0    418.41    418.41  0.03
  7.19   1.0  100418.41   13966.0      0.00    418.41   NaN
  8.96  -1.0  125138.23       0.0  24719.82  25138.23  1.77
  8.99   1.0  125138.23   13919.0      0.00  25138.23   NaN
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Code Different](https://stackoverflow.com/users/2538939)** (2023-04-07): You forgot to include the sample input
- **[bong kem](https://stackoverflow.com/users/21589998)** (2023-04-07): hi, the input is in the expected output itself, it's all calculated with Open price and Capital
- **me** (2023-04-07): @bongkem but the expected output doesn't have a `<Close>` column, which is used in the loop
- **[bong kem](https://stackoverflow.com/users/21589998)** (2023-04-08): oh it's a typo, it's all open price, thanks for spotting that, i'll edit that right away
- **[RK Replogle](https://stackoverflow.com/users/11671944)** (2023-04-08): Your problem is iterative by nature so you are stuck with some form of looping or apply as suggested below. This is because the Capital value is dependent on the previous row, so I don't believe that you can do a single calculation on the entire DataFrame.
