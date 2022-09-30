---
title: "how to scrape a website with pages that dont affect the url"
site: stackoverflow
question_id: 73912424
url: https://stackoverflow.com/q/73912424
asked: 2022-09-30T18:01:54Z
asked_by: "Nuspli"
asked_by_url: https://stackoverflow.com/users/19232040
last_edited: 2022-09-30T18:06:27Z
last_editor: "OneCricketeer"
last_editor_url: https://stackoverflow.com/users/2308683
tags: [python, web-scraping, beautifulsoup]
score: 1
views_at_snapshot: 176
answer_count: 1
accepted_answer_id: 73914652
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9c28eb452ada31b3c869285b8c9fe6759582fdadb6afb7361230232e1ec9f63c
---

# how to scrape a website with pages that dont affect the url

Asked by [Nuspli](https://stackoverflow.com/users/19232040) on Stack Overflow, <https://stackoverflow.com/q/73912424>, 2022-09-30, last edited 2022-09-30 by [OneCricketeer](https://stackoverflow.com/users/2308683). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

What I'd like to do is to scrape a Clash of Clans players profile site from clashofstats.com for instance: https://www.clashofstats.com/players/captain-morgan-L9YJUPY22/history/log

to get an approximation of the last and first time played based on the logged clan activity, first of which I have already implemented with the following:
```
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.clashofstats.com/players/captain-morgan
L9YJUPY22/history/log')

soup = BeautifulSoup(response.content, 'html.parser')

end_dates = soup.find_all(class_="end date")

last_played = str(end_dates[0]).replace("<span class=\"end date\">", "")
last_played = last_played.replace(",", "")
last_played = last_played.replace("</span>", "")

print(f"Last  time played| {last_played}")
```
Output:
``` Last  time played| Sep 30 2022 ```
(weird format is to match the rest of the code)

Now back to my question, the problem comes with the first time played. clashofstats has multiple pages of logged clans, but when going to the last page (where the first date is) the url doesn't change and nor does the source code. I can only see changes from the dev Tools, but how can I direct, preferably using BeautifulSoup, to that last page and get the date?, if that is even possible.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[OneCricketeer](https://stackoverflow.com/users/2308683)** (2022-09-30): `requests` is downloading static HTML (one and done). It does not "browse" a site to change the "source" or url. Perhaps you should be using selenium instead?
- **[David](https://stackoverflow.com/users/328193)** (2022-09-30): In general it sounds like what you're looking for is a "headless browser", which is more than just an HTML parser.  It's essentially an entire browser engine, to execute JavaScript and update the DOM and all that, that you'd interact with in code.
- **[Nuspli](https://stackoverflow.com/users/19232040)** (2022-09-30): So if I'm getting this right, there is no way to accomplish what I wanted with requests? Then also what would it look like using selenium ?
- **me** (2022-10-01): @Nuspli with selenium you can pretty much interact with the site as you would directly. So you could "click" on the 2nd page and then "select" or "find" all the end_dates there too
