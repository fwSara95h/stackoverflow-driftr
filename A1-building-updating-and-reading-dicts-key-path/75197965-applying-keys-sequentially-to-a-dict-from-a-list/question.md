---
title: "Applying keys sequentially to a dict from a list"
site: stackoverflow
question_id: 75197965
url: https://stackoverflow.com/q/75197965
asked: 2023-01-22T03:16:28Z
asked_by: "crystallikelaw"
asked_by_url: https://stackoverflow.com/users/12215120
last_edited: never
tags: [python, dictionary]
score: 0
views_at_snapshot: 81
answer_count: 3
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0200e545f49c3b7b428f30fb6d417b5f354af160d7b3ed9f59002d8cfbffdd9a
---

# Applying keys sequentially to a dict from a list

Asked by [crystallikelaw](https://stackoverflow.com/users/12215120) on Stack Overflow, <https://stackoverflow.com/q/75197965>, 2023-01-22. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm scraping a website, which returns a dictionary:

```
person = {'name0':{'first0': 'John', 'last0':'Smith'},
          'age0':'10',
          'location0':{'city0':'Dublin'}
         }
```

I'm trying to write a function that will return a dictionary `{'name':'John', 'age':'10'}` when passed the above dictionary.

I want to ideally put a `try:... except KeyError` around each item since sometimes keys will be missing.

```
def func(person):
    filters = [('age', 'age0'), ('name', ['name0', 'first0'])]
    result = {'name': None, 'age': None}
    for i in filters:
        try:
            result[i[0]] = person[i[1]]
        except KeyError:
            pass
    return result
```

The problem is `result[i[0]] = person[i[1]]` doesn't work for 'name' since there's two keys that need to be followed sequentially and I don't know how to do that.

I want some way of telling it (in the loop) to go to `person['name0']['first0']` (and so on to whatever depth the thing I want is).

I have lots of things to extract, so I'd rather do it in a loop instead of a `try..except` statement for each variable individually.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[wwii](https://stackoverflow.com/users/2823755)** (2023-01-22): Does [Flatten an irregular (arbitrarily nested) list of lists](https://stackoverflow.com/questions/2158395/flatten-an-irregular-arbitrarily-nested-list-of-lists) answer your question?
- **[wwii](https://stackoverflow.com/users/2823755)** (2023-01-22): You can use [dict.get()](https://docs.python.org/3/library/stdtypes.html#dict.get) to handle missing keys instead of using try/except.
- **[wwii](https://stackoverflow.com/users/2823755)** (2023-01-22): Some other ideas: [Nested dictionary value from key path](https://stackoverflow.com/questions/31033549/nested-dictionary-value-from-key-path).  [Python: Easily access deeply nested dict (get and set)](https://stackoverflow.com/questions/3797957/python-easily-access-deeply-nested-dict-get-and-set).
- **[Lidor Eliyahu Shelef](https://stackoverflow.com/users/8405296)** (2023-01-22): Can you supply the website you are trying to scrape?
