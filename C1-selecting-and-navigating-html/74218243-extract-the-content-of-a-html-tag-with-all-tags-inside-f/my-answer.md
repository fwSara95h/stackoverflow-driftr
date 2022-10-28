---
title: "extract the content of a html tag with all tags inside from beautifulsoup"
site: stackoverflow
question_id: 74218243
answer_id: 74235005
url: https://stackoverflow.com/a/74235005
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-28T11:52:41Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74235005/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 464a4d43d75e9f271e1a58e1b640b7eeb4bc5c14bb4c2ce5f1b5591840403623
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-28

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74235005>, 2022-10-28; score 0. Text as retrieved 2026-10-12.

TIL about `soup.find("td").decode_contents()` method, and that does seem like the simplest and best method, but even before,  there were several ways to get the "innerHTML".

Since you already noticed the `contents `
```python
''.join(soup_object.contents)
```
or, since we know prettify produces a certain format,
```python 
'\n'.join(soup_object.prettify().split('\n')[1:-1])
```
although I will admit that this is rather like using regex after all...

<hr>

Btw, `find()` is pretty much the same as `find_all()[0]` - wasn't sure you knew, but I find using just `find()` much more convenient in these situations
