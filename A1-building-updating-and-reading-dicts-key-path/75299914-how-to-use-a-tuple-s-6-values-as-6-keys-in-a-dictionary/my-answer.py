# Code from my Stack Overflow answer https://stackoverflow.com/a/75341756 (posted 2023-02-03), extracted verbatim; may need the question's context to run.
def get_tuple_of_values(dict_w100plus_kvp:dict, keysRef, defaultVal=None):
    return tuple(dict_w100plus_kvp.get(k,defaultVal) for k in keysRef)
