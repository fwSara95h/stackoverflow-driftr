---
title: "Trying to replace old \"names\" with new \"names\" in Python"
site: stackoverflow
question_id: 75655920
url: https://stackoverflow.com/q/75655920
asked: 2023-03-06T21:15:20Z
asked_by: "Anton Larsson"
asked_by_url: https://stackoverflow.com/users/21345004
last_edited: 2023-03-06T21:18:01Z
last_editor: "jonrsharpe"
last_editor_url: https://stackoverflow.com/users/3001761
tags: [python, excel]
score: 1
views_at_snapshot: 288
answer_count: 2
accepted_answer_id: 75657608
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b92e6e943a8f84a160a154f69f2c65463f1777739c6ee01d672ff20204db5c90
---

# Trying to replace old "names" with new "names" in Python

Asked by [Anton Larsson](https://stackoverflow.com/users/21345004) on Stack Overflow, <https://stackoverflow.com/q/75655920>, 2023-03-06, last edited 2023-03-06 by [jonrsharpe](https://stackoverflow.com/users/3001761). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have two Excel files. One of the Excel files has the new and old names in it in a random order, something like this:
```
Colum A        Colum B
apple-er3      horse-er45
alk-er43       erk-bf43
```
and it continues for around 400 rows.

The other is filled with the old names in a specific order:
```
colum A         colum B
*old name*       *old name*
```
I want to be able to translate all the old names in it with the new.

I was thinking about making a dictionary but I can't figure out a good way of writing it when there are so many names to translate. I would like to go into the Excel with the old names, copy one colum at the time and then paste it into the Python program for it to translate it all to the new names.
