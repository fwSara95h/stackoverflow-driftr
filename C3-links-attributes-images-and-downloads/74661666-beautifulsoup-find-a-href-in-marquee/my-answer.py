# Code from my Stack Overflow answer https://stackoverflow.com/a/74663126 (posted 2022-12-03), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# import json

marq = soup.find('marquee', attrs={'class':'h-48'})
if marq is None: print('Could Not Find marquee.h-48')
if not marq.get(':contents'): print('marquee.h-48 has no [:contents] attr')

try: mqCont =  json.loads(marq.get(':contents', '[]'))
except Exception as e:
    mqCont = []
    print('failed to parse marquee.h-48[:contents] <---', e)

# --- block 2 ---
mqCont = json.loads(soup.select_one('marquee.h-48').get(':contents', '[]'))

# --- block 3 ---
evtUrls = [f"{url.strip('/')}/event_detail?id={m['id']}" for m in mqCont if 'id' in m]

# --- block 4 ---
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
