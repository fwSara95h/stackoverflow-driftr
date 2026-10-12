# Code from my Stack Overflow answer https://stackoverflow.com/a/75338566 (posted 2023-02-03), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def yieldNestedVals(obj, key):
    if isinstance(obj, str): return
    try: yield obj[key]
    except: pass
    if isinstance(obj, dict): obj = obj.values()
    for i in (obj if hasattr(obj, '__iter__') else []):
        for v in yieldNestedVals(i, key): yield v

# --- block 2 ---
def search(name, params, defaultVal=None):
    for v in yieldNestedVals(params, name): return v # return 1st generated value
    return defaultVal # if nothing if generated

# --- block 3 ---
# p = [{'quantity': 1}, {'args': {'id': 12345678, 'age': 12}}]
{k: search(k, p) for k in ['quantity', 'args', 'id', 'age', 'dneKey']}

# --- block 4 ---
> {'quantity': 1,
>  'args': {'id': 12345678, 'age': 12},
>  'id': 12345678,
>  'age': 12,
>  'dneKey': None}
>
