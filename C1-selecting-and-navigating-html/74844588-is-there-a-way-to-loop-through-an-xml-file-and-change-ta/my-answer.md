---
title: "Is there a way to loop through an xml file and change tags to make them unique?"
site: stackoverflow
question_id: 74844588
answer_id: 74845261
url: https://stackoverflow.com/a/74845261
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-19T00:11:50Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74845261/revisions
accepted: true
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2a7cceb2461c5e0290b1dd346565a11c7301a107688db0ce4f9f15ea2494766b
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-19

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74845261>, 2022-12-19; **accepted**; score 0. Text as retrieved 2026-10-12.

Try like this

```python
tagListPairs = [(['stu:studentscreening'], ['sti:name'])]
for parentTags, enumTags in tagListPairs:
    for p in soup.find_all(parentTags):
        for name in enumTags:
            for i, t in enumerate(p.find_all(name)):
                t.name = f'{t.name}{i}'
```

`tagListPairs` should be in the format *`[(parentTags_1, enumTags_1), (parentTags_2, enumTags_2),....(parentTags_n, enumTags_n)]`* and both `parentTags` and `enumTags` should be a list of of tag names.
