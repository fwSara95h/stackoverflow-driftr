---
title: "beautifulsoup - obtaining the tag and it's parent from the text inside?"
site: stackoverflow
question_id: 74270903
answer_id: 74271051
url: https://stackoverflow.com/a/74271051
author: "user18708372"
author_url: (account no longer exists)
posted: 2022-11-01T02:55:29Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f003ad8a499778295b6d94cbff466e73e0840258b58cd8e0878c34d6cc479296
role: another answer on the same question, kept as context; not my work
---

# Answer by user18708372 (account no longer exists) — 2022-11-01

Posted on Stack Overflow, <https://stackoverflow.com/a/74271051>, 2022-11-01. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

```python3
for tag in soup.findAll(True, text="Top Rated Movies"):
    print(tag.name)
```
