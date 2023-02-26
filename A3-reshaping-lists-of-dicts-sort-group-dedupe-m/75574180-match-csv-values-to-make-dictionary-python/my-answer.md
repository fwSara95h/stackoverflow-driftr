---
title: "Match CSV Values to Make Dictionary Python"
site: stackoverflow
question_id: 75574180
answer_id: 75574315
url: https://stackoverflow.com/a/75574315
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-26T18:56:13Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75574315/revisions
accepted: false
score: 0
chapter: A3
chapter_title: "Reshaping lists of dicts: sort, group, dedupe, merge"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2b6ca6c58a9aa150bb85d7de6e78dee4226d8f000b03921fb019e6a76801a8a9
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-26

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75574315>, 2023-02-26; score 0. Text as retrieved 2026-10-12.

You were pretty close - <kbd>`dict(zip(*[data[col] for col in data.columns]))`</kbd> would have worked, but it's probably better to be more specific when you [`zip`](https://docs.python.org/3.3/library/functions.html#zip) the two columns together so that they become a list of key-value pairs that can be converted into a dictionary:

```py
wordFreq = dict(zip(data['word'], data['count'])) ## same as:
# wordFreq = {k:v for k,v in zip(data['word'], data['count'])}
```

---

Or you could make use of the [`<DataFrame>.to_dict`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html) function like 

```py
wordFreq = dict(data.to_dict('split')['data'])
```

Although, if you had more than two columns (or if they were in a different order), you'd need to specify which column to use for keys and which for values:

```py
wordFreq = dict(data.set_index('word')['count']) ## series with index ## OR
# wordFreq = dict(data[['word', 'count']].to_dict('split')['data']) ## list of lists
```
