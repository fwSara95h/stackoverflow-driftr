---
title: "Trying to isolate URL suffix's from list of href tags"
site: stackoverflow
question_id: 74723173
answer_id: 74752087
url: https://stackoverflow.com/a/74752087
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-10T10:26:01Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74752087/revisions
accepted: true
score: 0
chapter: C6
chapter_title: "Pagination and crawling"
cluster: scrape-pagination-crawling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a433c6691d9856ba7e138a03f0ddde39697a18bdec3ed0244034f242b9bbbd6a
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-10

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74752087>, 2022-12-10; **accepted**; score 0. Text as retrieved 2026-10-12.

> Is there any way I would be able to isolate the "/scp-xxxx" from each item in the list so I can append it to the parent URL?

If I understand correctly, you want to extract the `href` attribute - for that, you can use [`i.get('href')`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#attributes) (or probably even just `i['href']`). 

---

With [`.select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) and [list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp), you won't even need regex to filter the results:

```python
[a.get('href') for a in crawl.select('*[href*="scp-"]') if 'SCP-' in a.get_text()]
```

would return

```python
['/scp-1512', '/scp-2756', '/scp-002', '/scp-004']
```

---

If you want the parent url attached:

```python
root_url = 'https://PARENT-URL.com' ## replace with the actual parent url

scpLinks = [root_url + l for l, t in list(set([
    (a.get('href'), a.get_text()) for a in crawl.select('*[href*="scp-"]')
])) if 'SCP-' in t]
```

`scpLinks` should return 

```python
['https://PARENT-URL.com/scp-004', 'https://PARENT-URL.com/scp-002', 'https://PARENT-URL.com/scp-1512', 'https://PARENT-URL.com/scp-2756']
```

---

If you want to filter out `param`, add `str(param) not in t` to the filter:

```python
scpLinks = [root_url + l for l, t in list(set([
    (a.get('href'), a.get_text()) for a in crawl.select('*[href*="scp-"]')
])) if 'SCP-' in t and str(param) not in t]
```

if `str(param)` was `'SCP-002'`, then `scpLinks` would be

```python
['https://PARENT-URL.com/scp-004', 'https://PARENT-URL.com/scp-1512', 'https://PARENT-URL.com/scp-2756']
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[MrPigsWorth](https://stackoverflow.com/users/20717275)** (2022-12-10): Thanks for the assistance, got it to work without the `list(set` and am curious what you used them for.
- **me** (2022-12-10): @MrPigsWorth just to get a unique list - I wasn't sure if some links are repeated or not [actually, just `set(...` is enough in this context, but it's become a habit to convert the set back to a list]
