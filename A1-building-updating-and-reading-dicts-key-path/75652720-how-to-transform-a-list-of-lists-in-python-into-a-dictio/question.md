---
title: "How to transform a list of lists in Python into a dictionary"
site: stackoverflow
question_id: 75652720
url: https://stackoverflow.com/q/75652720
asked: 2023-03-06T15:28:09Z
asked_by: "Carabes"
asked_by_url: https://stackoverflow.com/users/7179546
last_edited: 2023-03-06T15:57:06Z
tags: [python, dictionary, graph]
score: -2
views_at_snapshot: 71
answer_count: 1
accepted_answer_id: 75653416
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 32c770e17ec6d624458fd3b749774c9e5975b2751c2727fcdbb935ede1dd4321
---

# How to transform a list of lists in Python into a dictionary

Asked by [Carabes](https://stackoverflow.com/users/7179546) on Stack Overflow, <https://stackoverflow.com/q/75652720>, 2023-03-06, last edited 2023-03-06. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have in Python an structure like this one

```
example = {
    ['g': 'h'],
    [
        {'a':'b'}, {'c': 'd'},
        {'a':'b'}, {'e', 'f'}
     ]
}
```

I want to create a dictionary that represents the information of this list considering it a graph in the sense that the info goes from left to right

The output I want, for the example above is:
```
output = {
{'a': 
    {'b': 
            {'c': 'd'},
            {'e', 'f'}
     }
     ,
    {'g': 'h'}
}
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Abdul Aziz Barkat](https://stackoverflow.com/users/14991864)** (2023-03-06): Your output is not a valid Python object. Also what output should something like `['Q']` produce if it succeeded by nothing else?
- **[RifloSnake](https://stackoverflow.com/users/20959773)** (2023-03-06): I'm not quite understanding the pattern it should follow.
