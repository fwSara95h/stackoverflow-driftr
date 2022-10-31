---
title: "How to find data-id content in webscraping (python)"
site: stackoverflow
question_id: 74261711
url: https://stackoverflow.com/q/74261711
asked: 2022-10-31T10:10:46Z
asked_by: "Lautjelief"
asked_by_url: https://stackoverflow.com/users/20340060
last_edited: never
tags: [python, web-scraping, beautifulsoup, python-requests]
score: 0
views_at_snapshot: 115
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9e3dd348c6fdeff89c55809201b76867196d40f59937325bcbd5f4b97e5089cd
---

# How to find data-id content in webscraping (python)

Asked by [Lautjelief](https://stackoverflow.com/users/20340060) on Stack Overflow, <https://stackoverflow.com/q/74261711>, 2022-10-31. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Im trying to extract all Product Names, Product Codes, Prices, and Specs from a website, but there's no classes I can use to dig deeper into the html tree, so I have to use data-type and data-id, and all the tr and td info inside of it. However, if I now search for data-id, it only shows me the names, but not actually the content inside of it.

Right now the code is a little chaotic, Ive been trying as many solutions as I can, but none of them worked so far

Heres my code:

```

from cgitb import text
from pickle import TRUE
from bs4 import BeautifulSoup 
import requests
import urllib
import pandas as pd
import json

url = "https://www.albelli.nl/prijsoverzicht"



result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")



WholeDoc = doc.find('div', 'arc3-container arc3-margin--bottom-none arc3-margin--top-none price-overview--content')



for letstry in WholeDoc.find_all('div', attrs={'data-type' : 'Photobook'}):
   for item in letstry.find_all('tbody'):
    for moop in item.find_all('tr', attrs=('data-id')):
        print(moop)
    
```

I tried using the attrs=() function,  but it doesnt get me the content INSIDE of the data-id, however, it seems to work with the data-type

```
.find_all('tr', attrs=('data-id'))

```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2022-11-01): When you say *"content INSIDE of the data-id"* do you mean the value of the `data-id` [attribute](https://www.w3schools.com/html/html_attributes.asp) or the content of the *row* (`tr`) with data-id?
