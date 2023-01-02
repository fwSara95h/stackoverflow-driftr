---
title: "Web Scraping Using Beautiful Soup (prints data group listed into one cell instead of across individual cells)"
site: stackoverflow
question_id: 74986498
url: https://stackoverflow.com/q/74986498
asked: 2023-01-02T19:52:02Z
asked_by: "Gregory Durgin"
asked_by_url: https://stackoverflow.com/users/20884965
last_edited: 2023-01-02T21:17:20Z
tags: [python, beautifulsoup, python-requests]
score: 0
views_at_snapshot: 31
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bd9dd169a87ebaf66127e15481fb912c57f274398bb70d50d03a7fc29f0ff81b
---

# Web Scraping Using Beautiful Soup (prints data group listed into one cell instead of across individual cells)

Asked by [Gregory Durgin](https://stackoverflow.com/users/20884965) on Stack Overflow, <https://stackoverflow.com/q/74986498>, 2023-01-02, last edited 2023-01-02. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Trying to get the "all splits" line of numbers from https://insider.espn.com/nba/player/splits/_/id/532/type/nba/year/2003/category/perGame and webpages like it to all be in their own cell across the row in a csv file. currently prints listed into one cell.
Ideal format would be 

|   Name   |   Year   |  PER # |   GP     | Min |  etc.. |
|----------|----------|--------|----------|-----|--------|
|  name    | 2003     |  Per#  |   75     |39.4 |        |






```
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import pandas as pd


names_list = ["name", "lots", "of", "names", "defined", "earlier"]  # names of players
pers = ['Per#', "lots", "of", "PER numbers (integers) ", "defined", "earlier"]  # player efficency ratings
statsurls = ['https://insider.espn.com/nba/player/splits/_/id/532/type/nba/year/2003/category/perGame']  # 100s of players pages in this same format (found by going through the 'id/#' and 'year/#')
statslist = []


def GetStats(statsurl):
    statsreq = requests.get(statsurl)
    statssoup = BeautifulSoup(statsreq.text, 'lxml')
    t = statssoup.select('main#fittPageContainer div.Table__Scroller > table > tbody')
    all_splits = [h.text for h in t[0].find_all('tr')[1].find_all('td')]
    split_list = [elem.split() for elem in all_splits]
    statslist.append(split_list)

with ThreadPoolExecutor() as executor:
    RunStats = [executor.submit(GetStats, statsurl) for statsurl in statsurls]


names_stats = pd.DataFrame(zip(names_list, pers, statslist))
names_stats.to_csv('names&stats.csv', index=False)
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[MendelG](https://stackoverflow.com/users/12349734)** (2023-01-02): The desired output isn't too clear, you only want the row under "all_splits"?
- **[Gregory Durgin](https://stackoverflow.com/users/20884965)** (2023-01-02): desired output would be the data in that row within an individual column, while also having name and PER data in the same row
