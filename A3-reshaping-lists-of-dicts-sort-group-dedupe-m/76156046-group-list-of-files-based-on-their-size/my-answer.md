---
title: "Group list of files based on their size"
site: stackoverflow
question_id: 76156046
answer_id: 76448771
url: https://stackoverflow.com/a/76448771
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-06-11T01:48:59Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/76448771/revisions
accepted: false
score: 0
chapter: A3
chapter_title: "Reshaping lists of dicts: sort, group, dedupe, merge"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3b1a6d701b4f8982114fbb7dfbc5ca692b73ac7f38c6c99c38bc0ac44161f549
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-06-11

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76448771>, 2023-06-11; score 0. Text as retrieved 2026-10-12.

Try something like

```py
# import os

max_group_size = 100000
docs = ['Doc3.pdf', 'Doc4.pdf', 'Doc2.pdf', 'Doc5.pdf', 'Doc1.pdf', 'Doc6.pdf']

grouped_docs, cur_size_total = [[]], 0
for d in docs:
    cur_doc_size = os.path.getsize(d)

    if (cur_size_total + cur_doc_size) > max_group_size:
        cur_size_total = 0
        grouped_docs.append([])

    grouped_docs[-1].append(d)
    cur_size_total += cur_doc_size
```

`grouped_docs` should look like your desired output
