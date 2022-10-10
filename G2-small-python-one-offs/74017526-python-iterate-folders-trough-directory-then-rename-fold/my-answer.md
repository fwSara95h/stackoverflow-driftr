---
title: "Python : Iterate folders trough directory then rename folders with condition"
site: stackoverflow
question_id: 74017526
answer_id: 74018989
url: https://stackoverflow.com/a/74018989
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-10T18:00:06Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74018989/revisions
accepted: false
score: 0
chapter: G2
chapter_title: "Small Python one-offs"
cluster: python-misc
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b7199ec9c408b410713c6770285dd9dee171b93c2dcf91b0986b5643e3b4a9a3
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-10

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74018989>, 2022-10-10; score 0. Text as retrieved 2026-10-12.

You can do something like this instead of your `if...else` block:

```python
    matchedStr = [s for s in list_of_str if s in dirname]
    if matchedStr:
        os.rename(f,"SET_STR")
    else: pass # REDUNDANT
```

`matchedStr` will have any string from `list_of_str` that contains `dirname`, and an  empty list will evaluate to `False` the folder will not be renamed if there are no matches.

The `else` is completely unnecessary here (even `if x==y:....else: pass` is the same as just `if x!=y:..`), but some people prefer a certain format so I left it in incase of that.

Also, I have a feeling that you don't quite understand how python's `enumerate` works. Please take a look at [this tutorial](https://www.guru99.com/python-enumerate-function.html) at some point for further understanding.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Johntix](https://stackoverflow.com/users/15782335)** (2022-10-11): thank you for your answer, my bad for the enumerate , i just put it here for my own meaning but obviously this is not the appropriate thing :) for dirname , i tried to set the variable as a windows path (with pathlib) but it return that a windows path is not iterable, any idea to avoid this problem ?
- **me** (2022-10-11): I think your current `os.listdir(start_path)` is just fine, but you could probably use something like `start_path.iterdir()` instead, if you want to use pathlib
- **me** (2022-10-11): Also, whether you end up using pathlib or os, you should add `f.is_dir()` or `os.path.isdir(f)` to the `if` conditions if you want to rename only folders and not files as well
