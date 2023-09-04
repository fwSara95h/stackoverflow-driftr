---
title: "How to Extract Content Inside Each <a href> Tag?"
site: stackoverflow
question_id: 77011194
answer_id: 77034640
url: https://stackoverflow.com/a/77034640
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-09-04T00:59:31Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/77034640/revisions
accepted: true
score: 0
chapter: C3
chapter_title: "Links, attributes, images and downloads"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8ad9a1c2c27469465cf920f0347fa4c776ecb8998aa5258090df9ae68e543da2
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-09-04

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/77034640>, 2023-09-04; **accepted**; score 0. Text as retrieved 2026-10-12.

You could request the page from each link and get the first line of the summary; something like:

```py
rootUrl = 'https://docs.derivative.ca'
req = requests.get(rootUrl+'/Category:CHOPs')
req.raise_for_status() # in case of error

## getting the links
soup = BeautifulSoup(req.content, 'html.parser')
groups = soup.select('div.mw-category-group:has(h3~ul)')
chops = [{
    'group': g.h3.get_text(strip=True),
    'category': a.get_text(strip=True),
    'link': rootUrl + a['href']
} for g in groups for a in g.select('li>a[href]')]

cLen = len(chops)
print('found', cLen, 'categories with links')

## getting the descriptions
for i, c in enumerate(chops):
    # print(f'scraping {i+1} of {cLen}: {repr(c["category"])} from {c["link"]}')
    cReq = requests.get(c['link'])
    try: cReq.raise_for_status()
    except: continue
    cSoup = BeautifulSoup(cReq.content, 'html.parser')

    summary_p1 = cSoup.select_one('h2:has(span#Summary)~p')
    if summary_p1: chops[i]['description'] = summary_p1.get_text(strip=True)
```

[![opdf][1]][1]


  [1]: https://i.sstatic.net/yk5fc.png
