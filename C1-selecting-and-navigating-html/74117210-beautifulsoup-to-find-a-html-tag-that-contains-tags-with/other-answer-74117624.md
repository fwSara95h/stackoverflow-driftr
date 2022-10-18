---
title: "BeautifulSoup to find a HTML tag that contains tags with specific class"
site: stackoverflow
question_id: 74117210
answer_id: 74117624
url: https://stackoverflow.com/a/74117624
author: "amirmohamad"
author_url: https://stackoverflow.com/users/18765925
posted: 2022-10-18T21:23:56Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 647103a5277df0c41f3d8d30586a47387bf0021d1cce93bd0afc1a7a1703b397
role: another answer on the same question, kept as context; not my work
---

# Answer by [amirmohamad](https://stackoverflow.com/users/18765925) — 2022-10-18

Posted on Stack Overflow, <https://stackoverflow.com/a/74117624>, 2022-10-18. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

This may help you:
```
from bs4 import BeautifulSoup
import re

t = 'your page source' 
pat = re.compile(r'class=TD.3')
classes = re.findall(pat,t)
classes = [j[6:] for j in classes]
soup = BeautifulSoup(t)
result = list()
for i in classes:
    item = soup.find_all(attrs={"class": i})
    result.extend(item)
for i in result:
    print(i.parent)
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Tomasz Maciążek](https://stackoverflow.com/users/15698050)** (2022-10-19): {NameError}name 'mtable' is not defined in re.py
