---
title: "Parsing inline elements of a paragraph with BeautifulSoup & Python"
site: stackoverflow
question_id: 74778497
answer_id: 74778904
url: https://stackoverflow.com/a/74778904
author: "kevski"
author_url: https://stackoverflow.com/users/17997098
posted: 2022-12-13T00:55:17Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fd79b8fc57cb17157cefc0b8a3fc13ce8c2cc37c49f2f16a21546bd8c66d937c
role: another answer on the same question, kept as context; not my work
---

# Answer by [kevski](https://stackoverflow.com/users/17997098) — 2022-12-13

Posted on Stack Overflow, <https://stackoverflow.com/a/74778904>, 2022-12-13. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Looks like what I was looking for is `.contents` which outputs

```
[<span class="icon-water icon"></span>,
 'Some text...',
 <span class="icon-steel icon"></span>,
 'some more text...']

```

Which gets me in the ballpark of what I'm looking for. Now I can just loop over the elements and apply my desired transformation.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2022-12-13): Yes, you can use `.contents` or `.children` in this case, but if there's some chance of having nested icons like `<p><a href="somelink"><span class="icon-..."></span></a></p>` then you'll need `.descendants` [ofc, if you'll never have a nested `span` then it doesn't really matter which of the three you use]
