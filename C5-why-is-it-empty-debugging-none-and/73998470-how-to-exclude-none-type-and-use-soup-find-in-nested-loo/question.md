---
title: "How to exclude \"None\" type and use soup.find() in Nested Loops in Python?"
site: stackoverflow
question_id: 73998470
url: https://stackoverflow.com/q/73998470
asked: 2022-10-08T15:57:29Z
asked_by: "econcoder"
asked_by_url: https://stackoverflow.com/users/20192387
last_edited: never
tags: [python, web-scraping, beautifulsoup]
score: -3
views_at_snapshot: 53
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 418b22ef30dcee00bf87572e44c6ef28a6ffa7c2de3199ca434288b8c9217822
---

# How to exclude "None" type and use soup.find() in Nested Loops in Python?

Asked by [econcoder](https://stackoverflow.com/users/20192387) on Stack Overflow, <https://stackoverflow.com/q/73998470>, 2022-10-08. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to use nested loops to do web scraping and obtain titles and author names. The first loop is over the page links and then the second loop is the articles ID within that link. The content that I want to obtain is within the article ID's, however, the problem I am facing is that when python loops through the first website link, and tries to find the ID that can only be found in other link, it returns a none and hence making soup.find stating that "NoneType" has no attribute find". I am wondering what can I include in my code to ensure that python only considers ID in the link where they belong.

To be more specific let's suppose that the link is: "https://www.aeaweb.org/issues/696"
and the ID is id=""10.1257/aer.20190668", then since the ID belongs in that links, its fine, however, when looping if there is any other ID that is also being searched in the first link and returns a none.

Below is my code:

```
for i in df2['links']:
    for j in dummy['id']:
        soup=BeautifulSoup(requests.get(i).content, "html.parser")
        results_j= soup.find(id=j)
        print(results_j)
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2022-10-10): I'm intrigued by `BeautifulSoup()` returning None - I've seen that happen...what kind of input causes it?
