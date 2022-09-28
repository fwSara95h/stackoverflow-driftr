---
title: "python beautifulsoup to download specific .zip files from a website"
site: stackoverflow
question_id: 73885207
answer_id: 73885525
url: https://stackoverflow.com/a/73885525
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-28T17:19:44Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73885525/revisions
accepted: false
score: 0
chapter: C3
chapter_title: "Links, attributes, images and downloads"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d3e99cc4f579a6c129e6439a1eb286543a445744e30be3f20fb1e4d52b3f9a62
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-09-28

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73885525>, 2022-09-28; score 0. Text as retrieved 2026-10-12.

You can either just select all links then filter them down to the weekly updates:

    ref = [
        a for a in soup.select('a') if a.text
        and 'Weekly Update' in a.text
    ]
OR you can narrow down to a parent element before selecting the links:

    ref = soup.find(
        'b', string='Weekly Incremental NPI Files'
    ).find_next('tr').select('a')
**Either way,** you'll end up with the same set of links:
[![enter image description here][1]][1]


  [1]: https://i.sstatic.net/LsY7X.png
