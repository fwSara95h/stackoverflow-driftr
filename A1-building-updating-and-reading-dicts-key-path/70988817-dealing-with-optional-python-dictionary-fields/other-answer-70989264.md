---
title: "Dealing with optional python dictionary fields"
site: stackoverflow
question_id: 70988817
answer_id: 70989264
url: https://stackoverflow.com/a/70989264
author: "derek"
author_url: https://stackoverflow.com/users/2327940
posted: 2022-02-04T15:56:47Z
last_edited: 2023-02-15T11:57:17Z
last_editor: "Flimm"
last_editor_url: https://stackoverflow.com/users/247696
accepted: false
score: 3
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 10aebbffb4124a86ef078c54475b692c884b818bdef649350380bbcb1f088694
role: another answer on the same question, kept as context; not my work
---

# Answer by [derek](https://stackoverflow.com/users/2327940) — 2022-02-04

Posted on Stack Overflow, <https://stackoverflow.com/a/70989264>, 2022-02-04, last edited 2023-02-15. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You could use [`toolz.dicttoolz.get_in()`][1] for this:
```
from toolz.dicttoolz import get_in

dictionary1 = {"required": {"value1": "one", "value2": "two"}, "optional": {"value1": "one"}}
dictionary2 = {"required": {"value1": "one", "value2": "two"}}

get_in(("optional", "value1"), dictionary1)
# 'one'

get_in(("optional", "value1"), dictionary2)
# None

```


If you don't want to install the whole library, you can just [copy the source][2] licensed under BSD:

```
import operator
from functools import reduce

def get_in(keys, coll, default=None, no_default=False):
    try:
        return reduce(operator.getitem, keys, coll)
    except (KeyError, IndexError, TypeError):
        if no_default:
            raise
        return default
```

  [1]: https://toolz.readthedocs.io/en/latest/api.html#toolz.dicttoolz.get_in
  [2]: https://toolz.readthedocs.io/en/latest/_modules/toolz/dicttoolz.html#get_in

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[c8999c 3f964f64](https://stackoverflow.com/users/11803687)** (2022-02-04): This seems very close to what I'm looking for! I'll consider using this library, thanks a lot!
