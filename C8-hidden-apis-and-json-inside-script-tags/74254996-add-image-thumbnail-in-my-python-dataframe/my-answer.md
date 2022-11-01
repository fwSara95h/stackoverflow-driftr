---
title: "Add Image/thumbnail in my python dataframe"
site: stackoverflow
question_id: 74254996
answer_id: 74270958
url: https://stackoverflow.com/a/74270958
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-01T02:38:37Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74270958/revisions
accepted: false
score: 0
chapter: C8
chapter_title: "Hidden APIs and JSON inside script tags"
cluster: scrape-json-in-script
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 941260d8931c9680a2f9a1e8a7d71751af0238ae3422d7b165a06b4c1472321b
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-01

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74270958>, 2022-11-01; score 0. Text as retrieved 2026-10-12.

Assuming that `i` is an imdb movie url (the kind that starts with `https://www.imdb.com/title`), you can target the `script` tag that [seems to contain][1] a lot of the main information for the movie - you can get that with 
```python
# import json
image_url = json.loads(soup.select_one('script[type="application/ld+json"]').text)['image']
```
or, if we're more cautious:
```python
# import json

scCont = [s.text for s in soup.select('script[type="application/ld+json"]') if '"image"' in s.text]
if scCont:
    try:
        scCont = json.loads(scCont[0])
        if 'image' not in scCont: 
            image_url = None
            print('No image found for', i)
        else: image_url = scCont['image']
    except Exception as e: 
        image_url = None
        print('Could not parse movie info for', i, '\n', str(e))
else:
    image_url = None
    print('Could not find script with movie info for', i)
```
(and you can get the trailer thumbnail with `scCont['trailer']['thumbnailUrl']`)

This way, instead of raising an error if anything on the path to the expected info is unavailable, it will just add `image_url` as `None`; if you *want* it to halt and raise error in such cases, use the first version.

<hr>

and then after the loop you can add in the column with something like
```python
df_database_url['image_urls'] = images
```
(you probably know that...)

  [1]: https://i.sstatic.net/vgICs.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[rufina_mar](https://stackoverflow.com/users/20373110)** (2022-11-04): Thank you for the answer. I managed to do it :D
