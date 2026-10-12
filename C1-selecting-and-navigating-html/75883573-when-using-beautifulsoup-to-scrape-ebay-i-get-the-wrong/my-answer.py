# Code from my Stack Overflow answer https://stackoverflow.com/a/75884306 (posted 2023-03-30), extracted verbatim; may need the question's context to run.

# --- block 1 ---
print(soup.select_one('ul.srp-results li span.s-item__price'))

# --- block 2 ---
print(soup.find(lambda s: s.name=='span' and 's-item__price' in s.get('class',[]) and s.find_parent(lambda p: p.name=='li' and p.find_parent('ul', {'class':'srp-results'}))))
