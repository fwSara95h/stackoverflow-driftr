---
title: "Navigate in JSON with nultiple keys"
site: stackoverflow
question_id: 74678361
answer_id: 74678936
url: https://stackoverflow.com/a/74678936
author: "Siddharth Asodariya"
author_url: https://stackoverflow.com/users/19526287
posted: 2022-12-04T17:08:02Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ad7026c56e8f239f08de366aff2b232ab0d89f7732a34efd11c0df33f358ff74
role: another answer on the same question, kept as context; not my work
---

# Answer by [Siddharth Asodariya](https://stackoverflow.com/users/19526287) — 2022-12-04

Posted on Stack Overflow, <https://stackoverflow.com/a/74678936>, 2022-12-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You can access current like below:

    data["props"]["XYZ"]["ABC"][0]["current"]

you can get a list of dictionaries by accessing "ABC" key's value.
So whenever you get curly {} bracket it shows that it is a dictionary and you can access value of particular keys using 
`dict[key] or dict.get(key,default_value)`
and whenever you get square [] bracket it shows that it is list and you can access its element by  index `list[0],list[1]`.

So, accessing list element and dictionary's key's value is two different things. I hope you understood my point.
