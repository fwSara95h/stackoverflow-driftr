---
title: "fetching value between an anchor tag with bs4 or regex"
site: stackoverflow
question_id: 74270556
answer_id: 74270713
url: https://stackoverflow.com/a/74270713
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-01T01:50:14Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74270713/revisions
accepted: true
score: 1
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c5ee38acebe2851b10b074ff26ec0950df6e0808ae0257b3bdddbe55964d391e
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-01

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74270713>, 2022-11-01; **accepted**; score 1. Text as retrieved 2026-10-12.

It's called the text content of a tag. As one of commenter mentioned, you can use `.text`, but I personally prefer `.get_text()` [which actually gets called to generate `.text` anyway] because it lets you add separators for keeping texts from multiple inline elements getting smushed together. You can check out the [documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#get-text) for more examples and options.
