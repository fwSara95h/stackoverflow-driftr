---
title: "how to unnest a list of json objects in dataframe column"
site: stackoverflow
question_id: 75802736
answer_id: 75808253
url: https://stackoverflow.com/a/75808253
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-22T03:38:09Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75808253/revisions
accepted: true
score: 0
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 313b239c45a3adbe94a9af103538ba070cfb137fa4ddf69d4c255543ab8a74bb
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-22

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75808253>, 2023-03-22; **accepted**; score 0. Text as retrieved 2026-10-12.

I don't know if pandas has anything for parsing stringified data like this, and [`json.loads`](https://docs.python.org/3/library/json.html#json.loads) would not work since that's not valid JSON, but you could use [`ast.literal_eval`](https://docs.python.org/3/library/ast.html#ast.literal_eval) and [`pd.json_normalize`](https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html) as below:

```py
# import ast
data = {'tax_info': [[], [{'price': '1.26', 'rate': 0.06, 'title': 'Idaho State Tax', 'price_set': {'shop_money': {'amount': '1.26', 'currency_code': 'USD'}, 'presentment_money': {'amount': '1.26', 'currency_code': 'USD'}}, 'channel_liable': False}], [{'price': '1.98', 'rate': 0.0625, 'title': 'Illinois State Tax', 'price_set': {'shop_money': {'amount': '1.98', 'currency_code': 'USD'}, 'presentment_money': {'amount': '1.98', 'currency_code': 'USD'}}, 'channel_liable': False}, {'price': '0.39', 'rate': 0.0125, 'title': 'Chicago City Tax', 'price_set': {'shop_money': {'amount': '0.39', 'currency_code': 'USD'}, 'presentment_money': {'amount': '0.39', 'currency_code': 'USD'}}, 'channel_liable': False}, {'price': '0.87', 'rate': 0.0275, 'title': 'Cook County Tax', 'price_set': {'shop_money': {'amount': '0.87', 'currency_code': 'USD'}, 'presentment_money': {'amount': '0.87', 'currency_code': 'USD'}}, 'channel_liable': False}]]}

data['tax_info'] = [ast.literal_eval(s) for s in data['tax_info']] 
df = pd.json_normalize(data, ['tax_info', []])

# in one statement, and without altering data:
# pd.json_normalize({**data, 'tax_info': [ast.literal_eval(s) for s in data['tax_info']]}, ['tax_info', []])
```
[![df][1]][1]


  [1]: https://i.sstatic.net/Eh4E3.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[DevNo](https://stackoverflow.com/users/21448649)** (2023-03-23): Yes it is helpful, thanks. But what is the optimal solution to deal with this issue if you have more nested list of dicts in the data. is it to everytime create a new df and go one level deeper?
- **me** (2023-03-23): The issue with multiple nested lists is that pandas doesn't know how you want them aligned with each other. So, I think you'll have to loop through the nested columns and make a list of DataFrames, and then [concat](https://pandas.pydata.org/docs/reference/api/pandas.concat.html) them along the x-axis [if you  have the same length list for all list-cells in any row (i.e, row 1 only has empty lists, row 2 only has lists of length 3, etc)], or merge them [like in this answer](https://stackoverflow.com/a/61197935/6146136)
- **me** (2023-03-23): (I usually flatten my data before converting to a DataFrame, but more because I feel like I have more control that way than for efficiency)
