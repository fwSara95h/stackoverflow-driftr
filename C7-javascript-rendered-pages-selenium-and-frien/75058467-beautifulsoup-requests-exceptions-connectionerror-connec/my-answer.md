---
title: "Beautifulsoup: requests.exceptions.ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response"
site: stackoverflow
question_id: 75058467
answer_id: 75062460
url: https://stackoverflow.com/a/75062460
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-09T20:13:06Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75062460/revisions
accepted: false
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a10662f8c127ed90ddfb52c5d7258ba282f989b51d40ef0ab703b995c4d3d86c
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-09

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75062460>, 2023-01-09; score 0. Text as retrieved 2026-10-12.

I'm pretty bad at figuring out the right set of headers and cookies, so in these situations, I often end up resorting to:

- either [`cloudscraper`](https://pypi.org/project/cloudscraper/) 

  ```python
  response = cloudscraper.create_scraper().get(URL)
  ```

<br>

- or [`HTMLSession`](https://requests.readthedocs.io/projects/requests-html/en/latest/) - which is particularly nifty in that it also parses the HTML and has some JavaScript support as well 

  ```python
  response = HTMLSession().get(URL)
  ```
