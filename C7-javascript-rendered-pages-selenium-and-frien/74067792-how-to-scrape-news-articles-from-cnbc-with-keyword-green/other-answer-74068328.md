---
title: "How to scrape news articles from cnbc with keyword \"Green hydrogen\"?"
site: stackoverflow
question_id: 74067792
answer_id: 74068328
url: https://stackoverflow.com/a/74068328
author: "Tornike Skhulukhia"
author_url: https://stackoverflow.com/users/8849892
posted: 2022-10-14T11:09:27Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bd9513f60110e7f6f69638b54cf56f803c70257bf897dc2cc594a03f3f838d34
role: another answer on the same question, kept as context; not my work
---

# Answer by [Tornike Skhulukhia](https://stackoverflow.com/users/8849892) — 2022-10-14

Posted on Stack Overflow, <https://stackoverflow.com/a/74068328>, 2022-10-14. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

The problem is that content is not present on page when it loads initially, only afterwards is it fetched from server using url like this 

https://api.queryly.com/cnbc/json.aspx?queryly_key=31a35d40a9a64ab3&query=green%20hydrogen&endindex=0&batchsize=10&callback=&showfaceted=false&timezoneoffset=-240&facetedfields=formats&facetedkey=formats%7C&facetedvalue=!Press%20Release%7C&needtoptickers=1&additionalindexes=4cd6f71fbf22424d,937d600b0d0d4e23,3bfbe40caee7443e,626fdfcd96444f28

and added to page.

Take a look at /json.aspx endpoint in devtools, data seems to be there.
