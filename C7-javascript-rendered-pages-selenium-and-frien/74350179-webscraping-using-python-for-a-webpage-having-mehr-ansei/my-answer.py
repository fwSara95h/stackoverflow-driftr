# Code from my Stack Overflow answer https://stackoverflow.com/a/74368223 (posted 2022-11-08), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# import pandas # for saving as table
# from linkToSoup_selenium import * ## OR PASTE HERE

cfList = (
    ['//div[@id="cmpbox"]//span[@id="cmpbntyestxt"]'] # "Akzeptieren" - for cookies, I think
    + ['//a[@id="mod-LoadMore--button"]']*30 # click LoadMore 30x
)

soup = linkToSoup_selenium(
     'https://www.gelbeseiten.de/suche/architekturb%c3%bcros/aachen?umkreis=21000'
    , ecx='//article[327]' # wait for listing #327 to load
    , clickFirst=cfList  # cookies + 30xLoadMore
    , strictMode=False # (is False by default but) do NOT set as True 
)

# --- block 2 ---
def getListingDetails(lSoup, refDict):
    detList = {}
    for k, (sel, attr, altr) in refDict.items():
        s = lSoup.select_one(sel)
        if s is None: detVal = None
        elif attr == '': detVal = s.get_text(' ', strip=True)
        else: detVal = s.get(attr)

        if detVal is None or type(altr) != list: altr = [] 
        for a, v in altr:
            if a == 'word1': detVal = detVal.split(v)[0]
            elif a == 'replace': detVal = detVal.replace(v[0], '', v[1]) 

        detList[k] = detVal
    return detList

# --- block 3 ---
selRef = {
    'Title': ('h2[data-wipe-name="Titel"]', '', ''),
    'Branch': ('p.mod-Treffer--besteBranche', '', ''),
    'Address': ('p[data-wipe-name="Adresse"]', '', ''),
    'Contact': ('p[data-wipe-name="Kontaktdaten"]', '', ''),
    'Website': ('a.contains-icon-homepage[href]', 'href', ''),
    'Email': ('a.contains-icon-email[href^="mailto:"]', 'href', [
        ('replace', ('mailto:', 1)), ('word1', '?')
    ]), 'DetailsPage': ('a.contains-icon-details[href]', 'href', '')
}

# --- block 4 ---
if soup:
    lDets = [
        getListingDetails(a, selRef)
        for a in soup.select('article[id^="treffer_"]')
    ]

    pandas.DataFrame(lDets).to_csv('listingDetails.csv', index=False) # save

# --- block 5 ---
ac_xpath = '//div[@id="cmpbox"]//span[@id="cmpbntyestxt"]'
WebDriverWait(browser, 25).until(EC.visibility_of_all_elements_located((By.XPATH, ac_xpath)))
browser.find_element(By.XPATH, ac_xpath).click()

loadMore_xpath = '//a[@id="mod-LoadMore--button"]'
loadMore_maxClicks = 50
for lm_clickCt in range(loadMore_maxClicks):
    print('', end=f'\rClicked "Mehr Anzeigen" {lm_clickCt} times')

    WebDriverWait(browser, 25).until(EC.visibility_of_all_elements_located((By.XPATH, loadMore_xpath)))
    loadMore_btn = browser.find_elements(By.XPATH, loadMore_xpath)
    browser.execute_script("arguments[0].scrollIntoView(false);", loadMore_btn[0])

    if not loadMore_btn: break
    loadMore_btn[0].click()
print('')

# --- block 6 ---
# def getListingDetails(lSoup, refDict): # becomes 
def getListingDetails(listingEl, refDict):

# --- block 7 ---
# s = lSoup.select_one(sel) # becomes 
s = listingEl.find_elements(By.CSS_SELECTOR, sel)

# --- block 8 ---
# detVal = s.get_text(' ', strip=True) # becomes 
detVal = s[0].get_attribute('innerText').strip()

# --- block 9 ---
# detVal = s.get(attr) # becomes 
detVal = s[0].get_attribute(attr)

# --- block 10 ---
lDets = [
    getListingDetails(a, selRef) for a in
    browser.find_elements(By.CSS_SELECTOR, 'article[id^="treffer_"]')
]
