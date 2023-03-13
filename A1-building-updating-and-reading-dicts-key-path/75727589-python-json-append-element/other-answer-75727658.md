---
title: "Python - Json: append element"
site: stackoverflow
question_id: 75727589
answer_id: 75727658
url: https://stackoverflow.com/a/75727658
author: "Gtzzy"
author_url: https://stackoverflow.com/users/5244513
posted: 2023-03-13T22:59:38Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 62d6caa20a6d53b1b3dcb5a96abb4a60f3021e1cbb854d12f5793028fd0b8738
role: another answer on the same question, kept as context; not my work
---

# Answer by [Gtzzy](https://stackoverflow.com/users/5244513) — 2023-03-13

Posted on Stack Overflow, <https://stackoverflow.com/a/75727658>, 2023-03-13. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

`jsondata["Job"]["LoggingData"]["Logs"]` in your example is a list of dictionaries so the first condition is `False` that's why else comes into play and adds your data to the `Logs` list.

If you want it to make it work in your example, you should check it that way
```
if "LogDetails" in jsondata["Job"]["LoggingData"]["Logs"][0]:
    ...
```
then the first condition would be `True`. 
But it might break if `Logs` would be an empty list (since this is not clear from your question), so you have to check if it's there.
