---
title: "how to unnest a list of json objects in dataframe column"
site: stackoverflow
question_id: 75802736
url: https://stackoverflow.com/q/75802736
asked: 2023-03-21T14:50:25Z
asked_by: "DevNo"
asked_by_url: https://stackoverflow.com/users/21448649
last_edited: 2023-03-22T02:24:23Z
last_editor: "Driftr95 (me)"
last_editor_url: https://stackoverflow.com/users/6146136
tags: [python, json, pandas, dataframe, nested]
score: -1
views_at_snapshot: 609
answer_count: 1
accepted_answer_id: 75808253
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ba4d8fdc58802c6a819e952a8c8105678c9c7cba6cc568255c0a18237953295f
---

# how to unnest a list of json objects in dataframe column

Asked by [DevNo](https://stackoverflow.com/users/21448649) on Stack Overflow, <https://stackoverflow.com/q/75802736>, 2023-03-21, last edited 2023-03-22 by me. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

What are the possible ways to unnest a list of nested json objects inside a dataframe column and join again with the same dataframe.

e.g.:

```py
data = {
 'tax_info': [
  '[]',
  "[{'price': '1.26', 'rate': 0.06, 'title': 'Idaho State Tax', 'price_set': {'shop_money': {'amount': '1.26', 'currency_code': 'USD'}, 'presentment_money': {'amount': '1.26', 'currency_code': 'USD'}}, 'channel_liable': False}]",
  "[{'price': '1.98', 'rate': 0.0625, 'title': 'Illinois State Tax', 'price_set': {'shop_money': {'amount': '1.98', 'currency_code': 'USD'}, 'presentment_money': {'amount': '1.98', 'currency_code': 'USD'}}, 'channel_liable': False}, {'price': '0.39', 'rate': 0.0125, 'title': 'Chicago City Tax', 'price_set': {'shop_money': {'amount': '0.39', 'currency_code': 'USD'}, 'presentment_money': {'amount': '0.39', 'currency_code': 'USD'}}, 'channel_liable': False}, {'price': '0.87', 'rate': 0.0275, 'title': 'Cook County Tax', 'price_set': {'shop_money': {'amount': '0.87', 'currency_code': 'USD'}, 'presentment_money': {'amount': '0.87', 'currency_code': 'USD'}}, 'channel_liable': False}]"
 ]
}
```

[sample df column](https://i.sstatic.net/DY7Tc.png)

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[inspectorG4dget](https://stackoverflow.com/users/198633)** (2023-03-21): Please edit your post to include the sample data, rather than posting a screenshot. Please also include the expected output in your post
