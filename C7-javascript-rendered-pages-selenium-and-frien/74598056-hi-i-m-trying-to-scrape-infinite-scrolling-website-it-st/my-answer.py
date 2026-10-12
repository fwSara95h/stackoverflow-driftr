# Code from my Stack Overflow answer https://stackoverflow.com/a/74631249 (posted 2022-11-30), extracted verbatim; may need the question's context to run.

# --- block 1 ---
if urel in scrapedUrls: continue ## add this line
result = requests.get(urel) ## from your code
scrapedUrls.append(urel) ## add this line

# --- block 2 ---
refDict = {
    'title': 'h1.js-lot-title',
    'price_text': 'div.price-container',
    'price_amt': 'div.price-container > .price span.price-val',
    'price_cur': 'div.price-container > .price span.price-cur',
    '.lot-text tr.property': {'k':'td.property-name', 'v':'td.property-value'},
    'contact_name': '.author > div.name',
    'contact_phone': '.author > a.phone',
    'lot_warning': 'div.lot-warning',
    'div.lot-info': {'sel': 'p', 'sep': ':'},
    'description': '.lot-text p'
}

# --- block 3 ---
## FIRST PASTE FUNTION DEFINITIONS FROM https://pastebin.com/hKXYetmj

productDetails = []
puLen = len(prodUrls)
for pi, pUrl in enumerate(prodUrls[:500]):
    print('', end=f'\rScraping [for {pi+1} of {puLen}] {pUrl}')
    pDets = {'prodId': [w for w in pUrl.split('/') if w][-1]}

    resp = requests.get(pUrl)
    if resp.status_code != 200:
        pDets['Error_Message'] = f'{resp.raise_for_status()}'
        pDets['sourceUrl'] = pUrl
        productDetails.append(pDets) 
        continue

    pSoup = BeautifulSoup(resp.content, 'html.parser')
    pDets = fillDict_fromTag(pSoup, refDict, pDets, rootUrl)

    pDets['sourceUrl'] = pUrl
    productDetails.append(pDets)
print()
prodDf = pd.DataFrame(productDetails).set_index('prodId')
prodDf.to_csv('ProductDetails.csv')
