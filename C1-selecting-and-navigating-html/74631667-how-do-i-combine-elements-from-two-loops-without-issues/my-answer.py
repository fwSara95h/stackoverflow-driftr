# Code from my Stack Overflow answer https://stackoverflow.com/a/74632004 (posted 2022-11-30), extracted verbatim; may need the question's context to run.

# --- block 1 ---
for z in zip(titles, prices[::2], prices[1::2]):
    z, lw = list(z), ''
    for i in len(z):
        if i == 0: # title
            z[0] = ' '.join(w for w in z[0].text.split('\n', 1)[-1] if w)
            if '\n' in z[0].text: lw = z[0].text.split('\n', 1)[0]
            continue
        z[i] = z[i].text.replace('$', '').replace('~', '')
    print(','.join(z+[lw]))

# --- block 2 ---
for g in doc.select('div[data-container-game-id]'):
    gameId = g.get('data-container-game-id')
    title = g.select_one('a.title')
    if title: title = ' '.join(w for w in title.text.split() if w)

    price_official = g.select_one('.price-wrap > div:first-child span.price')
    price_lowest = g.select_one('.price-wrap > div:first-child+div span.price')
    if price_official: 
        price_official = price_official.text.replace('$', '').replace('~', '')
    if price_lowest: 
        price_lowest = price_lowest.text.replace('$', '').replace('~', '')

    print(', '.join([title, price_official, price_lowest, gameId]))
