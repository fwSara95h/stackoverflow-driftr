# Code from my Stack Overflow answer https://stackoverflow.com/a/75516107 (posted 2023-02-21), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# import pandas as pd
# import numpy as np

df = pd.DataFrame({ 'id': [0, 1, 2], 'nm': ['pn1','pn2','pn3'], 
                    'v': [np.nan, 25, 0], 
                    'd': [{'k1':'v1'},{'k2':'v2'},{'k3':'v3'}] })
dtd = { 'pn1':{'s':100,'v':20, 'sv':{'sv1': 500}},
        'pn2':{'s':150,'v':30, 'sv':{'sv1': 400}}  }

# --- block 2 ---
def getVal(obj, *keys, vDef=None):
    try: 
        for k in keys: obj = obj[k]
    except: obj = vDef
    return obj

# --- block 3 ---
sv1 = df['nm'].map(lambda k: getVal(dtd, k, 'sv', 'sv1', vDef=np.nan))
# sv1 = df['nm'].apply(lambda k: getVal(dtd, k, 'sv', 'sv1', vDef=np.nan))

df['v'] = sv1.combine_first(df['v'])

# --- block 4 ---
df['v'] = df['nm'].combine(df['v'], lambda k,vd: getVal(dtd,k,'sv','sv1',vDef=vd))

# --- block 5 ---
df['v'] = [getVal(dtd,k,'sv','sv1',vDef=vd) for k,vd in zip(df['nm'],df['v'])]

# --- block 6 ---
> ╒════╤══════╤══════╤═════╤══════════════╕
> │    │   id │ nm   │   v │ d            │
> ╞════╪══════╪══════╪═════╪══════════════╡
> │  0 │    0 │ pn1  │ 500 │ {'k1': 'v1'} │
> ├────┼──────┼──────┼─────┼──────────────┤
> │  1 │    1 │ pn2  │ 400 │ {'k2': 'v2'} │
> ├────┼──────┼──────┼─────┼──────────────┤
> │  2 │    2 │ pn3  │   0 │ {'k3': 'v3'} │
> ╘════╧══════╧══════╧═════╧══════════════╛
>
