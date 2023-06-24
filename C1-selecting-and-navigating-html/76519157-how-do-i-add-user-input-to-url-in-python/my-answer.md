---
title: "How do I add user input to url in python?"
site: stackoverflow
question_id: 76519157
answer_id: 76544374
url: https://stackoverflow.com/a/76544374
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-06-24T02:41:32Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/76544374/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 4db5b6825d9a1cad9a4a476b1e5fd73c2b36b64eae1ceaba926ea1e51dae99e4
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-06-24

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76544374>, 2023-06-24; score 0. Text as retrieved 2026-10-12.

The issue is in the base URL itself. You want either `f'https://indexsubtitle.com/subtitles/{find_movie}'` [for a specific page] or `f'https://indexsubtitle.com/?search={find_movie}'` [for search results]. You'll also want to replaces spaces with `-` or `+`....
