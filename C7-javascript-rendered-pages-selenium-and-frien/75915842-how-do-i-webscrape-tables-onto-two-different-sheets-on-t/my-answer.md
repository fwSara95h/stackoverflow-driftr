---
title: "How do I webscrape tables onto two different Sheets on the Excel Spreadsheet?"
site: stackoverflow
question_id: 75915842
answer_id: 75916413
url: https://stackoverflow.com/a/75916413
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-03T06:02:20Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75916413/revisions
accepted: true
score: 1
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e8bc78a2e2a9ca8b92f8d27e8fd85dc0319ca14924c8db6a6011e71c66d71f1c
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-03

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75916413>, 2023-04-03; **accepted**; score 1. Text as retrieved 2026-10-12.

Try using [`ExcelWriter`](https://pandas.pydata.org/docs/reference/api/pandas.ExcelWriter.html#pandas.ExcelWriter) on append mode:

```py
            df = pd.read_html(str(table))[0]
            with pd.ExcelWriter("hkjc.xlsx", 
                                engine="openpyxl", 
                                mode='a', if_sheet_exists='new') as writer:
                df.to_excel(writer, sheet_name=sheet_name, index=True)
```

If you use `if_sheet_exists='replace'`, it will over-write if there's already a `sheet_name` sheet; `if_sheet_exists='overlay'` will add rows in such a case.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[NNBananas](https://stackoverflow.com/users/19672894)** (2023-04-03): Thanks, it worked perfectly! ExcelWriter seems really useful! I'll try and learn how to use it
- **me** (2023-04-03): @NicholasChan glad to help! I was delighted to discover it myself - quite recently as well
