---
title: "python: beautiful soup extracting info"
site: stackoverflow
question_id: 74240934
answer_id: 74240966
url: https://stackoverflow.com/a/74240966
author: "Andrej Kesely"
author_url: https://stackoverflow.com/users/10035985
posted: 2022-10-28T21:11:54Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ae0d0d5c127f8d49a486151307fdf96283b595f507a1785a12f8be99547aed08
role: another answer on the same question, kept as context; not my work
---

# Answer by [Andrej Kesely](https://stackoverflow.com/users/10035985) — 2022-10-28

Posted on Stack Overflow, <https://stackoverflow.com/a/74240966>, 2022-10-28. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Use `lambda tag: tag.name == "h3" and "Investment" in tag.text`:

```py
from bs4 import BeautifulSoup

html_content = """
<h3 style="cear: both;">
<abbr title="European Union">EU</abbr>Investment</h3>
<div class="conditions">
<p>bla bla bla
</p>
</div>
<p style="margin-bottom: 0;">
<span class="amount">66000 €</span>
</p>"""


soup = BeautifulSoup(html_content, "lxml")

amount = (
    soup.find(lambda tag: tag.name == "h3" and "Investment" in tag.text)
    .find_next("span", class_="amount")
    .text
)
print(amount)
```

Prints:

    66000 €

---

You can use CSS selectors too:

```py
amount = soup.select_one("h3:-soup-contains('Investment') ~ * .amount").text
print(amount)
```

Prints:

    66000 €
