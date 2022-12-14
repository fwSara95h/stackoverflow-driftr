---
title: "Webscraping all available repos from a topic search on github"
site: stackoverflow
question_id: 74796978
url: https://stackoverflow.com/q/74796978
asked: 2022-12-14T10:43:16Z
asked_by: "ladybug"
asked_by_url: https://stackoverflow.com/users/6708782
last_edited: never
tags: [python, web-scraping, beautifulsoup, request]
score: 0
views_at_snapshot: 894
answer_count: 1
accepted_answer_id: 74821773
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 01b95c61e5460c63521d7292f523041ec30c271c04d8557e45263700bbbd545e
---

# Webscraping all available repos from a topic search on github

Asked by [ladybug](https://stackoverflow.com/users/6708782) on Stack Overflow, <https://stackoverflow.com/q/74796978>, 2022-12-14. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to create a dataframe from a webscraping. Precisely: from a search of a topic on github, the objective is to retrieve the **name** of the owner of the repo, the **link** and the **about**.

I have many problems.

**1.** The search shows that there are, for example, more than 300,000 repos, but my scraping can only get the information from 90. **I would like to scrape all available repos**. 

**2.** Sometimes about is empty. It stops me after creating a dataframe
> ValueError: All arrays must be of the same length

**3.** My search for names is completely strange.

**My code:**

    import requests
    from bs4 import BeautifulSoup

    import pandas as pd
    import re

    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36'}

    search_topics = "https://github.com/search?p="

    stock_urls = []
    stock_names = []
    stock_about = []

    for page in range(1, 99):

        req = requests.get(search_topics + str(page) + "&q=" + "nlp" + "&type=Repositories", headers = headers)
        soup = BeautifulSoup(req.text, "html.parser")

        #about
        for about in soup.select("p.mb-1"):
            stock_about.append(about.text)

        #urls
        for url in soup.findAll("a", attrs = {"class":"v-align-middle"}):
            link = url['href']
            complete_link = "https://github.com" + link
            stock_urls.append(complete_link)

        #profil name
        for url in soup.findAll("a", attrs = {"class":"v-align-middle"}):
            link = url['href']
            names = re.sub(r"\/(.*)\/(.*)", "\1", link)
            stock_names.append(names)

    dico = {"name": stock_names, "url": stock_urls, "about": stock_about}       
   
    #df = pd.DataFrame({"name": stock_names, "url": stock_urls, "about": stock_about})
    df = pd.DataFrame.from_dict(dico)

My output:

> ValueError: All arrays must be of the same length

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[baduker](https://stackoverflow.com/users/6106791)** (2022-12-14): GitHub has a search [API](https://docs.github.com/en/rest/search?apiVersion=2022-11-28). Use this instead of scraping.
- **[baduker](https://stackoverflow.com/users/6106791)** (2022-12-14): As for the error you're getting, check this https://stackoverflow.com/questions/40442014/python-pandas-valueerror-arrays-must-be-all-same-length
