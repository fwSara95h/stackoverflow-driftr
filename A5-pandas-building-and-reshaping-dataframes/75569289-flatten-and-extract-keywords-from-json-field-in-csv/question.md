---
title: "Flatten and extract keywords from json field in csv"
site: stackoverflow
question_id: 75569289
url: https://stackoverflow.com/q/75569289
asked: 2023-02-26T00:26:07Z
asked_by: "Brie MerryWeather"
asked_by_url: https://stackoverflow.com/users/17192742
last_edited: 2023-06-20T15:43:14Z
tags: [python, json, pandas]
score: 0
views_at_snapshot: 189
answer_count: 1
accepted_answer_id: 75590907
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 377188106936e891a4197f1e787cc14ace379ac329da0267c487ed187a7fd464
---

# Flatten and extract keywords from json field in csv

Asked by [Brie MerryWeather](https://stackoverflow.com/users/17192742) on Stack Overflow, <https://stackoverflow.com/q/75569289>, 2023-02-26, last edited 2023-06-20. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I want to flatten the json,meaning divided all the parameters, so that means I get around 5-6 new columns( as these are all the parameters changing,first set of elements)

so I get output as something as follows:


```
info      paths      endpoints  components
version    modified   added      schemas:added
                                 requestBodies:added
```

I looked into `json_normalize` , `flatten` and `jsonpath`, but somehow neither of these work for the use case. It yields a completely different output to the one I want. It would be really great if someone could help me with this! I seem to be a bit stuck.


  [1]: https://i.sstatic.net/PbXC9.png

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Lukas Hestermeyer](https://stackoverflow.com/users/5240684)** (2023-02-28): Can you explain a bit more what the output is supposed to be? I dont understand your explanation. Are those different columns? Is the first row the expected header and the rest values?
- **[Brie MerryWeather](https://stackoverflow.com/users/17192742)** (2023-02-28): I edited the question to make it more clear, I hope its understandable now, if not, I will add further clarification
- **[Tranbi](https://stackoverflow.com/users/13525512)** (2023-02-28): It's still not clear what values should appear in your output. What would be `version` under `info` in your example? (value associated with `from` or `to` or something else?) Same question for the other fields: should `added` keys be filled with the corresponding values (lists like `['ObjectOfObjects', 'inline_object', 'ObjectOfObjects_inner']` for `schemas:added` in your case..)? `paths:modified` value is a dict: shall it appear in the output as a dict?
- **[fabianegli](https://stackoverflow.com/users/6018688)** (2023-02-28): Hi, you label the question as "pandas" but don't actually provide an example data structure in pandas. Please add one to make it clear what the input is and ideally also construct the desired output. Do you want `MultiIndex` in the result? Or not?
- **[Lukas Hestermeyer](https://stackoverflow.com/users/5240684)** (2023-02-28): @BrieMerryWeather, it would help if you could create a table with the values you are expecting and not only the headers. You can just use markdown to create a table here for the one row that you provided on top.
