# Code from my Stack Overflow answer https://stackoverflow.com/a/75205202 (posted 2023-01-23), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def getNestedVal(obj, kPath:list, defaultVal=None):
    if isinstance(kPath, str) or not hasattr(kPath, '__iter__'): 
        kPath = [kPath] ## if not iterable, wrap as list
    for k in kPath: 
        try: obj = obj[k]
        except: return defaultVal
    return obj 

def func(person):
    filters = [('age', 'age0'), ('name', ['name0', 'first0']),#] 
               ('gender', ['gender0'], 'N/A')] # includes default value
    return {k[0]: getNestedVal(person, *k[1:3]) for k in filters}

# --- block 2 ---
> {'age': '10', 'name': 'John', 'gender': 'N/A'}
>

# --- block 3 ---
def flattenDict(orig:dict, kList=[], kSep='_', stripNum=True):
    if not isinstance(orig, dict): return [(kList, orig)]

    tList = []
    for k, v in orig.items():
        if isinstance(k, str) and stripNum: k = k.strip('0123456789')
        tList += flattenDict(v, kList+[str(k)], None)

    if not isinstance(kSep, str): return tList
    return {kSep.join(kl): v for kl,v in tList}

# --- block 4 ---
> {'name_first': 'John', 'name_last': 'Smith', 'age': '10', 'location_city': 'Dublin'}
>
