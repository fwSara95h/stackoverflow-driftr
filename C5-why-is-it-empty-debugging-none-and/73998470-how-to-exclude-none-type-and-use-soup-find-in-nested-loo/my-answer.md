---
title: "How to exclude \"None\" type and use soup.find() in Nested Loops in Python?"
site: stackoverflow
question_id: 73998470
answer_id: 74018230
url: https://stackoverflow.com/a/74018230
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-10T16:49:25Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74018230/revisions
accepted: false
score: 0
chapter: C5
chapter_title: "Why is it empty? Debugging None and []"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f6cb49ce9acd65c1f04a7bcc12a38385f794f677bb016a27d8a97cde5f91d42f
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-10

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74018230>, 2022-10-10; score 0. Text as retrieved 2026-10-12.

If `soup.find` is giving NoneType error, add **before** it:

```python 
if soup is None or soup.find(id=j):
    continue 
```

that should allow you to skip both the potential AttributeError and when id can't found.
