---
title: "Writing csv file - Python-3.x web-scrapping"
site: stackoverflow
question_id: 73858513
answer_id: 73863336
url: https://stackoverflow.com/a/73863336
author: "hstk"
author_url: https://stackoverflow.com/users/7693929
posted: 2022-09-27T06:40:29Z
last_edited: never
accepted: true
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7c2567ca5199dcc8c29f239811a5b03549566a113b219707641fbaa107b4b796
role: another answer on the same question, kept as context; not my work
---

# Answer by [hstk](https://stackoverflow.com/users/7693929) — 2022-09-27

Posted on Stack Overflow, <https://stackoverflow.com/a/73863336>, 2022-09-27; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

By my experience, your `title` is a string, but `writerow ` need a `iterator` or `list` simply. So, just try

```
writer.writerow([title])
```
