---
title: "Ordering keys in a dictionary"
site: stackoverflow
question_id: 75700999
answer_id: 75702903
url: https://stackoverflow.com/a/75702903
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-11T05:06:42Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75702903/revisions
accepted: true
score: 0
chapter: A3
chapter_title: "Reshaping lists of dicts: sort, group, dedupe, merge"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: cbb315180d9471527327b23779e1fce32230a51a061a17ca0e7673d7ebf45e8d
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-11

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75702903>, 2023-03-11; **accepted**; score 0. Text as retrieved 2026-10-12.

> *`setdefault()` doesn't work in this situation because it either returns a value given a key or adds a key-value pair, none of which I want to do.*

Actually, [`setdefault`](https://www.programiz.com/python-programming/methods/dictionary/setdefault) adding a key-value pair *is* a bit handy in this situation as you can use it instead of *`if _ not in __: __[_]={}`* like:

```py
reordered = {}
for song in output:
    for chunk in output[song]:
        for attr, val in output[song][chunk].items():
            reordered.setdefault(attr, {})
            reordered[attr].setdefault(song, {})
            reordered[attr][song][chunk] = val
```

---

You can also try [flattening][1] `output` first with something like

```py
def get_flatDict(obj, parentKeys=tuple(), asDict=True):
    if not isinstance(obj, dict): 
        return {parentKeys: obj} if asDict else [(parentKeys, obj)]
    
    kvPairs = []
    for k, v in obj.items(): 
        kvPairs += get_flatDict(v, parentKeys=(*parentKeys,k), asDict=False)
    return dict(kvPairs) if asDict else kvPairs
```

and then building `reordered` like

```py
reordered = {}
for (song, chunk, attr), val in get_flatDict(output).items():
    reordered.setdefault(attr, {})
    reordered[attr].setdefault(song, {})
    reordered[attr][song][chunk] = val
```

---

Either way, if you had 

```py
output = { 'song1': {
    'chunk1': {'attr1': 'value1', 'attr2': 'value2', 'attr3': 'value3'},
    'chunk2': {'attr1': 'value4', 'attr2': 'value5', 'attr3': 'value6'},
    'chunk3': {'attr1': 'value7', 'attr2': 'value8', 'attr3': 'value9'}},
  'song2': {'chunk1': {'attr1': 'value0'}} }
```

then `reordered` would look like

>```py
> { 
>   'attr1': {
>     'song1': {'chunk1': 'value1', 'chunk2': 'value4', 'chunk3': 'value7'},
>     'song2': {'chunk1': 'value0'}
>   },
>   'attr2': {
>     'song1': {'chunk1': 'value2', 'chunk2': 'value5', 'chunk3': 'value8'}
>   },
>   'attr3': {
>     'song1': {'chunk1': 'value3', 'chunk2': 'value6', 'chunk3': 'value9'}
>   }
> }
>```


  [1]: https://i.sstatic.net/ykCPo.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Anthon](https://stackoverflow.com/users/1307905)** (2023-03-11): `get_flatDict`? It is not often I have seen the combination of both camelCase and snake_case in one (function) name.
- **me** (2023-03-11): @Anthon I'll spend hours settling on a name if I let myself, so I don't let myself 😅...but I do combine them a lot, and often in this `actionType_dataType` format
- **[Anthon](https://stackoverflow.com/users/1307905)** (2023-03-11): The big question then is if this should be named camelSnakeCase, snakeCamelCase, cameled_snakeCase or snaked_camelCase >:-) . Not to mention the fact that  a Python that has just eaten can have quite a hump...
- **me** (2023-03-11): @Anthon lmao my personal vote would go to snaked_camelCase or perhaps the lochNess_case (since some versions of Nessie has humps...)
