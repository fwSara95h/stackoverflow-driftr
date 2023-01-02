---
title: "How can i get values from 2 lists and put them into a dictionary in python"
site: stackoverflow
question_id: 74984177
url: https://stackoverflow.com/q/74984177
asked: 2023-01-02T15:26:17Z
asked_by: "CodingOwl"
asked_by_url: https://stackoverflow.com/users/19226226
last_edited: never
tags: [python, list, dictionary]
score: -1
views_at_snapshot: 52
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b37258a46308190ecf8a5ecfe53b49038ba51cdad7353b809d0403cba6ed4106
---

# How can i get values from 2 lists and put them into a dictionary in python

Asked by [CodingOwl](https://stackoverflow.com/users/19226226) on Stack Overflow, <https://stackoverflow.com/q/74984177>, 2023-01-02. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have 2 lists
~~~
list1 = ["ben", "tim", "john", "wally"]
list2 = [18,12,34,55]
~~~
the output im looking for is this
~~~
[{'Name': 'ben', 'Age': 18, 'Name': 'tim', 'Age': 12, 'Name': 'john', 'Age': 34, 'Name': 'wally', 'Age': 55}]
~~~

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[DarrylG](https://stackoverflow.com/users/3066077)** (2023-01-02): The output you're looking for is invalid since dictionaries can't have duplicate keys.  Perhaps you meant a list of dictionaries.
- **[CodingOwl](https://stackoverflow.com/users/19226226)** (2023-01-02): thanks, i forgot that keys in a dictionary need to be unique
- **[Daniel Hao](https://stackoverflow.com/users/10760768)** (2023-01-02): @CodingOwl - do you need to revise your problem description to make it clear?
