# Code from my Stack Overflow answer https://stackoverflow.com/a/75838329 (posted 2023-03-24), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# import pandas as pd
output_fp = 'digital-innovation-hubs.csv'
dfList, pg_num, max_pg = [], 0, None
base_url = 'https://s3platform.jrc.ec.europa.eu/digital-innovation-hubs-tool'
while (pg_num:=pg_num+1) and (not isinstance(max_pg,int) or pg_num<max_pg):
    pg_url = f'{base_url}?_eu_europa_ec_jrc_dih_web_DihWebPortlet_cur={pg_num}'
    # try: dfList += pd.read_html(pg_url, extract_links='all')[:1] ## [needs v1.5.0.]
    try: dfList += pd.read_html(pg_url)[:1]
    except Exception as e: pg_num, _ = -1, print(f'\n{e!r} from {pg_url}')
    else: print('', end=f'\rScraped {len(dfList[-1])} rows from {pg_url}')

# pd.concat(dfList).to_csv(output_fp, index=False) ## save without page numbers
df=pd.concat(dfList, keys=list(range(1,len(dfList)+1)),names=['from_pg','pgi'])
df.reset_index().drop('pgi',axis='columns').to_csv(output_fp, index=False)

# --- block 2 ---
# df = pd.concat(dfList.....
orig_cols = [c for c in df.columns if c != 'from_pg']
for ocn in orig_cols:
    if any(vals:=[cv for cv,*_ in df[ocn]]): df[ocn[0]] = vals
    if any(links:=[c[1] for c in df[ocn]]): df[ocn[0].split()[0]+' Links'] = links
if 'Email Links' in df.columns:
    df['Email'] = df['Email Links'].str.replace('mailto:','',1)
    df = df.drop('Email Links', axis='columns')
df = df.drop(orig_cols, axis='columns')
# df.....to_csv(output_fp, index=False)

# --- block 3 ---
def get_row_dict(trTag):
    row = { td['data-ecl-table-header']: td.get_text(' ', strip=True) 
            for td in trTag.select('td[data-ecl-table-header]')} 
    for td in trTag.select('td[data-ecl-table-header]:has(a[href])'):
        k, link = td['data-ecl-table-header'], td.find('a',href=True)['href']
        if k=='Email' and link.startswith('mailto:'):
            link = link.replace('mailto:', '', 1)
        row[(k.split()[0]+' Link') if row[k] else k] = link
    return row

# --- block 4 ---
# import requests
# import pandas as pd
# from bs4 import BeautifulSoup
# def get_row_dict...
output_fp = 'digital-innovation-hubs.csv'

all_rows, pg_num, max_pg = [], 0, None
next_link = 'https://s3platform.jrc.ec.europa.eu/digital-innovation-hubs-tool'
while next_link:
    pg_num += 1
    if isinstance(max_pg, int) and pg_num>max_pg: break
    pgSoup = BeautifulSoup((pgReq:=requests.get(next_link)).content, 'lxml')
    rows = pgSoup.select('tr:has(td[data-ecl-table-header])')
    all_rows += [{'from_pg': pg_num, **get_row_dict(r)} for r in rows]
    # all_rows += [get_row_dict(r) for r in rows] # no "from_pg" column

    ## just for printing ##
    pgNum = pgSoup.find('span', {'aria-current':"true", 'aria-label':True})
    if pgNum: pgNum = ['',*pgNum.get_text(' ', strip=True).split()][-1]
    from_pg=int(pgNum) if isinstance(pgNum,str) and pgNum.isdigit() else pg_num
    rowCt = pgSoup.find('div', class_='ecl-u-type-prolonged-s')
    rowCt = rowCt.text.split(':')[-1].strip() if rowCt else 'UNKNOWN'  
    vStr = f'{len(rows)} scraped [total: {len(all_rows)} of {rowCt}] - '
    vStr += f'<{pgReq.status_code} {pgReq.reason}> from {pgReq.url}'
    print(f'\r[{pg_num}][{pgNum}] {vStr}', end='')

    next_link = pgSoup.find('a', {'href':True, 'aria-label':'Go to next page'})
    if next_link: next_link = next_link['href']

pd.DataFrame(all_rows).to_csv(output_fp, index=False)

# --- block 5 ---
import requests
import pandas as pd
from bs4 import BeautifulSoup

# --- block 6 ---
def get_hub_section(h2_tag):
    sibs = h2_tag.find_next_siblings(True) ## section contents
    hTxt = ' '.join(h2_tag.get_text(' ').split()) ## header text - minimize space
    if not sibs: return hTxt, None

    if len(sibs)==1 and sibs[0].name in ['ul','ol']: ## list
        l_items = [li.get_text(' ',strip=True) for li in sibs[0].select('li')]
        return hTxt, l_items
    if not (len(sibs)==1 and sibs[0].name=='dl'): ## paragraphs [default]
        p_list = [p.get_text(' ') for p in sibs if p.text.strip()]
        return hTxt, '\n'.join([' '.join(p.split()) for p in p_list])

    sub_sections = {} ## section will be further parsed to a dictionary 
    for d in sibs[0].select('dt:has(+dd)'):
        k = ' '.join(d.get_text(' ').split()) ## subheader - minimize whitespace
        ss_text = d.find_next('dd').get_text(' ',strip=True)
        links = [a['href'] for a in d.find_next('dd').find_all('a', href=True)]
        if len(links)==1: links = links[0]

        if links: sub_sections[f'{k} Links'] = links
        if ss_text and ss_text!=links: sub_sections[k] = ss_text
    return hTxt, sub_sections

# --- block 7 ---
def get_hub_info(hub_link, pre_print='', post_print=''):
    hSoup = BeautifulSoup((hReq := requests.get(hub_link)).content, 'lxml') 
    hub_info = [get_hub_section(h2) for h2 in hSoup.find_all('h2', {'id':True})]

    rStatus = f'<{hReq.status_code} {hReq.reason}> from {hReq.url}'
    print(f'\r{pre_print}{len(hub_info)} sections {rStatus}', end=post_print)
    return {'Hub Link': hub_link, **{k: v for k, v in hub_info}}

# --- block 8 ---
output_fp = 'digital-innovation-hubs.csv' ## from previous output
hubs_opfp = 'DIH-hubs-detailed.csv' ## can be the same as output_fp to replace it

### GET LIST OF LINKS ###
# hub_links = set(df['Hub Link']) ## if you're scraping for both outputs at once
hub_links = set(pd.read_csv(output_fp)['Hub Link']) ## if you already have output_fp

## SCRAPE AND SAVE ##
llen = len(hub_links)
data = [get_hub_info(l, f'[{i} of {llen}] ') for i, l in enumerate(hub_links,1)]
pd.json_normalize(data, sep=' → ').to_csv(hubs_opfp, index=False)
# pd.DataFrame(data).to_csv(hubs_opfp, index=False) ## doesn't expand subheaders
