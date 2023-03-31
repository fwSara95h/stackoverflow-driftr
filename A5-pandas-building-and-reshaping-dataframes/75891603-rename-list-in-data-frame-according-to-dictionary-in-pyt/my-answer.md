---
title: "rename list in data frame according to dictionary in Python"
site: stackoverflow
question_id: 75891603
answer_id: 75896900
url: https://stackoverflow.com/a/75896900
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-31T09:30:43Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75896900/revisions
accepted: false
score: 0
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 4fbe830e6edcff94076b135ab50d5662c390af649c4b026b06a3695bc76671db
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-31

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75896900>, 2023-03-31; score 0. Text as retrieved 2026-10-12.

You can try with [`.get`](https://www.programiz.com/python-programming/methods/dictionary/get) in something like 

```py
getSingle = lambda l: l[0] if isinstance(l,list) and len(l)==1 else l
getName = lambda x: ','.join([getSingle(dict_name.get(c,c)) for c in x.split(',')])
for_ag_pivot['name_cod'] = for_ag_pivot['cod_last'].apply(getName)
```

If `dict_name` only contains values that are single-item lists, you don't need `getSingle` and `getName` can just be <kbd>`lambda x: ','.join([dict_name.get(c,[c])[0] for c in x.split(',')])`</kbd>.
