# Code from my Stack Overflow answer https://stackoverflow.com/a/74271340 (posted 2022-11-01), extracted verbatim; may need the question's context to run.

# --- block 1 ---
tags = soup.find_all(True, string="Top Rated Movies")

# --- block 2 ---
tags = soup.find_all(lambda x: x.name and x.text and 'Top Rated Movies' in x.text)

# --- block 3 ---
tags = soup.select(':-soup-contains("Top Rated Movies")')

# --- block 4 ---
tags = [t for t in tags if not [p for p in t.parents if p in tags]]

# --- block 5 ---
tags = [t for t in tags if t.find() is None]

# --- block 6 ---
for t in tags: print(t.name)
