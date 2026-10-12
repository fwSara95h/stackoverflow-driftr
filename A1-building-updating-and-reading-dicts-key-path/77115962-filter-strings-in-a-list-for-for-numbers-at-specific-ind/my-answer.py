# Code from my Stack Overflow answer https://stackoverflow.com/a/77116197 (posted 2023-09-16), extracted verbatim; may need the question's context to run.

# --- block 1 ---
rest = ["town name", "state", "98420", "description"],["222", "street", "state", "98420", "description"], ["town name", "state", "94820", "description"]

addr = []
for i in rest:
    addr_i = i[:1] # don't check the first string
    for j in i[1:]:
        addr_i.append(j)
        if j.isnumeric(): break # stop if numeric
    addr.append(addr_i)

# --- block 2 ---
[['town name', 'state', '98420'], ['222', 'street', 'state', '98420'], ['town name', 'state', '94820']]

# --- block 3 ---
rest = ["town name", "state", "98420", "description"],["222", "street", "state", "98420", "description"], ["town name", "state", "94820", "description"]

addr, serv = [], []
for i in rest:
    addr_i = i[:1] # don't check the first string
    for n, j in enumerate(i[1:],1):
        addr_i.append(j)
        if j.isnumeric(): 
            serv.append(i[n+1:]) # rest of the strings
            break # stop if numeric
    else: serv.append([]) ## no numerics found
    addr.append(addr_i)

# --- block 4 ---
> addr = [['town name', 'state', '98420'], ['222', 'street', 'state', '98420'], ['town name', 'state', '94820']]
> serv = [['description'], ['description'], ['description']]
>
