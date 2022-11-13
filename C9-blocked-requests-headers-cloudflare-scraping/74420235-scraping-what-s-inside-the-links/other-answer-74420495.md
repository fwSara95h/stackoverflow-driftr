---
title: "Scraping what's inside the links"
site: stackoverflow
question_id: 74420235
answer_id: 74420495
url: https://stackoverflow.com/a/74420495
author: "Samurai6465"
author_url: https://stackoverflow.com/users/20287896
posted: 2022-11-13T11:27:08Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7ab934cc0991d2f4b7a3092acc8fdb0f45cb0bca0019a5646d60494b2c1d35ca
role: another answer on the same question, kept as context; not my work
---

# Answer by [Samurai6465](https://stackoverflow.com/users/20287896) — 2022-11-13

Posted on Stack Overflow, <https://stackoverflow.com/a/74420495>, 2022-11-13. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

you can scrape the links via tag. The html template will have the hyperlink listed and the actual website it links you to should be listed in href. Ex: 

`<li href=“https://google.com > Site 1 </li> `
The href would be the destination link and the site 1 is just the text shown in page

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[ninj](https://stackoverflow.com/users/20491929)** (2022-11-13): yes but I want to actually scrape what's inside the tag, yk?
