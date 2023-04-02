---
title: "Split Pandas DF columns based on condition"
site: stackoverflow
question_id: 75909759
answer_id: 75909936
url: https://stackoverflow.com/a/75909936
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-02T03:13:16Z
last_edited: 2023-04-03T14:45:07Z
revisions: 4
revision_history: https://stackoverflow.com/posts/75909936/revisions
accepted: true
score: 1
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9b6b02291955d6cbcc7c74dfe769f8200009e296912b0cd0a7678d0a7b4c66af
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-02

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75909936>, 2023-04-02, last edited 2023-04-03; **accepted**; score 1. Text as retrieved 2026-10-12.

The suggested solution below uses [`.itertuples`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.itertuples.html) to go through all cells and splits any cells [unless they're in the first columns] containing `:` into a key-value pair, so it should work for any number of tag-types and `Tags_` columns.

```py
# import pandas as pd
# df = pd.read_html('https://stackoverflow.com/questions/75909759')[0] # from your q

parse_cols = [c for c in df.columns if c[:4]=='Tags' or c=='VideoId'] # [filter]
max_cols = 2 # None # [ set None to include all columns ]

new_df = pd.DataFrame([{'VideoId':vi, **{k:v for k,v in [
    rv.split(':',1) for rv in row[:max_cols] if isinstance(rv,str) and ':' in rv
]}} for _, vi, *row in df[parse_cols].itertuples()])
# ]}} for vi, *row in df.itertuples()]) ## if df['VideoId'] is also df.index
```

<sub>**NOTE: Omit the `_,` part in *`...for _, vi, *row in...`* if `df['VideoId']` is also `df.index`.**</sub>


`new_df` should look like 

>```py
> ╒═══════════╤═════════╤═════════╕
> │   VideoId │ Movie   │ Genre   │
> ╞═══════════╪═════════╪═════════╡
> │      1234 │ None    │ None    │
> ├───────────┼─────────┼─────────┤
> │      3456 │ Rocky   │ Drama   │
> ├───────────┼─────────┼─────────┤
> │      5678 │ Love Me │ Romance │
> ├───────────┼─────────┼─────────┤
> │      7890 │ Scream  │ Horror  │
> ├───────────┼─────────┼─────────┤
> │      9012 │ Shrek   │ None    │
> ╘═══════════╧═════════╧═════════╛
>```
>
> <sub>[Printed with `print(new_df.fillna('None').to_markdown(index=False, tablefmt='fancy_grid'))`.]</sub>

---

Btw, about

> <sup>*"What happens if both Tags1, Tags2 column has Movie: or Genre: in the same row?"*  -- [comment](https://stackoverflow.com/questions/75909759/split-pandas-df-columns-based-on-condition/75909936#comment133892091_75909759) by [SomeDude](https://stackoverflow.com/users/1410303/somedude)</sup>

In the case of this solution, the value from last column [`Tags2` in your sample data] will over-write any values with the same key from previous columns.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Aleksei Wolff](https://stackoverflow.com/users/21546506)** (2023-04-02): Yes. That's a problem. I simplified the data example above.  In reality, I could have Tags1,Tags2,Tags3.... and the Movie or Genre data could be in any one of the Tags columns.
- **me** (2023-04-02): @AlekseiWolff I thought that might be so, from what I remember of some other movie datasets. Did my answer work for your data btw?
- **[Aleksei Wolff](https://stackoverflow.com/users/21546506)** (2023-04-03): It did work, since it created two column (movie, genre) as requested. But since there are other columns with embedded colons in it (i.e. urls,timestamps etc.) then it's creating a whole bunch of other columns I don't need. Is there a way to limit it to just columns named TagsN?
- **me** (2023-04-03): @AlekseiWolff sure, just limit them in the *`...for rv in row if...`* bit by using `row[:N]` to limit the **number** of columns, or just select the columns you want to parse with `df[parse_cols]` in *`...for _, vi, *row in df.itertuples()...`* [I've edited my answer]
