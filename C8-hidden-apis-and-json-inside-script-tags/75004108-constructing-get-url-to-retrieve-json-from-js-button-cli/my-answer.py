# Code from my Stack Overflow answer https://stackoverflow.com/a/75022682 (posted 2023-01-05), extracted verbatim; may need the question's context to run.

# --- block 1 ---
> t = 469603 
> n = 78074484 
> a = 1 
>

# --- block 2 ---
headers = {
  'accept': 'application/json', 'user-agent': 'Mozilla/5.0', 'x-requested-with': 'XMLHttpRequest'
}
mmUrl = 'https://untappd.com/venue/more_menu/469603/15?section_id=287454773'
response = requests.get(mmUrl, headers=headers)
jData = response.json()

# --- block 3 ---
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

# --- block 4 ---
menuList = scrape_untappd_menu('/v/southern-cross-kitchen/469603')

# --- block 5 ---
menuList = []
for vl in venueLinks: 
    menuList += scrape_untappd_menu(vl, includeVenue=True)
    print()

# --- block 6 ---
pandas.DataFrame(menuList).to_csv('untappd.csv', index=False)
