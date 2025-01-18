---
title: "Why validate the `href` attribute twice?"
site: stackoverflow
question_id: 79366742
url: https://stackoverflow.com/q/79366742
asked: 2025-01-18T07:49:13Z
asked_by: "OuterTowner"
asked_by_url: https://stackoverflow.com/users/27551345
last_edited: never
tags: [python, web-scraping, beautifulsoup, urllib]
score: 2
views_at_snapshot: 100
answer_count: 1
accepted_answer_id: 79693292
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f0e8f2263d78de77bec1cde67c1abbc0b4a838f0d505af7f0acd4d549b2f1777
---

# Why validate the `href` attribute twice?

Asked by [OuterTowner](https://stackoverflow.com/users/27551345) on Stack Overflow, <https://stackoverflow.com/q/79366742>, 2025-01-18. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I found the following web scraping code in *Web Scraping with Python* by Ryan Mitchel:

```
from urllib.request import urlopen 
from bs4 import BeautifulSoup 
import re 
pages = set() 
def getLinks(pageUrl): 
    global pages 
    html = urlopen("http://en.wikipedia.org"+pageUrl) 
    bsObj = BeautifulSoup(html) 
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")): 
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages: 
            #find new page
                newPage = link.attrs['href'] 
                print(newPage) 
                pages.add(newPage) 
                getLinks(newPage) 
getLinks("")
```

I believe that in the `findAll()` for loop, all tag objects with `href` attributes that meet the criteria have already been retrieved. Why do we still need to check if the object has the `href` attribute afterward?

In my opinion, I think that this line code should be deleted: `if 'href' in link.attrs:` Do I think correctly?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[ouroboros1](https://stackoverflow.com/users/18470692)** (2025-01-18): Yes, I'd say you are correct in thinking that the `if` statement is redundant. `href` inside `bsObj.findAll` already ensures that each `link` will have a "href" attribute. This being study material, I can imagine that the author might have started with explaining this: `['do stuff' for link in bsObj.findAll("a") if 'href' in link.attrs]`, then moved on from there to: `['do stuff' for link in bsObj.findAll("a", href='some pattern') if 'href' in link.attrs]`, failing to delete the redundant `if`. (Using list comprehension here for convenience.) But I don't have access to the book, so who knows.
- **[chitown88](https://stackoverflow.com/users/7752296)** (2025-01-29): He's doing 2 things here. 1) He's getting all the <a> tags. Then he's saying if there are <a> tags, see if it has href attribute, then see if they are unique/new links not already grabbed. So essentially, if there is a `href` in the `<a>` tag, check if that `href` is not in the set `pages` - if it's not, add it. The redundancy part, or that first if statement is making sure to not get an error when it gets to `if link.attrs['href']` - that will throw an exception/will crash is there is no `'href'` attribute. So he only wants that bit to run if it has `['href']`
