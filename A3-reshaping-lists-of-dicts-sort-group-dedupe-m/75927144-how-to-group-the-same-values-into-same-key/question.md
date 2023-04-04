---
title: "How to group the same values into same key?"
site: stackoverflow
question_id: 75927144
url: https://stackoverflow.com/q/75927144
asked: 2023-04-04T08:29:29Z
asked_by: "user21308739"
asked_by_url: https://stackoverflow.com/users/21308739
last_edited: 2023-04-04T09:47:05Z
last_editor: "Cwt"
last_editor_url: https://stackoverflow.com/users/1091453
tags: [python, python-3.x, dictionary, nested, iterable-unpacking]
score: -3
views_at_snapshot: 83
answer_count: 1
accepted_answer_id: 75928321
closed: 2023-04-04T21:57:15Z (Needs details or clarity)
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8558f52f1f13e2841728ef4d40496ee9f773dcf996e4a7139bd34ee0ee7522ec
---

# How to group the same values into same key?

Asked by [user21308739](https://stackoverflow.com/users/21308739) on Stack Overflow, <https://stackoverflow.com/q/75927144>, 2023-04-04, last edited 2023-04-04 by [Cwt](https://stackoverflow.com/users/1091453). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have an assignment to do this things without import any helpful function, could you guys help me?
Thanks!


    data = [
        ['num','e1','e2','e3'],
        ['2002','p','r','i'],
        ['2002','k','r','i'],
        ['2001','k','r','e'],
        ['2004','p','a','p'],
        ['2004','p','s','f']
    ]

    newlist = [
        {'num': '2001', 'e1': 'k', 'e2': 'r', 'e3': 'e'},
        {'num': '2002', 'e1': 'p', 'e2': 'r', 'e3': 'i'},
        {'num': '2002', 'e1': 'k', 'e2': 'r', 'e3': 'i'},
        {'num': '2004', 'e1': 'p', 'e2': 'a', 'e3': 'p'},
        {'num': '2004', 'e1': 'p', 'e2': 's', 'e3': 'f'}
    ]

How can I convert `newlist` into this by `num` is main key and next key is `e1`

    {
        '2001':{
            'k':[{'num': '2001', 'e1': 'k', 'e2': 'r', 'e3': 'e'}]
        },
        '2002':{
            'k':[{'num': '2002', 'e1': 'k', 'e2': 'r', 'e3': 'i'}],
            'p':[{'num': '2002', 'e1': 'p', 'e2': 'r', 'e3': 'i'}]
        },
        '2004':{
            'p':[{'num': '2004', 'e1': 'p', 'e2': 'a', 'e3': 'p'}, {'num': '2004', 'e1': 'p', 'e2': 's', 'e3': 'f'}]
        }
    }

2001 and 2002 have only k and k have only one data so it will be the only one member of k
you will see its form `{ num:  {e1: [ {'num':..., 'e1': ..., 'e2': ... }, ... ], ...}, ... }`

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[motto](https://stackoverflow.com/users/21146235)** (2023-04-04): There are many [previous questions](https://stackoverflow.com/a/69587757/21146235) on this topic, perhaps they would be helpful to look at
- **[Gameplay](https://stackoverflow.com/users/15923186)** (2023-04-04): You didn't provide the code you've tried and from my POV the description is completely not understandable to be honest.
- **[TylerH](https://stackoverflow.com/users/2756409)** (2023-04-24): @Gameplay Note that code being added is only a requirement for debugging questions. This being a 'how to' question, code is not required.
