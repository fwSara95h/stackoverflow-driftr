---
title: "sort a list that contains dictionaries with same key"
site: stackoverflow
question_id: 75907811
answer_id: 75908411
url: https://stackoverflow.com/a/75908411
author: "Mark Tolonen"
author_url: https://stackoverflow.com/users/235698
posted: 2023-04-01T19:30:17Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6df662f9ee77dfa20939567eaadce48b3ec3760142c7b4d0919b0037cbb8572f
role: another answer on the same question, kept as context; not my work
---

# Answer by [Mark Tolonen](https://stackoverflow.com/users/235698) — 2023-04-01

Posted on Stack Overflow, <https://stackoverflow.com/a/75908411>, 2023-04-01. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Put the dictionaries in a list.  [`operator.itemgetter()`](https://docs.python.org/3/library/operator.html#operator.itemgetter) can be used to fetch the primary and secondary keys for sorting:
```py
import operator
from pprint import pprint

data = [{'key1': 5, 'key2': 3},
        {'key1': 3, 'key2': 7},
        {'key1': 4, 'key2': 2},
        {'key1': 4, 'key2': 1},
        {'key1': 2, 'key2': 8}]

data.sort(key=operator.itemgetter('key1', 'key2'))
pprint(data)
```
Output:
```
[{'key1': 2, 'key2': 8},
 {'key1': 3, 'key2': 7},
 {'key1': 4, 'key2': 1},
 {'key1': 4, 'key2': 2},
 {'key1': 5, 'key2': 3}]
```
