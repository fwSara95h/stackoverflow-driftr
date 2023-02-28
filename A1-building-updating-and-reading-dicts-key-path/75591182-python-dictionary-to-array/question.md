---
title: "Python Dictionary to Array"
site: stackoverflow
question_id: 75591182
url: https://stackoverflow.com/q/75591182
asked: 2023-02-28T11:07:25Z
asked_by: "Kaira Wadhwa"
asked_by_url: https://stackoverflow.com/users/13608661
last_edited: 2023-02-28T11:08:34Z
last_editor: "NIKUNJ KOTHIYA"
last_editor_url: https://stackoverflow.com/users/14870617
tags: [python, arrays, dictionary]
score: -3
views_at_snapshot: 60
answer_count: 1
accepted_answer_id: none
closed: 2023-02-28T16:26:31Z (Duplicate)
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 404b5fd2c083a3c1854b3ec0deee71d3719989509bd23a67bded7cce90734d8a
---

# Python Dictionary to Array

Asked by [Kaira Wadhwa](https://stackoverflow.com/users/13608661) on Stack Overflow, <https://stackoverflow.com/q/75591182>, 2023-02-28, last edited 2023-02-28 by [NIKUNJ KOTHIYA](https://stackoverflow.com/users/14870617). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have the following code in Python converting a dictionary D into a sorted array res
```
res=[]
res =sorted(D.items(),key=lambda x:(-x[1],x[0]))
```

What does `x:(-x[1],x[0])` mean?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Mathias R. Jessen](https://stackoverflow.com/users/712649)** (2023-02-28): `(-x[1],x[0])` is a _tuple literal_ - it creates a tuple consisting of the value of `-1 * x[1]` as its first element and the value of `x[0]` as it's second
- **[RomanPerekhrest](https://stackoverflow.com/users/3185459)** (2023-02-28): it sorts with priority on last item `-1`
- **[Tymon Tymoniasty](https://stackoverflow.com/users/20524112)** (2023-02-28): https://stackoverflow.com/questions/62208185/what-does-arr-sortkey-lambda-x-x0-x1-mean
- **[Daniel Hao](https://stackoverflow.com/users/10760768)** (2023-02-28): ^^^ Does this answer your question? [What does arr.sort(key=lambda x: (x\[0\],-x\[1\])) mean?](https://stackoverflow.com/questions/62208185/what-does-arr-sortkey-lambda-x-x0-x1-mean)
