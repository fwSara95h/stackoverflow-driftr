---
title: "Hide Data Series on Google Chart by Clicking Legend"
site: stackoverflow
question_id: 73849443
answer_id: 73849693
url: https://stackoverflow.com/a/73849693
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-26T04:42:17Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73849693/revisions
accepted: false
score: 1
chapter: G1
chapter_title: "JavaScript / DOM one-offs"
cluster: javascript-dom
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c9707df44f26ec8b3d7f29768102925e4fac1bb579dd6b747a5d87c465df77ec
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-09-26

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73849693>, 2022-09-26; score 1. Text as retrieved 2026-10-12.

Since they're greyed out, maybe you could add a for-loop in the date slider's listener to go through all the series and hide the ones with *color='#CCCCCC'* again. Maybe re-drawing after changing the dates reset the visibilities.
