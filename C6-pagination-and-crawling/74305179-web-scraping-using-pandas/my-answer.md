---
title: "web scraping using pandas"
site: stackoverflow
question_id: 74305179
answer_id: 74333634
url: https://stackoverflow.com/a/74333634
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-06T06:10:43Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74333634/revisions
accepted: false
score: 0
chapter: C6
chapter_title: "Pagination and crawling"
cluster: scrape-pagination-crawling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e866c92cf2d1f7ff5fb39d9d9a4cbd5235b30dabb2972e71ba0b5584758eb2c1
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-06

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74333634>, 2022-11-06; score 0. Text as retrieved 2026-10-12.

For me, just using [requests](https://pypi.org/project/requests/) to fetch the html before passing to `read_html` is getting the data. I just edited your code to 

```python
import pandas as pd
import re
url_link = 'https://www.taneps.go.tz/epps/viewAllAwardedContracts.do?d-3998960-p={}&selectedItem=viewAllAwardedContracts.do'
LIST = []
for number in range(1,5379):
  url = url_link.format(number)
  r = requests.get(url) # getting page -> html in r.text
  dframe = pandas.read_html(r.text, header=None)[0] 
  LIST.append(dframe)
Result_df = pd.concat(LIST)
Result_df.to_csv('Taneps_contracts.csv')
```

I didn't even have to add headers, but if this isn't enough for you (i.e., if the program breaks or if you don't end up with 53770+ rows), try [adding convincing headers](https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/#therightwaytorotateuseragentsinanyprogram) or using something like [HTMLSession](https://requests.readthedocs.io/projects/requests-html/en/latest/) instead of directly calling `requests.get`...
