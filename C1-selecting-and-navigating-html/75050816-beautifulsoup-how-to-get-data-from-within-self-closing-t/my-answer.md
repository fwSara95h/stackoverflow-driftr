---
title: "beautifulsoup - how to get data from within self closing tag"
site: stackoverflow
question_id: 75050816
answer_id: 75051145
url: https://stackoverflow.com/a/75051145
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-08T20:44:32Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75051145/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fe81d6eac69cf016d42a6715d60345f359be0e16e1a621090cdf36a9c1b9db01
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-08

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75051145>, 2023-01-08; score 0. Text as retrieved 2026-10-12.

I don't think it should make a difference that it's a self-closing tag in this case. The same methods should still be applicable. (Any of the methods in the comments should also work as an alternative.)

```python
nonceInp = soup.select_one('input[name="nonce"]')
# nonceInp = soup.find('input', {'name': 'nonce'})

if nonceInp:
    nonceVal = nonceInp['value'] 
    # nonceVal = nonceInp.attrs['value'] 
    # nonceVal = nonceInp.get('value') 
    # nonceVal = nonceInp.attrs.get('value')
else: nonceVal = None # print('could not find an input named "nonce"')
```
