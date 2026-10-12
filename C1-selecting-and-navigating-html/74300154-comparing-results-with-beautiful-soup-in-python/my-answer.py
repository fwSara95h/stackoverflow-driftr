# Code from my Stack Overflow answer https://stackoverflow.com/a/74333464 (posted 2022-11-06), extracted verbatim; may need the question's context to run.

# --- block 1 ---
from datetime import date
import dateutil.parser 

def get_days_til_closing(lSoup):
    cTxt = lSoup.previous_sibling.find('div', {'tmid':'closingtime'}).text
    cTime = dateutil.parser.parse(cTxt.replace('Closes:', '').strip())
    return (cTime.date() - date.today()).days

# --- block 2 ---
min_dtc = 3 # or as preferred

# your current code upto listings = soup.findAll....

new_listings = [l for l in listings if get_days_til_closing(l) > min_dtc]
print(len(new_listings), f'new listings [of {len(listings)}]')

for listing in new_listings: print(listing.text)

# --- block 3 ---
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

# --- block 4 ---
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
