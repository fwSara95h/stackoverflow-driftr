---
title: "Web Scrapping via python show AttributeError: 'NoneType' object has no attribute 'full_text'"
site: stackoverflow
question_id: 74525951
answer_id: 74571807
url: https://stackoverflow.com/a/74571807
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-25T11:01:29Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74571807/revisions
accepted: true
score: 0
chapter: C5
chapter_title: "Why is it empty? Debugging None and []"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6dc62bc6449ad4a6dae03b9dcdeed1f9c142a2647b503fe927bf2edae2f85f84
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-25

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74571807>, 2022-11-25; **accepted**; score 0. Text as retrieved 2026-10-12.

You shouldn't try to get `.full_text` without checking if `find` returned something. You should **remove the `.full_text` part** from the lines and just build `product` with the checks, like
```python
    product = {
        'title': title.full_text.strip() if title else 'DEFAULT_TITLE',
        'price': price[0].full_text.strip() if price else 'DEFAULT_PRICE', # remove [0] from find as well
        'tag': tag.full_text.strip() if tag else 'DEFAULT_TAG',
        'sku': sku.full_text.strip() if sku else 'DEFAULT_SKU',
    }
```
[Btw, why are there 2 `sku` lines? The first line gets over-written by the second, so it's not really doing anything...]

[Also, in `get_links`, you should maybe change the selector to `'div.product-small.box:has(a[href])'` and `item.find('a[href]',first=True)` to be safer and avoid None-type errors there as well.]
