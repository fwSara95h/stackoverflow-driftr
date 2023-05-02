---
title: "Group list of files based on their size"
site: stackoverflow
question_id: 76156046
url: https://stackoverflow.com/q/76156046
asked: 2023-05-02T14:41:18Z
asked_by: "Paul"
asked_by_url: https://stackoverflow.com/users/17122431
last_edited: 2023-05-02T15:08:56Z
last_editor: "ted"
last_editor_url: https://stackoverflow.com/users/3867406
tags: [python, list, nested]
score: 0
views_at_snapshot: 117
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2c694035da846ec217b6fd045509f899e6a3af13ee75ce5ba44ec84e5b39d0f3
---

# Group list of files based on their size

Asked by [Paul](https://stackoverflow.com/users/17122431) on Stack Overflow, <https://stackoverflow.com/q/76156046>, 2023-05-02, last edited 2023-05-02 by [ted](https://stackoverflow.com/users/3867406). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a sorted list of files.
I need to make a nested list from a list, grouping the files as follows (without changing the original list sequence):
so that the total size of the grouped files does not exceed 100 Kilobytes.

list   -    `['Doc3.pdf', 'Doc4.pdf', 'Doc2.pdf', 'Doc5.pdf', 'Doc1.pdf', 'Doc6.pdf']`

file size -      `30KB        60KB        120KB       20KB        10KB        35KB`

output - `[['Doc3.pdf', 'Doc4.pdf'], ['Doc2.pdf'], ['Doc5.pdf', 'Doc1.pdf', 'Doc6.pdf']]`


To find out the file size I use 

```
os.path.getsize("nameOfFile")
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[HMH1013](https://stackoverflow.com/users/17457846)** (2023-05-02): May this helps : https://stackoverflow.com/a/66538511/17457846
