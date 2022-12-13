---
title: "Scrape table from url"
site: stackoverflow
question_id: 74783304
answer_id: 74789229
url: https://stackoverflow.com/a/74789229
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-13T18:10:30Z
last_edited: 2022-12-14T13:23:26Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74789229/revisions
accepted: false
score: 2
chapter: C4
chapter_title: "Tables into DataFrames"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 68594b309fc2215b884af5c2354793e54055f266f58924d180fe618cc524ce1b
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-13

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74789229>, 2022-12-13, last edited 2022-12-14; score 2. Text as retrieved 2026-10-12.

The class you're using belongs to the header **row** of the table, not the `table` tag itself. <sub>(It's indicated by the class name itself - "datatable_**row**__qHMpQ"...)</sub>
[![table html][1]][1]

You can use one of the table classes instead (like `datatable_table__D_jso`) or you could use the `data-test` attribute:

```python
table = soup.find('table', {'data-test': "pre-market-most-active-stocks-table"})
```

---

```python
# import pandas
print(pandas.read_html(table.prettify())[0].to_markdown(index=False))
```

prints

```lang-none
| Name                | Symbol   |   Last |   Chg. | Chg. %   | Vol.   | Time     |
|:--------------------|:---------|-------:|-------:|:---------|:-------|:---------|
| Jiuzi Holdings Inc  | JZXN     | 0.24   | 0.092  | +62.09%  | 19.14M | 09:27:41 |
| OpGen Inc           | OPGN     | 0.245  | 0.12   | +96.00%  | 16.41M | 09:27:41 |
| Powerbridge         | PBTS     | 0.1001 | 0.0084 | +9.16%   | 12.07M | 09:26:40 |
| Faraday Future Int. | FFIE     | 0.57   | 0.11   | +24.59%  | 12.03M | 09:27:56 |
| Magenta Therapeuti. | MGTA     | 1.45   | 0.3    | +26.09%  | 9.12M  | 09:27:58 |
| Starry Holdings     | STRY     | 0.122  | 0.022  | +21.50%  | 8.34M  | 09:26:57 |
| Netcapital Inc      | NCPL     | 3.03   | 1.64   | +117.99% | 6.51M  | 09:27:59 |
| China Pharma        | CPHI     | 0.1449 | 0.0044 | +3.13%   | 3.55M  | 09:26:52 |
| 111 Inc             | YI       | 3.81   | 0.27   | +7.63%   | 2.98M  | 09:28:00 |
| Amesite             | AMST     | 0.369  | 0.059  | +19.03%  | 2.45M  | 09:21:45 |
```

---
---

**EDIT:** full code with some additions for debugging and/or error handling:

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

url = "https://www.investing.com/equities/pre-market"
resp = requests.get(url)
# resp.raise_for_status() # halt program right here if bad response

soup = BeautifulSoup(resp.content)
table = soup.find('table', {'data-test':"pre-market-most-active-stocks-table"})

if table is None and resp.status_code == 200: # ok respose, but no table
    hfn = 'MISSING_DATA investing-com_equities_premarket.html'
    with open(hfn, 'wb') as f: f.write(resp.content) 
    print('no such table found - inspect [on editor]: ', os.path.abspath(hfn))
elif table: print(pd.read_html(table.prettify())[0].to_markdown(index=False))
else: print(f'{resp.status_code} {resp.reason} - failed to scrape {url}')

```


  [1]: https://i.sstatic.net/HxOSL.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Raphael Hen](https://stackoverflow.com/users/10467327)** (2022-12-14): Thanks for the answer. I am getting this error - "AttributeError: 'NoneType' object has no attribute 'prettify'" although I have `from prettify import *`
- **me** (2022-12-14): @RaphaelHen this a different `prettify` that comes from bs4 Tags, and does not have to be imported `from prettify...`; it seems that there is some issue with the response you get from `requests.get`, like some suggested in the comments. I've added an edit to my answer - please try my full code and see if it clears up the situation (if it saves and html file, see how the html in the file is different from expected...)
- **[Raphael Hen](https://stackoverflow.com/users/10467327)** (2022-12-14): Thanks for your time. now with the new code I am getting "403 Forbidden - failed to scrape https://www.investing.com/equities/pre-market"
- **me** (2022-12-14): @RaphaelHen (I don't get that error) but this means the site is blocking you....So you need to [set good headers](https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/#therightwaytorotateuseragentsinanyprogram) [with `requests`] or try using [instead of `requests`] something like [cloudscraper](https://pypi.org/project/cloudscraper/) or [HTMLSession](https://requests.readthedocs.io/projects/requests-html/en/latest/)
- **[Raphael Hen](https://stackoverflow.com/users/10467327)** (2022-12-14): I used cloudscraper and it works great. thanks you! also by using this will I be blocked again in the future or its permeant?
- **[Raphael Hen](https://stackoverflow.com/users/10467327)** (2022-12-14): Also, 1 more question. how can I have access to the pandas data? I want to have the symbols as a list. thanks again.
- **me** (2022-12-14): @RaphaelHen I'm not sure - you can try in a few hours or tomorrow to check and see. Some sites have stricter security than others. [Btw, you can get blocked with cloudscraper/HTMLSession  too, but it's less likely.]
- **me** (2022-12-14): For *"the symbols as a list"*: either **`symList = list(pd.read_html(table.prettify())[0]['Symbol'])`** **OR** `iepDf = pd.read_html(table.prettify())[0]` [to have the dataframe as `iepDf` first] followed by `symList = list(iepDf['Symbol'])` should do
