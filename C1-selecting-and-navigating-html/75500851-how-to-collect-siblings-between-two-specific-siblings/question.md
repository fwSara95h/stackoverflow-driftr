---
title: "How to collect siblings between two specific siblings?"
site: stackoverflow
question_id: 75500851
url: https://stackoverflow.com/q/75500851
asked: 2023-02-19T14:33:34Z
asked_by: "user16950345"
asked_by_url: (account no longer exists)
last_edited: 2023-02-20T09:49:20Z
tags: [python, web-scraping, beautifulsoup]
score: 0
views_at_snapshot: 63
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 90f1d20a35d851bab9f48f560da9a1d962c41f1d9e5513034448c10277daa904
---

# How to collect siblings between two specific siblings?

Asked by user16950345 (account no longer exists) on Stack Overflow, <https://stackoverflow.com/q/75500851>, 2023-02-19, last edited 2023-02-20. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have an html book with many `<h2>` headers and I want to collect the content after each of them using `beautifulsoup`. This is my current code which crashes, because it is just adding over and over again every sibling through the entire document and then repeating the element loop:

```
chapter_data = []

for e in soup.select('h2'): # select the tags

    chapter = ''

    for sib in e.next_siblings:

        if sib.name == 'h2':
            break
        
        chapter += str(sib)
        
        # add data to list
        chapter_data.append({
            'chapter': e.get_text(strip=True).split()[-1],
            'text': chapter
        })


chapters = pd.DataFrame(chapter_data)
```

The goal is getting each chapter into its own cell. I figured that this would collect all the siblings and content after each `<h2></h2>` tag separately to store it in a list. There are a lot of headings and I could manually do this, but I would like to know the proper code that could do this for me.


I tried an `extract()` method but this doesn't work either.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[HedgeHog](https://stackoverflow.com/users/14460824)** (2023-02-19): Does this answer your question? [How to extract all <p> with its corresponding <h2>?](https://stackoverflow.com/questions/73756733/how-to-extract-all-p-with-its-corresponding-h2)
- **user16950345 (account no longer exists)** (2023-02-19): that doesn't quite answer it. though it's close. I need all the tags included, not just the text, and it appends data into a dictionary that can't be converted easily to a dataframe as my code intends
- **[HedgeHog](https://stackoverflow.com/users/14460824)** (2023-02-20): First and foremost, it should be a suggestion that can be adapted and a `dict` is predestined to generate a `dataframe` from it - but it is nice to see that it comes close. Probably an improvement of the question with details, an HTML example structure / URL and the expected result would allow a more targeted answer. Would be great and I am curious about the use case. Thanks
