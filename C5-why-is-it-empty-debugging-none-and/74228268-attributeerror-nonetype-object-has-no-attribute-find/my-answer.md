---
title: "AttributeError: nonetype object has no attribute 'find'"
site: stackoverflow
question_id: 74228268
answer_id: 74230047
url: https://stackoverflow.com/a/74230047
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-28T02:28:41Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74230047/revisions
accepted: false
score: 0
chapter: C5
chapter_title: "Why is it empty? Debugging None and []"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 66beee5fd0c063e42133a16b8f34905c46a387ed58c81824a5946447b7563b35
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-28

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74230047>, 2022-10-28; score 0. Text as retrieved 2026-10-12.

The error is likely because `listing`  has a  value of  `None`  - because the first `find` returned nothing. When working with requests+beautifulsoup, you should make a habit of checking what `requests` returned when your code doesn't behave as expected. Use
```python
with open('x.html', 'w', encoding="utf8") as f:
    f.write(str(job_request))
```
to save `job_request` to a file named "x.html" which can be opened to view what kind of response you have received. For me, it just looks like
[![enter image description here][1]][1]

<br>

If you see the same thing, you can probably resolve it just by adding some [headers](https://datagy.io/python-requests-headers/) to your request - for me, it was enough to just add [User Agent](https://www.useragentstring.com/Chrome104.0.5112.79_id_19986.php)
```json
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36"}
```
but I think the closest you can get to imitating your browser is to [copy the request from your browser][2] and then use [curlconverter](https://curlconverter.com/) to get python code you can paste into your own.

<hr>

Even so, you'll probably notice that only the first 10 results are in the fetched html - the rest are populated with JavaScript and [probably] APIs; if you want more than the first ten - and/or if adding headers doesn't work for you - you might have to resort to something like [selenium](https://medium.com/featurepreneur/an-introduction-to-web-automation-using-selenium-python-2ad84814b11c)...

  [1]: https://i.sstatic.net/GYYbk.png
  [2]: https://i.sstatic.net/HULbR.png
