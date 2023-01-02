---
title: "meet a problem when I used the a:nth-of-type(n) syntax"
site: stackoverflow
question_id: 74983655
answer_id: 74987691
url: https://stackoverflow.com/a/74987691
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-02T22:49:31Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74987691/revisions
accepted: true
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3e6a1c62fa99f2054dcd36e8331e8beb459676e2e3e0edf9de04ac23b3d95afe
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-02

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74987691>, 2023-01-02; **accepted**; score 0. Text as retrieved 2026-10-12.

> Could you tell me what happened?

There are only 4 `a` tags that are next-sibling to `p` tags. The last two `a` tags are *inside* the `p.introduce` element and have no previous-sibling `p` tags.

`soup.select('a:nth-of-type(1)')` would return 
```html
[<a href="http://c.biancheng.net/python/" id="link1">2023 is the new year</a>,
 <a href="http://c.biancheng.net/view/8066.html" id="link5">best</a>]
```

and `soup.select('a:nth-of-type(2)')` would return 
```html
[<a href="http://c.biancheng.net/c/" id="link2">hope you will be better</a>,
 <a href="http://c.biancheng.net/view/8092.html" id="link6">wishes</a>]
```

`html_doc` does not contain any `a:nth-of-type(5)` or `a:nth-of-type(6)` elements and contains only 4 `p~a` elements.
[![opex][1]][1]


  [1]: https://i.sstatic.net/NucCT.png
