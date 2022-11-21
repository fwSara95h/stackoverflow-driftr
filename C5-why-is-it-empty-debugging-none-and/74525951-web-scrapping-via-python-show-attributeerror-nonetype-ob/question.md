---
title: "Web Scrapping via python show AttributeError: 'NoneType' object has no attribute 'full_text'"
site: stackoverflow
question_id: 74525951
url: https://stackoverflow.com/q/74525951
asked: 2022-11-21T23:35:10Z
asked_by: "pengoul"
asked_by_url: https://stackoverflow.com/users/20497095
last_edited: 2022-11-24T23:29:18Z
tags: [python, image, web-scraping, woocommerce]
score: 0
views_at_snapshot: 92
answer_count: 1
accepted_answer_id: 74571807
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a103ad6feb4c7de252a54da9b4f6d6d8d39276923935e77d9203cf0f33333180
---

# Web Scrapping via python show AttributeError: 'NoneType' object has no attribute 'full_text'

Asked by [pengoul](https://stackoverflow.com/users/20497095) on Stack Overflow, <https://stackoverflow.com/q/74525951>, 2022-11-21, last edited 2022-11-24. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Scrap the data from the website by using python.
```

from requests_html import HTMLSession
import http.client
http.client._MAXHEADERS = 1000
url='https://agedcarestore.com.au/product-category/physio-products/arthritis/'

s=HTMLSession()
r=s.get(url)
print(r.html.find('#header'))

items=r.html.find('div.product-small.box')
print(items)

def get_links(url):
    r=s.get(url)
    items=r.html.find('div.product-small.box')
    links=[]
    for item in items:
        links.append(item.find('a',first=True).attrs['href'])
        
    return links
print(get_links(url))
def get_product(link):
    r=s.get(link)
    
    title=r.html.find('h1',first=True).full_text
    price=r.html.find('span.woocommerce-Price-amount.amount bdi')[1].full_text
    sku=r.html.find('nav.ruk_rating_snippet data-sku',first=True).full_text
    tag = r.html.find('a[rel=tag]', first=True).full_text
    sku = r.html.find('span.sku', first=True).full_text

    product = {
        'title': title.strip(),
        'price': price.strip(),
        'tag': tag.strip(),
        'sku': sku.strip()
    }
    print(product)
    return product 

results = []
links = get_links(url)

for link in links:
    results.append(get_product(link))
    time.sleep(1)

with open('version1.csv', 'w', encoding='utf8', newline='') as f:
    fc = csv.DictWriter(f, fieldnames=results[0].keys(),)
    fc.writeheader()
```

```
```

I want extract the data from the website which built on woocommerce, but my python code showed the error: AttributeError: 'NoneType' object has no attribute 'full_text'

how to solve it?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[tdelaney](https://stackoverflow.com/users/642070)** (2022-11-21): Please post the full traceback message so we can see the exact error. But generally, what if one of these things you are searching for, doesn't exist? This is the error that you'd expect. So, what do you want to do in that case? It may be reasonable to catch that error, post a message and exit.
- **[John Gordon](https://stackoverflow.com/users/494134)** (2022-11-21): `.find()` did not find the target text, so it returned None, so you ended up trying to access the `.full_text` attribute of a None object.
- **[Barry the Platipus](https://stackoverflow.com/users/19475185)** (2022-11-22): Can you  confirm the real url of the page?
- **[Khaled DELLAL](https://stackoverflow.com/users/15852600)** (2022-11-23): Please edit your question write a clear title
- **[pengoul](https://stackoverflow.com/users/20497095)** (2022-11-24): I have updated the question with the clear title.
