---
title: "Ebay Scraping, filter out international results, select parents that do not have specific descendants"
site: stackoverflow
question_id: 74673061
answer_id: 74677546
url: https://stackoverflow.com/a/74677546
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-04T14:27:57Z
last_edited: 2022-12-04T17:03:15Z
revisions: 3
revision_history: https://stackoverflow.com/posts/74677546/revisions
accepted: false
score: 1
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: aac86bb88b2d931ec32d999307683d8b61741ff1e1a01f197355d85af71c3860
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-04

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74677546>, 2022-12-04, last edited 2022-12-04; score 1. Text as retrieved 2026-10-12.

>  It has a Span Class for location. This class only exists if the item is from an international seller.

Assuming the class you mean is `s-item__location` you can use [`.select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) with the [`:has`](https://facelessuser.github.io/soupsieve/selectors/pseudo-classes/#has) and [`:not`](https://facelessuser.github.io/soupsieve/selectors/pseudo-classes/#:not) pseudo-classes as below
```python
    iDetSel = 'div[id="srp-river-results"] div.s-item__details'
    # results = soup.select(iDetSel) # --> your current resultset
    results = soup.select(f'{iDetSel}:not(:has(span.s-item__location))')
```
or, if you want to only use `find...`:
```python
    results = soup.find_all(
        lambda r: r.name == 'div' and 
        r.get('class') == ['s-item__details', 'clearfix'] and
        r.find_parent('div', {'class': 'srp-river-results clearfix'}) and
        not r.find('span', {'class': 's-item__location'})
    )
```
(I find the `.select`-with-[CSS-selectors](https://www.w3schools.com/cssref/css_selectors.php) method much more convenient.)

---

As an example:
```python
url = 'https://www.ebay.com/sch/57988/i.html?_from=R40&_nkw=Fjallraven%20nuuk%20parka&LH_Complete=1&LH_Sold=1&_udlo=50&_udhi=600&LH_PrefLoc=1'
soup = BeautifulSoup(requests.get(url).content)

iDetSel = 'div[id="srp-river-results"] div.s-item__details' 
selectors = [
    ('With Location', f'{iDetSel}:has(span.s-item__location)') , 
    ('Without Location', f'{iDetSel}:not(:has(span.s-item__location))')  
] 
for t, sel in selectors:
    print(f'\n\n{t}')
    for r in soup.select(sel):
        print('   ', ' '.join(w for w in r.get_text(' ').split() if w)) # minimize whitespace
```
prints
```lang-none


With Location
    $151.40 Best offer accepted +$16.72 shipping from Lithuania Free returns ​ Sponsored


Without Location
    $349.95 Buy It Now Free shipping ​ Sponsored
    $299.40 Was: Previous Price $499.00 40% off or Best Offer +$29.00 shipping ​ Sponsored
    $425.00 Best offer accepted +$13.45 shipping ​ Sponsored
    $329.99 Buy It Now +$19.99 shipping ​ Sponsored
    $349.30 Was: Previous Price $499.00 30% off or Best Offer +$29.00 shipping ​ Sponsored
    $296.65 Was: Previous Price $349.00 15% off Buy It Now +$20.00 shipping ​ Sponsored
    $339.99 Buy It Now +$17.87 shipping ​ Sponsored
    $361.00 Buy It Now +$10.51 shipping ​ Sponsored
    $202.00 16 bids +$25.05 shipping ​ Sponsored
    $236.00 Buy It Now +$5.99 shipping Extra 15% off ​ Sponsored
    $300.00 or Best Offer +$12.75 shipping ​ Sponsored
    $330.00 or Best Offer +$11.00 shipping ​ Sponsored
    $330.00 Best offer accepted +$11.00 shipping ​ Sponsored
    $289.00 Best offer accepted +$16.75 shipping ​ Sponsored
```

---
---

**Added EDIT:** To only get the first section, you can do
```python
    rsecSel = 'li:not(.srp-river-answer--REWRITE_START ~ li)'
    iDetSel = f'div[id="srp-river-results"] {rsecSel} div.s-item__details'
    results = soup.select(f'{iDetSel}:not(:has(span.s-item__location))')
```
(Although, since the international sellers seem to be in a separate section, the `:not(:has(span.s-item__location))` part might not be necessary...)

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Jose](https://stackoverflow.com/users/20679076)** (2022-12-04): This is great, thanks for all the detail! I have some learning to do for sure! This takes care of the location portion of the results, now I just have to figure out how to remove the "Results matching fewer words" portion. Any tips?
- **me** (2022-12-04): @Jose sorry I missed that part of the q before -  I've added an edit to my answer
- **[Jose](https://stackoverflow.com/users/20679076)** (2022-12-04): Going thru your Added EDIT now...getting a syntaxError in `results = soup.select(f'{iDetSel}`
- **me** (2022-12-04): @Jose sorry, I forgot the `f` a t the beginning of `iDetSel` (which is a formatted string now), I've fixed the edit now
