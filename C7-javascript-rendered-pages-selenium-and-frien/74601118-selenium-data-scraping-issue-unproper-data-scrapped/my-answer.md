---
title: "Selenium Data scraping issue, unproper data scrapped"
site: stackoverflow
question_id: 74601118
answer_id: 74604995
url: https://stackoverflow.com/a/74604995
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-28T18:27:53Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74604995/revisions
accepted: true
score: 1
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 4114c4b4dc4a9d462109383618af791deb08b3c6f7c07798651bbf84351f5e0d
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-28

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74604995>, 2022-11-28; **accepted**; score 1. Text as retrieved 2026-10-12.

**Note:** it's usually more reliable to build a list of dictionaries [rather than separate lists like you are in the selenium version.]

---

Without a sample/mockup of your desired output, I can't be sure this is the exact format you'd want it in, but I'd suggest something like this solution using requests+bs4 [on the 3 links you includes as example]
```python
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
```
and then to display as table:
```python
# import pandas

pricesDf = pandas.DataFrame(priceList).set_index('product_name')
colOrder = sorted(pricesDf.columns, key=lambda c: c == 'source_url')
pricesDf = pricesDf[colOrder] # (just to push 'source_url' to the end)
```
[![op1][1]][1]

---

You could also get separate columns for each tablet-count-option, if you remove
```python
            pDet[pvrStrength] = ', '.join([
                pvOp.get_text(' ').strip() for pvOp in pvRow.select(opSel)
            ]) 
```
and **replace** it with this loop:
```python
            for pvoi, pvOp in enumerate(pvRow.select(opSel)):  
                pvoTxt = pvOp.get_text(' ').strip()
                tabletCt = pvoTxt.split(' - ')[0]
                pvoPrice = pvoTxt.split(' - ')[-1]
                if not tabletCt.endswith(' tablets'): 
                    tabletCt = f'[option {pvoi + 1}]'    
                    pvoPrice = pvoTxt
                
                pDet[f'{pvrStrength} - {tabletCt}'] = pvoPrice 
```

|index|Abilify \(Aripiprazole\)|Generic Equivalent - Abilify \(Aripiprazole\)|Generic Equivalent - Accolate \(Zafirlukast\)|Abilify ODT \(Aripiprazole\)|Generic Equivalent - Abilify ODT \(Aripiprazole\)|
|---|---|---|---|---|---|
|product\_endpt|abilify-tablet|abilify-tablet|accolate|abilify-mt|abilify-mt|
|brand\_or\_generic|Brand|Generic|Generic|Brand|Generic|
|rx\_requirement|Prescription Required|NaN|NaN|Prescription Required|NaN|
|2mg - 30 tablets|$219\.99|NaN|NaN|NaN|NaN|
|2mg - 90 tablets|$526\.99|NaN|NaN|NaN|NaN|
|5mg - 28 tablets|$160\.99|NaN|NaN|NaN|NaN|
|5mg - 84 tablets|$459\.99|NaN|NaN|NaN|NaN|
|10mg - 28 tablets|$116\.99|NaN|NaN|NaN|NaN|
|10mg - 84 tablets|$162\.99|NaN|NaN|NaN|NaN|
|15mg - 28 tablets|$159\.99|NaN|NaN|NaN|NaN|
|15mg - 84 tablets|$198\.99|NaN|NaN|NaN|NaN|
|20mg - 90 tablets|$745\.99|$67\.99|NaN|NaN|NaN|
|30mg - 28 tablets|$104\.99|NaN|NaN|NaN|NaN|
|30mg - 84 tablets|$289\.99|$75\.99|NaN|NaN|NaN|
|1mg/ml Solution - \[option 1\]|150 ml - $239\.99|NaN|NaN|NaN|NaN|
|2mg - 100 tablets|NaN|$98\.99|NaN|NaN|NaN|
|5mg - 100 tablets|NaN|$43\.99|NaN|NaN|NaN|
|10mg - 90 tablets|NaN|$38\.59|NaN|NaN|NaN|
|15mg - 90 tablets|NaN|$56\.59|NaN|NaN|NaN|
|10mg - 60 tablets|NaN|NaN|$109\.00|NaN|NaN|
|20mg - 60 tablets|NaN|NaN|$109\.00|NaN|NaN|
|10mg ODT - 84 tablets|NaN|NaN|NaN|$499\.99|NaN|
|15mg ODT - 84 tablets|NaN|NaN|NaN|$499\.99|NaN|
|5mg ODT - 90 tablets|NaN|NaN|NaN|NaN|$59\.00|
|20mg ODT - 90 tablets|NaN|NaN|NaN|NaN|$89\.00|
|30mg ODT - 150 tablets|NaN|NaN|NaN|NaN|$129\.99|
|source\_url|https://www\.canadapharmacy\.com/products/abilify-tablet|https://www\.canadapharmacy\.com/products/abilify-tablet|https://www\.canadapharmacy\.com/products/accolate|https://www\.canadapharmacy\.com/products/abilify-mt|https://www\.canadapharmacy\.com/products/abilify-mt|

(I transposed the table since there were so many columns and so few rows. Table markdown can be copied from output of `print(pricesDf.T.to_markdown())`)


  [1]: https://i.sstatic.net/SmMVf.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Lalit Joshi](https://stackoverflow.com/users/19430670)** (2022-11-29): Thanks! I am sorry as I haven't updated the solution, but yes this is something I am looking for. Thanks for the suggestion, will try to use dictionaries rather than lists next time onwards.
