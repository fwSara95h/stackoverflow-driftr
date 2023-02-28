---
title: "Json Exercise to dictionary using python"
site: stackoverflow
question_id: 75594559
answer_id: 75594605
url: https://stackoverflow.com/a/75594605
author: "R. Baraiya"
author_url: https://stackoverflow.com/users/13888486
posted: 2023-02-28T16:11:58Z
last_edited: 2023-02-28T16:40:58Z
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 812d5085a888048ba5985dbd540b78df346a846e88e30741bb560c4adf15623a
role: another answer on the same question, kept as context; not my work
---

# Answer by [R. Baraiya](https://stackoverflow.com/users/13888486) — 2023-02-28

Posted on Stack Overflow, <https://stackoverflow.com/a/75594605>, 2023-02-28, last edited 2023-02-28. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You can update your json directly as:

    department[1]['employees'].append(employee)
    department

    #output
        [{'ID': 1,
      'Name': 'John',
      'Role': 'Manager',
      'employees': [{'ID': 4, 'Name': 'Mike', 'Role': 'Engineer'}]},
     {'ID': 3,
      'Name': 'Sam',
      'Role': 'Manager',
      'employees': [{'ID': [2], 'Name': 'Jack', 'Role': 'Analyst'}]}]
