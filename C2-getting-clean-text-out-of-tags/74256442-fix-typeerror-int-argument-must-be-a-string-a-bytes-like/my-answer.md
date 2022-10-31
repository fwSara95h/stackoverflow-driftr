---
title: "Fix TypeError: int() argument must be a string, a bytes-like object or a number, not 'Response'"
site: stackoverflow
question_id: 74256442
answer_id: 74257730
url: https://stackoverflow.com/a/74257730
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-31T00:34:53Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74257730/revisions
accepted: false
score: 1
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 34efd9edfc0633db003e019cc414eb16824d4625a64218837d668ac96ef13308
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-31

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74257730>, 2022-10-31; score 1. Text as retrieved 2026-10-12.

Don't use the same variable name for multiple variables. 

Change this 
```python 
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
```
to
```python 
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
```
or something because you're already using `page` for counting pages/chapters
