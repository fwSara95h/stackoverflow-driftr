---
title: "How to use a tuple's 6 values as 6 keys in a dictionary, and print the dictionary's corresponding values?"
site: stackoverflow
question_id: 75299914
url: https://stackoverflow.com/q/75299914
asked: 2023-01-31T16:07:29Z
asked_by: "pythonlearning"
asked_by_url: https://stackoverflow.com/users/17792156
last_edited: 2023-02-02T15:25:58Z
last_editor: "Driftr95 (me)"
last_editor_url: https://stackoverflow.com/users/6146136
tags: [python, dictionary, tuples, key]
score: -1
views_at_snapshot: 68
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5afc4030981812790036cda77c840ce4fb9349e09e6e892103713250832a76e1
---

# How to use a tuple's 6 values as 6 keys in a dictionary, and print the dictionary's corresponding values?

Asked by [pythonlearning](https://stackoverflow.com/users/17792156) on Stack Overflow, <https://stackoverflow.com/q/75299914>, 2023-01-31, last edited 2023-02-02 by me. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I hope to print `flist`(a dictionary)'s corresponding values(6 values in total) based on the all keys(6 keys in total) in a tuple, but how?


The 6 keys in the dictionary is all the tuple's values(6 in total). The dictionary has 100+ key, value pairs


```python
s = pd.Series(files['file_name'] + "." + files['file_type'])

for key, value in s.items():
    print(f" value : {value}")

for value in s:
    if value in flist.keys():
        print(flist.values())  
``` 

I know the last line is not correct, I should print `flist`'s corresponding values(6 values in total) based on the all keys(6 keys in total) in the tuple, but how?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Scott Hunter](https://stackoverflow.com/users/535275)** (2023-01-31): Can you provide sample data & what you hope to produce from it?
- **[PM 77-1](https://stackoverflow.com/users/2055998)** (2023-01-31): Correct indentation in Python code is crucial. [Edit] your question and fix it.
- **[chepner](https://stackoverflow.com/users/1126841)** (2023-01-31): Are you looking for [`operator.itemgetter`](https://docs.python.org/3/library/operator.html?highlight=operator%20itemgetter#operator.itemgetter)? `itemgetter(a, b, c)(d) == (d[a], d[b], d[c])`.
