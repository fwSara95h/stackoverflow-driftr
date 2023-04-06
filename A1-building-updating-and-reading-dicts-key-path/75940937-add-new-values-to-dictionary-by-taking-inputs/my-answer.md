---
title: "Add new values to dictionary by taking inputs"
site: stackoverflow
question_id: 75940937
answer_id: 75949885
url: https://stackoverflow.com/a/75949885
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-06T13:06:58Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75949885/revisions
accepted: true
score: 1
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 75a7474c0c312f56aeaa317e3f5e59289bf8ec3f1b967c20fec6d99833917c60
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-06

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75949885>, 2023-04-06; **accepted**; score 1. Text as retrieved 2026-10-12.

As some comments have pointed out you're always emptying the dictionary out with *`preprocessing_dict = {}`* inside `add_preprocessing_operation`. You should initialize it outside the function, maybe as a [global](https://www.programiz.com/python-programming/global-keyword) variable.
