---
title: "Trying to replace old \"names\" with new \"names\" in Python"
site: stackoverflow
question_id: 75655920
answer_id: 75655981
url: https://stackoverflow.com/a/75655981
author: "Samwise"
author_url: https://stackoverflow.com/users/3799759
posted: 2023-03-06T21:23:29Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 34a4c4209ab1e45a5d60394b647a1f42cc62f2d3d477810878a38ea2e187aa35
role: another answer on the same question, kept as context; not my work
---

# Answer by [Samwise](https://stackoverflow.com/users/3799759) — 2023-03-06

Posted on Stack Overflow, <https://stackoverflow.com/a/75655981>, 2023-03-06. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Given a CSV file that looks something like:

```
apple-er3,horse-er45
alk-er43,erk-bf43
```

you can build a dictionary that translates between the two very easily:

```
import csv

with open('names.csv') as f:
    name_trans = dict(csv.reader(f))
```

`dict()` will take an iterable of pairs (which is what a `csv.reader` of a 2-column CSV file will give you) and turn it into a dictionary where the first item is the key and the second item is the value, so the above two lines of code is all you need to build the name translation dictionary you want.

If the CSV has a header you need to skip, or if it has other columns you need to ignore, those are modifications that only represent another line or two of code; the basic strategy is the same.

Once you have `name_trans` you can do:

```
new_name = name_trans[old_name]
```

to translate any `old_name` to its corresponding `new_name`.
