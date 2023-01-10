---
title: "Why when extracting products data shows me that they are duplicate?"
site: stackoverflow
question_id: 75073129
answer_id: 75074128
url: https://stackoverflow.com/a/75074128
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-10T18:08:09Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75074128/revisions
accepted: true
score: -1
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d9e74f85c0838edb93540b16dd477821c90c35cb50642763b2a39086fc617714
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-10

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75074128>, 2023-01-10; **accepted**; score -1. Text as retrieved 2026-10-12.

> ```python
>     for i in range(len(brand)):
>         brands.append(brand[i].text)
>         filelist = ([titles, brands, prices, rates, rate_starts, productlink])
>         exported = zip_longest(*filelist)
>         with open('oo.csv', 'w' , encoding ='utf-8-sig' , newline='') as filecsv:
>             wr = csv.writer(filecsv)
>             wr.writerow(['title','brands','price','offer','rate','rate_starts','productlink'])
>             wr.writerows(exported)
> ```

Why are you saving in the the loop? the only thing that should be in that loop is `brands.append(brand[i].text)` - you're copying all the products all over again for every brand. That's most likely the reason for the duplicates; but there are several other issues with your method...

---

> ```python
>         except: title='non'
> ```
> ```python
>         except: price = 'non'
> ```
> ```python
>         except: offer='non'
> ```
> ```python
>         except: rate = 'non'
> ```
> ```python
>         except: rate_start = 'non'
> ```


You should be appending in except too, otherwise you'll have uneven and misaligned columns (like say product1 had no offer but product2 did. but you didn't append anything for product1's offer so product2's offer will be the first offer in the list. then when you form the DataFrame, it'll look like product1 had that offer since it will be in the first row, and so on.) 

---

> ```python
>     brand = productlist.find_all('h3', class_='brand-product mb-1')
>     for i in range(len(brand)):
>         brands.append(brand[i].text)
> ```

You can just do `brands = [brand.text for brand in productlist.find_all('h3', class_='brand-product mb-1')]` instead of appending on a loop, but it would be better if you had a surer way to make sure that the links and brands aligned perfectly - why don't you just get it in the *`for link in productlink...`* loop? 

```python
    # for link in productlink:
        # r = requests.get(link , headers=headers)
        # soup = BeautifulSoup(r.content,'lxml')

        # brand = soup.find(lambda t: t.name=='a' and t.parent.name=='h2')`)
        brand = soup.select_one('h2>a')
        brands.append(brand.text.strip() if brand else 'non')
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[CrazyChucky](https://stackoverflow.com/users/12975140)** (2023-01-10): All those `except`s are bare, too. Anything could trigger them.
