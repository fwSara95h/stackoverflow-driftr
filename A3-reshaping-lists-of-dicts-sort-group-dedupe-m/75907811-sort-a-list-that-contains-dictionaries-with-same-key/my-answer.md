---
title: "sort a list that contains dictionaries with same key"
site: stackoverflow
question_id: 75907811
answer_id: 75911088
url: https://stackoverflow.com/a/75911088
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-02T09:15:46Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75911088/revisions
accepted: true
score: 0
chapter: A3
chapter_title: "Reshaping lists of dicts: sort, group, dedupe, merge"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1645f260c1f698a20a83085755d2b9fb00ed7ed041197bb4399ac96be2b396d0
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-02

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75911088>, 2023-04-02; **accepted**; score 0. Text as retrieved 2026-10-12.

You can use [`sorted`](https://www.programiz.com/python-programming/methods/built-in/sorted) [which returns a new list] or [`.sort`](https://www.programiz.com/python-programming/methods/list/sort) [which just sorts whichever list it's applied to in-place and does not return anything] with a [`lambda`](https://www.programiz.com/python-programming/anonymous-function)-expression as the [`key`](https://note.nkmk.me/en/python-key-sort-sorted-max-min/) parameter. If you had a list of dictionaries `dictList` and a list of keys `keysList`, you could use

```py
sortedList = sorted(dictList, key=lambda d: [d.get(k) for k in keysList])
```

or 

```py
dictList.sort(key=lambda d: [d.get(k) for k in keysList])
```

---

For example, if you had <kbd>`keysList = ['key_1', 'key_2', 'key_3']`</kbd> and 

```
dictList = [
 {'key_1': 8, 'key_2': 6, 'key_3': 3, 'key_4': 7}, 
 {'key_1': 4, 'key_2': 2, 'key_3': 4, 'key_4': 4},
 {'key_1': 4, 'key_2': 5, 'key_3': 3, 'key_4': 3},
 {'key_1': 8, 'key_2': 5, 'key_3': 9, 'key_4': 2},
 {'key_1': 4, 'key_2': 5, 'key_3': 9, 'key_4': 0},
 {'key_1': 0, 'key_2': 7, 'key_3': 1, 'key_4': 0},
 {'key_1': 9, 'key_2': 0, 'key_3': 5, 'key_4': 5}]
```

then after being sorted by `key_1` first, then `key_2` and then `key_3`, the list would look like

> [![op][1]][1]


  [1]: https://i.sstatic.net/Qkhc5.png
