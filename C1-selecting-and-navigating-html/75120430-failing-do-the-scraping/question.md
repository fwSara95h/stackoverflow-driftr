---
title: "Failing do the scraping"
site: stackoverflow
question_id: 75120430
url: https://stackoverflow.com/q/75120430
asked: 2023-01-14T18:42:30Z
asked_by: "Joao Fernandes"
asked_by_url: https://stackoverflow.com/users/21008579
last_edited: 2023-01-14T18:47:33Z
last_editor: "MattDMo"
last_editor_url: https://stackoverflow.com/users/1426065
tags: [python, web-scraping]
score: -1
views_at_snapshot: 63
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1b8a62b33c13742bb03b0a6636214a83765939a4a1916da32573b854307ccf08
---

# Failing do the scraping

Asked by [Joao Fernandes](https://stackoverflow.com/users/21008579) on Stack Overflow, <https://stackoverflow.com/q/75120430>, 2023-01-14, last edited 2023-01-14 by [MattDMo](https://stackoverflow.com/users/1426065). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm having a problem when I try to scrape the lyrics from google. I just want to extract the lyrics but instead is giving me the all text

I tried 
```
import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.google.com/search?q=RaindropsKeepFallinonMyHead+lyrcis&')
soup = BeautifulSoup(page.content, 'html.parser').find_all('div',jsname="WbKHeb")
print(soup)
```

and this:

```
def extract(Title):
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    url= f'https://www.google.com/search?q={Title}lyrics'
    r= requests.get(url, headers) # starting to get data from bilboard website
    soup= BeautifulSoup(r.content,'html.parser') # pull html from the website
    return soup
def transform(soup):
    page = soup.find('div',class_="B03h3d V14nKc EN1f2d ptcLIOszQJu__wholepage-card wp-ms")
    pageTEXT=BeautifulSoup(page.prettify(), 'html.parser').get_text()
    return print(page)
    
c=extract('RaindropsKeepFallinonMyHead')
print(c)
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Barmar](https://stackoverflow.com/users/1491895)** (2023-01-14): In the second version, just use `page.get_text()`
- **[Barmar](https://stackoverflow.com/users/1491895)** (2023-01-14): You never call `transform()`
