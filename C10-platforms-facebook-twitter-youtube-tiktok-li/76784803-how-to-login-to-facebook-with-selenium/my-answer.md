---
title: "How to login to Facebook with Selenium?"
site: stackoverflow
question_id: 76784803
answer_id: 76789908
url: https://stackoverflow.com/a/76789908
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-07-28T17:25:05Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/76789908/revisions
accepted: false
score: 0
chapter: C10
chapter_title: "Platforms: Facebook, Twitter, YouTube, TikTok, LinkedIn, Glassdoor"
cluster: scrape-social-platforms
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 871a66e96e05dd362b65f4aa9f7af70e901bed99ec5ac41b84460c31cff37503
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-07-28

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76789908>, 2023-07-28; score 0. Text as retrieved 2026-10-12.

You  might find [this article/tutorial](https://www.askpython.com/python/examples/python-automate-facebook-login) helpful for your issue.

I think the main problem is 

> ```py
>     email_input = driver.find_element("email")
>     password_input = driver.find_element("pass")
> ```

you should be using something like 

```py
# from selenium.webdriver.common.by import By

    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "pass")
```

See the section on [Navigating](https://selenium-python.readthedocs.io/navigating.html) a page in the documentation for more details and examples.
