---
title: "Removing square brackets from dictionary"
site: stackoverflow
question_id: 75595013
url: https://stackoverflow.com/q/75595013
asked: 2023-02-28T16:49:23Z
asked_by: "nat-zad"
asked_by_url: https://stackoverflow.com/users/19701280
last_edited: 2023-02-28T16:50:22Z
last_editor: "Barmar"
last_editor_url: https://stackoverflow.com/users/1491895
tags: [python, database, dictionary]
score: -1
views_at_snapshot: 927
answer_count: 1
accepted_answer_id: 75598002
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 79b2b2040d9ba907673949325ccde521db68553f526ea141f70e03f87888ac6f
---

# Removing square brackets from dictionary

Asked by [nat-zad](https://stackoverflow.com/users/19701280) on Stack Overflow, <https://stackoverflow.com/q/75595013>, 2023-02-28, last edited 2023-02-28 by [Barmar](https://stackoverflow.com/users/1491895). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am working from a dataframe and one of my columns has square brackets enclosing a dictionary. I am trying to remove square brackets to map items from the dictionary.

Looks like this:
```
[{'name': 'Steve', 'type': 'Candy', 'likes': '2', 'confidence': '0', 'country': {'confidence': '0.0', 'abrv': 'STV', 'name': 'USA'}, 'region': 'North Amercica', 'subregion': 'Southern Asia', 'state': {'confidence': '0.0', 'numer': '0000', 'name': 'Sindh'},'class': 'High School'}]
```

I tried using str.strip('[]']) but it makes a NaN. 

Is there a way to just remove the square brackets and keep the information in tact?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[buran](https://stackoverflow.com/users/4046632)** (2023-02-28): You have one-element list. So `your_dict = your_list[0]`.
- **[Barmar](https://stackoverflow.com/users/1491895)** (2023-02-28): That means it's a list of dictionaries. Just index it with `[0]`.
- **[nat-zad](https://stackoverflow.com/users/19701280)** (2023-02-28): @Barmar Every row shows this type of list. My goal us to use the code below on every row in the column to extract the country name. I hae used this code successfully on the other columns which dont have the square brackets.  df.COLUMN.map(lambda x: x['country']['name'])
- **me** (2023-02-28): @nat-zad have you tried anything like `df.COLUMN.map(lambda x: x[0] if isinstance(x, list) and len(x)==1 else repr(x).strip('[]'))` ?
- **[nat-zad](https://stackoverflow.com/users/19701280)** (2023-02-28): @Driftr95 thank you for your response & suggestion. This removes the square brackets and replaces them with quotation marks. `"{'name': 'Steve', 'type': 'Candy', 'likes': '2', 'confidence': '0', 'country': {'confidence': '0.0', 'abrv': 'STV', 'name': 'USA'}, 'region': 'North Amercica', 'subregion': 'Southern Asia', 'state': {'confidence': '0.0', 'numer': '0000', 'name': 'Sindh'},'class': 'High School'}"` I still can't extract from the row as I have in other columns & I am stuck. I only need the curly brackets in place. Thanks again!
