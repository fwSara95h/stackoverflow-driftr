---
title: "Json Exercise to dictionary using python"
site: stackoverflow
question_id: 75594559
answer_id: 75594963
url: https://stackoverflow.com/a/75594963
author: "Alain T."
author_url: https://stackoverflow.com/users/5237560
posted: 2023-02-28T16:45:39Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ac966a6cd24455c563b78d16feae8544d53e2e8503a6321447a67738ca4dd78c
role: another answer on the same question, kept as context; not my work
---

# Answer by [Alain T.](https://stackoverflow.com/users/5237560) — 2023-02-28

Posted on Stack Overflow, <https://stackoverflow.com/a/75594963>, 2023-02-28. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Because other employee IDs are integers (not lists), you need to extract the first item from the "ID" key to fix the input data.

You can use the next function (or a loop) to find department 3's dictionary in the list (hard coding the position in the list seemed like cheating to me)

Then append the whole employee dictionary to the "employees" list in department 3
    
    employee["ID"] = employee["ID"][0]                        # fix employee ID
    department3 = next(d for d in department if d["ID"] == 3) # find department 3
    department3["employees"].append(employee)                 # add employee
    
result: 
    
    import json
    print(json.dumps(department,indent=2))
    
    [
      {
        "ID": 1,
        "Name": "John",
        "Role": "Manager",
        "employees": [
          {
            "ID": 4,
            "Name": "Mike",
            "Role": "Engineer"
          }
        ]
      },
      {
        "ID": 3,
        "Name": "Sam",
        "Role": "Manager",
        "employees": [
          {
            "ID": 2,
            "Name": "Jack",
            "Role": "Analyst"
          }
        ]
      }
    ]
