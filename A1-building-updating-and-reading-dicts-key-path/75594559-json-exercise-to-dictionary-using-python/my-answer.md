---
title: "Json Exercise to dictionary using python"
site: stackoverflow
question_id: 75594559
answer_id: 75595401
url: https://stackoverflow.com/a/75595401
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-28T17:27:31Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75595401/revisions
accepted: false
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3271c4e711d75d871b59bf45f066cb8ed9ebcd3dd99214aa72b84131bea6f60a
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-28

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75595401>, 2023-02-28; score 0. Text as retrieved 2026-10-12.

> 2- *The Database where the information will be ingested does not support columns of different data types. To do this, a function must be generated that corrects this in the inputs.*

You could use a function like this to enforce datatypes:

```py
def format_empData(val, key, enforce=False, defaultVal=None):
    if key == 'ID':
        try: return int(val[0] if val and isinstance(val, list) else val)
        except: return defaultVal if enforce else val
    return str(val)
``` 

---

> 1- *The employee of Identifier 2 is under the charge of the Manager with Identifier 3.*

You can loop through the departments until you find the right one and then add `employee` after processing each value in it with `format_empData`:

```py
managerId = 3
for di, dept in enumerate(department):
    if dept['ID'] == managerId:
        department[di]['employees'].append(
            {k: format_empData(v, k) for k, v in employee.items()})
        break
```

After that, `department` should look like

>```py
> [{'ID': 1, 'Name': 'John', 'Role': 'Manager',
>   'employees': [{'ID': 4, 'Name': 'Mike', 'Role': 'Engineer'}]},
>  {'ID': 3, 'Name': 'Sam', 'Role': 'Manager',
>   'employees': [{'ID': 2, 'Name': 'Jack', 'Role': 'Analyst'}]}]
>```
