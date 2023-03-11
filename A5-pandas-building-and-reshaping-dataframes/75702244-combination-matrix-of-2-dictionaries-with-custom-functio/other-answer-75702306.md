---
title: "Combination Matrix of 2 dictionaries with custom function in Python"
site: stackoverflow
question_id: 75702244
answer_id: 75702306
url: https://stackoverflow.com/a/75702306
author: "harriet"
author_url: https://stackoverflow.com/users/17433572
posted: 2023-03-11T01:44:35Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0eaa2d4da0c48fa6de63d0291e8865aef91d7d93d8bc7a67f0f347bcf3c81176
role: another answer on the same question, kept as context; not my work
---

# Answer by [harriet](https://stackoverflow.com/users/17433572) — 2023-03-11

Posted on Stack Overflow, <https://stackoverflow.com/a/75702306>, 2023-03-11. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You could create a dictionary that stores the return value of your function call (func(x[x_key], y[y_key]) at --> key: tuple = (x_key, y_key)

    x = {'a': 1, 'b': 2}
    y = {'a': 3, 'c': 4}

    def product(a, b):
        return a * b

    d = dict()
    for i in x:
        for j in y:
            d[(i, j)] = product(x[i], y[j])

    print(d)

This produces:

    {('a', 'a'): 3, ('a', 'c'): 4, ('b', 'a'): 6, ('b', 'c'): 8}
