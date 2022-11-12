---
title: "Replace span tags with whitespace or parse contents as new column with pandas.read_html"
site: stackoverflow
question_id: 74409839
url: https://stackoverflow.com/q/74409839
asked: 2022-11-12T01:56:35Z
asked_by: "Richard Herron"
asked_by_url: https://stackoverflow.com/users/334755
last_edited: never
tags: [python, pandas, selenium, beautifulsoup]
score: 0
views_at_snapshot: 483
answer_count: 2
accepted_answer_id: 74410430
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7106c06f082932ab4b805a642ad8ee002fa89a9bb067ce6c6f8023c16dcdfc7f
---

# Replace span tags with whitespace or parse contents as new column with pandas.read_html

Asked by [Richard Herron](https://stackoverflow.com/users/334755) on Stack Overflow, <https://stackoverflow.com/q/74409839>, 2022-11-12. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I want to scrape Congressional stock trades from [Capitol Trades](https://www.capitoltrades.com/trades). I can scrape the data, but the column that contains stock tickers has a span tag that separates company names from company tickers. `pandas.read_html()` removes this span tag, which concatenates company names and tickers and makes it difficult to recover tickers.

For example, company names that end with an "INC" suffix run into tickers, which are also capital letters. See my example below with "INC" and "AE". 

[![INC and AE][1]][1]

Here is where I found the span tag:

[![span tag][2]][2]

Company tickers are 1 to 5 characters in length, and I have failed to regex tickers because there are many varieties of company suffixes (e.g., "INC", "CORP", "PLC", "SE", etc.), and not all company names have suffixes.

How can I either replace span tags with whitespace to separate company names and tickers or parse the span as another column?

Here is my code:

```python

import pandas as pd
import yfinance as yf
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import datetime

def get_url(page=1, pageSize=50, assetType='stock'):
    if page == 1:
        return f'https://www.capitoltrades.com/trades?assetType={assetType}&pageSize={pageSize}'
    elif page > 1:
        return f'https://www.capitoltrades.com/trades?assetType={assetType}&page={page}&pageSize={pageSize}'
    else:
        return None

driver = webdriver.Firefox()
driver.get(get_url(page=1))
driver.implicitly_wait(10)
time.sleep(1)
soup = BeautifulSoup(driver.page_source, 'lxml')
tables = soup.find_all('table')
table = pd.read_html(str(tables))[0]
driver.close()

```

  [1]: https://i.sstatic.net/xSQey.png
  [2]: https://i.sstatic.net/uiEjW.png

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[QHarr](https://stackoverflow.com/users/6241235)** (2022-11-12): You could easily write something to use the API which guarantees standard format and the tickers are in there E.g. https://bff.capitoltrades.com/trades?page=1&pageSize=15#  Looks like this person even wrote a Flask app for it: https://github.com/KonradIT/hilltrades
- **[Richard Herron](https://stackoverflow.com/users/334755)** (2022-11-13): @QHarr Do you have documentation for this API? I had found an older SO answer with a different API URL, but I have not found any documentation on API limits, etc. I will have to learn what is a Flask app. :) Thanks!
- **[QHarr](https://stackoverflow.com/users/6241235)** (2022-11-14): I am not sure it is documented. I also couldn't find anything in ToS precluding scraping etc.  The author of the python wrapper automated with Flask but you don't need to. The link above returns trade info and has page size and page params. You play around to find max page size which, based on total items, will give you number of pages to increment the page param by in a loop of requests. The total items (irrespective of current page) is given in each response in the meta section. E.g. with the above param values currently meta reads "totalPages": 3022, "totalItems": 45319.
- **[QHarr](https://stackoverflow.com/users/6241235)** (2022-11-14): The author at some point also submitted an update on GitHub to account for the API endpoint change IIRC.  API info also _"documented"_ via the js in this file (though not worth the effort at present to review I'd think): https://www.capitoltrades.com/_next/static/chunks/9619-347b39d52358e034.js
