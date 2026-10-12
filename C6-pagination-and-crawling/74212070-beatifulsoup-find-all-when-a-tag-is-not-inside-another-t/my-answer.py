# Code from my Stack Overflow answer https://stackoverflow.com/a/74213323 (posted 2022-10-26), extracted verbatim; may need the question's context to run.

# --- block 1 ---
sel = soup.find_all(['p', 'li', 'dl', 'tr', 'div', re.compile("^h[1-6]$")])
sel = [s for s in sel if not [p for p in sel if p in s.parents]]

# --- block 2 ---
selTags = ['p', 'li', 'dl', 'tr', 'div'] + [f'h{i}' for i in range(1,7)]
sel = soup.find_all(lambda t: t.name in selTags and not t.find_parent(selTags))

# --- block 3 ---
parentMap = {'div':'div', 'p': 'tr'}
for i in range(1,7): parentMap[f'h{i}'] = 'div'
# parentMap = {'div': 'div', 'p': 'tr', 'h1': 'div', 'h2': 'div', 'h3': 'div', 'h4': 'div', 'h5': 'div', 'h6': 'div'}

sel = soup.find_all(
    lambda t: t.name in 
    ['p', 'li', 'dl', 'tr', 'div']+[f'h{i}' for i in range(1,7)]
    and not (
        t.name in parentMap and 
        t.find_parent(parentMap[t.name]) is not None
    )
)
