---
title: "Pull value from dictionaries embedded in pandas df"
site: stackoverflow
question_id: 75882977
url: https://stackoverflow.com/q/75882977
asked: 2023-03-29T23:29:50Z
asked_by: "SSD"
asked_by_url: https://stackoverflow.com/users/21521891
last_edited: 2023-03-30T17:29:34Z
tags: [python, pandas, dataframe, dictionary]
score: 0
views_at_snapshot: 92
answer_count: 1
accepted_answer_id: 75894702
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8be17708cfbfb639b07d4c35bc382bfb167a3bbe557860894494e61822877871
---

# Pull value from dictionaries embedded in pandas df

Asked by [SSD](https://stackoverflow.com/users/21521891) on Stack Overflow, <https://stackoverflow.com/q/75882977>, 2023-03-29, last edited 2023-03-30. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have pandas dataframe:

|Name|  A |  B |
| -------- | -------- | -------- |
|$overall| {'all': 26929}   | {'all': 2036}  |
|QWE| {'$overall': {'all': 6},'Mar 18, 2021': {'all': 3},'Mar 3, 2021': {'all': 3}} | {'$overall': {'all': 3},'Mar 3, 2021': {'all': 2},'Mar 18, 2021': {'all': 1} |

Desired output :


|Name|Date|  A |  B |
| -------- | -------- | -------- | -------- |
|XYZ| |26929  | 2036  |
|QWE|Mar 3, 2021 |3   | 2   |
|QWE|Mar 18, 2021| 3| 1 |

I tried below code and got below output:


```
df = df.apply(lambda s: s.str['all']).fillna(0).convert_dtypes()
```

|Name|  A |  B |
| -------- | -------- | -------- | 
|XYZ|26929  | 2036  |
|QWE|0   | 0   |
|QWE| 0| 0 |


```df.dict()``` gives me below: 

```
{'A': {'$XYZ': {'all': 26929},   
'QWE': {'$overall': {'all': 6},    
'Mar 18, 2021': {'all': 3},    
'Mar 3, 2021': {'all': 3}}, }  '
B.': {'$XYZ': {'all': 2036},   
'QWE': {'$overall': {'all': 3},    
'Mar 3, 2021': {'all': 2},    
'Mar 18, 2021': {'all': 1},   }  
'Name': {'$XYZ': '$overall',   
'QWE': 'QWE',   }}}```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Barmar](https://stackoverflow.com/users/1491895)** (2023-03-29): That's not JSON. JSON uses double quotes, not single quotes. It looks like they're just python dictionaries.
- **[SSD](https://stackoverflow.com/users/21521891)** (2023-03-29): That is correct. Its dictionaries.
- **[AlexK](https://stackoverflow.com/users/9987623)** (2023-03-30): Is that the entire input dataframe, or is this just a sample? It's not immediately clear what format each column/cell has and what logic should be implemented. Please add clarifying details.
- **me** (2023-03-30): @SSD can you include a snippet with the result of `df.to_dict()`? I can't reproduce `df` properly like this
- **[Timus](https://stackoverflow.com/users/14311263)** (2023-03-30): The `QWE`-row doesn't contain dictionaries: your sample shows invalid Python objects?
- **[SSD](https://stackoverflow.com/users/21521891)** (2023-03-30): I have updated my question, and `df.dict()` gives me below:  ```{'A': {'$XYZ': {'all': 27026},   'QWE': {'$overall': {'all': 6},    'Mar 18, 2021': {'all': 3},    'Mar 3, 2021': {'all': 3}}, }  'B.': {'$XYZ': {'all': 2042},   'QWE': {'$overall': {'all': 3},    'Mar 3, 2021': {'all': 2},    'Mar 18, 2021': {'all': 1},   }  'Name': {'$XYZ': '$overall',   'QWE': 'QWE',   }}}```  @Driftr95
