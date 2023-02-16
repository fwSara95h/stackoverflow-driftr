---
title: "Conversion of string dictionary with single quoted values to double quoted values"
site: stackoverflow
question_id: 75466686
answer_id: 75467703
url: https://stackoverflow.com/a/75467703
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-16T03:54:25Z
last_edited: 2023-02-16T03:58:13Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75467703/revisions
accepted: true
score: 1
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 79e561ad7360d074a00e8741b1cbe6b2601c3ea1dd5e3eed460611a4731d195a
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-16

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75467703>, 2023-02-16, last edited 2023-02-16; **accepted**; score 1. Text as retrieved 2026-10-12.

While your example string isn't valid JSON, it *is* valid for a python dictionary; so, you can get away with simply using [`eval`](https://www.programiz.com/python-programming/methods/built-in/eval) [at least for this particular string].

```python
dictStr = '''{'first_name': "John", "age": 89}'''

dictObj = eval(dictStr)
print('dictObj:', type(dictObj), repr(dictObj), '\n')

# import json
jsonStr = json.dumps(eval(dictStr))
print('jsonStr:', type(jsonStr), repr(jsonStr), '\n')
```

should print 

> ```python
> dictObj: <class 'dict'> {'first_name': 'John', 'age': 89} 
> 
> jsonStr: <class 'str'> '{"first_name": "John", "age": 89}' 
> 
> ```

`jsonStr` is exactly what your title is asking for, but I think your end goal is `dictObj` which you probably though you need `jsonStr` for [but in this case you don't need it, since you can get the dictionary directly with needing to fix the JSON.]

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[ShadowRanger](https://stackoverflow.com/users/364696)** (2023-02-16): Please don't recommend `eval` when the *safe* `ast.literal_eval` will do the trick. The OP is accepting user input; passing it to `eval` is asking for trouble, but `ast.literal_eval` can't do anything insane.
- **[Kelly Bundy](https://stackoverflow.com/users/12671057)** (2023-02-16): @ShadowRanger "Safer", not safe. The [doc](https://docs.python.org/3.11/library/ast.html#ast.literal_eval) also doesn't call it safe anymore.
