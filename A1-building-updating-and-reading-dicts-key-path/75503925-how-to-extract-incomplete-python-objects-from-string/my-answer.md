---
title: "How to extract incomplete Python objects from string"
site: stackoverflow
question_id: 75503925
answer_id: 75511708
url: https://stackoverflow.com/a/75511708
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-20T16:14:04Z
last_edited: 2023-02-20T20:07:11Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75511708/revisions
accepted: false
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b72cf7544dad9234175d1d46ec6fa03917347186d1e31dc2f9c4e4a9af894803
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-20

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75511708>, 2023-02-20, last edited 2023-02-20; score 0. Text as retrieved 2026-10-12.

> *I can't use `ast.literal_eval` because as I mentioned above the string output is incomplete such as `" [ { 'a' : 1 } , {'b' : "`*

But you *can* iteratively try to apply `ast.literal_eval` after slicing off the last character and closing the first bracket <sub>[similarly to how `json.loads` was used in [this solution](https://stackoverflow.com/a/53937551/6146136) suggested in [@mous](https://stackoverflow.com/users/16435355/mous)'s comment]</sub>.

```python
import ast

def eval_brokenLiteral(litStr:str, defaultVal=None, printError=True):
    try: return ast.literal_eval(litStr)
    except SyntaxError as se: evalError = se 
    # litStr = litStr[:getattr(evalError, 'offset', len(litStr))]

    bracketPairs = {'{': '}', '[': ']'}
    closers, curCloser = [], ''
    for c in ''.join(litStr.split()):
        if c not in bracketPairs: break
        curCloser = bracketPairs[c] + curCloser
        closers.append(curCloser)

    for closer in closers:
        subStr = litStr.strip() 
        while subStr[1:]:
            try: return ast.literal_eval(subStr + closer)
            except SyntaxError: subStr = subStr[:-1].strip()

    if printError: print(repr(evalError))
    return defaultVal
```

[If it can't find a valid literal, it will return `None` unless some other `defaultVal` is specified.]

---

### Tests:

```python
testCases = [
    "[{'a' : 1, 'b' : 2}, {'a' : 1'}]",
    '[[1, 2, 3], [11, 12, 21]',
    """[{'a': [{'a': 1, 'b': 2}, {'a': 1, 'b': 2}], 'b': [{'a':"""
]
for ti, tc in enumerate(testCases, 1):
    print(f'Case {ti}: {repr(tc)}\n  -  ----> ', end='')
    op = eval_brokenLiteral(tc)
    print(f'Output ---> {repr(op)}' if op else '', '\n\n---\n') 
```

> <sub>Case 1: *`"[{'a' : 1, 'b' : 2}, {'a' : 1'}]"`*</sub>
>   -  ----> Output ---> <kbd>**`[{'a': 1, 'b': 2}]`**</kbd> 
> 
> --- 
> 
> <sub>Case 2: *`'[[1, 2, 3], [11, 12, 21]'`*</sub>
>   -  ----> Output ---> <kbd>**`[[1, 2, 3], [11, 12, 21]]`**</kbd> 
> 
> --- 
> 
> <sub>Case 3: *`"[{'a': [{'a': 1, 'b': 2}, {'a': 1, 'b': 2}], 'b': [{'a':"`*</sub>
>   -  ----> Output ---> <kbd>**`[{'a': [{'a': 1, 'b': 2}, {'a': 1, 'b': 2}]}]`**</kbd> 
> 
> --- 
>
