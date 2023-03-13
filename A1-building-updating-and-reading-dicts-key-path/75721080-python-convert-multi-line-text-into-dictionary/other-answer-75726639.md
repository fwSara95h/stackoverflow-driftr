---
title: "Python: Convert multi-line text into dictionary"
site: stackoverflow
question_id: 75721080
answer_id: 75726639
url: https://stackoverflow.com/a/75726639
author: "Alain T."
author_url: https://stackoverflow.com/users/5237560
posted: 2023-03-13T20:30:40Z
last_edited: 2023-03-13T21:04:24Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a0dd2f75a31d2ccca8d277edf66fbfd77ed6a56fc1f730a09e3ee576fe44eb89
role: another answer on the same question, kept as context; not my work
---

# Answer by [Alain T.](https://stackoverflow.com/users/5237560) — 2023-03-13

Posted on Stack Overflow, <https://stackoverflow.com/a/75726639>, 2023-03-13, last edited 2023-03-13. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Loop on each line and detect the starting square bracket to start a new group. Use split to get key and value on other lines to update the current group:

    result = dict()
    for line in file:
        if line.startswith("["):
            result[line.strip("[] ")] = group = dict()
        elif "=" in line:
            group.update([line.strip().split("=",1)])
    
    print(result)
    {'ThisShouldBeAKey': {'Value1': 'yes', 'Value2': 'no', 
                          'Value3': 'fancywords', 'Value4': 'numbers'}, 
     'ThisShouldBeAnotherKey': {'Value2': 'true', 'Value3': '333',
                                'Value5': 'qqq'}}
