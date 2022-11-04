---
title: "Scrape multi page URL using Beautifulsoup"
site: stackoverflow
question_id: 74316658
url: https://stackoverflow.com/q/74316658
asked: 2022-11-04T11:54:13Z
asked_by: "tony michael"
asked_by_url: https://stackoverflow.com/users/18194427
last_edited: never
tags: [python, beautifulsoup]
score: 0
views_at_snapshot: 91
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d51ffea1af9a768caabe17d3f8663842b99f98dffeaa3a32d929eaa2c9ada705
---

# Scrape multi page URL using Beautifulsoup

Asked by [tony michael](https://stackoverflow.com/users/18194427) on Stack Overflow, <https://stackoverflow.com/q/74316658>, 2022-11-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

How to scrape multi page URL using BeautifulSoup,

I'm trying to scrape webpage but I'm stuck, any idea will be helpful

```
import os
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from pathlib import Path
import os.path
import urllib.request, urllib.error, urllib.parse
from tldextract import extract
# URL of the web page you want to extract
url = "https://www.taneps.go.tz/epps/viewAllAwardedContracts.do?d-3998960-p=1&selectedItem=viewAllAwardedContracts.do&T01_ps=100"

# initialize a session
session = requests.Session()
# set the User-agent as a regular browser
session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

# get the HTML content
html = session.get(url).content

# parse HTML using beautiful soup
soup = bs(html, "html.parser")
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Thomas Kimber](https://stackoverflow.com/users/4137061)** (2022-11-04): What is your code doing differently from what you want your code to do?
- **[tony michael](https://stackoverflow.com/users/18194427)** (2022-11-04): I'm stuck, I want to scrape all pages of that website
- **[skyriver](https://stackoverflow.com/users/15252941)** (2022-11-04): There is a page variable in the link before selected item  `-p=1&selectedItem`. Use a for loop through changing this `p=1` variable.
