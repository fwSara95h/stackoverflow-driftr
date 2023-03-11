---
title: "Compare dictionaries to check if they are equal or if they go from empty to having a value"
site: stackoverflow
question_id: 75688651
answer_id: 75702212
url: https://stackoverflow.com/a/75702212
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-11T01:06:55Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75702212/revisions
accepted: false
score: 0
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d40bb3ebdfa4a3c53ea0d7a0255ec936388d709babed8c1b40980a8e342b8c4d
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-11

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75702212>, 2023-03-11; score 0. Text as retrieved 2026-10-12.

Set-up:

```py
# import pandas as pd 

## [ can just read tables from your question with: ]
## df1, df2 = pd.read_html('https://stackoverflow.com/questions/75688651')[:2]

df1 = pd.DataFrame([{'NAME': 'Kelly', 'AGE': 15, 'CITY': 'London', 'GENDER': 'F', 'ID': 15}, {'NAME': 'Jack', 'AGE': 12, 'CITY': '', 'GENDER': 'M', 'ID': 98}, {'NAME': 'Josh', 'AGE': 30, 'CITY': 'Austin', 'GENDER': 'M', 'ID': 12}])
df2 = pd.DataFrame([{'NAME': 'Kelly', 'AGE': 15.0, 'CITY': '', 'GENDER': 'F', 'ID': 15}, {'NAME': 'Jack', 'AGE': '', 'CITY': 'Munich', 'GENDER': 'M', 'ID': 98}, {'NAME': 'Josh', 'AGE': 30.0, 'CITY': 'Austin', 'GENDER': 'M', 'ID': 12}])
```

---

> *is there a way to check this condition for the entire row at once/another way to write this?*

You can use [`zip`](https://www.programiz.com/python-programming/methods/built-in/zip) and [`.iterrows`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html) with [`for...else`](https://book.pythontips.com/en/latest/for_-_else.html) like:

```py
ids = []
for (i1,df1_row),(i2,df2_row) in zip(df1.fillna('').iterrows(),df2.fillna('').iterrows()): 
    for df1_val, df2_val in zip(df1_row, df2_row): 
        if not (df1_val==df2_val or df2_val==''): break
    else: ids.append(df2_row['ID'])
```

[With this `for...else`, it breaks if there are two unequal values where the `df2` value if not empty (and [`.fillna('')`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html) ensures that all `nan` values are replaced with `''` empty strings); if it never breaks (i.e., all values are equal *or* `df2` has the empty value), the `else` block will be executed and the `ID` will be added to `ids`.]

Instead of `for...else`, you can also use [list comprehension](https://www.programiz.com/python-programming/list-comprehension) with [`all`](https://www.programiz.com/python-programming/methods/built-in/all) to check every pair of values like you mentioned:

```py
checkPair = lambda df1_val, df2_val: df1_val==df2_val or df2_val=='' 
ids = [df2_row['ID'] for (i_1, df1_row), (i_2, df2_row) in zip(
    df1.fillna('').iterrows(), df2.fillna('').iterrows()
) if all(checkPair(v1, v2) for v1, v2 in zip(df1_row, df2_row))]
```


---

### Suggested Solution:

> *or maybe there is just a better way to compare two rows in a dataframe for the same id against each other using these conditions without having to turn the rows into dictionaries to compare?*

Yes, pandas has the [`.compare`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.compare.html) method, which I thinks is quite handy for situations like this. 

```py
comp_df = df1.set_index('ID').compare(df2.set_index('ID'), keep_shape=True)
```

As you can see from [comparison examples][1] (comparing `df1` to `df2`):
- `self` and `other` columns will [respectively] contain `df1` and `df2` values
- if both `df1` and `df2` have the same value, `self` and `other` will both contain `nan`
   - <sup>(unless you set `keep_equal=True`)</sup>
- so if you fill the `nan`s with `''`, you'll only need to check the `other` values 
   - <sup>(view [**`comp_df.fillna('')`**][3] for demonstration)</sup>

<br>

So, using list comprehension and [`any`](https://www.programiz.com/python-programming/methods/built-in/any):

```py
ids = [i for i, r in comp_df.fillna('').iterrows() if not any(list(r!='')[1::2])]
```

or with `for...else`:

```py
comp_df = df1.set_index('ID').compare(df2.set_index('ID'), keep_shape=True)
colNames = {c[0] for c in comp_df.columns} # --> {'GENDER', 'AGE', 'CITY', 'NAME'}

ids = []
for i, row in comp_df.fillna('').iterrows():
    for c in colNames:
        if row[c]['other'] != '': break
    else: ids.append(i)
```

---

Any of the 4 methods above should result is `id` returning `[15, 12]`.

**Note that `.compare` requires both DataFrames to have the same exact shape and labels [for columns and indices].** [And the `for...zip...` methods from the first half will not work reliably unless all the columns and rows are sorted in the same order as well (e.g.: you can't have Jack before Kelly in `df2` as Kelly comes first in `df1`).]






  [1]: https://i.sstatic.net/CInAq.png
  [3]: https://i.sstatic.net/nMGSq.png?s=256
