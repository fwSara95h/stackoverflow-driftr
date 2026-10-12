# Code from my Stack Overflow answer https://stackoverflow.com/a/75525251 (posted 2023-02-21), extracted verbatim; may need the question's context to run.
def stringify(value, replacer:str=' ', spaces_count:int=1) -> str:
    if not isinstance(value, dict): return str(value) # return repr(value) # 
    curIndent, braceIndent = replacer*spaces_count, replacer*(spaces_count-1)
    unbraced = '\n'.join([ # ',\n'.join([ #
        # f'{curIndent}{repr(k)}: {stringify(v, replacer, spaces_count+1).strip()}' 
        f'{curIndent}{k}: {stringify(v, replacer, spaces_count+1).strip()}' 
        for k, v in value.items()
    ])
    return braceIndent + '{\n' + unbraced + '\n' + braceIndent + '}'

dStr = stringify({ "hello": "world", "is": True, "nested": { "count": 5 } })
