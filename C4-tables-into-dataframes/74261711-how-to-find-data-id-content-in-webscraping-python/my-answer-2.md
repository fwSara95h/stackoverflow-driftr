---
title: "How to find data-id content in webscraping (python)"
site: stackoverflow
question_id: 74261711
answer_id: 74279923
url: https://stackoverflow.com/a/74279923
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-01T17:54:47Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74279923/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 09f0d12f775998a07b1f6975c4abe54caf9ff5c3d5b922c08b0373cbd941044d
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-01

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74279923>, 2022-11-01; score 0. Text as retrieved 2026-10-12.

[I thought it would be cleaner to post this as a separate a separate answer than to edit it into the previous.]

First, let's create a list of dictionaries, each of which can be used to create a dataframe:
```python
# (pretty much the same as before)
dataType_tables = [{
    'type': t.get('data-subtype', 'NO_SUBTYPE') + ' - ' + t.get('data-type'), 
    'headers': ['Data-ID'] + [
        col.get_text(strip=True) for col in t.select('th')], 
    'data': [[r.get('data-id')] + [
        col.get_text(strip=True) for col in r.select('td')
    ] for r in t.select('tr:has(td)')]
} for t in doc.select('div[data-type]')]
```
and then, the list can be looped through with a combination of [`ExcelWriter`](https://pandas.pydata.org/docs/reference/api/pandas.ExcelWriter.html#pandas.ExcelWriter) and `to_excel` to create the spreadsheets
```python
with pd.ExcelWriter("albelli_prijsoverzicht.xlsx") as w:
    for table_i in dataType_tables:
        pd.DataFrame(
            table_i['data'], columns=table_i['headers']
        ).set_index('Data-ID').to_excel(w, sheet_name=table_i['type'])
```
and the resulting file ("albelli_prijsoverzicht.xlsx" here) should look like
[![excel screenshot][1]][1]


  [1]: https://i.sstatic.net/TNMKb.png
