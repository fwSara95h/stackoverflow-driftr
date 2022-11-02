---
title: "Extract data from Dell Community Forum for a specific date"
site: stackoverflow
question_id: 74292169
answer_id: 74293587
url: https://stackoverflow.com/a/74293587
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-02T17:45:51Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74293587/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 498e83f9021570351bd177b0fe2f88cfe8fe2de540628ee108346228a6d6f3d5
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-02

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74293587>, 2022-11-02; score 0. Text as retrieved 2026-10-12.

You can get the usernames by targeting the `lia-component-message-view-widget-author-username` class

```python
username = doc.find_all('span', attrs={'class':'lia-component-message-view-widget-author-username'})
```
and then include it in `all_data` with an `if` for filtering:
```python
all_data = []
for u, t, d, m in zip(username, time, date, article):
    if d.get_text(strip=True)[1:] == '10-25-2022': 
        all_data.append([
            u.get_text(strip=True) , 
            t.text, 
            d.get_text(strip=True),
            m.get_text(strip=True, separator='\n')
        ])
```

<hr>

Btw, [list comprehension](https://realpython.com/list-comprehension-python/) is a bit faster than appending on loop, and you can just define and fill `all_data` in one statement:

```python
all_data = [[
        u.get_text(strip=True), 
        t.text, 
        d.get_text(strip=True),
        m.get_text(strip=True, separator='\n')
    ] for u, t, d, m in zip(uname, time, date, article)
    if d.get_text(strip=True)[1:] == '10-25-2022'
]
```
