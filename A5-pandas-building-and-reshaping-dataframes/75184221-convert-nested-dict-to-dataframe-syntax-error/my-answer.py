# Code from my Stack Overflow answer https://stackoverflow.com/a/75196824 (posted 2023-01-21), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def flattenDict(orig:dict, kList=[], kSep='_', rename={}):
    if not isinstance(orig, dict): return [(kList, orig)]
    tList, dCt = [], len([v for v in orig.values() if isinstance(v,dict)])
    for k, v in orig.items():
        kli = kList + ([] if isinstance(v,dict) and dCt==1 else [str(k)])
        tList += flattenDict(v, kli, None)
    if not isinstance(kSep, str): return tList
    return {kSep.join([rename.get(k,k) for k in kl]):v for kl,v in tList}

# --- block 2 ---
# import pandas as pd
nrMap = {'current':'cur','reference':'ref'}
rows = [flattenDict(result, rename=nrMap) for result in reprex_dict['metrics']]
rowsDf = pd.DataFrame(rows)

# --- block 3 ---
> [{'metric': 'DatasetCorrelationsMetric',
>   'cur_pearson_target_prediction_correlation': None,
>   'cur_pearson_abs_max_features_correlation': 0.1,
>   'cur_cramer_v_target_prediction_correlation': None,
>   'cur_cramer_v_abs_max_features_correlation': None,
>   'ref_pearson_target_prediction_correlation': None,
>   'ref_pearson_abs_max_features_correlation': 0.7,
>   'ref_cramer_v_target_prediction_correlation': None,
>   'ref_cramer_v_abs_max_features_correlation': None}]
>

# --- block 4 ---
rows = [flattenDict(result['result'], rename=nrMap) for result in reprex_dict['metrics']]
