---
title: "I'm having trouble replacing an empty element in a dictionary in python 3.7"
site: stackoverflow
question_id: 75905175
answer_id: 75905361
url: https://stackoverflow.com/a/75905361
author: "Alex"
author_url: https://stackoverflow.com/users/17973259
posted: 2023-04-01T09:36:06Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e9bc0caea4d1abdf0b41ef7a78e86546d4d58e6ff09620cb09ec00aa0dd73fee
role: another answer on the same question, kept as context; not my work
---

# Answer by [Alex](https://stackoverflow.com/users/17973259) — 2023-04-01

Posted on Stack Overflow, <https://stackoverflow.com/a/75905361>, 2023-04-01. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

To update the values of the dictionary, you need to use the key and assign the new value to it and also you should convert the `no_of_tasks_done` variable to an integer using the int() function because the user input will be a string.
This is the version of your code that should work as you want:

    import datetime
    import time
    
    A = {'name': '', 'age': 0, 'tasks done': '', 'number of tasks done': 0}
    name = ''
    age = ''
    tasksdone = ''
    no_of_tasks_done = 0
    
    print("hello 'Worker'")
    time.sleep(2)
    
    name = input("enter name: ")
    age = input("enter age: ")
    tasksdone = input("enter all names given to the tasks you've completed so far: ")
    no_of_tasks_done = int(input("enter the number of tasks done: "))
    
    x = datetime.datetime.now()
    print(x)
    
    A['name'] = name
    A['age'] = age
    A['tasks done'] = tasksdone
    A['number of tasks done'] = no_of_tasks_done
    
    print(A)

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[user19077881](https://stackoverflow.com/users/19077881)** (2023-04-01): Age should also be converted to a `int`. There is no error checking so if user enters such as TWO for number of tasks done then the code will fail with an error message. OP should note that this code forms only a single dictionary and a different structure (eg List of Dictionaries) should be used if the intention is to have multiple sets of entries.
- **[Alex](https://stackoverflow.com/users/17973259)** (2023-04-01): Thank you for pointing those things out and also making it more clear for OP!
