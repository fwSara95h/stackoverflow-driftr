# Code from my Stack Overflow answer https://stackoverflow.com/a/75903974 (posted 2023-04-01), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def get_product_details(prod_soup):
    rkSel = 'span.a-list-item>span.a-text-bold:first-child'
    rkSel = f'div#detailBullets_feature_div {rkSel}'

    pDets = {}
    for r in prod_soup.select(rkSel):
        k = r.get_text(' ', strip=True) 
        v = r.parent.get_text(' ', strip=True).replace(k,'',1).strip() 
        if 'Rank' in k and v[:1]=='#': v = ' • #'.join(v.split(' #'))

        pDets[k.split('\n')[0].strip(':')] = v
    return pDets

# --- block 2 ---
> {'Publisher': 'Matrix Editions (January 1, 2007)',
>  'Language': 'English',
>  'Hardcover': '640 pages',
>  'ISBN-10': '0971576610',
>  'ISBN-13': '978-0971576612',
>  'Item Weight': '2.3 pounds',
>  'Best Sellers Rank': '#7,261,544 in Books ( See Top 100 in Books )',
>  'Customer Reviews': '5.0 out of 5 stars 2 ratings'}
>

# --- block 3 ---
urls_list = [
    'https://www.amazon.com/Atomic-Habits-Proven-Build-Break/dp/0735211299',
    'https://www.amazon.com/Functional-Analysis-Dzung-Ha/dp/0971576610',
    'https://www.amazon.com/Daisy-Jones-Taylor-Jenkins-Reid/dp/1524798649',
    'https://www.amazon.com/Body-Keeps-Score-Healing-Trauma/dp/0143127748',
    'https://www.amazon.com/History-Uncertain-Future-Handwriting/dp/1620402157'
]

# --- block 4 ---
books_list = []
for url in urls_list:
    soup = linkToSoup_scrapingAnt(url)
    # books_list.append(get_product_details(soup)) ## no extra columns

    kList, sList = ['Title','Author'], ['span#productTitle','span.author']
    book_info = { k: t.get_text(' ', strip=True) if t else None for k,t 
                  in zip(kList, [soup.select_one(s) for s in sList])    }
    books_list.append({**book_info, **get_product_details(soup)})

# --- block 5 ---
rkSel = 'ul:first-of-type span.a-list-item>span.a-text-bold:first-child'
rkSel = f'h2+div#detailBullets_feature_div {rkSel}'
