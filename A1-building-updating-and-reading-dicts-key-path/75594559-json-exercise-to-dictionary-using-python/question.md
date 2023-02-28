---
title: "Json Exercise to dictionary using python"
site: stackoverflow
question_id: 75594559
url: https://stackoverflow.com/q/75594559
asked: 2023-02-28T16:08:33Z
asked_by: "Sebastian Hanania"
asked_by_url: https://stackoverflow.com/users/7858604
last_edited: 2023-02-28T16:38:01Z
tags: [python, json, python-3.x, dictionary]
score: 0
views_at_snapshot: 109
answer_count: 4
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 149673e951bb9b8eb9d2cbf47a63549ca9d3013236e4e6385cd9075bca2018cc
---

# Json Exercise to dictionary using python

Asked by [Sebastian Hanania](https://stackoverflow.com/users/7858604) on Stack Overflow, <https://stackoverflow.com/q/75594559>, 2023-02-28, last edited 2023-02-28. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm doing a course and I'm a little complicated with this exercise

I have 2 json that I have to join in a dictionary, but this must meet certain rules.

    department = [
     {"ID": 1, "Name": "John", "Role": "Manager", "employees" :[
     {"ID": 4, "Name": "Mike", "Role": "Engineer"}]},
     {"ID": 3, "Name": "Sam", "Role": "Manager", "employees" :[]
     }]
    employee = { "ID": [2],"Name": "Jack", "Role": "Analyst"}

1- The employee of Identifier 2 is under the charge of the Manager with Identifier 3.

2- The Database where the information will be ingested does not support columns of different data types.
  To do this, a function must be generated that corrects this in the inputs.

3- The expected output must be a nested dictionary

How can I manage to join these fulfilling all conditions?

And the expected result should be this:

[![enter image description here][1]][1]


  [1]: https://i.sstatic.net/K8ufO.png

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Alexander](https://stackoverflow.com/users/17829451)** (2023-02-28): Who is the employee of identifier 2?
- **[R. Baraiya](https://stackoverflow.com/users/13888486)** (2023-02-28): Can you give your desire output json ?
- **[Sebastian Hanania](https://stackoverflow.com/users/7858604)** (2023-02-28): I just added the desire output, it should be nested dictionary
