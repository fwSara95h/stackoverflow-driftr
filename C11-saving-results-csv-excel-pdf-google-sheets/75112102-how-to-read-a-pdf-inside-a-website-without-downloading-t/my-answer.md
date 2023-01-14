---
title: "how to read a pdf inside a website without downloading the file"
site: stackoverflow
question_id: 75112102
answer_id: 75115427
url: https://stackoverflow.com/a/75115427
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-14T02:45:28Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75115427/revisions
accepted: false
score: 0
chapter: C11
chapter_title: "Saving results: CSV, Excel, PDF, Google Sheets"
cluster: scrape-to-files-tables
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 478d8a709a9c61d88bc3a226051d09fbc3f1d129a2cfde754d99e211d26d48b0
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-14

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75115427>, 2023-01-14; score 0. Text as retrieved 2026-10-12.

You can try [`io.BytesIO`](https://docs.python.org/3/library/io.html#binary-i-o). For example:

```python
# import io, tabula
pdfUrl = 'https://www.premera.com/documents/052166_2023.pdf'
r = requests.get(pdfUrl, headers={'user-agent': 'Mozilla/5.0'})
r.raise_for_status()
tabula.read_pdf(io.BytesIO(r.content), pages='6')[0]
```

I'm not sure the page link will work as `pdfUrl` since it's embedded, so if `tabula.io` raises some error, try the download link of the pdf instead.
