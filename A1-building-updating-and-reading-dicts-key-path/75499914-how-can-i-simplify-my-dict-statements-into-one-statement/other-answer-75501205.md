---
title: "How can I simplify my dict statements into one statement?"
site: stackoverflow
question_id: 75499914
answer_id: 75501205
url: https://stackoverflow.com/a/75501205
author: "Kelly Bundy"
author_url: https://stackoverflow.com/users/12671057
posted: 2023-02-19T15:28:30Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2c99d04cf715ef9f5d14a30b5279f5aba02d7fa0e621fcb9aa33395a7d7210ec
role: another answer on the same question, kept as context; not my work
---

# Answer by [Kelly Bundy](https://stackoverflow.com/users/12671057) — 2023-02-19

Posted on Stack Overflow, <https://stackoverflow.com/a/75501205>, 2023-02-19. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You said you were told you *"needed to combine the two dictionaries for easier readability"*. Apparently, they'd find it easier to read if each room's whole data were in one place instead of spread over multiple dicts. So instead of
```
'Foyer': {'South': 'Great Hall'},
```
in one dict and
```
'Foyer': 'Shield',
```
in another, just combine that:
```
'Foyer': {'item': 'Shield', 'South': 'Great Hall'},
```
You could combine your dicts like that with this code:
```
for k, v in items.items():
    rooms[k]['item'] = v
del items
```
But really that would be missing the point. You should *write* that combined dict *instead* of your two dicts. Then you have that better readability.

If your code would somehow benefit from your two dicts, you can easily compute them from that *one* dict containing the *whole* game configuration. You don't necessarily need to use that game configuration directly.
