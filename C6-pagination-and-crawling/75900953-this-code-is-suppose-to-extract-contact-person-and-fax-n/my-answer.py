# Code from my Stack Overflow answer https://stackoverflow.com/a/75903215 (posted 2023-03-31), extracted verbatim; may need the question's context to run.

# --- block 1 ---
>     contact_div = link_soup.find("div", {"class": "info-gen-box clearfix"})
>     if contact_div:
>         contact_person = contact_div.find("div", {"class": "info-gen-box clearfix"})
>

# --- block 2 ---
>         fax_number = contact_div.find("div", {"class": "info-fax info-mar"})
>

# --- block 3 ---
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

# --- block 4 ---
# if not url.startswith('http'): url = f"https://www.usaopps.com{url}"

# Print contact person and fax number for this link
keys_list, company_info = ['Contact Person', 'Fax'], get_company_info(url) #, None)
for k in keys_list: print(f'    {k}: {company_info.get(k)}')

# --- block 5 ---
for link in page_soup.select('div.lr-title:has(a[href])'):
    url = link.find('a', href=True)['href']

# --- block 6 ---
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
