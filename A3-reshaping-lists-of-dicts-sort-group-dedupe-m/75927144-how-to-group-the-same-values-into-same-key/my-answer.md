---
title: "How to group the same values into same key?"
site: stackoverflow
question_id: 75927144
answer_id: 75928321
url: https://stackoverflow.com/a/75928321
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-04T10:33:02Z
last_edited: 2023-04-24T17:46:28Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75928321/revisions
accepted: true
score: 0
chapter: A3
chapter_title: "Reshaping lists of dicts: sort, group, dedupe, merge"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0); the revisions listed under edited_by_others are those users' work under CC BY-SA 4.0
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 274b7ce599d5adb9550100cfb6e86823882a1233ce4589885da6836ee3964110
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
edited_by_others:
  - "TylerH (https://stackoverflow.com/users/2756409), revision 2, 2023-04-24, CC BY-SA 4.0 — Removed extraneous new lines"
---

# My answer — 2023-04-04

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75928321>, 2023-04-04, last edited 2023-04-24; **accepted**; score 0. Text as retrieved 2026-10-12. Later revisions by other users are listed in the front matter.

One way would be to loop through the input list (`data` or `newlist`) and use [`.setdefault`](https://www.programiz.com/python-programming/methods/dictionary/setdefault) and `.append` to fill up the nested dictionary or lists.

---

To get the nested dictionary from `data`:

```py
result, kList, vData = {}, data[0], data[1:]
for r in vData:
    k_outer, k_inner = r[:2]
    dict_inner = result.setdefault(k_outer, {})
    list_inner = dict_inner.setdefault(k_inner, [])
    list_inner.append(dict(zip(kList, r)))
```

---

To get the nested dictionary from `newlist`:

```py
# newlist = [dict(zip(data[0],r)) for r in data[1:]] # <-- get newlist from data

result, k_outer_key, k_inner_key = {}, 'num', 'e1'
for r in newlist:
    k_outer, k_inner = r.get(k_outer_key), r.get(k_inner_key)
    dict_inner = result.setdefault(k_outer, {})
    list_inner = dict_inner.setdefault(k_inner, [])
    list_inner.append(r)
```
---

You can also use [dictionary comprehension](https://www.programiz.com/python-programming/dictionary-comprehension) to create a nested dictionary containing empty lists and then loop through `data` or `newlist` and add each dictionary in the input list to whichever list it belongs to in the nested dictionary. 

(You could filter the input list for each nested key right away with [list comprehension](https://www.programiz.com/python-programming/list-comprehension) when you're defining the nested dictionary, but doing it in a separate loop actually reduces the total number of times you loop through the input data.)

---

To get the nested dictionary from `data`, you can use

```py
kList, vData = data[0], data[1:]

result = {k_outer: {
    k_inner: [] for k, k_inner, *_ in vData if k==k_outer
} for k_outer in {k1 for k1, *_ in vData}}

for r in vData: result[r[0]][r[1]].append(dict(zip(kList,r)))

## OR 
''' ## [SLIGHTLY LESS EFFICIENT]
kList, vData = data[0], data[1:]
result = {k_outer: {
    k_inner: [dict(zip(kList,x)) for x in vData if x[0]==k_outer and x[1]==k_inner] 
    for k, k_inner, *_ in vData if k==k_outer
} for k_outer in {k1 for k1, *_ in vData}}
''' 
``` 

---
 
<br>

To get the nested dictionary from `newlist`, you can use

```py
k_outer, k_inner = 'num', 'e1'

result = {k: {
    d.get(k_inner): [] for d in newlist if k==d.get(k_outer)
} for k in {r.get(k_outer) for r in newlist}}

for r in newlist: result[r.get(k_outer)][r.get(k_inner)].append(r)

## OR 
''' ## [SLIGHTLY LESS EFFICIENT]
k_outer, k_inner = 'num', 'e1'
result = {k: {d.get(k_inner): [
    x for x in newlist if x.get(k_outer)==k and x.get(k_inner)==d.get(k_inner)
] for d in newlist if k==d.get(k_outer)} for k in {r.get(k_outer) for r in newlist}}
'''
```

---

Whichever approach is taken, `result` should look like

> ```py
> {
>   '2004': {
>     'p': [{'num': '2004', 'e1': 'p', 'e2': 'a', 'e3': 'p'}, {'num': '2004', 'e1': 'p', 'e2': 's', 'e3': 'f'}]
>   },
>   '2002': {
>     'p': [{'num': '2002', 'e1': 'p', 'e2': 'r', 'e3': 'i'}],
>     'k': [{'num': '2002', 'e1': 'k', 'e2': 'r', 'e3': 'i'}]
>   },
>   '2001': {
>     'k': [{'num': '2001', 'e1': 'k', 'e2': 'r', 'e3': 'e'}]
>   }
> }
> ```
