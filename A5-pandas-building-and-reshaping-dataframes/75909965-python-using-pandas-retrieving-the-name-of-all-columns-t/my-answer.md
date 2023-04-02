---
title: "Python using Pandas - Retrieving the name of all columns that contain numbers"
site: stackoverflow
question_id: 75909965
answer_id: 75910041
url: https://stackoverflow.com/a/75910041
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-02T03:53:54Z
last_edited: 2023-04-02T04:00:44Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75910041/revisions
accepted: false
score: 2
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1d7b9eae8a8a2730e47125f08666047334fae660d06fdad7fa35d3306e6a7ec2
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-02

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75910041>, 2023-04-02, last edited 2023-04-02; score 2. Text as retrieved 2026-10-12.

You can use [`.dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dtype.html) then [`.kind`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.kind.html) while filtering the the [column names](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html) with [list comprehension](https://www.programiz.com/python-programming/list-comprehension).

```py
# import pandas as pd
# df = pd.read_html('https://stackoverflow.com/questions/75909965')[0] # scraped your q

[c for c in df.columns if df[c].dtype.kind in 'iufc']
```

should return `['A', 'B', 'D']`. [Note that *`'iufc'`* covers signed and unsigned integers as well as real and complex floating-point numbers. Add `b` if you want to cover Booleans as well since they're a subclass of `int` in python....]

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Adrian](https://stackoverflow.com/users/6176440)** (2023-04-03): This is also a very interesting solution, I appreciate it.
