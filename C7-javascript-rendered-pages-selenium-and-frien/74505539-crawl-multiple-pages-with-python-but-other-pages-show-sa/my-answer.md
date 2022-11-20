---
title: "Crawl multiple pages with python but other pages show same results as first page"
site: stackoverflow
question_id: 74505539
answer_id: 74512696
url: https://stackoverflow.com/a/74512696
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-20T23:02:30Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74512696/revisions
accepted: false
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: [linkToSoup, linkToSoup_selenium]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c3d058d7079890afbfca3e3b3415edbe5d7b5bdea9a25212ccee22cddd4083e5
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-20

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74512696>, 2022-11-20; score 0. Text as retrieved 2026-10-12.

<sub>Btw, you can specifically check the [actual page number of the html][1] with something like `soup.select_one('li > a.current[data-view-id="product_list_pagination_item"][data-view-label]').get('data-view-label')`.</sub>

**Explanation**: No matter which page you use the link for, it's always the first page that is loaded first, and then the page is updated dynamically (with JavaScript and APIs). You can see this by going to the [network tab on devtools](https://help.searchie.io/en/articles/5342367-access-your-browser-s-console-and-network-logs) [ you might have to refresh page after opening, and make sure that [the "preserve log" option][2] is **not** checked ] and clicking on [the name of] the first request in the log [it should end the same as the link in the address bar] ; the html in the "Response" is what is fetched by `requests.get` - you might notice that [this html is of the first page][3]. 

If you scroll through the other requests in the log, you should find one to 
<sub>[`https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=3dddf2b8-1eb2-e891-0cdf-c23b37663c28&category=11232&page=5&sort=top_seller%3Fpage%3D5&urlKey=lam-sach-da-mat`](https://tiki.vn/api/personalish/v1/blocks/listings?limit=40&include=advertisement&aggregations=2&trackity_id=3dddf2b8-1eb2-e891-0cdf-c23b37663c28&category=11232&page=5&sort=top_seller%3Fpage%3D5&urlKey=lam-sach-da-mat)</sub>

and [the products are probably loaded from this][4]. All of the params PPEr to be fixed, or can be found in the page url, **except for `trackity_id`**; if you look at the [request initiator chain][5], you can see which JavaScript file made the request and you could try to figure out how `trackity_id` is generated; but personally, I'd find it easier to just use [selenium](https://www.scrapingbee.com/blog/selenium-python/).

---

**Suggested Solution 1:** It appears that you can actually use the API with only the params we already know (`category`, `urlKey`, `sort`):
```python
# import cloudscraper
r = cloudscraper.create_scraper().get('https://tiki.vn/api/personalish/v1/blocks/listings?limit=300&category=11232&sort=top_seller%3Fpage%3D5&urlKey=lam-sach-da-mat')
productList = r.json()['data']
print('### [{id}_{sku}: {name}] for first 10 products of', f'{len(productList)} ###\n')
for p in productList[:10]: print(f"{p['id']}_{p['sku']}: {p['name']}")
```
(I used [`cloudscraper`](https://pypi.org/project/cloudscraper/) because I'm not very familiar with `urlopen`, and also I'm not good at setting the right headers with `requests` to avoid 403 errors....) This prints
```lang-none
### [{id}_{sku}: {name}] for first 10 products of 100 ###

33606786_5722576750824: Lotion tẩy tế bào chết làm sáng da Paula’s Choice Skin Perfecting 8% AHA Lotion 100ml 2060
11239286_9792297299199: Gel tẩy da chết Arrahan Lemon White Peeling Gel (180ml)
33606848_8573828662870: Kem tẩy da chết làm trắng sáng và đều màu da Paula’s Choice RESIST Daily Smoothing Treatment With 5% AHA 50 ml - 7660
20525156_3751926198377: Tẩy Tế Bào Chết 3W Clinic Collagen Crystal Peeling Gel 180ml
67089667_9204550497315: Combo 2 chai tiện lợi - Natureine AQUA PEEL Moisture Peeling Gel - Gel tẩy tế bào da chết, cấp ẩm Nhật Bản - Chính Hãng
21481823_9335684703529: Gel tẩy tế bào chết sáng da hồng sâm Hàn Quốc My Gold Korea Red Ginseng Peeling Gel (130ml) – Hàng Chính Hãng
46203526_8584500833846: Bông Tẩy Da Chết Cosrx One-Step Original Clear Pad 70 Sheets (New 2019)
1941543_2999847759227: Kem tẩy tế bào chết mặt Organic Shop Organic Coffee & Powder 75ml
57783000_9733773668061: Natureine AQUA PEEL Moisture Peeling Gel - Gel tẩy tế bào da chết, cấp ẩm Nhật Bản - Chính Hãng
7319657_7325473003642: Trial Tinh chất dành cho da mụn cao cấp Resist BHA 9 0.83 ml
```
However, I feel like there should have been more than just 100 products - paginating with selenium (below) indicated that there should be 177 products.

---

**Suggested Solution 2:** You can loop through the pages using [this function](https://pastebin.com/kEC9gPC8) that I wrote to get and parse html (with selenium + bs4)
```python
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
```
and that printed
```lang-none
 page 1 [40 products]:    66640131   20116852   66638723   20525157   67089668 ...
 page 2 [40 products]:    63465592   20911921   54388844   58555745   13385021 ...
 page 3 [40 products]:     1515345   57703788    1060978   54929902    2076819 ...
 page 4 [40 products]:    35737314   26299382    7029351   14970693   32139853 ...
 page 5 [11 products]:    52274203   51988147   50422842   36828505   45439018 ...
```
(If you don't want to limit to `maxPages`, you can just use something like `while True` instead of `for pn in range(maxPages)`, but then you'll also need to use a counter or something to get `pn` for `ecx`, since that's what tells the function to wait until that part of the html is loaded.)

  [1]: https://i.sstatic.net/kjojd.png
  [2]: https://i.sstatic.net/J2lr8.png
  [3]: https://i.sstatic.net/7ZTbT.png
  [4]: https://i.sstatic.net/a2u3T.png
  [5]: https://i.sstatic.net/6lYlD.png
