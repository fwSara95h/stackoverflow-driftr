---
title: "how to print keys of dictionary in coordinate way?"
site: stackoverflow
question_id: 75659579
url: https://stackoverflow.com/q/75659579
asked: 2023-03-07T08:32:17Z
asked_by: "xzha_athena"
asked_by_url: https://stackoverflow.com/users/21338267
last_edited: 2023-03-07T08:41:28Z
tags: [python, dictionary, tuples]
score: -4
views_at_snapshot: 102
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 51c7b0c54473008b35ac58e6de0095f8ba6825c8a79aae5b9f580387b9d7e72e
---

# how to print keys of dictionary in coordinate way?

Asked by [xzha_athena](https://stackoverflow.com/users/21338267) on Stack Overflow, <https://stackoverflow.com/q/75659579>, 2023-03-07, last edited 2023-03-07. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

```
dic2={(0,0):'⬃',(-2,-2):'⇩',(-2,-3):'⇩'}
```

I would like to print the dictionary's values and they can be shown as the position I have allocated. How I can print that?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[R. Baraiya](https://stackoverflow.com/users/13888486)** (2023-03-07): try this `dic2.keys()`
- **[Corralien](https://stackoverflow.com/users/15239951)** (2023-03-07): You can use `list(dic2)` as alternative of `dic2.keys()`.
- **[xzha_athena](https://stackoverflow.com/users/21338267)** (2023-03-07): @Corralien I would like to print the values not keys. like ⬃ in (0,0) ⇩ in (-2,-2)
- **[Talha Tayyab](https://stackoverflow.com/users/13086128)** (2023-03-07): `list(dic2.values())` gives you `['⬃', '⇩', '⇩']`
- **[Corralien](https://stackoverflow.com/users/15239951)** (2023-03-07): @xzha_athena. Oh sorry. Can you check the title of your question?
- **[buran](https://stackoverflow.com/users/4046632)** (2023-03-07): As of python 3.7 the insertion order is preserved, if that is what you mean by _the position I have allocated_. Otherwise, show the expected output
