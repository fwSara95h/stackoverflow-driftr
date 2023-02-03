---
title: "How to use a tuple's 6 values as 6 keys in a dictionary, and print the dictionary's corresponding values?"
site: stackoverflow
question_id: 75299914
answer_id: 75341756
url: https://stackoverflow.com/a/75341756
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-03T22:52:41Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75341756/revisions
accepted: false
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 760b7b26fc0d61b518c2e3714e75aca386ae2e9f496e3bf205aacdb11ea7972c
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-03

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75341756>, 2023-02-03; score 0. Text as retrieved 2026-10-12.

I'm not entirely sure I understand your question fully, but you can use [`itemgetter`](https://docs.python.org/3/library/operator.html?highlight=operator%20itemgetter#operator.itemgetter) as suggested in one of the comments, or [if you don't want to depend on the `operator` module] something like

```python
def get_tuple_of_values(dict_w100plus_kvp:dict, keysRef, defaultVal=None):
    return tuple(dict_w100plus_kvp.get(k,defaultVal) for k in keysRef)
```

will return a tuple of the same length as `keysRef`, which can be be a tuple or dictionary or list [or any iterable really, as long as it only contains hashable values that might be keys in `dict_w100plus_kv`].

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[chepner](https://stackoverflow.com/users/1126841)** (2023-02-03): There's no drawback to depending on the `operator` module; it's part of the standard library, so if it's not available, something is very, very wrong.
- **me** (2023-02-04): @chepner my habit is to import as few modules as possible - it's mostly a matter of personal preference...but also, in this case I don't see much advantage to it either? this is pretty much what it does anyway [for multiple keys] except mine is more forgiving as it uses `.get`
- **[chepner](https://stackoverflow.com/users/1126841)** (2023-02-04): Importing as few modules as possible means you are reinventing the wheel a lot.
- **me** (2023-02-04): True, but I prefer not to buy a car when all I want is a wheel
