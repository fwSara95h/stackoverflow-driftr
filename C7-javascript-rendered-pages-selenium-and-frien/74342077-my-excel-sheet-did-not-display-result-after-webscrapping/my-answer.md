---
title: "my excel sheet did not display result after webscrapping using selenium and export to excel"
site: stackoverflow
question_id: 74342077
answer_id: 74343150
url: https://stackoverflow.com/a/74343150
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-07T07:20:00Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74343150/revisions
accepted: false
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fe40fc881e4e7004be912dc0f69c584401d6e9b19e3050c95430fccac44a778e
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-07

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74343150>, 2022-11-07; score 0. Text as retrieved 2026-10-12.

[I am unfamiliar with just passing a string as the first argument (`by="xpath"` rather that `By.XPATH`); if it works for you, great, but otherwise you might want to check out the [documentation](https://selenium-python.readthedocs.io/locating-elements.html).]

The xpaths for `serialnumber` and `expirydate` might be the issue. When I inspected the page, I saw that they were inside `p` tags, not `div` tags. 

On another note, if there were multiple elements in `frame`, you'd just be repeatedly getting the first serial number and expiry date, it should instead be something like
```python
# from selenium.webdriver.common.by import By

    serialnumber = result.find_elements(By.XPATH, "//p[@class='service-tag mb-0 d-none d-lg-block']")
    expirydate = result.find_elements(By.XPATH, "//p[@class='warrantyExpiringLabel mb-0 ml-1 mr-1']")
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Chloe Chew](https://stackoverflow.com/users/20238176)** (2022-11-07): Hello! Thank you! Yes, i've import By , removed the For loop and continue using the same code, except i've added .text behind my serialnumber and expiry date. It worked!
