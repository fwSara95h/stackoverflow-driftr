---
title: "Why is Beautifulsoup's selector showing error while the Scrapy's response.css working absolutely fine?"
site: stackoverflow
question_id: 74620048
answer_id: 74635420
url: https://stackoverflow.com/a/74635420
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-30T23:47:42Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74635420/revisions
accepted: true
score: 1
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c005de4dc73c7ab70323fa3c0846818463d6b3e339cacfe3d2c29fd6f5fc5f45
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-30

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74635420>, 2022-11-30; **accepted**; score 1. Text as retrieved 2026-10-12.

bs4 [or rather [soupsieve](https://facelessuser.github.io/soupsieve/selectors/basic/)] doesn't like it when id selectors [`#id`] have hyphens (`-`) in them for some reason, but you can get around it by using attribute selector instead
```python
cont = soup.select(f'div[id="{d1}"]')
```
should work - give it a try.
