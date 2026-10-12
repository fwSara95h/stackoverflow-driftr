# Code from my Stack Overflow answer https://stackoverflow.com/a/77034640 (posted 2023-09-04), extracted verbatim; may need the question's context to run.
rootUrl = 'https://docs.derivative.ca'
req = requests.get(rootUrl+'/Category:CHOPs')
req.raise_for_status() # in case of error

## getting the links
soup = BeautifulSoup(req.content, 'html.parser')
groups = soup.select('div.mw-category-group:has(h3~ul)')
chops = [{
    'group': g.h3.get_text(strip=True),
    'category': a.get_text(strip=True),
    'link': rootUrl + a['href']
} for g in groups for a in g.select('li>a[href]')]

cLen = len(chops)
print('found', cLen, 'categories with links')

## getting the descriptions
for i, c in enumerate(chops):
    # print(f'scraping {i+1} of {cLen}: {repr(c["category"])} from {c["link"]}')
    cReq = requests.get(c['link'])
    try: cReq.raise_for_status()
    except: continue
    cSoup = BeautifulSoup(cReq.content, 'html.parser')

    summary_p1 = cSoup.select_one('h2:has(span#Summary)~p')
    if summary_p1: chops[i]['description'] = summary_p1.get_text(strip=True)
