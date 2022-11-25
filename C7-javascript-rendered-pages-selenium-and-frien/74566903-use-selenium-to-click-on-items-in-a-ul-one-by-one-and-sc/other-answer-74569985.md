---
title: "Use Selenium to click on items in a UL one by one and scrape some information"
site: stackoverflow
question_id: 74566903
answer_id: 74569985
url: https://stackoverflow.com/a/74569985
author: "Prophet"
author_url: https://stackoverflow.com/users/3485434
posted: 2022-11-25T08:27:40Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ced73c5cdf2a302f7e701704680d832c6127cdf9f5a8f1b0d4c6e45a8dc84417
role: another answer on the same question, kept as context; not my work
---

# Answer by [Prophet](https://stackoverflow.com/users/3485434) — 2022-11-25

Posted on Stack Overflow, <https://stackoverflow.com/a/74569985>, 2022-11-25. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Probably this can be done much faster, without opening all those links, but not with Selenium. Selenium imitates human GUI actions, so as a human do scrape all that data you do need to open all those links and read the data on the opened pages. However this can be done much clearer and faster via API calls or with Beautifulsoup etc. But again, these are not Selenium UI approaches.
