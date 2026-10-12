# Code from my Stack Overflow answer https://stackoverflow.com/a/74114732 (posted 2022-10-18), extracted verbatim; may need the question's context to run.

# --- block 1 ---
test = [s for s in soup.find_all('a') if s.get('href')]

#for just the links:
#test = [s.get('href') for s in soup.find_all('a') if s.get('href')]

# --- block 2 ---
print(f'{len(test)} results:\n')
for t in test: print(f'[{t.get_text(strip=True)}]({t.get("href")})')
