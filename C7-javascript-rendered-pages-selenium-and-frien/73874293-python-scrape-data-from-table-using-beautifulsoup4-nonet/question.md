---
title: "Python - Scrape Data from Table using BeautifulSoup4: 'NoneType' object has no attribute 'find'"
site: stackoverflow
question_id: 73874293
url: https://stackoverflow.com/q/73874293
asked: 2022-09-27T22:16:04Z
asked_by: "LawrenceTN"
asked_by_url: https://stackoverflow.com/users/9078486
last_edited: never
tags: [python, beautifulsoup]
score: 0
views_at_snapshot: 38
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e73613ba54dcca92d2e7511a179e2a138627b73d95f21017e293da618022f229
---

# Python - Scrape Data from Table using BeautifulSoup4: 'NoneType' object has no attribute 'find'

Asked by [LawrenceTN](https://stackoverflow.com/users/9078486) on Stack Overflow, <https://stackoverflow.com/q/73874293>, 2022-09-27. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Python newbie here.

I am practicing and trying to scrape some data off a table using BeautifulSoup4 and then transfer it to an Excel sheet.
Been at it for a few hours and finally kicking in and asking for some help.

I keep getting the error:

*'NoneType' object has no attribute 'find'*

    from bs4 import BeautifulSoup
    import requests, openpyxl
    
    # Scrape data from inmotion.dhl
    
    try:
        url = requests.get('https://inmotion.dhl/en/formula-1/fastest-pit-stop-award')
        url.raise_for_status()
    
        soup = BeautifulSoup(url.text,'html.parser')
    
        table = soup.find("table", class_="f1-award-table")
        table_body = table.find('tbody')
    
        rows = table_body.find_all('tr')
    
        for row in rows:
            cols = row.find_all('td')
            print(cols)
    
    except Exception as e:
        print(e)
