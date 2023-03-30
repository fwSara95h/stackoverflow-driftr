---
title: "When using BeautifulSoup to scrape Ebay, I get the wrong price for a listing"
site: stackoverflow
question_id: 75883573
answer_id: 75884306
url: https://stackoverflow.com/a/75884306
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-30T05:04:42Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75884306/revisions
accepted: true
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b1f7e94829a63c80e73997349c84f4599376527ccb38a182d810101d85e4deb8
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-30

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75884306>, 2023-03-30; **accepted**; score 0. Text as retrieved 2026-10-12.

The $20 `span` is also on the page but inside a hidden element
[![hidden span][1]][1]

<br>

---

<br>

If you want the price from the first search result, I suggest using [`.select_one`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors)<sup>**([view example][2])**</sup> like

```py
print(soup.select_one('ul.srp-results li span.s-item__price'))
```

which is effectively the same as 

```py
print(soup.find(lambda s: s.name=='span' and 's-item__price' in s.get('class',[]) and s.find_parent(lambda p: p.name=='li' and p.find_parent('ul', {'class':'srp-results'}))))
```

[but `select` is obviously much simpler].




  [1]: https://i.sstatic.net/jUqmg.png
  [2]: https://i.sstatic.net/tVXit.png
