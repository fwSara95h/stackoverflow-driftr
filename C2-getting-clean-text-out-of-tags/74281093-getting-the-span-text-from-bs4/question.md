---
title: "getting the span text from bs4"
site: stackoverflow
question_id: 74281093
url: https://stackoverflow.com/q/74281093
asked: 2022-11-01T19:47:54Z
asked_by: "Paul Corcoran"
asked_by_url: https://stackoverflow.com/users/18776287
last_edited: never
tags: [python, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 89
answer_count: 2
accepted_answer_id: 74281266
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: adcce0e53f31d773b9ff5905152e0bfb4f1426bc1bd75b486b3302838dd45ae3
---

# getting the span text from bs4

Asked by [Paul Corcoran](https://stackoverflow.com/users/18776287) on Stack Overflow, <https://stackoverflow.com/q/74281093>, 2022-11-01. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a number of text items contained in span tags that i need to extract.
I am able to do this in a list comp in the class table-main__odds as shown. I need to get the same info fronm the table-main__odds coloured tag. The logic below does not return any values. any help is appreciated?

    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    
    url = 'https://www.betexplorer.com/soccer/england/premier-league/results/'
    soup = BeautifulSoup(requests.get(url).content)
    odds_raw = soup.find_all("td", class_="table-main__odds")
    fav_odds_raw = soup.find_all("td",class_="table-main__odds colored")
    
    
    odds = [o.get('data-odd') for o in odds_raw]

[![enter image description here][1]][1]


the desired result is a list with the values contained here in data-odd

[![enter image description here][2]][2]


  [1]: https://i.sstatic.net/OWgYm.png
  [2]: https://i.sstatic.net/5JpkF.png

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Dmitriy Neledva](https://stackoverflow.com/users/16786350)** (2022-11-01): there is `data-oid` but not `data-odd`, isn't there?
- **[Dmitriy Neledva](https://stackoverflow.com/users/16786350)** (2022-11-01): this line `fav_odds_raw = soup.find_all("td",class_="table-main__odds colored")` won't be working because there should be no wight spaces within class name
- **[Paul Corcoran](https://stackoverflow.com/users/18776287)** (2022-11-01): the list comp for data-oid returns the hashid. for some reason the data-odd is not captured like in odds_raw
- **[Dmitriy Neledva](https://stackoverflow.com/users/16786350)** (2022-11-01): instead of this `odds = [o.get('data-odd') for o in odds_raw]` try this `odds = [o.get('data-oid') for o in odds_raw]`
- **[Paul Corcoran](https://stackoverflow.com/users/18776287)** (2022-11-01): yeah you see its the text value in contained in data-odd that is the taget not the hashid
- **[Paul Corcoran](https://stackoverflow.com/users/18776287)** (2022-11-01): so for this its the fav_odds_raw that i cant get data-odd for
- **[Dmitriy Neledva](https://stackoverflow.com/users/16786350)** (2022-11-01): Let us [continue this discussion in chat](https://chat.stackoverflow.com/rooms/249230/discussion-between-dmitriy-neledva-and-paul-corcoran).
