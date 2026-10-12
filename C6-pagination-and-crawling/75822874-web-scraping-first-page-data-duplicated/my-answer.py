# Code from my Stack Overflow answer https://stackoverflow.com/a/75846242 (posted 2023-03-26), extracted verbatim; may need the question's context to run.

# --- block 1 ---
for product in sp.find_all('li', class_='grid__item'):
    title = product.find('div', class_='card__information')
    if title: title = title.find('a')
    price = product.find('span', class_='price-item price-item--regular')
    if title and title:
        data1.append({
            'Name of Product': title.text.strip(), 
            'Selling Price': re.sub(r'\s+', ' ', price.text.strip())
        })

# --- block 2 ---
title_sel,price_sel = 'div.card__information a','span.price-item.price-item--regular'
product_sel = f'li.grid__item:has({title_sel}):has({price_sel})'

data1 += [{
    'Name of Product': product.select_one(title_sel).text.strip(),
    'Selling Price': re.sub(r'\s+', ' ', product.select_one(price_sel).text.strip())
} for product in sp.select(product_sel)]

# --- block 3 ---
>         next_page = sp.find('a', {'class': 'page-link', 'rel': 'next'})
>

# --- block 4 ---
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

# --- block 5 ---
json_url = 'https://bekorganics.myshopify.com/collections/nuts/products.json'
json_data = requests.get(json_url).json()
data1 = [{
    'Name of Product': p['title'], 'Selling Price': f"£{p['variants'][0]['price']}"
} for p in json_data['products']]
