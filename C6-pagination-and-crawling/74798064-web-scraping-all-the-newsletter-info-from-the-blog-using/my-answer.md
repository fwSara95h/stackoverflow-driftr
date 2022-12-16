---
title: "Web scraping all the newsletter info from the blog using BeautifulSoup"
site: stackoverflow
question_id: 74798064
answer_id: 74819561
url: https://stackoverflow.com/a/74819561
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-16T02:24:14Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74819561/revisions
accepted: false
score: 1
chapter: C6
chapter_title: "Pagination and crawling"
cluster: scrape-pagination-crawling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 70570a88681656e1ecc7b8b086ca3538b8bdf733313f972ef6f6148fc80e5e2c
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-16

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74819561>, 2022-12-16; score 1. Text as retrieved 2026-10-12.

> `    page1_df = pd.concat(page1_df,pages_df)`

[`.concat`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html) expect a *list* of DataFrames to be passed as the main argument, so the correct usage would be 

```python
    page1_df = pd.concat([page1_df,pages_df])
```

---

However, my preferred approach would be to collect all the DataFrames in a list and then to concatenate them at the end [outside the loop].

```python
pgdfList = [page1_df]
# for page in page_urls:
    ##### SCRAPE AND EXTRACT FOR dict_2 ##### 

    pgdfList.append(pd.DataFrame(dict_2))

page1_df = pd.concat(pgdfList)
print(page1_df)
```
