---
title: "How to split and join specific letters of a string in Python?"
site: stackoverflow
question_id: 75669245
url: https://stackoverflow.com/q/75669245
asked: 2023-03-08T03:37:06Z
asked_by: "Heindryk"
asked_by_url: https://stackoverflow.com/users/21353284
last_edited: 2023-03-08T15:05:04Z
last_editor: "Yash Mehta"
last_editor_url: https://stackoverflow.com/users/20172954
tags: [python, string, join, split]
score: -2
views_at_snapshot: 398
answer_count: 7
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 81ebdfed1ec1ceb79cf0301d66243abdba28cb17c57aebf9bae78eae0586e519
---

# How to split and join specific letters of a string in Python?

Asked by [Heindryk](https://stackoverflow.com/users/21353284) on Stack Overflow, <https://stackoverflow.com/q/75669245>, 2023-03-08, last edited 2023-03-08 by [Yash Mehta](https://stackoverflow.com/users/20172954). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am a newbie in Python and ran into something I thought it is easy.


Let's say, I have strings with two letters, `'al'` in random positions, e.g.:

```
original_words = "installation alcohol international"
```
How can I split the original_words into letters but at the same time join letters `"a"` and `"l"`?
  
**The output I would like to achieve**:
```
['i', 'n', 's', 't', 'al', 'l', 'a', 't', 'i', 'o', 'n', 'al', 'c', 'o', 'h', 'o', 'l', 'i', 'n', 't', 'e', 'r', 'n', 'a', 't', 'i', 'o', 'n', 'al']
```
Thanks, a lot.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[John Gordon](https://stackoverflow.com/users/494134)** (2023-03-08): Simplest way would probably be to make a list of single letters, then iterate over the list and join consecutive a's and l's together.
