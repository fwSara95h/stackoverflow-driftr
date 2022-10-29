---
title: "Scrape select headings and inner text from a webpage using BeautifulSoup?"
site: stackoverflow
question_id: 74238931
answer_id: 74243113
url: https://stackoverflow.com/a/74243113
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-29T05:52:55Z
last_edited: 2022-11-13T21:18:22Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74243113/revisions
accepted: true
score: 0
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e785e6be654b15e25828b51edd69a5bf66cff732d34fa83634ccf3b0238768df
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-29

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74243113>, 2022-10-29, last edited 2022-11-13; **accepted**; score 0. Text as retrieved 2026-10-12.

I'm not sure I understand exactly how you want your table organized (which paragraphs you want for each heading? are overlaps ok for nested headings?), but the following suggested solution will set a row for each header tag, and then loop through its siblings collecting all `p` tags until it hits another header tag:
```python
from bs4 import BeautifulSoup
import requests
import pandas

website = requests.get('https://venngage.com/blog/landing-page-examples/')
preString =  {'h1': '', 'h2': '\t', 'h3':'\t\t', 'h4':'\t\t\t'}


htagNames = [k for k in preString.keys()]
htags = soup.find_all(htagNames)
# if you want from within a particular section
# htags = soup.select_one('article.post').find_all(htagNames) 

for h in htags:
    pStrings = []
    for tag in h.find_next_siblings(htagNames+['p']): 
        if tag.name == 'p' and tag.string is not None: 
            pStrings.append(tag.string)
        if tag.name in htagNames: break
    
    headingRows.append({
        'headingType': h.name, # 'headingText': h.string, 
        'headingText': preString[h.name] + h.get_text(' ' , strip=True),  
        'paragraphs': '\n'.join(pStrings)
    }) 

# can filter out heading with no paragraphs with
# headingRows = [hr for hr in headingRows if hr['paragraphs']]
        
# save as csv
pandas.DataFrame(headingRows).to_csv('hRows.csv', index=False)
```

or, if you're not sure that the `p` tags you want will share a parent tag with the header, then you can just blindly collect all the paragraphs until the next header:

```python
tags = soup.find_all(htagNames+['p']) 

lastTag = tags[-1]
headingRows = []
hInit = {'headingType': None, 'headingText': None, 'paragraphs': []}
curHeading = dict(hInit) # copy

for i, t in enumerate(tags): 
    if t.name == 'p' and t.string is not None: 
        curHeading['paragraphs'].append(t.string) 
    
    if t.name in preString: 
        curHeading['headingType'] = t.name
        #curHeading['preStr'] = preString[t.name]
        curHeading['headingText'] = preString[t.name] + t.get_text(' ' , strip=True) # + t.string
    
    if t == lastTag or tags[i+1].name in preString:
        # if you want possible paras before 1st heading, remove if condition
        if curHeading['headingType'] is not None :
            curHeading['paragraphs'] ='\n'.join(curHeading['paragraphs'])
            headingRows.append(curHeading)
        
        curHeading = dict(hInit) # copy
        curHeading['paragraphs'] = [] 
```
although, this runs the risk of getting paragraphs from a header-less section below...

<hr>

results will look something like

[![spreadsheet screenshot][1]][1]

[excel automatically hides leading whitespaces, but dw the indents are still there for the headingtext column]

  [1]: https://i.sstatic.net/X7oGN.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Outbound](https://stackoverflow.com/users/20134661)** (2022-11-13): Thanks a ton for this.   This works for some, but for a lot of blog post pages, it fails with the following error  'headingText': preString[h.name] + h.string,  TypeError: can only concatenate str (not "NoneType") to str - - SAMPLE URLS https://www.shopify.com/blog/product-page https://business.tutsplus.com/articles/product-landing-page-examples--cms-32174  Your help would be much appreciated
- **me** (2022-11-13): @Outbound try using `h.get_text(' ' , strip=True)` instead of `h.string` [I didn't consider `h_` tags with other tags nested inside]
- **[Outbound](https://stackoverflow.com/users/20134661)** (2022-11-15): This works awesome. I'm going to try creating a loop to see if I can feed it a list of URLs instead of a single one. Thanks for helping me get this far.
