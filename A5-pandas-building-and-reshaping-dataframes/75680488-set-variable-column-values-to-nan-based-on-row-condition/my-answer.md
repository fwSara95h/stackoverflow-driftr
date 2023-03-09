---
title: "Set variable column values to nan based on row condition"
site: stackoverflow
question_id: 75680488
answer_id: 75680677
url: https://stackoverflow.com/a/75680677
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-09T05:15:42Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75680677/revisions
accepted: false
score: 1
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0848a8fd0b5eab54f377557cf699d8e699fd11ea42083908dc808503e84b4b5f
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-09

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75680677>, 2023-03-09; score 1. Text as retrieved 2026-10-12.

You could create new columns with slices of the current columns and then replace

```py
for i, cn in enumerate(df.columns,1): 
    df[cn] = [*[np.nan]*i, *df[cn].loc[i:]]
```

> [![op][1]][1]


  [1]: https://i.sstatic.net/XjPFx.png
