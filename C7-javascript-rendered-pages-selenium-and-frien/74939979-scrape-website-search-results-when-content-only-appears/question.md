---
title: "Scrape website search results when content only appears after clicking 'search' (Python - Beautiful soup)"
site: stackoverflow
question_id: 74939979
url: https://stackoverflow.com/q/74939979
asked: 2022-12-28T11:57:06Z
asked_by: "zach dickson"
asked_by_url: https://stackoverflow.com/users/15538310
last_edited: 2022-12-28T11:59:40Z
tags: [python, web-scraping, beautifulsoup, request]
score: 0
views_at_snapshot: 670
answer_count: 1
accepted_answer_id: 74947523
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fa3141deeb334dd31e4a6045ea327611944afb438cf6cfc84f281f52367f6899
---

# Scrape website search results when content only appears after clicking 'search' (Python - Beautiful soup)

Asked by [zach dickson](https://stackoverflow.com/users/15538310) on Stack Overflow, <https://stackoverflow.com/q/74939979>, 2022-12-28, last edited 2022-12-28. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to scrape the press releases of a Danish political party (https://danskfolkeparti.dk/nyheder/) but the content of the press releases only appears after clicking 'search' within a web browser. There is no navigable html (that I can find) that allows for identifying a unique URL for the 'search' function, and the website URL does not change after clicking search within a browser. 




```
import pandas as pd
import requests
from bs4 import BeautifulSoup
url = 'http://danskfolkeparti.dk/nyheder.html'
headers = {'User-Agent': 'Mozilla/5.0'}
soup = BeautifulSoup(requests.get(url=url, headers=headers).content, 'html.parser')


### the data I'm looking for would usually be accessible using something like the following. 
### However, the HTML does not appear until AFTER the search is clicked within a browser 
soup.find_all("div", class_='timeline')

```


printing 'soup' shows the HTML without the content that's desired. The search button in the website (Søg, in Danish) is not accessible as an endpoint. After clicking the search button (<Søg>) in a web browser, the desired content appears in a web browser and is viewable by 'inspecting' the page, but the URL does not change so there's not a clear way to access the page with Beautiful soup. 

The desired content is the title, url and date of each individual press release. For example, the first press release that appears when searching with default settings is the following: 

title: Året 2022 viste hvad Dansk Folkeparti er gjort af

date: 23/12/2022

url: https://danskfolkeparti.dk/nyheder/mortens-nyhedsbrev/aaret-2022-viste-hvad-dansk-folkeparti-er-gjort-af/

Any help with this would be greatly appreciated!!

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Sergey K](https://stackoverflow.com/users/6593287)** (2022-12-28): site have Cloudflare protection, so u cant get result without setting up cookies
