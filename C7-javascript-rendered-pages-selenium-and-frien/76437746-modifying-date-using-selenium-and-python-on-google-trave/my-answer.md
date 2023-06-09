---
title: "Modifying date using Selenium and Python on Google Travel website"
site: stackoverflow
question_id: 76437746
answer_id: 76440789
url: https://stackoverflow.com/a/76440789
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-06-09T13:33:10Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/76440789/revisions
accepted: true
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2f41c17d25cf09980213e1af17d9b7daada63cbe8092f52220798ccd989ccc9d
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-06-09

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76440789>, 2023-06-09; **accepted**; score 0. Text as retrieved 2026-10-12.

<sub>[You *could* keep clicking the next-day button until the value matched the desired check-in date, but I can see why you might want to avoid such an inefficient method...]</sub>

> ```py
>         checkinElement.send_keys(search_query[j])
> ```

There are a couple of issues with what you're trying to do here:

- first off, you probably want **`checkin_query[j]`** and the *`search_query`* was just a typo...
- when I tried your code, it did input your value, but it added onto whatever was already there, so you need to clear the field first
  - unfortunately, `checkinElement.click()`+`checkinElement.clear()` didn't seem to be working [although you can give it a try - it could be a version problem...]

  So I tried using `Keys` instead and that worked for me
  ```py
  # from selenium.webdriver.common.keys import Keys

          checkinElement.send_keys(Keys.CONTROL, "a")
          checkinElement.send_keys(Keys.BACKSPACE)
          checkinElement.send_keys(checkin_query[j])
  ```
