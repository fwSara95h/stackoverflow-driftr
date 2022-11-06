---
title: "Python requests.get TikTok returns b''"
site: stackoverflow
question_id: 74310329
answer_id: 74333736
url: https://stackoverflow.com/a/74333736
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-06T06:32:43Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74333736/revisions
accepted: false
score: 0
chapter: C10
chapter_title: "Platforms: Facebook, Twitter, YouTube, TikTok, LinkedIn, Glassdoor"
cluster: scrape-social-platforms
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 67b0aec6f66b885aa88f06a0db21acae06437462d40bd17211a7187a3947d498
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-06

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74333736>, 2022-11-06; score 0. Text as retrieved 2026-10-12.

If you fail to [create convincing headers](https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/#therightwaytorotateuseragentsinanyprogram), consider using something like [ScrapingAnt](https://scrapingant.com/)

```python
api_url = "https://api.scrapingant.com/v2/general"
page_url = "https://www.tiktok.com/@thatlittlepuff/video/7160116843611475246"
myKey_sa = YOUR_API_TOKEN # register on https://scrapingant.com/ and paste here

page = requests.get(f'{api_url}?url={page_url}&x-api-key={myKey_sa}')

print(page.content)
```

the free tier allows a limited number of requests, and it's quite slow, but if you're not going to be making a huge number of requests, it really simplifies matters.

If you *are* going to be making a large number of requests, consider [selenium](https://selenium-python.readthedocs.io/) instead.
