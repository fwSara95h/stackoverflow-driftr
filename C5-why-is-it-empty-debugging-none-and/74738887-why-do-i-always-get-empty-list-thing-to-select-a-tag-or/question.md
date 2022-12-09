---
title: "Why do I always get empty list thing to select a tag or css property by using Python?"
site: stackoverflow
question_id: 74738887
url: https://stackoverflow.com/q/74738887
asked: 2022-12-09T04:19:51Z
asked_by: "yeolsim_coding"
asked_by_url: https://stackoverflow.com/users/20700679
last_edited: 2022-12-09T05:27:09Z
last_editor: "Mr. Stash"
last_editor_url: https://stackoverflow.com/users/13625800
tags: [python, web, web-scraping, beautifulsoup, request]
score: 1
views_at_snapshot: 156
answer_count: 1
accepted_answer_id: 74739128
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: febc8723072710eef737711ae47bcc530f0fcdb24ff1b9603b6ec97e86e82701
---

# Why do I always get empty list thing to select a tag or css property by using Python?

Asked by [yeolsim_coding](https://stackoverflow.com/users/20700679) on Stack Overflow, <https://stackoverflow.com/q/74738887>, 2022-12-09, last edited 2022-12-09 by [Mr. Stash](https://stackoverflow.com/users/13625800). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I just started studying Python, requests and BeautifulSoup.

I'm using VSCode and Python version is 3.10.8

I want to get HTML code using a 'taw' tag in google. but I can't get it. the result keeps getting an empty list.

```python
import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?client=safari&rls=en&q=프로그래밍+공부&ie=UTF-8&oe=UTF-8'

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

find = soup.select('#taw')

print(find)
 
```

and here's HTML code that I tried to get 'taw' tag

[![enter image description here][1]][1]

sorry for using image instead of codes.

Taw tag contains Google's ad site and I want to scrap this tag. I tried other CSS properties and tags, but the empty list keeps showing up as a result. I tried soup.find, but I got 'None'.


  [1]: https://i.sstatic.net/wc0qu.png
