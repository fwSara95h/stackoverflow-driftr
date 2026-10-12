# Code from my Stack Overflow answer https://stackoverflow.com/a/74512696 (posted 2022-11-20), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# import cloudscraper
r = cloudscraper.create_scraper().get('https://tiki.vn/api/personalish/v1/blocks/listings?limit=300&category=11232&sort=top_seller%3Fpage%3D5&urlKey=lam-sach-da-mat')
productList = r.json()['data']
print('### [{id}_{sku}: {name}] for first 10 products of', f'{len(productList)} ###\n')
for p in productList[:10]: print(f"{p['id']}_{p['sku']}: {p['name']}")

# --- block 2 ---
maxPages = 10  # or as you prefer
nextUrl = 'https://tiki.vn/lam-sach-da-mat/c11232?sort=top_seller'
pgi_sel = 'data-view-id="product_list_pagination_item"'
for pn in range(1, maxPages+1):
    curPage_xpath = f'//li/a[@class="current"][@{pgi_sel}][@data-view-label="{pn}"]'
    soup = linkToSoup_selenium(nextUrl, ecx=curPage_xpath)
    if soup is None or type(soup) == str: break

    ###################### EXTRACT DATA ######################
    # this is just printing the page# and 1st five IDs, but you can extract whatever you need from soup at this point
    curPg = soup.select_one(f'li > a.current[{pgi_sel}][data-view-label]')
    curPg = f'page {curPg.get("data-view-label")}' if curPg else '!! page ERROR !!'

    pageProds = soup.select('a.product-item[href*=".html?spid="]')
    curPg += f" [{len(pageProds)} products]:"
    first5ids = [a.get('href').split('.html?spid=')[-1] for a in pageProds][:5]
    print(f'{curPg:>22} ', " ".join([f'{i:>10}' for i in first5ids]), '...')
    ##########################################################

    nxtPg = soup.select_one(f'li > a[{pgi_sel}][href]:has(img[alt="arrow-right"])')
    if nxtPg is None or 'disabled' in nxtPg.get('class', ''): break
    nextUrl = nxtPg.get('href')
