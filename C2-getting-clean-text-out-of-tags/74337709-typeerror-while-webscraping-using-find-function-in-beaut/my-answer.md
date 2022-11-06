---
title: "TypeError while webscraping using find function in BeautifulSoup"
site: stackoverflow
question_id: 74337709
answer_id: 74338260
url: https://stackoverflow.com/a/74338260
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-06T17:41:01Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74338260/revisions
accepted: false
score: 0
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6ea723ffba4b315b3e02b162ab978f526f8a6767d10b329be0541fbc403062b0
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-06

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74338260>, 2022-11-06; score 0. Text as retrieved 2026-10-12.

The line `job = job.text` is causing issues for the next line, because now `job` is just a string rather than a bs4 tag, so `.find` is [a different function](https://www.programiz.com/python-programming/methods/string/find) entirely.

Change that line to something like `jobTxt = job.text` (so that you can still use `job`) and then `print(jobTxt)` if that's what you're trying to print at the end of the loop.
