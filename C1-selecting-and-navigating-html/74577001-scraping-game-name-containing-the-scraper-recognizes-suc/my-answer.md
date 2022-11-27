---
title: "Scraping game name containing the \"@\": scraper recognizes such name as email address"
site: stackoverflow
question_id: 74577001
answer_id: 74587510
url: https://stackoverflow.com/a/74587510
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-27T04:30:50Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74587510/revisions
accepted: true
score: 1
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f3b831b3b61d3a0ea0a0471156cd2e302c495f6cc1cbfa71b92213ff64a3beaf
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-27

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74587510>, 2022-11-27; **accepted**; score 1. Text as retrieved 2026-10-12.

[Expanded from my comment] If you tweak the function from [this answer](https://stackoverflow.com/a/58111681/6146136) a  bit to
```python
def deCFEmail(encTag):
    if not (encTag.get('data-cfemail') or encTag.select('*[data-cfemail]')):
        encTag.append(f'[! no "data-cfemail" attribute !]')
    else:
        fp = encTag.get('data-cfemail', None)
        if fp is None:
            fp = encTag.select_one('*[data-cfemail]').get('data-cfemail')
        try:
            r = int(fp[:2],16)
            encTag.string = ''.join([chr(int(fp[i:i+2], 16) ^ r) for i in range(2, len(fp), 2)]) 
        except Exception as e:
            encTag.append(f'! failed to decode "{e}"')
    return encTag
```

---

then you can use it conditionally:
```python
for i, h in enumerate(header): 
    if h.get_text()=='[email\xa0protected]': 
        header[i] = deCFEmail(h)
```

---

So, `header` can go from 
```HTML
[<a href="https://www.mobygames.com/game/amperst"><span class="__cf_email__" data-cfemail="8ecfe3feebfcfdcefa">[email protected]</span></a>,
 <a class="btn btn-xs btn-clear" href="https://www.mobygames.com/game/amperst/forums">Discuss</a>,
 <a class="btn btn-xs btn-clear" href="https://www.mobygames.com/game/sheet/review_game/amperst/">Review</a>,
 <a class="btn btn-xs btn-clear" href="https://www.mobygames.com/game/amperst/add-to-want-list">+ Want</a>,
 <a class="btn btn-xs btn-clear" href="https://www.mobygames.com/game/amperst/add-to-have-list">+ Have</a>,
 <a class="btn btn-xs btn-mobysuccess" href="https://www.mobygames.com/game/amperst/contribute">Contribute</a>]
```
to
```python
[<a href="https://www.mobygames.com/game/amperst">Ampers@t</a>,
 <a class="btn btn-xs btn-clear" href="https://www.mobygames.com/game/amperst/forums">Discuss</a>,
 <a class="btn btn-xs btn-clear" href="https://www.mobygames.com/game/sheet/review_game/amperst/">Review</a>,
 <a class="btn btn-xs btn-clear" href="https://www.mobygames.com/game/amperst/add-to-want-list">+ Want</a>,
 <a class="btn btn-xs btn-clear" href="https://www.mobygames.com/game/amperst/add-to-have-list">+ Have</a>,
 <a class="btn btn-xs btn-mobysuccess" href="https://www.mobygames.com/game/amperst/contribute">Contribute</a>]
```

---

> it is kind of a speed requirement

The additional time would not be unlike adding an extra `find` statement; and anyways, it would be insignificant compared to the parsing time (for `soup = BeautifulSoup(page, "lxml")`).
