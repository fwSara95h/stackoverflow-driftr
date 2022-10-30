---
title: "How to select element by class and get text?"
site: stackoverflow
question_id: 74249468
answer_id: 74251254
url: https://stackoverflow.com/a/74251254
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-30T07:32:49Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74251254/revisions
accepted: true
score: 0
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f164c700b4089b21cab1551c45158fcaddea3ca1354ef2eda84e37bacc94b327
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-30

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74251254>, 2022-10-30; **accepted**; score 0. Text as retrieved 2026-10-12.

Using find: 
```python
[t.get_text(strip=True) for t in soup.find_all(attrs={'class': 'sorting_1'})]
```
or if you're sure that's the only class for the tags you want:
```python
[t.get_text(strip=True) for t in soup.find_all(class_='sorting_1')]
```
or using select
```python
[t.get_text(strip=True) for t in soup.select('.sorting_1')]
```

<hr>

Any of the above should work; and if you're going to be working with BeautifulSoup, you should really familiarize yourself with [the documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and/or go through at least one [tutorial](https://www.dataquest.io/blog/web-scraping-python-using-beautiful-soup/).
