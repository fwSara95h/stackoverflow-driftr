---
title: "Facebook Scraping Python"
site: stackoverflow
question_id: 74100308
url: https://stackoverflow.com/q/74100308
asked: 2022-10-17T16:24:33Z
asked_by: "Ani G"
asked_by_url: https://stackoverflow.com/users/20265186
last_edited: 2024-08-07T12:54:26Z
last_editor: "VLAZ"
last_editor_url: https://stackoverflow.com/users/3689450
tags: [python, facebook, web-scraping, beautifulsoup, lxml]
score: 0
views_at_snapshot: 8818
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5d0ad7c69d129c473dba6422d90a1395ca3257d29b342025cc02c03c8f3dc2fb
---

# Facebook Scraping Python

Asked by [Ani G](https://stackoverflow.com/users/20265186) on Stack Overflow, <https://stackoverflow.com/q/74100308>, 2022-10-17, last edited 2024-08-07 by [VLAZ](https://stackoverflow.com/users/3689450). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Trying to scrape fb with python, I need the page's email, just downloaded BeautifulSoup, lxml, requests libraries

    from bs4 import BeautifulSoup
    import requests
    
    html_text = requests.get('https://www.facebook.com/KNOW-MORE-training-center-111698018315706/?ref=page_internal').text
    soup = BeautifulSoup(html_text, 'lxml')
    a = soup.find('h2', class_ = 'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv x1fey0fg').text.replace(' ','')
    
    print(a)

Code isn't working. What's wrong??? Grateful for the answers!!!

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Community](https://stackoverflow.com/users/-1)** (2022-10-17): Please edit the question to limit it to a specific problem with enough detail to identify an adequate answer.
- **[andyrandy](https://stackoverflow.com/users/757508)** (2022-10-17): css classes change all the time on facebook - most likely for two reasons: they use css modules with namespaces, and they dont want others to easily scrape it. because scraping is not allowed on facebook.
