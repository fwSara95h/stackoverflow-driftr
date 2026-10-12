# Code from my Stack Overflow answer https://stackoverflow.com/a/74150032 (posted 2022-10-21), extracted verbatim; may need the question's context to run.

# --- block 1 ---
blockSel = '#search div[eid] div[data-hveid][data-ved] > div[data-hveid]'
# blockSel = '#main > div > div > a'
soup.select(blockSel)

# --- block 2 ---
# selectors for headerless request in comments

blockSel = '#search div[eid] div[data-hveid][data-ved] > div[data-hveid]'
# blockSel = '#main > div > div > a'

innerSels = {
    'heading': 'div[role="heading"]', # 'h3',
    'link': (None, 'href'), # (None, 'href'),
    'snippet': 'div[role="heading"] + div', # '"parent"a > div + div',
    'date': 'div[role="heading"] ~ span + div', # 'div + div div > span',
    'site_name': 'g-img + span' # 'h3 + div'
}  

articles = []

srSectn = soup.select(blockSel)
srsLen = len(srSectn)
for i, s in enumerate(srSectn): 
    if s.select_one('a[jsname]'): s = s.select_one('a[jsname]')
    print('', end=f'\radding article {i+1} of {srsLen}...')

    aData = {}
    for k in innerSels:
        sel = innerSels[k]
        target = '"text"'
        if type(sel) in [tuple, list] and len(sel) > 1:
            target = None if sel[1] is None else str(sel[1])
            sel = None if sel[0] is None else str(sel[0])

        if type(sel) == str and sel.startswith('"parent"'): 
            sel = s.parent.select_one(sel.replace('"parent"', '', 1))
        else: 
            sel = s if sel is None else s.select_one(sel)
        if sel is None:
            aData[k] = None
            continue

        if target is None: 
            aData[k] = str(sel)
        elif target == '"text"': 
            aData[k] = sel.get_text(strip=True)
        else: aData[k] = sel.get(target)

    articles.append(aData)

print(f'\radded {len(articles)} articles from {srsLen} sections')
