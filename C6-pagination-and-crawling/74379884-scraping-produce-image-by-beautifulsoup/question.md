---
title: "Scraping Produce image by BeautifulSoup"
site: stackoverflow
question_id: 74379884
url: https://stackoverflow.com/q/74379884
asked: 2022-11-09T18:42:41Z
asked_by: "Ashraf"
asked_by_url: https://stackoverflow.com/users/20329031
last_edited: never
tags: [python, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 88
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b63075d1343d0d6cfd848f623a9ac5ee2fb947a5b0619dedb5e4e3b0d3780369
---

# Scraping Produce image by BeautifulSoup

Asked by [Ashraf](https://stackoverflow.com/users/20329031) on Stack Overflow, <https://stackoverflow.com/q/74379884>, 2022-11-09. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to Scrap the product image of this page:

https://www.noon.com/egypt-ar/golden-wood-edp-100ml/N39185122A/p/?o=d55236b5f16d3c9d

but i still have an error, I using beaurifaulSoup, but it give me none:

That what i got:

[![enter image description here](https://i.sstatic.net/4AZGu.png)](https://i.sstatic.net/4AZGu.png)

```
import requests
from bs4 import BeautifulSoup
import time
import json
import re



page_numbers = 1




 
while True:

    URL = "https://www.noon.com/egypt-ar/beauty-and-health/beauty/eg-nov22-clearance-2/?limit=50&page="+str(page_numbers)

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    products = soup.find_all("span",class_="sc-5e739f1b-0 gEERDr wrapper productContainer")
    


    time.sleep(1) 
    product_Source =soup.find("div",class_="sc-95314d04-3 dnAXkE")
    product_String = product_Source.text
    all_words = product_String.split()
    products_Numbers= all_words[0]

#loop to Get Data

    for product in products:

        product_link = product.find("a").attrs["href"]                                                         #Get product product links
        
        productFullLink = "https://www.noon.com"+product_link
        Moreinfo = requests.get(productFullLink,headers=headers)                                         # Get informattion from page
        Product_Details = BeautifulSoup(Moreinfo.text,"html.parser")
        #time.sleep(1)

       
            
        product_image = Product_Details.find_all("div",class_="sc-8cbb8e24-2 eDXUdi")
       
        

        print(product_image)
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Tim Roberts](https://stackoverflow.com/users/1883316)** (2022-11-09): Those links do not contain any divs with class "sc-8cbb8e24-2".  They have -0, -1, and -3, but not -2.
