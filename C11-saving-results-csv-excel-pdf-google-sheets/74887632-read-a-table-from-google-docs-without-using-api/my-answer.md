---
title: "Read a table from google docs without using API"
site: stackoverflow
question_id: 74887632
answer_id: 74910313
url: https://stackoverflow.com/a/74910313
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-24T21:03:21Z
last_edited: 2022-12-25T02:22:34Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74910313/revisions
accepted: false
score: 1
chapter: C11
chapter_title: "Saving results: CSV, Excel, PDF, Google Sheets"
cluster: google-sheets-docs
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6a47543bb2b9311aaf2bdf83ff59df783e044c29066c94c5bbbba561c9df91bf
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-24

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74910313>, 2022-12-24, last edited 2022-12-25; score 1. Text as retrieved 2026-10-12.

For reading a table from html, you can use [`pandas.read_html`](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html). 

---

**If** it's an **unrestricted** spreadsheet [like this one](https://docs.google.com/spreadsheets/d/1bQo1an4yS1tSOMDhmUTGYtUlgnHDQ47EmIcj4YyuIxo), you probably don't even need `requests` - you can just directly pass the URL to `read_html`. [[view dataframe](https://i.sstatic.net/DAHdG.png)]

```python
import pandas as pd
sheetId = '1bQo1an4yS1tSOMDhmUTGYtUlgnHDQ47EmIcj4YyuIxo' ## REPLACE WITH YOUR SHEETID
sheetUrl = f'https://docs.google.com/spreadsheets/d/{sheetId}'
sheetDF = pd.read_html(
    sheetUrl, attrs={'class': 'waffle'}, skiprows=1
)[0].drop(['1'], axis=1).dropna(axis=0, how='all').dropna(axis=1, how='all')
```

---

If it's not unrestricted, then the way you're using `requests.get` would not work either, because you're not passing [the `auth` argument](https://requests.readthedocs.io/en/latest/user/authentication/) correctly. I actually don't think there is any way to login to Google with just `requests.auth`. You could login to drive on your browser, open a sheet and then [copy the request](https://i.sstatic.net/9q6Ex.png) to https://curlconverter.com/ and [paste to your code from there](https://i.sstatic.net/iqOi6.png).

```python
import pandas as pd
import requests
from bs4 import BeautifulSoup

sheetUrl = 'YOUR_SHEET_URL'
cookies = 'PASTE_FROM_https://curlconverter.com/'
headers = 'PASTE_FROM_https://curlconverter.com/' 
req = requests.get(sheetUrl, cookies=cookies, headers=headers)

# in one line, no error-handling
# sheetDF = pd.read_html(req.text, attrs={'class': 'waffle'}, skiprows=1)[0].drop(['1'], axis=1).dropna(axis=0, how='all').dropna(axis=1, how='all')

# req.raise_for_status() # raise error if request fails
if req.status_code != 200: 
    print(req.status_code, req.reason, '- failed to get', url)

soup = BeautifulSoup(req.content)
wTable = soup.find('table', class_="waffle")
if wTable is not None:
    dfList = pd.read_html(str(wTable), skiprows=1) # set skiprows=1 to skip top row with column names A, B, C...
    sheetDF = dfList[0] # because read_html returns a LIST of dataframes
    sheetDF = sheetDF.drop(['1'], axis='columns') # drop row #s 1,2,3...
    sheetDF = sheetDF.dropna(axis='rows', how='all') # drop empty rows
    sheetDF = sheetDF.dropna(axis='columns', how='all') # drop empty columns
    ### WHATEVER ELSE YOU WANT TO DO WITH DATAFRAME ###
else: print('COULD NOT FIND TABLE')
```

---

**However,** please note that the cookies are probably only good for up to 5 hours maximum (and then you'll need to paste new ones), and that if there are multiple sheets in one spreadsheet, you'll only be able to scrape the first sheet with `requests`/`pandas`. So, it would be better to use the API for restricted or multi-sheet spreadsheets.
