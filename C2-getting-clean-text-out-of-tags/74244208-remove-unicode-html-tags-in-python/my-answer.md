---
title: "Remove unicode HTML tags in Python"
site: stackoverflow
question_id: 74244208
answer_id: 74246118
url: https://stackoverflow.com/a/74246118
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-29T14:27:00Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74246118/revisions
accepted: false
score: 1
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bfb2668e06a862ae044c24f8f3eb0d79738e68b5ad98f2d9a2cfa5cec5330e2b
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-29

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74246118>, 2022-10-29; score 1. Text as retrieved 2026-10-12.

You can just encode as utf-8 before passing to BeautifulSoup (since it also accepts input in `bytes`, not just `str`) and then extracting the text: 
```python
# pasted your string excerpt to variable xstr: 
xstr = '"overview":"\u003cp style=\"margin: 0px 0px 20px; padding: 0px; line-height: 20px; outline: none !important; min-height: 1em; color: #333333; font-family: Arial, Helvetica, sans-serif, emoji; font-size: 14px; font-style: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: auto; text-indent: 0px; text-transform: none; white-space: normal; widows: auto; word-spacing: 0px; -webkit-text-size-adjust: auto; text-align: center;\"\u003e\u003cspan style=\"font-family: arial, helvetica, sans-serif;\"\u003e\u003cstrong\u003e\u003cspan style=\"font-size: 18pt; outline: none !important;\"\u003eWTS/VDI macOS\u003c/span\u003e\u003c/strong\u003e\u003c/span\u003e\u003c/p\u003e\n\u003chr\u003e\n\u003cp\u003e\u003cspan ......'

print(BeautifulSoup(xstr.encode('utf-8')).text)
```
output: `"overview":"WTS/VDI macOS`
