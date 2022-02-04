---
title: "Dealing with optional python dictionary fields"
site: stackoverflow
question_id: 70988817
answer_id: 70988984
url: https://stackoverflow.com/a/70988984
author: "Max"
author_url: https://stackoverflow.com/users/10522970
posted: 2022-02-04T15:36:17Z
last_edited: 2022-02-04T15:42:39Z
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c5b4c29282817146cde5378e7bf65425fa0d49d75491b10def34b7210a927ffa
role: another answer on the same question, kept as context; not my work
---

# Answer by [Max](https://stackoverflow.com/users/10522970) — 2022-02-04

Posted on Stack Overflow, <https://stackoverflow.com/a/70988984>, 2022-02-04, last edited 2022-02-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

The pythonic way of going about it would be using the `try/except` block -

```
dictionary2 = {"required": {"value1": "one", "value2": "two"}}
try:
    value1 = dictionary2["optional"]["value1"]
except (KeyError, AttributeError) as e:
    value1 = ""
```
`KeyError` to capture the missing keys, and `AttributeError` to capture cases where you have a `list`/`str` instead of `dict` object.


----------


If you don't like tons of `try/except` in your code, you can consider using a helper function - 
```
def get_val(data, keys):
    try:
        for k in keys:
            data = data[k]
        return data
    except (KeyError, AttributeError) as e:
        return ""

dictionary2 = {"required": {"value1": "one", "value2": "two"}}
print(get_val(dictionary2, ("required", "value2")))
print(get_val(dictionary2, ("optional", "value1")))
```
outputs - 
```
two

```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[c8999c 3f964f64](https://stackoverflow.com/users/11803687)** (2022-02-04): I will consider the idea of a helper function, but is there really no built-in way for this, something like dictionary2.get("optional").get("value1") or " ", which ignores the chained .get() and returns the "or" value in case the optional field is missing? Thank you for the answer!
- **[Max](https://stackoverflow.com/users/10522970)** (2022-02-04): In that case the best pythonic way would be to keep doing as one of your suggestions `dictionary2.get("optional", {}).get("value1", "")`
