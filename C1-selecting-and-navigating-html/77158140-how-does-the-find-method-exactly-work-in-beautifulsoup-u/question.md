---
title: "how does the find method exactly work in BeautifulSoup using a LXML parser?"
site: stackoverflow
question_id: 77158140
url: https://stackoverflow.com/q/77158140
asked: 2023-09-22T13:41:37Z
asked_by: "boyLern"
asked_by_url: https://stackoverflow.com/users/20492735
last_edited: never
tags: [beautifulsoup]
score: -3
views_at_snapshot: 36
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 28ef73bd5bb7c8989b98012962a071317d518a926fd11d968648e3bd5209070c
---

# how does the find method exactly work in BeautifulSoup using a LXML parser?

Asked by [boyLern](https://stackoverflow.com/users/20492735) on Stack Overflow, <https://stackoverflow.com/q/77158140>, 2023-09-22. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

[a snap of the code](https://i.sstatic.net/7QCXJ.png)


i was trying to use find() method to excerpt info from an html element, but it shows find() takes no arguments

Error: 
     5 review = soup.find_all('article', itemprop = 'review')
      6 for review in reviews:
----> 7     date_flown = review.find('td', class_ = 'review-value ')
      8     if date_flown:
      9         print(date_flown)

TypeError: find() takes no keyword arguments

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[baduker](https://stackoverflow.com/users/6106791)** (2023-09-22): Please read [ask] and provide a [mre]!
- **me** (2023-09-22): can you paste your code instead of screenshot?
- **[valid](https://stackoverflow.com/users/1467307)** (2023-09-22): You should make it as easy as possible for others to provide an answer, e.g. formatting your question (especially distinguish between you stating the problem and code and messages) and providing the non-working code so others can try it out. You state "`find()` takes no argument" but the message says "no keyword argument" so `find(.., key=..)` is not allowed.
