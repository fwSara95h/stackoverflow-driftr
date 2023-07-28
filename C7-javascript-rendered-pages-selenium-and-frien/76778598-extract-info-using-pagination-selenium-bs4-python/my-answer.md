---
title: "Extract info using pagination- selenium bs4 python"
site: stackoverflow
question_id: 76778598
answer_id: 76789943
url: https://stackoverflow.com/a/76789943
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-07-28T17:35:05Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/76789943/revisions
accepted: true
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: [paginated scraper]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ca833b97d16e724b3f50a0bdabf33ef016178d2c1552d45666610169d44cdb30
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-07-28

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76789943>, 2023-07-28; **accepted**; score 0. Text as retrieved 2026-10-12.

Generally, the logic I use for pagination is

```py
while True:
    ## PAGE SCRAPING CODE [ie, your current code]
    
    ## SEARCH FOR NEXT PAGE [button/link]
    ### IF NEXT PAGE --> click button or go to link
    ### NO NEXT PAGE --> BREAK
```

If you included the link you're trying to scrape, I might be able to give you a more specific answer. For example, [this](https://pastebin.com/d21q6mZ2) is a function I often use to scrape paginated data, although it's not meant to be for scrollable pages....
