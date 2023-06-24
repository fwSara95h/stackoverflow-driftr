---
title: "How to deal with variations in web pages while web scrapping using Beautiful Soup"
site: stackoverflow
question_id: 76512508
answer_id: 76544401
url: https://stackoverflow.com/a/76544401
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-06-24T02:57:01Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/76544401/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f6afd1823a637e24b800cbd5c4f1e1219ac65d5172d5e4812d6215ca175b8715
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-06-24

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76544401>, 2023-06-24; score 0. Text as retrieved 2026-10-12.

Consider [using selectors](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors-through-the-css-property), particularly pseudo classes like [`:is`](https://facelessuser.github.io/soupsieve/selectors/pseudo-classes/#:is) or [`:where`](https://facelessuser.github.io/soupsieve/selectors/pseudo-classes/#:where), followed by if-else:

```py
MRP = soup.select_one('span:is(.a-price.a-text-price.a-size-base, .a-price.a-text-price) span')
MRP = MRP.text if MRP else ''
```

---

Although, you could just search only for the shared classes:

```py
MRP = soup.select_one('span.a-price.a-text-price span')
MRP = MRP.text if MRP else ''
```
