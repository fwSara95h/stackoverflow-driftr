# Code from my Stack Overflow answer https://stackoverflow.com/a/75645927 (posted 2023-03-05), extracted verbatim; may need the question's context to run.

# --- block 1 ---
item_links = [i.find(href=True)['href'] for i in soup.select('item.sale-item:has([href])')]

# --- block 2 ---
for item in soup.select('item.sale-item:has([href])'):
    item_link = item.find(href=True)['href'] # item.select_one('[href]')['href']
    ## WHATEVER YOU WANT TO DO WITH item AND item_link ##

# --- block 3 ---
for item in soup.find_all('item', class_="sale-item"): # soup.select('item.sale-item'):
    item_link = item.find(href=True) ## no Tags with href in item --> item_link=None
    if item_link: item_link = item_link['href']
    ## WHATEVER YOU WANT TO DO WITH item AND item_link ##
