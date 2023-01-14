---
title: "Data/Table Scraping from Website using Python"
site: stackoverflow
question_id: 75119631
answer_id: 75120574
url: https://stackoverflow.com/a/75120574
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-14T19:08:16Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75120574/revisions
accepted: true
score: 1
chapter: C4
chapter_title: "Tables into DataFrames"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8e285eb4a8e79dbe426b7b2b13d09302c9ecf57008612911b80057a9bf38cbc1
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-14

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75120574>, 2023-01-14; **accepted**; score 1. Text as retrieved 2026-10-12.

Rather than trying to fill an empty DataFrame, it would be simpler to utilize [`.read_html`](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html), which returns a list of DataFrames after parsing every `table` tag within the HTML.

Even though this page has only two tables (<sub>*"Top Youtube channels"* and *"Top Youtube channels - detail stats"*</sub>), 3 DataFrames are returned because the second table is [split into two][1] `table` tags [between rows 12 and 13][2] for some reason; but they can all be combined into DataFrame. 

```python
dfList = pd.read_html(url) # OR
# dfList = pd.read_html(page.text) # OR
# dfList = pd.read_html(soup.prettify())

allTime = dfList[0].set_index(['rank', 'Youtuber'])

# (header row in 1st half so 2nd half reads as headerless to pandas)
dfList[2].columns = dfList[1].columns 
perYear = pd.concat(dfList[1:]).set_index(['rank', 'Youtuber'])


columns_ordered = [
    'started', 'category', 'subscribers', 'subscribers/year', 
    'video views', 'Video views/Year', 'video count', 'Video count/Year'
] # re-order columns as preferred
combinedDf = pd.concat([allTime, perYear], axis='columns')[columns_ordered]
```

<sub>If the `[columns_ordered]` part is omitted from the last line, then the expected column order would be *`'subscribers', 'video views', 'video count', 'category', 'started', 'subscribers/year', 'Video views/Year', 'Video count/Year'`*.</sub>

`combinedDf` should look like
[![opdf][3]][3]


  [1]: https://i.sstatic.net/xITas.png
  [2]: https://i.sstatic.net/ECYA4.png
  [3]: https://i.sstatic.net/c3DrX.png
