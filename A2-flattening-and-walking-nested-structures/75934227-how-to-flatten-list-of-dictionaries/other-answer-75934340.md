---
title: "How to flatten list of dictionaries"
site: stackoverflow
question_id: 75934227
answer_id: 75934340
url: https://stackoverflow.com/a/75934340
author: "mozway"
author_url: https://stackoverflow.com/users/16343464
posted: 2023-04-04T22:32:45Z
last_edited: never
accepted: true
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 16555f21008628de44a8e26d9077fcb01792a6c1e406285e3f08397b002cf5f9
role: another answer on the same question, kept as context; not my work
---

# Answer by [mozway](https://stackoverflow.com/users/16343464) — 2023-04-04

Posted on Stack Overflow, <https://stackoverflow.com/a/75934340>, 2023-04-04; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

In such cases, it's always useful to use a recursive function/generator:
```
def flatten(x):
    if isinstance(x, list):
        for item in x:
            yield from flatten(item)
    elif isinstance(x, dict):
        for k, v in x.items():
            yield k
            yield from flatten(v)
    else:
        yield x
        
out = {k: list(flatten(v)) for d in process for k,v in d.items()}
```
Output:
```
out['process1']
# ['subprocess1', 'subprocess1_1', 'subprocess1_2', 'subprocess2',
#  'subprocess3', 'subprocess3_1', 'subprocess3_2', 'subprocess4',
#  'subprocess5', 'subprocess5_1', 'subprocess5_1_1', 'subprocess5_1_2']

out['process2']
# ['subprocess2_1']
```
