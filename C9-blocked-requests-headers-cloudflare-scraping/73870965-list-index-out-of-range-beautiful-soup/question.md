---
title: "list index out of range - beautiful soup"
site: stackoverflow
question_id: 73870965
url: https://stackoverflow.com/q/73870965
asked: 2022-09-27T16:33:24Z
asked_by: "Nicole_abdul"
asked_by_url: https://stackoverflow.com/users/20102708
last_edited: 2022-09-27T20:57:36Z
tags: [python, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 108
answer_count: 1
accepted_answer_id: 73874251
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 46ef245b06c0c51a715a3df2fdb1e877f74eb4fd623ecc619ab6f22ba828f74f
---

# list index out of range - beautiful soup

Asked by [Nicole_abdul](https://stackoverflow.com/users/20102708) on Stack Overflow, <https://stackoverflow.com/q/73870965>, 2022-09-27, last edited 2022-09-27. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

NEW TO PYTHON*** Below is my code I am using to pull a zip file from a website but I am getting the error, "list index out of range". I was given this code by someone else who wrote it but I had to change the URL and now I am getting the error. When I print(list_of_documents) it is blank. 

Can someone help me with this? The url requires access so you won't be able to try to input this code directly. I am trying to understand how to use beautiful soup in this and how I can get the list to populate correctly. 

    import datetime
    import requests
    import csv
    from zipfile import ZipFile as zf
    import os
    import pandas as pd
    import time
    from bs4 import BeautifulSoup
    import pyodbc
    import re

    #set download location

    downloads_folder = r"C:\Scripts\"


    ##### Creating outage dataframe

    #Get list of download links

    res = requests.get('https://www.ercot.com/mp/data-products/data-product-details?id=NP3-233-CD')

    ercot_soup = BeautifulSoup(res.text, "lxml")

    list_of_documents = ercot_soup.findAll('td', attrs={'class': 'labelOptional_ind'})
    list_of_links = ercot_soup.select('a')'

    ##create the url for the download 

    loc = str(list_of_links[0])[9:len(str(list_of_links[0]))-9]
    link = 'http://www.ercot.com' + loc
    link = link.replace('amp;','')

    # Define file name and set download path

    file_name = str(list_of_documents[0])[30:len(str(list_of_documents[0]))-5]
    file_path = downloads_folder + '/' + file_name

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[KaliMachine](https://stackoverflow.com/users/20071248)** (2022-09-27): can you put the output your answer?
- **[baduker](https://stackoverflow.com/users/6106791)** (2022-09-27): The site throws 403 `access denied` error.
- **[Community](https://stackoverflow.com/users/-1)** (2022-09-27): Please clarify your specific problem or provide additional details to highlight exactly what you need. As it's currently written, it's hard to tell exactly what you're asking.
- **[Nicole_abdul](https://stackoverflow.com/users/20102708)** (2022-09-27): @KaliMachine Do you mean to show the error I get?
- **me** (2022-09-27): @Nicole_abdul what are you trying to get with `labelOptional_ind` ? I don't see that when inspecting the page.
- **[Nicole_abdul](https://stackoverflow.com/users/20102708)** (2022-09-27): @Driftr95 that was there from the other person that created the original code using URL https://www.ercot.com/misapp/GetReports.do?reportTypeId=13103.
- **[Nicole_abdul](https://stackoverflow.com/users/20102708)** (2022-09-27): @Driftr95 I believe that is the part that is wrong but I am not sure what to change it to. I've never used Beautiful Soup so this is new to me.
- **me** (2022-09-27): @Nicole_abdul the list looks the same as far as I can see, and the source is the same. Why do you need to get it from this specific path?
