---
title: "How to put book information from amazon into a table form?"
site: stackoverflow
question_id: 75900624
answer_id: 75903974
url: https://stackoverflow.com/a/75903974
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-01T02:25:37Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75903974/revisions
accepted: true
score: 1
chapter: C9
chapter_title: "Blocked requests: headers, Cloudflare, scraping services"
cluster: scrape-blocked-headers-antibot
helpers_referenced: [linkToSoup]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7690b2cbcbf6d38f034d65243a018dac601ffb510943bdd6a2e7d768ea1fb556
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-01

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75903974>, 2023-04-01; **accepted**; score 1. Text as retrieved 2026-10-12.

You can build a dictionary by using the `span.a-text-bold`s for keys and the rest of the texts in each `span.a-list-item` as values (like in the function defined below), and that dictionary can be used to form a row in a DataFrame.

```py
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
```

---

For your `link`, `get_product_details(soup)` should return

>```py
> {'Publisher': 'Matrix Editions (January 1, 2007)',
>  'Language': 'English',
>  'Hardcover': '640 pages',
>  'ISBN-10': '0971576610',
>  'ISBN-13': '978-0971576612',
>  'Item Weight': '2.3 pounds',
>  'Best Sellers Rank': '#7,261,544 in Books ( See Top 100 in Books )',
>  'Customer Reviews': '5.0 out of 5 stars 2 ratings'}
>```

and `pd.DataFrame([get_product_details(soup)])` should return [![opdf1][1]][1]

---

You could loop through multiple links to fill multiple rows:

```py
urls_list = [
    'https://www.amazon.com/Atomic-Habits-Proven-Build-Break/dp/0735211299',
    'https://www.amazon.com/Functional-Analysis-Dzung-Ha/dp/0971576610',
    'https://www.amazon.com/Daisy-Jones-Taylor-Jenkins-Reid/dp/1524798649',
    'https://www.amazon.com/Body-Keeps-Score-Healing-Trauma/dp/0143127748',
    'https://www.amazon.com/History-Uncertain-Future-Handwriting/dp/1620402157'
]
```
```py
books_list = []
for url in urls_list:
    soup = linkToSoup_scrapingAnt(url)
    # books_list.append(get_product_details(soup)) ## no extra columns

    kList, sList = ['Title','Author'], ['span#productTitle','span.author']
    book_info = { k: t.get_text(' ', strip=True) if t else None for k,t 
                  in zip(kList, [soup.select_one(s) for s in sList])    }
    books_list.append({**book_info, **get_product_details(soup)})
```

[![opdfmr][2]][2]

---
---

**Note:** If you want only the section covered in the HTML snippet in your question (i.e., without the `Best Sellers Rank` and `Customer Reviews` keys/columns), you can define `rkSel` as

```py
    rkSel = 'ul:first-of-type span.a-list-item>span.a-text-bold:first-child'
    rkSel = f'h2+div#detailBullets_feature_div {rkSel}'
```


  [1]: https://i.sstatic.net/lWStM.png
  [2]: https://i.sstatic.net/9MrCA.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Akira](https://stackoverflow.com/users/7357673)** (2023-04-01): Thank you so much for your detailed answer! It is more than what I asked for :v
