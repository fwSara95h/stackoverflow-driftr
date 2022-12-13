---
title: "Check if column name from one dataframe matches with index value of another dataframe and populate value into a new column"
site: stackoverflow
question_id: 74790102
answer_id: 74790535
url: https://stackoverflow.com/a/74790535
author: "constantstranger"
author_url: https://stackoverflow.com/users/18135454
posted: 2022-12-13T20:29:07Z
last_edited: 2022-12-14T18:31:31Z
accepted: true
score: 2
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3f07419954f57ae487f2cc8372f5f940c335941035022c5716b94fb5c128d3b5
role: another answer on the same question, kept as context; not my work
---

# Answer by [constantstranger](https://stackoverflow.com/users/18135454) — 2022-12-13

Posted on Stack Overflow, <https://stackoverflow.com/a/74790535>, 2022-12-13, last edited 2022-12-14; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

As an alternative to the original answer (see below), here is a very straightforward way to do what OP asks:
```python
df_rates['Profit'] = df_profit.Profit.reindex(df_rates.columns[-1] - pd.to_timedelta(df_rates['Mins before time'], unit='min')).to_numpy()
```
Output:
```
   Mins before time  2012-03-31 23:45:00    Profit
0                 0               113.10  3504.664
1                 5               112.10       NaN
2                10               113.10       NaN
3                15               113.17  1215.760
4                20               103.17       NaN
5                25               133.17       NaN
6                30               101.39   -21.480
```
Explanation:
- create a Series of Timestamps by subtracting from the Timestamp label of the final column in df_rates (assumed to be of Timestamp type, otherwise wrap it in `pd.to_datetime()`) a Series of timedelta values created using the `Mins before time` column with units of minutes
- use `reindex` on df_profit to create a Series of profit figures that parallels the columns of df_rates and contains the `Profit` values from df_profit where the Timestamp labels in the df_profit index exactly match those in the Series of Timestamps created in the previous step, and NaN elsewhere
- convert that Series of profit figures (possibly including NaNs) to a numpy array with `to_numpy` and use it to initialize a new column labeled `Profit` (or whatever other label is desired) in df_rates.

----------
**Original answer:**

Here's a way to do it:
```python
df_rates = ( df_rates
    .set_index(df_rates.columns[-1] + pd.to_timedelta(-df_rates['Mins before time'], unit='min'))
    .join(df_profit).reset_index(drop=True) )
print(df_rates)
```
Output:
```
   Mins before time  2012-03-31 23:45:00    Profit
0                 0               113.10  3504.664
1                 5               112.10       NaN
2                10               113.10       NaN
3                15               113.17  1215.760
4                20               103.17       NaN
5                25               133.17       NaN
6                30               101.39   -21.480
```
Explanation
- set the index of df_rates to be the label of its final column (assumed to be of Timestamp type, otherwise wrap it in `pd.to_datetime()`) plus a Series of timedelta values equal to the `Mins before time` column with units of minutes
- use `join` with df_profit to add a `Profit` column with non-null values in rows with matching index values, and reset the index.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Newlearner](https://stackoverflow.com/users/19921895)** (2022-12-14): Thank you very much for the concise answer and explanation.
- **[Newlearner](https://stackoverflow.com/users/19921895)** (2022-12-14): Is there a way to loop through the code if I have multiple columns in df_rates with column name of various timestamps. And have the corresponding new column created after every column?
- **[constantstranger](https://stackoverflow.com/users/18135454)** (2022-12-14): Yes, that's certainly possible. You may want to post that as a new question.
- **[Newlearner](https://stackoverflow.com/users/19921895)** (2022-12-15): Sure, thank you.  Could you kindly check a similar question I have posted on (https://stackoverflow.com/questions/74814522/compare-a-timestamp-with-another-between-2-dataframes-and-populate-values-into-a?noredirect=1#comment132035000_74814522) but with slightly different answer expected?
