---
title: "Comparing results with Beautiful Soup in Python"
site: stackoverflow
question_id: 74300154
url: https://stackoverflow.com/q/74300154
asked: 2022-11-03T08:39:59Z
asked_by: "Spykerwolf"
asked_by_url: https://stackoverflow.com/users/7770930
last_edited: 2022-11-03T08:42:46Z
tags: [python, list, web-scraping, beautifulsoup, comparison]
score: -2
views_at_snapshot: 271
answer_count: 2
accepted_answer_id: 74339445
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9b0fc2b4f5970649619cca97655968d15d0d6e1e764b5c5a428a186fdd8f24a8
---

# Comparing results with Beautiful Soup in Python

Asked by [Spykerwolf](https://stackoverflow.com/users/7770930) on Stack Overflow, <https://stackoverflow.com/q/74300154>, 2022-11-03, last edited 2022-11-03. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I've got the following code that filters a particular search on an auction site.
I can display the titles of each value & also the len of all returned values:

```
from bs4 import BeautifulSoup
import requests


url = requests.get("https://www.trademe.co.nz/a/marketplace/music-instruments/instruments/guitar-bass/electric-guitars/search?search_string=prs&condition=used")
soup = BeautifulSoup(url.text, "html.parser")
listings = soup.findAll("div", attrs={"class":"tm-marketplace-search-card__title"})
print(len(listings))

for listing in listings:
    print(listing.text)
```

This prints out the following:
```
#print(len(listings))
3 

#for listing in listings:
#    print(listing.text)

 PRS. Ten Top Custom 24, faded Denim, Piezo. 
 PRS SE CUSTOM 22 
 PRS Tremonti SE *With Seymour Duncan Pickups* 
```
I know what I want to do next, but don't know how to code it. Basically I want to only display new results. I was thinking storing the len of the listings (3 at the moment) as a variable & then comparing that with another GET request (2nd variable) that maybe runs first thing in the morning. Alternatively compare both text values instead of the len. If it doesn't match, then it shows the new listings. Is there a better or different way to do this? Any help appreciated thank you

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[The Myth](https://stackoverflow.com/users/15042008)** (2022-11-03): Try finding the time when the product closes. I surfed through the website and found that the newest products close the latest. The first one closes on `Thu, 10 Nov`. Fetch that value and use `datetime` to compare dates.
