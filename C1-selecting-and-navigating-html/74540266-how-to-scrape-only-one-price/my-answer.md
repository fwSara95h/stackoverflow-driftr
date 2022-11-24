---
title: "How to scrape only one price?"
site: stackoverflow
question_id: 74540266
answer_id: 74559147
url: https://stackoverflow.com/a/74559147
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-24T10:22:28Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74559147/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fe5edf935ca0fa498e28748f76a20845a663d2e863dacb80c80f0af7647e131d
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-24

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74559147>, 2022-11-24; score 0. Text as retrieved 2026-10-12.

You can filter out the other prices [using CSS selectors](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors)
```python
# filsel = 'span.price-tag-fraction:not(span.ui-search-installments span):not(s.price-tag__disabled span)'
emiSp_sel = 'span.ui-search-installments span' # monthly
disab_sel = 's.price-tag__disabled span' # crossed out
filsel = f'span.price-tag-fraction:not({emiSp_sel}):not({disab_sel})'

pri = [p.get_text() for p in soup.select(filsel)]
``` 
or using [`lambda`](https://www.w3schools.com/python/python_lambda.asp) with `find`
```python
pri = soup.find_all(
    lambda p: p.name == 'span' and 'price-tag-fraction' in p.get('class', '')
    and p.find_parent('span', {'class': 'ui-search-installments'}) is None
    and p.find_parent('s', {'class': 'price-tag__disabled'}) is None
)
```
or even by combining [lists comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp) with your current method
```python
pri = [
    p for p in soup.find_all('span',class_ ="price-tag-fraction") 
    if p.find_parent('span', {'class': 'ui-search-installments'}) is None
    and p.find_parent('s', {'class': 'price-tag__disabled'}) is None
]
```
