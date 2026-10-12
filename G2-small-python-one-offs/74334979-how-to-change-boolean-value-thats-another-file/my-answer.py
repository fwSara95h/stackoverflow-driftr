# Code from my Stack Overflow answer https://stackoverflow.com/a/74335222 (posted 2022-11-06), extracted verbatim; may need the question's context to run.

# --- block 1 ---
with open('boolean.py', 'w') as f: 
    f.write('storepass = False')

# --- block 2 ---
# import json
boolean = json.load(open('boolean.json', 'r'))

# --- block 3 ---
# import json
boolean.storepass = True
with open('boolean.json', 'w') as f:
    json.dump(boolean, f, indent=4)
    ## NOT f.write(boolean)
