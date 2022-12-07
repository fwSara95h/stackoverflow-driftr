---
title: "Find pattern in HTML elements with Selenium/BeautifulSoup"
site: stackoverflow
question_id: 74709027
answer_id: 74711529
url: https://stackoverflow.com/a/74711529
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-07T03:43:39Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74711529/revisions
accepted: false
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5350aaea0dfe368c7f7bcff0fc0ce2b7d6e48bdc6101ac907bcfbe5c60ee1299
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-07

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74711529>, 2022-12-07; score 0. Text as retrieved 2026-10-12.

You can try something like

```python
# heats = driver.find_elements(By.XPATH, '//*[starts-with(@id,"heat-")]')
heats = driver.find_elements(By.CSS_SELECTOR, '*[id^="heat-"]')
for heat in heats:
    names = heat.find_elements(By.XPATH, '/div/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/span')
    for n in names[:4]:
        name = n.text
```

or

```python
# heats = driver.find_elements(By.XPATH, '//*[starts-with(@id,"heat-")]')
heats = driver.find_elements(By.CSS_SELECTOR, '*[id^="heat-"]')
for heat in heats:
    for i in range(4):
        name = heat.find_element(By.XPATH, f'/div/div[2]/div[{i + 1}]/div[1]/div[1]/div/div[2]/div[1]/span').text
```

(I can't test these without more of your html so I'm not quite confident in any of them.)
