---
title: "add a prefix to all lines of a dataframe's column"
site: stackoverflow
question_id: 75048117
answer_id: 75048298
url: https://stackoverflow.com/a/75048298
author: "Ron Serruya"
author_url: https://stackoverflow.com/users/2126254
posted: 2023-01-08T13:55:21Z
last_edited: never
accepted: true
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 51883f46c410ee688b152218a720d90f256efbae84f56ec8f8cf391fa31fbac9
role: another answer on the same question, kept as context; not my work
---

# Answer by [Ron Serruya](https://stackoverflow.com/users/2126254) — 2023-01-08

Posted on Stack Overflow, <https://stackoverflow.com/a/75048298>, 2023-01-08; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You can just concatenate your prefix with the desired column:
```python
df['review'] = 'xxx' + df['review']
```
