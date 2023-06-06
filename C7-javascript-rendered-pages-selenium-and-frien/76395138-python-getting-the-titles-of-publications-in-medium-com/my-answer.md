---
title: "Python - Getting the titles of publications in medium.com"
site: stackoverflow
question_id: 76395138
answer_id: 76416860
url: https://stackoverflow.com/a/76416860
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-06-06T16:56:58Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/76416860/revisions
accepted: false
score: 1
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: dc271ee82450a2aeddb0c56f2e0b5f72b7e8063cb9de01d944d72b78542012b6
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-06-06

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76416860>, 2023-06-06; score 1. Text as retrieved 2026-10-12.

You can try selecting the links to the articles (which also contain their titles) with `a[href][aria-label="Post Preview Title"]`. For example:

```py
        h2Sel = 'a[href][aria-label="Post Preview Title"] h2'
        elements = driver.find_elements(By.CSS_SELECTOR, h2Sel)
        for x in elements:
            print(x.text)
```
