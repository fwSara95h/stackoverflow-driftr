---
title: "Python: can not save all links to a dict in json file, only the last one"
site: stackoverflow
question_id: 76530648
answer_id: 76530683
url: https://stackoverflow.com/a/76530683
author: "rochard4u"
author_url: https://stackoverflow.com/users/19593035
posted: 2023-06-22T09:55:34Z
last_edited: never
accepted: false
score: 2
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5a5cb12bceaf49f6155a8289878c1e49fecb47ed993963db2d8da23d8780acc1
role: another answer on the same question, kept as context; not my work
---

# Answer by [rochard4u](https://stackoverflow.com/users/19593035) — 2023-06-22

Posted on Stack Overflow, <https://stackoverflow.com/a/76530683>, 2023-06-22. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

This is because `all_links_dict[number + 1] = value_links` is not in your `for item in name_link` loop. Hence you only add to the dict once.

You must also increment number in the loop.
```python
for item in name_link:
    value_links = ("https://www.sothebysrealty.com" + item.get("href"))
    all_links_dict[number] = value_links
    number += 1
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Swifty](https://stackoverflow.com/users/20267366)** (2023-06-22): If I may add a comment for @Alberi , using a dict whose keys are actually indexes seems useless: simply use a list in this case.
