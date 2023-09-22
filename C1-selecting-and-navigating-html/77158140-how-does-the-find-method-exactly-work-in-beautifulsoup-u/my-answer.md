---
title: "how does the find method exactly work in BeautifulSoup using a LXML parser?"
site: stackoverflow
question_id: 77158140
answer_id: 77161033
url: https://stackoverflow.com/a/77161033
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-09-22T22:59:21Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/77161033/revisions
accepted: false
score: -1
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1e73ce0e6356140876d4b89b62e2eadd4ae2348d90d3a2a03865a34bef2d0518
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-09-22

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/77161033>, 2023-09-22; score -1. Text as retrieved 2026-10-12.

> ```py
> review = soup.find_all('article', itemprop = 'review') ## should be reviews!!
> for review in reviews:
> ```

I think you meant to write `reviews = soup.find_all('article', itemprop = 'review')` not `review=....` and that might be why `review.find` is behaving unexpectedly
