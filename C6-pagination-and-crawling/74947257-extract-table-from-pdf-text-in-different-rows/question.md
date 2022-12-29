---
title: "Extract table from PDF - text in different rows"
site: stackoverflow
question_id: 74947257
url: https://stackoverflow.com/q/74947257
asked: 2022-12-29T04:28:36Z
asked_by: "R. Carrillo"
asked_by_url: https://stackoverflow.com/users/8843206
last_edited: never
tags: [python, pdf, web-scraping, tabula]
score: 0
views_at_snapshot: 5264
answer_count: 1
accepted_answer_id: 74973195
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0ba4b4b339eb5d6b339ef08eff344bd8afbc4f4d94ed5519fc8afb1066287969
---

# Extract table from PDF - text in different rows

Asked by [R. Carrillo](https://stackoverflow.com/users/8843206) on Stack Overflow, <https://stackoverflow.com/q/74947257>, 2022-12-29. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a bunch of PDFs like this: <https://www.premera.com/documents/045632_2023.pdf>

Where there is a large table: Important Questions | Answers | Why this matters. I need to extract that table and have it as CSV. I need CSVs that look like the table in the PDF. The problem: the text of one cell gets split into multiple rows.

I've seen others have had a similar problem but they used these PDFs as images: <https://stackoverflow.com/questions/57210148/what-is-the-best-way-to-extract-text-contained-within-a-table-in-a-pdf-using-pyt> But I still need to use the PDF as "text' (not image).

When I use :

> df = tabula.read_pdf('045632_2023.pdf', pages = 'all')
>
> df\[0\]

The table looks like this. See for example rows 2-4 for the first column (Important Questions). That question, which in the original table was in one cell, is now split into three rows.

[![enter image description here](https://i.sstatic.net/DXDFD.png)](https://i.sstatic.net/DXDFD.png)

When I use :

> df = tabula.read_pdf('045632_2023.pdf', pages='all', lattice=True)
>
> df\[0\]

This partially solves the problem; see row 1 for the first column where the question is now in one cell only. However, there are still plenty of sentences/cells that are split into several rows.

[![enter image description here](https://i.sstatic.net/N1fE1.png)](https://i.sstatic.net/N1fE1.png)

Please, how would you solve this problem? I need to extract that table and have it as CSV. I need CSVs that look like the table in the PDF.
