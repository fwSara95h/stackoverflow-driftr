---
title: "Any easy way to extract details from a HTM webpage?"
site: stackoverflow
question_id: 74129022
answer_id: 74132169
url: https://stackoverflow.com/a/74132169
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-19T21:37:24Z
last_edited: 2022-10-19T22:26:22Z
revisions: 3
revision_history: https://stackoverflow.com/posts/74132169/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1f9fb57c62c8388e86bf0464da11b2191e91492c927ac5100bbff7cf479db018
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-19

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74132169>, 2022-10-19, last edited 2022-10-19; score 0. Text as retrieved 2026-10-12.

As you have already realized, the data is added from the `https://www.sec.gov/Archives....` site, and you would need something like selenium to get it from the `https://www.sec.gov/ix?doc=/Archives....` site. 

[The URL I used was [https://www.sec.gov/Archives/edgar/data/1318605/000095017022012936/tsla-20220630.htm][1] and I just copied the cookies and headers from my own browser to pass into the request. I tried to open the link in [your answer](https://stackoverflow.com/a/74130417/12652373), but I got a `NoSuchKey` error...]

*If* you've managed to fetch a html containing 10-Q form, I feel that the simplest way to extract the address would be with [css selectors](https://www.w3schools.com/cssref/css_selectors.asp)
```python
[s.text for s in soup.select('td *[name^="dei:EntityAddress"]')]
```
will return `['1 Tesla Road', 'Austin', 'Texas', '78725']` and so, with
```python
print(', '.join([
    s.get_text(strip=True) for s in 
    soup.select('p>span *[name^="dei:EntityAddress"]')
    if 'ZipCode' not in s.get('name') # excludes zipcode
]))
```
`1 Tesla Road, Austin, Texas` will be printed.

<br>

You can also use 
```python
addrsCell = soup.find(attrs={'name':'dei:EntityAddressAddressLine1'})
if addrsCell and addrsCell.find_parent('td'): # is not None
  print(' '.join([
      s.text for s in addrsCell.find_parent('td').select('p')]))
```
to get `1 Tesla Road Austin, Texas`, which is exactly as you formatted it in your question.


  [1]: https://www.sec.gov/Archives/edgar/data/1318605/000095017022012936/tsla-20220630.htm
