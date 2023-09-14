---
title: "Open a list of keywords in txt/csv and search each keyword on Google"
site: stackoverflow
question_id: 77108312
url: https://stackoverflow.com/q/77108312
asked: 2023-09-14T20:53:37Z
asked_by: "Geovanne Santos"
asked_by_url: https://stackoverflow.com/users/22563194
last_edited: 2023-09-20T05:12:53Z
last_editor: "Trenton McKinney"
last_editor_url: https://stackoverflow.com/users/7758804
tags: [python, web-scraping, beautifulsoup]
score: -3
views_at_snapshot: 116
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d7d2edeaf8fb1ab5f76027acac9269c81bb38f1dc21cf896e0ce7248242337bb
---

# Open a list of keywords in txt/csv and search each keyword on Google

Asked by [Geovanne Santos](https://stackoverflow.com/users/22563194) on Stack Overflow, <https://stackoverflow.com/q/77108312>, 2023-09-14, last edited 2023-09-20 by [Trenton McKinney](https://stackoverflow.com/users/7758804). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm new to Python and I want to develop something automatic to Open a list of keywords in txt/csv, search each keyword and collect only the first link and save the first link of each first key.

How can I do this?

With a lot of research, I found this code but it only collects 1 link and only carries a specific keyword. Is it possible to add something that collects the keywords from a txt/csv file and searches one by one and saves each first url of the Google results?


```
from bs4 import BeautifulSoup
import requests

search = 'keyword here'
url = 'https://www.google.com/search'

headers = {
	'Accept' : '*/*',
	'Accept-Language': 'en-US,en;q=0.5',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
}
parameters = {'q': search}

content = requests.get(url, headers = headers, params = parameters).text
soup = BeautifulSoup(content, 'html.parser')

search = soup.find(id = 'search')
first_link = search.find('a')

print(first_link['href'])
```
