---
title: "Python | How i get the link of products that doesn't have href with selenium"
site: stackoverflow
question_id: 75426987
answer_id: 75442484
url: https://stackoverflow.com/a/75442484
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-14T00:40:58Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75442484/revisions
accepted: false
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: [selectGet]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 24813710c139ebe14ebdf6c391709644f8fb6e324016467e2417c6929ada736f
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-14

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75442484>, 2023-02-14; score 0. Text as retrieved 2026-10-12.

While I think the API is more efficient, if you want a selenium+bs4 solution, this is an example.

Using these function:

```python
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup


## scroll to an element and click [targetEl can be and element or selector] ##
def scrollClick(driverX, targetEl, maxWait=5, scroll2Top=False, printErr=True):
    try:
        xWait = WebDriverWait(driverX, maxWait)
        if isinstance(targetEl, str):
            xWait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR,targetEl)))
            targetEl = driverX.find_element(By.CSS_SELECTOR, targetEl)
        xWait.until(EC.element_to_be_clickable(targetEl))
        driverX.execute_script('''
            arguments[0].scrollIntoView(arguments[1]);
        ''', targetEl, bool(scroll2Top)) ## execute js to scroll
        targetEl.click()
    except Exception as e: 
        if printErr: print(repr(e), '\nFailed to click', targetEl)


## find a nextSibling of refEl that matches selector [if specified by sel] ##
def selectNextSib(driverX, refEl, sel=False, printError=False):
    sel = sel.strip() if isinstance(sel, str) and sel.strip() else False
    try: ## execute js code to find next card
        return driverX.execute_script('''
            var sibling = arguments[0].nextElementSibling;
            while (sibling && arguments[1]) {
                if (sibling.matches(arguments[1])) break;
                sibling = sibling.nextElementSibling; } 
            return sibling;''', refEl, sel)
    except Exception as e: 
        if printError: print(f'Error finding next "{sel}":',repr(e))


## [bs4] extract text or attribute from a tag inside tagSoup ##
def selectGet(tagSoup, selector='', ta='', defaultVal=None):
    el = tagSoup.select_one(selector) if selector else tagSoup
    if el is None: return defaultVal
    return el.get(ta, defaultVal) if ta else el.get_text(' ', strip=True)


## parse product page html and extract product details ##
def getProductDetails(prodPgHtml:str, prodUrl=None):
    pSoup = BeautifulSoup(prodPgHtml.encode('utf-8'))
    detsDiv = pSoup.select_one('div.detail-item')
    detKeys = ['category_id', 'is_bulky', 'is_bumped',
               'is_free_shipping_allowed', 'item_id', 'item_uuid',
               'main_image_thumbnail', 'mine', 'sell_price',
               'seller_user_id', 'subcategory_id', 'itle', 'title']
    pDets = {} if detsDiv is None else {
        k.lstrip('data-').replace('-', '_'): v
        for k, v in sorted(detsDiv.attrs.items(), key=lambda x: x[0])
        if k.lstrip('data-').replace('-', '_') in detKeys
    }
    pDets['description'] = selectGet(pSoup, 'div.card-product-detail-top>p')
    pDets['date_posted'] = selectGet(pSoup, 'div[class$="published"]')
    pDets['views_count'] = selectGet(pSoup, 'i.ico-eye+span')
    pDets['likes_count'] = selectGet(pSoup, 'i.ico-coounter_favourites+span')
    pDets['seller_name'] = selectGet(pSoup, 'h2.card-user-detail-name')
    uLink = selectGet(pSoup, 'a.card-user-right[href]', 'href')
    if uLink: pDets['seller_link'] = urljoin(prodUrl, uLink)

    ### EXTRACT ANY OTHER DETAILS YOU WANT ###

    pDets['product_link'] = prodUrl
    return pDets
```

you can loop through the cards on the results page, clicking on each to open on a new tab and scrape the product details

