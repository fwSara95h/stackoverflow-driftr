---
title: "Constructing GET url to retrieve JSON from JS button click function"
site: stackoverflow
question_id: 75004108
answer_id: 75022682
url: https://stackoverflow.com/a/75022682
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-05T18:11:54Z
last_edited: 2023-01-06T04:34:39Z
revisions: 4
revision_history: https://stackoverflow.com/posts/75022682/revisions
accepted: false
score: 0
chapter: C8
chapter_title: "Hidden APIs and JSON inside script tags"
cluster: scrape-hidden-api-json
helpers_referenced: [selectForList]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d3d90f51b757d41e184e7eca837ccf12c52654e2a3f2dbcef3d351975d0f5ae4
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-05

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75022682>, 2023-01-05, last edited 2023-01-06; score 0. Text as retrieved 2026-10-12.

> So for the required values in the function, `t`, `a` and `n` are:
> 
> ```python 
> t = 469603 
> n = 78074484 
> a = 1 
> ```


I think you mixed up the `n` and `a` values, but how do you get your `n`? In the JS code, it counts the number of elements that can be css-selected with `.section-area .menu-section` [basically, the number of menu sections displayed] - is it really just 1? 

And you don't need to add `data=..` in your url - the key-value pairs *inside* `data` should be joined by ampersand in the query like `?key1=value1&key2=value2...` [URL encoded ofc], so just `?menu_id={a}` in this case.

---

However, getting the URL right isn't enough - are you setting the right headers? If I look at the network logs, you need to set `'accept': 'application/json'` and `'x-requested-with': 'XMLHttpRequest'` to get the JSON response [with html in `$.value`], and you should set some [user agent](https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/) [like `'user-agent': 'Mozilla/5.0'`] to not get blocked.

---

