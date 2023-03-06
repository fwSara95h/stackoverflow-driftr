---
title: "Counting positive words in a passage python"
site: stackoverflow
question_id: 75646277
answer_id: 75646466
url: https://stackoverflow.com/a/75646466
author: "Talha Tayyab"
author_url: https://stackoverflow.com/users/13086128
posted: 2023-03-06T01:50:31Z
last_edited: never
accepted: true
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b84504ff504e1a7f0fe17fd13bb27aecf7a500293c2e24d3acb7b8860e82492e
role: another answer on the same question, kept as context; not my work
---

# Answer by [Talha Tayyab](https://stackoverflow.com/users/13086128) — 2023-03-06

Posted on Stack Overflow, <https://stackoverflow.com/a/75646466>, 2023-03-06; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

I little modification in your code:

    def calculate_words(y):
        num_pos_words = 0 
        num_neg_words = 0 
        num_words_total = 0 
        for x in y.split(): # ['I', 'love', 'CSS', '1,', "it's", 'my', 'favorite', 'class', 'and', 'not', 'as', 'horrible', 'as', 'I', 'thought']
         if x in pos_words and x in passage_excerpt:
            num_pos_words += 1 
         if x in neg_words and x in passage_excerpt: 
            num_neg_words += 1 
        num_words_total = num_pos_words + num_neg_words
    
        return{'num_pos_words': num_pos_words,
         'num_neg_words': num_neg_words,
         'num_words_total': num_words_total}


    print(calculate_words(passage_excerpt))
    #{'num_pos_words': 2, 'num_neg_words': 1, 'num_words_total': 3}
