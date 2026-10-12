# Code from my Stack Overflow answer https://stackoverflow.com/a/74559147 (posted 2022-11-24), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# filsel = 'span.price-tag-fraction:not(span.ui-search-installments span):not(s.price-tag__disabled span)'
emiSp_sel = 'span.ui-search-installments span' # monthly
disab_sel = 's.price-tag__disabled span' # crossed out
filsel = f'span.price-tag-fraction:not({emiSp_sel}):not({disab_sel})'

pri = [p.get_text() for p in soup.select(filsel)]

# --- block 2 ---
pri = soup.find_all(
    lambda p: p.name == 'span' and 'price-tag-fraction' in p.get('class', '')
    and p.find_parent('span', {'class': 'ui-search-installments'}) is None
    and p.find_parent('s', {'class': 'price-tag__disabled'}) is None
)

# --- block 3 ---
pri = [
    p for p in soup.find_all('span',class_ ="price-tag-fraction") 
    if p.find_parent('span', {'class': 'ui-search-installments'}) is None
    and p.find_parent('s', {'class': 'price-tag__disabled'}) is None
]
