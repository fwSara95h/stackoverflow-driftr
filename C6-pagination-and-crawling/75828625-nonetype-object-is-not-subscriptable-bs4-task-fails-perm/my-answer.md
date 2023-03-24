---
title: "NoneType' object is not subscriptable : bs4 task fails permanently"
site: stackoverflow
question_id: 75828625
answer_id: 75838329
url: https://stackoverflow.com/a/75838329
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-24T21:43:56Z
last_edited: 2023-03-27T21:47:56Z
revisions: 5
revision_history: https://stackoverflow.com/posts/75838329/revisions
accepted: true
score: 1
chapter: C6
chapter_title: "Pagination and crawling"
cluster: scrape-pagination-crawling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: be404fde2407d20a3c90e682e4b570077be3283b0bcadc02b1566b159fe13b26
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-24

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75838329>, 2023-03-24, last edited 2023-03-27; **accepted**; score 1. Text as retrieved 2026-10-12.

### `pandas`-only Solution

If you just want the [immediately visible] table data, you can just use pandas [`read_html`](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html) on loop until it raises an exception and then [`concat`](https://pandas.pydata.org/docs/reference/api/pandas.concat.html) to concatenate all the scraped DataFrames together:

```py
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
```

As you would see from [**the output**][1], the links are not scraped. However, it should be noted that in `pandas` [1.5.0](https://pandas.pydata.org/pandas-docs/version/1.5/whatsnew/v1.5.0.html) you can set an `extract_links` parameter in `read_html`; results will look [**like this**][2], but can be [cleaned up][3] with something like:

```py
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
```

<br>

---

<br>

### `requests`+`bs4` Solution

The function below<sup>([**view outputs for first page**][4])</sup> should extract all the data from a single table row (`tr` tag):

```py
def get_row_dict(trTag):
    row = { td['data-ecl-table-header']: td.get_text(' ', strip=True) 
            for td in trTag.select('td[data-ecl-table-header]')} 
    for td in trTag.select('td[data-ecl-table-header]:has(a[href])'):
        k, link = td['data-ecl-table-header'], td.find('a',href=True)['href']
        if k=='Email' and link.startswith('mailto:'):
            link = link.replace('mailto:', '', 1)
        row[(k.split()[0]+' Link') if row[k] else k] = link
    return row 
```

<br>

My preferred approach when scraping paginated data is to use a `while` loop conditional on there being a next link.

```py
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
```
[![opdf][5]][5]

<br>

---

<br>

### **ADDED EDIT:** Scraping Hub Links

```py
import requests
import pandas as pd
from bs4 import BeautifulSoup
```

```py
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
```

```py
def get_hub_info(hub_link, pre_print='', post_print=''):
    hSoup = BeautifulSoup((hReq := requests.get(hub_link)).content, 'lxml') 
    hub_info = [get_hub_section(h2) for h2 in hSoup.find_all('h2', {'id':True})]

    rStatus = f'<{hReq.status_code} {hReq.reason}> from {hReq.url}'
    print(f'\r{pre_print}{len(hub_info)} sections {rStatus}', end=post_print)
    return {'Hub Link': hub_link, **{k: v for k, v in hub_info}}
```

```py
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
```

[![opdfnorm][6]][6]

<br>

---

<br>

[ [view results spreadsheet](https://docs.google.com/spreadsheets/d/1-GFwgAs77ThjyWfMPz-TQCbLf_x9foFgMllvs26WNV8/edit?usp=sharing) ]


  [1]: https://i.sstatic.net/GvEWH.png
  [2]: https://i.sstatic.net/3kwu1.png
  [3]: https://i.sstatic.net/yzcZh.png
  [4]: https://i.sstatic.net/JZHFS.png
  [5]: https://i.sstatic.net/wGPmc.png
  [6]: https://i.sstatic.net/ST2bJ.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[zero](https://stackoverflow.com/users/525865)** (2023-03-25): awesome . i  am overwhelmed - ii tried these scripots in google-colab - and got some questions - the scripts failed - and was not succesful - queston. at the beginning of the scripts i have noticed that some lines are commendted out. why is this so.  i will try to investigate more - meanwhile thanks alot..-. awesome. -. i will try the scripts locally on the vscode later the weekend - i  come back and report.. - conclusio: many many thanks for all your help this is so incredible-- i am  very happy...
- **me** (2023-03-25): @malaga what errors are you getting? Some of the commented lines are necessary (especially if they're `import`s, and if it's like `# def some_function...`, then you should replace that comment with that function definition). They're there to indicate where that section should be in the full code, but commented out to bring focus to the method being discussed in that section. [ See the full solutions: [pandas-only](https://pastebin.com/YwxHeKDT) , [pandas-only-with_links](https://pastebin.com/34ryb1AS) , [bs4+reqs+pandas](https://pastebin.com/FQGSCi3z) ]
- **me** (2023-03-25): If the commented line is very similar to the line above or below it, they're alternatives, [and the difference it makes should indicated at the end of the commented line] - for example: [in the bs4+requests solution] using *`all_rows += [{'from_pg': pg_num, **get_row_dict(r)} for r in rows]`* will add a `from_pg` column (with the page numbers) to the left of the DataFrame/table, but using the commented line ( *`all_rows += [get_row_dict(r) for r in rows]`* ) instead will not add that column
- **[zero](https://stackoverflow.com/users/525865)** (2023-03-26): hi - many thanks for the reply and the explanation - the errors i am getting are shown in the updated posting - below the image of a result page - called the second idea with the awesome scripts-  here you see what i am getting while running it in google-colab - see also here https://pastebin.com/wbEUE8MR - well i am trying to digg deeper and to get full understansing of your explanaton . it is really great that you do such an awesome support and show me so much-.
- **me** (2023-03-26): @malaga all 3 errors are [NameError](https://docs.python.org/3/library/exceptions.html#NameError) *___ is not defined* - whichever object is raising the error, you just have to [**import**](https://www.digitalocean.com/community/tutorials/how-to-import-modules-in-python-3) [like: pandas as *`pd`* and bs4 as *`BeautifulSoup`*] or [**define**](https://www.guru99.com/variables-in-python.html) [like: *`df`*]
- **[zero](https://stackoverflow.com/users/525865)** (2023-03-27): hello dear driftr95 many thanks for the reply try to figure it out - as far as i understand you  right - i of course have to run the script as is with all the imports and so on. Will try to figure out whats going on - afaikt colab does not block me from successfully runing. btw: did you see that we have two differnt targets with a different size of information -. if we take the full page - view then we have lots more of information -see a page up in the threadstart and here .. there is a true difference - see
- **[zero](https://stackoverflow.com/users/525865)** (2023-03-27): see the page - and see (also )  the image up in the threadstart - a true difference in the amount of data ... https://s3platform.jrc.ec.europa.eu/digital-innovation-hubs-tool/-/dih/17265/view?_eu_europa_ec_jrc_dih_web_DihWebPortlet_backUrl=%2Fdigital-innovation-hubs-tool  - well Driftr95 - . it would be awesome if we were able to get this full set of data... - BTW. i really appreciate any and all help in this.,. . have agreat day
- **me** (2023-03-27): @malaga I've written a `get_hub_info` function which will take a url like [the one in your comment](https://s3platform.jrc.ec.europa.eu/digital-innovation-hubs-tool/-/dih/17265/view?_eu_europa_ec_jrc_dih_web_DihWebPortlet_backUrl=%2Fdigital-innovation-hubs-tool) and return a dictionary ([view example](https://i.sstatic.net/6YGMU.png)) of the sections on that page.
- **me** (2023-03-27): I've added that as an edit to my answer and also added 2 sheets ["detailed-normalized" and "detailed-not-normalized"] to the [results spreadseet](https://docs.google.com/spreadsheets/d/1-GFwgAs77ThjyWfMPz-TQCbLf_x9foFgMllvs26WNV8/edit?usp=sharing)
- **[zero](https://stackoverflow.com/users/525865)** (2023-03-28): hi dear Driftr95 - many thanks for the reply and for all the efforts. This is awesome. and i am pretty sure that this is a big big learning-asset. Thanks for the structured guidance and for all the code: a true step forward in python for me. I am figuring out all the methods that you have showed in such a structured and didactical superb manner. This is more (much more) than expected. Your support here is just awesome.  -many many thanks ;)
- **[zero](https://stackoverflow.com/users/525865)** (2025-08-01): dear Drift95  many thanks for all the hints - and the brilliant help so far!
- **me** (2025-08-01): @zero Always happy to help!
