---
title: "bs4.element.Tag and split, python"
site: stackoverflow
question_id: 76489877
answer_id: 76498923
url: https://stackoverflow.com/a/76498923
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-06-18T03:27:11Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/76498923/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ede0846e64e82061ea0b0a5293a4c32bd31e89a33a424434a42f2c1fa3488d2e
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-06-18

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76498923>, 2023-06-18; score 0. Text as retrieved 2026-10-12.

The error is due to *`match.find({'div': {'class': 'matchDayHeadline'}})`* not finding anything; you cannot apply `.split()` to a result that does not exist, so the error is raised. 

Also, `.split` is generally applied to strings, not Tags. Try

```py
        date = match.find({'div': {'class': 'matchDayHeadline'}})
        if date: date = date.text.split()[-1]
```

Note that this will only avoid the error, so you might just get <kbd>`date`=**`None`**</kbd> instead. If it's happening consistently, you should inspect *`data.solution.response`* more carefully to see if you're using the correct class or if the date field even exists in the fetched html.
