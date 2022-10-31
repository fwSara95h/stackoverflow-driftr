---
title: "Scraping a table Including hyperlinks and upload it to google sheet using python"
site: stackoverflow
question_id: 74263905
url: https://stackoverflow.com/q/74263905
asked: 2022-10-31T13:19:11Z
asked_by: "Mohamad Abdelsamad"
asked_by_url: https://stackoverflow.com/users/14140095
last_edited: never
tags: [python, pandas, web-scraping, beautifulsoup, python-requests]
score: -1
views_at_snapshot: 175
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 614da03843fecb0e28256289b5f54d5bfd50b76e0a9a9391df851ec36ec6e296
---

# Scraping a table Including hyperlinks and upload it to google sheet using python

Asked by [Mohamad Abdelsamad](https://stackoverflow.com/users/14140095) on Stack Overflow, <https://stackoverflow.com/q/74263905>, 2022-10-31. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to scrape a table and keep any hyperlinks included then upload the result to a google sheet
I have finished the first part using this code:

        
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    import re
    # Define URL
    url = 'https://www.marefa.org/%D9%82%D8%A7%D8%A6%D9%85%D8%A9_%D8%A3%D9%81%D8%B6%D9%84_%D8%A7%D9%84%D9%83%D8%AA%D8%A8_%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9'# Ask hosting server to fetch url
    requests.get(url)
    response=requests.get(url)
    print(response.status_code)
    #If the output is <Response [200]> so that means the server allows us to collect 
    soup = BeautifulSoup(response.content, 'lxml')
    indiatable=soup.find('table',{'class':"wikitable"})
    
    
    df=pd.read_html(str(indiatable))
    # convert list to dataframe
    df=pd.DataFrame(df[0])
    df.head()
    #df.to_excel("hi2.xlsx", index=False)


------------
Can anyone give me some hint on how to finish the rest of the task?
