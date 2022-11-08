---
title: "How do I apply table class criteria in a web-scraper through python?"
site: stackoverflow
question_id: 74366039
url: https://stackoverflow.com/q/74366039
asked: 2022-11-08T19:13:40Z
asked_by: "NewGuy1"
asked_by_url: https://stackoverflow.com/users/14745788
last_edited: 2022-11-10T06:39:05Z
tags: [python, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 87
answer_count: 1
accepted_answer_id: 74367438
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8e8265540344379e3cea2979ac64b7d97f9e58d81ec66a9d5128fed42dfc8dae
---

# How do I apply table class criteria in a web-scraper through python?

Asked by [NewGuy1](https://stackoverflow.com/users/14745788) on Stack Overflow, <https://stackoverflow.com/q/74366039>, 2022-11-08, last edited 2022-11-10. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Although the web-scraper below works, it also includes listed hyperlinks unrelated to the webpage tables. What I would like to have help with is limiting the class criteria to only relevant tennis match hyperlinks within the class table "table-main only12 js-nrbanner-t".

    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    
    r = requests.get('https://www.betexplorer.com/results/tennis/?year=2022&month=11&day=02')
    soup = BeautifulSoup(r.text, "html.parser")
    
    matchlist = set('https://www.betexplorer.com'+a.get('href') for a in soup.select('a[href^="/tennis"]:has(strong)'))
    
    print(pd.DataFrame(matchlist))

Edit: Driftr95 has found the exact solution I was looking for, even when I didn't phrase the question correctly

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[esqew](https://stackoverflow.com/users/269970)** (2022-11-08): Does this answer your question? [How to find elements by class](https://stackoverflow.com/questions/5041008/how-to-find-elements-by-class)
- **me** (2022-11-08): where in the page are you getting unrelated links from with your current selector? Can you share some of those links as example?
- **[NewGuy1](https://stackoverflow.com/users/14745788)** (2022-11-09): @Driftr95 the problem with this program is that it includes tennis matches that appear on different days than the one specified on the webpage.
- **me** (2022-11-09): @NewGuy1 it seems that `requests.get` returns extra results from the days before and after that are probably dynamically filtered out by the time the actual page finishes loading on browser....please see the edit added to my answer
- **me** (2022-11-09): @NewGuy1 btw, were you trying to filter by date all along? because then you should have made the question about that, or at least included it in the post - all three days' matches are in the same table in the html fetched by `requests.get`, so adding table to the selector doesn't narrow down the date at all.
