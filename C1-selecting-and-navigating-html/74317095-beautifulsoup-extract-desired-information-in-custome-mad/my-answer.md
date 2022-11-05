---
title: "BeautifulSoup extract desired information in custome-made list from different html snippets"
site: stackoverflow
question_id: 74317095
answer_id: 74331712
url: https://stackoverflow.com/a/74331712
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-05T21:45:18Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74331712/revisions
accepted: true
score: 1
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 78f9c6e54c6cb6a6f21793295636187939047316616fdbc274a5654d0be2dd14
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-05

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74331712>, 2022-11-05; **accepted**; score 1. Text as retrieved 2026-10-12.

You might just define a list of selectors corresponding to `desired_list`:
```python
selectors = [
    'span.badge.badge-secondary.ng-star-inserted',                                             #badge 
    'span.font-weight-bold span.ng-star-inserted:has(span[translate])',                        #issue 
    'span.font-weight-bold span.ng-star-inserted:last-child',                                  #date 
    'span.font-weight-bold ~ span.ng-star-inserted:-soup-contains(", ")',                      #publisher 
    'span.font-weight-bold ~ span.ng-star-inserted:-soup-contains(", ") + span.ng-star-inserted:-soup-contains(", ")', #city 
    'span.font-weight-bold ~ span.ng-star-inserted:-soup-contains(":")',                       #page 
]
```
and then 
```python
desired_list = [None if s[0] is None else (
    s[0].get_text(' ', strip=True)[2:] if '-soup-contains' in s[1] 
    else s[0].get_text(' ', strip=True)
) for s in [(soup.select_one(sel), sel) for sel in selectors]]
```
should give you what you're looking for.

**Please note that** you *might* need to install and use [html5lib](https://pypi.org/project/html5lib/) parser (which can be a bit slower than lxml)
```python
soup = BeautifulSoup(html, "html5lib") # html_1, html_2, html_3
```
otherwise, [pseudoclasses](https://facelessuser.github.io/soupsieve/selectors/pseudo-classes/) like `:has` and `:-soup-contains` might raise errors or just return nothing. [Although, after installing html5lib, I noticed the selectors started working no matter which parser I used, including lxml...but I *did* need to install html5lib first]

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[farid](https://stackoverflow.com/users/5437090)** (2022-11-07): Dude, I really appreciate your help! I did `pip install html5lib` in my conda workspace and it works with both `lxml` and `html5lib` parsers!
