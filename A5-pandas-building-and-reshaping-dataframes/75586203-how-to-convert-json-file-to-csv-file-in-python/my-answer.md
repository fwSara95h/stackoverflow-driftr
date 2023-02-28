---
title: "How to convert json file to csv file in python"
site: stackoverflow
question_id: 75586203
answer_id: 75587185
url: https://stackoverflow.com/a/75587185
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-28T01:47:56Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75587185/revisions
accepted: false
score: 1
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: [flattenObj]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b639854333ffaad1e4fb19c91207a30cc6192e5883fd0254dd27a3a75ef4408a
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-28

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75587185>, 2023-02-28; score 1. Text as retrieved 2026-10-12.

My preferred method to save to CSV is with [`DataFrame.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv) and pandas also has a [`json_normalize`](https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html) method which could have been the shortest way to flatten this, but I'm not quite sure how to handle the `infos` lists.

However, if you parse the JSON into a list of python dictionaries (`pData`)

```py
import json
jData = '''
[ { "infos": [{ "localisation": "Kassel" }, { "date": "01.08.2023" }, { "places": "1 freier Platz" }],
    "applying email": "exemple@starke.ma",
    "additional infos": {"name": "jhon", "position": "RH", "email": "email@email.com" }  },
  { "infos": [{ "places": "1 freier Platz" }],
    "applying email": "", "applying link": "www.exemple.com",
    "additional infos": {"name": "jhon", "position": "RH", "email": "email@email.com"} }] 
''' ## I removed the last comma bc it was causing error when parsing

pData = json.loads(jData) 
```

then you can flatten it with this [`flattenObj`](https://pastebin.com/v3Fep60B) function<sup>([view examples][1])</sup> before converting to pandas DataFrames and the saving as CSV:

```py
import pandas as pd
csv_path = 'x.csv' ## path/name of csv file to save to

# pd.DataFrame([flattenObj(d, kSep=' > ') for d in pData]).to_csv(csv_path, index=False)
df = pd.DataFrame([flattenObj(d, kSep=' > ') for d in pData])
df.to_csv(csv_path, index=False)
```


  [1]: https://i.sstatic.net/CzCDa.png
