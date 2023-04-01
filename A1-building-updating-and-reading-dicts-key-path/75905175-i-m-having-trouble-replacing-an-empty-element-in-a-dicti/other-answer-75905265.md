---
title: "I'm having trouble replacing an empty element in a dictionary in python 3.7"
site: stackoverflow
question_id: 75905175
answer_id: 75905265
url: https://stackoverflow.com/a/75905265
author: "Seyed Amirreza Kabodian"
author_url: https://stackoverflow.com/users/20940198
posted: 2023-04-01T09:14:10Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ae48ab34d0a11072724cbd3b17c62601f5de84b857def4402123491f6f6ced59
role: another answer on the same question, kept as context; not my work
---

# Answer by [Seyed Amirreza Kabodian](https://stackoverflow.com/users/20940198) — 2023-04-01

Posted on Stack Overflow, <https://stackoverflow.com/a/75905265>, 2023-04-01. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

it has to be:

    name = input("enter name")
    age = input("enter age")
    A['name'] = name
    A['age'] = age
    print(A)
