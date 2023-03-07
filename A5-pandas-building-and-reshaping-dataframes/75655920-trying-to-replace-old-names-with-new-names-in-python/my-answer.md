---
title: "Trying to replace old \"names\" with new \"names\" in Python"
site: stackoverflow
question_id: 75655920
answer_id: 75657608
url: https://stackoverflow.com/a/75657608
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-07T02:43:36Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75657608/revisions
accepted: true
score: 0
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b76f733c340cf37d4a631eda8aca3495468cdcf2b3b78509b009dd6402cd5cd8
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-07

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75657608>, 2023-03-07; **accepted**; score 0. Text as retrieved 2026-10-12.

I find [`pandas`](https://pandas.pydata.org/docs/user_guide/10min.html) quite handy for loading data from [and saving data to] spreadsheets. You could use [`read_excel`](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html) to read the old and new names from the fist file and convert them into a dictionary (`tRef_dict`) as below.

**<sub>[NOTE: If your file is a CSV, use [`read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) instead of `read_excel`.]</sub>**

```py
import pandas as pd

tRef_fp = 'map_old_new.xlsx' ## path to file with new&old names
tRef_dict = pd.read_excel(tRef_fp).to_dict('split')
tRef_dict = {k:v for v,k,*_ in tRef_dict['data']} # colA->new, colB->old
# tRef_dict = dict(tRef_dict['data']) # only 2 cols, colA->old, colB->new
```

- Use `pd.read_excel(tRef_fp, header=None).to_dict('split')` if the sheet doesn't have a header row (otherwise, the first row would not be included in `tRef_dict['data']`).
- With your example data, *`dict(tRef_dict['data'])`* would return 
  ```py
  {'apple-er3': 'horse-er45', 'alk-er43': 'erk-bf43'}
  # 'apple-er3' will get translated to  'horse-er45'
  ```
- and *`{k:v for v,k,*_ in tRef_dict['data']}`* would return 
  ```py
  {'horse-er45': 'apple-er3', 'erk-bf43': 'alk-er43'}
  # 'horse-er45' will get translated to  'apple-er3'
  ```

---

Then, you can load the file with only old names, use [`.applymap`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.applymap.html) and `tRef_dict` to update the names, and then save the updated names with [`.to_excel`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html) <sup>(or [`.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html) to save to a CSV file)</sup> :

```py
old_fp = 'old.xlsx' ## path to file with old names
new_fp = 'new.xlsx' ## [can be the same as old_fp]

names_df = pd.read_excel(old_fp) #, header=None) ## if there is no header row, specify
names_df = names_df.applymap(lambda x: tRef_dict.get(x,x)) ## [update names]
names_df.to_excel(new_fp, index=False) #, header=False) ## [save updated]
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Anton Larsson](https://stackoverflow.com/users/21345004)** (2023-03-07): Wow worked perfectly. Im just trying to understand how all this work. Im very new to programming. Do you mind if i ask some questions? I dont know if i should put them here or if i can send them in some sort of DM on here.
- **me** (2023-03-07): @AntonLarsson there are [chat](https://chat.stackoverflow.com/), but you need at least 20rp to send messages (and also, afaik they're not private like DMs typically are). You can ask anything about here and I'll try to answer if I can. [Btw, if the comment thread gets too long, a chatroom gets automatically generated and the link is added to the thread.]
- **[Anton Larsson](https://stackoverflow.com/users/21345004)** (2023-03-08): Oh okey. So im woundering 1.  the first parts i do understand but what does this do?    .to_dict('split')  2. I read your notes and they are well writen but this:  tRef_dict = {k:v for v,k,*_ in tRef_dict['data']}  would you mind explaining  {k:v for v,k,*_ in tRef_dict['data']} i guess k means colume? the rest i cant figure out, especially the "data" part.
- **me** (2023-03-08): @AntonLarsson [`.to_dict`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html) returns the DataFrame as a dictionary, and specifying `orient='split'` tells it to form a dictionary with the index, column names and data separated into 3 lists *`{‘index’ -> [index], ‘columns’ -> [columns], ‘data’ -> [values]}`* [`data` will be a list of sub-lists, with each sub-list representing one row]
- **[Anton Larsson](https://stackoverflow.com/users/21345004)** (2023-03-10): Oh okey, what is a DataFrame? is it just the csv or excel file?  and what is "index" i guess columns is just the excel colums A and B and data is the value in the cells? Or is data the rows?
- **me** (2023-03-10): A [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame) is a [pandas](https://pandas.pydata.org/docs/getting_started/index.html#intro-to-pandas) data structure for organizing 2D data (such as a table) [ view [`tRef_df`](https://i.sstatic.net/ME7wS.png) for example ].
- **me** (2023-03-10): Just like columns have names, rows have index. `data` is a list of rows in this case (**`[['apple-er3', 'horse-er45'], ['alk-er43', 'erk-bf43']]`**), but when constructing a df it can also be a dictionary of columns (like *`{'Colum A': ['apple-er3', 'horse-er45'], 'Colum B': ['alk-er43', 'erk-bf43']}`*)
