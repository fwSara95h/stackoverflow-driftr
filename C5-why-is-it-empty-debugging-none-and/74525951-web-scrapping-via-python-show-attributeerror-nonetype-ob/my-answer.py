# Code from my Stack Overflow answer https://stackoverflow.com/a/74571807 (posted 2022-11-25), extracted verbatim; may need the question's context to run.
product = {
    'title': title.full_text.strip() if title else 'DEFAULT_TITLE',
    'price': price[0].full_text.strip() if price else 'DEFAULT_PRICE', # remove [0] from find as well
    'tag': tag.full_text.strip() if tag else 'DEFAULT_TAG',
    'sku': sku.full_text.strip() if sku else 'DEFAULT_SKU',
}
