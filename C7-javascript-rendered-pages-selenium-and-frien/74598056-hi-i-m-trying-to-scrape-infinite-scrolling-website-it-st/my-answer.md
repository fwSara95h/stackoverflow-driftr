---
title: "Hi. I'm trying to scrape infinite scrolling website. It stuck in 200th data"
site: stackoverflow
question_id: 74598056
answer_id: 74631249
url: https://stackoverflow.com/a/74631249
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-30T16:40:53Z
last_edited: 2022-12-01T12:29:04Z
revisions: 3
revision_history: https://stackoverflow.com/posts/74631249/revisions
accepted: true
score: 1
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: [getUniqLinks, row-dict builders]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5a19366ece26031b2ec5f7d85199d3205de0e3275c4053579b39cab9dbc32562
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-30

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74631249>, 2022-11-30, last edited 2022-12-01; **accepted**; score 1. Text as retrieved 2026-10-12.

A cause of duplicates is that every time you get `lnks`, you're getting the products you scraped before scrolling as well. You can probably skip duplicate scrapes by initiating `scrapedUrls = []` somewhere at the beginning of your code (OUTSIDE of all loops), and then checking `urel` against it, as well as adding to it
```python
        if urel in scrapedUrls: continue ## add this line
        result = requests.get(urel) ## from your code
        scrapedUrls.append(urel) ## add this line
```
but I'm not sure it'll solve your issue.

---

