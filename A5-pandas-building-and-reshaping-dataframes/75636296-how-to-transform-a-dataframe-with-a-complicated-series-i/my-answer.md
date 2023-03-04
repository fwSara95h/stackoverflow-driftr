---
title: "How to transform a DataFrame with a complicated series in a new DataFrame"
site: stackoverflow
question_id: 75636296
answer_id: 75636599
url: https://stackoverflow.com/a/75636599
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-04T15:17:27Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75636599/revisions
accepted: true
score: 1
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 10d3dbc2b1f01b7f9c63298f0463fd93bcd1d93100f12a910c725c29daa70420
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-04

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75636599>, 2023-03-04; **accepted**; score 1. Text as retrieved 2026-10-12.

There's probably a more elegant way to do this by applying [`pd.json_normalize`](https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html) to your original data, but I'll suggest a solution using [list comprehension](https://www.programiz.com/python-programming/list-comprehension) (and [`zip`](https://docs.python.org/3.3/library/functions.html#zip)).

If your current DataFrame is named [`tickets_df`][1], then you can try

```py
cashflows_df = pd.DataFrame([{'Ticket': tId, **{
    k: v for k, v in cfd.items() if k != 'TicketId'
}} for tId, cf in zip(
    # tickets_df['TicketId'], tickets_df['CashFlows']
    tickets_df.index, tickets_df['CashFlows'] # if TicketId is the index
) for cfd in cf['CashFlowDto']])
```

> [![op][2]][2]
> <sup>(I edited the `Type` field just to demonstrate that the rows are separate as they should be.)</sup>

  [1]: https://i.sstatic.net/bkg2y.png
  [2]: https://i.sstatic.net/oWpWV.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[pedrosjo](https://stackoverflow.com/users/20278443)** (2023-03-04): Nice, solved my problem bro.
