# Code from my Stack Overflow answer https://stackoverflow.com/a/73932397 (posted 2022-10-03), extracted verbatim; may need the question's context to run.

# --- block 1 ---
tags = soup.find_all([t for t in preString])
for soups in [t for t in tags if t.string]:
    print(preString[soups.name]+soups.string)

# --- block 2 ---
tags = soup.find_all(['h1', 'h2'])
for soups in tags:
    preStr = preString[soups.name] if soups.name in preString else ''
    print(preStr+soups.string)
