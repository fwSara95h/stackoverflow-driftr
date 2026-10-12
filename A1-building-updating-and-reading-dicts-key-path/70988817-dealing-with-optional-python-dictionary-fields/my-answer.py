# Code from my Stack Overflow answer https://stackoverflow.com/a/75466591 (posted 2023-02-16), extracted verbatim; may need the question's context to run.

# --- block 1 ---
getattr(dictionary2.get("optional"), "get", {}.get)("value1", " ")

# --- block 2 ---
# get_v2 = lambda d, k1, k2, vDef=None: getattr(d.get(k1), 'get', {}.get)(k2,vDef) ## OR
def get_v2(d, k1, k2, vDef=None): 
    return getattr(d.get(k1), 'get', {}.get)(k2,vDef)

a = get_v2(dictionary1, 'optional', 'value1', vDef=' ') ## -->  a='one'
b = get_v2(dictionary2, 'optional', 'value1', vDef=' ') ## -->  b=' '

# --- block 3 ---
def getVal(obj, k1, *keys, vDef=None):
    nxtVal = getattr(obj, 'get', {}.get)(k1, vDef)
    return getVal(nxtVal, *keys, vDef=vDef) if keys else nxtVal

# --- block 4 ---
def getVal(obj, *keys, vDef=None):
    for k in keys: obj = getattr(obj, 'get', {}.get)(k, vDef)
    return obj

# --- block 5 ---
def getVal(obj, k1, *keys, vDef=None):
    try: return getVal(obj[k1], *keys, vDef=vDef) if keys else obj[k1]
    except: return vDef

# --- block 6 ---
def getVal(obj, *keys, vDef=None):
    try: 
        for k in keys: obj = obj[k]
    except: obj = vDef
    return obj

# --- block 7 ---
def valGetter(k1, *keys):
    if keys:
        def rFunc(obj, vDef=None):
            try: 
                for k in (k1,)+(keys): obj = obj[k]
            except: obj = vDef
            return obj
    else: 
        def rFunc(obj, vDef=None):
            try: return obj[k1]
            except: return vDef 
    return rFunc
