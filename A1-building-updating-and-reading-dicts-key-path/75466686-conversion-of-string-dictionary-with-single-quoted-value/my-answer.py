# Code from my Stack Overflow answer https://stackoverflow.com/a/75467703 (posted 2023-02-16), extracted verbatim; may need the question's context to run.

# --- block 1 ---
dictStr = '''{'first_name': "John", "age": 89}'''

dictObj = eval(dictStr)
print('dictObj:', type(dictObj), repr(dictObj), '\n')

# import json
jsonStr = json.dumps(eval(dictStr))
print('jsonStr:', type(jsonStr), repr(jsonStr), '\n')

# --- block 2 ---
> dictObj: <class 'dict'> {'first_name': 'John', 'age': 89} 
> 
> jsonStr: <class 'str'> '{"first_name": "John", "age": 89}' 
> 
>
