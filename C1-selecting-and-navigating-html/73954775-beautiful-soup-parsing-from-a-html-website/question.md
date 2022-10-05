---
title: "Beautiful Soup Parsing from a HTML Website"
site: stackoverflow
question_id: 73954775
url: https://stackoverflow.com/q/73954775
asked: 2022-10-05T00:10:54Z
asked_by: "laisp-lostlamb"
asked_by_url: https://stackoverflow.com/users/20162704
last_edited: 2022-10-05T00:27:38Z
last_editor: "Andrej Kesely"
last_editor_url: https://stackoverflow.com/users/10035985
tags: [python, pandas, beautifulsoup]
score: 0
views_at_snapshot: 136
answer_count: 1
accepted_answer_id: 74138200
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 82267944888c1541c8936f36ae1b001bd4df48cbf5aec0a9d28564a580a5652f
---

# Beautiful Soup Parsing from a HTML Website

Asked by [laisp-lostlamb](https://stackoverflow.com/users/20162704) on Stack Overflow, <https://stackoverflow.com/q/73954775>, 2022-10-05, last edited 2022-10-05 by [Andrej Kesely](https://stackoverflow.com/users/10035985). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm very new to web scrapping and perhaps python3 as well, was hoping to receive help in order to solve my problem.

I am scraping from the following webpage: http://ets.aeso.ca/ets_web/ip/Market/Reports/CSDReportServlet

I received code from: https://stackoverflow.com/questions/72651724/new-to-beautiful-soup-need-to-scrape-tables-from-an-online-report

Here's the code example of what I have. (See below)

This generates:

```
                                      GAS            GAS.1            GAS.2  \
0                            Simple Cycle     Simple Cycle     Simple Cycle   
1                                   ASSET               MC              TNG   
2                     AB Newsprint (ANC1)               63               65   
3                           Bantry (ALP1)                7                6   
4                        Bellshill (BHL1)                5                5   
5                     Carson Creek (GEN5)               15               12   
6                     Cloverbar #1 (ENC1)               48               35   
7                     Cloverbar #2 (ENC2)              101               93   
8                     Cloverbar #3 (ENC3)              101               91   
9      Crossfield Energy Centre #1 (CRS1)               48                0   
10     Crossfield Energy Centre #2 (CRS2)               48               41   
11    Crossfield Energy Centre #3 (CRS3)^               48               41   
```

Question: Not sure why the code splits this into different columns.
GAS.2  \ this splits the data for GAS.3 onto a entirely different line.

What I'm looking for is how do I write this information into excel?
ie. the first 3 rows need to be removed, GAS & Simple Cycle & ASSET is not information I need to display.
```
                                      GAS            GAS.1            GAS.2  \
0                            Simple Cycle     Simple Cycle     Simple Cycle   
1                                   ASSET               MC              TNG   
2                     AB Newsprint (ANC1)               63               65   
3                           Bantry (ALP1)                7                6   
```
I need the first two items with the name in a dictionary with two values.

ie 
afc = {'AB Newsprint (ANC1)': {'MC':63,'TNG': 65}, 'Bantry (ALP1)': {'MC': 7,'TNG': 6}}

For the entire list of td scraped from the GAS table, into dictionary above.

Then I need to display it in a DataPipe (excel) fashion.

ie

    A1 = AB Newsprint (ANC1)
    B1 = 63
    C1 = 65
    
    A2 = Bantry (ALP1)
    B2 = 7
    C2 = 6

[Please click to see image][1]

How should I code or proceed in order to accomplish this?

```
import requests, sys, re
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
#np.set_printoptions(threshold=sys.maxsize)
#np.set_printoptions(threshold='nan')
pd.set_option('display.max_rows', 100000)
pd.set_option('display.max_columns', 100000)

def get_summary(soup):
    summary = soup.select_one(
        "table:has(b:-soup-contains(SUMMARY)):not(:has(table))"
    )
    summary.tr.extract()
    return pd.read_html(str(summary))[0]

def get_generation(soup):
    generation = soup.select_one(
        "table:has(b:-soup-contains(GENERATION)):not(:has(table))"
    )
    generation.tr.extract()
    for td in generation.tr.select("td"):
        td.name = "th"
    return pd.read_html(str(generation))[0]

def get_interchange(soup):
    interchange = soup.select_one(
        "table:has(b:-soup-contains(INTERCHANGE)):not(:has(table))"
    )
    interchange.tr.extract()
    for td in interchange.tr.select("td"):
        td.name = "th"
    return pd.read_html(str(interchange))[0]

def get_gas(soup):
    gas = soup.select_one(
        "table:has(b:-soup-contains(GAS)):not(:has(table))"
    )
    #for td in gas.tr.select("td"):
        #td.name = "th"
    return pd.read_html(str(gas))[0]
'''    
def print_full(x):
    dim = x.shape
    pd.set_option('display.max_rows', dim[0])#dim[0] = len(x)
    pd.set_option('display.max_columns', dim[1])
    #print(x)
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')
'''
url = "http://ets.aeso.ca/ets_web/ip/Market/Reports/CSDReportServlet"
#html5lib: A pure-python library for parsing HTML. It is designed to conform to the WHATWG HTML specification
soup = BeautifulSoup(requests.get(url).content, "html5lib")

#print(get_summary(soup))
#print(get_generation(soup))
#print(get_interchange(soup))
print (get_gas(soup))
#print(get_hydro(soup))
#print(get_biomass(soup))
#print(get_energystorage(soup))
#print(get_solar(soup))
#print(get_wind(soup))
#print(get_coal(soup))
```


  [1]: https://i.sstatic.net/fjRX4.png
