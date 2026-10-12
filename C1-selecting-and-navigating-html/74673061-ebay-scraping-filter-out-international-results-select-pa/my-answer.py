# Code from my Stack Overflow answer https://stackoverflow.com/a/74677546 (posted 2022-12-04), extracted verbatim; may need the question's context to run.

# --- block 1 ---
iDetSel = 'div[id="srp-river-results"] div.s-item__details'
# results = soup.select(iDetSel) # --> your current resultset
results = soup.select(f'{iDetSel}:not(:has(span.s-item__location))')

# --- block 2 ---
results = soup.find_all(
    lambda r: r.name == 'div' and 
    r.get('class') == ['s-item__details', 'clearfix'] and
    r.find_parent('div', {'class': 'srp-river-results clearfix'}) and
    not r.find('span', {'class': 's-item__location'})
)

# --- block 3 ---
url = 'https://www.ebay.com/sch/57988/i.html?_from=R40&_nkw=Fjallraven%20nuuk%20parka&LH_Complete=1&LH_Sold=1&_udlo=50&_udhi=600&LH_PrefLoc=1'
soup = BeautifulSoup(requests.get(url).content)

iDetSel = 'div[id="srp-river-results"] div.s-item__details' 
selectors = [
    ('With Location', f'{iDetSel}:has(span.s-item__location)') , 
    ('Without Location', f'{iDetSel}:not(:has(span.s-item__location))')  
] 
for t, sel in selectors:
    print(f'\n\n{t}')
    for r in soup.select(sel):
        print('   ', ' '.join(w for w in r.get_text(' ').split() if w)) # minimize whitespace

# --- block 4 ---
rsecSel = 'li:not(.srp-river-answer--REWRITE_START ~ li)'
iDetSel = f'div[id="srp-river-results"] {rsecSel} div.s-item__details'
results = soup.select(f'{iDetSel}:not(:has(span.s-item__location))')
