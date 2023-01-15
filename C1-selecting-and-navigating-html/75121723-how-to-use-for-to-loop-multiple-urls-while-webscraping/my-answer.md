---
title: "How to use \"for\" to \"loop\" multiple urls while webscraping?"
site: stackoverflow
question_id: 75121723
answer_id: 75123779
url: https://stackoverflow.com/a/75123779
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-15T08:18:50Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75123779/revisions
accepted: true
score: -1
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d44893235818addc8b7eb03fdecc5b668c7169eb4288589a4a4d6c465e70484a
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-15

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75123779>, 2023-01-15; **accepted**; score -1. Text as retrieved 2026-10-12.

There are countless ways to do it; this is one example: parametrize `source_product_url` in `main` and call it in loop. (Add `return id_element` if you want to save the data for future use.)

```python
def get_sku(source_product_url):
 print("bdr.sandbox")
 generated_on = datetime.datetime.now()
 print(generated_on) 
 url_data = get_url_data_from_url_request(url=source_product_url)
 soup = BeautifulSoup(url_data, "lxml")
 id_element = soup.find('span', {"itemprop": "sku"}).text
 print(id_element)
 return id_element
```

You could just do `for url in urlsList: get_sku(url)` at this point, but if you want to  collect some data [and also make sure that, even if any errors are raised while scraping some of the pages, the program still attempts to scrape the rest], then you could do something like

```python
def try_get_sku(srcProdUrl):
 try: return {'source_product_url': srcProdUrl, 'sku': get_sku(srcProdUrl)}
 except Exception as e:
  errorMsg = f'{type(e)} {e}'
  print(f'failed to scrape {srcProdUrl} \n ', errorMsg)
  return {'source_product_url': srcProdUrl, 'errorMsg': errorMsg} 
```

( This also facilitates [list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp) )

```python 
def main():
 spUrls = [
  'https://www.6pm.com/p/easy-spirit-epic-gray/product/9450972/color/11',
  ## ADD ALL URLS TO SCRAPE ##
 ]
 productsInfo = [try_get_sku(spUrls) for url in spUrls]
 # do something with productsInfo if you want to, like
 # pandas.DataFrame(productsInfo).to_csv('productsInfo.csv') # saves in csv file [import pandas]
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[nesqluck](https://stackoverflow.com/users/21009472)** (2023-01-15): Thanks a lot , you the only one who understood my question and gave me the right answer. I really appreciate.
