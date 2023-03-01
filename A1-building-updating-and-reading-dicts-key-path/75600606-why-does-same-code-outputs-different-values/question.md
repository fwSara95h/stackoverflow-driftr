---
title: "Why does same code outputs different values?"
site: stackoverflow
question_id: 75600606
url: https://stackoverflow.com/q/75600606
asked: 2023-03-01T07:22:22Z
asked_by: "Jvnko_Developer"
asked_by_url: https://stackoverflow.com/users/21309631
last_edited: 2023-03-01T09:04:53Z
last_editor: "pmqs"
last_editor_url: https://stackoverflow.com/users/2030808
tags: [python, dictionary, python-itertools, python-zip]
score: 0
views_at_snapshot: 116
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ee48f0b07f11e3e777603bbd0e9578b7bcc1be38864256a77a1bac4f6f28c8bb
---

# Why does same code outputs different values?

Asked by [Jvnko_Developer](https://stackoverflow.com/users/21309631) on Stack Overflow, <https://stackoverflow.com/q/75600606>, 2023-03-01, last edited 2023-03-01 by [pmqs](https://stackoverflow.com/users/2030808). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.


```
import itertools
def f(x,y,z,w):
    return ((x and y) or (y and z)) == ((not(x) or w) and (not(w) or z))

for p in itertools.permutations("xyzw"):
    ans = []
    t = [(0,1,1,1), (0,1,0,0), (0,1,0,1)]
    for r in t:
        #ans.append(f(*r))
        #ans.append(f(**dict(zip(p,r))))
    if ans == [1,1,1]:
        print(*p)
        break

```
If I uncomment `ans.append(f(*r))` it outputs nothing, but if I uncomment `ans.append(f(**dict(zip(p,r))))` it outputs my answer. Why does that happen?

I'm expecting the same output, but there are different arrays after `dict(zip)` values.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[jackal](https://stackoverflow.com/users/17580381)** (2023-03-01): Add *print(f(*r))* and you'll see why
- **[blhsing](https://stackoverflow.com/users/6890912)** (2023-03-01): You aren't using `p` at all if you do `ans.append(f(*r))`, so how is it "the same code" as `ans.append(f(**dict(zip(p,r))))`?
- **[Jvnko_Developer](https://stackoverflow.com/users/21309631)** (2023-03-01): i dont understand why *r and **dict(zip(p,r)) sometimes output different values
- **[Jvnko_Developer](https://stackoverflow.com/users/21309631)** (2023-03-01): im making keys for dict from `r`, so i think that `r` and keys from dict should be equal, but they arent
- **[blhsing](https://stackoverflow.com/users/6890912)** (2023-03-01): No, you're making keys for dict from `p`, not `r`. `r` is where you draw values from.
