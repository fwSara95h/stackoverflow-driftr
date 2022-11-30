---
title: "How do I combine elements from two loops without issues?"
site: stackoverflow
question_id: 74631667
answer_id: 74632004
url: https://stackoverflow.com/a/74632004
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-30T17:41:29Z
last_edited: 2022-11-30T21:44:18Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74632004/revisions
accepted: false
score: 1
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: [extractAttr/getListingDetails]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: accc675d6edfffea4c868187c17b505c0ab4c9b12e0b4fdb454ec5f078363707
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-30

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74632004>, 2022-11-30, last edited 2022-11-30; score 1. Text as retrieved 2026-10-12.

I feel like all 3 details (title, price_official, price_lowest) are probably all in a shared container. It would be better to loop through these containers and select the details as sets from each container to make sure the wight prices and titles are being paired up, but I can't tell you how to do that without seeing at least a snippet from (or all of) "games.html"....

---

Anyway, assuming that `'110837\nCall of Duty: Modern Warfare II (2022)'` is from the first title here, you can rewrite your last loop as something like:
```python
for z in zip(titles, prices[::2], prices[1::2]):
    z, lw = list(z), ''
    for i in len(z):
        if i == 0: # title
            z[0] = ' '.join(w for w in z[0].text.split('\n', 1)[-1] if w)
            if '\n' in z[0].text: lw = z[0].text.split('\n', 1)[0]
            continue
        z[i] = z[i].text.replace('$', '').replace('~', '')
    print(','.join(z+[lw]))
```

---

**Added EDIT:** After seeing the html, this is my suggested solution:
```python
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
```
prints
```lang-none
Call of Duty: Modern Warfare II (2022), 69.99, 77.05, 153356
Red Dead Redemption 2, 14.85, 13.79, 80011
God of War, 28.12, 22.03, 130187
ELDEN RING, 50.36, 48.10, 119003
Cyberpunk 2077, 29.99, 28.63, 73502
EA SPORTS FIFA 23, 41.99, 39.04, 156474
Warhammer 40,000: Darktide, 39.99, 45.86, 96592
Marvel's Spider-Man Remastered, 30.71, 27.07, 154207
Persona 5 Royal, 37.79, 43.32, 155123
The Callisto Protocol, 59.99, 69.41, 152790
Need for Speed Unbound, 69.99, 42.29, 165013
Days Gone, 15.00, 9.01, 110837
```
<sub>Btw, this might look ok for just four values, but if you have a large amount of details that you want to extract, you might want to consider using [a function like this](https://pastebin.com/BpjZSQPi).</sub>

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Magicskid](https://stackoverflow.com/users/3341926)** (2022-11-30): The HTML file is... https://jsfiddle.net/m3hqy54x/
- **me** (2022-11-30): @Magicskid I see now. I've added an edit. Hope it helps
