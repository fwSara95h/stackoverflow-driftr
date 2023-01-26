---
title: "Isolating a link with beautifulsoup"
site: stackoverflow
question_id: 75250425
url: https://stackoverflow.com/q/75250425
asked: 2023-01-26T18:48:41Z
asked_by: "Coding Bachaa"
asked_by_url: https://stackoverflow.com/users/21088789
last_edited: 2023-01-26T18:49:51Z
tags: [python, beautifulsoup]
score: 0
views_at_snapshot: 78
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 80d024bdcd31b1293208e90e8accc9aa3f57123c940e508db232fc64d81cc12a
---

# Isolating a link with beautifulsoup

Asked by [Coding Bachaa](https://stackoverflow.com/users/21088789) on Stack Overflow, <https://stackoverflow.com/q/75250425>, 2023-01-26, last edited 2023-01-26. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have to scrape through the text of a website: [link](https://crmhelpcenter.gitbook.io/wahi-digital/getting-started/readme). I created a set using beautifulsoup of all the links on the page and then eventually I want to iterate through the set.


```
import requests
from bs4 import BeautifulSoup


url = 'https://crmhelpcenter.gitbook.io/wahi-digital/getting-started/readme'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')
check = []
for link in links:
    link = 'https://crmhelpcenter.gitbook.io' + link.get('href')
    check.append(link)
print(check)
```

With this method it is not adding the sub-links of some of the links in the sidebar. I could loop through  each page and add the links accordingly but then I have to go through each link again and check if it is included in a set which makes the time expensive. Is there any way I can instead just isolate the "next" link that is on each page and go through that recursively till I reach the end?
