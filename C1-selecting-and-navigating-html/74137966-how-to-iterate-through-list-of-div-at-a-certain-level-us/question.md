---
title: "How to iterate through list of div at a certain level using BeautifulSoup?"
site: stackoverflow
question_id: 74137966
url: https://stackoverflow.com/q/74137966
asked: 2022-10-20T09:58:14Z
asked_by: "mike.depetriconi"
asked_by_url: https://stackoverflow.com/users/10824073
last_edited: 2022-10-21T07:59:00Z
last_editor: "HedgeHog"
last_editor_url: https://stackoverflow.com/users/14460824
tags: [python, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 111
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 94d22edba6da317ef94bf589929df10f131b914353e7e531dc1bbc4c774d2e42
---

# How to iterate through list of div at a certain level using BeautifulSoup?

Asked by [mike.depetriconi](https://stackoverflow.com/users/10824073) on Stack Overflow, <https://stackoverflow.com/q/74137966>, 2022-10-20, last edited 2022-10-21 by [HedgeHog](https://stackoverflow.com/users/14460824). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to webscrape the news from the following URL:
https://www.google.com/search?num=250&q=Apple+innovation%20performance&oq=Apple+innovation%20performance%3D1600&source=lnt&tbs=cdr:1,cd_min:1/1/2018,cd_max:12/31/2018&tbm=nws&hl=en-US

However I can see that Google is changing the name of their news's div classes every time I do a request, so I was wondering if it was possible to iterate through the list of each news section by specifying BeautifulSoup to go a certain level of div.

Please see below a screenshot showing a bit more what I'm trying to explain (I'd like to iterate through the "SoaBEf xuvV6b" sections, however the name changes on every request):

[![screenshot of the page structure][1]][1]


  [1]: https://i.sstatic.net/3AMMk.png

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[cards](https://stackoverflow.com/users/16462878)** (2022-10-20): try with _CSS selectors_, `soup.select`
- **[baduker](https://stackoverflow.com/users/6106791)** (2022-10-20): Google randomizes the class names to prevent just exactly what you're trying to do. You'd be better off using an API.
- **[mike.depetriconi](https://stackoverflow.com/users/10824073)** (2022-10-20): which API can I use?
