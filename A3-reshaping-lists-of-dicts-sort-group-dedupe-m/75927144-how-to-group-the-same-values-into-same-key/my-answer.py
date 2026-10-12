# Code from my Stack Overflow answer https://stackoverflow.com/a/75928321 (posted 2023-04-04), extracted verbatim; may need the question's context to run.
# Includes later revisions by: TylerH (https://stackoverflow.com/users/2756409), revision 2, 2023-04-24, CC BY-SA 4.0.

# --- block 1 ---
result, kList, vData = {}, data[0], data[1:]
for r in vData:
    k_outer, k_inner = r[:2]
    dict_inner = result.setdefault(k_outer, {})
    list_inner = dict_inner.setdefault(k_inner, [])
    list_inner.append(dict(zip(kList, r)))

# --- block 2 ---
# newlist = [dict(zip(data[0],r)) for r in data[1:]] # <-- get newlist from data

result, k_outer_key, k_inner_key = {}, 'num', 'e1'
for r in newlist:
    k_outer, k_inner = r.get(k_outer_key), r.get(k_inner_key)
    dict_inner = result.setdefault(k_outer, {})
    list_inner = dict_inner.setdefault(k_inner, [])
    list_inner.append(r)

# --- block 3 ---
kList, vData = data[0], data[1:]

result = {k_outer: {
    k_inner: [] for k, k_inner, *_ in vData if k==k_outer
} for k_outer in {k1 for k1, *_ in vData}}

for r in vData: result[r[0]][r[1]].append(dict(zip(kList,r)))

## OR 
''' ## [SLIGHTLY LESS EFFICIENT]
kList, vData = data[0], data[1:]
result = {k_outer: {
    k_inner: [dict(zip(kList,x)) for x in vData if x[0]==k_outer and x[1]==k_inner] 
    for k, k_inner, *_ in vData if k==k_outer
} for k_outer in {k1 for k1, *_ in vData}}
'''

# --- block 4 ---
k_outer, k_inner = 'num', 'e1'

result = {k: {
    d.get(k_inner): [] for d in newlist if k==d.get(k_outer)
} for k in {r.get(k_outer) for r in newlist}}

for r in newlist: result[r.get(k_outer)][r.get(k_inner)].append(r)

## OR 
''' ## [SLIGHTLY LESS EFFICIENT]
k_outer, k_inner = 'num', 'e1'
result = {k: {d.get(k_inner): [
    x for x in newlist if x.get(k_outer)==k and x.get(k_inner)==d.get(k_inner)
] for d in newlist if k==d.get(k_outer)} for k in {r.get(k_outer) for r in newlist}}
'''

# --- block 5 ---
> {
>   '2004': {
>     'p': [{'num': '2004', 'e1': 'p', 'e2': 'a', 'e3': 'p'}, {'num': '2004', 'e1': 'p', 'e2': 's', 'e3': 'f'}]
>   },
>   '2002': {
>     'p': [{'num': '2002', 'e1': 'p', 'e2': 'r', 'e3': 'i'}],
>     'k': [{'num': '2002', 'e1': 'k', 'e2': 'r', 'e3': 'i'}]
>   },
>   '2001': {
>     'k': [{'num': '2001', 'e1': 'k', 'e2': 'r', 'e3': 'e'}]
>   }
> }
>
