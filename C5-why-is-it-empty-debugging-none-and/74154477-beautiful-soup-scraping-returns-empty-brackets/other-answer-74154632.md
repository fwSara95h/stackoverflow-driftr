---
title: "Beautiful Soup Scraping returns empty brackets"
site: stackoverflow
question_id: 74154477
answer_id: 74154632
url: https://stackoverflow.com/a/74154632
author: "0stone0"
author_url: https://stackoverflow.com/users/5625547
posted: 2022-10-21T13:48:21Z
last_edited: never
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5de9eaf81b49616bcb8b18c15f2c188e86993634eab2bfc52ec8ae32734b26bb
role: another answer on the same question, kept as context; not my work
---

# Answer by [0stone0](https://stackoverflow.com/users/5625547) — 2022-10-21

Posted on Stack Overflow, <https://stackoverflow.com/a/74154632>, 2022-10-21. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You're looking for a table with that id. However, the links shows that ID in a 
span.


----------

Change the first selector to find a span, then use `findNext()` to get the table.

There you can find the `tr` and `td` and print the `.text`:


```python3
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


html = 'https://en.wikipedia.org/wiki/List_of_largest_banks'

html_data = requests.get(html)

html_data_text = html_data.text

soup = BeautifulSoup(html_data_text, 'html.parser')

span = soup.find('span', id="By_market_capitalization")
table = span.findNext('table')

for row in table.findAll('tr'):
    tds = row.findAll('td')
    if len(tds) > 1:
        print(tds[1].text.strip())
```

```none
JPMorgan Chase
Industrial and Commercial Bank of China
Bank of America
Wells Fargo
China Construction Bank
Agricultural Bank of China
HSBC Holdings PLC
Citigroup Inc.
... more
```
