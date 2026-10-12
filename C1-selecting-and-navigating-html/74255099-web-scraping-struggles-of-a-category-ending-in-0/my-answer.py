# Code from my Stack Overflow answer https://stackoverflow.com/a/74274619 (posted 2022-11-01), extracted verbatim; may need the question's context to run.

# --- block 1 ---
soup = BeautifulSoup(r.content, 'html5lib')

# --- block 2 ---
soup.find_all('div', {'class':'prdt', 'class':'Product'})

# --- block 3 ---
soup.select('div.prdt.Product')
