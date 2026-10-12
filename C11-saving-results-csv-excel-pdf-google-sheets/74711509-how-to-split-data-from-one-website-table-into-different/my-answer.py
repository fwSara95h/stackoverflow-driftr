# Code from my Stack Overflow answer https://stackoverflow.com/a/74749317 (posted 2022-12-09), extracted verbatim; may need the question's context to run.

# --- block 1 ---
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

# --- block 2 ---
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

# --- block 3 ---
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
