---
title: "I am having a problem scraping a table from a website"
site: stackoverflow
question_id: 75044011
url: https://stackoverflow.com/q/75044011
asked: 2023-01-07T21:48:16Z
asked_by: "Danny Scott"
asked_by_url: https://stackoverflow.com/users/20953909
last_edited: 2023-01-08T02:24:35Z
last_editor: "Driftr95 (me)"
last_editor_url: https://stackoverflow.com/users/6146136
tags: [python, web-scraping, beautifulsoup]
score: -2
views_at_snapshot: 47
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6f1aca6a7ce5bc806ab8ad13b483e65103edf823d022b19e6aff94e8c6afa1b4
---

# I am having a problem scraping a table from a website

Asked by [Danny Scott](https://stackoverflow.com/users/20953909) on Stack Overflow, <https://stackoverflow.com/q/75044011>, 2023-01-07, last edited 2023-01-08 by me. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.


I have web scraped a few tables before but now it seems like it's just not working. The code is very simple - just the beginning 10 or so lines. I can't specifically get the details for the table; the program keeps returning `table` as the value for the variable table, in which I am trying to store the table. Super confused. Would appreciate some assistance!!


```python
# from selenium import webdriver 
# from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup 
import requests
# import pandas as pd 
# import time 

url = 'https://basketball.realgm.com/nba/team-stats'

page = requests.get(url) 
page.text

soup = BeautifulSoup(page.text, 'lxml')
soup

table = soup.find('table', {'class' : "tablesaw tablesaw-swipe"})
table
```

**I expected to get the html for the table, however I got the output below. Also, the variable soup returns the correct information.**



**Output:**

```
In[28]: runfile('/Users/dannyscott/Documents/Python Web Scraping/discord bot code V1.py', wdir='/Users/dannyscott/Documents/Python Web Scraping')
```
```
In[29]: table
```


**also, if I try to `table.find_all` , it will say *"'NoneType' object has no attribute 'find_all''"***
