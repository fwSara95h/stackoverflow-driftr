---
title: "This code is suppose to extract contact person and fax number looks okay but does not work"
site: stackoverflow
question_id: 75900953
answer_id: 75903215
url: https://stackoverflow.com/a/75903215
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-31T22:33:02Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75903215/revisions
accepted: false
score: 0
chapter: C6
chapter_title: "Pagination and crawling"
cluster: scrape-pagination-crawling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f41b967fcce4f9f6c6396a61aeb2df63352f4cda79082cad3dd8111ac7790ae5
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-31

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75903215>, 2023-03-31; score 0. Text as retrieved 2026-10-12.

### Reason Behind the Missing Information

In `get_contact_person_and_fax_number` you have

> ```py
>     contact_div = link_soup.find("div", {"class": "info-gen-box clearfix"})
>     if contact_div:
>         contact_person = contact_div.find("div", {"class": "info-gen-box clearfix"})
> ```
> ```py
>         fax_number = contact_div.find("div", {"class": "info-fax info-mar"})
> ```

However, there is no nested `div.info-gen-box.clearfix`<sup>([view][1])</sup> on these pages (was that a typo?) and `div.info-fax.info-mar`<sup>([view][2])</sup> is not inside *`contact_div`* (you could just have `fax_number=link_soup.find("div",{"class":"info-fax info-mar"})` **outside** the *`if contact_div`* block).

---

### Suggested Solution

Below is my suggested version of `get_contact_person_and_fax_number`<sup>([view example output][3])</sup>

```py
def get_company_info(compUrl, pre_print=''):
    # Fetch and Parse HTML content with requests + BeautifulSoup
    lSoup = BeautifulSoup((lr:=requests.get(compUrl)).content, "html.parser")

    # Find the side box and zip together dt/dd tags with company info
    contact_div = lSoup.select_one('div[id="box-sideinfo"] dl:has(dt+dd)') 
    ckv = zip(
        contact_div.select('dt:has(+dd)'), contact_div.select('dt+dd')
    ) if contact_div else [] ## use empty list if container is not found 
    
    # Build a dictionary from zip
    get_k = lambda dx: ' '.join(dx.get_text(' ').split()).strip(':') ## [minimal spacing]
    def get_v(dx):
        if dx.find('dd'): return list(dx.stripped_strings)[0] ## for nested info
        return dx.get_text(' • ', strip=True)
    company_dets = {get_k(dt): get_v(dd) for dt,dd in ckv} ## [dict comprehension]

    # Print and Return
    lrStat = f'<[{lr.status_code} {lr.reason}]> in {lr.elapsed} from {lr.url}'
    if isinstance(pre_print, str):
        print(pre_print + f'{len(company_dets)} company details - {lrStat}')
    if not contact_div: company_dets['Error Message'] = f'No info - {lrStat}'
    return company_dets if company_dets else {'msg': f'!Error! No info - {lrStat}'}

def get_contact_person_and_fax_number(url):
    cDets = get_company_info(url, None)
    return (cDets.get('Contact Person'), cDets.get('Fax'))
```

You could also directly use `get_company_info` in *`for link in links:`*<sup>([view example output][4])</sup>

```py
        # if not url.startswith('http'): url = f"https://www.usaopps.com{url}"

        # Print contact person and fax number for this link
        keys_list, company_info = ['Contact Person', 'Fax'], get_company_info(url) #, None)
        for k in keys_list: print(f'    {k}: {company_info.get(k)}')
```

---

#### Other Suggestions

These are not essential, but I have some recommendations/notes about your *`for page_num...`* loop:
- imo it would be safer to have 
  ```py
      for link in page_soup.select('div.lr-title:has(a[href])'):
          url = link.find('a', href=True)['href']
  ```
  - [btw, why do you have `results` and `links`, which I expect are the same ResultSet, especially since you don't see to be using `results` for anything?]
- there should be something to stop the loop after the last page, otherwise you could be unnecessarily sending requests to pages without results; either
  - just `if not links: break` to stop as soon as you get to a page without results
  - or use a `while` loop with two conditions [demonstrated below]

```py
# Prompt user for NAICS code and build page 1 URL
naics_code = input("Enter NAICS code: ")
page_url = f"https://www.usaopps.com/government_contractors/search.htm?naics={naics_code}"

# Begin while loop
all_rows, pg_num, max_pgs = [], 0, 81
# max_pgs = int(max_pgs) if (max_pgs:=input('Page limit:')).isdigit() else None
while page_url and (pg_num:=pg_num+1)<=(max_pgs if max_pgs else pg_num):
    if not page_url.startswith('http'): page_url = f"https://www.usaopps.com{page_url}"
    pgSoup = BeautifulSoup((pr:=requests.get(page_url)).content, "html.parser")
    llen = len(links := pgSoup.select('div.lr-title:has(a[href])'))

    ## JUST FOR PRINTING PROGRESS (how many results and which page)
    abtRes = pgSoup.select('div.list-total,div.list-head>h2')[:2]
    pgProgressPlus = ' for '.join([p.get_text(' ',strip=True) for p in abtRes])
    print(f'[Page {pg_num}][{llen} Links]', pgProgressPlus, '\n')

    # Loop through and scrape result links while printing and/or collecting company info
    for ln, link in enumerate(links,1):
        url = link.find('a', href=True)['href']
        if not url.startswith('http'): url = f"https://www.usaopps.com{url}"

        # all_rows.append(company_info:=get_company_info(url,None)) ## collect data
        company_info = get_company_info(url, f'\n  [Page {pg_num}][Link {ln} of {llen}]')
        
        # for k,v in company_info.items():print(f'      {k}: {v}') ## print all
        keys_list = ['Contact Person','Fax']
        for k in keys_list: print(f'      {k}: {company_info.get(k)}')
    
    # Find next page link and update for next loop
    next_link = pgSoup.select_one('span.page-link a[href]:-soup-contains("Next")')
    page_url = next_link['href'] if next_link else None
    print('\n\n')
```

If you uncomment the *`## collect data`* line, the collected data would be something like [![opdf][5]][5]


  [1]: https://i.sstatic.net/4CPue.png
  [2]: https://i.sstatic.net/NszKg.png
  [3]: https://i.sstatic.net/L2LNI.png
  [4]: https://i.sstatic.net/MCRhM.png
  [5]: https://i.sstatic.net/2MDmR.png
