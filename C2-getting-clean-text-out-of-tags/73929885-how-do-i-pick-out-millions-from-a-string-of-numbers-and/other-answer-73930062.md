---
title: "How do I pick out millions from a string of numbers and commas?"
site: stackoverflow
question_id: 73929885
answer_id: 73930062
url: https://stackoverflow.com/a/73930062
author: "kosciej16"
author_url: https://stackoverflow.com/users/3361462
posted: 2022-10-02T23:42:38Z
last_edited: never
accepted: false
score: 2
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 26507a0fe0d538dd511c08868c3bff3397b802f11d2d57424985674382ddb35d
role: another answer on the same question, kept as context; not my work
---

# Answer by [kosciej16](https://stackoverflow.com/users/3361462) — 2022-10-02

Posted on Stack Overflow, <https://stackoverflow.com/a/73930062>, 2022-10-02. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

If you are sure of the format you have, the simplest I found is:
```
s = "42,965,39136,483,93920,139,65822,588,85825,067,279"
end = prev_end = 0
while end < len(s):
    # find next comma position. Milion end is 8 positions later
    end = s.index(",", end) + 8
    my_milion = s[prev_end:end]
    print(my_milion) # or int(my_milion.replace(",", "")) if you want integer
    prev_end = end
```
