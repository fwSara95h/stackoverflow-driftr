---
title: "beautifulsoup for google search result"
site: stackoverflow
question_id: 76547451
answer_id: 76547487
url: https://stackoverflow.com/a/76547487
author: "diviquery"
author_url: https://stackoverflow.com/users/7776212
posted: 2023-06-24T18:30:25Z
last_edited: never
accepted: false
score: 2
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f01155fbc8ea43e81cb2d1913a6db1a9392719428d8cd919bad66505c91e3ff9
role: another answer on the same question, kept as context; not my work
---

# Answer by [diviquery](https://stackoverflow.com/users/7776212) — 2023-06-24

Posted on Stack Overflow, <https://stackoverflow.com/a/76547487>, 2023-06-24. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

I am assuming you want to change the search keyword, which is the `text` variable in your current code. If that is the case:

You want to use the `sys` module. Here is how you should use:

```python
import sys

text = sys.argv[1]  # Note that sys.argv[0] is the file name itself.
```

Now you can run your file as:
```bash
$ python <file_name.py> <keyword>
```
