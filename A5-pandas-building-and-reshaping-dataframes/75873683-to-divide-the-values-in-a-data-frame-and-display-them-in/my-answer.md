---
title: "To divide the values in a data frame and display them in the row below"
site: stackoverflow
question_id: 75873683
answer_id: 75874944
url: https://stackoverflow.com/a/75874944
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-29T08:42:15Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75874944/revisions
accepted: false
score: 1
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f107bfd5494995aad66eafe6570e1fdc1507b571150109bf92f36649a7779a82
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-29

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75874944>, 2023-03-29; score 1. Text as retrieved 2026-10-12.

After using [`.str.split`](http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.split.html) to change `feature` to a Series of lists, you can [`.explode`](http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.explode.html) those lists into multiple rows [as in *`df_exp`* below].

To wrangle the duplicates, you could 
- just use [`.set_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html) to convert the entire DataFrame to a [multiindex](https://pandas.pydata.org/docs/user_guide/advanced.html#hierarchical-indexing-multiindex) [like *`df_exp_mi`* below], or
- empty out the duplicate cells [like in *`df_exp_nodup`* below] by finding them with [`.duplicated`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html) and then
  - either just set them with a Boolean [`.loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html) (like in jezrael's answer)
  - or use [`.mask`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mask.html) on the first two columns.

```py 
target_col = 'feature'
other_cols = [c for c in df.columns if c!=target_col]

## before clearing out duplicates
df_exp = df.assign(**{target_col:df['feature'].str.split('/')}).explode(target_col)

## convert whole df into a multiIndex
df_exp_mi = df_exp.set_index(other_cols+[target_col]) 

## just empty out duplicate cells
df_exp_nodup = df_exp.copy() ## not necessary, only copying for demo stages
# df_exp_nodup.loc[df_exp.index.duplicated(), ['model','kind']] = '' # simpler
dups = df_exp.duplicated(subset=['model', 'kind'])
for c in other_cols: df_exp_nodup[c] = df_exp_nodup[c].mask(dups, '')
```

|`df_exp`|`df_exp_mi`|`df_exp_nodup`|
|:-:|:-:|:-:|
|[![df_exp][1]][1]|[![df_exp_mi][2]][2]|[![df_exp_nodup][3]][3]|


  [1]: https://i.sstatic.net/VoqSe.png
  [2]: https://i.sstatic.net/VHckA.png
  [3]: https://i.sstatic.net/LzCuR.png
