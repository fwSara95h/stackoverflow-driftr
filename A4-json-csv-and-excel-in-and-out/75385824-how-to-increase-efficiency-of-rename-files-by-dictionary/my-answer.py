# Code from my Stack Overflow answer https://stackoverflow.com/a/75391748 (posted 2023-02-08), extracted verbatim; may need the question's context to run.

# --- block 1 ---
for (dir_path, dir_names, file_names) in walk(dir_path):
    for file_name in file_names:
        for keyWords in nameKeyWords:
            if keyWords in file_name:
                old_name = os.path.join(dir_path,file_name)
                new_name = os.path.join(dir_path,nameKeyWords.get(keyWords)+'.csv')
                os.rename(old_name, new_name)
                break ## [ no need to keep checking ]
        else: print(file_name) ## [ only prints if for never breaks ]

# --- block 2 ---
fNameGenerator = (
    (dPath, fName) for dPath, dnames, fNames
    in os.walk(dir_path) for fName in fNames
)

for dPath, file_name in fNameGenerator:
    for keyWords in nameKeyWords:
        if keyWords in file_name:
            new_name = os.path.join(dPath, f'{nameKeyWords.get(keyWords)}.csv')
            os.rename(os.path.join(dPath, file_name), new_name)
            break
    else: print(file_name)

# --- block 3 ---
# nameKeyWords = {....}
def getNewFn(oldFn:str):
    for k in nameKeyWords:
        if k in oldFn: return f"{nameKeyWords[k]}.csv"

fNameGenerator = (
    (dPath, fName, getNewFn(fName)) for dPath, dnames, fNames 
    in os.walk(dir_path) for fName in fNames
)

for dPath, file_name, new_name in fNameGenerator:
    if new_name is None: print(file_name)
    else: os.rename(*[os.path.join(dPath, fn) for fn in [file_name, new_name]])
