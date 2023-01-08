---
title: "Beautiful soup findAll returns empty list on this website?"
site: stackoverflow
question_id: 75050882
answer_id: 75051095
url: https://stackoverflow.com/a/75051095
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-08T20:36:26Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75051095/revisions
accepted: false
score: 0
chapter: C5
chapter_title: "Why is it empty? Debugging None and []"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b07ad8ae8e7ad5d90492ff764ff00dfaf13ac8ff105e98eb7ef0dd4c0d539e57
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-08

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75051095>, 2023-01-08; score 0. Text as retrieved 2026-10-12.

> ```python
> officials = soup.findAll("table",{"id":"property-history"})
> ```

On browser, I don't see a `table` with `id="property-history"` - but there *is* [a `div` with that `id`][1], so maybe you can instead get the data you want through

```python
officials = soup.find_all("div", {"id":"property-history"})
```

<sub>Btw, the only `table` I could find while inspecting the page was [inside the map][2], and I don't think it holds any useful information for you.</sub>


  [1]: https://i.sstatic.net/iCSzt.png
  [2]: https://i.sstatic.net/K0Brp.png
