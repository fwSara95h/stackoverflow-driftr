# Code from my Stack Overflow answer https://stackoverflow.com/a/76448138 (posted 2023-06-10), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def yield_key_paths(objC, valT, kPath=None, validTypes=(tuple,list,dict,set)):
    ''' Traverse objC data structure recursively to yield path/s to valT'''

    if not isinstance(kPath, list): kPath = []
    if objC == valT: yield kPath
    if not isinstance(objC, validTypes): return 

    for k,v in (objC.items() if isinstance(objC,dict) else enumerate(objC)):
        yield from yield_key_paths(v, valT, kPath+[k], validTypes)



def find_nested_val(obj, val, findAll=False, validTypes=(tuple,list,dict,set)):
    '''Get a list of or the first path to val in obj (No path -> [] or None)'''

    paths = yield_key_paths(obj, val, [], validTypes)
    return list(paths) if findAll else next(paths, None)

# --- block 2 ---
thisdict = {"brand": {"color":"Red","model": "Mustang"},
            "manufactured": {"year":"1964","month":"Oct"}}

find_nested_val(thisdict, 'Red') ## --> ['brand', 'color']
find_nested_val(thisdict, 'Red', findAll=True) ## --> [['brand', 'color']]

find_nested_val(thisdict, '1966') ## --> None # since it cannot be found
find_nested_val(thisdict, '1966', findAll=True) ## --> []
find_nested_val(thisdict, '1964') ## --> ['manufactured', 'year']

find_nested_val(thisdict, thisdict) ## --> []
find_nested_val(thisdict, thisdict, findAll=True) ## --> [[]]

# --- block 3 ---
## !pip install -U varname
## from varname import nameof

def abc(*args):
    print(nameof(args[0], frame=2))
    ###### OTHER CODE ######

abc(thisdict, thisdict["brand"]["color"],"111","222") ## --> prints `thisdict`

# --- block 4 ---
def abc(*args):
    dictname = nameof(args[0], frame=2)

    for v in args[1:]:
        vPath = find_nested_val(args[0], v)
        if vPath is None: print(f'!!{v!r} could not be found in {dictname}!!')
        else:
            vPath = ']['.join([repr(k) for k in vPath])
            if vPath: vPath = f'[{vPath}]'
            print(f'{dictname}{vPath} = {v!r}')
