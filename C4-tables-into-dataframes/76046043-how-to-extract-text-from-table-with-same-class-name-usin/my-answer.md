---
title: "how to extract text from table with same class name using BeautifulSoup?"
site: stackoverflow
question_id: 76046043
answer_id: 76059273
url: https://stackoverflow.com/a/76059273
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-19T22:34:25Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/76059273/revisions
accepted: false
score: 0
chapter: C4
chapter_title: "Tables into DataFrames"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 88f4b36936dbf4d9524f1f70ba4ca8394a902e01057cb55e8342419e5aeffb94
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-19

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76059273>, 2023-04-19; score 0. Text as retrieved 2026-10-12.

> ```py
>         type_of_traveller=Reviewer.find("tr", class_="review-rating-header type_of_traveller")
> ```

There are no `tr` tags with that class on that page - you probably want the **`td`** tags with that class.

[![td not tr][1]][1]

---

<br>

Just change the line to 

```py
        type_of_traveller=Reviewer.find("td", class_="review-rating-header type_of_traveller")
```

and it should be fine after that.


  [1]: https://i.sstatic.net/bhy8D.png
