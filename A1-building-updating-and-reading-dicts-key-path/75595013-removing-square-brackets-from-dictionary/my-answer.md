---
title: "Removing square brackets from dictionary"
site: stackoverflow
question_id: 75595013
answer_id: 75598002
url: https://stackoverflow.com/a/75598002
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-28T22:41:52Z
last_edited: 2023-02-28T23:00:17Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75598002/revisions
accepted: true
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 635d818c4a38953ca93f26db5f6e27e7267844a2b59ec677f962ad750e623b4b
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-28

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75598002>, 2023-02-28, last edited 2023-02-28; **accepted**; score 0. Text as retrieved 2026-10-12.

> *This removes the square brackets and replaces them with quotation marks.....I still can't extract from the row as I have in other columns & I am stuck. I only need the curly brackets in place.*

The quotes indicates that it's stringified; but the *`else repr(x).strip('[]')`* of my suggested expression only applied because it wasn't a list to start with, which means you need to attempt to parse it; so a `lambda` expression will no longer be enough. You could try something like **`df.COLUMN.map(try_parse)`** where `try_parse` is defined as:

```py
import ast
def try_parse(obj, unlistSingles=True, enforceType=None, defaultVal=None):
    if isinstance(obj, str) and enforceType!=str:
        try: obj = ast.literal_eval(obj) ## safer than just eval
        except: pass
    if isinstance(obj, list) and len(obj)==1 and enforceType!=list: obj = obj[0]
    if isinstance(enforceType,type):
        if isinstance(obj,enforceType): return obj
        try: obj = enforceType(obj)
        except: return defaultVal
    return obj
```

If you want to ensure that a dictionary is returned, use <kbd>**`df.COLUMN.map(lambda x: try_parse(x, enforceType=dict, defaultVal={}))`**</kbd> [or with `defaultVal={'country':{'name': None}}`]

---

Btw, about

> *I have used this code successfully on the other columns which dont have the square brackets. `df.COLUMN.map(lambda x: x['country']['name'])`*

If you want this to work for any dictionary at all without raising error, you can change the expression to <kbd>**`lambda x: getattr(x.get('country'), 'get', {}.get)('name', '!no_country_name!')`**</kbd> [you use a different default value than *`'!no_country_name!'`*, or just omit that part entirely, in which case the expression will return `None` if it can't get `x['country']['name']`].
