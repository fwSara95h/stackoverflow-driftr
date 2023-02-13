---
title: "Having trouble adding both one and 2 word dict key values to inventory list in my text based game"
site: stackoverflow
question_id: 75430676
answer_id: 75439085
url: https://stackoverflow.com/a/75439085
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-13T17:10:52Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75439085/revisions
accepted: false
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 67022082a8c50ad306914fd71de2cc45cd0308328bd7fcd25609b21b8ebf609c
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-13

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75439085>, 2023-02-13; score 0. Text as retrieved 2026-10-12.

> ```python
>         if obj in rooms[current_room]['item']:
> ```

That's searching for `skull` but `Skull` doesn't match. You could use [for a case-insensitive search]

```python
        if obj.lower() in [i.lower() for i in rooms[current_room]['item']]:
```

but that doesn't feel very efficient. It might be better to just apply [`.title()`](https://www.programiz.com/python-programming/methods/string/title) or [`.capitalize()`](https://www.programiz.com/python-programming/methods/string/capitalize) to `obj` and make sure that all items in `rooms[current_room]['item']` are in consistent format.