```python
kSearch, maxItems = 'monitor', 1500 ## adjust as preferred
url = f'https://es.wallapop.com/app/search?keywords={"+".join(kSearch.split())}'
url = f'{url}&filters_source=search_box&latitude=39.46895&longitude=-0.37686'

browser = webdriver.Chrome() 
browser.get(url)
browser.maximize_window()

scrollClick(browser, 'button[id="onetrust-accept-btn-handler"]') ## accept cookies
scrollClick(browser, 'tsl-button[id="btn-load-more"]') ## load more [then ∞-scroll]

itemCt, scrapedLinks, products = 0, [], [] ## initiate
itemSel, nextItem = 'a.ItemCardList__item[title]', None
try: nextItem = browser.find_element(By.CSS_SELECTOR, itemSel) ## first card
except Exception as e: print('No items found:', repr(e))

while nextItem:
    itemCt += 1 # counter
    cpHtml, cpTxt = '', '' # clear/initiate
    resultsTab = browser.current_window_handle # to go back

    try: # click card -> open new tab -> scrape product details
        cpHtml, cpTxt = nextItem.get_attribute('outerHTML'), nextItem.text
        scrollClick(browser, nextItem) ## click current card
        # add wait ?
        browser.switch_to.window(browser.window_handles[1]) ## go to 2nd tab
        WebDriverWait(browser, 5).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.detail-item'))) ## wait to load details
        pLink = browser.current_url ## product URL
        if pLink not in scrapedLinks: # skip duplicates [just in case]
            products.append(getProductDetails(browser.page_source, pLink))
        scrapedLinks.append(pLink)
    except Exception as e:
        print('!', [itemCt], ' '.join(cpTxt.split()), repr(e)) ## print error
        pSoup = BeautifulSoup(cpHtml.encode('utf-8'), 'lxml')
        products.append({
            'title': selectGet(pSoup, '', 'title'),
            'price': selectGet(pSoup, 'span.ItemCard__price'),
            'errorMsg': f'{type(e)} {e}'
        }) ## [ make do with info in card ]

    try: # close all tabs other than results tab
        for w in browser.window_handles:
            if w != resultsTab:
                browser.switch_to.window(w)
                browser.close()
            browser.switch_to.window(resultsTab)
    except Exception as e:
        print('Failed to restore results-tab-only window:', repr(e))
        break

    # print('', end=f"\r[{itemCt} of {maxItems}] {' '.join(cpTxt.split())} {repr(e)}")

    if isinstance(maxItems, int):
        if maxItems < itemCt: break

    nextItem = selectNextSib(browser, nextItem, itemSel) # get next result card
```

Some notes:
- The second `scrollClick` call is for the "Load More" button - it only needs to be clicked once and after that more results load as you scroll down.
- Maintaining and checking `scrapedLinks` doesn't seem to be necessary as there doesn't appear to be any duplicates to filter out. [It's just a habit since some sites do have duplicates, especially if there's pagination...]
- If you set `maxItems` as `None` [or a really high number], it should keep scrolling and scraping until either 
  - there's no more to results to load, or
  - the page crashes [it crashed before 800 results when I tested]. In this, the API has an advantage (you can observe the [network logs](https://support.happyfox.com/kb/article/882-accessing-the-browser-console-and-network-logs/) as you click "Load More" and copy the [API request][1] to [curlconverter](https://curlconverter.com/python/) to generate code to replicate it, if you want a start on exploring it...)
- The resulting `products` should be [a list of dictionaries][2] each containing details about a different product.


Results should look something like [![opdf][3]][3]

---

Btw, you can also save the results using something like pandas [`.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html) like 

```python
# import pandas as pd
pd.DataFrame(products).to_csv('monitors.csv', index=False)
```


  [1]: https://i.sstatic.net/jQBL7.png
  [2]: https://i.sstatic.net/mWNBU.png
  [3]: https://i.sstatic.net/rWhm8.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[SkyManu](https://stackoverflow.com/users/21197547)** (2023-02-16): These code works really well but im scared of opening so muchs tabs
- **me** (2023-02-17): @SkyManu The `try...except` for closing all tabs except for the results tabs is exactly for that reason. Each product tab is closed before moving on to the next product, so there would only be one product tab open at any time....but I get what you're worried about. Like I said, using the API definitely seems preferable. Tbh, I just want to practice switching tabs with selenium
