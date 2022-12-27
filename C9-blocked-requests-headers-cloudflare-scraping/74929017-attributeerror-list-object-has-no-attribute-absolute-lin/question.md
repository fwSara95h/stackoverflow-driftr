---
title: "AttributeError: 'list' object has no attribute 'absolute_links'"
site: stackoverflow
question_id: 74929017
url: https://stackoverflow.com/q/74929017
asked: 2022-12-27T12:02:43Z
asked_by: "Mathematics physics Biology"
asked_by_url: https://stackoverflow.com/users/20677844
last_edited: 2022-12-27T12:04:25Z
tags: [python, web-scraping, python-requests-html]
score: 0
views_at_snapshot: 370
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8b6c6b158209ccd39611ebae1a98aec79f8fee0415d67a37a13bbaadc365ac15
---

# AttributeError: 'list' object has no attribute 'absolute_links'

Asked by [Mathematics physics Biology](https://stackoverflow.com/users/20677844) on Stack Overflow, <https://stackoverflow.com/q/74929017>, 2022-12-27, last edited 2022-12-27. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

```
from requests_html import HTMLSession
url = 'https://www.walmart.com/search?q=70+inch+tv&page=2&affinityOverride=default'

s = HTMLSession()
r = s.get(url)

r.html.render(sleep=1,timeout=20)
product = r.html.find('div.mb1.ph1.pa0-xl.bb.b--near-white.w-25')



productinfo = []
for item in product.absolute_links:
    # ra = s.get(item)
    # name = ra.html.find('h1',first=True).text
    products = {
        'link' :item,

    }

    productinfo.append(products)

print(productinfo)
print(len(productinfo))
```

Output
```
for item in product.absolute_links:
AttributeError: 'list' object has no attribute 'absolute_links'
```

I want to get link of  every product than scrape some data from this website by requests-html library , but i'm getting attribute error.please help me.chack  the website html

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[MattDMo](https://stackoverflow.com/users/1426065)** (2022-12-27): When I run your code, `product` is an empty list. It looks like you need to log in, or at least solve a captcha first.
- **[Mathematics physics Biology](https://stackoverflow.com/users/20677844)** (2022-12-27): how to select tag in requests-html ?
- **[MattDMo](https://stackoverflow.com/users/1426065)** (2022-12-27): It's not about selecting a tag. The tag doesn't exist in the returned HTML because you need to log in to the site first. Examine the returned HTML and see for yourself.
- **[Mathematics physics Biology](https://stackoverflow.com/users/20677844)** (2022-12-27): so that's mean's I have to use selenium. But can  I solve captcha and logging via requests-html library? I'm not super familiar with requests-html library
