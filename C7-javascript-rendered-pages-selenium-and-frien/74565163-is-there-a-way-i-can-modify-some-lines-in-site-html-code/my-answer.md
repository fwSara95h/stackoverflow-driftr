---
title: "Is there a way I can modify some lines in site html code so it marks the checkbox?"
site: stackoverflow
question_id: 74565163
answer_id: 74565584
url: https://stackoverflow.com/a/74565584
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-24T19:41:55Z
last_edited: 2022-11-24T19:50:14Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74565584/revisions
accepted: true
score: 2
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f1c3d4ba84c10d707f613aa4e98d6dd9123065438dec0b6396b684e91f092a28
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-24

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74565584>, 2022-11-24, last edited 2022-11-24; **accepted**; score 2. Text as retrieved 2026-10-12.

You can't use `By.CLASS_NAME` here since it has no `class`.
You *can* use:

---

- [`By.CSS_SELECTOR`](https://selenium-python.readthedocs.io/locating-elements.html#locating-elements-by-css-selectors) to find by [CSS selectors](https://www.w3schools.com/cssref/css_selectors.php) 
```python
chbVal = '613' # in case you need be able to change this

(By.CSS_SELECTOR, f'label > input[type="checkbox"][value="{chbVal}"][checked=""]') # for checked

(By.CSS_SELECTOR, f'label > input[type="checkbox"][value="{chbVal}"]:not([checked])') # for unchecked
```

---

- or [`By.XPATH`](https://selenium-python.readthedocs.io/locating-elements.html#locating-by-xpath) to find by [Xpath](https://devhints.io/xpath)
```python
chbVal = '613' # in case you need be able to change this

(By.XPATH, f'//label/input[@type="checkbox"][@value="{chbVal}"][@checked=""]') # for checked

(By.XPATH, f'//label/input[@type="checkbox"][@value="{chbVal}"][not(@checked="")]') # for unchecked
```

---

**Note:** These are just based on the html snippet you've included - there might by parent elements with better identifiers that you need to include in your path/selector.

---

Also,
> Somehow in html code the checkbox doesn't have value

but [in your snippet][1] it *does* have `value`...? Anyway, the examples above include `value`, but you don't have to include them; you can even *exclude* them with `not(...)` as shown for `checked`. (Btw, `not(checked)`/`not(@checked)` should exclude elements that have a `checked` attribute at all, no matter what the value is.)


  [1]: https://i.sstatic.net/IDOGx.png
