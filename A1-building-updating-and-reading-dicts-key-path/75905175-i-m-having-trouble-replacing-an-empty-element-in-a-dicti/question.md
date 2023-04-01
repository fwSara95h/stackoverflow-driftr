---
title: "I'm having trouble replacing an empty element in a dictionary in python 3.7"
site: stackoverflow
question_id: 75905175
url: https://stackoverflow.com/q/75905175
asked: 2023-04-01T09:01:55Z
asked_by: "mr. code"
asked_by_url: https://stackoverflow.com/users/21228735
last_edited: 2023-04-01T16:59:33Z
tags: [python, dictionary, object, input]
score: 0
views_at_snapshot: 98
answer_count: 3
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 46c6fa5157c22e4fb6e851ae3f904daa451dd3c2da3c57aa4d2e3fbb6f0266da
---

# I'm having trouble replacing an empty element in a dictionary in python 3.7

Asked by [mr. code](https://stackoverflow.com/users/21228735) on Stack Overflow, <https://stackoverflow.com/q/75905175>, 2023-04-01, last edited 2023-04-01. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to find a way to replace an empty object in python but it never worked out


here is the code i tried

```
import datetime
import time

A = {'name : '', ' 'age': 0, 'tasks done': '', 'number of tasks done': 0}
name = ''
age = ''
tasksdone = ''
no_of_tasks_done = 0
print("hello 'Worker'")
time.sleep(2)
name = input("enter name")
age = input("enter age")
tasksdone = input("enter all names given to the tasks you've completed so far")
no_of_tasks_done = input("enter the number of tasks done")

x = datetime.datetime.now()
print(x)
A['name'] : A[name]
A['a'] = A[age]

```
ignore datetime for now 
its not yet finished because i need to solve this problem
the user is supposed to make an input into the console and its supposed to put it in the object list
i dont know why it failed
please help me

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[jackal](https://stackoverflow.com/users/17580381)** (2023-04-01): I suggest you start by printing *A*. It's almost certainly not what you want
