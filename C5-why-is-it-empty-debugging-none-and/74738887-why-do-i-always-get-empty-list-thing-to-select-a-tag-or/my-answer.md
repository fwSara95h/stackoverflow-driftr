---
title: "Why do I always get empty list thing to select a tag or css property by using Python?"
site: stackoverflow
question_id: 74738887
answer_id: 74739128
url: https://stackoverflow.com/a/74739128
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-09T05:09:11Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74739128/revisions
accepted: true
score: 0
chapter: C5
chapter_title: "Why is it empty? Debugging None and []"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: cffbefa6a57057be69cbac0a50e5f132e46a5962be937f90358e504fe5ebe757
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-09

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74739128>, 2022-12-09; **accepted**; score 0. Text as retrieved 2026-10-12.

For various possible reasons, you don't always get the exact same html via python's `requests.get` as what you see in your browser. Sometimes it's because of blockers or JavaScript loading, but for this specific page and element, it's just that google will format the response a bot differently based on the source of the request. Try adding some headers

```python
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'
}
url = 'https://www.google.com/search?client=safari&rls=en&q=프로그래밍+공부&ie=UTF-8&oe=UTF-8'

response = requests.get(url, headers=headers)
reqErr = response.raise_for_status() # just a good habit to check
if reqErr: print(f'!"{reqErr}" - while getting ', url)

soup = BeautifulSoup(response.content, 'html.parser')

find = soup.select('#taw')
if not find: ## save html to check [IN AN EDITOR, NOT a browser] if expected elements are missing
    hfn = 'x.html'
    with open(hfn, 'wb') as f: f.write(response.content)
    print(f'saved html to  "{hfn}"')

print(find)
```

<sub>The `reqErr` and *`if not find....`* parts are just to help understand why in case you don't get the expected results. They're helpful for debugging in general for requests+bs4 scraping attempts.</sub>

The printed output I got with the code above was:

```html
[<div id="taw"><div data-ved="2ahUKEwjvjrj04ev7AhV3LDQIHaXeDCkQL3oECAcQAg" id="oFNiHe"></div><div id="tvcap"></div></div>]
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[yeolsim_coding](https://stackoverflow.com/users/20700679)** (2022-12-09): thanks to reply to my question! I can't fully understand the code you answered yet, but I will study hard and understand it perfectly
