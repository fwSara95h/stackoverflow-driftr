---
title: "TypeError: 'str' object is not callable beautifulsoup"
site: stackoverflow
question_id: 74198654
answer_id: 74248514
url: https://stackoverflow.com/a/74248514
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-29T20:15:55Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74248514/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 431233499a5eec308f91a440212cb7604dcbed578709beb9798aed8d497ea410
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-29

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74248514>, 2022-10-29; score 0. Text as retrieved 2026-10-12.

This might be easier to figure out if you share **which line** triggered this, but according to [this thread about the same error message](https://www.physicsforums.com/threads/very-basic-website-scraper-str-object-is-not-callable.984485/), 

> ...suggests that this can happen if you've defined a variable called str before running your script. Then python thinks you are referring to this variable and wonders why you are trying to call a variable

so the error might go away if you add
```python
str = None # in case str HASN'T been defined...
del str
```
somewhere before whichever line caused the error.
