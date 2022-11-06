---
title: "Comparing results with Beautiful Soup in Python"
site: stackoverflow
question_id: 74300154
answer_id: 74333464
url: https://stackoverflow.com/a/74333464
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-06T05:21:39Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74333464/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e29cc2143aad3e54ecef3808203c2adad3516d007eecdc8991b43371dad678f0
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-06

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74333464>, 2022-11-06; score 0. Text as retrieved 2026-10-12.

With length-comparison, there is the issue of some results being removed between checks, so it might *look* like there are no new results even if there are; and text-comparison does not account for results with similar titles.

I can suggest 3 other methods. (The 3rd uses my preferred approach.)

<hr>

1. **Closing time**

A comment suggested using the closing time, which can be found [in the tag before the title][1]; you can define a function to get the days until closing 
```python
from datetime import date
import dateutil.parser 

def get_days_til_closing(lSoup):
    cTxt = lSoup.previous_sibling.find('div', {'tmid':'closingtime'}).text
    cTime = dateutil.parser.parse(cTxt.replace('Closes:', '').strip())
    return (cTime.date() - date.today()).days
```
and then filter by the returned value
```python
min_dtc = 3 # or as preferred

# your current code upto listings = soup.findAll....

new_listings = [l for l in listings if get_days_til_closing(l) > min_dtc]
print(len(new_listings), f'new listings [of {len(listings)}]')

for listing in new_listings: print(listing.text)
```
However, I don't know if sellers are allowed to set their own closing times or if they're set at a fixed offset; also, I don't see the closing time text when inspecting with the browser dev tools [even though I could extract it with the code above], and that makes me a bit unsure of whether it's always available.

<hr>

2. **JSON list of Listing IDs**

Each result is in a "card" with a link to the relevant listing, and that link contains a number that I'm calling the "listing ID". You can save that in a list as a JSON file and keep checking against it every new scrape
```python
from bs4 import BeautifulSoup
import requests
import json

lFilename = 'listing_ids.json' # or as preferred
url = requests.get("https://www.trademe.co.nz/a/marketplace/music-instruments/instruments/guitar-bass/electric-guitars/search?search_string=prs&condition=used")

try:
    prev_listings = json.load(open(lFilename, 'r'))
except Exception as e:
    prev_listings = []
print(len(prev_listings), 'saved listings found')

soup = BeautifulSoup(url.text, "html.parser")
listings = soup.select("div.o-card > a[href*='/listing/']")
new_listings = [
    l for l in listings if 
    l.get('href').split('/listing/')[1].split('?')[0] 
    not in prev_listings
]
print(len(new_listings), f'new listings [of {len(listings)}]')

for listing in new_listings:
    print(listing.select_one('div.tm-marketplace-search-card__title').text)

with open(lFilename, 'w') as f: 
    json.dump(prev_listings + [
        l.get('href').split('/listing/')[1].split('?')[0] 
        for l in new_listings
    ], f)
```
This should be fairly reliable as long as they don't tend to recycle the listing ids, this should be fairly reliable. (Even then, every once in a while, after checking the new listings for that day, you can just delete the JSON file and re-run the program once; it will also keep the file from getting too big...)

<hr>

3. **CSV Logging [including Listing IDs]**

Instead of just saving the IDs, you can save pretty much all the details from each result
```python
from bs4 import BeautifulSoup
import requests
from datetime import date
import pandas

lFilename = 'listings.csv' # or as preferred
max_days = 60 # or as preferred
date_today = date.today()
url = requests.get("https://www.trademe.co.nz/a/marketplace/music-instruments/instruments/guitar-bass/electric-guitars/search?search_string=prs&condition=used")

try:
    prev_listings = pandas.read_csv(lFilename).to_dict(orient='records')
    prevIds = [str(l['listing_id']) for l in prev_listings]
except Exception as e:
    prev_listings, prevIds = [], []
print(len(prev_listings), 'saved listings found')

def get_listing_details(lSoup, prevList, lDate=date_today):
    selectorsRef = {
        'title': 'div.tm-marketplace-search-card__title',
        'location_time': 'div.tm-marketplace-search-card__location-and-time',
        'footer': 'div.tm-marketplace-search-card__footer',
    }
    
    lId = lSoup.get('href').split('/listing/')[1].split('?')[0]
    lDets = {'listing_id': lId}

    for k, sel in selectorsRef.items(): 
        s = lSoup.select_one(sel)
        lDets[k] = None if s is None else s.text

    lDets['listing_link'] = 'https://www.trademe.co.nz/a/' + lSoup.get('href')
    lDets['new_listing'] = lId not in prevList
    lDets['last_scraped'] = lDate.isoformat()

    return lDets

soup = BeautifulSoup(url.text, "html.parser")

listings = [
    get_listing_details(s, prevIds) for s in
    soup.select("div.o-card > a[href*='/listing/']")
]
todaysIds = [l['listing_id'] for l in listings]
new_listings = [l for l in listings if l['new_listing']]
print(len(new_listings), f'new listings [of {len(listings)}]')

for listing in new_listings: print(listing['title'])

prev_listings = [
    p for p in prev_listings if str(p['listing_id']) not in todaysIds
    and (date_today - date.fromisoformat(p['last_scraped'])).days < max_days
]
pandas.DataFrame(prev_listings + listings).to_csv(lFilename, index=False)
```
You'll end up with a [spreadsheet of scraping history/log][2] that you can check anytime, and depending on what you set `max_days` to, the oldest data will be automatically cleared.


  [1]: https://i.sstatic.net/iGn6W.png
  [2]: https://i.sstatic.net/lftlh.png
