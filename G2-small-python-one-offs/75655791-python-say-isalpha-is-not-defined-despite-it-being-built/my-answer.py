# Code from my Stack Overflow answer https://stackoverflow.com/a/75655893 (posted 2023-03-06), extracted verbatim; may need the question's context to run.

# --- block 1 ---
if str(things).isalpha(): continue

# --- block 2 ---
if isinstance(things, str) and things.isalpha(): 
    continue

# --- block 3 ---
yes = []
item=[1,7,-10,34,2,"a",-8]
for things in item:
    if isinstance(things, str) and things.isalpha(): 
        continue
    yes.append(things)
    print(yes)

# --- block 4 ---
item=[1,7,-10,34,2,"a",-8]
yes = [i for i in item if not (isinstance(i, str) and i.isalpha())] 
print(*yes, sep='\n')
