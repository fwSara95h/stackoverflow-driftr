---
title: "Why does same code outputs different values?"
site: stackoverflow
question_id: 75600606
answer_id: 75639198
url: https://stackoverflow.com/a/75639198
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-04T23:00:43Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75639198/revisions
accepted: false
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e11939495e996875e4fa4c142ec8d2fd0d70b300c2f89bb9722fb30c09185262
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-04

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75639198>, 2023-03-04; score 0. Text as retrieved 2026-10-12.

Calling `f(*r)` is similar to calling `f(**dict(zip(['x', 'y', 'z', 'w'], r)))` [or `f(**dict(zip('xyzw',r)))`, or `f(x=r[0], y=r[1], z=r[2], w=r[3])`], but `p` has the argument names shifted around every loop; so you need to `zip` with `p`, otherwise you'll be doing the same thing for every `p`, and the outermost loop becomes entirely redundant.
