---
title: "how to return values in a python dictionary"
site: stackoverflow
question_id: 75512990
answer_id: 75513079
url: https://stackoverflow.com/a/75513079
author: "samuelmorse"
author_url: https://stackoverflow.com/users/15271707
posted: 2023-02-20T18:44:17Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 21e5350eee51396b99767cf72dca3eff6427a95bb73d634cd28cec9b9f46f467
role: another answer on the same question, kept as context; not my work
---

# Answer by [samuelmorse](https://stackoverflow.com/users/15271707) — 2023-02-20

Posted on Stack Overflow, <https://stackoverflow.com/a/75513079>, 2023-02-20. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

you can access each entry in the dictionary like this:

    dict["Jake"]

which would return the list

    ['green', 'burger', 'juice']

Then you can just grab whichever element you need from that list like so (for example their favorite color):

    dict["Jake"][0]

which would return

    'green'
