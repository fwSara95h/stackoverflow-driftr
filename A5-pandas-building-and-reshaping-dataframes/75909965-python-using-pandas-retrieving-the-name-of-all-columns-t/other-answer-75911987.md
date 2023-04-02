---
title: "Python using Pandas - Retrieving the name of all columns that contain numbers"
site: stackoverflow
question_id: 75909965
answer_id: 75911987
url: https://stackoverflow.com/a/75911987
author: "PaulS"
author_url: https://stackoverflow.com/users/11564487
posted: 2023-04-02T12:20:53Z
last_edited: 2023-04-02T12:32:11Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 209210d38a26803c3238df22582d5b59027d1cd0f04ae35b43dcedd52b6e5f28
role: another answer on the same question, kept as context; not my work
---

# Answer by [PaulS](https://stackoverflow.com/users/11564487) — 2023-04-02

Posted on Stack Overflow, <https://stackoverflow.com/a/75911987>, 2023-04-02, last edited 2023-04-02. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Another possibles solution:

    import re
    
    df.columns[
        [re.match(r'^(int|float)', x.name) != None for x in df.dtypes]].to_list()

Output:

    ['A', 'B', 'D']
