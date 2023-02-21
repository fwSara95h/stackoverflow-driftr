---
title: "Pandas - look up key and map dictionary to a column"
site: stackoverflow
question_id: 75515493
answer_id: 75516107
url: https://stackoverflow.com/a/75516107
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-21T03:42:14Z
last_edited: 2023-02-21T08:55:40Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75516107/revisions
accepted: false
score: 1
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: [getVal]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1c03a6d35ea3664060de31b3f5856793135f20bf51447b5320df3a41c19a9f23
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-21

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75516107>, 2023-02-21, last edited 2023-02-21; score 1. Text as retrieved 2026-10-12.

Both your definitions raise some kind of error [*`df`* because all columns need to have the same length and `d` just had 1 item, and *`dtd`* because *`['sv1': 500]`* is not valid syntax]. However, if you had

```python
# import pandas as pd
# import numpy as np

df = pd.DataFrame({ 'id': [0, 1, 2], 'nm': ['pn1','pn2','pn3'], 
                    'v': [np.nan, 25, 0], 
                    'd': [{'k1':'v1'},{'k2':'v2'},{'k3':'v3'}] })
dtd = { 'pn1':{'s':100,'v':20, 'sv':{'sv1': 500}},
        'pn2':{'s':150,'v':30, 'sv':{'sv1': 400}}  }
```

then you could use something like the function below for extracting nested values <sub>[see [this question](https://stackoverflow.com/q/70988817/6146136) if you're interested in other variations of it]</sub>

```python
def getVal(obj, *keys, vDef=None):
    try: 
        for k in keys: obj = obj[k]
    except: obj = vDef
    return obj
```

---

If you want to use `.map` or `.apply` to create the new column,

```python
sv1 = df['nm'].map(lambda k: getVal(dtd, k, 'sv', 'sv1', vDef=np.nan))
# sv1 = df['nm'].apply(lambda k: getVal(dtd, k, 'sv', 'sv1', vDef=np.nan))

df['v'] = sv1.combine_first(df['v'])
```

<br>

or you can use `.combine` directly


```python
df['v'] = df['nm'].combine(df['v'], lambda k,vd: getVal(dtd,k,'sv','sv1',vDef=vd))
```

<br>

or you can also use list comprehension <sub>(I find it more readable, but it's mostly just a personal preference)</sub>

```python
df['v'] = [getVal(dtd,k,'sv','sv1',vDef=vd) for k,vd in zip(df['nm'],df['v'])]
```

---

whichever of the 3 methods is used, the resulting `df` should look like 

>```python
> ╒════╤══════╤══════╤═════╤══════════════╕
> │    │   id │ nm   │   v │ d            │
> ╞════╪══════╪══════╪═════╪══════════════╡
> │  0 │    0 │ pn1  │ 500 │ {'k1': 'v1'} │
> ├────┼──────┼──────┼─────┼──────────────┤
> │  1 │    1 │ pn2  │ 400 │ {'k2': 'v2'} │
> ├────┼──────┼──────┼─────┼──────────────┤
> │  2 │    2 │ pn3  │   0 │ {'k3': 'v3'} │
> ╘════╧══════╧══════╧═════╧══════════════╛
>```
>
> <sub>[ printed with `print(df.to_markdown(tablefmt='fancy_grid'))` ]</sub>
