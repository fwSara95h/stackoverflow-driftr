---
title: "Why am I getting a python RecursionError"
site: stackoverflow
question_id: 74978098
answer_id: 74978234
url: https://stackoverflow.com/a/74978234
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-02T00:35:13Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74978234/revisions
accepted: false
score: 0
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 45d0bd48bf2d2b03043dfdc36faed0e8f7272cdb0cbe9f8c5d05dead4984b6fb
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-02

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74978234>, 2023-01-02; score 0. Text as retrieved 2026-10-12.

Python's default [maximum recursion depth](https://www.codingem.com/python-maximum-recursion-depth/) is 1000, but you can check yours with *`print(sys.getrecursionlimit())`* or set a new one with

```python
# import sys
new_recursion_limit = 2000 # set as you prefer
sys.setrecursionlimit(new_recursion_limit)
# print('recursion limit is now', sys.getrecursionlimit()) 
```

**but this is considered a dangerous method.**

---

Instead you should consider setting extra parameters for `GetPdcResults` [or any other recursive function] - something like 

```python
def GetPdcResults(parts, start=0, maxDepth=999, curDepth=0):
```

and then increment `curDepth` with every recursive call, such as

```python
        # if response.status_code == 401:
            # logger.log_error('[-] Cookie Error', part=part)
            # print('\n[-] Cookie Error')
            if curDepth < maxDepth: 
                GetPdcResults(parts, start=i, maxDepth=maxDepth, curDepth=curDepth+1)
            ## else: print(curDepth, 'is too deep') # if you want an alternate action...
            # break
```
