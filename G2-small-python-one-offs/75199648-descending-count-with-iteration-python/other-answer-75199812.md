---
title: "Descending count with iteration - Python"
site: stackoverflow
question_id: 75199648
answer_id: 75199812
url: https://stackoverflow.com/a/75199812
author: "MARVEL"
author_url: https://stackoverflow.com/users/16702151
posted: 2023-01-22T10:53:15Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a9684ff635c126811de9ae2e08d05eb38daa254881377f24bcafb5a93412e438
role: another answer on the same question, kept as context; not my work
---

# Answer by [MARVEL](https://stackoverflow.com/users/16702151) — 2023-01-22

Posted on Stack Overflow, <https://stackoverflow.com/a/75199812>, 2023-01-22. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

the suggestion below needs numpy

    import numpy as np
    a=30
    token=0
    for i in range(a,0,-1):
        x=np.repeat(token,i)
        print(x)
        token=token+1
