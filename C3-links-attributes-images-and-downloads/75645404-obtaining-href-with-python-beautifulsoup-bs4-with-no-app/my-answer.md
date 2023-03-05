---
title: "Obtaining HREF with Python BeautifulSoup (BS4) with no apparent tags"
site: stackoverflow
question_id: 75645404
answer_id: 75645927
url: https://stackoverflow.com/a/75645927
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-05T23:11:40Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75645927/revisions
accepted: true
score: 1
chapter: C3
chapter_title: "Links, attributes, images and downloads"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 36b08266745dbb30bd48e43c78bb2179c2569cbfa03278e96320eec460912212
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-05

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75645927>, 2023-03-05; **accepted**; score 1. Text as retrieved 2026-10-12.

If you just want a list (`item_links` below) of all the first `href`s from inside `item` tags [that have any], you can use [`select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) (with [CSS selectors](https://facelessuser.github.io/soupsieve/selectors/#selector)) and [list comprehension](https://www.programiz.com/python-programming/list-comprehension):

```py
item_links = [i.find(href=True)['href'] for i in soup.select('item.sale-item:has([href])')]
```

---

If you want to loop through `item`s and do more things than just getting links, you can use a `for` loop like:

```py
for item in soup.select('item.sale-item:has([href])'):
    item_link = item.find(href=True)['href'] # item.select_one('[href]')['href']
    ## WHATEVER YOU WANT TO DO WITH item AND item_link ##
```

---

If you want to loop through `item`s regardless of whether they contain any Tags with `href`:

```py
for item in soup.find_all('item', class_="sale-item"): # soup.select('item.sale-item'):
    item_link = item.find(href=True) ## no Tags with href in item --> item_link=None
    if item_link: item_link = item_link['href']
    ## WHATEVER YOU WANT TO DO WITH item AND item_link ##
```

---

These will find the first `href`s no matter the kind of Tag the attribute belongs to.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[walksonair](https://stackoverflow.com/users/15696430)** (2023-03-07): Thank you! This is why I ask as I'm thinking I haven't begun scratching what can really be done w BS4. Documentation is great and all but somehow I miss it. Thanks for your help again!
