---
title: "How to split and join specific letters of a string in Python?"
site: stackoverflow
question_id: 75669245
answer_id: 75669342
url: https://stackoverflow.com/a/75669342
author: "Learning2Code"
author_url: https://stackoverflow.com/users/21353506
posted: 2023-03-08T04:01:08Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6c2d9bd9eb86536e0bb137238f941d998608386579a07064aecfbf19ba373984
role: another answer on the same question, kept as context; not my work
---

# Answer by [Learning2Code](https://stackoverflow.com/users/21353506) — 2023-03-08

Posted on Stack Overflow, <https://stackoverflow.com/a/75669342>, 2023-03-08. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You could do something like this with a loop to go through the letters. It looks like the output you provided has ['al', 'c', 'o', 'h', 'o', 'l'] instead of ['al', 't', 'i', 't', 'u', 'd', 'e']. But this method should work for any input string, as long as 'al' are the only letters you want to group every time.

    

    original_words = "installation altitude international"
    split_words = []
    indx = 0

    while indx in range(len(original_words)):
        # Check if letter grouping is "al"
        if original_words[indx] + original_words[indx+1] == 'al':
            # Append "al" and skip 2 indicies
            split_words.append(original_words[indx] + original_words[indx+1])
            indx += 2
        else:
            # Otherwise, append letter and skip 1 index
            split_words.append(original_words[indx])
            indx += 1
    print(split_words)
