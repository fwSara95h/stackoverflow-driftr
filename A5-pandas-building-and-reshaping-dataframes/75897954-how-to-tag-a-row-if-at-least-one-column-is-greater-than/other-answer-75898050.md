---
title: "How to tag a row if at least one column is greater than a specific value"
site: stackoverflow
question_id: 75897954
answer_id: 75898050
url: https://stackoverflow.com/a/75898050
author: "rorshan"
author_url: https://stackoverflow.com/users/21371426
posted: 2023-03-31T11:32:05Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 792c8efaf22c9829e13527520858228dfcc7bb031aa77bd0aadb1c6090e58309
role: another answer on the same question, kept as context; not my work
---

# Answer by [rorshan](https://stackoverflow.com/users/21371426) — 2023-03-31

Posted on Stack Overflow, <https://stackoverflow.com/a/75898050>, 2023-03-31. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You can use a boolean expression on each column:
```
df['tag'] = ((df['Value_1']>10) | (df['Value_2']>10) | (df['Value_3'] > 10)).astype(int)
df
```
If you want to do that on an arbitrary number of columns this could work
`df['tag'] = (df[df.columns[1:]] > 10).any(axis=1)`
