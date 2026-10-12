# Code from my Stack Overflow answer https://stackoverflow.com/a/75818064 (posted 2023-03-22), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# import csv
with open('caselist.csv', newline='') as f:
    links = [l for l, *_ in csv.reader(f)]

# --- block 2 ---
with open('caselist.csv') as f:
    links = [l.strip() for l in f.read().splitlines() if l.strip().startswith('https://dockets.justia.com/docket')]

# --- block 3 ---
from bs4 import BeautifulSoup
import requests
th_fields = { 'case_plaintiff': 'Plaintiff', 'case_defendant': 'Defendant', 'case_number': 'Case Number', 
              'case_filed': 'Filed', 'court': 'Court', 'case_nature_of_suit': 'Nature of Suit', 
              'case_cause_of_action': 'Cause of Action',  'jury_demanded': 'Jury Demanded By' }
fgtParams = [('div', {'class': 'title-wrapper'})] + [('td', {'data-th': f}) for f in th_fields.values()]

# --- block 4 ---
## a simpler version of my selectGet function [ https://pastebin.com/ZnZ7xM6u ] 
def find_get_text(bsTag, tName='div', tAttrs=None):
    t = bsTag.find(tName, {} if tAttrs is None else tAttrs)
    if t: return t.get_text(' ',strip=True) # safer as a conditional

def scrape_docketsjustia(djUrl, paramsList=fgtParams):
    soup = BeautifulSoup((r:=requests.get(djUrl)).content, 'lxml')
    cases_class = 'wrapper jcard has-padding-30 blocks has-no-bottom-padding'
    cases = soup.find_all('div', class_=cases_class)

    # print(f'{len(cases)} cases <{r.status_code} {r.reason}> from {r.url}')
    return [[find_get_text(c, n, a) for n, a in paramsList] for c in cases]

# --- block 5 ---
all_ouputs = []
for url in links: 
    all_ouputs += scrape_docketsjustia(url)

# --- block 6 ---
with open("posts/caselist_output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(['case_title', *th_fields]) # [ header row with column names ]
    writer.writerows(all_ouputs)

# --- block 7 ---
## setup ##

import requests
from bs4 import BeautifulSoup
import pandas as pd # [I just prefer pandas]

input_fp = 'caselist.csv'
output_fp = 'posts/caselist_output.csv'
th_fields = { 'case_plaintiff': 'Plaintiff', 'case_defendant': 'Defendant', 'case_number': 'Case Number', 
              'case_filed': 'Filed', 'court': 'Court', 'case_nature_of_suit': 'Nature of Suit', 
              'case_cause_of_action': 'Cause of Action',  'jury_demanded': 'Jury Demanded By' }
fgtParams = [('case_title', 'div', {'class': 'title-wrapper'})] + [(k, 'td', {'data-th': f}) for k,f in th_fields.items()]

# --- block 8 ---
## function definitions ##

def find_get_text(bsTag, tName='div', tAttrs=None):
    t = bsTag.find(tName, {} if tAttrs is None else tAttrs)
    if t: return t.get_text(' ',strip=True)

def scrape_docketsjustia(djUrl, paramsList=fgtParams):
    soup = BeautifulSoup((r:=requests.get(djUrl)).content, 'lxml')
    cases_class = 'wrapper jcard has-padding-30 blocks has-no-bottom-padding'
    for c in soup.find_all('div', class_=cases_class): 
        return {k:find_get_text(c,n,a) for k,n,a in paramsList}

    # return {} # just return empty row if cases_class can't be found
    return {'error_msg': f'no cases <{r.status_code} {r.reason}> from {r.url}'}

# --- block 9 ---
## main logic ##

## load list of links 
# links = list(pd.read_csv(input_fp, header=None)[0]) # [ if you're sure ]
links = [l.strip() for l in pd.read_csv(input_fp, header=None)[0]  
         if l.strip().startswith('https://dockets.justia.com/docket/')] # safer

## scrape for each link
df = pd.DataFrame([scrape_docketsjustia(u) for u in links])
# df = pd.DataFrame(map(scrape_docketsjustia,links)).dropna(axis='rows') # drop empty rows
# df['links'] = links # [ add another column with the links ]

## save scraped data
# df.to_csv(output_fp, index=False, header=False) # no column headers
df.to_csv(output_fp, index=False)

# --- block 10 ---
def scrape_docketsjustia(djUrl, paramsList=fgtParams):
    soup = BeautifulSoup((r:=requests.get(djUrl)).content, 'lxml')
    cases_class = 'wrapper jcard has-padding-30 blocks has-no-bottom-padding'
    print(rStatus:=f'<{r.status_code} {r.reason}> from {r.url}') 

    c1 = soup.find('div', class_=cases_class)
    case1 = {k:find_get_text(c1 if c1 else soup, n, a) for k,n,a in paramsList}
    return {**case1, 'msg': rStatus}
    # return {**case1, 'msg': rStatus, 'from_link': djUrl}

# --- block 11 ---
columns = [*[k for k,*_ in fgtParams], 'msg']
# columns = [*[k for k,*_ in fgtParams], 'msg', 'from_link': djUrl]

with open(input_fp) as f:
    for li, l in enumerate(f):
        if not l.strip().startswith('https://dockets.justia.com/'): continue
        df = pd.DataFrame([scrape_docketsjustia(l.strip())])

        m, h = ('a', False) if li else ('w', True) ## new file if li==0
        df[columns].to_csv(output_fp, mode=m, index=False, header=h)
