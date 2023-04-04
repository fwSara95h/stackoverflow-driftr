---
title: "How to flatten list of dictionaries"
site: stackoverflow
question_id: 75934227
url: https://stackoverflow.com/q/75934227
asked: 2023-04-04T22:11:11Z
asked_by: "user1552698"
asked_by_url: https://stackoverflow.com/users/1552698
last_edited: 2023-05-01T17:04:43Z
last_editor: "halfer"
last_editor_url: https://stackoverflow.com/users/472495
tags: [python, list, dictionary]
score: 0
views_at_snapshot: 1046
answer_count: 3
accepted_answer_id: 75934340
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 009b29e6d1e69d9c7e82d693839569d41dce930deeb4b9dcb6532e05839bb2bd
---

# How to flatten list of dictionaries

Asked by [user1552698](https://stackoverflow.com/users/1552698) on Stack Overflow, <https://stackoverflow.com/q/75934227>, 2023-04-04, last edited 2023-05-01 by [halfer](https://stackoverflow.com/users/472495). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am learning how to traverse lists and dictionaries in Python. I am a beginner.

    process = [
                    {
                    'process1':
                                [
                                    {"subprocess1":["subprocess1_1","subprocess1_2"]},
                                    "subprocess2",
                                    {"subprocess3":["subprocess3_1", "subprocess3_2"]},
                                    "subprocess4",
                                    {"subprocess5":[{"subprocess5_1":["subprocess5_1_1","subprocess5_1_2"]}]},
                                ],
                        },
                    {
                    'process2':
                                [
                                    "subprocess2_1"
                                ]
                    }
          ]


How do I flatten above list of dictionaries into the following?

    process1 = [subprocess1, subprocess1_1, subprocess1_2, subprocess2, subprocess3, subprocess3_1, subprocess3_2, subprocess4, subprocess5, subprocess5_1, subprocess5_1_1, subprocess5_1_2]
    process2 = [subprocess2_1]

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Gino Mempin](https://stackoverflow.com/users/2745495)** (2023-04-04): Figure out first how to iterate over a simple flat list (item by item) and a simple flat dictionary (key-value pairs). Once you know that, a nested list of dicts with lists is essentially the same: loop over the outer list, then each item would be a dict, so loop over the keys and values of the dict, then each value of the dict would be a list, so on and on..
