---
title: "Applying keys sequentially to a dict from a list"
site: stackoverflow
question_id: 75197965
answer_id: 75202896
url: https://stackoverflow.com/a/75202896
author: "crystallikelaw"
author_url: https://stackoverflow.com/users/12215120
posted: 2023-01-22T18:30:59Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: cd92f0c5692c329049c6b19ffca73a45399160774366148f9152f2423f54a1a6
role: another answer on the same question, kept as context; not my work
---

# Answer by [crystallikelaw](https://stackoverflow.com/users/12215120) — 2023-01-22

Posted on Stack Overflow, <https://stackoverflow.com/a/75202896>, 2023-01-22. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Best I could manage was using a for loop to iterate through the keys:

```
person = {'name0':{'first0': 'John', 'last0':'Smith'},
          'age0':'10',
          'location0':{'city0':'Dublin'}
         }
```
Additionally I used `.get(key)` rather than `try..except` as suggested by @wiwi

```

def func(person):
    filters = [('age', ['age0']), ('name', ['name0', 'first0'])]
    result = {'name': None, 'age': None}
    for filter in filters:
        temp = person.copy()
        for key in filter[1]:
            temp = temp.get(key)
            if not temp: # NoneType doesn't have .get method
                break
        result[filter[0]] = temp
    return result

```
`func(person)` then returns `{'name': 'John', 'age': '10'}`.

It handles missing input too: 
```
person2 = {'age0':'10',
          'location0':{'city0':'Dublin'}}
```

`func(person2)` returns `{'name': None, 'age': '10'}`
