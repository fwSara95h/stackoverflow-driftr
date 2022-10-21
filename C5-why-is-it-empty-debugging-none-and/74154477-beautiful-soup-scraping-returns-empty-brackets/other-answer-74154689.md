---
title: "Beautiful Soup Scraping returns empty brackets"
site: stackoverflow
question_id: 74154477
answer_id: 74154689
url: https://stackoverflow.com/a/74154689
author: "Adithyapranav Gupta Kolluru"
author_url: https://stackoverflow.com/users/19886737
posted: 2022-10-21T13:52:22Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 10528e8a8e5099db8bcc6122df03536f2319e07c0dc91993d5f43ac47cc48aba
role: another answer on the same question, kept as context; not my work
---

# Answer by [Adithyapranav Gupta Kolluru](https://stackoverflow.com/users/19886737) — 2022-10-21

Posted on Stack Overflow, <https://stackoverflow.com/a/74154689>, 2022-10-21. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

@David,

I have tried using the code and it needed some changes.

**Note:- You have tried using the id attribute which is not an attribute present in the tables**

Here is the code that after fixing:-

    import requests
    from bs4 import BeautifulSoup
    
    req = requests.get('https://en.wikipedia.org/wiki/List_of_largest_banks')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find_all('table', {id : "By_market_capitalization"})
    print(table)
