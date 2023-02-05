---
title: "Creating dataframe from XML file with non-unique tags"
site: stackoverflow
question_id: 75346930
answer_id: 75350849
url: https://stackoverflow.com/a/75350849
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-05T08:03:32Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75350849/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 56307b93c5330c9032903a4143205d19fdc7d3b6eaa4e89e63688381dfb000b4
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-05

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75350849>, 2023-02-05; score 0. Text as retrieved 2026-10-12.

If working with `BeautifulSoup`, I suggest looking into using [`.select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) with [CSS selectors](https://www.w3schools.com/cssref/css_selectors.php) so that you can do something like

```python
# from bs4 import BeautifulSoup

def getXMLdata(xmlFile:str, defaultVal=None):
    with open(xmlFile, 'r') as f: xSoup = BeautifulSoup(f, 'xml')
    selRef = {
        'FileName': 'MediaLocation[sourceType="Primary"] Location',
        'Brand': 'BrandName', 'ID': 'ContentId',
        'URL': 'MediaLocation[sourceType="Proxy"] Location'
    }
    xfDets = {} # {'fromFile': xmlFile} 
    for k, sel in selRef.items():
        t = xSoup.select_one(sel)
        xfDets[k] = t.get_text(' ').strip() if t else defaultVal 

    fn = xfDets.get('FileName')
    if isinstance(fn, str) and '.' in fn:  # remove extensions like ".mp4"
        xfDets['FileName'] = '.'.join(fn.split('.')[:-1])
    return xfDets
```

---

Since I've seen only one example, I can't know for sure if the selectors in `selRef` will apply for *all* your files; but I saved the snippet from your question to a file name `x.xml`, and **`getXMLdata('x.xml')`** returned

```python
{'FileName': 'zzTap_zzTop_AAAA1111999Z_30s_Pill_aa-bb',
 'Brand': 'zzTop',
 'ID': 'AAAA1111999Z',
 'URL': 'https://app.url.com/DMM/DL/wew52f'}
```

---

If you had a list of paths to XML files (let's say `filesList`), you could tabulate their outputs with pandas like

```python
# import pandas
# filesList = ['x.xml', ...] ## LIST OF XML FILES
xDF = pandas.DataFrame([getXMLdata(x) for x in filesList])
```

[![opdf][1]][1]

**<sup>[ If you wanted to save that output to a csv file, you can use [`.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html) like *`xDF.to_csv('xmldata.csv')`*. ]</sup>**

  [1]: https://i.sstatic.net/H8VDw.png
