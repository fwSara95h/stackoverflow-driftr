---
title: "Is there a 'rowspan' or 'merge two table cells to single table cell' function for pandas tables/dataframes?"
site: stackoverflow
question_id: 75933430
answer_id: 75935246
url: https://stackoverflow.com/a/75935246
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-05T02:40:50Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75935246/revisions
accepted: false
score: 0
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2731103d9bbb1d8f825c56a432e9b0d6d579d6881fb3f888336ee9fdb86fe6bd
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-05

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75935246>, 2023-04-05; score 0. Text as retrieved 2026-10-12.

Pandas doesn't really do merged cells (as some have already commented); although, index columns do get grouped together:

```py
data={'index': [('LCS', 'sequence1'), ('LCS', 'sequence2')], 'columns': ['alignment', 'score', 'pathcoordinates'], 'data': [['AAAGT', 5, '[4,5] -> [5,5]'], ['GGTAC', 5, '[4,5] -> [5,5]']], 'index_names': ['', 'sequence'], 'column_names': ['']}

df1 = pd.DataFrame.from_dict(data, orient='tight')
df2 = df1.reset_index().set_index(['', 'score', 'pathcoordinates', 'sequence'])
```

|`df1`||`df2`|
|:-:|:-:|:-:|
|[![df1][1]][1]|**⇨**|[![df2][2]][2]|

<br>

and [`.to_excel`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html) will output those grouped labels as merged cells, even though most other writer methods wouldn't:

| Output Type | Example |
|:-:|:-:|
| Excel |[![xlsx_op][5]][5]|
| Markdown |[![md_op][3]][3]|
| CSV |[![csv_op][4]][4]|


  [1]: https://i.sstatic.net/UOP5S.png
  [2]: https://i.sstatic.net/P1laR.png
  [3]: https://i.sstatic.net/xnk4O.png
  [4]: https://i.sstatic.net/Jzors.png
  [5]: https://i.sstatic.net/w3uli.png
