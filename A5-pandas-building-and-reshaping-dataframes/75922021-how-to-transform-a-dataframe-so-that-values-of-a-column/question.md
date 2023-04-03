---
title: "How to transform a dataframe so that values of a column are the column names and column names are rows but unstacked?"
site: stackoverflow
question_id: 75922021
url: https://stackoverflow.com/q/75922021
asked: 2023-04-03T17:04:20Z
asked_by: "Yisroel Len"
asked_by_url: https://stackoverflow.com/users/16627602
last_edited: never
tags: [python, pandas, data-transform]
score: 2
views_at_snapshot: 119
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d6071739353baa1c9a40a3d5795988b195dc2a98488738fb4171258c60451f12
---

# How to transform a dataframe so that values of a column are the column names and column names are rows but unstacked?

Asked by [Yisroel Len](https://stackoverflow.com/users/16627602) on Stack Overflow, <https://stackoverflow.com/q/75922021>, 2023-04-03. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm comparing two tables to monitor for changes. I need a resulting table that shows a before and after the change per user per attribute changed. 

I used the pandas .compare method and below is an example of my current result, but I can't figure out what the next steps would be. If I'm going about this completely wrong feel free to let me know as well.

I currently have a table that looks like this:

| User ID | Name | Favorite | Status |
| -------- | -------- | ------ | ------ |
| 1   | Steve | Chocolate | Before |
| 2   | John | Chocolate | Before |
| 1   | Stevy | Chocolate | After |
| 2   | John | Vanilla | After |

I need it to look like this:

| User ID| Attribute Changed | Before | After |
| -------- | -------- | -------- | -------- |
| 1 | Name | Steve | Stevy |
| 2 | Name | John | John |
| 1 | Favorite | Chocolate | Chocolate |
| 2 | Favorite | Chocolate | Vanilla |

I can eliminate the lines where no changes were made.
