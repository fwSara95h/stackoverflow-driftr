---
title: "How to specify an class NOT to select with BeautifulSoup 4"
site: stackoverflow
question_id: 75621267
answer_id: 75643095
url: https://stackoverflow.com/a/75643095
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-05T14:56:27Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75643095/revisions
accepted: true
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f90ca58eaeb89fbd3833cb54d2098ef212f46875e05d34b4326d87316a05578f
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-05

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75643095>, 2023-03-05; **accepted**; score 0. Text as retrieved 2026-10-12.

Use 

```py
bs.select('[href*="str"]:not(.footer-wikiwalk-nav)')
``` 

like Barmar suggested [see the [pseudo-classes section](https://facelessuser.github.io/soupsieve/selectors/pseudo-classes/#:not) of the soupsieve docs for more details]. 

You could also use 

```py
bs.find_all(href=lambda h: h and "str" in h, class_= lambda c: 'footer-wikiwalk-nav' not in c.split())
```

(but `select` is probably preferable...)

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[hc_dev](https://stackoverflow.com/users/5730279)** (2023-03-06): Beautiful Soup since version 4.7 supports [CSS-selectors via _SoupSieve_ library](https://beautiful-soup-4.readthedocs.io/en/latest/#css-selectors).  The [_negation_ psuedo-class `:not(X)`](https://drafts.csswg.org/selectors-3/#negation) exists since CSS 3 (Selectors Level 3, recommended 2018).
- **me** (2023-03-06): @hc_dev thanks? since op was already using `select` I assumed they know how `select` basically works...
- **[hc_dev](https://stackoverflow.com/users/5730279)** (2023-03-06): It's not about this question only, but for all future visitors. They should know why SoupSieve is mentioned and which BS-version to use or that other standard CSS selectors are supported as well.
