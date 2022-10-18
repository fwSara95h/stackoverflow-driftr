---
title: "Scraping a.href returns blank value?"
site: stackoverflow
question_id: 74114161
answer_id: 74114341
url: https://stackoverflow.com/a/74114341
author: "Sudip550"
author_url: https://stackoverflow.com/users/16897958
posted: 2022-10-18T16:25:08Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d4f15cc4c9966387ca64390449daac0b259dfdfb0a6a8759ae52c24b50329a9f
role: another answer on the same question, kept as context; not my work
---

# Answer by [Sudip550](https://stackoverflow.com/users/16897958) — 2022-10-18

Posted on Stack Overflow, <https://stackoverflow.com/a/74114341>, 2022-10-18. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

please see the code below, its working good--

    url = 'https://smws.com/all-whisky?sort=pricedesc&page=1&per-page=128'
    r = requests.get(url)
    soup = BeautifulSoup(r.content,features="html.parser")
    
    for link in soup.find_all('a'):
       print(link.get('href'))
