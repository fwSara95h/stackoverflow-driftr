---
title: "How to read table from url as DataFrame and modify format of data in one column in Python Pandas?"
site: stackoverflow
question_id: 74913448
answer_id: 74913588
url: https://stackoverflow.com/a/74913588
author: "notafk"
author_url: https://stackoverflow.com/users/13094282
posted: 2022-12-25T13:36:32Z
last_edited: 2022-12-25T13:38:04Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b71bdfd64edb0bb04fa7353a47488926cd525ce8f2d2324e586698925334b02e
role: another answer on the same question, kept as context; not my work
---

# Answer by [notafk](https://stackoverflow.com/users/13094282) — 2022-12-25

Posted on Stack Overflow, <https://stackoverflow.com/a/74913588>, 2022-12-25, last edited 2022-12-25. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You can do this thanks to beautifulsoup library ... If you click right in the web page with google chrome, you can see the structure of the web page, it's well structured, and easy to extract data between html tags.
Also, if you want to extract data of all years, just loop on the web url.

> https://www.timeanddate.com/holidays/kenya/2022
> https://www.timeanddate.com/holidays/kenya/2021
...

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[dingaro](https://stackoverflow.com/users/12242085)** (2022-12-25): could you present sample of code with loop ?
- **[Community](https://stackoverflow.com/users/-1)** (2022-12-26): Your answer could be improved with additional supporting information. Please [edit] to add further details, such as citations or documentation, so that others can confirm that your answer is correct. You can find more information on how to write good answers [in the help center](/help/how-to-answer).
