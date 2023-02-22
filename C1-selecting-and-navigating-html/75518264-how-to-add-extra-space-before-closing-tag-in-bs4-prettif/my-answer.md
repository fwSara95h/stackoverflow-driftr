---
title: "how to add extra space before closing tag in bs4 prettify?"
site: stackoverflow
question_id: 75518264
answer_id: 75536103
url: https://stackoverflow.com/a/75536103
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-22T17:18:00Z
last_edited: 2023-03-05T23:18:09Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75536103/revisions
accepted: true
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8797210416c1add4f66e523c0b0127161befdb7ce151b6945d3601001ad88a2c
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-22

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75536103>, 2023-02-22, last edited 2023-03-05; **accepted**; score 0. Text as retrieved 2026-10-12.

If you pass `void_element_close_prefix=' /'` to `.HTMLFormatter` then the source tag should end with `... />` instead of `.../>`

```py
fmt = bs4.formatter.HTMLFormatter(indent=2, void_element_close_prefix=' /')
```

[![op][1]][1]


  [1]: https://i.sstatic.net/2HQs5.png
