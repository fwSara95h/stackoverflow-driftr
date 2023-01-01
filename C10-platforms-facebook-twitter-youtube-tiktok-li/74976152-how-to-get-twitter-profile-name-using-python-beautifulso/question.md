---
title: "How to get twitter profile name using python BeautifulSoup module?"
site: stackoverflow
question_id: 74976152
url: https://stackoverflow.com/q/74976152
asked: 2023-01-01T17:21:18Z
asked_by: "mac"
asked_by_url: https://stackoverflow.com/users/713200
last_edited: never
tags: [python, html, beautifulsoup, html-parser]
score: 0
views_at_snapshot: 798
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9df8ee7d2a8aa26d8e0465a8f8f76f10396889c3a113b6b5c6b7b3b232c4bc51
---

# How to get twitter profile name using python BeautifulSoup module?

Asked by [mac](https://stackoverflow.com/users/713200) on Stack Overflow, <https://stackoverflow.com/q/74976152>, 2023-01-01. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to get twitter profile name using profile url with beautifulsoup in python,
but whatever html tags I use, I'm not able to get the name. What html tags can I use to
get the profile name from twitter user page ? 

```
url = 'https://twitter.com/twitterID'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

# Find the display name
name_element = soup.find('span', {'class':'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})
if name_element != None:
    display_name = name_element.text
else:
    display_name = "error"
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[S. C.](https://stackoverflow.com/users/16168260)** (2023-01-01): Because Twitter's class names do not remain the same, they are dynamic.
- **[sami-amer](https://stackoverflow.com/users/13560010)** (2023-01-01): Is there a reason you aren't using the Twitter API? I don't think HTML parsing will get you very far.
