---
title: "Beautiful soup getting the next span element"
site: stackoverflow
question_id: 74331339
answer_id: 74334049
url: https://stackoverflow.com/a/74334049
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-06T07:33:57Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74334049/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0a1750896e0a10663761284b5753202a0eb28bd8ff88afba8fda7a252f742c0e
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-06

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74334049>, 2022-11-06; score 0. Text as retrieved 2026-10-12.

`.next_sibling` gets the next child [from the parent tag], which isn't necessarily a tag. In this case, it's probably an empty [NavigableString](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigablestring). To get the next sibling *Tag*, use [`.find_next_sibling()`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-next-siblings-and-find-next-sibling) instead
```python
html = '''
<br/>
<h4>Dieses Jahr</h4>
<br/>
<span class="parName">Januar:</span> <span class="parValue">143.92 kWh</span> | 
<span class="parName">Diesen Monat:</span> <span class="parValue">67.54 kWh</span> | 
<span class="parName">Februar:</span> <span class="parValue">350.51 kWh</span> | 
'''
BeautifulSoup(html).find("span", string="Diesen Monat:").find_next_sibling()
```
returns `<span class="parValue">67.54 kWh</span>`. 

<hr>

Btw, if you have [html5lib](https://pypi.org/project/html5lib/) parser installed, you can do it with a single `select_one` call
```python
BeautifulSoup(html, 'html5lib').select_one("span:-soup-contains('Diesen Monat:') + span")
```
