---
title: "Combination Matrix of 2 dictionaries with custom function in Python"
site: stackoverflow
question_id: 75702244
url: https://stackoverflow.com/q/75702244
asked: 2023-03-11T01:15:39Z
asked_by: "Luke Sharp"
asked_by_url: https://stackoverflow.com/users/21374069
last_edited: 2023-03-11T01:17:15Z
tags: [python, pandas, dictionary]
score: -1
views_at_snapshot: 52
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b2dc00f7b446e0fbd12f4f6345073a5df5b3c9a51a38c653cdc0feb981dadb74
---

# Combination Matrix of 2 dictionaries with custom function in Python

Asked by [Luke Sharp](https://stackoverflow.com/users/21374069) on Stack Overflow, <https://stackoverflow.com/q/75702244>, 2023-03-11, last edited 2023-03-11. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have 2 dictionaries of key value pairs. I need a combination matrix representation that retains key information while performing a custom calculation on the value pair.

Input:
```
x = {'a': 1, 'b': 2}
y = {'a': 3, 'c': 4}
```

Custom function:
```
def sum(a, b):
    return a*b
```

Desired output:
```
  | a        | b        | 
a | sum(1,3) | sum(2,3) |
c | sum(1,4) | sum(2,4) |
```

Is there any elegant solution to do this? I'm struggling to produce the desired result.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Ignatius Reilly](https://stackoverflow.com/users/15032126)** (2023-03-11): Why the tag `pandas`? Is this suppose to be a DataFrame?
- **[Ignatius Reilly](https://stackoverflow.com/users/15032126)** (2023-03-11): _a combination matrix representation that retains key information_, How? What are you going to do with that? Could it be a dictionary with (xi, yj) values as keys? A dictionary with column-keys nested in a dict with row-keys? If you need a particular data structure, we need to know which operation do you need to perform on it.
