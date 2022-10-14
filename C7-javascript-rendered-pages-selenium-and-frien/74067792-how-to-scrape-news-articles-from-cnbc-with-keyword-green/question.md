---
title: "How to scrape news articles from cnbc with keyword \"Green hydrogen\"?"
site: stackoverflow
question_id: 74067792
url: https://stackoverflow.com/q/74067792
asked: 2022-10-14T10:17:44Z
asked_by: "Hitesh Prajapati"
asked_by_url: https://stackoverflow.com/users/20239660
last_edited: 2022-10-14T10:52:11Z
last_editor: "HedgeHog"
last_editor_url: https://stackoverflow.com/users/14460824
tags: [python, web-scraping, beautifulsoup, feed, feedparser]
score: 0
views_at_snapshot: 1264
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c29b55fcfbbea16e76d2a97c93a8ccf96c15543b58d4137b7e163bc6db9139f0
---

# How to scrape news articles from cnbc with keyword "Green hydrogen"?

Asked by [Hitesh Prajapati](https://stackoverflow.com/users/20239660) on Stack Overflow, <https://stackoverflow.com/q/74067792>, 2022-10-14, last edited 2022-10-14 by [HedgeHog](https://stackoverflow.com/users/14460824). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to scrap news article listed in this url, all article are in `span.Card-title`. But this  gives blank output. Is there any to resolve this?

    from bs4 import BeautifulSoup as soup
    
    import requests
    
    cnbc_url = "https://www.cnbc.com/search/?query=green%20hydrogen&qsearchterm=green%20hydrogen"
    
    html = requests.get(cnbc_url)
    
    bsobj = soup(html.content,'html.parser')
    
    day = bsobj.find(id="root")
    
    print(day.find_all('span',class_='Card-title'))
    
    for link in bsobj.find_all('span',class_='Card-title'):
    
        print('Headlines : {}'.format(link.text))

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2022-10-14): I think it would be much easier to use [selenium](https://medium.com/featurepreneur/an-introduction-to-web-automation-using-selenium-python-2ad84814b11c) for this, than to try to trace and imitate the sequence of requests and parsing that might be necessary otherwise
