---
title: "How can i get values from 2 lists and put them into a dictionary in python"
site: stackoverflow
question_id: 74984177
answer_id: 75269053
url: https://stackoverflow.com/a/75269053
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-28T16:12:57Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75269053/revisions
accepted: false
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 28aa5ab851248fa06e3b3988e332482ac10927635d3cfdda6bbbee9fbc893598
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-28

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75269053>, 2023-01-28; score 0. Text as retrieved 2026-10-12.

As mentioned in the comments, you can't have duplicate keys in a dictionary; even your output snippet would just return `[{'Name': 'wally', 'Age': 55}]`

[![opret][1]][1]

---

However, **`{k: v for k, v in zip(list1, list2)}`** will return

```python
{'ben': 18, 'tim': 12, 'john': 34, 'wally': 55}
```

---

And **`[{'Name': n, 'Age': a} for n, a in zip(list1, list2)]`** will return

```python
[{'Name': 'ben', 'Age': 18},
 {'Name': 'tim', 'Age': 12},
 {'Name': 'john', 'Age': 34},
 {'Name': 'wally', 'Age': 55}]
```



  [1]: https://i.sstatic.net/RRibe.png
