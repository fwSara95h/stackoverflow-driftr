---
title: "Applying keys sequentially to a dict from a list"
site: stackoverflow
question_id: 75197965
answer_id: 75201700
url: https://stackoverflow.com/a/75201700
author: "Tranbi"
author_url: https://stackoverflow.com/users/13525512
posted: 2023-01-22T15:40:11Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 64e39c1b8b77b312993994392a559b65112f61083273709e945ebfb553077031
role: another answer on the same question, kept as context; not my work
---

# Answer by [Tranbi](https://stackoverflow.com/users/13525512) — 2023-01-22

Posted on Stack Overflow, <https://stackoverflow.com/a/75201700>, 2023-01-22. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

In order to follow several key sequentially, you can use [get](https://www.geeksforgeeks.org/python-dictionary-get-method/) and set the default value to `{}` (empty dictionary) for the upper levels. Set the default value to `None` (or whatever suits you) for the last level:
```python
def func(person):
    return {'name': person.get('name0', {}).get('first0', None),
            'age': person.get('age0', None)}
```
