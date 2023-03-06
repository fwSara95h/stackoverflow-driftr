---
title: "Counting positive words in a passage python"
site: stackoverflow
question_id: 75646277
answer_id: 75646465
url: https://stackoverflow.com/a/75646465
author: "Alain T."
author_url: https://stackoverflow.com/users/5237560
posted: 2023-03-06T01:50:11Z
last_edited: never
accepted: false
score: -1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9e0853e3dff0f5f5c2c9914bae37aa0a16dbe1a65a74f180e47171f8d234552e
role: another answer on the same question, kept as context; not my work
---

# Answer by [Alain T.](https://stackoverflow.com/users/5237560) — 2023-03-06

Posted on Stack Overflow, <https://stackoverflow.com/a/75646465>, 2023-03-06. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

you can use sum() with a condition in a comprehension to count matching words (True counts as 1 and False as zero):

    words = passage_excerpt.split()
    D = {'num_pos_words': sum(word in pos_words for word in words),
         'num_neg_words': sum(word in neg_words for word in words),
         'num_words_total': len(words) }
    
    
    {'num_pos_words': 2, 'num_neg_words': 1, 'num_words_total': 15}
