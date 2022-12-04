---
title: "Ebay Scraping, filter out international results, select parents that do not have specific descendants"
site: stackoverflow
question_id: 74673061
url: https://stackoverflow.com/q/74673061
asked: 2022-12-04T05:15:32Z
asked_by: "Jose"
asked_by_url: https://stackoverflow.com/users/20679076
last_edited: 2022-12-04T17:28:49Z
tags: [python, beautifulsoup]
score: 0
views_at_snapshot: 126
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 641e01cf73796588105214919d80ef679859f520c6f8874b0199200f3e6e0c97
---

# Ebay Scraping, filter out international results, select parents that do not have specific descendants

Asked by [Jose](https://stackoverflow.com/users/20679076) on Stack Overflow, <https://stackoverflow.com/q/74673061>, 2022-12-04, last edited 2022-12-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

EDIT:

I have solved this thanks to @Driftr95

Here is the working code: 

```
import xlwings as xw
from bs4 import BeautifulSoup
import requests
import statistics

@xw.func
def get_prices(url,args =[]):
    url = requests.get(url).content
    soup = BeautifulSoup(url,'lxml')

    products = []
    rsecSel = 'li:not(.srp-river-answer--REWRITE_START ~ li)'
    iDetSel = f'div[id="srp-river-results"] {rsecSel} div.s-item__details'
    results = soup.select(f'{iDetSel}:not(:has(span.s-item__location))')
    for item in results:
        price = item.find('span', class_='s-item__price').text.replace('$', '').replace(',', '')

        if 'to' not in price:
            price = float(price)
            products.append(price)
    
        mean = round(statistics.mean(products), 2)
        median = round(statistics.median(products), 2)

    return mean, median
```
I now have a working function in excel that will automatically look up sold prices on ebay that I can iterate over a large amount of products instantly!

I have some code that I put together to scrape ebay sold prices using BeautifulSoup and so far it is working pretty good. The only issue I currently have is that it also pulls prices for 2 categories that ebay adds to the search results page (International Sellers, and results matching fewer words)

I am struggling to filter these out. Its like I need to identify if the listing (the parent) contains a specific descendant and then filter out that parent. I hope that is clear, here is a sample:

https://www.ebay.com/sch/57988/i.html?_from=R40&_nkw=Fjallraven%20nuuk%20parka&LH_Complete=1&LH_Sold=1&_udlo=50&_udhi=600&LH_PrefLoc=1

The picture is an example of an item that I would like to filter out. It has a Span Class for location. This class only exists if the item is from an international seller.


```
import xlwings as xw
import bs4 as bs
import requests
import statistics

@xw.func
def get_prices(url,args =[]):
    url_base = requests.get(url).text
    soup = bs.BeautifulSoup(url_base,'lxml')

    products = []
    results = soup.find('div', {'class': 'srp-river-results clearfix'}).find_all('div', {'class': ['s-item__details clearfix'] })
    for item in results:
        price = item.find('span', class_='s-item__price').text.replace('$', '').replace(',', '')

        if 'to' not in price:
            price = float(price)
            products.append(price)

#def calculate_averages(products):
    mean = round(statistics.mean(products), 2)
    median = round(statistics.median(products), 2)
    mode = round(statistics.mode(products), 2)

    return mean, median, mode
```


I have tried several different methods but cannot seem to filter out the parents based on a class in one of the children.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Andrej Kesely](https://stackoverflow.com/users/10035985)** (2022-12-04): I don't understand...so what results do you want to get from that page?
- **[Jose](https://stackoverflow.com/users/20679076)** (2022-12-04): I am trying to only get the "Main" results if you will. Ebay adds international results and results that are not as relevant.
