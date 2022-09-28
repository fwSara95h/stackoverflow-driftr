---
title: "python beautifulsoup to download specific .zip files from a website"
site: stackoverflow
question_id: 73885207
url: https://stackoverflow.com/q/73885207
asked: 2022-09-28T16:54:08Z
asked_by: "Anusha"
asked_by_url: https://stackoverflow.com/users/19907888
last_edited: never
tags: [python, web-scraping, beautifulsoup, python-requests]
score: 1
views_at_snapshot: 1093
answer_count: 4
accepted_answer_id: 73885556
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 96accb7b314de702aaf12dd6ca10e1f4478e4a250024665e99274dd367c3d8c4
---

# python beautifulsoup to download specific .zip files from a website

Asked by [Anusha](https://stackoverflow.com/users/19907888) on Stack Overflow, <https://stackoverflow.com/q/73885207>, 2022-09-28. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.


I am new to web scraping. I am trying to download only the weekly .zip files from the below website. I could able to parse the </li> label and couldn't go beyond that to download the weekly zip files.

[https://download.cms.gov/nppes/NPI_Files.html][1]


[html code for 'li' tag][2]


    import requests
    from bs4 import BeautifulSoup
    URL = "https://download.cms.gov/nppes/NPI_Files.html"
    r = requests.get(URL)
    #print(r.content)
    soup = BeautifulSoup(r.content, 'html.parser')
    #print(soup.prettify())
    links=[]
    
    ref = soup.select('li')
    #print(ref)
    
    for i in ref:


  [1]: https://download.cms.gov/nppes/NPI_Files.html
  [2]: https://i.sstatic.net/pl04m.png
