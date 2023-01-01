---
title: "replace function to remove \"\\\" in text"
site: stackoverflow
question_id: 74964057
answer_id: 74973318
url: https://stackoverflow.com/a/74973318
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-01T06:06:28Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74973318/revisions
accepted: false
score: 0
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: abaecb0498a70af1f87627b7c4954b939bcdbd7052bb8fba001d0cd25cfc404e
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-01

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74973318>, 2023-01-01; score 0. Text as retrieved 2026-10-12.

Escape the backslash as well

```python
str(video).replace('\\', '')
```
