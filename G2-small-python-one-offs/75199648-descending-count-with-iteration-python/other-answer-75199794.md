---
title: "Descending count with iteration - Python"
site: stackoverflow
question_id: 75199648
answer_id: 75199794
url: https://stackoverflow.com/a/75199794
author: "RomanPerekhrest"
author_url: https://stackoverflow.com/users/3185459
posted: 2023-01-22T10:50:04Z
last_edited: 2023-01-22T10:55:35Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 787bf589440eb207fdc3909bd88e6dfeaa62329cadc906dc9b26dad080b92c4d
role: another answer on the same question, kept as context; not my work
---

# Answer by [RomanPerekhrest](https://stackoverflow.com/users/3185459) — 2023-01-22

Posted on Stack Overflow, <https://stackoverflow.com/a/75199794>, 2023-01-22, last edited 2023-01-22. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Instead of using nested loops and reassigning into a temporary list, use the following short approach based on *inversed* `range` and string *multiplication*:

    a = 30
    for fill_v, k in enumerate(range(a + 1, 0, -1)):
        print((f'{str(fill_v)},' * k).rstrip(','))


----------

    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
    2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2
    3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3
    4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4
    5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5
    6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6
    7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7
    8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8
    9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9
    10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10
    11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11
    12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12
    13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13
    14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14
    15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15
    16,16,16,16,16,16,16,16,16,16,16,16,16,16,16
    17,17,17,17,17,17,17,17,17,17,17,17,17,17
    18,18,18,18,18,18,18,18,18,18,18,18,18
    19,19,19,19,19,19,19,19,19,19,19,19
    20,20,20,20,20,20,20,20,20,20,20
    21,21,21,21,21,21,21,21,21,21
    22,22,22,22,22,22,22,22,22
    23,23,23,23,23,23,23,23
    24,24,24,24,24,24,24
    25,25,25,25,25,25
    26,26,26,26,26
    27,27,27,27
    28,28,28
    29,29
    30
