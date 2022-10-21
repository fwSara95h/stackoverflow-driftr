---
title: "How to iterate through list of div at a certain level using BeautifulSoup?"
site: stackoverflow
question_id: 74137966
answer_id: 74150032
url: https://stackoverflow.com/a/74150032
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-21T07:18:22Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74150032/revisions
accepted: false
score: 1
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d7f336998160a43fe111344780712412f3f6bfe3ccea7047900c29f14e0a176f
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-21

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74150032>, 2022-10-21; score 1. Text as retrieved 2026-10-12.

As one of the comments mentioned, you can use [CSS selectors](https://www.w3schools.com/cssref/css_selectors.asp) with [`select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors).
For the news section, this should work
```python
blockSel = '#search div[eid] div[data-hveid][data-ved] > div[data-hveid]'
# blockSel = '#main > div > div > a'
soup.select(blockSel)
```

The first version should work for the tree shown in your question, but if you don't use the right headers, the tree from the response can look like
[![enter image description here][1]][1]

as you can see above, there is no `div id="search"` element; in such cases, the commented out selector might work.

<hr>

Sample usage:

```python
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
```
Data collected:
[![enter image description here][2]][2]


  [1]: https://i.sstatic.net/pWr8q.png
  [2]: https://i.sstatic.net/EZNdi.png
