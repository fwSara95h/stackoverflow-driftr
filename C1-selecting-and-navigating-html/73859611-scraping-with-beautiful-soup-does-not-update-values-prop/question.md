---
title: "Scraping with Beautiful Soup does not update values properly"
site: stackoverflow
question_id: 73859611
url: https://stackoverflow.com/q/73859611
asked: 2022-09-26T20:26:46Z
asked_by: "kobo"
asked_by_url: https://stackoverflow.com/users/17280882
last_edited: never
tags: [python, web-scraping, beautifulsoup, urllib]
score: 0
views_at_snapshot: 129
answer_count: 2
accepted_answer_id: 73862506
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 4e5b9913c570818dcbe827065fd9e9d576f8c4007848f8054aa4ccfce1ab5f45
---

# Scraping with Beautiful Soup does not update values properly

Asked by [kobo](https://stackoverflow.com/users/17280882) on Stack Overflow, <https://stackoverflow.com/q/73859611>, 2022-09-26. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I try to web-scrape weather website but the data does not update properly. The code:

    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    
    url = 'https://www.wunderground.com/dashboard/pws/KORPISTO1'
    
    while True:
        soup = BeautifulSoup(urlopen(url), 'html.parser')
        data = soup.find("div", {"class": "weather__text"})
        print(data.text)

I am looking at 'WIND & WIND GUST' in 'CURRENT CONDITIONS' section. It prints the first values correctly (for example 1.0 / 2.2 mph) but after that the values update very slowly (at times 5+ minutes pass by) even though they change every 10-20-30 seconds in the website.

And when the values update in Python they are still different from the current values in the website.
