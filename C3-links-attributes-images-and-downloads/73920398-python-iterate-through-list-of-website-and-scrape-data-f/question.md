---
title: "Python - Iterate through list of website and scrape data - failing at requests.get"
site: stackoverflow
question_id: 73920398
url: https://stackoverflow.com/q/73920398
asked: 2022-10-01T17:29:11Z
asked_by: "JJH"
asked_by_url: https://stackoverflow.com/users/14197433
last_edited: 2022-10-02T13:04:10Z
tags: [python, loops, beautifulsoup]
score: -1
views_at_snapshot: 162
answer_count: 1
accepted_answer_id: 73929247
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9f914d7a3b00b4da6c27607de6a09ac204244dc752f9939ea1aae9921fae3c0e
---

# Python - Iterate through list of website and scrape data - failing at requests.get

Asked by [JJH](https://stackoverflow.com/users/14197433) on Stack Overflow, <https://stackoverflow.com/q/73920398>, 2022-10-01, last edited 2022-10-02. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a list of items that I scraped from Github. This is sitting in df_actionname ['ActionName'].
Each ['ActionName'] can then be converted into a ['Weblink'] to create a website link.
I am trying to loop through each weblink and scrape data from it.

My code:
    
    #Code to create input data

    import pandas as pd
    actionnameListFinal = ['TruffleHog OSS','Metrics embed','Super-Linter',]
    df_actionname = pd.DataFrame(actionnameListFinal, columns = ['ActionName'])

    # Create dataframes
    df_actionname = pd.DataFrame(actionnameListFinal, columns = ['ActionName'])

    #Create new column for parsed action names
    df_actionname['Parsed'] = df_actionname['ActionName'].str.replace( r'[^A-Za-z0-9]+','-', regex = True)
    df_actionname['Weblink'] = 'https://github.com/marketplace/actions/' + df_actionname['Parsed']

    for website in df_actionname['Weblink']:
    URL = df_actionname['Weblink']
    detailpage = requests.get(URL)



My code is failing at " detailpage= requests.get(URL) " 
The error message I am getting is: 


in get_adapter raise InvalidSchema(f"No connection adapters were found for {url!r}") requests.exceptions.InvalidSchema: No connection adapters were found for '0     https://github.com/marketplace/actions/Truffle...\n1     https://github.com/marketplace/actions/Metrics...\n2     https://github.com/marketplace/actions/Super-L...\n3       https://github.com/marketplace/actions/Swift-Doc\nName: Weblink, dtype: object'

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Code-Apprentice](https://stackoverflow.com/users/1440565)** (2022-10-01): It looks like you removed some parts of the error message. This is the critical detail for us to help answer your question. We will need to see the rest of the output with the URL to help you.
- **[EvensF](https://stackoverflow.com/users/2387806)** (2022-10-01): Can you give us an example of the input data `actionnameListFinal` ? In other words, can you provide a [example] ?
- **[JJH](https://stackoverflow.com/users/14197433)** (2022-10-02): I've copied the entirety of the error message and added code for a sample of the input data.
- **me** (2022-10-02): why are you inputting into `requests.get`  an entire pandas series (which is what `df_actionname['Weblink']` is and therefore what your `URL` is every time) ? wouldn't `detailpage = requests.get(website)` get you what you need instead?
