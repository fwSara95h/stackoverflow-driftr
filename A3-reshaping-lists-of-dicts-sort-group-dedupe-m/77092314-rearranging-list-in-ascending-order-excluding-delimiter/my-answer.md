---
title: "Rearranging list in ascending order excluding delimiter"
site: stackoverflow
question_id: 77092314
answer_id: 77092374
url: https://stackoverflow.com/a/77092374
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-09-12T20:05:30Z
last_edited: 2023-09-12T21:59:21Z
revisions: 2
revision_history: https://stackoverflow.com/posts/77092374/revisions
accepted: false
score: 2
chapter: A3
chapter_title: "Reshaping lists of dicts: sort, group, dedupe, merge"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0); the revisions listed under edited_by_others are those users' work under CC BY-SA 4.0
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: de835d2d30ebcf1cece1351da7d96e8cbf19cb1c7a9c216ad25f15912aa9fb4f
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
edited_by_others:
  - "Kelly Bundy (https://stackoverflow.com/users/12671057), revision 2, 2023-09-12, CC BY-SA 4.0 — deleted 7 characters in body"
---

# My answer — 2023-09-12

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/77092374>, 2023-09-12, last edited 2023-09-12; score 2. Text as retrieved 2026-10-12. Later revisions by other users are listed in the front matter.

You can use the [key](https://docs.python.org/3/howto/sorting.html#key-functions) function to separate and extract the second number.

---

If you have 

```py
list1 = ['1=8.06225774829855', '2=2.23606797749979', '3=8.602325267042627', '4=7.280109889280518', '5=3.1622776601683795']
```

You can build a new list with the [`sorted`](https://www.w3schools.com/python/ref_func_sorted.asp) function:

```py
list2 = sorted(list1, key=lambda s: float(s.split('=')[-1]))
# list2 = ['2=2.23606797749979', '5=3.1622776601683795', '4=7.280109889280518', '1=8.06225774829855', '3=8.602325267042627']
```

or sort the list it in place with [`.sort`](https://docs.python.org/3/library/stdtypes.html#list.sort)

```py
list1.sort(key=lambda s: float(s.split('=')[-1]))
# list1 = ['2=2.23606797749979', '5=3.1622776601683795', '4=7.280109889280518', '1=8.06225774829855', '3=8.602325267042627']
```

---

(This is assuming that all your stings are formatted perfectly, otherwise you'll need a more complex key function.)
