---
title: "How do I apply table class criteria in a web-scraper through python?"
site: stackoverflow
question_id: 74366039
answer_id: 74367438
url: https://stackoverflow.com/a/74367438
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-08T21:38:09Z
last_edited: 2022-11-09T06:02:50Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74367438/revisions
accepted: true
score: 1
chapter: C4
chapter_title: "Tables into DataFrames"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 43718e18ae3ca16ca3021549143216317abd4d7874225372714dab0d0b0210dc
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-08

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74367438>, 2022-11-08, last edited 2022-11-09; **accepted**; score 1. Text as retrieved 2026-10-12.

You can just add the table to the selector in `select`
```python
tLinkSel = 'table.table-main.only12.js-nrbanner-t a[href^="/tennis"]:has(strong)'
matchlist = set('https://www.betexplorer.com'+a.get('href') for a in soup.select(tLinkSel))
```
although, I have to mention that I did not see any difference in the results when searching in dev tools, but this will limit the links to only those in the table.

<hr>

**Additional EDIT:**

You can target specific dates with the `data-dt` attribute of the rows [`tr`]; for example, for Nov 2, 2022, you can set
```python
tLinkSel = 'tr[data-dt^="2,11,2022,"] a[href^="/tennis"]:has(strong)'
```
