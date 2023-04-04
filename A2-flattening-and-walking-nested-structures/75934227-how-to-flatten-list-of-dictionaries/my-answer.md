---
title: "How to flatten list of dictionaries"
site: stackoverflow
question_id: 75934227
answer_id: 75934500
url: https://stackoverflow.com/a/75934500
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-04T23:09:40Z
last_edited: 2023-04-04T23:57:26Z
revisions: 3
revision_history: https://stackoverflow.com/posts/75934500/revisions
accepted: false
score: 1
chapter: A2
chapter_title: "Flattening and walking nested structures"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 26f4ab56a1d16ef32150b30c5e21df2878c59f18d154b021dd76c0a8d9f6da73
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-04

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75934500>, 2023-04-04, last edited 2023-04-04; score 1. Text as retrieved 2026-10-12.

[Nested for-loops](https://www.geeksforgeeks.org/python-nested-loops/) or [list comprehension](https://www.programiz.com/python-programming/list-comprehension) are common ways to [flatten objects of **fixed** depth](https://stackoverflow.com/a/45079294/6146136); and [recursion](https://www.programiz.com/python-programming/recursion) is generally useful for flattening objects of **arbitrary** depth, so you can 
- flatten by one more level with each recursive call, and
- use [`isinstance`](https://www.programiz.com/python-programming/methods/built-in/isinstance) to detect dictionaries before getting [`.values`](https://www.programiz.com/python-programming/methods/dictionary/values), and 
- use [`hasattr`](https://www.programiz.com/python-programming/methods/built-in/hasattr) to check if an input has `__iter__` (and is, therefore, [iterable](https://www.geeksforgeeks.org/how-to-check-if-an-object-is-iterable-in-python/))

<br>

You can use the nested loop in a [generator](https://www.programiz.com/python-programming/generator) function

```py
def flatten_obj(obj):
    if hasattr(obj, '__iter__') and not isinstance(obj, str): 
        for i in (obj.values() if isinstance(obj, dict) else obj):
            for v in flatten_obj(i): yield v
    else: yield obj
```

<br>

But if you want the function to return a list, list comprehension might be preferable to initiating an empty list and appending to it in a nested loop.

``` py
def get_flat_list(obj, listify_single=False):
    if isinstance(obj, str) or not hasattr(obj, '__iter__'): 
        return [obj] if listify_single else obj
    
    if isinstance(obj, dict): obj = obj.values()
    return [v for x in obj for v in get_flat_list(x,listify_single=True)]
```

---

<br>

Using
- either <kbd>**`{k: list(flatten_obj(v)) for i in process for k,v in i.items()}`**</kbd>
- or <kbd>**`{k: get_flat_list(v) for i in process for k,v in i.items()}`**</kbd>

should return 

> ```py
> {
>   'process1': ['subprocess1_1', 'subprocess1_2', 'subprocess2', 'subprocess3_1', 'subprocess3_2', 'subprocess4', 'subprocess5_1_1', 'subprocess5_1_2'],
>   'process2': ['subprocess2_1']
> }
> ```

<br>

Ofc you can also define `process1` and `process2` as separate variables:

```py
process1 = get_flat_list(process[0]['process1']) 
# list(flatten_obj(process[0]['process1']))

process2 = get_flat_list(process[1]['process2']) 
# list(flatten_obj(process[1]['process2']))
```

or

```py
process1, process2, *_ = [list(flatten_obj(v)) for i in process for v in i.values()]
# process1, process2, *_ = [get_flat_list(v) for i in process for v in i.values()]
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[jtlz2](https://stackoverflow.com/users/1021819)** (2023-08-03): Love the fixed depth vs arbitrary depth point - thank you!
