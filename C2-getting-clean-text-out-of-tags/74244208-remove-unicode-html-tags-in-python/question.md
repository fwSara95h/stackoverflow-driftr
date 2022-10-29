---
title: "Remove unicode HTML tags in Python"
site: stackoverflow
question_id: 74244208
url: https://stackoverflow.com/q/74244208
asked: 2022-10-29T09:35:10Z
asked_by: "Vishnukk"
asked_by_url: https://stackoverflow.com/users/3152686
last_edited: never
tags: [python, html, css, beautifulsoup]
score: 0
views_at_snapshot: 698
answer_count: 3
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 32ddba2cd2dca883346ca48383604e747af52aced12f38b40d3ea05cf8d02ed3
---

# Remove unicode HTML tags in Python

Asked by [Vishnukk](https://stackoverflow.com/users/3152686) on Stack Overflow, <https://stackoverflow.com/q/74244208>, 2022-10-29. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a string from which I would like to remove the HTML tags.

    

> "overview":"\\u003cp style=\\"margin: 0px 0px 20px; padding: 0px;
> line-height: 20px; outline: none !important; min-height: 1em; color:
> #333333; font-family: Arial, Helvetica, sans-serif, emoji; font-size: 14px; font-style: normal; font-variant-caps: normal; font-weight:
> normal; letter-spacing: normal; orphans: auto; text-indent: 0px;
> text-transform: none; white-space: normal; widows: auto; word-spacing:
> 0px; -webkit-text-size-adjust: auto; text-align:
> center;\\"\\u003e\\u003cspan style=\\"font-family: arial, helvetica,
> sans-serif;\\"\\u003e\\u003cstrong\\u003e\\u003cspan
> style=\\"font-size: 18pt; outline: none !important;\\"\\u003eWTS/VDI macOS\\u003c/span\\u003e\\u003c/strong\\u003e\\u003c/span\\u003e\\u003c/p\\u003e\\n\\u003chr\\u003e\\n\\u003cp\\u003e\\u003cspan ......

I would like to just have 

> "overview":"WTS/VDI macOS.....

I tried with BeautifulSoap and Python Bleach, but it only recognizes if the tags are written in '<' and '>' format. Is there a library or any function which removes this for me? Or should I convert the unicode characters and do it manually?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[G-Cyrillus](https://stackoverflow.com/users/2442099)** (2022-10-29): text-overflow + white-space ? Is this something you tried via CSS or does it need to be reduced from the code itself , not only at screen ?
