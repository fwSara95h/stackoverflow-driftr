# Code from my Stack Overflow answer https://stackoverflow.com/a/74251254 (posted 2022-10-30), extracted verbatim; may need the question's context to run.

# --- block 1 ---
[t.get_text(strip=True) for t in soup.find_all(attrs={'class': 'sorting_1'})]

# --- block 2 ---
[t.get_text(strip=True) for t in soup.find_all(class_='sorting_1')]

# --- block 3 ---
[t.get_text(strip=True) for t in soup.select('.sorting_1')]
