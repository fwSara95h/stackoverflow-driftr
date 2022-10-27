---
title: "want to scrap image urls from json data"
site: stackoverflow
question_id: 74214571
answer_id: 74215563
url: https://stackoverflow.com/a/74215563
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-27T00:35:05Z
last_edited: 2022-10-28T03:27:36Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74215563/revisions
accepted: false
score: 0
chapter: C3
chapter_title: "Links, attributes, images and downloads"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 238d6ab4172ffcb17f4ff4027562783af216f9800d2e7460fff568a6fbc1dacf
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-27

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74215563>, 2022-10-27, last edited 2022-10-28; score 0. Text as retrieved 2026-10-12.

Instead of
```python
link = data['product']['response']['product']['data']['attributes']['media_map']
```
have
```python
mediaMap = data['product']['response']['product']['data']['attributes']['media_map']
```

Then you can extract you want from `mediaMap`

If you want the alts:

```python
mediaAlts = [m['alt'] for m in mediaMap.values() if 'alt' in m]
```
(just get `mediaAlts[0]` if you only want the first one)

Or if you want only the *image* alts:
```python
imgAlts = [
    m['alt'] for m in mediaMap.values() if 'alt' in m 
    and 'type' in m and m['type'] == 'image'
]
```

<br>

If you want all the src links in the **first** object in media_map:
```python
m1srcs = list(list(mediaMap.values())[0]['src'].values())
```
To filter down to only jpg:
```python
m1srcs = [s for s in m1srcs if type(s) == str and s.endswith('.jpg')]
```

<hr><hr>

**EDIT:**

For all jpgs of images with alts:

```python 
altJpgs = [
    src for srcs in [[
            s for s in mv['src'].values()
            if type(s) == str and s.endswith('.jpg')
        ] for mv in mediaMap.values()
        if type(mv) == dict and 'src' in mv
        and 'alt' in mv # has alt
        and 'type' in mv and mv['type'] == 'image' # has type listed as image 
    ] for src in srcs
]
```

or maybe for-loops are more readable than  list comprehension in this case:

```python 
altJpgs = []

for mv in mediaMap.values():
    if type(mv) != dict or 'src' not in mv: continue 
    if 'alt' not in mv: continue 
    if 'type' not in mv and mv['type'] != 'image': continue 

    for s in mv['src'].values():
        if type(s) == str and s.endswith('.jpg'):
            altJpgs.append(s)
```

<br>

(Edit or remove any of the `if...` lines to adjust the filter)

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[babar akhter](https://stackoverflow.com/users/16720394)** (2022-10-27): thanks ,,, ```m1srcs = list(list(mediaMap.values())[0]['src'].values())``` its only getting back the value of "b" not all src in nested json ,,, actually i only want all jpg from all "src"
- **[babar akhter](https://stackoverflow.com/users/16720394)** (2022-10-27): some products have jpg in "c" , or even some products have in "AZ" so i will have to grab all jpg files from all src
- **me** (2022-10-28): (I did mention that m**1**srcs was just for the *first* object...) I've added an edit with how you might get srcs from all the objects, but I should probably warn you that I typed it on my phone - so watch out for typos/syntax errors 😅
- **[babar akhter](https://stackoverflow.com/users/16720394)** (2022-11-03): extremly thankfull dear ,, its working and save alot of time
