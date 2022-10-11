---
title: "Scraping links from the Abstract, and Early Life sections separately"
site: stackoverflow
question_id: 74031411
url: https://stackoverflow.com/q/74031411
asked: 2022-10-11T16:37:55Z
asked_by: "Minda"
asked_by_url: https://stackoverflow.com/users/12863170
last_edited: 2022-10-11T16:59:34Z
tags: [python, beautifulsoup, wikipedia]
score: -1
views_at_snapshot: 117
answer_count: 1
accepted_answer_id: 74036946
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 874c5297486d9d0851a89fedfbd9399b0e9ba7e3f198faa29e522aff3c50224c
---

# Scraping links from the Abstract, and Early Life sections separately

Asked by [Minda](https://stackoverflow.com/users/12863170) on Stack Overflow, <https://stackoverflow.com/q/74031411>, 2022-10-11, last edited 2022-10-11. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I want to scrape all the links from the Abstract and Early Life section of this page. https://en.wikipedia.org/wiki/Barack_Obama 
I want to store the links I get from the two sections separately. However, I am having issues with isolating that tag/class. I tried to use class "mw-headline" for the early life section but that is returning only the header text. Any hints are really appreciated. 

I couldn't figure out how to the get abstract and early life sections separately. 

    url='https://en.wikipedia.org/wiki/Barack_Obama'
    response = requests.get(url)
    soup=bs(response.content,'html.parser')
    page=soup.find('div',attrs={'id':'bodyContent'})

    early_life=page.findAll('span',attrs={'class':'mw-headline'})

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[HedgeHog](https://stackoverflow.com/users/14460824)** (2022-10-11): Help us to help you - Please improve your question, so that we can reproduce your issue easily. Take a minute to check - How to create [mcve] Thanks
