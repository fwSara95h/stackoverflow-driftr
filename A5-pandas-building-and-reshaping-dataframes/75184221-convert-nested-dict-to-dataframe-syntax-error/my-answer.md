---
title: "Convert nested dict to dataframe, syntax error?"
site: stackoverflow
question_id: 75184221
answer_id: 75196824
url: https://stackoverflow.com/a/75196824
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-21T21:55:54Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75196824/revisions
accepted: true
score: 1
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: [flattenDict, flattenObj]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d1e712e6ed4dfe3051e9a1d81a8979957540a0d1042b6d50e95392003818c4c0
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-21

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75196824>, 2023-01-21; **accepted**; score 1. Text as retrieved 2026-10-12.

As mentioned in the comments, the `TypeError` is due `result['result']` (which is a dictionary) not being usable as a key. If you used some thing [like `result['metric']`] then the error would no longer be raised, but I think that the [resulting structure][1] is not the outcome you want. 

For flattening nested data, I often take a recursive approach. Below is a simplified version of my [`flattenObj`](https://pastebin.com/v3Fep60B) function:

```python
def flattenDict(orig:dict, kList=[], kSep='_', rename={}):
    if not isinstance(orig, dict): return [(kList, orig)]
    tList, dCt = [], len([v for v in orig.values() if isinstance(v,dict)])
    for k, v in orig.items():
        kli = kList + ([] if isinstance(v,dict) and dCt==1 else [str(k)])
        tList += flattenDict(v, kli, None)
    if not isinstance(kSep, str): return tList
    return {kSep.join([rename.get(k,k) for k in kl]):v for kl,v in tList}
```

---

```python
# import pandas as pd
nrMap = {'current':'cur','reference':'ref'}
rows = [flattenDict(result, rename=nrMap) for result in reprex_dict['metrics']]
rowsDf = pd.DataFrame(rows)
```
> | `rows` |
> |:-:|
> ```python
> [{'metric': 'DatasetCorrelationsMetric',
>   'cur_pearson_target_prediction_correlation': None,
>   'cur_pearson_abs_max_features_correlation': 0.1,
>   'cur_cramer_v_target_prediction_correlation': None,
>   'cur_cramer_v_abs_max_features_correlation': None,
>   'ref_pearson_target_prediction_correlation': None,
>   'ref_pearson_abs_max_features_correlation': 0.7,
>   'ref_cramer_v_target_prediction_correlation': None,
>   'ref_cramer_v_abs_max_features_correlation': None}]
> ```
> ---
>
> | `rowsDf.T` [Transposed to fit better] |
> |:-:|
> | [![opdf][2]][2] |

---

If you don't want the `metric` column, you can either [`drop`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html) it or [omit it][3] by defining `rows` as

```python
rows = [flattenDict(result['result'], rename=nrMap) for result in reprex_dict['metrics']]
```


  [1]: https://i.sstatic.net/VlHHE.png
  [2]: https://i.sstatic.net/vr0H3.png
  [3]: https://i.sstatic.net/Rtst8.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[prayner](https://stackoverflow.com/users/12403550)** (2023-01-22): Amazing, thank you for sharing your approach too as I am learning how to wrangle dicts.
