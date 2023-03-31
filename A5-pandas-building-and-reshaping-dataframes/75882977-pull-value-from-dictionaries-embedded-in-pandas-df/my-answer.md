---
title: "Pull value from dictionaries embedded in pandas df"
site: stackoverflow
question_id: 75882977
answer_id: 75894702
url: https://stackoverflow.com/a/75894702
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-31T03:45:09Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75894702/revisions
accepted: true
score: 0
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0bf8e3ce9f24235d999679d7545ea41971f2b2fa6feed9427307daf354e0efbf
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-31

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75894702>, 2023-03-31; **accepted**; score 0. Text as retrieved 2026-10-12.

Given this `df`:

```py
df = pd.DataFrame([
    [ 'XYZ', {'all': 27026}, {'all': 2042} ], 
    [ 'QWE', {'$overall': {'all': 6}, 'Mar 18, 2021': {'all': 3}, 'Mar 3, 2021': {'all': 3}}, {'$overall': {'all': 3}, 'Mar 3, 2021': {'all': 2}, 'Mar 18, 2021': {'all': 1}}]
], index=['$XYZ', 'QWE'], columns=['Name', 'A', 'B'])
```

[![origDF][1]][1]

---

There's probably a more elegant way to do it [maybe with [`json_normalize`](https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html) on the dictionary or [`.explode`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.explode.html)...], but this should work:


```py
nested_index = 'Date'
expand_rows = ['QWE'] # include indices of rows with dates
expand_cols = ['A','B'] # include names of columns with dates

static_cols = [c for c in df.columns if c not in expand_cols]
exp_dfs = []
for ind in expand_rows:
    df_ind = pd.DataFrame(df.loc[ind][expand_cols].to_dict())
    df_ind = df_ind.drop('$overall',axis='rows')
    df_ind = df_ind.rename_axis(nested_index).reset_index()
    for c in static_cols: df_ind[c] = df.loc[ind][c]
    exp_dfs.append(df_ind.set_index(pd.Series([ind]*len(df_ind))))

exp_df = pd.concat([df.drop(expand_rows, axis='rows')]+exp_dfs)
exp_df = exp_df.applymap(lambda x: getattr(x,'get',{'all':x}.get)('all', x))
```

|`exp_df`|`exp_df[[*static_cols, nested_index, *expand_cols]]`|`exp_df.set_index('Date', append=True)`|
|:-:|:-:|:-:|
|[![exp_df][2]][2]|[![colsList][3]][3]|[![appendIndex][4]][4]|


  [1]: https://i.sstatic.net/2Xfql.png
  [2]: https://i.sstatic.net/3MT5q.png
  [3]: https://i.sstatic.net/RAEvU.png
  [4]: https://i.sstatic.net/l71cD.png
