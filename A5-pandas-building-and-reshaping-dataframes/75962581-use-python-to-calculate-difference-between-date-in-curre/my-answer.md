---
title: "Use Python to calculate difference between date in current row and date in previous row and previous column"
site: stackoverflow
question_id: 75962581
answer_id: 75962918
url: https://stackoverflow.com/a/75962918
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-08T01:40:25Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75962918/revisions
accepted: true
score: 1
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d5fce62640493fd8b7e2242beeb80ee0ad61b252065db2b60f1fe1d7277830e6
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-08

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75962918>, 2023-04-08; **accepted**; score 1. Text as retrieved 2026-10-12.

Use [`.shift`](https://pandas.pydata.org/docs/reference/api/pandas.Series.shift.html) align `Offline` dates and subtract from `Online` dates and then use [`.where`](https://pandas.pydata.org/docs/reference/api/pandas.Series.where.html) to empty on when the `Kiosk` changes [or to remove negative differences].

```py
# df = pd.read_html('https://stackoverflow.com/questions/75962581')[0]
# df[['Online','Offline']] = df[['Online','Offline']].applymap(pd.to_datetime)

offline_days = df['Online'] - df['Offline'].shift(1)
df['Offline Days'] = offline_days.where(df['Kiosk']==df['Kiosk'].shift(1))
# df['Offline Days'] = offline_days.where(lambda td: td>pd.Timedelta(0))
```

[![opdf][1]][1]


  [1]: https://i.sstatic.net/K4fob.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[the_zeef](https://stackoverflow.com/users/6266807)** (2023-04-10): Thanks for your solution Driftr95!
