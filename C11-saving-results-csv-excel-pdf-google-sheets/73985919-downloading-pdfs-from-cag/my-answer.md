---
title: "Downloading PDFs from CAG"
site: stackoverflow
question_id: 73985919
answer_id: 73986919
url: https://stackoverflow.com/a/73986919
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-07T12:04:42Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73986919/revisions
accepted: true
score: 1
chapter: C11
chapter_title: "Saving results: CSV, Excel, PDF, Google Sheets"
cluster: scrape-to-files-tables
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1501ef125016981707ddc989ee4652595002f9d956465ee977a60f32455dd305
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-07

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73986919>, 2022-10-07; **accepted**; score 1. Text as retrieved 2026-10-12.

You could try narrowing down the tab from which the links are selected. The tab id can be found using 
```python
tabId = soup.find(
    lambda t: t.name == 'a' and t.get('href') and 
    t.get('href').startswith('#tab') and # just in case
    'Monthly Key Indicators' == t.get_text(strip=True)
).get('href')
```
(Or, if it's always the same id, you can just set as `tabId = "#tab-360"`. ) Then, you can just change your selection to
```python
soup.select(f"{tabId} a[href$='.pdf']")
```

But aren't you downloading the same file 3x with each report? You could alter your for-loop to only download from the links with "Download" as text:
```python
pdfLinks = soup.select(f"{tabId} a[href$='.pdf']")
pdfLinks = [pl for pl in pdfLinks if pl.get_text(strip=True) == 'Download']
for link in pdfLinks:
  #download
```
