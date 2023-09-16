---
title: "Filter strings in a list for for numbers at specific index"
site: stackoverflow
question_id: 77115962
answer_id: 77116197
url: https://stackoverflow.com/a/77116197
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-09-16T03:04:46Z
last_edited: 2023-09-16T19:02:18Z
revisions: 2
revision_history: https://stackoverflow.com/posts/77116197/revisions
accepted: true
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c23b8394eabee9c03206c4cbc32992fa859fb6956d5c8347c0bb6ac5892237d0
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-09-16

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/77116197>, 2023-09-16, last edited 2023-09-16; **accepted**; score 0. Text as retrieved 2026-10-12.

You could do something like

```py
rest = ["town name", "state", "98420", "description"],["222", "street", "state", "98420", "description"], ["town name", "state", "94820", "description"]

addr = []
for i in rest:
    addr_i = i[:1] # don't check the first string
    for j in i[1:]:
        addr_i.append(j)
        if j.isnumeric(): break # stop if numeric
    addr.append(addr_i)
```

resulting `addr`:

```py
[['town name', 'state', '98420'], ['222', 'street', 'state', '98420'], ['town name', 'state', '94820']]
```

---

#### EDIT :

> *can you help me get the rest of the list into a new list called serv?*

You could use [`enumerate`](https://realpython.com/python-enumerate/) and do something like

```py
rest = ["town name", "state", "98420", "description"],["222", "street", "state", "98420", "description"], ["town name", "state", "94820", "description"]

addr, serv = [], []
for i in rest:
    addr_i = i[:1] # don't check the first string
    for n, j in enumerate(i[1:],1):
        addr_i.append(j)
        if j.isnumeric(): 
            serv.append(i[n+1:]) # rest of the strings
            break # stop if numeric
    else: serv.append([]) ## no numerics found
    addr.append(addr_i)
```

> ```py
> addr = [['town name', 'state', '98420'], ['222', 'street', 'state', '98420'], ['town name', 'state', '94820']]
> serv = [['description'], ['description'], ['description']]
> ```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Jackie Marie](https://stackoverflow.com/users/22572344)** (2023-09-16): This solves it, thank you so much for the help and the break down too!
- **[Jackie Marie](https://stackoverflow.com/users/22572344)** (2023-09-16): By chance can you help me get the rest of the list into a new list called serv?  serv (short for services) Like the all of the descriptions, I decided to iterate through the  list in reverse and want to stop at the zip code again, but this time, not include it.
- **me** (2023-09-16): @JackieMarie see my edit. hope it helps
