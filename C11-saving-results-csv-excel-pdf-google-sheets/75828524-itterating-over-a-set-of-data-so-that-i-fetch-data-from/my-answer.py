# Code from my Stack Overflow answer https://stackoverflow.com/a/75831803 (posted 2023-03-24), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# [import requests,bs,pd..]
#soup=BeautifulSoup(requests.get('https://schulen.bildung-rp.de').content,'html.parser')
# fieldnames = ['Kurzbezeichnung','Schulnummer','Anschrift', 'Telefon',...] 
get_row = lambda tr: [c.text.strip() for c in tr.find_all('td')]
data_gen = (get_row(row) for row in soup.find('table').find_all('tr'))
data = [dict(zip(fieldnames, row)) for row in data_gen if len(row)==len(fieldnames)]

# --- block 2 ---
> # send a GET request to the target URL
> url = 'https://schulen.bildung-rp.de'
> response = requests.get(url)
>

# --- block 3 ---
sl_sel='table#schulen tr td:first-child+td+td>a[href^="\/einzelanzeige.html?"]'
school_links = ['https://schulen.bildung-rp.de'+a['href'] for a in soup.select(sl_sel)]

# --- block 4 ---
checkHref = lambda h: isinstance(h,str) and h.startswith('/einzelanzeige.html?')
school_links = ['https://schulen.bildung-rp.de'+a['href'] for a in soup.find_all('a', href=checkHref)]

# --- block 5 ---
def get_school_details(school_link): 
    if not school_link.startswith('https://schulen.bildung-rp.de'):
        school_link = 'https://schulen.bildung-rp.de' + school_link
    return {k.strip(':').title(): v for k, v, *_ in 
            pd.read_html(school_link)[0].to_dict('split')['data']}

# --- block 6 ---
def get_school_details(school_link, typeFinder=lambda n:n.split()[0], sMsg=''):
    base_url = 'https://schulen.bildung-rp.de'
    if not school_link.startswith(base_url): school_link = base_url+school_link
    sSoup = BeautifulSoup((r:=requests.get(school_link)).content, 'html.parser')
    print(f'\r{sMsg}', rStatus:=f'<{r.status_code} {r.reason}> from {r.url}', end='')

    scName = sSoup.select_one('h1:has(~table)') 
    sDets = {'Schulname': scName.get_text(' ', strip=True)} if scName else {}

    carrier_link = None
    for row in sSoup.select('h1~table tr:has(td+td)'):
        k = ' '.join(row.find('td').get_text(' ').split()).rstrip(':').title()
        v = row.select_one('td+td').get_text(' ')

        if k.strip() == 'E-Mail': v = [''.join(v.replace('(at) ', '@').split())]
        else: v = [' '.join(l.split()) for l in v.splitlines() if l.strip()]

        if k.strip()=='Kurzbezeichnung': sDets['Schultyp'] = typeFinder(v[0]) if v else ''
        sDets[k.strip()] = '\n'.join(v)

    sDets['Schullink'] = school_link
    lRefs = {'Trägerlink': 'a[href^="/traeger.html?"]', 
             'osm_link':'a[href^="https://www.openstreetmap.org/#map="]',
             'dpo_link': f'a[href^="{base_url}/datenschutz.html?"]'}
    for k, s in lRefs.items():
        if (a:=sSoup.select_one(s.replace("/", "\\/"))): 
            sDets[k] = (base_url if k=='Trägerlink' else '') + a['href']

    return sDets if sDets else {'error_msg': f'Failed to scrape: {rStatus}'}

# --- block 7 ---
import requests
from bs4 import BeautifulSoup
import pandas as pd

## function for scraping a single school link ##
# def get_school_details..... # [choose from above or define your own]

## fetching homepage to extract school links ##
url = 'https://schulen.bildung-rp.de' 
soup = BeautifulSoup((response:=requests.get(url)).content, 'html.parser')

## [ optional ] for finding school type ##
tInps = [(s, s.next) for s in soup.select('input[name="schart"][value]')]
sTyps=[(s['value'],sn.strip().title()) for s,sn in tInps if isinstance(sn,str)]
get_stypes = lambda abbr: ', '.join({v for k,v in sTyps if k in str(abbr).split()})

## collecting the individual school links ##
sl_sel='table#schulen tr td:first-child+td+td>a[href^="\/einzelanzeige.html?"]'
school_links = [a['href'] for a in soup.select(sl_sel)]
links_ct = len(school_links)

''' ## scraping all the school links and saving - version 1 (pandas) ##
df = pd.DataFrame([get_school_details(l) for l in school_links])
# df['Schultyp'] =  df['Kurzbezeichnung'].apply(get_stypes) ## [if you want to add it]
# df['Schullink'] = school_links ## [if you want to add it]
df.to_csv('schulen_bildung.csv', index=False)
'''

## scraping all the school links and saving - version 2 (req+bs) ##
data = [get_school_details(l, get_stypes, f'\r[{li} of {links_ct}] ') 
        for li, l in enumerate(school_links, 1)]
