---
title: "Descending count with iteration - Python"
site: stackoverflow
question_id: 75199648
url: https://stackoverflow.com/q/75199648
asked: 2023-01-22T10:22:19Z
asked_by: "TF7"
asked_by_url: https://stackoverflow.com/users/21000447
last_edited: never
tags: [python, loops, count]
score: -1
views_at_snapshot: 90
answer_count: 5
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2fb0313bb8fb2fd581bfa19ab49ed90d5f88e72d5b5155881a16c9bc61bae9d7
---

# Descending count with iteration - Python

Asked by [TF7](https://stackoverflow.com/users/21000447) on Stack Overflow, <https://stackoverflow.com/q/75199648>, 2023-01-22. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I need help on how to iterate over rows. For example, let's say I have a variable

    a = 30


What I would like to do is using a loop in order to obtain something like that:

    0,0,0,0,0,0,0,0,.....,0     (30 zeros, because a=30)
    1,1,1,1,1,1,1,1,....,1      (29 ones)
    2,2,2,2,2,2,2,2,...,2       (28 twos)
    .....
    30                          (1 thirty)
I tried something like this:

    L = [0]
    for x in L:
       while L[x] < a:
         print(x)
         L[0] = L[0]+1
But doing this I obtain only 30 zeros. I'm not able to increase L to restart the count.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Karl Knechtel](https://stackoverflow.com/users/523612)** (2023-01-22): In your own words, where the code says `for x in L:`, what do you think this means? What is the intended purpose of that loop? How many times do you expect it to run, and what do you expect to be the value of `x` each time? What is `a` in this code? Overall, please try to explain the intended logic, step by step.
