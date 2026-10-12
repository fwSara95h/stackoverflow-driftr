# Code from my Stack Overflow answer https://stackoverflow.com/a/75368606 (posted 2023-02-07), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def selectTxt(tagSoup, selector='', defaultVal=None):
    el = tagSoup.select_one(str(selector).strip()) if selector else tagSoup
    return defaultVal if el is None else el.get_text(' ', strip=True)

# --- block 2 ---
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

# --- block 3 ---
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

# --- block 4 ---
cmntList = detailed_soup.select('.dsq-widget-comment>p:only-child')
liDets['comments_list'] = [selectTxt(x)for x in cmntList]
