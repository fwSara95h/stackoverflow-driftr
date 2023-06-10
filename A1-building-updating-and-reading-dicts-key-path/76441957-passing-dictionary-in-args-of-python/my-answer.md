---
title: "Passing dictionary in args of python"
site: stackoverflow
question_id: 76441957
answer_id: 76448138
url: https://stackoverflow.com/a/76448138
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-06-10T20:56:58Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/76448138/revisions
accepted: false
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1ca6bdb37697ce3fbd062083fbb316a002264e7db9e542b0326d80a637cf60a5
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-06-10

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76448138>, 2023-06-10; score 0. Text as retrieved 2026-10-12.

> and keys associated with as the user passed

> The function call is like this `abc(thisdict["brand"]["color"],"111","222")`


Do you *have* to call `abc` like that? Unless you pass the actual dictionary (`thisdict`), I don't think you can trace the keys that lead to the value `"Red"`. If `abc` had access to `thisdict` itself, it could use something like the helper functions below:

```py
def yield_key_paths(objC, valT, kPath=None, validTypes=(tuple,list,dict,set)):
    ''' Traverse objC data structure recursively to yield path/s to valT'''

    if not isinstance(kPath, list): kPath = []
    if objC == valT: yield kPath
    if not isinstance(objC, validTypes): return 

    for k,v in (objC.items() if isinstance(objC,dict) else enumerate(objC)):
        yield from yield_key_paths(v, valT, kPath+[k], validTypes)



def find_nested_val(obj, val, findAll=False, validTypes=(tuple,list,dict,set)):
    '''Get a list of or the first path to val in obj (No path -> [] or None)'''

    paths = yield_key_paths(obj, val, [], validTypes)
    return list(paths) if findAll else next(paths, None)  
```

For example,

```py
thisdict = {"brand": {"color":"Red","model": "Mustang"},
            "manufactured": {"year":"1964","month":"Oct"}}

find_nested_val(thisdict, 'Red') ## --> ['brand', 'color']
find_nested_val(thisdict, 'Red', findAll=True) ## --> [['brand', 'color']]

find_nested_val(thisdict, '1966') ## --> None # since it cannot be found
find_nested_val(thisdict, '1966', findAll=True) ## --> []
find_nested_val(thisdict, '1964') ## --> ['manufactured', 'year']

find_nested_val(thisdict, thisdict) ## --> []
find_nested_val(thisdict, thisdict, findAll=True) ## --> [[]]
```

---

> In the function abc I am trying to extract the dictionary name

Again, I don't think you can do this without passing the dictionary itself, but if you do, then you can use the [`varname`](https://pypi.org/project/varname/) library's `nameof` function, like

```py
## !pip install -U varname
## from varname import nameof

def abc(*args):
    print(nameof(args[0], frame=2))
    ###### OTHER CODE ######

abc(thisdict, thisdict["brand"]["color"],"111","222") ## --> prints `thisdict`
```

<br>

---
---

<br>

So, if you defined `abc` as

```py
def abc(*args):
    dictname = nameof(args[0], frame=2)

    for v in args[1:]:
        vPath = find_nested_val(args[0], v)
        if vPath is None: print(f'!!{v!r} could not be found in {dictname}!!')
        else:
            vPath = ']['.join([repr(k) for k in vPath])
            if vPath: vPath = f'[{vPath}]'
            print(f'{dictname}{vPath} = {v!r}') 
```

then <kbd>`abc(thisdict, thisdict['brand']['color'],"111","222",'Oct')`</kbd> would print

> ```lang-none
> thisdict['brand']['color'] = 'Red'
> !!'111' could not be found in thisdict!!
> !!'222' could not be found in thisdict!!
> thisdict['manufactured']['month'] = 'Oct'
> ```
