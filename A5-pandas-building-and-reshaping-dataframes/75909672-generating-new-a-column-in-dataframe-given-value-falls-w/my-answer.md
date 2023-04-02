---
title: "Generating new a column in dataframe given value falls within a certain range of another column value"
site: stackoverflow
question_id: 75909672
answer_id: 75909789
url: https://stackoverflow.com/a/75909789
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-02T02:16:33Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75909789/revisions
accepted: false
score: 2
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5c0cb49cc7305c253832d56dd02d936eb802c16308425c2027d83738e313bd59
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-02

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75909789>, 2023-04-02; score 2. Text as retrieved 2026-10-12.

This shouldn't take much longer than maybe 2x the time it took when you checked if the columns matched (as int):

```py
range_limit = 2

lower_limits = df['B'] - range_limit
upper_limits = df['B'] + range_limit
df['Eq'] = ((lower_limits < df['A']) & (df['A'] < upper_limits)).astype(int)

# df['Eq'] = (((df['B'] - 2) < df['A']) & (df['A'] < (df['B'] + 2))).astype(int)
```

[It took about 0.1s on colab.]
