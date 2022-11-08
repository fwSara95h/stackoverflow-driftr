---
title: "Webscraping using python for a webpage having \"Mehr Anseigen\" i.e(eng: Show more)"
site: stackoverflow
question_id: 74350179
answer_id: 74368223
url: https://stackoverflow.com/a/74368223
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-08T23:15:08Z
last_edited: 2023-02-01T10:49:01Z
revisions: 4
revision_history: https://stackoverflow.com/posts/74368223/revisions
accepted: true
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: [extractAttr/getListingDetails, getListingDetails, linkToSoup, linkToSoup_selenium]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 90d6f46053152453358377ec3421343bad103cdb6e3e28935d4bc38ca5621ef7
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-08

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74368223>, 2022-11-08, last edited 2023-02-01; **accepted**; score 0. Text as retrieved 2026-10-12.

I have [a function (`linkToSoup_selenium`)](https://gist.github.com/Driftr95/cbae6710c134df708f44ade8503f6638#file-linktosoup_selenium-py) that can click through the button a set number of times and then scrape the page
```python
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
```
(You can either save it as a file and import or paste it at the beginning of your code.) Through the `clickFirst` parameter [a list of xpaths of elements to click], add the [XPath](https://devhints.io/xpath) of "Mehr Anzeigen" as many times as you want to click (it's better to overestimate, since it will only print an error message if it can't click, but since it's inside an isolated `try` block, the rest of program will continue - that's why `strictMode=False` is important here).

<hr>

And then, to get the details, you can define a function as below <sub>(or copy [the full version](https://pastebin.com/BpjZSQPi))</sub>

```python
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
```
as well as a dictionary of [selectors](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) for each detail
```python
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
```

<hr>

Then, you can simply use list comprehension with `getListingDetails` [from above] and `select`, and then save with `pandas`

```python
if soup:
    lDets = [
        getListingDetails(a, selRef)
        for a in soup.select('article[id^="treffer_"]')
    ]

    pandas.DataFrame(lDets).to_csv('listingDetails.csv', index=False) # save
```
(`lDets` is a list of dictionaries in the same format as `selRef` but with details of the ads instead of selectors.)

The resulting CSV looks like [![Output CSV][1]][1]

<hr><hr>

### <h3 id="SeleniumOnly_edit">[EDIT] Selenium without BeautifulSoup</h3>

First, to clear the cookies popup and then repeatedly load more without the function,
```python
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
```
It will stop trying to load more once the button disappears, or after clicking a maximum number of time (50 as it is); if you don't want to set a maximum, use `while True` instead of `for lm_clickCt in range(loadMore_maxClicks)`, but the button stops working for me sometimes (even when I'm using the browser directly) and I didn't want the program to hang due to an infinite loop.

For extracting details, `selRef` can remain as is but `getListingDetails` will need some adjustments:
```python
# def getListingDetails(lSoup, refDict): # becomes 
def getListingDetails(listingEl, refDict):
```
```python
        # s = lSoup.select_one(sel) # becomes 
        s = listingEl.find_elements(By.CSS_SELECTOR, sel)
```
```python
            # detVal = s.get_text(' ', strip=True) # becomes 
            detVal = s[0].get_attribute('innerText').strip()
```
```python
            # detVal = s.get(attr) # becomes 
            detVal = s[0].get_attribute(attr)
```
and creating `lDets` will also be altered a little
```python
lDets = [
    getListingDetails(a, selRef) for a in
    browser.find_elements(By.CSS_SELECTOR, 'article[id^="treffer_"]')
]
```


  [1]: https://i.sstatic.net/WMhve.png
