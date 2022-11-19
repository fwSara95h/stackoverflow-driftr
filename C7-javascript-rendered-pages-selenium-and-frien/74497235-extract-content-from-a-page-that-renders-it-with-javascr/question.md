---
title: "Extract content from a page that renders it with javascript using Beautifulsoup"
site: stackoverflow
question_id: 74497235
url: https://stackoverflow.com/q/74497235
asked: 2022-11-19T02:57:41Z
asked_by: "Álan Gabriel"
asked_by_url: https://stackoverflow.com/users/19396132
last_edited: never
tags: [python, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 2227
answer_count: 2
accepted_answer_id: 74498329
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3dfa3651ca2ff53c225d75486ae0a0c0cac1bf602cd7161c6f279b508caf6af0
---

# Extract content from a page that renders it with javascript using Beautifulsoup

Asked by [Álan Gabriel](https://stackoverflow.com/users/19396132) on Stack Overflow, <https://stackoverflow.com/q/74497235>, 2022-11-19. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I started programming not long ago and came across this problem. I want to collect stock data from the website: https://statusinvest.com.br/acoes/petr4. But apparently they are rendered with javascript and BeautifulSoup does not collect, if you can help I appreciate it



[My soup code](https://i.sstatic.net/KhxG9.png)
[Example of information loaded with javascript](https://i.sstatic.net/5lIeP.png)

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Ammar Abdullah](https://stackoverflow.com/users/15218726)** (2022-11-19): Kindly Post your `code` in Code block instead of image
- **[Jacob Lee](https://stackoverflow.com/users/13746389)** (2022-11-19): `bs4` is not capable of scraping content rendered by JavaScript. You would need to use a different third-party package, such as `selenium` or `playwright`, which supports virtual browsers.
