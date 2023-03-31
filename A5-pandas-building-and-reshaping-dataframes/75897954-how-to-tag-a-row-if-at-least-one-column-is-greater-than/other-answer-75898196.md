---
title: "How to tag a row if at least one column is greater than a specific value"
site: stackoverflow
question_id: 75897954
answer_id: 75898196
url: https://stackoverflow.com/a/75898196
author: "RomanPerekhrest"
author_url: https://stackoverflow.com/users/3185459
posted: 2023-03-31T11:49:19Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f5a55f24fafb52b90b6cdc2931e46c5d597f44e26a489332144175e8cd3d991f
role: another answer on the same question, kept as context; not my work
---

# Answer by [RomanPerekhrest](https://stackoverflow.com/users/3185459) — 2023-03-31

Posted on Stack Overflow, <https://stackoverflow.com/a/75898196>, 2023-03-31. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Filter `Value*` columns to check them for the needed condition:

    df['tag'] = (df.filter(like='Value') > 10).any(axis=1).astype(int)


----------

       Unique ID  Value_1  Value 2  Value 3  tag
    0        111       10       50       18    1
    1        222        5        8        2    0
    2        333       12        3        5    1
