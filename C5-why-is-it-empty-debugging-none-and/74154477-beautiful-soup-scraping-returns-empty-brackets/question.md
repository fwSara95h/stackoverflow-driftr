---
title: "Beautiful Soup Scraping returns empty brackets"
site: stackoverflow
question_id: 74154477
url: https://stackoverflow.com/q/74154477
asked: 2022-10-21T13:35:29Z
asked_by: "David Schlosser"
asked_by_url: https://stackoverflow.com/users/20301563
last_edited: 2022-10-21T13:37:44Z
tags: [python, web, web-scraping, beautifulsoup]
score: -1
views_at_snapshot: 89
answer_count: 3
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c748aa728332097b030408234e33a5ad98c225e2daeabb622c17397f66b74abb
---

# Beautiful Soup Scraping returns empty brackets

Asked by [David Schlosser](https://stackoverflow.com/users/20301563) on Stack Overflow, <https://stackoverflow.com/q/74154477>, 2022-10-21, last edited 2022-10-21. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

```python
html = 'https://en.wikipedia.org/wiki/List_of_largest_banks'

html_data = requests.get('https://en.wikipedia.org/wiki/List_of_largest_banks')

html_data_text = html_data.text

soup = bs(html_data_text, 'html.parser')

table = soup.find_all('table', {id : "By_market_capitalization"})

print(table)
```

returns empty bracket. I have to only use BS for this assignment. I've seen other libraries help but i can't use them. Any idea whats going wrong with trying to get this table?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[esqew](https://stackoverflow.com/users/269970)** (2022-10-21): Where on the target page is there a `<table>` element with the ID value `By_market_capitalization`?
