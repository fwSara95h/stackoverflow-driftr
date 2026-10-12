# Code from my Stack Overflow answer https://stackoverflow.com/a/75583260 (posted 2023-02-27), extracted verbatim; may need the question's context to run.

# --- block 1 ---
with open('TEST.txt') as f: 
    inputList = f.read().splitlines()

# for inp in inputList: print(process(inp)) ## OR
outputList = [process(inp) for inp in inputList] 
for op in outputList: print(op)

# --- block 2 ---
import pandas as pd
# pd.DataFrame(outputList, index=inputList).to_csv('TEST.csv') ## same as:
# pd.DataFrame([process(i) for i in inputList], index=inputList).to_csv('TEST.csv')

pd.DataFrame(
    [{'input': inp, **process(inp)} for inp in inputList]
).set_index('input').to_csv('TEST.csv')

# --- block 3 ---
import json

with open('TEST.json', 'w') as f: 
    # json.dump([{'input':inp, 'output': process(inp)} for inp in inputList], f) ## op1
    json.dump({inp: process(inp) for inp in inputList}, f) #, indent=4) ## op2

# --- block 4 ---
inpFiles = ['text1.txt', 'text2.txt', 'text3.txt']
# ifLen = len(ifLen)
for inpf in inpFiles: # for ifi, inpf in enumerate(inpFiles, 1):
    # print('', end=f'\r[{ifi} of {ifLen}] processing "{inpf}"...')
    with open(inpf) as f: inputList = f.read().splitlines()
    with open(f'{inpf[:-4]}.json', 'w') as f:   
        json.dump({inp: process(inp) for inp in inputList}, f, indent=4)
