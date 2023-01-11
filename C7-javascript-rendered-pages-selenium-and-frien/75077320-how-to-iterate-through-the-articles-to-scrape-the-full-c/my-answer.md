---
title: "How to iterate through the articles to scrape the full content?"
site: stackoverflow
question_id: 75077320
answer_id: 75079960
url: https://stackoverflow.com/a/75079960
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-11T08:09:44Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75079960/revisions
accepted: true
score: 2
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e54b35b582aa4badf0580dd096c21523b4c8a81eed3122f81d13629955899a53
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-11

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75079960>, 2023-01-11; **accepted**; score 2. Text as retrieved 2026-10-12.

> I see that I would need to click into each article return to previous page and continue to the next article

Not necessarily. Instead, you could just gather all links into a list that you can loop through and scrape.

```python
# while....[ load more ]
article_links = driver.find_elements(By.CSS_SELECTOR, "div.row div.row h5>a[href]")
article_links = list(set([l.get_attribute('href') for l in article_links])) ## set <-> unique

for url in article_links:
    driver.get(url)
    ### SCRAPE ARTICLE ###
```

**Note:** I can't find any elements with selector `.card-deck > .card`, but `div.row.feature-items` or [excluding thumbnail area] `div.row div.row` seems to work for article containers.

---

Btw, about 

> ```python
>         driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#main-content > div.wrapper.clearfix > div.col-a.pull-left > section.widget-area-2.pull-right > div > div > div.row > div > button'))))
> ```

Simply `button.load-mores:has(+a.load-more-basic)` [or even just **`button.load-mores`**] should be enough to select the load-more button.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[krsnbcd](https://stackoverflow.com/users/14322290)** (2023-01-11): Thanks so much! This saves me a lot of time, can't thank you enough for this.
