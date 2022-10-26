---
title: "How can I scrape an information from Wester Union webpage?"
site: stackoverflow
question_id: 74212250
url: https://stackoverflow.com/q/74212250
asked: 2022-10-26T18:00:13Z
asked_by: "Vinícius"
asked_by_url: https://stackoverflow.com/users/11453261
last_edited: never
tags: [python, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 121
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c5c113a46fa1cfbd14ec6716ec04733a0743b2651b96a7de8c908e3aa27bf302
---

# How can I scrape an information from Wester Union webpage?

Asked by [Vinícius](https://stackoverflow.com/users/11453261) on Stack Overflow, <https://stackoverflow.com/q/74212250>, 2022-10-26. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to scrape the currency convertion information of https://www.westernunion.com/ (attached photo). I found the corresponding tag but it returns an empty list. 

Can anyone help me? I appreciate that.




Here is my current code (using BeautifulSoup):

```python
# Web Crawling:
import requests
# Web Scrapping:
from bs4 import BeautifulSoup
# Regular Expressions: 
import re

url = 'https://www.westernunion.com/br/pt/web/send-money/start?ReceiveCountry=AR&ISOCurrency=ARS&SendAmount=100.00&FundsOut=BA&FundsIn=WUPay'

soup = BeautifulSoup(requests.get(url).content, 'html.parser')
information = soup.find_all('span', {'class': 'ng-star-inserted'})
information
```

Only need that simple information "*1.00 BRL = 0.1596 British Pound*"
Thanks!
