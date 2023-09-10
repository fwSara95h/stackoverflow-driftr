---
title: "Webcrawler for Testing und learn"
site: stackoverflow
question_id: 77060537
answer_id: 77077760
url: https://stackoverflow.com/a/77077760
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-09-10T20:22:50Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/77077760/revisions
accepted: false
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 65a411690a8442f83c72e391b58ed3f2d7a50ba886fd38cf87cf22f1838c0abf
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-09-10

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/77077760>, 2023-09-10; score 0. Text as retrieved 2026-10-12.

you could try using [`HTMLSession`](https://requests.readthedocs.io/projects/requests-html/en/latest/) instead of `requests` - that worked for me.

```py
from bs4 import BeautifulSoup 
from requests_html import HTMLSession

url = "https://www.anisearch.de/anime/2788,naruto"
source = HTMLSession().get(url)
# source.raise_for_status() ## good habit in general

soup = BeautifulSoup(source.content, 'html.parser')
```

[![op][1]][1]


  [1]: https://i.sstatic.net/iHnTg.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[D1skanime](https://stackoverflow.com/users/18557168)** (2023-09-29): Thx for the help but it still not work for me  maybe to try with a user Agent like this?  `headers = {     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' } source = HTMLSession().get(url, headers=headers)`
- **me** (2023-10-01): @D1skanime does it work for you then? I usually use HTMLSession bc I'm not good with headers, but it doesn't work 100%
- **[D1skanime](https://stackoverflow.com/users/18557168)** (2023-10-04): No it doesn't work for me, that's why I ask if it works for you with header. Are there other possibilities?  Must possibly try with a porxy that I start directly from python? Or what other possibilities are there?
