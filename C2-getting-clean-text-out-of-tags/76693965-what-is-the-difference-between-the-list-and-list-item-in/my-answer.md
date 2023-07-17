---
title: "What is the difference between the list and list item in Beautiful Soup?"
site: stackoverflow
question_id: 76693965
answer_id: 76707256
url: https://stackoverflow.com/a/76707256
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-07-17T18:37:54Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/76707256/revisions
accepted: false
score: 0
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fe098015b3cdd7c7c31486354c667455ffc17d7bc4e82a942e5b3726d26aeb04
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-07-17

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76707256>, 2023-07-17; score 0. Text as retrieved 2026-10-12.

I think the weird escaped characters are whitespace characters, which is why you don't see them when printing. To minimize whitespace, you could try something like  <kbd>`' '.join(title.split())`</kbd> but note that it will also get rid of the line breaks and extra space at the beginning and end.
