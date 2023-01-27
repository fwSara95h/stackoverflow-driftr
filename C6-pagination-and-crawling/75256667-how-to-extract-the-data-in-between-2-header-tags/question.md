---
title: "How to extract the data in between 2 header tags?"
site: stackoverflow
question_id: 75256667
url: https://stackoverflow.com/q/75256667
asked: 2023-01-27T10:14:05Z
asked_by: "Akshay Toranagatti"
asked_by_url: https://stackoverflow.com/users/20786649
last_edited: 2023-01-28T18:02:41Z
tags: [html, web-scraping, beautifulsoup, text-extraction, data-extraction]
score: -1
views_at_snapshot: 424
answer_count: 1
accepted_answer_id: 75272195
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d2375d886954ce7123d80126b9bf32d907d562f01d222d8a1aa3607fae3d3f10
---

# How to extract the data in between 2 header tags?

Asked by [Akshay Toranagatti](https://stackoverflow.com/users/20786649) on Stack Overflow, <https://stackoverflow.com/q/75256667>, 2023-01-27, last edited 2023-01-28. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm working on scraping the website and I want to extract the data in between the 2 headers and tag it to first tag as key-value pair.  

How to extract the text under headers (like h1 and h2) ?
 

```python
soup = BeautifulSoup(page.content, 'html.parser')
items = soup.select("div.conWrap")

htag_count = []
item_header = soup.find_all(re.compile('^h[1-6]'))
for item in item_header:
    htag_count.append({item.name:item.text})

print(htag_count)
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Andrej Kesely](https://stackoverflow.com/users/10035985)** (2023-01-27): Can you please edit your question and put there sample of HTML and what info exactly you want to get?
