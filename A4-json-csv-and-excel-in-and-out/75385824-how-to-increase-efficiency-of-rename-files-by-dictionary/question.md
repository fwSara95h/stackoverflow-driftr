---
title: "How to increase efficiency of rename files by dictionary value according to keywords(keys) from dictionary?"
site: stackoverflow
question_id: 75385824
url: https://stackoverflow.com/q/75385824
asked: 2023-02-08T12:30:33Z
asked_by: "Victor Pan"
asked_by_url: https://stackoverflow.com/users/21093275
last_edited: 2023-02-08T16:59:28Z
last_editor: "Driftr95 (me)"
last_editor_url: https://stackoverflow.com/users/6146136
tags: [python, list, dictionary, for-loop, python-os]
score: 0
views_at_snapshot: 94
answer_count: 1
accepted_answer_id: 75391748
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c8b1964dcad916c7158675c611fe8c4814ffec733bbe487c9184c0322f3c031a
---

# How to increase efficiency of rename files by dictionary value according to keywords(keys) from dictionary?

Asked by [Victor Pan](https://stackoverflow.com/users/21093275) on Stack Overflow, <https://stackoverflow.com/q/75385824>, 2023-02-08, last edited 2023-02-08 by me. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I try to rename files by the dictionary value according to the keywords(key) I have. The old name of the files is a long string containing the keywords(key) not exactly the same!! I want to find the key included in the file name and rename the file by the corresponding value. The value should be the new name for all files. The dictionary structure would look like the table below:

Dictionary name: `nameKeyWords`

| Key (Keywords)| Value (Name) |
|-|-|
| abb           | 1            |
| ave           | 2            |
| asp           | 3            |


Below is the code I wrote, and it does work. However, the code is very inefficient because I use three for loop to go through all the files, `keywords`(keys) in the dictionary, and all the `file_name` in `file_names`. Is there any method that can make the code more efficient? Thanks!

```python
for (dir_path, dir_names, file_names) in walk(dir_path):
    for file_name in file_names:
        for keyWords in nameKeyWords:
            if keyWords in file_name:
                old_name = os.path.join(dir_path,file_name)
                new_name = os.path.join(dir_path,nameKeyWords.get(keyWords)+'.csv')
                os.rename(old_name, new_name)
            else:
                print(file_name)
```
