---
title: "Comparing results with Beautiful Soup in Python"
site: stackoverflow
question_id: 74300154
answer_id: 74339445
url: https://stackoverflow.com/a/74339445
author: "Spykerwolf"
author_url: https://stackoverflow.com/users/7770930
posted: 2022-11-06T20:19:00Z
last_edited: never
accepted: true
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: aeebeb63acdb0cb3cb38ef727227c334429b8d3564640d460032d69d4f621894
role: another answer on the same question, kept as context; not my work
---

# Answer by [Spykerwolf](https://stackoverflow.com/users/7770930) — 2022-11-06

Posted on Stack Overflow, <https://stackoverflow.com/a/74339445>, 2022-11-06; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Fixed it with the following:
```
allGuitars = ["",]

latestGuitar = soup.select("#-title")[0].text.strip()

 if latestGuitar in allGuitars[0]:
    print("No change. The latest listing is still: " + allGuitars[0])
  elif not latestGuitar in allGuitars[0]:
    print("New listing detected! - " + latestGuitar)
    allGuitars.clear()
    allGuitars.insert(0, latestGuitar)
```
