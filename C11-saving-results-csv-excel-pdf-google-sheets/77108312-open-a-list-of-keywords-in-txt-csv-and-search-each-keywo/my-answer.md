---
title: "Open a list of keywords in txt/csv and search each keyword on Google"
site: stackoverflow
question_id: 77108312
answer_id: 77109059
url: https://stackoverflow.com/a/77109059
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-09-15T00:44:09Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/77109059/revisions
accepted: false
score: 2
chapter: C11
chapter_title: "Saving results: CSV, Excel, PDF, Google Sheets"
cluster: scrape-to-files-tables
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bfaac773034a879396729b6cd3be52465d0ca59c31483c2e641f0c600cee3bc4
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-09-15

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/77109059>, 2023-09-15; score 2. Text as retrieved 2026-10-12.

Here's an edited version of the code from your q, which scrapes for a list of keywords:

```py
search_list = ['weather', 'home depot', 'USPS Tracking'] ## FOR EXAMPLE
url = 'https://www.google.com/search'

headers = {
    'Accept' : '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
}

results_list = []
for search in search_list:
    parameters = {'q': search}

    page = requests.get(url, headers = headers, params = parameters)
    try: page.raise_for_status()
    except Exception as e: 
        results_list.append({'keyword': search, 'error': repr(e)})
        continue
    soup = BeautifulSoup(page.content, 'html.parser')

    first_link = soup.select_one('#search a[href]:has(h3)')
    results_list.append({
        'keyword': search, 
        'first result': first_link.h3.get_text(' ', strip=True),
        'first link': first_link['href']
    })

    print(*[f'{k}: {v}' for k, v in results_list[-1].items()], '-'*80, sep='\n')
```

prints [![op1][1]][1]


  [1]: https://i.sstatic.net/uEDC5.png
