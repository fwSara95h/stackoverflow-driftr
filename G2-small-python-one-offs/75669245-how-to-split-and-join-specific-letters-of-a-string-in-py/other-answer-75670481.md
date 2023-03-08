---
title: "How to split and join specific letters of a string in Python?"
site: stackoverflow
question_id: 75669245
answer_id: 75670481
url: https://stackoverflow.com/a/75670481
author: "Matthias"
author_url: https://stackoverflow.com/users/1209921
posted: 2023-03-08T07:51:33Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3e6fb575d95a162a1755c43b5c1da9f89598a1c9a91df9b9be6dffd2557a3ebf
role: another answer on the same question, kept as context; not my work
---

# Answer by [Matthias](https://stackoverflow.com/users/1209921) — 2023-03-08

Posted on Stack Overflow, <https://stackoverflow.com/a/75670481>, 2023-03-08. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

With `list` you can split the string into single characters. Then you can loop over the list, compare two consecutive characters and if they are "a" and "l" you replace the first one with "al" and remove the second element. 

    original_words = "installation alcohol international"
    
    l = list(original_words)
    
    for i in range(len(l) - 1, -1, -1):
        if l[i] == 'a' and l[i + 1] == 'l':
            l[i] = 'al'
            del l[i + 1]
    
    print(l)
