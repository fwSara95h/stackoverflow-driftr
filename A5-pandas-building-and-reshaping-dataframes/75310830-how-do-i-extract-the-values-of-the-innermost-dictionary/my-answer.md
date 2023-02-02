---
title: "How do I extract the values of the innermost dictionary of a 3-level dictionary and save those values in a Pandas DataFrame?"
site: stackoverflow
question_id: 75310830
answer_id: 75325285
url: https://stackoverflow.com/a/75325285
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-02T15:20:51Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75325285/revisions
accepted: false
score: 0
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0d06bc135c0391176abc49eaaed1927b71b0bde4a8ccb530a3981c9f21c7d58a
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-02

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75325285>, 2023-02-02; score 0. Text as retrieved 2026-10-12.

> I want to save the data in four Pandas DataFrames

I'll assume you're okay with nested DataFrames, since you haven't specified otherwise, and your desired output structure indicates nothing against it. If you want to flatten it, then I'd need more details about the output structure and preferably some sample of the output as well.

---

You could use something like

```python
def dict2df(seasonDict:dict):
    df = pd.DataFrame(seasonDict).T.rename_axis('Year', axis='rows')
    return df.rename(lambda n: f'Hour {n}', axis='columns')
```

or

```python
def dict2df(seasonDict:dict):
    return pd.DataFrame([{'Year': yk, **{
        f'Hour {hk}': hdf for hk, hdf in yd.items()
    }} for yk, yd in seasonDict.items()]).set_index('Year')
```

[ I wrote the second one before I realized/discovered that *<kbd>{column->{index->value}}</kbd>* is a valid input structure for `pd.DataFrame` and that the 4 dictionaries in `pm_10_abs_season` have an *<kbd>{index->{column->value}}</kbd>* structure, which just needs to be [transposed](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transpose.html) (`.T`) to get quite close to your desired output structure. The second version does appear to be a tiny bit faster (about 10%) but I'm not sure if you'd consider that significant enough to matter.]

---

Anyway, I generated a **test input** ([<kbd>`seasons_dfs`</kbd>][1]) to mimic your `pm_10_abs_season` (but the DataFrames inside just have one cell containing the string `'<DataFrame>'`)

```python
seasonRef = {k:v for k,v in enumerate(['winter','spring','summer','autumn'],1)}
# seasonRef = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}

seasons_dfs = {sk: {yk: {
    hk: pd.DataFrame(
        {f'{sn[0]}_{str(yk)[-2:]}':{f'hour{hk:0>2}':f'<DataFrame>'}}
    ) for hk in range(24)
} for yk in range(2005,2019)} for sk,sn in seasonRef.items()}
```

and then used the function <sup>(*`dict2df(sd)`*)</sup> to convert it to a dictionary of DataFrames ([<kbd>`nestedDfs`</kbd>][2]).

```python
nestedDfs = {
    seasonRef.get(s, f'[season {s}]'): dict2df(sd) 
    for s, sd in seasons_dfs.items()
}
```

The 4 DataFrames inside `nestedDfs` should have your desired output structure:
[![winter][3]][3]
[![spring][4]][4]
[![summer][5]][5]
[![autumn][6]][6]


  [1]: https://i.sstatic.net/dBVce.png
  [2]: https://i.sstatic.net/BuH1l.png
  [3]: https://i.sstatic.net/txfeN.png
  [4]: https://i.sstatic.net/opOR6.png
  [5]: https://i.sstatic.net/E5nca.png
  [6]: https://i.sstatic.net/I1uw5.png
