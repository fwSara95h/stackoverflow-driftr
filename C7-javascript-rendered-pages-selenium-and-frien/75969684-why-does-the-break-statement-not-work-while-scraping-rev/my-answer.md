---
title: "Why does the break statement not work while scraping reviews with Selenium and BeautifulSoup in Python?"
site: stackoverflow
question_id: 75969684
answer_id: 75969778
url: https://stackoverflow.com/a/75969778
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-09T09:46:30Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75969778/revisions
accepted: true
score: 1
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c22615cdb949d44f2db3d2841b60e311ccfc9d582d80874c787496176b62b2ff
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-09

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75969778>, 2023-04-09; **accepted**; score 1. Text as retrieved 2026-10-12.

> *From what I understand it should work as there is no "next page" button on the last review page anymore.*

Except there *is*, even though its disabled:

> [![next page][1]][1]

<br>

So, the `while` probably ends up clicking it endlessly to no effect. I would suggest using as selector <kbd>**`.a-pagination .a-last:not(.a-disabled)`**</kbd> instead of just *`.a-pagination .a-last`*.

  [1]: https://i.sstatic.net/Q4uXB.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Mina](https://stackoverflow.com/users/19684355)** (2023-04-09): It works now! Thank you very much! :) I thought this entire time that because it says 'disabled' this would be considered as a different element.
- **me** (2023-04-09): @Mina glad to help! yes, `.{class}` selectors select every element *containing* that class. For example `.a-pagination .a-last.a-disabled` would pick the disabled "Next Page" button specifically, even if they had `class="a-disabled a-last btn-grey"`
