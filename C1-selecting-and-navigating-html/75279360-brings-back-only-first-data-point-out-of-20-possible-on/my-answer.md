---
title: "Brings back only first data point out of 20 possible on page(BeautifulSoup Scraping)"
site: stackoverflow
question_id: 75279360
answer_id: 75283560
url: https://stackoverflow.com/a/75283560
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-30T11:08:27Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75283560/revisions
accepted: false
score: 1
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c54a59d63c12febbd140060abf059bd9873e36ba7a084eeafc6837a152c45140
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-30

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75283560>, 2023-01-30; score 1. Text as retrieved 2026-10-12.

The class `jsx-1526930885` seems to be specific to an agent - so you will probably not find anyone else's listings with it. You could try targeting the `data-testid` attribute instead.

```python
    container = soup.find_all('div', {'data-testid': 'component-agentCard'})
```

And you should remove that class inside the `for` loop as well - just go with `con.find('div', {'class': 'agent-name'})` and `con.find('div', {'class': 'agent-phone'})` instead.

For **example**:

```python
for con in soup.find_all('div', {'data-testid': 'component-agentCard'}):
    print({kk: t.get_text(' ').strip() if t else None for kk, t in [
        (k ,con.find('div', {'class':f'agent-{k}'})) for k in ['name', 'phone']
    ]})
```

prints

> ```python
> {'name': 'Christopher Marti', 'phone': '(830) 660-1004'}
> {'name': 'Matthew Guzman', 'phone': '(281) 650-0533'}
> {'name': 'Adam Olsen', 'phone': '(936) 689-9123'}
> {'name': 'Cyndi Kornegay', 'phone': '(713) 952-6767'}
> {'name': 'The Gayden Team Team', 'phone': '(832) 692-2000'}
> {'name': 'Christy Buck', 'phone': '(832) 264-8934'}
> {'name': 'Tammy Fruge', 'phone': '(281) 709-5124'}
> {'name': 'Todd Spencer', 'phone': '(512) 665-3747'}
> {'name': 'JOHN PRELL, Broker', 'phone': '(214) 696-4663'}
> {'name': 'Rene Sorola', 'phone': '(832) 816-4673'}
> {'name': 'Wendy Cline Team', 'phone': '(281) 858-3451'}
> {'name': 'Andrea Kitzmann', 'phone': '(979) 217-1722'}
> {'name': 'Tammie Bell', 'phone': '(979) 292-6163'}
> {'name': 'Mike Seder', 'phone': '(713) 806-6796'}
> {'name': 'Scott Laird Team', 'phone': '(281) 339-1800'}
> {'name': 'Cari Goeke Team', 'phone': '(979) 530-2714'}
> {'name': 'Travis Edmunds', 'phone': '(281) 363-2500'}
> {'name': 'Libby Mitchell Team', 'phone': '(409) 718-1933'}
> {'name': 'Robbie Jansky', 'phone': '(361) 293-8759'}
> {'name': 'Ronnie Matthews Team', 'phone': '(281) 440-7900'}
> ```

for [/pg-1](https://www.realtor.com/realestateagents/houston_tx/photo-1/sort-activelistings/pg-1).


  [1]: https://i.sstatic.net/S6Ydx.png
