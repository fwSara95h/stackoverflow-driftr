---
title: "Flatten and extract keywords from json field in csv"
site: stackoverflow
question_id: 75569289
answer_id: 75590907
url: https://stackoverflow.com/a/75590907
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-28T10:42:35Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75590907/revisions
accepted: true
score: 1
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: [flattenDict]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: aa0a8ade1345ee31710388ccd05852e2c249e87ef6115a3086585449ac241d80
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-28

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75590907>, 2023-02-28; **accepted**; score 1. Text as retrieved 2026-10-12.

If you had [for example] a DataFrame `df` with a `diff` column containing nested dictionaries as below:

```py
# import pandas as pd 
df = pd.DataFrame({'diff': [
    {'info': {'version': {'from': '2.0.0_1', 'to': '2.3.4_1'}}, 'paths': {'modified': {'/dummy': {'operations': {'added': ['PUT_1']}}}}, 'endpoints': {'added': [{'method': 'PUT_1', 'path': '/dummy_1'}]}, 'components': {'schemas': {'added': ['ObjectOfObjects_1', 'inline_object_1', 'ObjectOfObjects_inner_1']}, 'requestBodies': {'added': ['inline_object_1', 'nested_response_1']}}},
    {'info': {'version': {'from': '2.0.0_2', 'to': '2.3.4_2'}}, 'paths': {'modified': {'/dummy': {'operations': {'added': ['PUT_2']}}}}, 'endpoints': {'added': [{'method': 'PUT_2', 'path': '/dummy_2'}]}, 'components': {'schemas': {'added': ['ObjectOfObjects_2', 'inline_object_2', 'ObjectOfObjects_inner_2']}, 'requestBodies': {'added': ['inline_object_2', 'nested_response_2']}}}
] })
```

[I'm assuming that the dictionaries in `diff` are not stringified; if they are, then they should be parsed with `json.loads`/`ast.literal_eval`/etc.]

---

You could [`.map`](https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html) specific nested values to additional columns with something like 

```py
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
```

[![op1][1]][1]

If you wanted the new columns in a new DataFrame instead of adding to `df`:

```py
f_df = pd.DataFrame([{
    # kSep.join(kl): try_get(d, *kl) for kl in df['diff'] ## NO diff COLUMN
    'diff': d, **{kSep.join(kl): try_get(d, *kl) for kl in extractKeys}
} for d in df['diff']])
```

---

Or, if you just wanted to flatten all the nested dictionaries in `diff`:

```py
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
```

[![op2][2]][2]


  [1]: https://i.sstatic.net/sNmWW.png
  [2]: https://i.sstatic.net/4IrH4.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Brie MerryWeather](https://stackoverflow.com/users/17192742)** (2023-03-01): this was quite helpful, thank you so much for your help!
