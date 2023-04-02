---
title: "Python using Pandas - Retrieving the name of all columns that contain numbers"
site: stackoverflow
question_id: 75909965
answer_id: 75910288
url: https://stackoverflow.com/a/75910288
author: "mozway"
author_url: https://stackoverflow.com/users/16343464
posted: 2023-04-02T05:33:26Z
last_edited: never
accepted: true
score: 4
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c379fed94f9062c53ea5819b874ecb5be68220605106647e41ad218c410ad695
role: another answer on the same question, kept as context; not my work
---

# Answer by [mozway](https://stackoverflow.com/users/16343464) — 2023-04-02

Posted on Stack Overflow, <https://stackoverflow.com/a/75910288>, 2023-04-02; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Using [`select_dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html):
```
dataframe.select_dtypes('number').columns.tolist()
```
Output:
```
['A', 'B', 'D']
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Adrian](https://stackoverflow.com/users/6176440)** (2023-04-03): This is a very compact solution, thank you.
