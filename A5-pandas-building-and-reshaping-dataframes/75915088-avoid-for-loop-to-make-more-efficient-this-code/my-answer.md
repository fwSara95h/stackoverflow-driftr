---
title: "Avoid for loop to make more efficient this code"
site: stackoverflow
question_id: 75915088
answer_id: 75920208
url: https://stackoverflow.com/a/75920208
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-03T13:49:57Z
last_edited: 2023-04-03T17:00:48Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75920208/revisions
accepted: true
score: 0
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f4f91f358b3b9792bd983e5fde98cfa3da2c13abebd1cb26bef287c7fb7d8293
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-03

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75920208>, 2023-04-03, last edited 2023-04-03; **accepted**; score 0. Text as retrieved 2026-10-12.

This might seem a bit hacky, but you can try with multiple [`applymap`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.applymap.html)s. [I don't know any other flexible element-wise method for DataFrames...]

```py
def my_formula(di_dm_dmm_vals):
    di_val, dm_val, dmm_val = di_dm_dmm_vals
    if di_val >= dm_val + 5*dmm_val: return dm_val + 5*dmm_val
    if di_val <= dm_val - 5*dmm_val: return dm_val - 5*dmm_val
    return di_val ## [ no need for elif/else after return ]
```

```py
listify = lambda x: [x]
df_new = di.applymap(listify) + dm.applymap(listify) + dmm.applymap(listify) 
df_new = df_new.applymap(my_formula)
```

[Using `listify` then `+` creates a DataFrame of lists of which can each can be passed as a `di_dm_dmm_vals` argument to `my_formula`.]

<sub>**Please note that this will only work properly is all 3 DataFrames have the same shape.**</sub>

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[AM27](https://stackoverflow.com/users/21551448)** (2023-04-03): it says NameError: name 'di_dm_dmm' is not defined; it referres on the second row of the function
- **me** (2023-04-03): @AlessandroMarchi sorry about the typo - it should have been `di_dm_dmm_vals` (I've corrected it)
- **[AM27](https://stackoverflow.com/users/21551448)** (2023-04-03): Thank you very much! it works and it is much much faster than before
