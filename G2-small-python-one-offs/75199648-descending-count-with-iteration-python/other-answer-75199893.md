---
title: "Descending count with iteration - Python"
site: stackoverflow
question_id: 75199648
answer_id: 75199893
url: https://stackoverflow.com/a/75199893
author: "PrathameshB"
author_url: https://stackoverflow.com/users/21058702
posted: 2023-01-22T11:05:07Z
last_edited: 2023-01-22T11:08:34Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 11c9554c2a27d9ec6f997982d6cead1d9ec30c59c95a46dbb2209af8b28494c0
role: another answer on the same question, kept as context; not my work
---

# Answer by [PrathameshB](https://stackoverflow.com/users/21058702) — 2023-01-22

Posted on Stack Overflow, <https://stackoverflow.com/a/75199893>, 2023-01-22, last edited 2023-01-22. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

    var = 30
    count = 0
    for i in range(var+1, 0, -1):
        for j in range(0,i):
            print(count, end='', sep='')
        print("\n")
        count = count + 1

The code defines two variables var with a value of 30, and count with a value of 0. It then uses a nested for loop to iterate over a range of numbers, starting from var+1 and ending at 0 in descending order. On each iteration of the inner loop, the code prints the current value of the count variable, followed by a newline character. The value of count is incremented by 1 on each iteration of the outer loop. The output is a series of rows, each row containing a different number of the same value, starting from 0 and ending with 30. The number of times each number is printed in each row will be decremented by 1 starting from 30 to 1.
