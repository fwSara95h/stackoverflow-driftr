---
title: "Python BeautifulSoup4 Finding Attributes"
site: stackoverflow
question_id: 76815403
answer_id: 76815616
url: https://stackoverflow.com/a/76815616
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-08-01T22:46:21Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/76815616/revisions
accepted: false
score: 0
chapter: C3
chapter_title: "Links, attributes, images and downloads"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 30e2cfa164078dde98207a81854f56a58094da59a1d1acb7af206c1ef6b33798
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-08-01

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76815616>, 2023-08-01; score 0. Text as retrieved 2026-10-12.

<sub>You could try `link= s[0]['href']`</sub>


As the error message indicates, you should have used `s = soup.find('a')` instead of `find_all` which returns a ResultSet (which is like a list of tags). Also, you need to use `.get('href')` or even simply `['href']`, not `.find`; see the [docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#bs4.Tag.attrs) for more details.
