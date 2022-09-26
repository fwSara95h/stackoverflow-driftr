---
title: "Element not interactable while click() function is used in input type radio"
site: stackoverflow
question_id: 73856177
answer_id: 73856878
url: https://stackoverflow.com/a/73856878
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-26T16:04:45Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73856878/revisions
accepted: false
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3864e245ca0aedd5d6221967a21b8c2dd7ff28d2b97e61f9c8b699815bb4b131
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-09-26

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73856878>, 2022-09-26; score 0. Text as retrieved 2026-10-12.

Beautifulsoup just allows you to view the data, it doesn't allow interaction -  so the click function wouldn't work no matter which element you tried. 

For the selenium error, there are several possible reasons and potential solutions that are suggested in [this edureka thread][1]. I cannot pinpoint which of them might apply to your case without the actual link you're scraping from, but hopefully you'll find something helpful there.


  [1]: https://www.edureka.co/community/55217/resolve-elementnotinteractableexception-selenium-webdriver
