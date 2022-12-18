---
title: "Finding IDs in BeautifulSoup tag output"
site: stackoverflow
question_id: 74830177
answer_id: 74838470
url: https://stackoverflow.com/a/74838470
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-18T00:53:43Z
last_edited: 2022-12-28T21:08:40Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74838470/revisions
accepted: false
score: 0
chapter: C6
chapter_title: "Pagination and crawling"
cluster: scrape-pagination-crawling
helpers_referenced: [deepParseJson]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a224a59d9783247a422628176939eb000fb654be80fb285c4c3d6a51ab070c9a
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-18

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74838470>, 2022-12-18, last edited 2022-12-28; score 0. Text as retrieved 2026-10-12.

If you want a non-selenium solution, this would have been my suggestion:

If `results` [looks like this](https://i.sstatic.net/MpkX6.png) for you, then you need to parse the [JSON](https://www.w3schools.com/python/python_json.asp) in the `:results` attribute of the `iw-search` tag:

```python
import json
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.immoweb.be/en/search/apartment/for-sale/Antwerp/2000?countries=BE&page=1&orderBy=relevance&card=10286959"
page = requests.get(URL)
page.raise_for_status() # raise error if request fails

soup = BeautifulSoup(page.content, "html.parser")

resultsList = json.loads(soup.find('iw-search').get(':results'))
resultIds = [r['id'] for r in resultsList]
```

`resultIds` should return

```python
[10083851, 10147541, 9607277, 9614247, 10110818, 10286959, 10067819, 10186552, 10209440, 10135372, 10182817, 7412146, 9309581, 10176146, 10186729, 10157914, 10201488, 10267579, 10267583, 10276232, 10204059, 9802962, 10261577, 10128809, 10250713, 10149009, 10173283, 10285603, 9028052, 10224443]
```

---

If you want the all the attributes, you can use [this function](https://pastebin.com/y0TmGG8g) [simply *`deepParseJson(soup.find('iw-search').attrs)`*, or `deepParseJson(getattr(soup.find('iw-search'), 'attrs', None))` if you want to avoid raising any errors and just return `None` if `iw-search` can't be found], or try parsing all `attrs` values with

```python
# import json

iws_attrs = soup.find('iw-search').attrs
for k, v in iws_attrs.items():
    try: iws_attrs[k] = json.loads(v)
    except: pass
```

and then `iws_attrs` should return something like

```json
{
    ":criteria": {"countries": "BE", "postalCodes": [{"queryValue": "2000", "queryParam": "postalCodes", "slug": "Antwerp", "shortLabel": "Antwerp (2000)", "label": "Antwerp (2000)", "translations": {"fr": "Anvers", "en": "Antwerp", "nl": "Antwerpen"}}], "propertyTypes": "APARTMENT", "transactionTypes": "FOR_SALE", "trigger": "USER", "place": "CLASSIFIED_SEARCH_RESULT", "client": "WEB"}, 
    ":results": [
        {"id": 10083851, "cluster": {"minPrice": 425000, "maxPrice": 1795000, "minRoom": null, "maxRoom": null, "minSurface": 63, "maxSurface": 205, "projectInfo": {"constructor": null, "groupId": 10083851, "phase": null, "projectName": "Antwerp Tower", "deliveryDate": null, "soldPercentage": 41, "unitsDisplayMode": null}, "bedroomRange": "1 - 3", "surfaceRange": "63 - 205"}, "customerLogoUrl": "https://static.immoweb.be/logos/2184.gif?cache=2020381504833", "customerName": "Makelaarskantoor De Meester", "flags": {"main": null, "secondary": ["new_real_estate_project", "percent_sold"], "percentSold": 41}, "media": {"pictures": [{"smallUrl": "https://static.immoweb.be/photos/1/0/0/8/3/8/5/1/10083851_1.gif?cache=20220930053848", "mediumUrl": "https://static.immoweb.be/photos/1/0/0/8/3/8/5/1/M_10083851_1.jpg?cache=20220930053848", "largeUrl": "https://static.immoweb.be/photos/1/0/0/8/3/8/5/1/10083851_1.jpg?cache=20220930053848", "isVertical": false}, {"smallUrl": "https://static.immoweb.be/photos/1/0/0/8/3/8/5/1/10083851_2.gif?cache=20220930053348", "mediumUrl": "https://static.immoweb.be/photos/1/0/0/8/3/8/5/1/M_10083851_2.jpg?cache=20220930053348", "largeUrl": "https://static.immoweb.be/photos/1/0/0/8/3/8/5/1/10083851_2.jpg?cache=20220930053348", "isVertical": false}, {"smallUrl": "https://static.immoweb.be/photos/1/0/0/8/3/8/5/1/10083851_3.gif?cache=20220930053348", "mediumUrl": "https://static.immoweb.be/photos/1/0/0/8/3/8/5/1/M_10083851_3.jpg?cache=20220930053348", "largeUrl": "https://static.immoweb.be/photos/1/0/0/8/3/8/5/1/10083851_3.jpg?cache=20220930053348", "isVertical": false}]}, "property": {"type": "APARTMENT_GROUP", "subtype": "APARTMENT_GROUP", "title": "One of the iconic buildings that make up the Antwerp skyline", "bedroomCount": null, "location": {"country": "Belgium", "region": "Flanders", "province": "Antwerp", "district": "Antwerp", "locality": "Antwerp", "postalCode": "2018", "street": null, "number": null, "box": null, "propertyName": null, "floor": null, "latitude": null, "longitude": null, "distance": null, "approximated": null, "regionCode": "FLANDERS", "type": null, "hasSeaView": null, "pointsOfInterest": null, "placeName": null}, "netHabitableSurface": null, "landSurface": null, "roomCount": null}, "publication": {"publisherId": null, "visualisationOption": "XL", "size": "xl"}, "transaction": {"certificateLogoUrl": null, "certificate": null, "type": "FOR_SALE", "rental": null, "sale": {"lifeAnnuity": null, "hasStartingPrice": false, "oldPrice": null, "price": null, "pricePerSqm": null, "publicSale": null, "toBuild": null, "isSubjectToVat": null}}, "priceType": null, "price": {"type": "group_sale", "mainValue": null, "alternativeValue": null, "additionalValue": null, "oldValue": null, "minRangeValue": 425000, "maxRangeValue": 1795000, "mainDisplayPrice": "\u20ac425,000 - \u20ac1,795,000", "HTMLDisplayPrice": "<span aria-hidden=\"true\">\u20ac425,000 - \u20ac1,795,000</span>", "alternativeDisplayPrice": "", "oldDisplayPrice": null, "shortDisplayPrice": "\u20ac425K - 1.8M", "accessibilityPrice": "From 425000\u20ac To 1795000\u20ac", "label": "Min price - Max price", "date": null, "language": "en"}, "isBookmarked": false, "has360Tour": null, "hasVirtualTour": null, "advertisementId": null}, 
        {"id": 10147541, "cluster": {"minPrice": 695000, "maxPrice": 1195000, "minRoom": null, "maxRoom": null, "minSurface": 110, "maxSurface": 163, "projectInfo": {"constructor": null, "groupId": 10147541, "phase": null, "projectName": "Montevideo Residence", "deliveryDate": null, "soldPercentage": null, "unitsDisplayMode": null}, "bedroomRange": "2", "surfaceRange": "110 - 163"}, "customerLogoUrl": "https://static.immoweb.be/logos/3855276.gif?cache=2022271101293", "customerName": "DCA Woonprojecten", "flags": {"main": null, "secondary": ["new_real_estate_project"], "percentSold": null}, "media": {"pictures": [{"smallUrl": "https://static.immoweb.be/photos/1/0/1/4/7/5/4/1/10147541_1.gif?cache=20221114142454", "mediumUrl": "https://static.immoweb.be/photos/1/0/1/4/7/5/4/1/M_10147541_1.jpg?cache=20221114142454", "largeUrl": "https://static.immoweb.be/photos/1/0/1/4/7/5/4/1/10147541_1.jpg?cache=20221114142454", "isVertical": false}, {"smallUrl": "https://static.immoweb.be/photos/1/0/1/4/7/5/4/1/10147541_2.gif?cache=20221114142454", "mediumUrl": "https://static.immoweb.be/photos/1/0/1/4/7/5/4/1/M_10147541_2.jpg?cache=20221114142454", "largeUrl": "https://static.immoweb.be/photos/1/0/1/4/7/5/4/1/10147541_2.jpg?cache=20221114142454", "isVertical": false}, {"smallUrl": "https://static.immoweb.be/photos/1/0/1/4/7/5/4/1/10147541_3.gif?cache=20221114142454", "mediumUrl": "https://static.immoweb.be/photos/1/0/1/4/7/5/4/1/M_10147541_3.jpg?cache=20221114142454", "largeUrl": "https://static.immoweb.be/photos/1/0/1/4/7/5/4/1/10147541_3.jpg?cache=20221114142454", "isVertical": false}]}, "property": {"type": "APARTMENT_GROUP", "subtype": "APARTMENT_GROUP", "title": "A destination for many. A home for some.", "bedroomCount": null, "location": {"country": "Belgium", "region": "Flanders", "province": "Antwerp", "district": "Antwerp", "locality": "Antwerp", "postalCode": "2000", "street": "Limastraat", "number": null, "box": null, "propertyName": null, "floor": null, "latitude": 51.2344478, "longitude": 4.4043354, "distance": null, "approximated": null, "regionCode": "FLANDERS", "type": null, "hasSeaView": null, "pointsOfInterest": null, "placeName": null}, "netHabitableSurface": null, "landSurface": null, "roomCount": null}, "publication": {"publisherId": null, "visualisationOption": "XL", "size": "xl"}, "transaction": {"certificateLogoUrl": null, "certificate": null, "type": "FOR_SALE", "rental": null, "sale": {"lifeAnnuity": null, "hasStartingPrice": false, "oldPrice": null, "price": null, "pricePerSqm": null, "publicSale": null, "toBuild": null, "isSubjectToVat": null}}, "priceType": null, "price": {"type": "group_sale", "mainValue": null, "alternativeValue": null, "additionalValue": null, "oldValue": null, "minRangeValue": 695000, "maxRangeValue": 1195000, "mainDisplayPrice": "\u20ac695,000 - \u20ac1,195,000", "HTMLDisplayPrice": "<span aria-hidden=\"true\">\u20ac695,000 - \u20ac1,195,000</span>", "alternativeDisplayPrice": "", "oldDisplayPrice": null, "shortDisplayPrice": "\u20ac695K - 1.2M", "accessibilityPrice": "From 695000\u20ac To 1195000\u20ac", "label": "Min price - Max price", "date": null, "language": "en"}, "isBookmarked": false, "has360Tour": null, "hasVirtualTour": null, "advertisementId": null}, 
        {"id": 9607277, "cluster": {"minPrice": null, "maxPrice": null, "minRoom": null, "maxRoom": null, "minSurface": null, "maxSurface": null, "projectInfo": null, "bedroomRange": "", "surfaceRange": ""}, "customerLogoUrl": "https://static.immoweb.be/logos/1284223.gif?cache=2016051503403", "customerName": "Engel & V\u00f6lkers Antwerpen-Centrum", "flags": {"main": null, "secondary": [], "percentSold": null}, "media": {"pictures": [{"smallUrl": "https://static.immoweb.be/photos/0/9/6/0/7/2/7/7/9607277_1.gif?cache=20211108094138", "mediumUrl": "https://static.immoweb.be/photos/0/9/6/0/7/2/7/7/M_9607277_1.jpg?cache=20211108094138", "largeUrl": "https://static.immoweb.be/photos/0/9/6/0/7/2/7/7/9607277_1.jpg?cache=20211108094138", "isVertical": false}, {"smallUrl": "https://static.immoweb.be/photos/0/9/6/0/7/2/7/7/9607277_2.gif?cache=20211108094138", "mediumUrl": "https://static.immoweb.be/photos/0/9/6/0/7/2/7/7/M_9607277_2.jpg?cache=20211108094138", "largeUrl": "https://static.immoweb.be/photos/0/9/6/0/7/2/7/7/9607277_2.jpg?cache=20211108094138", "isVertical": false}, {"smallUrl": "https://static.immoweb.be/photos/0/9/6/0/7/2/7/7/9607277_3.gif?cache=20211108094138", "mediumUrl": "https://static.immoweb.be/photos/0/9/6/0/7/2/7/7/M_9607277_3.jpg?cache=20211108094138", "largeUrl": "https://static.immoweb.be/photos/0/9/6/0/7/2/7/7/9607277_3.jpg?cache=20211108094138", "isVertical": false}]}, "property": {"type": "APARTMENT", "subtype": "PENTHOUSE", "title": "Charming penthouse at Wilde Zee", "bedroomCount": 2, "location": {"country": "Belgium", "region": "Flanders", "province": "Antwerp", "district": "Antwerp", "locality": "Antwerpen", "postalCode": "2000", "street": "Lombardenvest", "number": "80", "box": "301", "propertyName": null, "floor": 4, "latitude": 51.2173467, "longitude": 4.4038566, "distance": null, "approximated": null, "regionCode": "FLANDERS", "type": null, "hasSeaView": null, "pointsOfInterest": null, "placeName": "Wilde Zee"}, "netHabitableSurface": 133, "landSurface": null, "roomCount": null}, "publication": {"publisherId": null, "visualisationOption": "XL", "size": "xl"}, "transaction": {"certificateLogoUrl": null, "certificate": null, "type": "FOR_SALE", "rental": null, "sale": {"lifeAnnuity": null, "hasStartingPrice": false, "oldPrice": null, "price": 565000, "pricePerSqm": null, "publicSale": null, "toBuild": null, "isSubjectToVat": null}}, "priceType": null, "price": {"type": "residential_sale", "mainValue": 565000, "alternativeValue": null, "additionalValue": null, "oldValue": null, "minRangeValue": null, "maxRangeValue": null, "mainDisplayPrice": "\u20ac565,000", "HTMLDisplayPrice": "<span aria-hidden=\"true\">\u20ac565,000</span>", "alternativeDisplayPrice": "", "oldDisplayPrice": null, "shortDisplayPrice": "\u20ac565K", "accessibilityPrice": "565000\u20ac", "label": "Price", "date": null, "language": "en"}, "isBookmarked": false, "has360Tour": null, "hasVirtualTour": null, "advertisementId": null}
    ], 
    ":results-storage": [
        {"id": 10083851, "property": {"type": "APARTMENT_GROUP", "subtype": "APARTMENT_GROUP", "location": {"locality": "Antwerp", "postalCode": "2018"}}, "transaction": {"type": "FOR_SALE"}}, 
        {"id": 10147541, "property": {"type": "APARTMENT_GROUP", "subtype": "APARTMENT_GROUP", "location": {"locality": "Antwerp", "postalCode": "2000"}}, "transaction": {"type": "FOR_SALE"}}, 
        {"id": 9607277, "property": {"type": "APARTMENT", "subtype": "PENTHOUSE", "location": {"locality": "Antwerpen", "postalCode": "2000"}}, "transaction": {"type": "FOR_SALE"}}
    ], 
    ":result-count": 519, 
    ":marketing-count": 519, 
    ":geo-point-count": 410, 
    ":page": 1, 
    "sort": "relevance", 
    "price-type": "", 
    ":unique-id": "661b253feeebbc4deea94a1d2483d9ad32e58b33", 
    ":labellized-search": "Apartment for sale - Antwerp (2000)", 
    ":meta-title": "Apartment for sale - antwerp (2000) - Immoweb", 
    ":meta-description": "Apartment for sale - antwerp (2000) - Immoweb", 
    ":anchor-card-id": 10286959, 
    ":is-popular-search": false, 
    ":has-premium-position": false
}
```

[ Lists truncated to 3 items or less - see full version as json [here](https://pastebin.com/hm2SUmRy). ]
