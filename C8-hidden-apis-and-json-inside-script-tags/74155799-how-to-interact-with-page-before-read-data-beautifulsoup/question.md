---
title: "how to interact with page before read data beautifulsoup"
site: stackoverflow
question_id: 74155799
url: https://stackoverflow.com/q/74155799
asked: 2022-10-21T15:17:44Z
asked_by: "Ahmad Lahluob"
asked_by_url: https://stackoverflow.com/users/20302322
last_edited: never
tags: [python, asp.net, web-scraping, beautifulsoup]
score: -2
views_at_snapshot: 315
answer_count: 1
accepted_answer_id: 74201794
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2d97ca002f4542a84104aabc05f3ddc1d3169b6e63884cdc63e1b3afc9e49f4f
---

# how to interact with page before read data beautifulsoup

Asked by [Ahmad Lahluob](https://stackoverflow.com/users/20302322) on Stack Overflow, <https://stackoverflow.com/q/74155799>, 2022-10-21. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

i want to read table from aspx page , before that i want to change some dropdownlists values to show the exact table 

i tried 

the website 
```
http://webapp.ttu.edu.jo/corse_study/Default.aspx
```
```
from bs4 import BeautifulSoup
import requests

url = 'http://webapp.ttu.edu.jo/corse_study/Default.aspx'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
print(soup.select('select', {'id': 'd_deg'}))
print(soup.select('select', {'id': 'd_coll'}))
print(soup.select('select', {'id': 'd_dept'}))
print(soup.select('table', {'id': 'GridView1'}))
````
and it did not work

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Robert](https://stackoverflow.com/users/1431720)** (2022-10-21): https://idownvotedbecau.se/itsnotworking/
- **me** (2022-10-22): when you say "it did not work" what do you mean? that nothing printed? what were you expecting to see here?
- **me** (2022-10-22): Also, from the arguments you're passing, I think you actually meant to use `find` (or `find_all` if you want a list) -  the correct way to use [`select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) (or `select_one` when you *don't* want a list) is to pass a [css selector](https://www.w3schools.com/cssref/css_selectors.asp) as argument - like `soup.select('select#d_deg')`
