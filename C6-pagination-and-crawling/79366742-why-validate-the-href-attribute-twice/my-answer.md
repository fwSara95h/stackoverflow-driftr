---
title: "Why validate the `href` attribute twice?"
site: stackoverflow
question_id: 79366742
answer_id: 79693292
url: https://stackoverflow.com/a/79693292
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2025-07-07T18:37:01Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/79693292/revisions
accepted: true
score: 1
chapter: C6
chapter_title: "Pagination and crawling"
cluster: scrape-pagination-crawling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9c4384479f55be60b1a898537175fcddbca8b5fbb3d52a2ce61406254bb5af11
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2025-07-07

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/79693292>, 2025-07-07; **accepted**; score 1. Text as retrieved 2026-10-12.

I'd agree that the `if 'href' in link.attrs:` is redundant given that `link` is from the results of `bsObj.findAll("a", href=re.compile("^(/wiki/)"))`. 

It was probably added as a habit or just to be extra careful or because it's a tutorial and it's a common error - forgetting to check whether an attribute or descendant exists before doing something with it, and then the whole thing breaks and you lose a good bit of data, etc.

I would have used something like `if link.get('href') in pages+[None]` if I wanted to keep the redundancy, just because I don't like unnecessary nesting. But also, recursive crawling [or recursive anything really] without an exit point is not ideal. Something queue-based might be better.
