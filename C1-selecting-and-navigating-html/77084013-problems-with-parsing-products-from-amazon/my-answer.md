---
title: "Problems with parsing products from amazon"
site: stackoverflow
question_id: 77084013
answer_id: 77091432
url: https://stackoverflow.com/a/77091432
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-09-12T17:29:06Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/77091432/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d82f25ca6f2813c8770971599d5334fbf25d6bffee9565dd5d8e2afe23bd74cb
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-09-12

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/77091432>, 2023-09-12; score 0. Text as retrieved 2026-10-12.

> *How can i make my program more consistent and reliable.*

You could run the scraper multiple times [with some time in between in case you get blocked] and update with only non-null values, or [as suggested in my comment] try selenium because that will likely give more consistent and reliable results.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Timur](https://stackoverflow.com/users/22539580)** (2023-09-12): i am already using Selenium and trying to connect mulptiple times with some intervals and generally get the data after 2 or 3 retries (and this is one of the reasons i called my program inconsistent) and i added the check for some of the value i.e. if the product name is Null i parse it from alt inside the image tag etc. but it is not good enough still
