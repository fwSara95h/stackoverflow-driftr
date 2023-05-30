---
title: "Can someone help me properly scrape YouTube titles in Python using BS4?"
site: stackoverflow
question_id: 76361069
url: https://stackoverflow.com/q/76361069
asked: 2023-05-30T01:16:49Z
asked_by: "Peter"
asked_by_url: https://stackoverflow.com/users/15442983
last_edited: 2023-05-30T03:11:24Z
last_editor: "Robert"
last_editor_url: https://stackoverflow.com/users/1431720
tags: [python, html, beautifulsoup, youtube]
score: -4
views_at_snapshot: 324
answer_count: 1
accepted_answer_id: 76366675
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d94ab75ddce7fdb1b4299020bd6d9e1a6bc6ae2d77229e61756b89cfe21f60fd
---

# Can someone help me properly scrape YouTube titles in Python using BS4?

Asked by [Peter](https://stackoverflow.com/users/15442983) on Stack Overflow, <https://stackoverflow.com/q/76361069>, 2023-05-30, last edited 2023-05-30 by [Robert](https://stackoverflow.com/users/1431720). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

i wanna collect youtube titles from useing BS4 in python. this is code i got recommended by GPT but doesnt work well. im looking for some intelligent coder here. thank you :)

```
import requests
from bs4 import BeautifulSoup

def get_youtube_titles():
url = 'https://www.youtube.com/'

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
    
        # Find YouTube title elements
        title_elements = soup.find_all('a', class_='yt-simple-endpoint focus-on-expand style-scope ytd-rich-grid-media')
    
        # Extract and print the titles
        for title_element in title_elements:
            title = title_element.text.strip()
            print(title)
    
    except requests.exceptions.RequestException as e:
        print('Network connection error:', e)

# Get YouTube titles

get_youtube_titles()
```

I asked to GPT but doesn't work well

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[NotAName](https://stackoverflow.com/users/2825403)** (2023-05-30): If you look at the html of a Youtube page you'll see that the title of a video is not a simple text, but is inside `aria-label` attribute. So just get it instead: `title = title_element.get('aria-label')`
- **[buran](https://stackoverflow.com/users/4046632)** (2023-05-30): [Why is "Can someone help me?" not an actual question?](https://meta.stackoverflow.com/q/284236/4046632)
