---
title: "How to split data from one website table into different outputs using Python"
site: stackoverflow
question_id: 74711509
answer_id: 74749317
url: https://stackoverflow.com/a/74749317
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-09T23:57:05Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74749317/revisions
accepted: true
score: 1
chapter: C11
chapter_title: "Saving results: CSV, Excel, PDF, Google Sheets"
cluster: google-sheets-docs
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: eb5377e0c283517668953a6fc25cdc95bb2fef1a73ca6debf58c7abfa1cf2b0c
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-09

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74749317>, 2022-12-09; **accepted**; score 1. Text as retrieved 2026-10-12.

[Not sure if you still need a solution or if the Google Sheets method is enough for you, but here's my suggested method.]

> I want one script that pulls all of the wave data, then separately another that pulls the high/low tide data

You can separate them out into two different functions:

```python
def getWaveData(mSoup, endPt='UNKNOWN'):
    wRows = []
    for tb in mSoup.select('.table-forecast > tbody'):
        wDay = tb.select_one('tr.tbody-title > th > h6')
        if wDay: wDay = wDay.get_text(' ')

        for tr in tb.select('tr[data-timestamp]'):
            wDets = [endPt, wDay]
            for td in tr.select('td'):
                td_ot = td.get('data-original-title', '').strip() 
                td_t = td.get('title', '').strip().replace('&deg', '°') 
                td_c = td.get('class', [])

                if td_ot and 'row-title' not in td_c: wDet = td_ot
                elif td_t and 'row-title' not in td_c: wDet = td_t
                elif td.select('ul.rating'): 
                    wDet = ''.join([mark*len(
                        td.select(f'ul.rating > li.{liClass}')
                    ) for liClass, mark in zip([
                        'active', 'inactive', 'placeholder'
                    ], ['*', '.', '_'])]) 
                elif 'table-forecast-wind' in td_c and td.select('.text-left'):
                    wDet = td.select_one('.text-left').get_text(' ') 
                else: wDet = td.get_text(' ')

                wDets.append(wDet)
            if len(wDets) < 19: 
                wDets = wDets[:-5] + [None]*(19 - len(wDets)) + wDets[-5:]
            if len(wDets) > 18: 
                wRows.append(tuple([' '.join(
                    w for w in wd.split() if w # minimize whitespace
                ) if type(wd) == str else wd for wd in wDets[:19]]))
    return wRows

def getTidesData(mSoup, endPt='UNKNOWN'):
    tRows = []
    for tb in mSoup.select('.table-forecast > tbody'):
        tDay = tb.select_one('tr.tbody-title > th > h6')
        if tDay: tDay = tDay.get_text(' ') 

        rSel = 'tr[data-filter="tides"]'
        cSel = 'td + td:has(+td.text-right), td.text-right'
        for tr in tb.select(f'{rSel}:has(td:is({cSel}))'):
            tDets = [endPt, tDay] + [td.get_text(' ') for td in tr.select(cSel)]

            if len(tDets) < 14:
                tDets = tDets[:-4] + [None]*(14 - len(tDets)) + tDets[-4:]
            if len(tDets) > 13: 
                tRows.append(tuple([' '.join(
                    w for w in t.split() if w # minimize whitespace
                ) if type(t) == str else t for t in tDets[:14]])) 
    return tRows
```

[`endPt` is for the `City` column.] This is not something you can simply use `pd.read_html` for if you want all the data, since some of it is inside tag attributes - also the tides tables are actually pairs of tables inside the last rows of the waves tables.

---

Now you just have to initialize the csv files [and `id_list` and `headers`]

```python
logFp = 'magicseaweed_scrapeLogs.csv' #<-- set None to just print not save
wavesFp = 'waves.csv' #<-- path to csv with waves data
tidesFp = 'tides.csv' #<-- path to csv with tides data
waveCols = [
    'City', 'Date', 'Time', 'Breaking Wave', # ps/ss = primary/secondary swell
    'Swell Rating', 'ps_height', 'ps_length', 'ps_angle', 'ss1_height', 
    'ss1_length', 'ss1_angle', 'ss2_height', 'ss2_length', 'ss2_angle',
    'Wind Speed', 'Wind Direction', 'Weather', 'Temperature', 'Prob.'
]
tideCols = [
    'City', 'Date', 'High1_time', 'High1_ft', 'Low1_time', 'Low1_ft', 
    'High2_time', 'High2_ft', 'Low2_time', 'Low2_ft', 
    'First Light', 'Sunrise', 'Sunset', 'Last Light'
]

for f, h in [(wavesFp, waveCols), (tidesFp, tideCols)]:
    if not os.path.isfile(f):
        pd.DataFrame([tuple(h)]).to_csv(f, index=False, header=False)

# id_list = [....]
# headers = {....}
root_url, idLen, scrapeLog = 'https://magicseaweed.com', len(id_list), []
```

`logFp`/`scrapeLog` is good for keeping track of which sites it failed to scrape from; `logFp` is also the only csv that will be over-written. `wavesFp` and `tidesFp` will be appended to, so they're initialized with the column headers [unless they already exist], because if you're use `.to_csv` with `mode='a'`, you should also use `header=False` if you don't want the header row repeated for every batch of rows.

---

After initializing, you can go ahead and loop through the links:

```python
for i, x in enumerate(id_list[:5]):
    url = root_url + x
    print('', end=f'\r[{i+1} of {idLen}] scraping {url}')
    try:
        r = requests.get(url, headers=headers)
        reqError = r.raise_for_status()
        if reqError:
            scrapeLog.append({'url': url, 'status': 'error', 'msg': reqError})
            continue
    
        soup = BeautifulSoup(r.content, 'html.parser')
        wList, tList = getWaveData(soup, x), getTidesData(soup, x)

        xMsg, xStatus = [], ('success' if wList and tList else 'missing data')
        for f, l in [(wavesFp, wList), (tidesFp, tList)]:
            pd.DataFrame(l).to_csv(f, mode='a', index=False, header=False)
            xMsg.append(f'added {len(l)} rows to {f}') 

        scrapeLog.append({'url':url, 'status':xStatus, 'msg':', '.join(xMsg)})
    except Exception as e:
        scrapeLog.append({'url': url, 'status': 'error', 'msg': f'{type(e)} - {e}'})

print('\n', pd.DataFrame(scrapeLog).to_csv(logFp, index=False))
```

**Please note that this code is dependent on the tables in the scraped page having the same columns as in `waveCols` and `tideCols`, arranged exactly in that order.**

[Spreadsheet with the CSV outputs I got.](https://docs.google.com/spreadsheets/d/12YGR3mTlcJcgGQ9RQkb_aLXjMiaBGV8_91nnuV9KiJk/edit?usp=sharing)

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Anthony Madle](https://stackoverflow.com/users/19425874)** (2022-12-10): This is amazing, thank you for such a thorough and well-thought out answer
