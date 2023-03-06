---
title: "python say isalpha() is not defined despite it being built in (I think)"
site: stackoverflow
question_id: 75655791
url: https://stackoverflow.com/q/75655791
asked: 2023-03-06T20:57:56Z
asked_by: "conronro"
asked_by_url: https://stackoverflow.com/users/21231287
last_edited: never
tags: [python, python-3.x, isalpha]
score: -3
views_at_snapshot: 1669
answer_count: 2
accepted_answer_id: none
closed: 2023-03-07T08:10:13Z (Not suitable for this site)
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9c29838b85e89480c228425008a64d9fa26f920eab3c4b1b8e7111f6b9db9c72
---

# python say isalpha() is not defined despite it being built in (I think)

Asked by [conronro](https://stackoverflow.com/users/21231287) on Stack Overflow, <https://stackoverflow.com/q/75655791>, 2023-03-06. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

i am running a program that takes a list of numbers and letters, and separates the numbers into a sperate list and printing that list, but every time i run the code it says that isalpha is not defined. 


```
yes = []
item=[1,7,-10,34,2,"a",-8]
for things in item:
    if isalpha() ==True:
        continue
    else:
        yes.append
        print(yes)

```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Axe319](https://stackoverflow.com/users/12479639)** (2023-03-06): `isalpha` is a method on the `str` class. You would need something more along the lines of `if isinstance(things, str) and things.isalpha():`.
- **[B Remmelzwaal](https://stackoverflow.com/users/17200348)** (2023-03-06): Did you mean `if str(things).isalpha():` and `yes.append(things)`?
