---
title: "Python3 AttributeError: 'NoneType' object has no attribute 'find_all'"
site: stackoverflow
question_id: 75953316
url: https://stackoverflow.com/q/75953316
asked: 2023-04-06T19:58:24Z
asked_by: "Saiful Miqdar"
asked_by_url: https://stackoverflow.com/users/15867121
last_edited: 2023-04-07T02:16:34Z
last_editor: "Driftr95 (me)"
last_editor_url: https://stackoverflow.com/users/6146136
tags: [python-3.x, beautifulsoup, python-requests]
score: -1
views_at_snapshot: 583
answer_count: 3
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 80369b24e80a8dc50ac1a9a3890b9e618640ceaa2d83c544a3e3602ed99dbe7f
---

# Python3 AttributeError: 'NoneType' object has no attribute 'find_all'

Asked by [Saiful Miqdar](https://stackoverflow.com/users/15867121) on Stack Overflow, <https://stackoverflow.com/q/75953316>, 2023-04-06, last edited 2023-04-07 by me. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I want to do web scraping using Python 3 using `requests` and `BeautifulSoup` modules, but I encountered an error. Is there something wrong with my code? How can I fix the error?



```
import requests
from bs4 import BeautifulSoup

url = 'https://otakudesu.lol/genre-list/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

genres_div = soup.find('div', class_='genres')
genre_links = genres_div.find_all('a')

path = []
text = []

for link in genre_links:
    path.append(link['href'])
    text.append(link.text)

print(path)
print(text)
```

Error :
 
```
genre_links = genres_div.find_all('a')
                  ^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'find_all'
``` 

How do I fix the error ?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[pippo1980](https://stackoverflow.com/users/9877065)** (2023-04-06): what does print(genres_div) or print(type(genres_div)) gives you ??
- **[pippo1980](https://stackoverflow.com/users/9877065)** (2023-04-06): have a look at https://stackoverflow.com/questions/16322862/beautiful-soup-findall-doesnt-find-them-all
- **[baduker](https://stackoverflow.com/users/6106791)** (2023-04-06): Does this answer your question? [Beautiful Soup findAll doesn't find them all](https://stackoverflow.com/questions/16322862/beautiful-soup-findall-doesnt-find-them-all)
