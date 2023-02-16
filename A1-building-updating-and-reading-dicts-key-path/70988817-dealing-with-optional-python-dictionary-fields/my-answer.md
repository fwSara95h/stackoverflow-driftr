---
title: "Dealing with optional python dictionary fields"
site: stackoverflow
question_id: 70988817
answer_id: 75466591
url: https://stackoverflow.com/a/75466591
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-16T00:05:56Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75466591/revisions
accepted: false
score: 2
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: [getVal, valGetter]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fef2d2b5a53affccaea870138c920c1696232af69d8840bf272aab3e86832e1d
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-16

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75466591>, 2023-02-16; score 2. Text as retrieved 2026-10-12.

<sup>Since you like one-liners like <kbd>`dictionary2["optional"]["value1"] if "optional" in dictionary2 else " "`</kbd> and <kbd>`dictionary2.get("optional", {}).get("value1", " ")`</kbd>, I thought to also suggest</sup>

```python
getattr(dictionary2.get("optional"), "get", {}.get)("value1", " ")
```

By using **[`getattr`](https://www.programiz.com/python-programming/methods/built-in/getattr)**, this also accounts for [and would return `" "` on] *`dictionary2['optional']`* not being a dictionary [instead of raising an `AttributeError` or `TypeError` with the other two methods].

If wrapped as a function, it would be something like

```python
# get_v2 = lambda d, k1, k2, vDef=None: getattr(d.get(k1), 'get', {}.get)(k2,vDef) ## OR
def get_v2(d, k1, k2, vDef=None): 
    return getattr(d.get(k1), 'get', {}.get)(k2,vDef)

a = get_v2(dictionary1, 'optional', 'value1', vDef=' ') ## -->  a='one'
b = get_v2(dictionary2, 'optional', 'value1', vDef=' ') ## -->  b=' '
```

---

However, if you want to be able to call it for any number of keys you'll need to used either **recursion**

```python
def getVal(obj, k1, *keys, vDef=None):
    nxtVal = getattr(obj, 'get', {}.get)(k1, vDef)
    return getVal(nxtVal, *keys, vDef=vDef) if keys else nxtVal
```

or **a loop**

```python
def getVal(obj, *keys, vDef=None):
    for k in keys: obj = getattr(obj, 'get', {}.get)(k, vDef)
    return obj
```

---

Although, I think it's more efficient to use **`try..except`** as already suggested by some.

```python
def getVal(obj, k1, *keys, vDef=None):
    try: return getVal(obj[k1], *keys, vDef=vDef) if keys else obj[k1]
    except: return vDef
```

or

```python
def getVal(obj, *keys, vDef=None):
    try: 
        for k in keys: obj = obj[k]
    except: obj = vDef
    return obj
```

---

You can also write a function that returns a function [ a bit like [`operator.itemgetter`](https://docs.python.org/3/library/operator.html#operator.itemgetter) ] and can be used like <kbd>`valGetter("optional", "value1")(dictionary2, " ")`</kbd>

```python
def valGetter(k1, *keys):
    if keys:
        def rFunc(obj, vDef=None):
            try: 
                for k in (k1,)+(keys): obj = obj[k]
            except: obj = vDef
            return obj
    else: 
        def rFunc(obj, vDef=None):
            try: return obj[k1]
            except: return vDef 
    return rFunc
```



but please note that this can turn out to be [rather slow compared to the other methods][1].


  [1]: https://i.sstatic.net/b6kQx.png
