---
title: "beautifulsoup - obtaining the tag and it's parent from the text inside?"
site: stackoverflow
question_id: 74270903
url: https://stackoverflow.com/q/74270903
asked: 2022-11-01T02:27:38Z
asked_by: "dirtyw0lf"
asked_by_url: https://stackoverflow.com/users/1219322
last_edited: never
tags: [python, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 215
answer_count: 2
accepted_answer_id: 74271340
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1625fbe531fe6423ae6df0c76d3df3c0e69d2598bf0811fed52968bc0d062b20
---

# beautifulsoup - obtaining the tag and it's parent from the text inside?

Asked by [dirtyw0lf](https://stackoverflow.com/users/1219322) on Stack Overflow, <https://stackoverflow.com/q/74270903>, 2022-11-01. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Using beautifulsoup it is possible to do the following:


    for heading in soup.find_all('h1'):
       print(heading.text)

    Top Rated Movies

However, is there a method to extract the tags themselves, given the text? A way of working backwards from the above example, something like: 

    soup.find_tag('Top Rated Movies')
    
    h1
