---
title: "How to split and join specific letters of a string in Python?"
site: stackoverflow
question_id: 75669245
answer_id: 75669343
url: https://stackoverflow.com/a/75669343
author: "Yash Mehta"
author_url: https://stackoverflow.com/users/20172954
posted: 2023-03-08T04:01:30Z
last_edited: 2023-03-08T04:07:19Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c1c2b93c3ebacc120235e86334ee607026d1903043406c72f3e9f62a2cbeffed
role: another answer on the same question, kept as context; not my work
---

# Answer by [Yash Mehta](https://stackoverflow.com/users/20172954) — 2023-03-08

Posted on Stack Overflow, <https://stackoverflow.com/a/75669343>, 2023-03-08, last edited 2023-03-08. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

**Code:**

    original_words = "installation altitude international"
    
    # removing the spaces between the words.!
    t=original_words.replace(" ","")
    
    # created a temporary string in which 'al' is replaced by '^' you can replace with any character/word which is not in the original_words
    temp_str = t.replace("al", "^")
    
    # converted into a list
    letters_list = list(temp_str)
    
    #List comprehension [replace the '^' to al]
    res = [x.replace("^", "al") for x in letters_list]
    
    print(res)

**Output:**

    ['i', 'n', 's', 't', 'al', 'l', 'a', 't', 'i', 'o', 'n', 'al', 't', 'i', 't', 'u', 'd', 'e', 'i', 'n', 't', 'e', 'r', 'n', 'a', 't', 'i', 'o', 'n', 'al']

I think the desired output you want is this. let me know if this is not your desired output.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Yash Mehta](https://stackoverflow.com/users/20172954)** (2023-03-08): Op's just changing `original_words` to `installation altitude international` and `installation alcohol international` that's why my output list contains `c` .. anyway my bad!! thank you to notify me :) @GauravHazra
