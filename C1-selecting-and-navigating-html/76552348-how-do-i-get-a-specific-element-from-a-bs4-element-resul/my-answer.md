---
title: "How do I get a specific element from a bs4.element.ResultSet?"
site: stackoverflow
question_id: 76552348
answer_id: 76553683
url: https://stackoverflow.com/a/76553683
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-06-26T05:16:05Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/76553683/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7e71b4cd5840e2dade883b0e73d065d70d071f4b9f90501ce29332991281d311
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-06-26

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76553683>, 2023-06-26; score 0. Text as retrieved 2026-10-12.

> So I would like something like: [/Company/apple-hospitality-reit-inc, /Company/apple-in, /Company/maui-land-pineapple-co-inc, /Company/pineapple-energy-inc]

Using [`select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors-through-the-css-property) with [list comprehension](https://www.programiz.com/python-programming/list-comprehension):

```py
company_urls = [a['href'] for a in soup.select('a[href*="\/Company\/"]')]
```

You can do it with `find_all` as well, with a [`lambda`](https://www.programiz.com/python-programming/anonymous-function) expression for the `href` argument, but it feels a bit more clunky to me:

```py
company_urls = [a['href'] for a in soup.find_all('a', href=lambda h: h and '/Company/' in h)]
```

---

Of course, you can also filter the list comprehension with an `if` instead of using `lambda` in the `find_all`

```py
company_urls = [a['href'] for a in soup.find_all('a', href=True) if '/Company/' in a['href']]
```

which is the same as

```py
company_urls = [a['href'] for a in soup.select('a[href]') if '/Company/' in a['href'])]
```
