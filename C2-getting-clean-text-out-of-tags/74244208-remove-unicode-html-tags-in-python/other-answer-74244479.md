---
title: "Remove unicode HTML tags in Python"
site: stackoverflow
question_id: 74244208
answer_id: 74244479
url: https://stackoverflow.com/a/74244479
author: "Steve Barnes"
author_url: https://stackoverflow.com/users/2298070
posted: 2022-10-29T10:22:48Z
last_edited: never
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 29d7b202adf4e4ad588c0fb0ff276b0af3962a457ca0bef2a1e8be2afa146144
role: another answer on the same question, kept as context; not my work
---

# Answer by [Steve Barnes](https://stackoverflow.com/users/2298070) — 2022-10-29

Posted on Stack Overflow, <https://stackoverflow.com/a/74244479>, 2022-10-29. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You string is presumably from somewhere else if you encode it as utf-8 then it becomes:

`'"overview":"<p style="margin: 0px 0px 20px; padding: 0px; line-height: 20px; outline: none !important; min-height: 1em; color: #333333; font-family: Arial, Helvetica, sans-serif, emoji; font-size: 14px; font-style: normal; font-variant-caps: normal; font-weight: normal; letter-spacing: normal; orphans: auto; text-indent: 0px; text-transform: none; white-space: normal; widows: auto; word-spacing: 0px; -webkit-text-size-adjust: auto; text-align: center;"><span style="font-family: arial, helvetica, sans-serif;"><strong><span style="font-size: 18pt; outline: none !important;">WTS/VDI macOS</span></strong></span></p>\n<hr>\n<p><span...'` which tools such as BeautifulSoap should handle.

Note that if your string is the result of a `subprocess.run` with capture turned on then adding a `encoding="utf-8"` parameter should do this for you.
