---
title: "How to solve \"Move target out of bounds\" Selenium error?"
site: stackoverflow
question_id: 75011359
answer_id: 75011988
url: https://stackoverflow.com/a/75011988
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-04T22:22:36Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75011988/revisions
accepted: false
score: 1
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fb6b5dbe37de42d05feb09625632c280e744cbd70fe661f0c90ed97ff435f3aa
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-04

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75011988>, 2023-01-04; score 1. Text as retrieved 2026-10-12.

I have no idea *why*, but **trying to click twice** works for me. [I still get the same error if I try to click twice with `ActionChains`, and I'm not familiar enough with `ActionChains` to try to fix that; my usual approach is to use `.execute_script` to scroll to the element with JavaScript and then just apply `.click()` to the element, so that's what I've done below.]

```python
while True:
    try:
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Load More Listings')]")))

        # ActionChains(driver).move_to_element(element).click().perform()
        driver.execute_script('arguments[0].scrollIntoView(false);', element)
        try: element.click() # for some reason, the 1st click always fails
        except: element.click() # but after the 1st attempt, the 2nd click works...

    except Exception as e:
        print (e)
        break
```
