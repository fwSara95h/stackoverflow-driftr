---
title: "How to split and join specific letters of a string in Python?"
site: stackoverflow
question_id: 75669245
answer_id: 75669410
url: https://stackoverflow.com/a/75669410
author: "MrVinChi01"
author_url: https://stackoverflow.com/users/21332372
posted: 2023-03-08T04:18:33Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e765b7289a73857688df16e90d5f57e2105d80c77f42db8f47fc247aaf460446
role: another answer on the same question, kept as context; not my work
---

# Answer by [MrVinChi01](https://stackoverflow.com/users/21332372) — 2023-03-08

Posted on Stack Overflow, <https://stackoverflow.com/a/75669410>, 2023-03-08. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

```
original_words = "installation altitude international".replace(" ", "")
original_words_split = original_words.split("al")
print(original_words_split)
new_list =[]

for split_word in original_words_split:
    if(""!=split_word):
        new_list.extend(list(split_word.strip()))
        new_list.append("al")


print( new_list)
```
