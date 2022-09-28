---
title: "python beautifulsoup to download specific .zip files from a website"
site: stackoverflow
question_id: 73885207
answer_id: 73885318
url: https://stackoverflow.com/a/73885318
author: "StSav012"
author_url: https://stackoverflow.com/users/8554611
posted: 2022-09-28T17:02:55Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 33323483cf2b69306eb5d338914ee214f3aa595e00f25cd2bf54d10f6814c249
role: another answer on the same question, kept as context; not my work
---

# Answer by [StSav012](https://stackoverflow.com/users/8554611) — 2022-09-28

Posted on Stack Overflow, <https://stackoverflow.com/a/73885318>, 2022-09-28. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Access `a` tags if there are any:
```python
for i in ref:
    if i.a is not None:
        print(i.a.get('href'))
```
