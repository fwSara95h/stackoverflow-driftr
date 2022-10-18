---
title: "BeautifulSoup to find a HTML tag that contains tags with specific class"
site: stackoverflow
question_id: 74117210
answer_id: 74117379
url: https://stackoverflow.com/a/74117379
author: "Andrej Kesely"
author_url: https://stackoverflow.com/users/10035985
posted: 2022-10-18T20:57:15Z
last_edited: never
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9f715b2be5b0a28fa64c8e445c953923bf61b13606b4570cc644b412eb316ca6
role: another answer on the same question, kept as context; not my work
---

# Answer by [Andrej Kesely](https://stackoverflow.com/users/10035985) — 2022-10-18

Posted on Stack Overflow, <https://stackoverflow.com/a/74117379>, 2022-10-18. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

I suppose you want to find all `<tr>` that contains any tag with class `TD<any character>3`:

```py
import re

# `html` contains your html from the question
soup = BeautifulSoup(html, "html.parser")
pat = re.compile(r"TD.3")

for tr in soup.find_all(
    lambda tag: tag.name == "tr"
    and tag.find(class_=lambda cl: cl and pat.match(cl))
):
    print(tr)
```

Prints:

```html
<tr>
<td class="TDq1"><a href="p.pl?t=410">GpWl(op) 4.01/02</a></td>
<td class="TDq2"><a href="p.pl?t=410&amp;r=4">17.02.02</a></td>
<td class="TDq3">34/75</td>
<td class="TDq5">39. John Deep</td>
<td class="TDq9">68. <a href="p.pl?ply=1229">Mark Deep</a></td>
</tr>
<tr>
<td class="TDp1"><a href="p.pl?t=410">GpWl(op) 4.01/02</a></td>
<td class="TDp2"><a href="p.pl?t=410&amp;r=4">17.02.02</a></td>
<td class="TDp3">34/75</td>
<td class="TDp6">39. John Deep</td>
<td class="TDp8">7. <a href="p.pl?ply=10">Darius Star</a></td>
</tr>
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Tomasz Maciążek](https://stackoverflow.com/users/15698050)** (2022-10-19): That is the best solution because I need insert data from that group of TD insert in single record in DB. Thanks
- **[Tomasz Maciążek](https://stackoverflow.com/users/15698050)** (2022-10-19): And how to extract each TD into element of a record: ["p.pl?t=410", GpWl(op), 4.01/02, "p.pl?t=410&amp;r=4", 17.02.02, 34/75, "TDp6", 39, John Deep ...] TDP6 is when John Deep is loser and TDP5 is when John Deep is winner
