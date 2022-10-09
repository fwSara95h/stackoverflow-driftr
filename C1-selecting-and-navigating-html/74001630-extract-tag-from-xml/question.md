---
title: "Extract Tag from XML"
site: stackoverflow
question_id: 74001630
url: https://stackoverflow.com/q/74001630
asked: 2022-10-09T01:47:19Z
asked_by: "TaxAssassin"
asked_by_url: https://stackoverflow.com/users/20194598
last_edited: 2022-10-09T05:35:02Z
last_editor: "HedgeHog"
last_editor_url: https://stackoverflow.com/users/14460824
tags: [python, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 144
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 54e8da49c56eed14b1d6d9b7b39499c5fe79c4a1ad7f321fc33d4e78ff753426
---

# Extract Tag from XML

Asked by [TaxAssassin](https://stackoverflow.com/users/20194598) on Stack Overflow, <https://stackoverflow.com/q/74001630>, 2022-10-09, last edited 2022-10-09 by [HedgeHog](https://stackoverflow.com/users/14460824). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm very new to Python and am attempting my first web scraping project. I'm attempting to extract the data following a tag within a XML data source. I've attached an image of the data I'm working with. My issue is that, it seems like no matter what tag I try to extract I constantly return no results. I am able to return the entire data source so I know the connection is not the issue. 

My ultimate goal is to loop through all of the data and return the data following a particular tag. I think if I can understand why I'm unable to print a singular particular tag I should be able to figure out how to loop through all of the data. I've looked through similar posts but I think the tree in my set of data is particularly troublesome (that and my inexperience).

My Code:

    from bs4 import BeautifulSoup    
    import requests 
    #Assign URL to scrape    
    URL = "http://api.powertochoose.org/api/PowerToChoose/plans?zip_code=78364"
    #Fetch the raw HTML Data
    Data = requests.get(URL)
    Soup = BeautifulSoup(Data.text, "html.parser")
    tags = Soup.find_all('fact_sheet')
    print (tags)


[![enter image description here][1]][1]


  [1]: https://i.sstatic.net/R8wft.png
