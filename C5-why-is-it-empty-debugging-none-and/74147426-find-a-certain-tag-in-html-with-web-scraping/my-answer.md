---
title: "Find a certain tag in HTML with web scraping"
site: stackoverflow
question_id: 74147426
answer_id: 74248353
url: https://stackoverflow.com/a/74248353
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-29T19:50:07Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74248353/revisions
accepted: false
score: 0
chapter: C5
chapter_title: "Why is it empty? Debugging None and []"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a52c9f6c7618befa2431a5fdff624d26ce53836c4f50b19584df2501fc603775
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-29

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74248353>, 2022-10-29; score 0. Text as retrieved 2026-10-12.

As the error message is saying, you can't run `find` on a list directly - you have to run it on each item

If you want to print '1' only if *none of them* have heading row use:
```python
if not [s for s in sal_play if s.find('tr', class_='thead')]: 
    print('1')
```
or if you want to print '1' as long *some* of them *don't* have a heading row use: 
```python
if [s for s in sal_play if s.find('tr', class_='thead') is None]: 
    print('1')
```

By the way, if a tag does not exist, `find_all` will return an empty list (`[]`) and  `find` will return `None`, so `if ...find_all(....) is None: do x` will pretty much make sure x never happens....
