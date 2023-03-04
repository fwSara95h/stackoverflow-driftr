---
title: "How to transform a DataFrame with a complicated series in a new DataFrame"
site: stackoverflow
question_id: 75636296
answer_id: 75636581
url: https://stackoverflow.com/a/75636581
author: "ouroboros1"
author_url: https://stackoverflow.com/users/18470692
posted: 2023-03-04T15:13:46Z
last_edited: 2023-03-04T16:09:43Z
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 474c1239ba1463c66747c0dc81eed55ecb9e5d365dd8ed7e675d243cda5533c5
role: another answer on the same question, kept as context; not my work
---

# Answer by [ouroboros1](https://stackoverflow.com/users/18470692) — 2023-03-04

Posted on Stack Overflow, <https://stackoverflow.com/a/75636581>, 2023-03-04, last edited 2023-03-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Here's one approach:
* First, use [`Series.tolist`](https://pandas.pydata.org/docs/reference/api/pandas.Series.tolist.html) on column `CashFlowDto` and use within [`pd.DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html). See this [SO answer](https://stackoverflow.com/a/63311361/18470692).
* Next, repeat the result *n* times (i.e. `n = len(df)`) using [`pd.concat`](https://pandas.pydata.org/docs/reference/api/pandas.concat.html), and make sure to put parameter `ignore_index` to `True`.
* Now, also get a repeat for `df['TicketId']`, for which we can use [`np.repeat`](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html), and keep only the values (using [`Series.to_numpy`](https://pandas.pydata.org/pandas-docs/version/0.24.0rc1/api/generated/pandas.Series.to_numpy.html); alternatively, reset `Series.index`).
* Finally, combine the new `df` and the repeats for `df['TicketId']`, using [`df.assign`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html).

```
n = len(df)
res = (pd.concat([pd.DataFrame(df['CashFlowDto'].tolist())]*n,ignore_index=True)
       .assign(TicketId=np.repeat(df.TicketId, n).to_numpy()))

res

   TicketId  Type  Amount  PercentualAmount MaturityDate PaymentDate
0         1  Amrt  560.61          0.049448   2023-07-10  2023-07-10
1         1  Amrt  552.05          0.048693   2023-08-10  2023-08-10
2         2  Amrt  560.61          0.049448   2023-07-10  2023-07-10
3         2  Amrt  552.05          0.048693   2023-08-10  2023-08-10
```
