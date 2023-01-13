---
title: "Data Frame, how to save data extracted with webscraping?"
site: stackoverflow
question_id: 75103683
url: https://stackoverflow.com/q/75103683
asked: 2023-01-13T00:28:54Z
asked_by: "Felipe"
asked_by_url: https://stackoverflow.com/users/20021812
last_edited: 2023-01-14T21:12:34Z
tags: [python, pandas, web-scraping]
score: 1
views_at_snapshot: 53
answer_count: 1
accepted_answer_id: 75105219
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e6a05b2359cca1e1c1a3337c984a86f2fa860f6eb41ae724ee6ae79fc84cafd4
---

# Data Frame, how to save data extracted with webscraping?

Asked by [Felipe](https://stackoverflow.com/users/20021812) on Stack Overflow, <https://stackoverflow.com/q/75103683>, 2023-01-13, last edited 2023-01-14. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a spreadsheet where columns "A", "B" and "C" have data, I need to save the webscraping data in column "D".

Currently, it deletes the contents of all columns and saves the information in column "B", this is my problem, as it should save in column "D" and keep the data from the other columns

I tried the command below and I had no success, because it just created a column named "c".
pd.DataFrame(data, columns=["c"])

[![enter image description here][1]][1]

just below the command I use to save all my webscraping data

    data = {'Video': links} 
    df = pd.DataFrame(data)
    df.to_excel(r"C:\__Imagens e Planilhas Python\Facebook\Youtube.xlsx", engine='xlsxwriter')   
    print(df)


  [1]: https://i.sstatic.net/CnLqB.png
