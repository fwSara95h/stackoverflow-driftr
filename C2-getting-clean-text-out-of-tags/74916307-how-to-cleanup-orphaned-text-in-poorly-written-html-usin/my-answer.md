---
title: "How to cleanup ‘orphaned’ text in poorly written html using Python?"
site: stackoverflow
question_id: 74916307
answer_id: 74935343
url: https://stackoverflow.com/a/74935343
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-28T00:55:42Z
last_edited: 2022-12-28T13:08:47Z
revisions: 3
revision_history: https://stackoverflow.com/posts/74935343/revisions
accepted: false
score: 0
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d0ec9d2f8375a62aa69a0cb86906d9cfd494db026c0e8e4a05abe1b5b241aee8
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-28

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74935343>, 2022-12-28, last edited 2022-12-28; score 0. Text as retrieved 2026-10-12.

> I've tried BeautifulSoup.prettify() and lxml clean_html() to no avail.

These generally just make sure that the html is valid, so even if you consider it poorly written, they are unlikely to correct anything unless it makes the html invalid.

---

It's probably not most elegant solution, but I think this will do what you're wanting to:

```python
# from bs4 import BeautifulSoup

## just a function I use often to reduce whitespace ##
def miniStr(obj, lineSep=' ', wordSep=' '):
    return lineSep.join(wordSep.join(
        w for w in l.split() if w) for l in str(obj).splitlines() if l.strip())


## the solution ##
def containStrings(inpObj, asHtmlStr=True, tCont='div'): 
    ### initiate [main] container - "fixed" html will be added to this ###
    cDiv = BeautifulSoup('<div></div>', "html.parser").div 

    ### format inputs ###
    tCont = str(tCont) if str(tCont).isalpha() else 'div' # can only contain letters
    if not isinstance(inpObj, type(cDiv)): 
        # parses html strings twice [first time to correct errors - like open tags] 
        inpObj = BeautifulSoup(
            f'<div>{BeautifulSoup(inpObj, "html.parser")}</div>', "html.parser").div
    
    ### loop through input and fill up cDiv ###
    for c in inpObj.children:
        if isinstance(c, str): 
            c = BeautifulSoup(f'<{tCont}>{c}</{tCont}>', "html.parser").find(tCont)
        cDiv.append(BeautifulSoup(c.prettify(), "html.parser").find(c.name))

    return cDiv.prettify()[6:-7] if asHtmlStr else cDiv
```

The input can be a HTML string or a bs4 Tag, and the output can also be either [default output is string - set `asHtmlStr` argument as `False` to get a Tag instead].

Also, the "orphan" strings don't necessarily have to be enclosed in `div` tags - you can specify a different Tag name via the `tCont` argument.

---

For test inputs, I copied your sample lines [into a list](https://i.sstatic.net/HFmRf.png) named `linesList` - see some of the HTMLs after and before being processed by the function:

[![op screencap][1]][1]

The outputs in the above screenshot were printed with:

```python
# the inputs [before processing]
print('\n\n'.join(f'<!--from line{i+1}-->\n'+'\n'.join(
    [miniStr(c, '') for c in BeautifulSoup(l,'html.parser').children]
) for i, l in enumerate(linesList)))
```

```python
# the outputs [after processing]
print('\n\n'.join(f'<!--from line{i+1}-->\n'+'\n'.join(
    [miniStr(c, '') for c in containStrings(l, False).children]
) for i, l in enumerate(linesList)))
```


  [1]: https://i.sstatic.net/ncEcJ.png
