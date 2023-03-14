---
title: "Python: Convert multi-line text into dictionary"
site: stackoverflow
question_id: 75721080
answer_id: 75737946
url: https://stackoverflow.com/a/75737946
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-14T20:13:10Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75737946/revisions
accepted: false
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fa50d8d348cecb8f912fb11dae82d85b2f79db302376218839a9e505b209e49d
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-14

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75737946>, 2023-03-14; score 0. Text as retrieved 2026-10-12.

You could just iterate through the lines with [`<dict>.setdefault`](https://www.programiz.com/python-programming/methods/dictionary/setdefault) and [`<str>.split`](https://www.programiz.com/python-programming/methods/string/split)

```py
filepath = 'x.txt' #<-- name of / path to your file

with open(filepath, 'r') as f: fLines = f.read().splitlines() #<-- read file
kCur = '__no_parent_key__' #<-- set a default for if 1st line isn't a [key]
result = {kCur: {}} #<-- initiate

for l in fLines:
    if '=' in l: _, l = result[kCur].update([l.split('=', 1)]), ''# [l empty -> skip]

    l = l.strip()
    if not l: continue #<-- skip empty lines

    kCur = l[1:-1] if (l[0], l[-1]) == ('[', ']') else l #<-- trim [] 
    result.setdefault(kCur, {})

# remove '__no_parent_key__' if empty:
if not result['__no_parent_key__']: del result['__no_parent_key__']
```

For your sample snippet, `result` will look like

>```py
> { 
>   'ThisShouldBeAKey': {'Value1': 'yes', 'Value2': 'no', 'Value3': 'fancywords', 'Value4': 'numbers'},
>   'ThisShouldBeAnotherKey': {'Value2': 'true', 'Value3': '333', 'Value5': 'qqq'} 
> }
>```

---

You could also use a reference dictionary <sup>(like `kwList` below)</sup> and [`ast.literal_eval`](https://stackoverflow.com/q/15197673/6146136) to parse the values a bit further.

```py
kwList = {'true':True, 'false':False, 'null': None, 'none': None}
def try_eval(literalStr:str, kwRef=kwList):
    if literalStr.strip().lower() in kwRef: 
        return kwRef[literalStr.strip().lower()]
    try: return ast.literal_eval(literalStr)
    except: return literalStr
```

To make use of `try_eval`, change the *`if '=' in l:..`* block in my suggested solution to

```py
    if '=' in l: 
        k, v = l.split('=', 1) 
        result[kCur][k] = try_eval(v)
        continue
```

then `result` will look like

>```py
> { 
>   'ThisShouldBeAKey': {'Value1': 'yes', 'Value2': 'no', 'Value3': 'fancywords', 'Value4': 'numbers'},
>   'ThisShouldBeAnotherKey': {'Value2': True, 'Value3': 333, 'Value5': 'qqq'} 
> }

[Note the changes in `Value2` and `Value3` of `ThisShouldBeAnotherKey`.]
