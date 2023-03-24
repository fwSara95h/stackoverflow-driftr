---
title: "itterating over a set of data - so that i fetch data from a site with beautiful-soup, panda and store it subsequently"
site: stackoverflow
question_id: 75828524
answer_id: 75831803
url: https://stackoverflow.com/a/75831803
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-24T09:13:22Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75831803/revisions
accepted: false
score: 1
chapter: C11
chapter_title: "Saving results: CSV, Excel, PDF, Google Sheets"
cluster: scrape-to-files-tables
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 854d1855bbce20fbba315fdd98dca71bb0c53ae6e8cf5a025a01519178dda053
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-24

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75831803>, 2023-03-24; score 1. Text as retrieved 2026-10-12.

Note: you can reduce your code to

```py
# [import requests,bs,pd..]
#soup=BeautifulSoup(requests.get('https://schulen.bildung-rp.de').content,'html.parser')
# fieldnames = ['Kurzbezeichnung','Schulnummer','Anschrift', 'Telefon',...] 
get_row = lambda tr: [c.text.strip() for c in tr.find_all('td')]
data_gen = (get_row(row) for row in soup.find('table').find_all('tr'))
data = [dict(zip(fieldnames, row)) for row in data_gen if len(row)==len(fieldnames)]
```

But unless you have a `fieldnames` containing exactly 6 names, the *`if len(row)==__`* condition [in either code - yours or mine] will keep `data` empty, because the table at [schulen.bildung-rp.de](https://schulen.bildung-rp.de) has exactly 6 columns <sup>(**[view][1]** *`['Schulart','Schulnummer', 'Kurzbezeichnung','Adresse','PLZ','Datenschutz']`*)</sup>, and unless `fieldnames` represents them, the column headers will not make much sense even if `data` is not empty.

---

> ***update**: see a result-page here.* <sup>**[[screenshot](https://i.sstatic.net/EAkNT.png)]**</sup>

> *well i am looking for the following things -( categories ) in the dataset... 'Kurzbezeichnung','Schulnummer','Anschrift','Telefon','Telefax','E-Mail','Internet','Träger'*

> ```py
> # send a GET request to the target URL
> url = 'https://schulen.bildung-rp.de'
> response = requests.get(url)
> ```

The screenshot added [and the data you want] ***are from another page***<sup>([///einzelanzeige.html?///D=50360](https://schulen.bildung-rp.de/einzelanzeige.html?tx_wfqbe_pi1%5Buid%5D=50360))</sup>, not from [schulen.bildung-rp.de](https://schulen.bildung-rp.de), although the links to the page with that data are there. To get to that data, you will have to request it from each individual school's page link by link.

Since the links are in the third column (`Kurzbezeichnung`) of the [schulen.bildung-rp.de](https://schulen.bildung-rp.de) table, you can get the links with [`.select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) like:

```py
sl_sel='table#schulen tr td:first-child+td+td>a[href^="\/einzelanzeige.html?"]'
school_links = ['https://schulen.bildung-rp.de'+a['href'] for a in soup.select(sl_sel)]
```

or with `.find_all` like:

```py
checkHref = lambda h: isinstance(h,str) and h.startswith('/einzelanzeige.html?')
school_links = ['https://schulen.bildung-rp.de'+a['href'] for a in soup.find_all('a', href=checkHref)]
```

And below are 2 versions of a `get_school_details` which should be applied on loop to each URL in `school_links` to get each row of our final DataFrame.

---

### Version 1: With `pandas.read_html`

Since the data at each school page is also in a `table` tag, one option would be to use `pd.read_html`, which would get you those exact 8 fields. <sup>(not 7 btw)</sup> [ **[view output][2]** ]

```py
def get_school_details(school_link): 
    if not school_link.startswith('https://schulen.bildung-rp.de'):
        school_link = 'https://schulen.bildung-rp.de' + school_link
    return {k.strip(':').title(): v for k, v, *_ in 
            pd.read_html(school_link)[0].to_dict('split')['data']}
```

However, `pd.read_html` often clumps cell values into single-line strings without even spaces between separate lines, and you have less control over the data extracted.

---

### Version 2: With `requests`+`BeautifulSoup`

Using `requests`+`BeautifulSoup` can be slower and won't be as simple, but you will be able to extract more data. [ **[view output][3]** ]

```py
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
```

---

### Scraping All Links

```py
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
```

[![opdf][4]][4]

The screenshot above shows the results with version 2 of `get_school_details`, but you can see the full results with both versions in [this spreadsheet](https://docs.google.com/spreadsheets/d/1oroKd_TUYj90TxUbfj8_MVZm7tdfz2jrBIEPnMAPgDQ).

  [1]: https://i.sstatic.net/dwMm7.png
  [2]: https://i.sstatic.net/cFjdX.png
  [3]: https://i.sstatic.net/Ae9hr.png
  [4]: https://i.sstatic.net/pge4E.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[zero](https://stackoverflow.com/users/525865)** (2023-03-24): many thanks dear Drift95 for sharing your ideas and thoughts - this is really cool. And i am learning alot. Your explanation and the guidance is so awsome: Your great!!  Your help is appreciated alot! Have agreat weekend!
- **[zero](https://stackoverflow.com/users/525865)** (2023-03-24): hello dear Driftr95 - again this is so awesome - you have aawesome teaching style and i have gained lots of insights do your brilliant ideas: really i have learne alot from you - and your competence to solve problems. Dear Driftr95 one question left:  Could you perhaps have a look at this tiny script that i struggle with  - here: https://stackoverflow.com/questions/75828625/nonetype-object-is-not-subscriptable-bs4-task-fails-permanently - i would be more than happy. - have a great weekend.  Yours Malaga
