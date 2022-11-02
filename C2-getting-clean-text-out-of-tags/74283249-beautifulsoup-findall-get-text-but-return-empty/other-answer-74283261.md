---
title: "BeautifulSoup findall get text but return empty"
site: stackoverflow
question_id: 74283249
answer_id: 74283261
url: https://stackoverflow.com/a/74283261
author: "Andrej Kesely"
author_url: https://stackoverflow.com/users/10035985
posted: 2022-11-02T00:48:21Z
last_edited: never
accepted: true
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b51bdd540c1d7c17462532d911bc99eecdf5e0692aa05263d45f93e2a2a5e201
role: another answer on the same question, kept as context; not my work
---

# Answer by [Andrej Kesely](https://stackoverflow.com/users/10035985) — 2022-11-02

Posted on Stack Overflow, <https://stackoverflow.com/a/74283261>, 2022-11-02; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Try `.contents[0]`:

```py
from bs4 import BeautifulSoup


html_doc = """\
<style>
    th { border: none; }
</style>"""

soup = BeautifulSoup(html_doc, "html5lib")

print(soup.find("style").contents[0])
```

Prints:

```none

    th { border: none; }

```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[user15410844](https://stackoverflow.com/users/15410844)** (2022-11-02): I use `soup.find_all('style')[0].contents`, and it works! Thank you!
