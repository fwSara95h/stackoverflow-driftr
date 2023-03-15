---
title: "How to convert a dictionary with DataFrame values to DataFrame using Pandas"
site: stackoverflow
question_id: 75747803
answer_id: 75750483
url: https://stackoverflow.com/a/75750483
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-15T22:05:02Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75750483/revisions
accepted: false
score: 0
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 85f1f748974356af58aeda6217ce0b35d7e20e2fbeada4ba1c7971ee2c5ad308
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-15

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75750483>, 2023-03-15; score 0. Text as retrieved 2026-10-12.

> *Try `df_join = pd.concat(dict)` (NB. Don't use `dict` as variable name, this is a python built-in)* 
>
> <sup>- [comment](https://stackoverflow.com/questions/75747803/how-to-convert-a-dictionary-with-dataframe-values-to-dataframe-using-pandas#comment133623944_75747803) by [mozway](https://stackoverflow.com/users/16343464/mozway)</sup>

[`concat`](https://pandas.pydata.org/docs/reference/api/pandas.concat.html) is the simplest [and probably the most efficient] way to join multiple DataFrames together.

> *I need to add an additional column to each data frame and then specify the indices* - [about `R1` and `R2`]

You can use the `keys` argument to do so

```py
df_join = pd.concat([df1,df2], keys=['R1','R2'])

# for a list of DataFrames of unknown length: 
# df_join = pd.concat(dfs_list, keys=[f'R{i}' for i in range(1, len(dfs_list)+1)])
```

---

And if you really want to combine them as dictionaries first for some reason, you can do it on loop

```py
dfs_list = [df1, df2]
index_join, data_join = [], []
for di, df in enumerate(dfs_list):
    data_join += df.to_dict('records')

    index_join += [(f'R{di}', *i) for i in df.index] # if df is multi-indexed
    # index_join += list(df.index) # if df is not multi-indexed

df_join = pd.DataFrame(data=data_join, index=pd.MultiIndex.from_tuples(index_join))   
```

or with dictionary comprehension

```py
df_join = pd.DataFrame.from_dict({
    (f'R{di}', *df_index): df_row for di,df in enumerate([df1,df2]) 
    for df_index, df_row in df.to_dict('index').items()
}, orient="index")
```

which effectively does the same as if you edited your code to

```py
dict_val = {}
dict_val.update({('R1',i1,i2):row for (i1,i2), row in df1.to_dict('index').items()})
dict_val.update({('R2',i1,i2):row for (i1,i2), row in df2.to_dict('index').items()})
df_join = pd.DataFrame.from_dict(dict_val, orient="index")
```
