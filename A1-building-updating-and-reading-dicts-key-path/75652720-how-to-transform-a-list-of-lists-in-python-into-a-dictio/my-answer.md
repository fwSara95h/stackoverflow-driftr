---
title: "How to transform a list of lists in Python into a dictionary"
site: stackoverflow
question_id: 75652720
answer_id: 75653416
url: https://stackoverflow.com/a/75653416
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-06T16:33:02Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75653416/revisions
accepted: true
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 05cb483307970b5b95bef382fa630bdd427e445650b2dce1faf883137004b000
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-06

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75653416>, 2023-03-06; **accepted**; score 0. Text as retrieved 2026-10-12.

If you used a set of functions like 

```py
def kvCombine(obj:list):
    if isinstance(obj, dict): obj = list(obj.items()) 
    if not isinstance(obj, list): return obj
    obj = [t for lt in [
        list(o.items()) if isinstance(o,dict) else [o] for o in obj
    ] for t in lt]
    
    if not all(isinstance(t, tuple) and len(t)==2 for t in obj): return obj
    kList = set(k for k, v in obj)
    kvPairs = [(ki, [v for k, v in obj if k==ki]) for ki in kList]
    return {k: v[0] if len(v)==1 else kvCombine(v) for k, v in kvPairs}

def dict_graph(pList):
    if not isinstance(pList, list): return pList
    if not pList: return None # {} # []
    if len(pList)==1: return dict_graph(pList[0])

    if any(isinstance(p, list) for p in pList):
        return kvCombine([  (p,None) if not isinstance(p,list) else 
                            (p[0],dict_graph(p[1:])) for p in pList if p!=[] ])
    
    if len(pList)==2: return {pList[0]: pList[1]}
    return {pList[0]: dict_graph(pList[1:])}
```

then with a list of lists:

```py
example = [[ 'a', 'b', 'c', 'd'], [ 'a', 'b', 'e', 'f'], [ 'g', 'h']]
example_graph = dict_graph(example)
```

`example_graph` would look like 

> ```py
> {'a': {'b': {'c': 'd', 'e': 'f'}}, 'g': 'h'}
> ```

>```json
> {
>     "a": {
>         "b": {
>             "c": "d",
>             "e": "f"
>         }
>     },
>     "g": "h"
> }
>```
