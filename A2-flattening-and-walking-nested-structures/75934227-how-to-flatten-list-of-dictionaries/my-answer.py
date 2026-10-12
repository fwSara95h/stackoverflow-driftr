# Code from my Stack Overflow answer https://stackoverflow.com/a/75934500 (posted 2023-04-04), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def flatten_obj(obj):
    if hasattr(obj, '__iter__') and not isinstance(obj, str): 
        for i in (obj.values() if isinstance(obj, dict) else obj):
            for v in flatten_obj(i): yield v
    else: yield obj

# --- block 2 ---

---

<br>

Using
- either <kbd>**`{k: list(flatten_obj(v)) for i in process for k,v in i.items()}`**</kbd>
- or <kbd>**`{k: get_flat_list(v) for i in process for k,v in i.items()}`**</kbd>

should return 

>

# --- block 3 ---
if isinstance(obj, str) or not hasattr(obj, '__iter__'): 
    return [obj] if listify_single else obj

if isinstance(obj, dict): obj = obj.values()
return [v for x in obj for v in get_flat_list(x,listify_single=True)]
