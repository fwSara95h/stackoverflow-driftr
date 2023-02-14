---
title: "Remove redundant tuples from dictionary based on the score"
site: stackoverflow
question_id: 75448227
answer_id: 75448541
url: https://stackoverflow.com/a/75448541
author: "Dorian Turba"
author_url: https://stackoverflow.com/users/6251742
posted: 2023-02-14T13:29:14Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e0782d21f14fe21a4e02d51fa28f80020cbcf501a247cd7c30d51ffde3d185ea
role: another answer on the same question, kept as context; not my work
---

# Answer by [Dorian Turba](https://stackoverflow.com/users/6251742) — 2023-02-14

Posted on Stack Overflow, <https://stackoverflow.com/a/75448541>, 2023-02-14. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

To remove lower values, you need to detect duplicate, compare, keep track of the higher value, and remove value if a bigger one is found. The algorithm you want is at least time O(n) and space O(n).

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Erwin](https://stackoverflow.com/users/14471688)** (2023-02-14): Can you propose a simple solution?
- **[Dorian Turba](https://stackoverflow.com/users/6251742)** (2023-07-12): Nope, do you homework ;)
