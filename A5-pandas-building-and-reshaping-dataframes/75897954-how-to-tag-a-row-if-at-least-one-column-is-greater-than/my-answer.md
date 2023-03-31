---
title: "How to tag a row if at least one column is greater than a specific value"
site: stackoverflow
question_id: 75897954
answer_id: 75898435
url: https://stackoverflow.com/a/75898435
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-31T12:16:01Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75898435/revisions
accepted: false
score: 0
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 910ea1f745da8cb77cace6afb89cd1be392f22a0e280c698322012be39d79096
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-31

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75898435>, 2023-03-31; score 0. Text as retrieved 2026-10-12.

You can try like this:

```py
# import pandas as pd
# df = pd.read_html('https://stackoverflow.com/questions/75897954')[0] # scraped from your q

valCols = [c for c in df.columns if c.startswith('Value')]
df['Flag'] = df[valCols].apply(lambda r: int(any(v>10 for v in r)), axis='columns')
```

> [![opdf][1]][1]

---

The reason for your error was that when you pass a function to [`.apply`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html), it's not called with the DataFrame as a parameter, but on each of its columns [or each of its rows, if you specify *`axis='columns'`* as above (or *`axis=1`* as you did)]. It might have worked if you had defined it as 

```py
# flag_df_new = lambda df_row: 1 if any(v>10 for v in df_row[1:]) else 0 ## same as
def flag_df_new(df_row):
    return 1 if any(v>10 for v in df_row[1:]) else 0
```


  [1]: https://i.sstatic.net/yFSs5.png
