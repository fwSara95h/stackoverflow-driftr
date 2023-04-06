---
title: "convert txt into dictionaries"
site: stackoverflow
question_id: 75947650
answer_id: 75949375
url: https://stackoverflow.com/a/75949375
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-06T12:10:27Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75949375/revisions
accepted: true
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: aa669a84fd80bf70634a88868317b6149a1325a737c88186c1edc012f6d2543f
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-06

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75949375>, 2023-04-06; **accepted**; score 0. Text as retrieved 2026-10-12.

Try using [`.readlines`](https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/) and then [combine](https://www.geeksforgeeks.org/python-convert-two-lists-into-a-dictionary/) the first line with every other line with [`zip`](https://www.programiz.com/python-programming/methods/built-in/zip) to form each dictionary in **`dict_list`** below:

```py
input_fp = 'x.txt' ## set the path to the ACTUAL file
sep_str = None # ' ' # ',' # ' | ' # '\t' # 

with open(input_fp) as f:
    # text_lines = [l.rstrip() for l in f.readlines()] # keep empty lines
    text_lines = [l.rstrip() for l in f.readlines() if l.strip()] ## no empty lines

dKeys = text_lines[0].split(sep_str) if text_lines else [] 

maxSplits = len(dKeys) - 1
dict_list = [dict(zip(dKeys, tl.split(sep_str,maxSplits))) for tl in text_lines[1:]]
```

- You can also use `f.read().strip().splitlines()` instead of *`f.readlines()`* and omit the *`if l.strip()`* part if you want to skip whitespace at the beginning but still represent empty lines later on with empty dictionaries (`{}`).
- Use `l.strip()` instead of *`l.rstrip()`* if you might have spaces at the beginning of lines that you need to ignore.
- Omit `maxSplits` if you don't want to mash the last "word"s together if a line has more "word"s than in the fist line. For example, if your file contains <kbd>*`'k1 k2 k3\nv1 v2 v3 v4'`*</kbd>, then
  - as it is above, it would be converted to **`[{'k1': 'v1', 'k2': 'v2', 'k3': 'v3 v4'}]`** 
  - but if you only used 
    ```py
    dict_list = [dict(zip(dKeys, tl.split(sep_str))) for tl in text_lines[1:]]
    ```
    then the resulting `dict_list` would be **`[{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}]`** (i.e., `v4` would be cropped out instead of being tacked onto `v3`)
- About the `sep_str` value that will be used to [`.split`](https://www.programiz.com/python-programming/methods/string/split) each line into values:
  - `sep_str=None` --> *`'v1  v2 v3'.split()`* would return **`['v1', 'v2', 'v3']`**
  - `sep_str= ' '` --> *`'v1  v2 v3'.split(' ')`* would return **`['v1', '', 'v2', 'v3']`**

---

For an example, if your file contained

```py
First_Name Last_Name Gender Age Phone Occupation
Penelope Miller Female 23 069-5515-87 Teacher
Julian Watson Male 19 355-0427-79 Cook
Gianna Barnes Female 27 641-6494-91 Mechanic
Walter Walker Male 28 164-8407-47 Mechanic
Chelsea Scott Female 28 272-2601-10 Florist
```

then the resulting `dict_list` should be:

> ```py
> [
>   {'First_Name': 'Penelope', 'Last_Name': 'Miller', 'Gender': 'Female', 'Age': '23', 'Phone': '069-5515-87', 'Occupation': 'Teacher'},
>   {'First_Name': 'Julian', 'Last_Name': 'Watson', 'Gender': 'Male', 'Age': '19', 'Phone': '355-0427-79', 'Occupation': 'Cook'},
>   {'First_Name': 'Gianna', 'Last_Name': 'Barnes', 'Gender': 'Female', 'Age': '27', 'Phone': '641-6494-91', 'Occupation': 'Mechanic'},
>   {'First_Name': 'Walter', 'Last_Name': 'Walker', 'Gender': 'Male', 'Age': '28', 'Phone': '164-8407-47', 'Occupation': 'Mechanic'},
>   {'First_Name': 'Chelsea', 'Last_Name': 'Scott', 'Gender': 'Female', 'Age': '28', 'Phone': '272-2601-10', 'Occupation': 'Florist'}
> ]
> ```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Frank Vel](https://stackoverflow.com/users/4000964)** (2023-04-06): There is no need to use `f.readlines()`,  `f` is already an iterator.
- **[Lynn](https://stackoverflow.com/users/21579646)** (2023-04-06): Thanks that's really helpful and easy to follow!!
