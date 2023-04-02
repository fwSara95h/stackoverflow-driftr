---
title: "Find and Update Dictionary Value Using Key List"
site: stackoverflow
question_id: 75903026
answer_id: 75910689
url: https://stackoverflow.com/a/75910689
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-02T07:39:03Z
last_edited: 2023-04-02T07:44:43Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75910689/revisions
accepted: false
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 390f5f8526c64ae42c70c0f7c3a5f9b6bd6356bf28e1beed9eff9244ce48bee2
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-02

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75910689>, 2023-04-02, last edited 2023-04-02; score 0. Text as retrieved 2026-10-12.

> *"I want to check if the dictionary (say `gen_dict`) has that value stored at that location and if not, update it."*

But why? If it's the same value, updating won't change it so it'll effectively remain unchanged....

---

### Suggested Solution 1

You can [loop](https://www.programiz.com/python-programming/for-loop) through the keys in `topics` [except for the last one] and check if they're paired to a dictionary with [`.get`](https://www.programiz.com/python-programming/methods/dictionary/get) and [`isinstance`](https://www.programiz.com/python-programming/methods/built-in/isinstance).

```py
# topics = ['general_topic', 'born', 'to', 'fly']
set_val = 100

cur_dict = gen_dict ## gen_dict MUST BE a dictionary
for k in topics[:-1]:
    if isinstance(cur_dict.get(k), dict): cur_dict = cur_dict[k]
cur_dict[topics[-1]] = set_val 
# if topics[-1] in cur_dict: cur_dict[topics[-1]] = set_val ## only set if path exists
# if cur_dict[topics[-1]]!=set_val: cur_dict[topics[-1]] = set_val # redundant condition
```

This is quite forgiving, so even if some keys are missing, it will still work

- *`{'other': 'blah', 'general_topic': {'born': {'to': {'fly': 30}}}, 'another': 324}`* (from [your comment](https://stackoverflow.com/questions/75903026/find-and-update-dictionary-value-using-key-list#comment133881592_75903026)) will become
  > ```py
  > {'other': 'blah', 'general_topic': {'born': {'to': {'fly': 100}}}, 'another': 324}
  > ```
- *`{'born': {'fly': 30}}`* will become <kbd>`{'born': {'fly': 100}}`</kbd>, but
- *`{'born': {'to': 10}}`* will become <kbd>`{'born': {'to': 10, 'fly': 100}}`</kbd>, and
- an empty dictionary (*`{}`*) will become <kbd>`{'fly': 100}`. 

<sup>[The last 2 (*`{'born': {'to': 10}}`*, *`{}`*) will remain unchanged if you use the *`if topics[-1] in cur_dict`* condition.]</sup>

---

### Suggested Solution 2

If you want to create the path if any part is missing [with the first key being optional], then use [`.setdefault`](https://www.programiz.com/python-programming/methods/dictionary/setdefault) as below.

```py
set_val = 100

cur_dict = gen_dict ## gen_dict MUST BE a dictionary
for i, k in enumerate(topics[:-1]):
    if not i and not isinstance(cur_dict.get(k), dict): continue
    kval = cur_dict.setdefault(k, {})

    if not isinstance(kval, dict): cur_dict[f'prev_{k}'], cur_dict[k] = kval, {}
    cur_dict = cur_dict[k]
cur_dict[topics[-1]] = set_val 
```

<sup>[If the first key is **not** optional, then omit the *`if...continue`* line at the beginning of the loop; and using [`enumerate`](https://www.programiz.com/python-programming/methods/built-in/enumerate) should no longer be necessary, so you can go back to *`for k in topics[:-1]`*.]</sup>

- *`{'other': 'blah', 'general_topic': {'born': {'to': {'fly': 30}}}, 'another': 324}`* will still become
  > ```py
  > {'other': 'blah', 'general_topic': {'born': {'to': {'fly': 100}}}, 'another': 324}
  > ```
  [just like before], but
- *`{'born': {'fly': 30}}`* will become <kbd>`{'born': {'fly': 30, 'to': {'fly': 100}}}`</kbd>, and
- *`{'born': {'to': 10}}`* will become <kbd>`{'born': {'to': {'fly': 100}, 'prev_to': 10}}`</kbd>, and
- an empty dictionary (*`{}`*) will become <kbd>`{'born': {'to': {'fly': 100}}}`</kbd></kbd>.
