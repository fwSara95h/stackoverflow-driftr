---
title: "Getting empty list after running scaping code in python to get reviews of users from play store of my app"
site: stackoverflow
question_id: 75054860
answer_id: 75104392
url: https://stackoverflow.com/a/75104392
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-13T02:49:57Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75104392/revisions
accepted: false
score: 0
chapter: C5
chapter_title: "Why is it empty? Debugging None and []"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 29556146acb83eda08af884752386afe47a4406bd9a4b0b2ea12af52cffd42d3
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-13

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75104392>, 2023-01-13; score 0. Text as retrieved 2026-10-12.

> *Print your status, see what it returns `print(response.status_code)`* – 
Samuel
 
You should always check `response` first. I usually add a line after a `request.get` call with something like

```python 
print(response.status_code, response.reason, 'from', response.url)
```

so that I can see if the response is [ok](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200) and also so that I'll know if the request was redirected to another page. (You can also proceed conditionally with `if response.status_code == 200`  or [`if response.ok`](https://www.geeksforgeeks.org/response-ok-python-requests/), or interrupt the program by raising an error in case of a bad response with [`response.raise_for_status()`](https://www.geeksforgeeks.org/response-raise_for_status-python-requests/))

In this case, the link itself also appears to be problematic
[![404][1]][1]


  [1]: https://i.sstatic.net/SsI8d.png
