---
title: "Scraping with Beautiful Soup does not update values properly"
site: stackoverflow
question_id: 73859611
answer_id: 73859795
url: https://stackoverflow.com/a/73859795
author: "Khaled Koubaa"
author_url: https://stackoverflow.com/users/5539782
posted: 2022-09-26T20:47:59Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e924fd8be4a4b3b72e501d5aee33ac8efcdb5244641cb96a2d776cbaad58fbba
role: another answer on the same question, kept as context; not my work
---

# Answer by [Khaled Koubaa](https://stackoverflow.com/users/5539782) — 2022-09-26

Posted on Stack Overflow, <https://stackoverflow.com/a/73859795>, 2022-09-26. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

try:
```
import requests
from bs4 import BeautifulSoup

url = 'https://www.wunderground.com/dashboard/pws/KORPISTO1'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'}
session = requests.Session()
r = session.get(url, timeout=30, headers=headers)     # print(r.status_code)
soup = BeautifulSoup(r.content, 'html.parser')

#'WIND & WIND GUST' in 'CURRENT CONDITIONS' section
wind_gust = [float(i.text) for i in soup.select_one('.weather__header:-soup-contains("WIND & GUST")').find_next('div', class_='weather__text').select('span.wu-value-to')]

print(wind_gust)
[1.8, 2.2]

wind = wind_gust[0]
gust = wind_gust[1]

print(wind)
1.8

print(gust)
2.2
```
