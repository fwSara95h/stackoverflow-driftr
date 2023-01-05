---
title: "Python Beautiful Soup scrape website giving forbidden error 403"
site: stackoverflow
question_id: 75009201
answer_id: 75013193
url: https://stackoverflow.com/a/75013193
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-05T02:07:01Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75013193/revisions
accepted: false
score: 1
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: [linkToSoup, linkToSoup_scrapingAnt, selectForList]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 19c8ae14b89a7689a95691dd615a2b7e5d5713482592ad43faefe823dba02730
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-05

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75013193>, 2023-01-05; score 1. Text as retrieved 2026-10-12.

Sometimes, blockers can be evaded with modules [cloudscraper](https://pypi.org/project/cloudscraper/) like, but these ones are too good. I tend to use [ScrapingAnt](https://scrapingant.com/) or [selenium](https://www.scrapingbee.com/blog/selenium-python/) when this happens - I have 2 functions ([`linkToSoup_scrapingAnt`](https://pastebin.com/5ibz2F6p) and [`linkToSoup_selenium`](https://pastebin.com/VLZ2vPYK)) which make it more convenient to use them with `BeautifulSoup`. You could make use of them in your code:

```python
### PASTE FOR linkToSoup_scrapingAnt FROM https://pastebin.com/5ibz2F6p 
### OR PASTE FOR linkToSoup_selenium FROM https://pastebin.com/VLZ2vPYK 

roorUrl = 'https://ae.indeed.com'
for current_page in range(1, 3):
        page_url = f'https://ae.indeed.com/jobs?q=&l=UAE&start={current_page}'
        print(page_url)

        # r = s.get(f'https://ae.indeed.com/jobs?q=&l=UAE&start={current_page}')  
        # soup = BeautifulSoup(r.text, 'html.parser')
        ## INSTEAD:

        # pgSoup = linkToSoup_scrapingAnt(page_url, isv=True, returnErr=False) # OR
        pgSoup = linkToSoup_selenium(page_url, isv=True, returnErr=False)
        if not pgSoup: continue

        links = [a.get('href') for a in pgSoup.select('a[id^="job_"][href]')]
        for link in links: 
             if link[:1] == '/': link = f'{roorUrl}{link}'
             # soup = linkToSoup_scrapingAnt(link, isv=True, returnErr=False) # OR
             soup = linkToSoup_selenium(link, isv=True, returnErr=False) 
             if not soup: continue

             ####### EXTRACT DATA #######
             # try...soup.select_one....text.strip()...except...
             # links_list.append(....) # print(f'done ....') # t.sleep(1)

# df = pd.DataFrame....df.to_csv....
```

Since it looks like you need to scrape quite a few pages, and ScrapingAnt only allows 1000 request a month (or even less, if you want to use their proxies) in the free tier, I'd recommend using selenium if you can.

---

Btw, if you're going to be using *`try...select...text`* repeatedly, you might also want to check out my [`selectForList`](https://pastebin.com/ZnZ7xM6u) function.
