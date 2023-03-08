---
title: "How to split and join specific letters of a string in Python?"
site: stackoverflow
question_id: 75669245
answer_id: 75669446
url: https://stackoverflow.com/a/75669446
author: "Alain T."
author_url: https://stackoverflow.com/users/5237560
posted: 2023-03-08T04:27:24Z
last_edited: 2023-03-08T04:39:57Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 87f70f033a5caacca7a111967b057fa18c8b70681fa18e27ada892b1f521714d
role: another answer on the same question, kept as context; not my work
---

# Answer by [Alain T.](https://stackoverflow.com/users/5237560) — 2023-03-08

Posted on Stack Overflow, <https://stackoverflow.com/a/75669446>, 2023-03-08, last edited 2023-03-08. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You can insert a comma between every character then remove the ones between "a" and "l" and split again on commas:


    ",".join(original_words).replace("a,l","al").split(",")

    ['i', 'n', 's', 't', 'al', 'l', 'a', 't', 'i', 'o', 'n', ' ', 'al', 'c',
     'o', 'h', 'o', 'l', ' ', 'i', 'n', 't', 'e', 'r', 'n', 'a', 't', 'i',
     'o', 'n', 'al']

*You can use something other than a comma as a separator (e.g. "\n") if the string may already contain commas*

If you want to remove spaces, you should do it on the resulting list (after the split) otherwise you could end up getting "al" when a word ending in "a" is followed by a word starting with "l"  (e.g: "data log")
