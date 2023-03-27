---
title: "Accessing tabbed elements with BeautifulSoup"
site: stackoverflow
question_id: 75847824
answer_id: 75852976
url: https://stackoverflow.com/a/75852976
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-27T07:11:57Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75852976/revisions
accepted: true
score: 1
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 47acd088c76941536d26aeccdd37c9b5c92bd8d3593a192dc3f67a240a5734c5
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-27

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75852976>, 2023-03-27; **accepted**; score 1. Text as retrieved 2026-10-12.

You can't with bs4 (unless you're obtaining the html with something that supports JavaScript and automated interaction with the page, like [selenium](https://medium.com/ymedialabs-innovation/2f8ad15efe25)), but you *can* request the data from the same API that the site fetches it from<sup>(view [screenshot][1] from [network logs](https://support.happyfox.com/kb/article/882-accessing-the-browser-console-and-network-logs/))</sup>. 

---

For example, for Japanese Yen:

```py
import request
import pandas as pd

cur_tab = 'JPY' # 'MostViewed' # 'USD' # 'EUR' #
api_endpt = f'https://markets.businessinsider.com/ajax/ExchangeRate_PopularListData' 
api_data = requests.get(f'{api_endpt}?currency={cur_tab}').json()
df = pd.DataFrame(api_data['ExchangeRates'])
```
[![opdf][2]][2]

---

Or to get all of the tabs:

```py
import request
import pandas as pd

cur_tabs = ['MostViewed', 'USD', 'EUR', 'JPY']
api_endpt = 'https://markets.businessinsider.com/ajax/ExchangeRate_PopularListData'

dfList = [pd.DataFrame(
    requests.get(f'{api_endpt}?currency={cur_tab}').json()['ExchangeRates']
) for cur_tab in cur_tabs] 
df = pd.concat(dfList, keys=cur_tabs)
```

[![opdf2][3]][3]


  [1]: https://i.sstatic.net/iDZWY.png
  [2]: https://i.sstatic.net/4gMsi.png
  [3]: https://i.sstatic.net/sLuz0.png
