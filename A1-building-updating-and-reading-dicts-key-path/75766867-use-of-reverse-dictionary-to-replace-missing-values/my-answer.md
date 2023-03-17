---
title: "use of reverse dictionary to replace missing values"
site: stackoverflow
question_id: 75766867
answer_id: 75769838
url: https://stackoverflow.com/a/75769838
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-17T16:10:21Z
last_edited: 2023-03-20T16:30:43Z
revisions: 4
revision_history: https://stackoverflow.com/posts/75769838/revisions
accepted: false
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d402637a017694a907a50110154c91d739475dc12d83b5ebe4598a2638ff6be7
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-17

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75769838>, 2023-03-17, last edited 2023-03-20; score 0. Text as retrieved 2026-10-12.

when you do *`df = df.set_index('Country')['Region']`* you're reducing `df` to just the `Region` column [and `Country` as that's the index now]. 

Try [filling](https://stackoverflow.com/a/38134049/6146136) `Region` in a separate statement 

```py
df = df.set_index('Country')

df['Region'] = df['Region'].fillna(revdct)
# df['Region'].fillna(revdct, inplace=True) ## [not sure it won't set off warnings]

df = df.reset_index()
df # print(df.to_markdown(tablefmt='fancy_grid'))
```

---

You could also try using [`.map`](https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html) on `Country` instead of setting-then-resetting index.

```py
df['Region'] = df['Region'].fillna(df['Country'].map(revdct))
# df['Region'].fillna(df['Country'].map(revdct), inplace=True)

df
```
[![samplop][1]][1]


  [1]: https://i.sstatic.net/aQHP1.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Anastasia](https://stackoverflow.com/users/20689651)** (2023-03-20): Thank you for your answer, but unfortunately the code didn't work. The 'Region' column didn't got filled, there are still Nan's.
- **me** (2023-03-20): @Anastasia sorry I forgot to move `reset_index` to after `fillna` - I've edited my answer and also added an alternative method with demonstration. Would you mind giving it another try?
- **[Anastasia](https://stackoverflow.com/users/20689651)** (2023-03-21): Thank you Driftr95! I tried .map and it worked!
