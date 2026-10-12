# Code from my Stack Overflow answer https://stackoverflow.com/a/74990544 (posted 2023-01-03), extracted verbatim; may need the question's context to run.

# --- block 1 ---
> for item in product.absolute_links: 
> AttributeError: 'list' object has no attribute 'absolute_links' 
>

# --- block 2 ---
product = r.html.find('div.mb1.ph1.pa0-xl.bb.b--near-white.w-25')

productinfo = []
for prod in product:
    item = prod.absolute_links # get product link/s
    # ra = s.get(list(item)[0]) # go to first product link
    # name = ra.html.find('h1',first=True).text
    products = {'link' :item, }
    productinfo.append(products)

# --- block 3 ---
product = r.html.find('div.mb1.ph1.pa0-xl.bb.b--near-white.w-25')
prodUrls = set().union(*[d.absolute_links for d in product]) # combine all sets of product links

productinfo = []
for item in prodUrls:
    # ra = s.get(item) 
    # name = ra.html.find('h1',first=True).text
    products = {'link' :item, }
    productinfo.append(products)

# --- block 4 ---
print(r.status_code, r.reason, f' - {len(product)} products and {len(prodUrls)} product links from', r.url)
