---
title: "Navigate in JSON with nultiple keys"
site: stackoverflow
question_id: 74678361
answer_id: 74680512
url: https://stackoverflow.com/a/74680512
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-04T20:13:13Z
last_edited: 2023-02-03T16:08:46Z
revisions: 3
revision_history: https://stackoverflow.com/posts/74680512/revisions
accepted: false
score: 1
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: [getNestedVal]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d0b0552b17a0f5d1546ac0f0fc4fc48b4281922a5d620809eb4cf6983816265d
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-04

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74680512>, 2022-12-04, last edited 2023-02-03; score 1. Text as retrieved 2026-10-12.

As the other answers have already explained, you need to add `[0]` between `['ABC']` and `['current']` because the value that corresponds to the `"ABC"` key is a list containing a dictionary with the `"current"` key, so you can access it with
```python
data["props"]["XYZ"]["ABC"][0]["current"]
```

---

Also, if you have a very complex and nested data structure and you want to quickly you can use [this set of functions](https://pastebin.com/NRxKRJPn)

```python
getNestedVal(data, 'current')
```

returns `'sold'`, and
 
```python 
getNestedVal(data, 'current', 'just_expr', objName='data')
```

returns `'data["props"]["XYZ"]["ABC"][0]["current"]'` so that you can copy it from the terminal and use in your code. (It's not the best idea to use it other than for just figuring out data structure since it can use up quite a bit of time and memory.)
