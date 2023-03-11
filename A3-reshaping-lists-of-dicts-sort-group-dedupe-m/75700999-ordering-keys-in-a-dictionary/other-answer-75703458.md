---
title: "Ordering keys in a dictionary"
site: stackoverflow
question_id: 75700999
answer_id: 75703458
url: https://stackoverflow.com/a/75703458
author: "Anthon"
author_url: https://stackoverflow.com/users/1307905
posted: 2023-03-11T07:31:51Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0af265717b8ca5db0e626d550d9531930630fde881d41fb565146814f3af2e9b
role: another answer on the same question, kept as context; not my work
---

# Answer by [Anthon](https://stackoverflow.com/users/1307905) — 2023-03-11

Posted on Stack Overflow, <https://stackoverflow.com/a/75703458>, 2023-03-11. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Your example data structure consists of nested dicts. One can interpret what you are
doing in different ways, but one way is to say you bump the most deeply nested
key to the root dict. This can be solved in general for any depth of nesting using
a recursive function and `setdefault`:

```python
import sys
from pathlib import Path
import ruamel.yaml

file_in = Path('input.yaml')

yaml = ruamel.yaml.YAML()

data = yaml.load(file_in)

def reverse_keys(d, path=None, result=None):
    if path is None:
        path = []
    if result is None:
        result = {}
    if isinstance(d, dict):
        for k, v in d.items():
            reverse_keys(v, path[:] + [k], result)
    else:
        # ran out of dicts to traverse
        tmp = result
        tmp = tmp.setdefault(path[-1], {}) # use the last key as the first 
        for k in path[:-2]:  # use the first few keys to create dicts
            tmp = tmp.setdefault(k, {})
        tmp[path[-2]] = d  # use the second to last key to assign the non-dict value
    return result

yaml.dump(reverse_keys(data), sys.stdout)
```
which gives: 
            

```lang-none
attr1:
  song1:
    chunk1: value
    chunk2: value
    chunk3: value
  song2:
    chunk1: value
    chunk2: value
    chunk3: value
  song3:
    chunk1: value
    chunk2: value
    chunk3: value
attr2:
  song1:
    chunk1: value
    chunk2: value
    chunk3: value
  song2:
    chunk1: value
    chunk2: value
    chunk3: value
  song3:
    chunk1: value
    chunk2: value
    chunk3: value
attr3:
  song1:
    chunk1: value
    chunk2: value
    chunk3: value
  song2:
    chunk1: value
    chunk2: value
    chunk3: value
  song3:
    chunk1: value
    chunk2: value
    chunk3: value
```
