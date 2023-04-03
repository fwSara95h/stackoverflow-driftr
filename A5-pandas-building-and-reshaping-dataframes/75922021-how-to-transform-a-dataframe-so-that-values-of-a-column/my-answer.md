---
title: "How to transform a dataframe so that values of a column are the column names and column names are rows but unstacked?"
site: stackoverflow
question_id: 75922021
answer_id: 75922226
url: https://stackoverflow.com/a/75922226
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-03T17:32:57Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75922226/revisions
accepted: false
score: 0
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 80f0afb2e386eab68ceb466066b7f81fc7dd7144be766855e21714691e1dcf74
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-03

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75922226>, 2023-04-03; score 0. Text as retrieved 2026-10-12.

You could [`unstack`](https://pandas.pydata.org/docs/reference/api/pandas.Series.unstack.html) and [concatenate](https://pandas.pydata.org/docs/reference/api/pandas.concat.html) like

```py
# import pandas as pd
# df = pd.read_html('https://stackoverflow.com/questions/75922021')[0]

unstacked_df = df.set_index(['User ID','Status']).unstack()

kList = {c[0] for c in unstacked_df.columns} ## {'Name','Favorite'}
dfList = [unstacked_df[k] for k in kList] ## [u__df['Name'],u__df['Favorite']]
conc_df = pd.concat(dfList, keys=kList, names=['Attribute Changed', 'User ID'])

df2Cols = ['User ID', 'Attribute Changed', 'After', 'Before']
df2 = conc_df.reset_index().rename_axis(None,axis='columns')[df2Cols]
```

|`unstacked_df`|`conc_df`|`df2`|
|:-:|:-:|:-:|
|[![unstack][1]][1]|[![concat][2]][2]|[![df2][3]][3]|


  [1]: https://i.sstatic.net/1dDHZ.png
  [2]: https://i.sstatic.net/LLfwK.png
  [3]: https://i.sstatic.net/Yy3Ry.png
