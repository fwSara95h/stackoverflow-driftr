---
title: "Downloading all Images from a page with beautifulSoup not working"
site: stackoverflow
question_id: 74294192
answer_id: 74332271
url: https://stackoverflow.com/a/74332271
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-05T23:44:38Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74332271/revisions
accepted: true
score: 1
chapter: C8
chapter_title: "Hidden APIs and JSON inside script tags"
cluster: scrape-hidden-api-json
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c6c1eff87237013949acbf7a43cdcc4a4a741d298ab54e52cf38c3871b7f8e86
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-05

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74332271>, 2022-11-05; **accepted**; score 1. Text as retrieved 2026-10-12.

You can try via the api they seem to be using to populate the page
```python
api_url = 'https://apis-edge-prod.tech.tvnz.co.nz/api/v1/web/play/page/categories/sci-fi-and-fantasy'
r = requests.get(api_url)
try:
    embVals = r.json()['_embedded'].values() 
except Exception as e:
    embVals = []
    print('failed to get embedded items\n', str(e))

urls = [img for images in [ [
    v['src'] for k, v in ev.items() if 
    k is not None and 'image' in k.lower() 
    and v is not None and 'src' in v
] for ev in embVals] for img in images]

# for url in urls: # should work the same
```
(Images seem to be in nested dictionaries with keys like 'portraitTileImage', 'image', 'tileImage', 'coverImage'. You can also use for-loop/s to go through `embVals` and extract other data if you want to include more in the filename/metadata/etc.)

I don't know if it will get you ALL the images on the page, but when I tried it, `urls` had 297 links.