But also, the URL I noticed in the network logs (for the [Southern Cross Kitchen page](https://untappd.com/v/southern-cross-kitchen/469603) to be specific) seems to be more in the **`/venue/more_menu/{venue_id}/{n}?section_id={section_id}`** format - I got an empty `$.value` with both
- the link that would be formed from your JS+HTML snippets (*`/venue/more_menu_section/469603/1?menu_id=78074484`*), as well as
- the `/more_menu/` link containing the sectionId in your html snippet (*`/venue/more_menu_section/469603/1?section_id=286735920`*), but 

I got a [html string with 3 more items](https://i.sstatic.net/cGe6e.png) in `jData['value']` with

```python
headers = {
  'accept': 'application/json', 'user-agent': 'Mozilla/5.0', 'x-requested-with': 'XMLHttpRequest'
}
mmUrl = 'https://untappd.com/venue/more_menu/469603/15?section_id=287454773'
response = requests.get(mmUrl, headers=headers)
jData = response.json()
```

(`mmUrl` copied from network logs just now - maybe the sectionId changes?) 

---

#### Complete Example

I've wrapped it in a function (`scrape_untappd_menu`) because I find it more convenient, especially in terms of error-handling.

<sub>**(If you try to run this, don't forget to include [`selectForList`](https://pastebin.com/ZnZ7xM6u).)**</sub>
```python
# def extract_..., selectForList ## PASTE FROM https://pastebin.com/ZnZ7xM6u

## just for returning and printing a message with one statement ##
def vRet(toPrint, toReturn=[]):
    print(toPrint)
    return toReturn

def scrape_untappd_menu(umLink, includeVenue=False):
    rootUrl,addSlash = 'https://untappd.com','' if umLink[:1]=='/' else '/'
    if not umLink.startswith(rootUrl):umLink=f'{rootUrl}{addSlash}{umLink}'
    selRef = {
      'name': 'div.beer-details>h5>a',
      'description': 'div.beer-details>h5>em',
      'rating': ('div[data-rating]', 'data-rating'),
      'label': 'div.beer-label',
      'label_updated':('div.beer-label>span[data-update-at]','data-update-at'),
      'about': 'div.beer-details>h6>span',
      'link': ('a[data-href=":beer"][href]', 'href'),
      'brewery': 'a[data-href=":brewery"]',
      'brewery_link': ('a[data-href=":brewery"][href]', 'href'),
      'log_src': ('a[data-href=":beer"]>img[src]', 'src')
    }

    ## fetch and parse page html ##
    pgResp = requests.get(umLink, headers={'user-agent': 'Mozilla/5.0'})
    try: pgResp.raise_for_status() 
    except Exception as e: return vRet(f'failed2scrape:{type(e)} - {e}')
    pgSoup = BeautifulSoup(pgResp.content)

    ## get some venue name and id ##
    vName, vn_h2, venuId = selectForList(pgSoup, [
        'div.venue-name>h1', 'div.venue-name>h2', 
        ('*[data-venue-id]', 'data-venue-id')])
    if not vName: vName =  umLink.split('/v/', 1)[-1].replace('-', ' ')
    if vn_h2: vName += f' [{vn_h2}]'
    if not venuId: print(f"could not find '*[data-venue-id]'") 
    
    ## get menu items from page ##
    mSel = 'ul.menu-section-list>li>div.beer-info'    
    mList = [selectForList(li, selRef) for li in pgSoup.select(mSel)]

    ## find moremenu button ##
    fetchMore, lmmCt = True, 1
    mmBtn_sel = [
        'a[data-href=":moremenu"][data-section-id]', 
        'a[data-href=":moremenusection"][data-menu-id]'
    ]
    mmBtn, msBtn = pgSoup.select_one(mmBtn_sel[0]), False
    if not mmBtn: 
        mmBtn, msBtn = pgSoup.select_one(mmBtn_sel[1]), True
        if not mmBtn: 
            fetchMore = False
            print(f"could not find '{', '.join(mmBtn_sel)}'")
    
    ## load more ##
    mSel = 'li>div.beer-info'   
    sectCt = len(pgSoup.select('.section-area .menu-section')) 
    sectId = mmBtn.get('data-section-id') if mmBtn else None
    menuId = mmBtn.get('data-menu-id') if mmBtn else None
    while fetchMore:
        lmmUrl = f'/venue/more_menu/{venuId}/{len(mList)}?section_id={sectId}'
        if msBtn: 
            lmmUrl = f'/venue/more_menu_section/{venuId}/{sectCt}'
            lmmUrl += f'?menu_id={menuId}'
        print(f'[{lmmCt}] loading more from {rootUrl+lmmUrl}', end='')
        lmReq = requests.get(f'{rootUrl}{lmmUrl}', headers={
            'accept': 'application/json', 
            'user-agent': 'Mozilla/5.0', 
            'x-requested-with': 'XMLHttpRequest'})
        try: 
            lmReq.raise_for_status() 
            jData = lmReq.json()
            fetchMore = jData['count']
            lmSoup = BeautifulSoup(jData['view'])
            if lmmUrl: sectCt += fetchMore
            print(f'\r[{lmmCt}] loaded {fetchMore} more from {rootUrl+lmmUrl}')
        except Exception as e: 
            return vRet(f'\n{type(e)} - {e}', mList)
        
        ## get more menu items from html string instide json response ##
        mList += [selectForList(li, selRef) for li in lmSoup.select(mSel)]
        lmmCt += 1
    
    ## some cleanup [and maybe add venue name,id,link] ##
    for mi, m in enumerate(mList):
        m['about'] = m['about'].replace(m['brewery'], '').strip(' \u2022')
        for k in ['link', 'brewery_link', 'log_src']:
            if str(m[k])[:1] == '/': mList[mi][k] = f'{rootUrl}{m[k]}'
        
        mDets = {'venueId': venuId, 'venue': vName} if includeVenue else {}
        for k, v in mList[mi].items(): 
            if k=='about' and v: v = v.strip('\u2022').strip().strip('\u2022')
            mDets[k] = v.strip() if isinstance(v, str) else v
        if includeVenue: mDets['venue_link'] = umLink
        mList[mi] = mDets
    
    return vRet(f'{len(mList)} menu items from {umLink}', mList)
```

You could call it for a single venue like

```python
menuList = scrape_untappd_menu('/v/southern-cross-kitchen/469603')
```
[![svenop][1]][1]

or, if you want to scrape menus from multiple venues:

```python
menuList = []
for vl in venueLinks: 
    menuList += scrape_untappd_menu(vl, includeVenue=True)
    print()
```

and you can also save the results as CSV (using [`pandas`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html) below):

```python
pandas.DataFrame(menuList).to_csv('untappd.csv', index=False)
```


  [1]: https://i.sstatic.net/s9z3p.png
