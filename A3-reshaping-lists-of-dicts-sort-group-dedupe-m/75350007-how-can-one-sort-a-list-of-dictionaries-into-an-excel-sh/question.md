---
title: "How can one sort a list of dictionaries into an excel sheet such that each unique key and one corresponding key are placed into columns?"
site: stackoverflow
question_id: 75350007
url: https://stackoverflow.com/q/75350007
asked: 2023-02-05T03:54:21Z
asked_by: "Sanjiv Prasad"
asked_by_url: https://stackoverflow.com/users/8286578
last_edited: 2023-02-05T09:30:26Z
tags: [python, excel, dictionary]
score: 0
views_at_snapshot: 156
answer_count: 2
accepted_answer_id: 75351812
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7b365814c3394fb1aca914b1b3709f53ae88f3cbd289ff85bfed31d60ee0175e
---

# How can one sort a list of dictionaries into an excel sheet such that each unique key and one corresponding key are placed into columns?

Asked by [Sanjiv Prasad](https://stackoverflow.com/users/8286578) on Stack Overflow, <https://stackoverflow.com/q/75350007>, 2023-02-05, last edited 2023-02-05. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a list of dictionaries organized as such:

```py 
listofdictionaries = [{'key1': (A, B, C), 'key2':[1, 2, 3]}, 
                      {'key1': (AA, BB, CC), 'key2':[1, 2, 3]}, 
                      {'key1': (AAA, BBB, CCC), 'key2':[4, 5, 6]}]
```

This list's first and second items have an equivalent value for key2. The third item has a different value for key2. Still using Python, I want the columns organized as such:



| Group 1 | Group 1 Items | Group 2 | Group 2 Items | 
| -------- | -------- | -------- | -------- | 
| [1, 2, 3]   | (A, B, C)   | [4, 5, 6] | (AAA, BBB, CCC) |
|    | (AA, BB, CC)   |  |  |



In addition I would like the output to be a .csv file.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[ccolin](https://stackoverflow.com/users/8987319)** (2023-02-05): The elements inside the lists in `key2`'s values are unique or can they be repeated? Meaning, could you have {'key2': [1,1,3]}?
- **[Sanjiv Prasad](https://stackoverflow.com/users/8286578)** (2023-02-05): @ccolin They are unique.
