---
title: "Why would I get an AttributeError here if I provide an if statement to get around it?"
site: stackoverflow
question_id: 75103179
url: https://stackoverflow.com/q/75103179
asked: 2023-01-12T22:58:39Z
asked_by: "filifunk"
asked_by_url: https://stackoverflow.com/users/6115999
last_edited: never
tags: [python, html, beautifulsoup]
score: 0
views_at_snapshot: 79
answer_count: 1
accepted_answer_id: 75104085
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fe0cf3640c5df2daf9df7a6e89630ab549cc40f763f65278acc00723ce7fcf8c
---

# Why would I get an AttributeError here if I provide an if statement to get around it?

Asked by [filifunk](https://stackoverflow.com/users/6115999) on Stack Overflow, <https://stackoverflow.com/q/75103179>, 2023-01-12. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I've been inspired by the code here: https://towardsdatascience.com/stock-news-sentiment-analysis-with-python-193d4b4378d4

I'm basically scraping news from a financial website using Beautiful Soup. This particular flavor of the code I made is where I'm stumped:

``` 
for i, table_row in enumerate(df_tr): 
    if table_row.a.text is not None: 
        print(table_row.a.text) 
```

I get this error:

`AttributeError: 'NoneType' object has no attribute 'text'`

But I literally provide an if statement that says if that table_row is None, it wont reach the print statement. I even did a version where I put an else statement that tells it to `continue` and I still get the same error. Why is this?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Galo do Leste](https://stackoverflow.com/users/2794417)** (2023-01-12): You haven't provided an if statement that says 'if that table_row is None'. You provided an if statement that says 'if table_row.a.text is not None'. In order to evaluate that statement, python must investigate the value in table_row.a.text. table_row.a is obviously None and hence the error trying to read table_row.a.text. This error occurs in the if statement not the print statement. change it to: if table_row.a is not None
