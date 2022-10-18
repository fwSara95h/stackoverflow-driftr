---
title: "Scraping a.href returns blank value?"
site: stackoverflow
question_id: 74114161
url: https://stackoverflow.com/q/74114161
asked: 2022-10-18T16:10:16Z
asked_by: "Ianucci"
asked_by_url: https://stackoverflow.com/users/16344097
last_edited: 2022-10-18T16:11:56Z
tags: [python-3.x, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 58
answer_count: 3
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fae2e23bfddaa845863fa1d7d6fc15a1b672337e687ffc08b9672943a97bef8b
---

# Scraping a.href returns blank value?

Asked by [Ianucci](https://stackoverflow.com/users/16344097) on Stack Overflow, <https://stackoverflow.com/q/74114161>, 2022-10-18, last edited 2022-10-18. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to scrape some information from the following webpage https://smws.com/all-whisky?sort=pricedesc&page=1&per-page=128

The information I'm trying to scrape is the name of each item plus the product code (not quite there yet with the below code). For example, for the first item this would be "Goodnight and Joy" & "53.389". I then wish to iterate this over the whole webpage. My code is as follows:

``` import ssl
import requests
import time
import smtplib
from email.message import EmailMessage
import hashlib
from urllib.request import urlopen
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://smws.com/all-whisky?sort=pricedesc&page=1&per-page=128'

soup = BeautifulSoup(urlopen(url).read(),features="html.parser")

test = soup.find_all('a.href')

print(test) 
```

However this simply returns
```
[]
```

Please could someone help me to return the information returned in a.href and potentially iterated for the entire page.

Thank you!
