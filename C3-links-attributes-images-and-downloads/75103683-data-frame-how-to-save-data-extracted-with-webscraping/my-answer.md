---
title: "Data Frame, how to save data extracted with webscraping?"
site: stackoverflow
question_id: 75103683
answer_id: 75105219
url: https://stackoverflow.com/a/75105219
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-13T05:30:50Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75105219/revisions
accepted: true
score: 1
chapter: C3
chapter_title: "Links, attributes, images and downloads"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 00081eea3f3b28c4351a2d70dd70e856e23c28ba35a6a71460b31fb932242d28
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-13

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75105219>, 2023-01-13; **accepted**; score 1. Text as retrieved 2026-10-12.

<sup>**You should have included what the data in "Youtube.xlsx" and `data` look like. The answer below is suggested with the assumption that they're the same length and that "Youtube.xlsx" has no index column and exactly 3 columns so any added column will be the 4th by default.**</sup>

I don't know what's in "Youtube.xlsx" or in `data`, but the way it's coded `df` will have only one column (`Video`), and `.to_excel` uses write mode by default, so

> Currently, it deletes the contents of all columns and saves the information in column "B"

[I expect it uses column the first column as index, so `Video` ends up as the second column.] If you don't want to write over the previous contents, the usual approach is to append with `mode='a'`; but that will append rows, and [afaik] there is **no way to append columns directly** to a file.

---

You could [read the file into a DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html), then add the column and save.

```python
filepath = r"C:\__Imagens e Planilhas Python\Facebook\Youtube.xlsx"
df = df.read_excel(filepath) #, header=None) # if there is no header row
df['Video'] = links
df.to_excel(filepath, engine='xlsxwriter') #, index=False)
```

[Use a different column name if the file already had a `Video` column that you want to preserve.]

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Felipe](https://stackoverflow.com/users/20021812)** (2023-01-14): perfect, it worked as it should, thanks for the feedback.
- **me** (2023-01-14): @Felipe good to hear, glad it helped
