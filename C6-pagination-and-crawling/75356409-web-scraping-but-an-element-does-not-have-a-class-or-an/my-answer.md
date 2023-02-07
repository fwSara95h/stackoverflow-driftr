---
title: "web scraping but an element does not have a class or an attribute"
site: stackoverflow
question_id: 75356409
answer_id: 75368606
url: https://stackoverflow.com/a/75368606
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-07T03:11:33Z
last_edited: 2023-02-07T15:33:57Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75368606/revisions
accepted: true
score: 0
chapter: C6
chapter_title: "Pagination and crawling"
cluster: scrape-pagination-crawling
helpers_referenced: [selectForList, selectGet]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5a8eb4eb5b28697e8ed8c5c9a00bcd42ec1f97b756eb4f109f8cf88f2eafc94f
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-07

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75368606>, 2023-02-07, last edited 2023-02-07; **accepted**; score 0. Text as retrieved 2026-10-12.

Can you include a link to a page as well as a screenshot or snippet of the source html that led you to use the `div[itemprop="color"]` / `div.fuel` / `div.carrosserie` / `div.puissance_fiscale` selectors? I only inspected [/peugeot/208/84502](https://www.automobile.tn/fr/occasion/peugeot/208/84502) on my browser, but I couldn't find any of them there which means at least SOME of the sites don't have any elements that match these selectors. 

If you're not sure that your target element will be found, you should check for `None` before trying to extract text like in the function below. <sub>(It's a simplification of `selectGet` from [this set of functions](https://pastebin.com/ZnZ7xM6u).)</sub>

```python
def selectTxt(tagSoup, selector='', defaultVal=None):
    el = tagSoup.select_one(str(selector).strip()) if selector else tagSoup
    return defaultVal if el is None else el.get_text(' ', strip=True)
```

So, using **`color = selectTxt(detailed_soup,'div[itemprop="color"]')`** would avoid raising error, but would also just return `None` for the page that I inspected. The solution below uses the function but also just loops to get all items from the [specs preview][1] of the listing, the [info section][2] of the details page, and the [technical details section][3] (which has the color btw) of the details page.

```python
firstPg, lastPg = 1, 25
car_info = [] ## AS BEFORE
renameKeys = {
    'Kms': 'Kilométrage', 'Localité': 'Gouvernorat', 'Boîte vitesses': 'Boîte'
}

headers = { ## AS BEFORE
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
session = requests.Session() ## AS BEFORE
session.headers.update(headers) ## AS BEFORE


for page_num in tqdm(range(firstPg, lastPg+1)): 
    url = f'https://www.automobile.tn/fr/occasion/{page_num}' ## AS BEFORE
    page = session.get(url) ## AS BEFORE
    soup = BeautifulSoup(page.content, "html.parser") ## AS BEFORE
    car_listings = soup.find_all("div", class_="occasion-item") ## AS BEFORE 

    for listing in car_listings:
        liDets = { k: selectTxt(listing, s) for k, s in [
            ('title','h2'), ('price','div.price'), ('description','p')] }
        
        sPrvw_sel = 'span.name~span.value'
        for spec in listing.select(f'ul.specs-preview>li:has({sPrvw_sel})'):
            k = selectTxt(spec,'span.name:has(~span.value)').strip(':').strip()
            liDets[renameKeys.get(k,k)] = selectTxt(spec,sPrvw_sel)
        
        listingLink = listing.select_one('a[href]')
        if not listingLink: ## JUST IN CASE
            car_info.append(liDets)
            continue
        detailed_page_link = "https://www.automobile.tn" + listingLink["href"] 
        detailed_page = session.get(detailed_page_link) ## AS BEFORE
        detailed_soup = BeautifulSoup(detailed_page.content, "html.parser") ## AS BEFORE

        for info in detailed_soup.select('div.infos>ul>li:has(label~span)'):
            k = selectTxt(info,'label:has(~span)').strip(':').strip()
            liDets[renameKeys.get(k,k)] = selectTxt(info,'label~span')

        tblSel = 'table[data-index="main"]:has(thead~tbody>tr:only-child)'
        for spec in detailed_soup.select(tblSel):
            k = selectTxt(spec,'thead').strip(':').strip()
            liDets[renameKeys.get(k,k)] = selectTxt(spec,'tbody>tr') 
        
        # phoneSel = 'div.infos>ul>li>span:has(i.fa-phone-alt)'
        # liDets['phone'] = selectTxt(detailed_soup, phoneSel)
        # liDets['details_link'] = detailed_page_link
        car_info.append(liDets) 
```

Use `firstPg` and `lastPg` to set which pages to scrape, and `renameKeys` to change any column names that are scraped from the page with *`k= selectTxt...`*. [The 3 I've already set are just to not have duplicate columns with different names from overlaps between the specs preview and the details page.] With **`lastPg=2`** I get [![df with 24 rows][4]][4]

---

Btw, if you uncomment the last 3 lines and add two more `for` loops to also include the [bottom of the info section][5] and the [collapsed] [equipments section][6]:

```python
        for desc in detailed_soup.select('div.description>p:has(b+br)'):
            k = selectTxt(desc,'b:has(+br)').strip(':').strip()
            desc.select_one('b:has(+br)').replace_with('') # !THIS EDITS detailed_soup
            liDets[renameKeys.get(k,k)] = desc.get_text(' ', strip=True)

        for e,eq in enumerate(detailed_soup.select('table[data-index="add"]')):
            k = selectTxt(eq,'thead',f'Equipements {e}').strip(':').strip()
            liDets[renameKeys.get(k,k)]=[selectTxt(x) for x in eq.select('td')]

        phoneSel = 'div.infos>ul>li>span:has(i.fa-phone-alt)'
        liDets['phone'] = selectTxt(detailed_soup, phoneSel)
        liDets['details_link'] = detailed_page_link
```

then the DataFrame might have [7 more columns][7] and you'll have collected pretty much all the data available on the details page [except for the comments].

If you want the comments as well, you can target them with the [`.dsq-widget-comment`][8] selector 
```python
        cmntList = detailed_soup.select('.dsq-widget-comment>p:only-child')
        liDets['comments_list'] = [selectTxt(x)for x in cmntList]
```


  [1]: https://i.sstatic.net/WsyTw.png
  [2]: https://i.sstatic.net/tWtCy.png
  [3]: https://i.sstatic.net/aGx1v.png
  [4]: https://i.sstatic.net/EyapD.png
  [5]: https://i.sstatic.net/qmnpI.png
  [6]: https://i.sstatic.net/5iBoh.png
  [7]: https://i.sstatic.net/B7phc.png
  [8]: https://i.sstatic.net/4rPUq.png