I don't know *why* it's happening, but when I try to scrape the links with selenium's `find_elements`, I get the same url over and over; so I wrote [a fuction [`getUniqLinks`]](https://pastebin.com/b3gwUAJZ) that you can use to get a unique list of links (`prodUrls`) by scrolling up to a certain number of times and then parsing `page_source` to `BeautifulSoup`. Below are two lines from the printed output of `prodUrls = getUniqLinks(fullUrl, rootUrl, max_scrolls=250, tmo=1)`:
```lang-none
WITH SELENIUM found 10957 product links [1 unique] 
 
PARSED PAGE_SOURCE  --->  found   12583 product links   [12576 unique]
```
(The full function and printed output are at [https://pastebin.com/b3gwUAJZ](https://pastebin.com/b3gwUAJZ).)

Some notes:
- If you increase `tmo`, you can increase `max_scrolls` too, but it starts getting quite slow after 100 scrolls.
- I used selenium to get links as well, just to print and show the difference, but you can remove all lines that end with `# remove` to get rid of those unnecessary parts.
- I used [selenium's `WebDriverWait`](https://selenium-python.readthedocs.io/waits.html#explicit-waits) instead of `time.sleep` because it stops waiting after the relevant elements have loaded - it raises an error if it doesn't load it the allowed time (`tmo`), so I found it more convenient and readable to use in a `try...except` block instead of using [`driver.implicitly_wait`](https://selenium-python.readthedocs.io/waits.html#implicit-waits)
- I don't know if this is related to whatever is causing your program to hang [since mine is probably just because of the number of elements being too many], but mine also hangs if I try to use selenium to get all the links after scrolling instead of adding to `prodLinks` in chunks inside the loop.

---

Now, you can loop through `prodUrls` and get the data you want, but I think it's better to build a list with a separate dictionary for each link [i.e., having a dictionary for each row rather than having a separate list for each column].

If you use [these two functions](https://pastebin.com/hKXYetmj), then you just have to prepare a reference dictionary of selectors like
```python
refDict = {
    'title': 'h1.js-lot-title',
    'price_text': 'div.price-container',
    'price_amt': 'div.price-container > .price span.price-val',
    'price_cur': 'div.price-container > .price span.price-cur',
    '.lot-text tr.property': {'k':'td.property-name', 'v':'td.property-value'},
    'contact_name': '.author > div.name',
    'contact_phone': '.author > a.phone',
    'lot_warning': 'div.lot-warning',
    'div.lot-info': {'sel': 'p', 'sep': ':'},
    'description': '.lot-text p'
}
```
that can be passed to `fillDict_fromTag` like in the code below:
```python
## FIRST PASTE FUNTION DEFINITIONS FROM https://pastebin.com/hKXYetmj

productDetails = []
puLen = len(prodUrls)
for pi, pUrl in enumerate(prodUrls[:500]):
    print('', end=f'\rScraping [for {pi+1} of {puLen}] {pUrl}')
    pDets = {'prodId': [w for w in pUrl.split('/') if w][-1]}

    resp = requests.get(pUrl)
    if resp.status_code != 200:
        pDets['Error_Message'] = f'{resp.raise_for_status()}'
        pDets['sourceUrl'] = pUrl
        productDetails.append(pDets) 
        continue
    
    pSoup = BeautifulSoup(resp.content, 'html.parser')
    pDets = fillDict_fromTag(pSoup, refDict, pDets, rootUrl)

    pDets['sourceUrl'] = pUrl
    productDetails.append(pDets)
print()
prodDf = pd.DataFrame(productDetails).set_index('prodId')
prodDf.to_csv('ProductDetails.csv')
```

---

I have uploaded both ['prodLinks.csv' and 'ProductDetails.csv' here](https://docs.google.com/spreadsheets/d/1dw-BNMv1DH0qGj2lNpPTdnmdwfH2XbUEjMos_oCa4sI/edit?usp=sharing), although there are only the first 500 scrapes' results since I manually interrupted after around 20 minutes; I'm also pasting the first 3 rows here (printed with `print(prodDf.loc[prodDf.index[:3]].to_markdown())`)
```lang-none
|   prodId | title                                                    | price_text   | price_amt   | price_cur   | Şəhər   | Elanın tipi    | Elanın tipi [link]                                              | Binanın tipi   | Binanın tipi [link]                                             |   Sahə, m² |   Otaq sayı | Yerləşmə yeri   | contact_name   | contact_phone   | lot_warning                                                                  |   Elanın nömrəsi |   Baxışların sayı | Yeniləndi      | description                                                                                                                                                                                                                                                                                                                                                                    | sourceUrl                                                |
|---------:|:---------------------------------------------------------|:-------------|:------------|:------------|:--------|:---------------|:----------------------------------------------------------------|:---------------|:----------------------------------------------------------------|-----------:|------------:|:----------------|:---------------|:----------------|:-----------------------------------------------------------------------------|-----------------:|------------------:|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------|
| 35828514 | 2-otaqlı yeni tikili kirayə verilir, 20 Yanvar m., 45 m² | 600 AZN      | 600         | AZN         | Bakı    | Kirayə verilir | https://tap.az/elanlar/dasinmaz-emlak/menziller?p%5B740%5D=3724 | Yeni tikili    | https://tap.az/elanlar/dasinmaz-emlak/menziller?p%5B747%5D=3849 |         45 |           2 | 20 Yanvar m.    | Elşad Bəy      | (055) 568-12-13 | Diqqət! Beh göndərməmişdən öncə sövdələşmənin təhlükəsiz olduğuna əmin olun! |         35828514 |               105 | 22 Noyabr 2022 | 20 Yanvar metrosuna və Inşatcılar metrosuna 8 - 11 dəiqqə arası olan ərazidə, yeni tikili binada 1 otaq 2 otaq təmirli şəraitiynən mənzil kirayə 600 manata, ailiyə və iş adamına verilir. Qabaqçadan 2 ay ödəniş olsa kamendant pulu daxil, ayı 600 manat olaçaq, mənzili götūrən şəxs 1 ayın 20 % vasitəciyə ödəniş etməlidir. Xahìş olunur, rial olmuyan şəxs zəng etməsin. | https://tap.az/elanlar/dasinmaz-emlak/menziller/35828514 |
| 35833080 | 1-otaqlı yeni tikili kirayə verilir, Quba r., 60 m²      | 40 AZN       | 40          | AZN         | Quba    | Kirayə verilir | https://tap.az/elanlar/dasinmaz-emlak/menziller?p%5B740%5D=3724 | Yeni tikili    | https://tap.az/elanlar/dasinmaz-emlak/menziller?p%5B747%5D=3849 |         60 |           1 | Quba r.         | Orxan          | (050) 604-27-60 | Diqqət! Beh göndərməmişdən öncə sövdələşmənin təhlükəsiz olduğuna əmin olun! |         35833080 |               114 | 22 Noyabr 2022 | Quba merkezde her weraiti olan GUNLUK KIRAYE EV.Daimi isti soyuq su hamam metbex wifi.iwciler ve aile ucun elveriwlidir Təmirli                                                                                                                                                                                                                                                | https://tap.az/elanlar/dasinmaz-emlak/menziller/35833080 |
| 35898353 | 4-otaqlı mənzil, Nizami r., 100 m²                       | 153 000 AZN  | 153 000     | AZN         | Bakı    | Satılır        | https://tap.az/elanlar/dasinmaz-emlak/menziller?p%5B740%5D=3722 | Köhnə tikili   | https://tap.az/elanlar/dasinmaz-emlak/menziller?p%5B747%5D=3850 |        100 |           4 | Nizami r.       | Araz M         | (070) 723-54-50 | Diqqət! Beh göndərməmişdən öncə sövdələşmənin təhlükəsiz olduğuna əmin olun! |         35898353 |                71 | 27 Noyabr 2022 | X.Dostluğu metrosuna 2 deq mesafede Leninqrad lahiyeli 9 mərtəbəli binanın 5-ci mərtəbəsində 4 otaqlı yaxsi temirli mənzil satılır.Əmlak ofisinə ödəniş alıcı tərəfindən məbləğin 1%-ni təşkil edir.                                                                                                                                                                           | https://tap.az/elanlar/dasinmaz-emlak/menziller/35898353 |
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Rasim Dilbani](https://stackoverflow.com/users/20316348)** (2022-12-01): @Drift95 Firstly Thank you so much. How did you get Product detail 'ProductDetails.csv' just have links and code, which is in https://pastebin.com/b3gwUAJZ just gave links. Could you please  share code which's output is product details.
- **[Rasim Dilbani](https://stackoverflow.com/users/20316348)** (2022-12-01): I want to get details always but every time I had to get detail by detail. Is there any way to do it just having all details in that way.If you advice me some videos or readings about that I would be happy. @Driftr95
- **[Rasim Dilbani](https://stackoverflow.com/users/20316348)** (2022-12-01): So sorry, I did not see you pasted it actually. So thanks again.
