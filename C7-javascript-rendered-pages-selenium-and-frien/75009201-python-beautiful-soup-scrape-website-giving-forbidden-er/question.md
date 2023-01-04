---
title: "Python Beautiful Soup scrape website giving forbidden error 403"
site: stackoverflow
question_id: 75009201
url: https://stackoverflow.com/q/75009201
asked: 2023-01-04T17:36:57Z
asked_by: "lily"
asked_by_url: https://stackoverflow.com/users/20880180
last_edited: 2023-01-04T18:54:57Z
last_editor: "Robert"
last_editor_url: https://stackoverflow.com/users/1431720
tags: [python, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 759
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1dfdeddfcb473394ab45cd4d558218e90dd1b3ed65d6827dfdb47490095a5f16
---

# Python Beautiful Soup scrape website giving forbidden error 403

Asked by [lily](https://stackoverflow.com/users/20880180) on Stack Overflow, <https://stackoverflow.com/q/75009201>, 2023-01-04, last edited 2023-01-04 by [Robert](https://stackoverflow.com/users/1431720). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I want to scrape jobs from indeed using beautiful soup only(not selenium), am facing forbidden error 403. below is my code:

```
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time as t

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
s = requests.Session()
s.headers.update(headers)
       
links_list = []
for current_page in range(1, 3):
        print(f'https://ae.indeed.com/jobs?q=&l=UAE&start={current_page}')
        r = s.get(f'https://ae.indeed.com/jobs?q=&l=UAE&start={current_page}') 
        page_num = (f'https://ae.indeed.com/jobs?q=&l=UAE&start={current_page}')  
   
        #mosaic-provider-jobcards > ul > li:nth-child(1) > div > div.slider_container.css-g7s71f.eu4oa1w0 > div > div.slider_item.css-kyg8or.eu4oa1w0 > div > table.jobCard_mainContent.big6_visualChanges > tbody > tr > td > div.css-1m4cuuf.e37uo190 > h2

        soup = BeautifulSoup(r.text, 'html.parser')
        links = soup.find_all('a')
        for link in links: 
             try:
                 url = link.select_one('a').get('href')
                 print(url)
                 r = s.get(f'{url}')
                 soup = BeautifulSoup(r.text, 'html.parser')
                 try:
                    title = soup.select_one(' div.jobsearch-JobInfoHeader-title-container > h1').text.strip() 
                 except Exception as e:
                   title = ''
                 links_list.append((url, title))
                 print(f'done {title}----{url}---{page_num} ')
                 t.sleep(1)
             except Exception as e:
                 print(e)
                 
df = pd.DataFrame(links_list, columns = ['URL','Job Title', 'Company','Job Description','Job Application'])
df.to_csv('uae.csv')
```                

I have tried to use User Agent but not solving anything.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[cards](https://stackoverflow.com/users/16462878)** (2023-01-04): have a look at the `https://ae.indeed.com/robots.txt` politic
- **[lily](https://stackoverflow.com/users/20880180)** (2023-01-04): Hi @cards, so many disallowed, so what can I do?, am a newbie. thanks
