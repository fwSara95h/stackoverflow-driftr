---
title: "How to find the total number of pages on a website with BeautifulSoup?"
site: stackoverflow
question_id: 73977709
answer_id: 73982156
url: https://stackoverflow.com/a/73982156
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-07T03:47:19Z
last_edited: 2022-10-07T08:18:41Z
revisions: 2
revision_history: https://stackoverflow.com/posts/73982156/revisions
accepted: false
score: 1
chapter: C6
chapter_title: "Pagination and crawling"
cluster: scrape-pagination-crawling
helpers_referenced: [getPageTotal]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: dec4ff4ee7118b5d97cb5c4083cbaae40fca28297787b37c2490ec6bb55a4392
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-07

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73982156>, 2022-10-07, last edited 2022-10-07; score 1. Text as retrieved 2026-10-12.

There's a bit at the top that says *"Showing the 217 results as per selected criteria"*. You can code to extract the number from that, then count the number number of results per page and divide by that to get the expected number of pages (don't forget to round *up* ). 

If you want to double check, add more code to go to the calculated last page and 

 - if there's no such page, keep decrementing the total and checking until you hit a page that exists
 - if there *is* such a page, but it has an active/enabled "Next" button, keep going to Next page until reaching the last (basically as you are now)

(Remember that the two listed above are *contingencies* and wouldn't be executed in an ideal scenario.)

So, just to find the number of pages, you could do something like:

```python
import requests
from bs4 import BeautifulSoup
import math

def soupFromUrl(scrapeUrl):
  req = requests.get(scrapeUrl)
  if req.status_code == 200:
    return BeautifulSoup(req.text, 'html.parser')
  else:
    raise Exception(f'{req.reason} - failed to scrape {scrapeUrl}')


def getPageTotal(url):
  soup = soupFromUrl(url)

  #totalResults = int(soup.find('label').get_text().split('(')[-1].split(')')[0])  
  totalResults = int(soup.p.strong.get_text()) # both searches should work
  perPageResults = len(soup.select('.m-show')) #probably always 20

  print(f'{perPageResults} of {totalResults} results per page') 
  if not (perPageResults > 0 and totalResults > 0):
    return 0 
  
  lastPageNum = math.ceil(totalResults/perPageResults)

  # Contingencies - will hopefully never be needed
  lpSoup = soupFromUrl(f'{url}?page={lastPageNum}')
  if lpSoup.select('.m-show'): #page exists
    while lpSoup.select_one('a[rel="next"]'):
      nextLink = lpSoup.select_one('a[rel="next"]')['href']
      lastPageNum = int(nextLink.split('page=')[-1])
      lpSoup = soupFromUrl(nextLink)
  else: #page does not exist
    while not (lpSoup.select('.m-show') or lastPageNum < 1): 
      lastPageNum = lastPageNum - 1
      lpSoup = soupFromUrl(f'{url}?page={lastPageNum}')
  # end Contingencies section
  
  return lastPageNum
```

However, it looks like you only want the total pages in order to start the for-loop, but it's not even necessary to use a for-loop at all - a while-loop might be better:

```python
def data_fetch(url):
  school_info = []  
  nextUrl = url
  while nextUrl:
    soup = soupFromUrl(nextUrl)

    #GET YOUR DATA FROM PAGE

    nextHL = soup.select_one('a[rel="next"]')
    nextUrl = nextHL.get('href') if nextHL else None 
  
  # code after fetching all pages' data
```

Although, you *could* still use for-loop if you had a maximum page number in mind:

```python
def data_fetch(url, maxPages):
  school_info = []  

  for p in range(1, maxPages+1):
    soup = soupFromUrl(f'{url}?page={p}')
    if not soup.select('.m-show'):
      break

    #GET YOUR DATA FROM PAGE 
  
  # code after fetching all pages' data [upto max]
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[theycallmepix](https://stackoverflow.com/users/12320089)** (2022-10-07): I never thought of that while loop thing! It's really good IMO, like scrape the present page, go to next page, just like we do in real life.. However, I do believe that  scraping from _"Showing the 217 results as per selected criteria"_ might not be feasible as the website looks damn too old and the results are pretty in accurate.
