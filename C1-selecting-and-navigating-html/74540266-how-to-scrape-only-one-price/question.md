---
title: "How to scrape only one price?"
site: stackoverflow
question_id: 74540266
url: https://stackoverflow.com/q/74540266
asked: 2022-11-22T23:48:52Z
asked_by: "MATIAS IGNACIO OLIVA ALCAYAGA"
asked_by_url: https://stackoverflow.com/users/20334107
last_edited: never
tags: [python, beautifulsoup, jupyter-notebook]
score: -1
views_at_snapshot: 54
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5650ac199fe1f677b532d8381acc27acac3b431414dd1202a422dc62d93947f4
---

# How to scrape only one price?

Asked by [MATIAS IGNACIO OLIVA ALCAYAGA](https://stackoverflow.com/users/20334107) on Stack Overflow, <https://stackoverflow.com/q/74540266>, 2022-11-22. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to scrape product prices from a website and both real price and the monthly payment quota value has exactly the same class, so I can't figure it out how to only get main price.

[![Page description](https://i.sstatic.net/WBsAT.png)](https://i.sstatic.net/WBsAT.png)

and this is for the main price: "<span class="price-tag-fraction">879.990</span>"
this is for the monthly payment quota: "<span class="price-tag-fraction">39.990</span>",

this is the URL: https://listado.mercadolibre.cl/macbook#D[A:macbook]


```
#THIS GETS ALL THE NAMES AND STORES IT IN A LIST

prod = soup.find_all('h2', class_ ='ui-search-item__title shops__item-title') 

productos = list()
count=0
for i in prod:
    if count < 33:
        productos.append(i.text)
    else:
        break
        count +=1
size= len(productos) +1
#print(size)
#print(productos, len(productos))
print(productos)

#THIS GETS ALL THE NAMES AND STORES IT IN A LIST

pri = soup.find_all('span',class_ ="price-tag-fraction")
precios = list()
count=0
for i in pri:
    if count < 33:
        precios.append(i.text)
     
    else:
        break
        count +=1
#rint(precios)
prices= [item.split(',')for item in precios]
```

Here is the output
[![output](https://i.sstatic.net/jBWI9.png)](https://i.sstatic.net/jBWI9.png)

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[TomServo](https://stackoverflow.com/users/5741073)** (2022-11-23): Hard to believe they're the exact same class, since they are quite different in appearance.
- **[MATIAS IGNACIO OLIVA ALCAYAGA](https://stackoverflow.com/users/20334107)** (2022-11-23): right but both prices has the same class wich is 'span',class_ ="price-tag-fraction"
