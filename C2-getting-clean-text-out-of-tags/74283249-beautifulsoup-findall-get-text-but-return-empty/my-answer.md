---
title: "BeautifulSoup findall get text but return empty"
site: stackoverflow
question_id: 74283249
answer_id: 74283516
url: https://stackoverflow.com/a/74283516
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-02T01:38:36Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74283516/revisions
accepted: false
score: 0
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d18e90e0e04502de2844d97c3cc1542e4e5652b3fade547ed7ca28952e491668
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-02

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74283516>, 2022-11-02; score 0. Text as retrieved 2026-10-12.

If nothing else, you can just use
```python
str(soup.find('style')).strip()[7:-8].strip()
```
to get the stylesheet as one string. If you want to know more about parsing the css, you might like to [check this out.](https://stackoverflow.com/a/11685846/12652373)
