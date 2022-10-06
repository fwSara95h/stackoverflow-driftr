---
title: "Why is my CSV file coming out empty after code runs w/no errors?"
site: stackoverflow
question_id: 73965600
answer_id: 73970669
url: https://stackoverflow.com/a/73970669
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-06T08:22:18Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73970669/revisions
accepted: true
score: 1
chapter: C11
chapter_title: "Saving results: CSV, Excel, PDF, Google Sheets"
cluster: google-sheets-docs
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 70f7b5164fb765f343990419ebd05e3060f4cc9e76939baea0910d745fafec5a
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-06

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73970669>, 2022-10-06; **accepted**; score 1. Text as retrieved 2026-10-12.

Are you absolutely *sure* the csv is empty? When I ran your code, I noticed that the file *looked* empty when I viewed on Excel, but not if I opened with notepad or Google Sheets, and also that `print(title.text + " - " + desc.text)` shows that the cell entries are surrounded in a lot of whitespace.

So, actually the Excel cells are just showing the whitespace at the beginning because the default format doesn't show more than what fits in the cell. I can see the contents after I:

 1. Select All by pressing `Ctrl`+`A`, and then
 2. Toggle the [Wrap Text](https://support.microsoft.com/en-us/office/wrap-text-in-a-cell-2a18cff5-ccc1-4bce-95e4-f0d4f3ff4e84) setting by pressing `Alt` + `H` + `W` (try toggling once more if there seems to be no difference the first time)

However, the approach I would personally recommend here is to **remove** the whitespaces in the first place - you can do so by using the [`strip()` method](https://www.w3schools.com/python/ref_string_strip.asp) (like `.text.strip()`) or by using `.get_text(strip=True)` instead of `.text`.
