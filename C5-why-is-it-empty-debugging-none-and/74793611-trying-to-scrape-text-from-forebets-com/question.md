---
title: "Trying to scrape text from forebets.com"
site: stackoverflow
question_id: 74793611
url: https://stackoverflow.com/q/74793611
asked: 2022-12-14T04:34:04Z
asked_by: "Coder"
asked_by_url: https://stackoverflow.com/users/20772125
last_edited: 2022-12-14T07:48:13Z
last_editor: "baduker"
last_editor_url: https://stackoverflow.com/users/6106791
tags: [python, web-scraping, beautifulsoup, python-requests]
score: -4
views_at_snapshot: 1290
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 49bc9c6e06a5cdc15f22b9adf63169c99c0f3ae9e3d23ef8b254d27e7d981b21
---

# Trying to scrape text from forebets.com

Asked by [Coder](https://stackoverflow.com/users/20772125) on Stack Overflow, <https://stackoverflow.com/q/74793611>, 2022-12-14, last edited 2022-12-14 by [baduker](https://stackoverflow.com/users/6106791). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to scrape certain information from forebet.com. I seem to be able to scrape the hometeam,awayteam,location but not the predicted score,correct score or weather.

Can somebody please look at my code and tell me home to scrape the predicted score, correct score and weather.
This is my code so far:


```
from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.forebet.com/en/predictions-world/world-cup').text


soup = BeautifulSoup(source, 'lxml')
teams= soup.find_all('a', class_= 'tnmscn')
for team in teams:
    hometeam = team.find('span',class_= 'homeTeam').text

    predictedscore = team.select_one('div', class_='ex_sc tabonly')
    awayteam = team.find('span',class_ = 'awayTeam').text
    date = team.find('span', class_='date_bah').text
    location = team.find('name address', 'content').text
    weather = team.find('span', class_="wnums")[0].text
    print(hometeam,predictedscore ,awayteam,date,weather)

```

Thank you for the help


Try to scrape forebet.com can't seem to scrape all the necessary data.
