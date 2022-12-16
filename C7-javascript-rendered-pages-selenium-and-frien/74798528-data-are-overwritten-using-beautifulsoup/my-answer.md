---
title: "Data are overwritten using beautifulsoup"
site: stackoverflow
question_id: 74798528
answer_id: 74819089
url: https://stackoverflow.com/a/74819089
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-16T00:44:16Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74819089/revisions
accepted: true
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: [queue crawler (saveScrawlSess), saveScrawlSess]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a6793977757a105529a14aa064ced3f706b508d89075ef9b26f095479c88a1b6
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-16

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74819089>, 2022-12-16; **accepted**; score 0. Text as retrieved 2026-10-12.

Currently, you're clearing the `product` list at the beginning of each page loop - either move the `product=[]` line to before `for page in range(1,3)` OR indent the last two lines [with append mode - `df.to_csv('firm.csv', mode='a' )`] to get then inside the page loop; i.e., **the `product=[]` line and the `df...` lines should have the SAME indent level**.

(I don't recommend append mode btw, it's a bit annoying - if you use `header=False`, you won't have any headers [unless you write extra code to initialize the csv with them, like in `saveScrawlSess` in [this crawler](https://pastebin.com/TBtYja5D) ], but if you don't then the header row keeps getting repeated every few rows....)
