---
title: "How to make a comprehensive composition table efficiently"
site: stackoverflow
question_id: 75923863
answer_id: 75925193
url: https://stackoverflow.com/a/75925193
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-04T02:59:06Z
last_edited: 2023-04-04T12:04:14Z
revisions: 3
revision_history: https://stackoverflow.com/posts/75925193/revisions
accepted: true
score: 1
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a9e39293041683ad3af649ba462cba417b9bb2480bbfc4f091f20ea52db71386
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-04

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75925193>, 2023-04-04, last edited 2023-04-04; **accepted**; score 1. Text as retrieved 2026-10-12.

You could use [`itertools.product`](https://docs.python.org/3/library/itertools.html#itertools.product) and then filter out the compositions that exceed the limit with [list comprehension](https://www.programiz.com/python-programming/list-comprehension).

```py
import itertools

def get_compositions(raw_materials:list, factor_x:int,lim_y:int,col_prefix='Material '):
    multiples = [factor_x*i for i in range(int(lim_y/factor_x)+1)]
    cart_prod = itertools.product(multiples, repeat=len(raw_materials))
    composites = [c for c in cart_prod if sum(c)<=lim_y] ## filter

    composite_labels = [f'Composite{i}' for i in range(1, len(composites)+1)]
    material_labels = [f'{col_prefix}{m}' for m in raw_materials]

    return pd.DataFrame(composites, index=composite_labels, columns=material_labels)
```

<kbd>**`get_compositions(['A', 'B','C'], 1, 2)`**</kbd> should return 

> [![opdf][1]][1]


  [1]: https://i.sstatic.net/O0Zei.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[hiro](https://stackoverflow.com/users/15115362)** (2023-04-04): Thank you for your answer which solves my problem. Based on your codes, I could make a table even when factor_x is float.
- **me** (2023-04-04): @hiro glad to help! But I don't think my original code would have worked properly with float `factor_x` values because of the *`range((lim_y//factor_x)+1)`* part [also, I forgot to multiply `factor_x` accross `range`]; so I've edited it to `range(int(lim_y/factor_x)+1)` and added `factor_x*i for i in...` in `multiples` ([view example with floating point `factor_x`](https://i.sstatic.net/MhO2P.png))
- **[hiro](https://stackoverflow.com/users/15115362)** (2023-04-04): Thank you for updating your codes. When factor_x wass float, I deleted ":int", and multiplied factor_x and lim_y by 10, and fainally 0.1 was multiplied. However, your new codes look much better, so I will use yours. Thank you.
