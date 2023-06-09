---
title: "How to loop over the div to extract the sentence in the paragraph from a webpage?"
site: stackoverflow
question_id: 76433775
answer_id: 76444181
url: https://stackoverflow.com/a/76444181
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-06-09T23:46:32Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/76444181/revisions
accepted: false
score: 0
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: cd9532f3f2191e897b07f64edc1b9f469d4b66b25dbc5e4a9355c9930a657492
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-06-09

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76444181>, 2023-06-09; score 0. Text as retrieved 2026-10-12.

As the error message indicates, `findAll` returns a `ResultSet` [which is like a list of elements] rather than a single element [as `find` might return], so you cannot apply `.find` to *your* `every_review`. Try it in a `for` loop, like

```py
for every_review in soup.findAll('shreddit-comment-tree', {'id':'comment-tree'}):
  for rev in every_review.findAll('div', {'class':'md pl-[28px] xs:pl-xl text-14'}):
    for d in rev.findAll('div', {'id':'-post-rtjson-content'}):
      print(d.p.text if d.p else '!EMPTY -post-rtjson-content!') ## JUST IN CASE
```
