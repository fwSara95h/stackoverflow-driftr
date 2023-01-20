---
title: "Convert nested dict to dataframe, syntax error?"
site: stackoverflow
question_id: 75184221
url: https://stackoverflow.com/q/75184221
asked: 2023-01-20T12:45:51Z
asked_by: "prayner"
asked_by_url: https://stackoverflow.com/users/12403550
last_edited: never
tags: [python, dataframe, dictionary]
score: 0
views_at_snapshot: 59
answer_count: 1
accepted_answer_id: 75196824
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ef2f8de1fd3048e61f36ef27798fa5e910402bc5e7b3662a199fd05c63ff9560
---

# Convert nested dict to dataframe, syntax error?

Asked by [prayner](https://stackoverflow.com/users/12403550) on Stack Overflow, <https://stackoverflow.com/q/75184221>, 2023-01-20. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

#### Problem

I am converting multiple nested dicts to dataframes. I have a slightly different dict that I haven't been able to convert to a dataframe using my attempted solution. I am providing a shortened copy of my dict with dummy values as the reprex. 

#### Reprex dict:
```
{'metrics': [{'metric': 'DatasetCorrelationsMetric',
   'result': {'current': {'stats': {'pearson': {'target_prediction_correlation': None,
       'abs_max_features_correlation': 0.1},
      'cramer_v': {'target_prediction_correlation': None,
       'abs_max_features_correlation': None}}},
    'reference': {'stats': {'pearson': {'target_prediction_correlation': None,
       'abs_max_features_correlation': 0.7},
      'cramer_v': {'target_prediction_correlation': None,
       'abs_max_features_correlation': None}}}}}]}
```

#### My attempted solution
Code is based on similar dict wrangling problems that I had, but I am not sure how to apply it for this specific dict.

    data = {}
    for result in reprex_dict['metrics']:
        data[result['result']] = {
            **{f"ref_{key}": val for key, val in result['result']['reference'].items()},
            **{f"cur_{key}": val for key, val in result['result']['current'].items()}
        }

#### Expected dataframe format:

| cur_pearson_target_prediction_correlation | cur_pearson_abs_max_features_correlation | cur_cramer_v_target_prediction_correlation |
|:---- |------:| -----:|
| None | 0.1 | None | 

#### Error message

I am currently getting this error too.

    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    Cell In [403], line 7
          5 data = {}
          6 for result in corr_matrix_dict['metrics']:
    ----> 7     data[result['result']] = {
          8         **{f"ref_{key}": val for key, val in result['result']['reference']['stats'].items()},
          9         **{f"cur_{key}": val for key, val in result['result']['current']['stats'].items()}
         10     }
    
    TypeError: unhashable type: 'dict'

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Amin S](https://stackoverflow.com/users/20875923)** (2023-01-20): problem is in ur data[result['result']]. your key is a dictionary which u cannot do that
- **[prayner](https://stackoverflow.com/users/12403550)** (2023-01-20): Right, but I don't understand how to access the 'stats' key from the beginning.
- **[Amin S](https://stackoverflow.com/users/20875923)** (2023-01-20): the problem here is how you are defining the keys in data.  the second part works fine.
