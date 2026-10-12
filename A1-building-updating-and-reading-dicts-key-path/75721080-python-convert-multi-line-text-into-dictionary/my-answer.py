# Code from my Stack Overflow answer https://stackoverflow.com/a/75737946 (posted 2023-03-14), extracted verbatim; may need the question's context to run.

# --- block 1 ---
filepath = 'x.txt' #<-- name of / path to your file

with open(filepath, 'r') as f: fLines = f.read().splitlines() #<-- read file
kCur = '__no_parent_key__' #<-- set a default for if 1st line isn't a [key]
result = {kCur: {}} #<-- initiate

for l in fLines:
    if '=' in l: _, l = result[kCur].update([l.split('=', 1)]), ''# [l empty -> skip]

    l = l.strip()
    if not l: continue #<-- skip empty lines

    kCur = l[1:-1] if (l[0], l[-1]) == ('[', ']') else l #<-- trim [] 
    result.setdefault(kCur, {})

# remove '__no_parent_key__' if empty:
if not result['__no_parent_key__']: del result['__no_parent_key__']

# --- block 2 ---
> { 
>   'ThisShouldBeAKey': {'Value1': 'yes', 'Value2': 'no', 'Value3': 'fancywords', 'Value4': 'numbers'},
>   'ThisShouldBeAnotherKey': {'Value2': 'true', 'Value3': '333', 'Value5': 'qqq'} 
> }
>

# --- block 3 ---
kwList = {'true':True, 'false':False, 'null': None, 'none': None}
def try_eval(literalStr:str, kwRef=kwList):
    if literalStr.strip().lower() in kwRef: 
        return kwRef[literalStr.strip().lower()]
    try: return ast.literal_eval(literalStr)
    except: return literalStr

# --- block 4 ---
if '=' in l: 
    k, v = l.split('=', 1) 
    result[kCur][k] = try_eval(v)
    continue
