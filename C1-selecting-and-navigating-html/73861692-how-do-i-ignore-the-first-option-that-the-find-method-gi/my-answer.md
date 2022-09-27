---
title: "How do I ignore the first option that the find method gives me?"
site: stackoverflow
question_id: 73861692
answer_id: 73872040
url: https://stackoverflow.com/a/73872040
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-27T18:07:59Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73872040/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 24c71dcb1dfd9c54efa809c092ce89c1d3f9c1c264c4f7b99fd05bd891d75079
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-09-27

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73872040>, 2022-09-27; score 0. Text as retrieved 2026-10-12.

You can try 

    dateLabel = "Fecha de publicación" #copy label text EXACTLY
    response = root.find("label", string=dateLabel).findNext('input').get('value')

but you must make sure `dateLabel` is an **exact** match for the label text or use a suitable regex. Include input class in `findNext` if there might be more than one input tag after the label.

Or, if you know the (`index`), use `root.find_all(....)[index]` instead of just `find`
