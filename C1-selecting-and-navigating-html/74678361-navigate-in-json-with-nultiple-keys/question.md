---
title: "Navigate in JSON with nultiple keys"
site: stackoverflow
question_id: 74678361
url: https://stackoverflow.com/q/74678361
asked: 2022-12-04T16:05:00Z
asked_by: "Paul Mark"
asked_by_url: https://stackoverflow.com/users/6484462
last_edited: 2022-12-04T16:18:47Z
last_editor: "accdias"
last_editor_url: https://stackoverflow.com/users/6789321
tags: [python, json, python-3.x, beautifulsoup, python-requests]
score: 0
views_at_snapshot: 68
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6909960feec0700ebcbaf21ad34f7a49ee090f4b90813899d9142005b6169456
---

# Navigate in JSON with nultiple keys

Asked by [Paul Mark](https://stackoverflow.com/users/6484462) on Stack Overflow, <https://stackoverflow.com/q/74678361>, 2022-12-04, last edited 2022-12-04 by [accdias](https://stackoverflow.com/users/6789321). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to get a key from a `JSON` from a website using the following code:

```python
import json
import requests
from bs4 import BeautifulSoup

url = input('Enter url:')
html = requests.get(url)
soup = BeautifulSoup(html.text,'html.parser')

data = json.loads(soup.find('script', type='application/json').text)
print(data)
print("####################################")
```
And here is the `JSON`:

```json
{"props": {
    "XYZ": {
        "ABC": [
            {
                "current": "sold",
                 "location": "FD",
                 "type": "d",
                 "uid": "01020633"
            }
        ],
        "searchTerm": "asd"
    }
}}
```

I'm able to load the page, find the `JSON`, and print all data. The question is, how can I print only the information from the `current` key? Will something like the following work? 

```python
print(data['props']['XYZ']['ABC']['current']
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[ms12](https://stackoverflow.com/users/10671274)** (2022-12-04): current_value = data['props']['XYZ']['ABC'][0]['current']
- **[accdias](https://stackoverflow.com/users/6789321)** (2022-12-04): @newbie, add that as an answer and explain OP that `ABC` key holds a list, hence the need to access it using an index.
