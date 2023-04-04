---
title: "How to read json file and stored it in data frame with columns and multiple rows in pandas"
site: stackoverflow
question_id: 75926838
answer_id: 75929728
url: https://stackoverflow.com/a/75929728
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-04T13:04:21Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75929728/revisions
accepted: false
score: 0
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 018a3e9e5e97fd18c79f5fcdc61a7345f6ba7e8610b3e64ee782440c54019bbc
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
redacted_at_import: "13 lines removed at import (output table removed at import: it reproduced the asker's credit-report records (column names kept in the text above))"
---

# My answer — 2023-04-04

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75929728>, 2023-04-04; score 0. Text as retrieved 2026-10-12. Redacted at import; see the front matter.

You could use [`json_normalize`](https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html) with [`.explode`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.explode.html) and then clean up a bit

```py
import pandas as pd
import json

json_fp = 'x.json' ## put the ACTUAL file path here
with open(json_fp) as f: data = json.load(f)

df = pd.json_normalize(data)
df.columns = [c.split('.')[-1] for c in df.columns]

df = df.explode('accountInfo').reset_index(drop=True)
df = pd.concat([df, pd.json_normalize(df['accountInfo'])], axis=1)
df = df.drop(columns=['accountInfo','enquiryInfo','officeInfo'])
```

At the end of that, `df` should look like

> *[output table removed at import: it reproduced the asker's credit-report records (column names kept in the text above)]*
> 
> <sup>[Printed with `print(df.to_markdown(tablefmt='fancy_grid'))`]</sup>
