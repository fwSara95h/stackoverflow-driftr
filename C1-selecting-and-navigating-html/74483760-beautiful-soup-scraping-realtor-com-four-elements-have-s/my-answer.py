# Code from my Stack Overflow answer https://stackoverflow.com/a/74498917 (posted 2022-11-19), extracted verbatim; may need the question's context to run.
# [price, address, beds, baths, sqft, sqftlot, link]
selectors = [
    'div[data-label="pc-price-wrapper"]', ## can use 'div.ldp-redesign-price' 
    'div[data-label="pc-address"]', ## can use 'div.address'
    'li[data-label="pc-meta-beds"]', 
    'li[data-label="pc-meta-baths"]', 
    'li[data-label="pc-meta-sqft"]',
    'li[data-label="pc-meta-sqftlot"]'
]
infoList = [ # first, selecting tags
    ([r.select_one(s) for s in selectors], r.select_one('a[href]'))
    for r in soup.select('li[data-testid="result-card"]')
]# --> list of ([tags for rest of the list], hyperlink tag)

infoList = [( # getting the text (or link) from selected tags
    [(t.get_text(' ').strip() if t else None) for t in tags] + 
    [('https://www.realtor.com'+hl.get('href')) if hl else None]
) for tags, hl in infoList]

# you can use for-loop just for printing now
for info in infoList: print(info)
## although, you could also: # print('\n'.join([str(info) for info in infoList]))
