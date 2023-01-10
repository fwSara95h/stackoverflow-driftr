---
title: "Why when extracting products data shows me that they are duplicate?"
site: stackoverflow
question_id: 75073129
url: https://stackoverflow.com/q/75073129
asked: 2023-01-10T16:37:50Z
asked_by: "ALI ALHARBI"
asked_by_url: https://stackoverflow.com/users/19026499
last_edited: never
tags: [python, beautifulsoup, data-extraction]
score: 0
views_at_snapshot: 73
answer_count: 2
accepted_answer_id: 75074128
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f38b9ae4465e1cb6939c8173c4b14af820fdbab5a9412f1b2392a3cd80196e8b
---

# Why when extracting products data shows me that they are duplicate?

Asked by [ALI ALHARBI](https://stackoverflow.com/users/19026499) on Stack Overflow, <https://stackoverflow.com/q/75073129>, 2023-01-10. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

When using bs4 the products show me that they are frequent despite all attempts to know solving this problem. I have failed to inform me to solve this problem and where is it?



```
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from itertools import zip_longest


page = 'https://niceonesa.com/ar/'

headers = {
    'User-Argent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Viewer/97.9.3678.79'
}

productlink =[]
titles = []
brands=[]
prices=[]
offers = []
rates =[]
rate_starts=[]

for x in range(1,2):
    r= requests.get(f'https://niceonesa.com/ar/appcomponent--best-sales/?page={x}')
    soup = BeautifulSoup(r.content,'lxml')

    productlist = soup.find_all('div' , class_='product-container bg-white rounded-lg')



    for item in productlist:
        for link in item.find_all('a',href= True):
            productlink.append(page + link ['href'])

    # testlink = 'https://niceonesa.com/ar/gifts/travel-size/ola-hair-mini-straightener-brush-n-215-n16250/'
    for link in productlink:
        r = requests.get(link , headers=headers)
        soup = BeautifulSoup(r.content,'lxml')

        try:
            title  =soup.find('h1',class_='title').text.strip()
            titles.append(title)
            print(title)


        except:
            title='non'




        try:
            price = soup.find('h3',class_='preReductionPrice mb-2').text.strip()
            prices.append(price)

        except:
            price = 'non'
        try:
            offer = soup.find('h3',class_='sellingPrice text-nowrap')
            offers.append(offer)
        except:
            offer='non'
        try:
            rate = soup.find('span',class_='num-rating align-review').text.strip()
            rates.append(rate)

        except:
            rate = 'non'
        try:
            rate_start =soup.find('div', class_='num-rating start').text.strip()
            rate_starts.append(rate_start)
        except:
            rate_start = 'non'

    brand = productlist.find_all('h3', class_='brand-product mb-1')
    for i in range(len(brand)):
        brands.append(brand[i].text)
        filelist = ([titles, brands, prices, rates, rate_starts, productlink])
        exported = zip_longest(*filelist)
        with open('oo.csv', 'w' , encoding ='utf-8-sig' , newline='') as filecsv:
            wr = csv.writer(filecsv)
            wr.writerow(['title','brands','price','offer','rate','rate_starts','productlink'])
            wr.writerows(exported)

```


Thank you 


I tried all possible solutions by searching on the Internet for the problem, but I did not find a way, and I could not understand the problem.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[BrokenBenchmark](https://stackoverflow.com/users/17769815)** (2023-01-10): Please add more details about the specific problem and the desired behavior.
- **[Frank Yellin](https://stackoverflow.com/users/6457407)** (2023-01-10): What exactly is the problem?  What are you expecting to see vs what are you actually seeing?
