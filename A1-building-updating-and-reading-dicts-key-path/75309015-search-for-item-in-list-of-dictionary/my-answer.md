---
title: "Search for item in list of dictionary"
site: stackoverflow
question_id: 75309015
answer_id: 75338566
url: https://stackoverflow.com/a/75338566
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-03T16:33:02Z
last_edited: 2023-02-03T16:47:40Z
revisions: 3
revision_history: https://stackoverflow.com/posts/75338566/revisions
accepted: false
score: 1
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: [getNestedVal]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6186066f2dfcb60c6cc506d4a4524b8406b573cb236041c0bec59d1d32793b9d
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-03

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75338566>, 2023-02-03, last edited 2023-02-03; score 1. Text as retrieved 2026-10-12.

I have a [set of functions](https://pastebin.com/NRxKRJPn) that you could use for this [ <kbd>`getNestedVal(p, 'args')`</kbd> would return `{'id': 12345678, 'age: 12}` ]...or you can use this generator

```python
def yieldNestedVals(obj, key):
    if isinstance(obj, str): return
    try: yield obj[key]
    except: pass
    if isinstance(obj, dict): obj = obj.values()
    for i in (obj if hasattr(obj, '__iter__') else []):
        for v in yieldNestedVals(i, key): yield v
```

inside <kbd>`search`</kbd> like

```python
def search(name, params, defaultVal=None):
    for v in yieldNestedVals(params, name): return v # return 1st generated value
    return defaultVal # if nothing if generated
```

<sup>[ Ofc you can omit both the `defaultVal` parameter and the last line if you want to just return `None` when nothing if found, since that is the [default behavior](https://stackoverflow.com/q/15300550/6146136) when a function doesn't come across a `return` statement. ]</sup>

Now <kbd>`search('args', p)`</kbd> should also return `{'id': 12345678, 'age: 12}` and you can try it with other keys as well:

```python
# p = [{'quantity': 1}, {'args': {'id': 12345678, 'age': 12}}]
{k: search(k, p) for k in ['quantity', 'args', 'id', 'age', 'dneKey']}
```

would return

> ```python
> {'quantity': 1,
>  'args': {'id': 12345678, 'age': 12},
>  'id': 12345678,
>  'age': 12,
>  'dneKey': None}
> ```
