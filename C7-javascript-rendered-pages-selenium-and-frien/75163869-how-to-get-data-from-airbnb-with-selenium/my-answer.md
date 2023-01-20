---
title: "How to get data from Airbnb with selenium"
site: stackoverflow
question_id: 75163869
answer_id: 75180049
url: https://stackoverflow.com/a/75180049
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-20T05:21:04Z
last_edited: 2023-01-20T05:26:52Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75180049/revisions
accepted: false
score: 1
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3974173bcb040a7f60e2597b0eddcfb0a164eab38dda1161603e2118ad7e5f50
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-20

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75180049>, 2023-01-20, last edited 2023-01-20; score 1. Text as retrieved 2026-10-12.

>  I received the error: `NoSuchWindowException: Message: no such window: target window already closed from unknown error: web view not found`

Which line is raising this error? I don't see anything in your snippets that could be causing it, but is there anything in your code [before the included snippet], or some external factor that could be causing the automated window to get closed? You could see if any of the answers to [this](https://stackoverflow.com/q/51775122/6146136) helps you with the issue, especially if you're using `.switch_to.window` anywhere in your code.

---

### Searching

(You should include screenshots or better descriptions of the fields you are targeting, especially when the issue is that you're having difficulty targeting them.)
> Secondly, I do the other stuffs:
> 
> ```python
> driver.get('https://www.airbnb.com.br/')
> a = driver.find_element(By.CLASS_NAME, "cqtsvk7 dir dir-ltr")
> ```
 
> want that selenium search for me the country where I want to extract the data (Poland, in this case) 

If you mean that you're trying to enter *"Poland"* into [this input field](https://i.sstatic.net/kzLrY.png), then the class `cqtsvk7` in *`cqtsvk7 dir dir-ltr`* appears to change. The `id` attribute might be more reliable; but also, it seems like you need to click on the [search area](https://i.sstatic.net/XLAbu.png) to make the input interactable; and after entering *"Poland"* you also have to click on the <img src="https://i.sstatic.net/RYriz.png?s=32"> search icon and wait to load the results.

```python
# from selenium.webdriver.support.ui import WebDriverWait

def search_airbnb(search_for, browsr, wait_timeout=5):
    wait_til = WebDriverWait(browsr, wait_timeout).until
    browsr.get('https://www.airbnb.com.br/')

    wait_til(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'div[data-testid="little-search"]')))
    search_area = browsr.find_element(
        By.CSS_SELECTOR, 'div[data-testid="little-search"]')
    search_area.click()
    print('CLICKED search_area')

    wait_til(EC.visibility_of_all_elements_located(
        (By.ID, "bigsearch-query-location-input")))
    a = browsr.find_element(By.ID, "bigsearch-query-location-input")
    a.send_keys(search_for)
    print(f'ENTERED "{search_for}"')

    wait_til(EC.element_to_be_clickable((By.CSS_SELECTOR, 
        'button[data-testid="structured-search-input-search-button"]')))
    search_btn = browsr.find_element(By.CSS_SELECTOR, 
        'button[data-testid="structured-search-input-search-button"]')
    search_btn.click()
    print('CLICKED search_btn')


searchFor = 'Poland'
search_airbnb(searchFor, driver)  # , 15) # adjust wait_timeout if necessary
```

**<sub>Notice that for the clicked elements, I used [`By.CSS_SELECTOR`](https://selenium-python.readthedocs.io/locating-elements.html#locating-elements-by-css-selectors); if unfamiliar with CSS selectors, you can consult [this reference](https://www.w3schools.com/cssref/css_selectors.php). You can also use [`By.XPATH`](https://selenium-python.readthedocs.io/locating-elements.html#locating-by-xpath) in these cases; this [XPath cheatsheet](https://devhints.io/xpath) might help then.</sub>**

---

### Scraping Results

> How can I get the place, city and price of all of my query of place to travel in airbnb?

Again, you can use CSS selectors [or XPaths] as they're quite versatile. If you use a function like

```python
def select_get(elem, sel='', tAttr='innerText', defaultVal=None, isv=False):
    try:
        el = elem.find_element(By.CSS_SELECTOR, sel) if sel else elem
        rVal = el.get_attribute(tAttr)
        if isinstance(rVal, str): rVal = rVal.strip()
        return defaultVal if rVal is None else rVal
    except Exception as e:
        if isv: print(f'failed to get "{tAttr}" from "{sel}"\n', type(e), e)
        return defaultVal
```

then even if a certain element or attribute is missing in any of the cards, it'll just fill in with `defaultVal` and all the other cards will still be scraped instead of raising an error and crashing the whole program. 

You can get a list of dictionaries in [`listings`](https://i.sstatic.net/mfKzt.png) by looping through the [result cards](https://i.sstatic.net/i1tLd.png) with [list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp) like

```python
listings = [{ 
        'name': select_get(el, 'meta[itemprop="name"]', 'content'),  # SAME TEXT AS
        # 'title_sub': select_get(el, 'div[id^="title_"]+div+div>span'),
        'city_title': select_get(el, 'div[id^="title_"]'),
        'beds': select_get(el, 'div[id^="title_"]+div+div+div>span'),
        'dates': select_get(el, 'div[id^="title_"]+div+div+div+div>span'),
        'price': select_get(el, 'div[id^="title_"]+div+div+div+div+div div+span'),
        'rating': select_get(el, 'div[id^="title_"]~span[aria-label]', 'aria-label')
        # 'url': select_get(el, 'meta[itemprop="url"]', 'content', defaultVal='').split('?')[0],
    } for el in driver.find_elements(
        By.CSS_SELECTOR, 'div[itemprop="itemListElement"]' ## RESULT CARD SELECTOR
    )]
```

---

### Dealing with Pagination

If you wanted to scrape from multiple pages, you can loop through them. [You can also use `while True` (instead of a `for` loop as below) for unlimited pages, but I feel like it's safer like this, even if you set an absurdly high limit like `maxPages=5000` or something; either way, it should `break` out of the loop once it rreaches the last page.]

```python
maxPages = 50 # adjust as preferred
wait = WebDriverWait(browsr, 3) # adjust timeout as necessary

listings, addedIds = [], []
isFirstPage = True
for pgi in range(maxPages):
    prevLen = len(listings) # just for printing progress

    ## wait to load all the cards ##
    try:
        wait.until(EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, 'div[itemprop="itemListElement"]')))
    except Exception as e:
        print(f'[{pgi}] Failed to load listings', type(e), e)
        continue # losing one loop for additional wait time

    ## check current page number according to driver ##
    try:
        pgNum = driver.find_element(
            By.CSS_SELECTOR, 'button[aria-current="page"]'
        ).text.strip() if not isFirstPage else '1'
    except Exception as e:
        print('Failed to find pgNum', type(e), e)
        pgNum = f'?{pgi+1}?'

    ## collect listings ##
    pgListings = [{
        'listing_id': select_get(
            el, 'div[role="group"]>a[target^="listing_"]', 'target',
            defaultVal='').replace('listing_', '', 1).strip(),
        # 'position': 'pg_' + str(pgNum) + '-pos_' + select_get(
            # el, 'meta[itemprop="position"]', 'content', defaultVal=''),
        'name': select_get(el, 'meta[itemprop="name"]', 'content'),
        #####################################################  
        ### INCLUDE ALL THE key-value pairs THAT YOU WANT ###
        #####################################################  
    } for el in driver.find_elements(
        By.CSS_SELECTOR, 'div[itemprop="itemListElement"]'
    )]

    ## [ only checks for duplicates against listings frm previous pages ] ##
    listings += [pgl for pgl in pgListings if pgl['listing_id'] not in addedIds]
    addedIds += [l['listing_id'] for l in pgListings]

    ### [OR] check for duplicates within the same page as well ###
    ## for pgl in pgListings:
    ##     if pgl['listing_id'] not in addedIds:
    ##         listings.append(pgl)
    ##     addedIds.append(addedIds) 

    print(f'[{pgi}] extracted', len(listings)-prevLen, 
          f'listings [of {len(pgListings)} total] from page', pgNum)

    ## got to next page ##
    nxtPg = driver.find_elements(By.CSS_SELECTOR, 'a[aria-label="Próximo"]')
    if not nxtPg:
        print(f'No more next page [{len(listings)} listings so far]\n')
        break ### [OR] START AGAIN FROM page1 WITH:
        ## try: _, isFirstPage = search_airbnb(searchFor, driver), True
        ## except Exception as e: print('Failed to search again', type(e), e)
        ## continue
        ### bc airbnb doesn't show all results even across all pages
        ### so you can get a few more every re-scrape [but not many - less than 5 per page]
    try: _, isFirstPage = nxtPg[0].click(), False
    except Exception as e: print('Failed to click next', type(e), e)

dMsg = f'[reduced from {len(addedIds)} after removing duplicates]'
print('extracted', len(listings), 'listings with', dMsg)
```

[`listing_id` seems to be the easiest way to ensure that only unique listings are collected. You can also form a link to that listing like `f'https://www.airbnb.com.br/rooms/{listing_id}'`.]

---

### Combining with Old Data [Load & Save]

If you want to save to CSV and also load previous from the same file with old and new data combined without duplicates, you can do some thing like

```python
# import pandas as pd
# import os

fileName = 'pol_airbnb.csv'
maxPages = 50

try:
    listings = pd.read_csv(fileName).to_dict('records')
    addedIds = [str(l['listing_id']).strip() for l in listings]
    print(f'loaded {len(listings)} previously extracted listings')
except Exception as e:
    print('failed to load previous data', type(e), e)
    listings, addedIds = [], []

#################################################
# for pgi... ## LOOP THROUGH PAGES AS ABOVE #####
#################################################
dMsg = f'[reduced from {len(addedIds)} after removing duplicates]'
print('extracted', len(listings), 'listings with', dMsg)

pd.DataFrame(listings).set_index('listing_id').to_csv(fileName)
print('saved to', os.path.abspath(fileName))
```

<sub>**Note that keeping the old data might mean that some the listings are no longer available.**</sub>

View [pol_airbnb.csv](https://docs.google.com/spreadsheets/d/118ETC3w_m7b3gaiZCcsx39tRA6KaNC0QhGdGak2HiDw/edit?usp=sharing) for my results with `maxPages=999` and searching again instead of `break`-ing in *`if not nxtPg....`*.
