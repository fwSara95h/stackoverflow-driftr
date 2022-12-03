---
title: "BeautifulSoup find a href in marquee"
site: stackoverflow
question_id: 74661666
answer_id: 74663126
url: https://stackoverflow.com/a/74663126
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-03T00:57:26Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74663126/revisions
accepted: true
score: 0
chapter: C3
chapter_title: "Links, attributes, images and downloads"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7688a284db836116726122c97ab4836b408196d3e3d1027380e2d4d0f3a16b83
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-03

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74663126>, 2022-12-03; **accepted**; score 0. Text as retrieved 2026-10-12.

> I can get the links easy peasy with selenium and chrome driver

Probably because the `div` with `h-48` class is loaded with JavaScript; even if it wasn't, I don't think `soup.find('div', class_='h-48')` would work because [that element has more classes](https://i.sstatic.net/707be.png), and you need to pass *all* of them as `class_` [and I don't think [`soup.select('div', class_='h-48')`](https://i.sstatic.net/gnIC2.png) gives the exact results you expect it to - [`select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) isn't really supposed to have a [`class_` argument](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class) - just a [CSS selector](https://www.w3schools.com/cssref/css_selectors.php) string]. 

<sub>**`soup.find('div', attrs={'class':'h-48'})`** or **`soup.select('div.h-48')`** can be expected to work on the html that is formed **after** JS loading, but you need selenium to get that...</sub>

---
---

Fortunately, I think the data you want is already in the fetched html, just [in a different format](https://i.sstatic.net/FiHOi.png) - you can extract a list of dictionaries (`mqCont`) with
```python
# import json

marq = soup.find('marquee', attrs={'class':'h-48'})
if marq is None: print('Could Not Find marquee.h-48')
if not marq.get(':contents'): print('marquee.h-48 has no [:contents] attr')

try: mqCont =  json.loads(marq.get(':contents', '[]'))
except Exception as e:
    mqCont = []
    print('failed to parse marquee.h-48[:contents] <---', e)
```
or, more shortly (if you're confident there won't be any error to debug/breakdown):
```python
mqCont = json.loads(soup.select_one('marquee.h-48').get(':contents', '[]'))
```

---

You can get a list of [links to news articles](https://i.sstatic.net/yb1bt.png) with **`[m['url'] for m in mqCont if 'url' in m]`**, but since you were trying to get `find` with `class_='flex p-2'`, you probably want the [`.../event_detail?id=...`](https://i.sstatic.net/1JyxR.png) links. You can form them as below
```python
evtUrls = [f"{url.strip('/')}/event_detail?id={m['id']}" for m in mqCont if 'id' in m]
```

---

You can also view the list of dictionaries as a table [with pandas] by doing something like:
```python
# import pandas

omitKeys = ['domain_event_types', 'country']
for i, m in enumerate(mqCont):
    mDesc = ' '.join(w for w in BeautifulSoup(
        m['description'] if 'description' in m else ''
    ).get_text().split() if w)
    if mDesc: m['description'] = mDesc
    if 'id' in m: m['eventUrl'] = f"{url.strip('/')}/event_detail?id={m['id']}"
    mqCont[i] = {k:v for k, v in m.items() if k not in omitKeys}

mqcDF = pandas.DataFrame(mqCont).dropna(axis='columns', how='all').set_index('id')
```
and the first 5 rows [of 100 rows total] of `mqcDF`:

|       id |   country_id | address                                    | event_gmt_time      | severity   | infrastructure   | tip_text                                                                             | url                                                                                                                                            | description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |   latitude |   longitude |   created_user_id |   location_granularity_id |   is_approved | created_at                  | updated_at                  | eventUrl                                                     |
|---------:|-------------:|:-------------------------------------------|:--------------------|:-----------|:-----------------|:-------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------:|------------:|------------------:|--------------------------:|--------------:|:----------------------------|:----------------------------|:-------------------------------------------------------------|
| 11919404 |          231 | Pennsylvania, USA                          | 2022-12-01 18:36:53 | Severe     | Unknown          | PENNSYLVANIA - Photos - Suspects - Evidence In Multi-County Drug Bust                | https://www.wfmz.com/news/area/berks/photos-suspects-evidence-in-multi-county-drug-bust/collection_bf795c98-71ad-11ed-99fe-4305f426699b.html#1 | [69 NEWS] PENNSYLVANIA - PHOTOS: Suspects, evidence in multi-county drug bust "Authorities said they seized evidence that included 27.5 kilograms of cocaine with a potential street value of $2.7 million and 5.5 kilograms of fentanyl with a potential street value of $1.6 million." Read full article at: https://www.wfmz.com/news/area/berks/photos-suspects-evidence-in-multi-county-drug-bust/collection_bf795c98-71ad-11ed-99fe-4305f426699b.html#1                                                                       |    41.2033 |    -77.1945 |                14 |                         8 |             1 | 2022-12-02T18:44:43.000000Z | 2022-12-02T18:44:43.000000Z | https://drugs.globalincidentmap.com/event_detail?id=11919404 |
| 11919401 |           40 | Vancouver Island, British Columbia, Canada | 2022-12-01 18:33:01 | Severe     | Unknown          | CANADA - Drugs - Guns Seized As 4 BC Men With Hells Angels Ties Face Serious Charges | https://www.terracestandard.com/news/alleged-drug-traffickers-on-vancouver-island-with-hells-angels-ties-face-serious-charges/                 | [terracestandard.com] CANADA - Drugs, guns seized as 4 B.C. men with Hells Angels ties face ‘serious charges’ "CFSEU said the seized drugs included 7.75kg of cocaine, 4kg of cannabis, 1.9kg of methamphetamine, 248 oxycodone pills, and more." Read full article at: https://www.terracestandard.com/news/alleged-drug-traffickers-on-vancouver-island-with-hells-angels-ties-face-serious-charges/                                                                                                                              |    49.6506 |   -125.449  |                14 |                         5 |             1 | 2022-12-02T18:36:37.000000Z | 2022-12-02T18:36:37.000000Z | https://drugs.globalincidentmap.com/event_detail?id=11919401 |
| 11919397 |          133 | Male, Maldives                             | 2022-11-20 18:29:26 | Severe     | Unknown          | MALDIVES - Drugs Worth Mvr 2 Mln Seized By Customs                                   | https://avas.mv/en/125385                                                                                                                      | [avas.mv] MALDIVES - Drugs worth MVR 2 mln seized by Customs "Maldives Customs Service has seized 1.34 kg of drugs smuggled into the Maldives via courier." Read full article at: https://avas.mv/en/125385                                                                                                                                                                                                                                                                                                                         |     4.1755 |     73.5093 |                14 |                         5 |             1 | 2022-12-02T18:32:45.000000Z | 2022-12-02T18:32:45.000000Z | https://drugs.globalincidentmap.com/event_detail?id=11919397 |
| 11919394 |          231 | 100 South Willow Avenue, Compton, CA, USA  | 2022-11-29 18:23:50 | Severe     | Unknown          | CALIFORNIA - USD4 Million Worth Of Illegal Drugs Seized In Compton                   | https://www.foxla.com/news/4-million-worth-of-illegal-drugs-seized-in-compton                                                                  | [foxla] CALIFORNIA - $4 million worth of illegal drugs seized in Compton "A search warrant at the home resulted in the seizure of about 5.5 lbs. of suspected tar heroin, 10 kilos of suspected powder cocaine, 6 kilos of suspected powder fentanyl, 6,000 suspected ecstasy pills containing fentanyl, and 254,000 suspected fentanyl pills all worth a combined estimated street value of $4.17 million, authorities said. " Read full article at: https://www.foxla.com/news/4-million-worth-of-illegal-drugs-seized-in-compton |    33.896  |   -118.218  |                14 |                         5 |             1 | 2022-12-02T18:29:25.000000Z | 2022-12-02T18:29:25.000000Z | https://drugs.globalincidentmap.com/event_detail?id=11919394 |
| 11919392 |          166 | Gwadar, Pakistan                           | 2022-12-01 18:22:00 | Severe     | Unknown          | PAKISTAN - Convoy Of Camels Loaded With Drugs Seized                                 | https://pakobserver.net/convoy-of-camels-loaded-with-drugs-seized/                                                                             | [pakobserver.net] PAKISTAN - Convoy Of Camels Loaded With Drugs Seized "While searching the goods carried by the camels, ANF officials found them to be full of drugs (hashish). The drugs weighed around 1.4 tons." Read full article at: https://pakobserver.net/convoy-of-camels-loaded-with-drugs-seized/                                                                                                                                                                                                                       |    25.1313 |     62.325  |                14 |                         5 |             1 | 2022-12-02T18:23:49.000000Z | 2022-12-02T18:23:49.000000Z | https://drugs.globalincidentmap.com/event_detail?id=11919392 |

<sub>Markdown for the above table was printed with **`print(mqcDf.loc[mqcDf.index[:5]].to_markdown())`**</sub>

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[facepet](https://stackoverflow.com/users/16836514)** (2022-12-03): Wow, this is awesome. Thank you so much for the detailed explanation. Looks like i was just stuck on accessing ':contents'. I really appreciate it.
- **me** (2022-12-03): @facepet glad I could help! (That *is* a very unusual attribute....)
