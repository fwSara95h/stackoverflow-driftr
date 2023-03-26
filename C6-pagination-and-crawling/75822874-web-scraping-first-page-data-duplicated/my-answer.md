---
title: "Web scraping. First page data duplicated"
site: stackoverflow
question_id: 75822874
answer_id: 75846242
url: https://stackoverflow.com/a/75846242
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-26T06:39:20Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75846242/revisions
accepted: false
score: 0
chapter: C6
chapter_title: "Pagination and crawling"
cluster: scrape-pagination-crawling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5a0ca3119cf2f79c38df0ab00fac12fbc8ec02c47b20cad19b6346101c4388fe
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-26

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75846242>, 2023-03-26; score 0. Text as retrieved 2026-10-12.

**Mis-aligned data is a common issue that crops up when you `zip` lists together** without checking whether they are actually aligned with each other. 

> *but instead of showing second page data first page's data duplicated*

It's not just the first page data - **names** from *all* pages are duplicate (not the prices though). Add `print(len(title1), 'titles and', len(sellprice1), 'prices from', url)` just before the ***`for title0, sellprice0 ...`*** loop and you'll see that there are always twice as many items in `title1` as there are in `sellprice1` ([**view screenshot**][1]).

---

Rather than zipping different ResultSets together, it would be better to loop through a single ResultSet of elements that [contain all the data][2] you might want in a row. Something like

```py  
        for product in sp.find_all('li', class_='grid__item'):
            title = product.find('div', class_='card__information')
            if title: title = title.find('a')
            price = product.find('span', class_='price-item price-item--regular')
            if title and title:
                data1.append({
                    'Name of Product': title.text.strip(), 
                    'Selling Price': re.sub(r'\s+', ' ', price.text.strip())
                })
```

or with [`.select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) and [list comprehension](https://www.programiz.com/python-programming/list-comprehension):

```py
        title_sel,price_sel = 'div.card__information a','span.price-item.price-item--regular'
        product_sel = f'li.grid__item:has({title_sel}):has({price_sel})'

        data1 += [{
            'Name of Product': product.select_one(title_sel).text.strip(),
            'Selling Price': re.sub(r'\s+', ' ', product.select_one(price_sel).text.strip())
        } for product in sp.select(product_sel)]
```

---

> ```py
>         next_page = sp.find('a', {'class': 'page-link', 'rel': 'next'})
> ```

If you fix this (`.find('a', {'href':True, 'aria-label':"Next page"})`), you can change to a while loop:

```py
    max_pg = None # 2 # 10 # set any limit
    url = f'https://bekorganics.myshopify.com/collections/nuts'

    data1, cur_pg = [], 0
    title_sel,price_sel = 'div.card__information a','span.price-item.price-item--regular'
    product_sel = f'li.grid__item:has({title_sel}):has({price_sel})'
    while url and (cur_pg:=cur_pg+1)<=(max_pg if max_pg is not None else cur_pg): 
        sp = BeautifulSoup((webpage:=requests.get(url)).content, 'html.parser')
        
        data1 += [{
          'Name of Product': product.select_one(title_sel).text.strip(),
          'Selling Price': re.sub(r'\s+', ' ', product.select_one(price_sel).text.strip())
        } for product in sp.select(product_sel)]

        nextPg = sp.find('a', {'href':True, 'aria-label':"Next page"})
        url = 'https://bekorganics.myshopify.com'+nextPg['href'] if nextPg else None
```

---

> *"...FYI you can add "/products.json" to the end of the url to get pretty json back instead of having to parse html..."* - [comment](https://stackoverflow.com/questions/75822874/web-scraping-first-page-data-duplicated#comment133747921_75822874) by [childnick](https://stackoverflow.com/users/11338900/childnick)

Then you don't have to bother with looping through pagination at all.

```py
json_url = 'https://bekorganics.myshopify.com/collections/nuts/products.json'
json_data = requests.get(json_url).json()
data1 = [{
    'Name of Product': p['title'], 'Selling Price': f"£{p['variants'][0]['price']}"
} for p in json_data['products']]
```

---

With any of the above suggestions, the output should look like:

[![opdf1][3]][3]


  [1]: https://i.sstatic.net/fMBke.png
  [2]: https://i.sstatic.net/TlYkq.png
  [3]: https://i.sstatic.net/puFTK.png
