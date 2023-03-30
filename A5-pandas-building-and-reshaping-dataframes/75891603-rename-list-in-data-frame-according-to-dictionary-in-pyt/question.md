---
title: "rename list in data frame according to dictionary in Python"
site: stackoverflow
question_id: 75891603
url: https://stackoverflow.com/q/75891603
asked: 2023-03-30T18:09:10Z
asked_by: "Михаил Беляков"
asked_by_url: https://stackoverflow.com/users/16432167
last_edited: 2023-03-30T21:23:05Z
last_editor: "wjandrea"
last_editor_url: https://stackoverflow.com/users/4518341
tags: [python, pandas, dictionary, lambda]
score: -1
views_at_snapshot: 70
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b350aff87f5eedc9e2b1768751bda5c728c56a2dc4ff7850e1220d4118c8e680
---

# rename list in data frame according to dictionary in Python

Asked by [Михаил Беляков](https://stackoverflow.com/users/16432167) on Stack Overflow, <https://stackoverflow.com/q/75891603>, 2023-03-30, last edited 2023-03-30 by [wjandrea](https://stackoverflow.com/users/4518341). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

it is necessary to create a column with the name according to their code. I have a dictionary, I'm trying to rename codes to titles. There are two conditions, because the code may not be in the dictionary, then you need to write the code, or if the code field is empty, then write the void.if there is only one code, everything works, if there are several codes, a problem arises

[![enter image description here](https://i.sstatic.net/LjXwQ.png)](https://i.sstatic.net/LjXwQ.png)
[![enter image description here](https://i.sstatic.net/J6uQL.png)](https://i.sstatic.net/J6uQL.png)


I tried to write a lambda function
```
missing_values = {}
dict_=dict_name
dict_fr=pd.DataFrame.from_dict(dict_name, orient='index')
dict_fr.index=dict_fr.index.map(str)
for_ag_pivot['name_cod']=for_ag_pivot['cod_last'].apply(lambda x: ",".join(dict_fr[0].loc[str(x).split(',')].tolist() if x in dict_name.keys() else x))

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[wjandrea](https://stackoverflow.com/users/4518341)** (2023-03-30): The question is completely unclear. Maybe you would prefer to ask on [ru.so]? Otherwise, check out [ask] and [How to make good reproducible pandas examples](/q/20109391/4518341). Either way, [please don't post pictures of text](https://meta.stackoverflow.com/q/285551/4518341).
