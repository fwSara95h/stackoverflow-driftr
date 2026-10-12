# Code from my Stack Overflow answer https://stackoverflow.com/a/75598002 (posted 2023-02-28), extracted verbatim; may need the question's context to run.
import ast
def try_parse(obj, unlistSingles=True, enforceType=None, defaultVal=None):
    if isinstance(obj, str) and enforceType!=str:
        try: obj = ast.literal_eval(obj) ## safer than just eval
        except: pass
    if isinstance(obj, list) and len(obj)==1 and enforceType!=list: obj = obj[0]
    if isinstance(enforceType,type):
        if isinstance(obj,enforceType): return obj
        try: obj = enforceType(obj)
        except: return defaultVal
    return obj
