---
title: "How to get full text when scraping with beautifulsoup in Python?"
site: stackoverflow
question_id: 74098691
answer_id: 74104766
url: https://stackoverflow.com/a/74104766
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-18T01:32:00Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74104766/revisions
accepted: false
score: 1
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9193ede318d9261d2c183b95efab7f520a1a656c05880c114c5904be04f1f2ab
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-18

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74104766>, 2022-10-18; score 1. Text as retrieved 2026-10-12.

[I can't reproduce it exactly without knowing the link/s you're scraping from, but] I suspect that your code *is* getting the full description, but `print(df)` truncates it to maintain that tabular display.

You could examine it all as a spreadsheet with [`df.to_excel`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html) or even [`df.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html) or you could add a line to print all of just the cell in first row's "about" column
```python
print(df['about'].iloc[0])
```

<br>

```python
print(list(df['about']))
```
will print the "about" column as a list and
```python
print(list(df.iloc[0]))
```
will print the first row as a list.
