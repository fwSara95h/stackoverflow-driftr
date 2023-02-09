---
title: "Python converting a list in a nested dictionary into a Pandas Dataframe"
site: stackoverflow
question_id: 75404195
url: https://stackoverflow.com/q/75404195
asked: 2023-02-09T20:39:09Z
asked_by: "griefter"
asked_by_url: https://stackoverflow.com/users/20800402
last_edited: 2023-02-09T21:18:37Z
last_editor: "wjandrea"
last_editor_url: https://stackoverflow.com/users/4518341
tags: [python, json, pandas, dictionary]
score: 1
views_at_snapshot: 178
answer_count: 1
accepted_answer_id: 75404500
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 63354df8583eb528bfb2efd34d6954e6f9d080bc9fb6648c3304492b61b9492c
---

# Python converting a list in a nested dictionary into a Pandas Dataframe

Asked by [griefter](https://stackoverflow.com/users/20800402) on Stack Overflow, <https://stackoverflow.com/q/75404195>, 2023-02-09, last edited 2023-02-09 by [wjandrea](https://stackoverflow.com/users/4518341). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have the following dictionary
```
test = {'data': [
  {'actions': [
    {'action_type': 'link_click', 'value': '16'},
    {'action_type': 'post_engagement', 'value': '16'},
    {'action_type': 'page_engagement', 'value': '16'}],
   'spend': '13.59',
   'date_start': '2023-02-07',
   'date_stop': '2023-02-07'},
  {'actions': [
    {'action_type': 'comment', 'value': '5'},
    {'action_type': 'onsite_conversion.post_save', 'value': '1'},
    {'action_type': 'link_click', 'value': '465'},
    {'action_type': 'post', 'value': '1'},
    {'action_type': 'post_reaction', 'value': '20'},
    {'action_type': 'video_view', 'value': '4462'},
    {'action_type': 'post_engagement', 'value': '4954'},
    {'action_type': 'page_engagement', 'value': '4954'}],
   'spend': '214.71',
   'date_start': '2023-02-07',
   'date_stop': '2023-02-07'}]}
```
And I am trying to convert it where each element after action type is a pandas DataFrame column, and the value as row. Something like
```
link_click post_engagement page_engagement   spend comment onsite_conversion ...
        16              16              16   13.59     N/A               N/A
       465            4954            4954  214.71       5                 1
```
I understand that the first list does not have comment, post, etc, and the rows would be N/A. How do I manage this complicated data structure?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[wjandrea](https://stackoverflow.com/users/4518341)** (2023-02-09): I'm not quite sure how to work this, but you might try using [`json_normalize`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.json_normalize.html), then you might need to do a pivot. Or I suppose you could do it manually :| i.e. use Python structures like list comprehensions and such.
