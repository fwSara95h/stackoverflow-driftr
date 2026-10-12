# Code from my Stack Overflow answer https://stackoverflow.com/a/75653416 (posted 2023-03-06), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def kvCombine(obj:list):
    if isinstance(obj, dict): obj = list(obj.items()) 
    if not isinstance(obj, list): return obj
    obj = [t for lt in [
        list(o.items()) if isinstance(o,dict) else [o] for o in obj
    ] for t in lt]

    if not all(isinstance(t, tuple) and len(t)==2 for t in obj): return obj
    kList = set(k for k, v in obj)
    kvPairs = [(ki, [v for k, v in obj if k==ki]) for ki in kList]
    return {k: v[0] if len(v)==1 else kvCombine(v) for k, v in kvPairs}

def dict_graph(pList):
    if not isinstance(pList, list): return pList
    if not pList: return None # {} # []
    if len(pList)==1: return dict_graph(pList[0])

    if any(isinstance(p, list) for p in pList):
        return kvCombine([  (p,None) if not isinstance(p,list) else 
                            (p[0],dict_graph(p[1:])) for p in pList if p!=[] ])

    if len(pList)==2: return {pList[0]: pList[1]}
    return {pList[0]: dict_graph(pList[1:])}

# --- block 2 ---
example = [[ 'a', 'b', 'c', 'd'], [ 'a', 'b', 'e', 'f'], [ 'g', 'h']]
example_graph = dict_graph(example)

# --- block 3 ---
> {'a': {'b': {'c': 'd', 'e': 'f'}}, 'g': 'h'}
>
