---
title: "Check a subkey value using a random variable and a condition. KeyError: \"x\""
site: stackoverflow
question_id: 75851646
answer_id: 75851835
url: https://stackoverflow.com/a/75851835
author: "user21485801"
author_url: (account no longer exists)
posted: 2023-03-27T03:10:32Z
last_edited: 2023-03-31T07:01:23Z
last_editor: "Adrian Mole"
last_editor_url: https://stackoverflow.com/users/10871073
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5fe1d12d33bd3eb45f33ca56c7866cbdf7a6a607705783da628a02b6f5808ab8
role: another answer on the same question, kept as context; not my work
---

# Answer by user21485801 (account no longer exists) — 2023-03-27

Posted on Stack Overflow, <https://stackoverflow.com/a/75851835>, 2023-03-27, last edited 2023-03-31. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

The problem is that the value, `"gender"`, is not a dictionary containing either `"male"` or `"female"`. 

This may work:
```python
if data[random_data]["gender"] == "male":
    print(f"{random_data}: word is Male")
else:
    print(f"{random_data}: word is Female")
```
