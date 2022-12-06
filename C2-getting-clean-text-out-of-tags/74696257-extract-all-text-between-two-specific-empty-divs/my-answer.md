---
title: "Extract all text between two specific empty divs"
site: stackoverflow
question_id: 74696257
answer_id: 74703790
url: https://stackoverflow.com/a/74703790
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-06T14:00:12Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74703790/revisions
accepted: false
score: 0
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 940736a16d87d684f1195a3f04b320d7834aa6e84175ff85d4ca0bf505833140
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-06

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74703790>, 2022-12-06; score 0. Text as retrieved 2026-10-12.

To get the tags between the last `class ="start"` and first `class ="end"` tags, you can use either [`.select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) with [CSS selectors](https://facelessuser.github.io/soupsieve/selectors/combinators/#general-sibling-combinator) or [`.find_all`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all) with the [`lambda`](https://www.w3schools.com/python/python_lambda.asp) function

```python
from bs4 import BeautifulSoup
pasted_html = '''many<divs></divs>and other tags<div class="start"></div><div>bla bla bla</div><div class="start"></div><div><i><a><span><p>Text I want</p></span></a></i></div><div><p>Text I want</p><p>Text I want</p></div><div class="end"></div><div>bla bla bla</div><div class="end"></div>many<divs></divs>and other tags'''
soup = BeautifulSoup(pasted_html, 'html5lib')
```
<sub>Parsing with `html5lib` is more reliable if using `.select`, but you can use a different parser if you go with `.find`.</sub>

<sub>**Please note that this will not return anything unless the last `.start` comes *before* the first `.end`.**</sub>


<br>

Using `.select`

```python
s, e = 'div.start', 'div.end' 
mTags = soup.select(f'{s}:not(:has(~ {s})) ~ *:not({e}):not({e} ~ *):has(~ {e})')
```
should give you the same ResultSet as when you use `.find_all`

```python
mTags = soup.find_all(
    lambda t: t.find_previous_sibling('div', {'class': 'start'}) and
    not t.find_next_sibling('div', {'class': 'start'}) and
    t.find_next_sibling('div', {'class': 'end'}) and
    not t.find_previous_sibling('div', {'class': 'end'})
)
```
(I prefer `.select` just because the code is shorter.)

---

To extract the text, you can either join the texts from each tag in `mTags`

```python
mText = ' '.join([t.get_text(' ').strip() for t in mTags])
# mText = "Text I want Text I want     Text I want"
```

or you can join the htmls and parse again before using `.get_text` (less efficient)

```python
mText = BeautifulSoup(
    '\n'.join([t.prettify().strip() for t in mTags])
).get_text(' ').strip()
# mText = "Text I want\n     \n \n \n \n \n \n \n  Text I want\n  \n \n  Text I want"
```

---

If you want to minimize whitespace you can do something like
```python
mText = ' '.join(w for w in mText.split() if w)
```
then `mText` should be `"Text I want Text I want Text I want"` no matter which of the above approaches were used.
