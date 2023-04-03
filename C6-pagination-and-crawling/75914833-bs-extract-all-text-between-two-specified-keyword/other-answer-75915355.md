---
title: "BS Extract all text between two specified keyword"
site: stackoverflow
question_id: 75914833
answer_id: 75915355
url: https://stackoverflow.com/a/75915355
author: "Atbjbiye"
author_url: https://stackoverflow.com/users/21552291
posted: 2023-04-03T00:39:12Z
last_edited: 2023-04-03T00:40:05Z
accepted: true
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e28f74cc95ba3279972d202f4e6b9b9864214f8440a197338dafe8f2eded6469
role: another answer on the same question, kept as context; not my work
---

# Answer by [Atbjbiye](https://stackoverflow.com/users/21552291) — 2023-04-03

Posted on Stack Overflow, <https://stackoverflow.com/a/75915355>, 2023-04-03, last edited 2023-04-03; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Assuming that you have extracted all the words between the specified tag, you now have a string extracted in chronological order to the way that the text was written...

Once you have your full text string, you can get a substring between two words that are different and each only occur once in the text:

    text = {text}
    def get_textchunk(word1, word2, text):
            new_text = text.split(word1)
            new_text = new_text[1]
            newnew_text = new_text.split(word2)
            return newnew_text
    print(get_textchunk('word1','word2',text)[0])

This is a function that will split in two steps using two different words.

If you want to get text between two of the same words that occur only twice (once at the start of the text and once at the end) use this code:

    def get_textchunk(word, text):
            text = text.split(word)
            return text
    print(get_textchunk('word', text)[1])

This will get you the middle of the text you just split.

If you want to get text between two words that are different but occur frequently in the body of your text use this code:

    def get_textchunk(word1, word2, text):
            idx1 = text.index(word1)
            idx2 = text.index(word2)
            for idx in range(idx1 + len(word1) + 1, idx2):
                    new_text = new_text + text[idx]
            return new_text
    
This function may be the most helpful for you.
