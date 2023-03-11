---
title: "Combination Matrix of 2 dictionaries with custom function in Python"
site: stackoverflow
question_id: 75702244
answer_id: 75702340
url: https://stackoverflow.com/a/75702340
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-11T01:57:23Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75702340/revisions
accepted: false
score: 0
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 986b21e051ba248a148e298f6f8e448cda3311807b53dec4ab4c1e5021003161
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-11

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75702340>, 2023-03-11; score 0. Text as retrieved 2026-10-12.

[I'm assuming you want the output as a DataFrame as your question has pandas as a tag.]

```py
# import pandas as pd

x = {'a': 1, 'b': 2}
y = {'a': 3, 'c': 4}
custom_function = lambda v1,v2: f'{v1}*{v2} = {v1*v2}'

df = pd.DataFrame({col:{
    ind: custom_function(cv, rv) for ind, rv in y.items()
} for col, cv in x.items()})
```

will result in `df` returning

>```py
> ╒════╤═════════╤═════════╕
> │    │ a       │ b       │
> ╞════╪═════════╪═════════╡
> │ a  │ 1*3 = 3 │ 2*3 = 6 │
> ├────┼─────────┼─────────┤
> │ c  │ 1*4 = 4 │ 2*4 = 8 │
> ╘════╧═════════╧═════════╛
>```
>
> <sup>(Printed with `print(df.to_markdown(tablefmt='fancy_grid'))`)</sup>

---

The dictionary used to build the DataFrame 

```py
{col:{ind: custom_function(cv, rv) for ind, rv in y.items()} for col, cv in x.items()}
```

looks like

> ```py
> {'a': {'a': '1*3 = 3', 'c': '1*4 = 4'}, 'b': {'a': '2*3 = 6', 'c': '2*4 = 8'}}
> ```
