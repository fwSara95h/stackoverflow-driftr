---
title: "AttributeError: 'list' object has no attribute 'absolute_links'"
site: stackoverflow
question_id: 74929017
answer_id: 74990544
url: https://stackoverflow.com/a/74990544
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-03T08:06:57Z
last_edited: 2023-01-03T08:15:24Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74990544/revisions
accepted: false
score: 0
chapter: C9
chapter_title: "Blocked requests: headers, Cloudflare, scraping services"
cluster: scrape-blocked-headers-antibot
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b57719def0808a409288bd3b3d049f95b9529340823f6e594762d5509311e4fd
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-03

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74990544>, 2023-01-03, last edited 2023-01-03; score 0. Text as retrieved 2026-10-12.

> But can I solve captcha and logging via requests-html library? I'm not super familiar with requests-html library

Neither am I, but you can paste the request from your browser to https://curlconverter.com/ (they also [have instructions](https://i.sstatic.net/RgrHp.png) on how to copy the request) and they'll convert it to python code for a request with headers and cookies that you can then paste into your code. The last line of their code will be *`response = requests.get(.....`*, but you can replace it with *`r = s.get(...`* so that your code can still use `requests_html` methods like `.html.render` and `.absolute_links` (`requests` doesn't parse the HTML).

Just keep in mind that the **cookies will expire**, likely within a few hours, and that you'll have to copy them from your browser again by then if you want to keep scraping this way.

---

> ```python 
> for item in product.absolute_links: 
> AttributeError: 'list' object has no attribute 'absolute_links' 
> ```

You can only apply `.absolute_links` to an *element* and [`.find`](https://requests.readthedocs.io/projects/requests-html/en/latest/#requests_html.Element.find) returns a *list* of elements (unless you specify `first=True`). Also `.absolute_links` returns a [set](https://www.w3schools.com/python/python_sets.asp) of links [even when that set only contains one link], so you need to either loop through them or convert to list and access it through indexing to get at the link/s.

```python
product = r.html.find('div.mb1.ph1.pa0-xl.bb.b--near-white.w-25')

productinfo = []
for prod in product:
    item = prod.absolute_links # get product link/s
    # ra = s.get(list(item)[0]) # go to first product link
    # name = ra.html.find('h1',first=True).text
    products = {'link' :item, }
    productinfo.append(products)
```

or, to absolutely ensure that you're looping through a *unique* urls,

```python
product = r.html.find('div.mb1.ph1.pa0-xl.bb.b--near-white.w-25')
prodUrls = set().union(*[d.absolute_links for d in product]) # combine all sets of product links

productinfo = []
for item in prodUrls:
    # ra = s.get(item) 
    # name = ra.html.find('h1',first=True).text
    products = {'link' :item, }
    productinfo.append(products)
```

---

Btw, if it doesn't *find* any products, then ofc you won't get any links even if the error goes away, so add a line to print the request status (in case something went wrong there) as well as how many products and links were extracted.

```python
print(r.status_code, r.reason, f' - {len(product)} products and {len(prodUrls)} product links from', r.url)
```
