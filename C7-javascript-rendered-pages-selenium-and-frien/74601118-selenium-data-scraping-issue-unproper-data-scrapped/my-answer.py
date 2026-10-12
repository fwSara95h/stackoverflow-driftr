# Code from my Stack Overflow answer https://stackoverflow.com/a/74604995 (posted 2022-11-28), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# import requests
# from bs4 import BeautifulSoup

rootUrl = 'https://www.canadapharmacy.com'
prodList = ['abilify-tablet', 'accolate', 'abilify-mt']
priceList = []
for prod in prodList:
    prodUrl = f'{rootUrl}/products/{prod}'
    print('', end=f'Scraping {prodUrl} ')
    resp = requests.get(prodUrl)
    if resp.status_code != 200:
        print(f'{resp.raise_for_status()} - failed to get {prodUrl}')
        continue
    pSoup = BeautifulSoup(resp.content)

    pNameSel = 'div.product-name > h3'
    for pv in pSoup.select(f'div > div.card.product:has({pNameSel})'):
        pName = pv.select_one(pNameSel).get_text('\n').strip().split('\n')[0] 
        pDet = {'product_endpt': prod, 'product_name': pName.strip()}

        brgen = pv.select_one('div.badge-container > div.badge')
        if brgen: pDet['brand_or_generic'] = brgen.get_text(' ').strip()
        rxReq = pv.select_one(f'{pNameSel} p.mn')
        if rxReq: pDet['rx_requirement'] = rxReq.get_text(' ').strip()

        mgSel = 'div.product-select-options'
        opSel = 'option[value]:not([value=""])'
        opSel = f'{mgSel} + {mgSel}  select[name="productsizeId"] {opSel}'
        for pvRow in pv.select(f'div.product-select-options-row:has({opSel})'):
            pvrStrength = pvRow.select_one(mgSel).get_text(' ').strip()

            pDet[pvrStrength] = ', '.join([
                pvOp.get_text(' ').strip() for pvOp in pvRow.select(opSel)
            ])                 

        pDet['source_url'] = prodUrl
        priceList.append(pDet)
    print(f' [total {len(priceList)} product prices]')

# --- block 2 ---
# import pandas

pricesDf = pandas.DataFrame(priceList).set_index('product_name')
colOrder = sorted(pricesDf.columns, key=lambda c: c == 'source_url')
pricesDf = pricesDf[colOrder] # (just to push 'source_url' to the end)

# --- block 3 ---
pDet[pvrStrength] = ', '.join([
    pvOp.get_text(' ').strip() for pvOp in pvRow.select(opSel)
])

# --- block 4 ---
for pvoi, pvOp in enumerate(pvRow.select(opSel)):  
    pvoTxt = pvOp.get_text(' ').strip()
    tabletCt = pvoTxt.split(' - ')[0]
    pvoPrice = pvoTxt.split(' - ')[-1]
    if not tabletCt.endswith(' tablets'): 
        tabletCt = f'[option {pvoi + 1}]'    
        pvoPrice = pvoTxt

    pDet[f'{pvrStrength} - {tabletCt}'] = pvoPrice
