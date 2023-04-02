---
title: "Python using Pandas - Retrieving the name of all columns that contain numbers"
site: stackoverflow
question_id: 75909965
answer_id: 75910920
url: https://stackoverflow.com/a/75910920
author: "Sajil Alakkalakath"
author_url: https://stackoverflow.com/users/12881134
posted: 2023-04-02T08:38:39Z
last_edited: 2023-04-05T19:25:59Z
accepted: false
score: -1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 74dc508bf246f048bb73e86a8810536b3897e00fc2452b764a66742a8d595131
role: another answer on the same question, kept as context; not my work
---

# Answer by [Sajil Alakkalakath](https://stackoverflow.com/users/12881134) — 2023-04-02

Posted on Stack Overflow, <https://stackoverflow.com/a/75910920>, 2023-04-02, last edited 2023-04-05. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Use the below function:

First it select all the numeric columns, then it finds the columns, which is finally converted into list.

    df.select_dtypes(include="number").columns.to_list()
