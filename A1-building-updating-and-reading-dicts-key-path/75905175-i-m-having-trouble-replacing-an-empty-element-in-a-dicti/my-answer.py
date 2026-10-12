# Code from my Stack Overflow answer https://stackoverflow.com/a/75912007 (posted 2023-04-02), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# keys_A = [*A] ## if you already have A from a previous block
keys_A = ['name', 'age', 'tasks done', 'number of tasks done']

# print("hello 'Worker'")
# time.sleep(2)

A = {k:input(f'enter {k}') for k in keys_A}

# --- block 2 ---
# ref_A = {k:type(v) for k,v in A.items()} ## if you already have A from a previous block
ref_A = {'name': str, 'age': int, 'tasks done': str, 'number of tasks done': int}

# print("hello 'Worker'")
# time.sleep(2)

A = {} ## [ not necessary if you already have A ]
for k, t in ref_A.items():
    while not isinstance((inp:=input(f'enter {k}: ')), t):
        try: inp = t(inp)
        except ValueError as ve: print('! Invalid Input -', ve, '!')
        else: break
    A[k] = inp

# --- block 3 ---
def validated_input(promptStr:str, inp_type:type=str):
    while not isinstance((inp:=input(promptStr)), inp_type):
        try: return inp_type(inp)
        except ValueError as ve: print('! Invalid Input -', ve, '!')
    return inp

# --- block 4 ---
A = {k: validated_input(f'enter {k}: ', t) for k, t in ref_A.items()}

## if you already have A and you just want to update the keys in ref_A:
# for k, t in ref_A.items(): A[k] = validated_input(f'enter {k}: ', t) ## OR
# A = {**A, **{k: validated_input(f'enter {k}: ', t) for k, t in ref_A.items()}}

# --- block 5 ---
def list_input(itemName:str):
    inps = [] 
    promptStr = f'Enter a {itemName} to add [Or just press ENTER to stop]: ' 
    while (inp:=input(promptStr)).strip(): inps.append(inp)
    return inps

# --- block 6 ---
def validated_input(promptStr:str, inp_type:type=str):
    if inp_type in [list, tuple, set]:
        return inp_type(list_input(promptStr))
    while not isinstance((inp:=input(promptStr)), inp_type):
        try: return inp_type(inp)
        except ValueError as ve: print('! Invalid Input -', ve, '!')
    return inp

# --- block 7 ---
A =  {'name': input('enter name: ')} ## A['name']=input('enter name: ') # if A exists
A['age'] = validated_input('enter age: ', int)
A['tasks done'] = list_input('"task done"') # validated_input('"task done"', list)
A['number of tasks done'] = len(A['tasks done'])
