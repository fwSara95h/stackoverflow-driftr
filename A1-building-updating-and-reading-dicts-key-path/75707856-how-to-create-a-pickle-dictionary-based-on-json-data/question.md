---
title: "How to create a Pickle dictionary based on JSON data"
site: stackoverflow
question_id: 75707856
url: https://stackoverflow.com/q/75707856
asked: 2023-03-11T18:19:23Z
asked_by: "kseny a."
asked_by_url: https://stackoverflow.com/users/21378721
last_edited: never
tags: [python, json, pickle]
score: -3
views_at_snapshot: 158
answer_count: 1
accepted_answer_id: 75710236
closed: 2023-03-12T14:13:13Z (Not suitable for this site)
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8a83339e91b058e1c7ffeae15cc273e63d01cca1d0c644bb437538643ea314bc
---

# How to create a Pickle dictionary based on JSON data

Asked by [kseny a.](https://stackoverflow.com/users/21378721) on Stack Overflow, <https://stackoverflow.com/q/75707856>, 2023-03-11. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

# Hi!
I need to create a dictionary as:
> {
> job: [list of 'username', who has this job title in json data]
> }

Heres the json data

```
{'address': '01261 Cameron Spring\nTaylorfurt, AK 97791',
 'id': 35193,
 'jobs': ['Energy engineer',
          'Engineer, site',
          'Environmental health practitioner',
          'Biomedical scientist',
          'Jewellery designer'],
 'mail': 'jsalazar@gmail.com',
 'name': 'Lindsey Nguyen',
 'sex': 'F',
 'username': 'uhebert'}
{'address': '66992 Welch Brooks\nMarshallshire, ID 56004',
 'id': 91970,
 'jobs': ['Music therapist',
          'Volunteer coordinator',
          'Designer, interior/spatial'],
 'mail': 'bhudson@gmail.com',
 'name': 'Cheryl Lewis',
 'sex': 'F',
 'username': 'vickitaylor'}
{'address': 'Unit 1632 Box 2971\nDPO AE 23297',
 'id': 1848091,
 'jobs': ['Management consultant',
          'Engineer, structural',
          'Lecturer, higher education',
          'Theatre manager',
          'Designer, textile'],
 'mail': 'darren44@yahoo.com',
 'name': 'Julia Allen',
 'sex': 'F',
 'username': 'sheilaadams'}
{'address': '9880 Michelle Bridge\nNew Kimberlybury, WY 02583',
 'id': 50969,
 'jobs': ['Mechanical engineer', 'Retail banker', 'Barrister'],
 'mail': 'stevensonsarah@hotmail.com',
 'name': 'Gina Stevens',
 'sex': 'F',
 'username': 'nicole82'}
{'address': '9080 Monica Crescent Suite 820\nNorth Deanbury, HI 28977',
 'id': 676820,
 'jobs': ['Network engineer',
          'Youth worker',
          'Primary school teacher',
          'Engineer, broadcasting (operations)'],
 'mail': 'denise42@gmail.com',
 'name': 'Nicholas Harrington',
 'sex': 'M',
 'username': 'jean67'}
{'address': '635 Kenneth Ways Suite 172\nHancockfort, AZ 50544',
 'id': 64918,
 'jobs': ['Designer, ceramics/pottery',
          'Engineer, energy',
          'Engineer, manufacturing'],
 'mail': 'monique02@hotmail.com',
 'name': 'Allison Gomez',
 'sex': 'F',
 'username': 'james67'}
```


I had few ideas how to make it, but unfortunately it didn't work. It has to be done with pickle and then saved as file named "job_people.pickle"

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Robert](https://stackoverflow.com/users/1431720)** (2023-03-11): Welcome to stackoverflow. This is not a free code-writing service. We can help with problems in your code, but we don't do your homework for you. See [ask].
- **[chepner](https://stackoverflow.com/users/1126841)** (2023-03-11): You won't do this "with" `pickle`. You have a stream of JSON objects you'll have to parse to a sequence of Python `dict`s, which you'll then have to manipulate to create the final expected `dict`. *Then* you can just use the `pickle` module to serialize the `dict` and write it to disk.
