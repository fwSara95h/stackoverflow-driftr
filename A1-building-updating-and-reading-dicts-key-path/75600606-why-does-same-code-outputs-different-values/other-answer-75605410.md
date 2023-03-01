---
title: "Why does same code outputs different values?"
site: stackoverflow
question_id: 75600606
answer_id: 75605410
url: https://stackoverflow.com/a/75605410
author: "Jeff"
author_url: https://stackoverflow.com/users/5905029
posted: 2023-03-01T14:59:00Z
last_edited: 2023-03-01T15:15:43Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f944877d84b8925d347585c2224e049ab52911c47c98704626a05fbdf016c2fd
role: another answer on the same question, kept as context; not my work
---

# Answer by [Jeff](https://stackoverflow.com/users/5905029) — 2023-03-01

Posted on Stack Overflow, <https://stackoverflow.com/a/75605410>, 2023-03-01, last edited 2023-03-01. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

The reason you're getting different outputs is because the two function calls are not passing the same values to the arguments of `f()`:

- `f(*r)` passes positional arguments from the array of tuples `t`, with the first value being assigned to `x`, the second to `y`, the third to `z`, and the fourth to `w`. So no matter what `p` is, you're getting `ans = [f(0,1,1,1), f(0,1,0,0), f(0,1,0,1)]`.

- `f(**dict(zip(p,r)))` passes keyword arguments with the expected keys `x`, `y`, `z`, `w`, but the order in which the values from the array of tuples `t` are assigned to `x`, `y`, `z`, `w` is determined by the current permutation `p`. For example, on the first iteration of the for loop, with `p = ('x', 'y', 'z', 'w')`, you'll get `ans = [f(x=0,y=1,z=1,=w=1), ...]` equivalent to `[f(0,1,1,1), ...]` as in the positional argument version above, but on a later iteration, with `p = ('y', 'x', 'z', 'w')` you'll get `ans = [f(y=0,x=1,z=1,w=1), ...]` (**note the inverted assignments of values to x and y**) which is equivalent to `ans = [f(1,0,1,1), ...]`.
