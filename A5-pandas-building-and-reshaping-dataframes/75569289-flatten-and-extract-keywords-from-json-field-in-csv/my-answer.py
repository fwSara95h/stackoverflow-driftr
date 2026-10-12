# Code from my Stack Overflow answer https://stackoverflow.com/a/75590907 (posted 2023-02-28), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# import pandas as pd 
df = pd.DataFrame({'diff': [
    {'info': {'version': {'from': '2.0.0_1', 'to': '2.3.4_1'}}, 'paths': {'modified': {'/dummy': {'operations': {'added': ['PUT_1']}}}}, 'endpoints': {'added': [{'method': 'PUT_1', 'path': '/dummy_1'}]}, 'components': {'schemas': {'added': ['ObjectOfObjects_1', 'inline_object_1', 'ObjectOfObjects_inner_1']}, 'requestBodies': {'added': ['inline_object_1', 'nested_response_1']}}},
    {'info': {'version': {'from': '2.0.0_2', 'to': '2.3.4_2'}}, 'paths': {'modified': {'/dummy': {'operations': {'added': ['PUT_2']}}}}, 'endpoints': {'added': [{'method': 'PUT_2', 'path': '/dummy_2'}]}, 'components': {'schemas': {'added': ['ObjectOfObjects_2', 'inline_object_2', 'ObjectOfObjects_inner_2']}, 'requestBodies': {'added': ['inline_object_2', 'nested_response_2']}}}
] })

# --- block 2 ---
def try_get(obj, *keys, defaultVal=None):
    try:
        for k in keys: obj = obj[k]
        return obj
    except: return defaultVal

kSep = '.' ## specify a separator
extractKeys = [ ('info', 'version'), 
                ('paths', 'modified'), 
                ('endpoints', 'added'),
                ('components', 'schemas', 'added'), 
                ('components', 'requestBodies', 'added') ]
for kl in extractKeys:
    df[kSep.join(kl)] = df['diff'].map(lambda d: try_get(d, *kl))

# --- block 3 ---
f_df = pd.DataFrame([{
    # kSep.join(kl): try_get(d, *kl) for kl in df['diff'] ## NO diff COLUMN
    'diff': d, **{kSep.join(kl): try_get(d, *kl) for kl in extractKeys}
} for d in df['diff']])

# --- block 4 ---
def flattenDict(obj:dict, kSep='.', kRoot=[], unlistSingles=True):
    if unlistSingles and isinstance(obj, list) and len(obj)==1: return obj[0]
    if isinstance(obj, (list, set, tuple)) and not kRoot:
        return type(obj)(flattenDict(i, kSep, [], unlistSingles) for i in obj)

    if isinstance(obj, dict):
        kJoin = lambda kx: kSep.join(kRoot + [kx])
        flatDict = {}
        for k, v in obj.items():
            fv = flattenDict(v, kSep, kRoot+[k], unlistSingles)
            if not isinstance(fv, dict):
                flatDict[kSep.join(kRoot + [k])] = fv
                continue
            for kn, vn in fv.items(): flatDict[kn] = vn
        return flatDict

    return obj

# f_df = pd.DataFrame(flattenDict(list(df['diff']))) ## NO diff COLUMN
f_df = pd.DataFrame([{'diff': d, **flattenDict(d)} for d in df['diff']])
