---
title: "Scrape webpage element with text or href criteria simultaneously"
site: stackoverflow
question_id: 74410699
answer_id: 74417369
url: https://stackoverflow.com/a/74417369
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-12T23:32:19Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74417369/revisions
accepted: true
score: 0
chapter: C3
chapter_title: "Links, attributes, images and downloads"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 11262cbbee24c3b0ad420f0553d5d4298715300a5bca22d18c6edff89c8b6074
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-12

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74417369>, 2022-11-12; **accepted**; score 0. Text as retrieved 2026-10-12.

In this particular case, if you have [`html5lib`](https://pypi.org/project/html5lib/) parser, you can use [CSS selectors](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors)
```python
auction_results = soup.select('tr:-soup-contains("3rd Incremental Auction"), tr:has(*[href*="base-residual"])')
```
or, if you want to parametrize it a bit
```python
inText, inAttr = "3rd Incremental Auction", "base-residual"
tag, attr = "tr", "href"
selector = f'{tag}:-soup-contains("{inText}"), tr:has(*[{attr}*="{inAttr}"])'
auction_results = soup.select(selector)
```

---

It's pretty much the same as 
```python
auction_results = soup.find_all(lambda t: t.name == tag and ((
    t.find(lambda c: c.get(attr) and inAttr in c.get(attr)) is not None
) or (t.text and inText in t.text)))
```
It's case-sensitive, but with `find_all`, you can also use `re.search(inText, t.text, re.IGNORECASE | re.DOTALL)` instead of `inText in t.text` (and similarly replace `inAttr in c.get(attr)` as well).

---

It's not a problem in this particular case, but if `tag` is something commonly nested like `div` [or even sometimes with `tr` in nested tables], parent tags with the same name will also be included in `auction_results`; but you can filter those out with
```python
auction_results = [
    ar for ar in auction_results if not 
    [c for c in auction_results if ar in c.parents]
]
```

---
---

Or, you can also put it all in a function so that parent tags also get filtered out in one call with something like `soup.find_all(lambda t: find_results(t, inText , inAttr))`
```python
def checkPat(pat, main): # for convenience
    return True if re.search(pat, main, re.IGNORECASE | re.DOTALL) else False

def find_results(tag, textPat, attrPat, tagName='tr', attrName='href'):     
    if tag.name != tagName: return False  
       
    hasText = checkPat(textPat, tag.text) if tag.text else False
    hasAttr = tag.find(lambda t: t.get(attrName) and checkPat(
        attrPat, t.get(attrName))) is not None
    
    if hasText or hasAttr:
        if not tag.find(lambda t: find_results(t,textPat,attrPat,tagName,attrName)): 
            return True
    return False
```

---

Or, if you'll always be using the same parameters and want to be able to just use something like `soup.find_all(find_auction_results)` without `lambda`
```python
# def checkPat... # as before

def find_auction_results(tag):  
    textPat = "3rd Incremental Auction" 
    attrPat = "base-residual"
    tagName, attrName = "tr", "href"
    
    if tag.name != tagName: return False # has to be tr
       
    hasText = checkPat(textPat, tag.text) if tag.text else False
    hasAttr = tag.find(lambda t: t.get(attrName) and checkPat(
        attrPat, t.get(attrName))) is not None
    
    if hasText or hasAttr:
        # if nested like [ tr -> tr -> a ] , will only allow inner tr
        if not tag.find(find_auction_results): return True
    return False
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[randomrandom123](https://stackoverflow.com/users/19686176)** (2022-11-13): Having all in a function is great. Speed is not important in my code. It has to run once in a month.
- **me** (2022-11-13): @randomrandom123 thanks for letting me know [I actually didn't know before that you could just call `find(method_name)`. I haven't yet needed to target anything I couldn't figure out a selector or `lambda....` expression for, but this opens up so many possibilities!]
