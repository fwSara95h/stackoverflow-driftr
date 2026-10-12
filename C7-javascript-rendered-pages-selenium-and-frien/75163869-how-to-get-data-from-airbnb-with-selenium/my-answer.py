# Code from my Stack Overflow answer https://stackoverflow.com/a/75180049 (posted 2023-01-20), extracted verbatim; may need the question's context to run.

# --- block 1 ---
> driver.get('https://www.airbnb.com.br/')
> a = driver.find_element(By.CLASS_NAME, "cqtsvk7 dir dir-ltr")
>

# --- block 2 ---
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

# --- block 3 ---
def select_get(elem, sel='', tAttr='innerText', defaultVal=None, isv=False):
    try:
        el = elem.find_element(By.CSS_SELECTOR, sel) if sel else elem
        rVal = el.get_attribute(tAttr)
        if isinstance(rVal, str): rVal = rVal.strip()
        return defaultVal if rVal is None else rVal
    except Exception as e:
        if isv: print(f'failed to get "{tAttr}" from "{sel}"\n', type(e), e)
        return defaultVal

# --- block 4 ---
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

# --- block 5 ---
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

# --- block 6 ---
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
