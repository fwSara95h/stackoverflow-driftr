---
title: "Read a table from google docs without using API"
site: stackoverflow
question_id: 74887632
url: https://stackoverflow.com/q/74887632
asked: 2022-12-22T11:08:34Z
asked_by: "Irina"
asked_by_url: https://stackoverflow.com/users/20647625
last_edited: 2022-12-24T00:13:20Z
last_editor: "Driftr95 (me)"
last_editor_url: https://stackoverflow.com/users/6146136
tags: [python-3.x, google-sheets, beautifulsoup]
score: 0
views_at_snapshot: 7410
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c70e9b5ae98c7bf654be8a3870eb0f10e2d6f9e6d93927e92a491375d655a76b
---

# Read a table from google docs without using API

Asked by [Irina](https://stackoverflow.com/users/20647625) on Stack Overflow, <https://stackoverflow.com/q/74887632>, 2022-12-22, last edited 2022-12-24 by me. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I want to read a google sheet table in python, but without using API.
I tried with `BytesIO`, `Beatifulsoup`.

I know about the soluthion with gspread, but I need to read table without token. Only using url.


```python
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from lxml.etree import tostring
from io import BytesIO
import requests

req=requests.get('https://docs.google.com/spreadsheets/d/sheetId/edit#gid=', auth=('email', 'password'))

page = req.text
```

here i've got html code, like `<!doctype html><html lang="en-US" dir="ltr"><head><base href="h` and so on...

i also tried lib BeautifulSoup, but the result is same.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[John Harrington](https://stackoverflow.com/users/15239077)** (2022-12-22): Welcome to Stack Overflow! Looking over your code, it does exactly what I would expect it to, it returns the textual representation of a page as HTML. Are you looking to get the values of individual cells?
- **me** (2022-12-24): can you please include the code from your attempts with BytesIO and Beatifulsoup?
- **[Xiddoc](https://stackoverflow.com/users/11985743)** (2022-12-24): Your attempt of authenticating with `requests` will not work. You need to sign into your Google account, which will be much more complicated. Hence, you will need a large library to do this for you, such as the one you mentioned, or use a public API that Google offers.
- **[Stephen C](https://stackoverflow.com/users/139985)** (2022-12-25): What do you mean by "api"?  Strictly speaking, bytesio, beautifulsoup and etree all have apis.  As does any other library you care to mention.
