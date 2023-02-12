---
title: "Python: Trying to create nested dictionary from CSV File, but getting KeyError"
site: stackoverflow
question_id: 75392274
answer_id: 75424722
url: https://stackoverflow.com/a/75424722
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-12T03:23:53Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75424722/revisions
accepted: false
score: 0
chapter: A2
chapter_title: "Flattening and walking nested structures"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5191ff6270338f2b8a079da7e529783c22e6f2b81f55bdc5c4479f5d72ff6878
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-12

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75424722>, 2023-02-12; score 0. Text as retrieved 2026-10-12.

This solution requires no imports at all, but will **only work if there are no escaped separators** [i.e., none of the values contain a `,` or newline]:

```python
def load_csv(filename, sep=','):
    with open(filename, 'r') as csvfile:
        csvlines = csvfile.read().strip().splitlines()
    csvRows = [[v.strip() for v in l.split(sep)] for l in csvlines]
    if not csvRows: return {}
    keys = csvRows[0][1:]
    return {r[0]: dict(zip(keys, r[1:])) for r in csvRows[1:] if r} 
```

At the very least, it works [for the csv in your snippet][1], but if your csv contains `,` or newlines at any unexpected positions, this function will no longer be reliable - it would definitely be better to use a module built for reading and parsing csv.



  [1]: https://i.sstatic.net/FXQkT.png
