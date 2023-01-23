---
title: "Applying keys sequentially to a dict from a list"
site: stackoverflow
question_id: 75197965
answer_id: 75205202
url: https://stackoverflow.com/a/75205202
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-23T02:10:09Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75205202/revisions
accepted: false
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: [flattenDict, flattenObj, getNestedVal]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0e58223291b42ea22fbeff3b620779cc1162b91f6251f67a72dc61aa7b82a92e
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-23

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75205202>, 2023-01-23; score 0. Text as retrieved 2026-10-12.

You can put the `try...except` in another loop, if there's a list of keys instead of a single key:

```python
def getNestedVal(obj, kPath:list, defaultVal=None):
    if isinstance(kPath, str) or not hasattr(kPath, '__iter__'): 
        kPath = [kPath] ## if not iterable, wrap as list
    for k in kPath: 
        try: obj = obj[k]
        except: return defaultVal
    return obj 

def func(person):
    filters = [('age', 'age0'), ('name', ['name0', 'first0']),#] 
               ('gender', ['gender0'], 'N/A')] # includes default value
    return {k[0]: getNestedVal(person, *k[1:3]) for k in filters}
```

<sup>[I added `gender` just to demonstrate how defaults can also be specified for missing values.]</sup>

With this, `func(person)` should return

> ```python
> {'age': '10', 'name': 'John', 'gender': 'N/A'}
> ```

---

I also have a [`flattenObj`](https://pastebin.com/v3Fep60B) function, a version of which is defined below:

```python
def flattenDict(orig:dict, kList=[], kSep='_', stripNum=True):
    if not isinstance(orig, dict): return [(kList, orig)]

    tList = []
    for k, v in orig.items():
        if isinstance(k, str) and stripNum: k = k.strip('0123456789')
        tList += flattenDict(v, kList+[str(k)], None)
        
    if not isinstance(kSep, str): return tList
    return {kSep.join(kl): v for kl,v in tList}
```

<sup>[I added `stripNum` just to get rid of the `0`s in your keys...]</sup>

`flattenDict(person)` should return

> ```python
> {'name_first': 'John', 'name_last': 'Smith', 'age': '10', 'location_city': 'Dublin'}
> ```
