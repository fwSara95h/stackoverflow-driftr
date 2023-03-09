---
title: "Set variable column values to nan based on row condition"
site: stackoverflow
question_id: 75680488
answer_id: 75680750
url: https://stackoverflow.com/a/75680750
author: "Shubham Sharma"
author_url: https://stackoverflow.com/users/12833166
posted: 2023-03-09T05:30:48Z
last_edited: never
accepted: true
score: 5
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bf51c6af8b060ec937b8d1a145b2eb472f3f0d8ead355502463f45668c361dd4
role: another answer on the same question, kept as context; not my work
---

# Answer by [Shubham Sharma](https://stackoverflow.com/users/12833166) — 2023-03-09

Posted on Stack Overflow, <https://stackoverflow.com/a/75680750>, 2023-03-09; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Lets use broadcasting to check the indices which can be masked

    c = df.columns[1:]
    m = range(len(c), 0, -1) <= df['col_ind'].values[:, None]
    
    df[c] = df[c].mask(m)


Result

       col_ind col_1 col_2 col_3
    0        3   NaN   NaN   NaN
    1        2     d   NaN   NaN
    2        1     g     h   NaN
