# Code from my Stack Overflow answer https://stackoverflow.com/a/74978234 (posted 2023-01-02), extracted verbatim; may need the question's context to run.

# --- block 1 ---
# import sys
new_recursion_limit = 2000 # set as you prefer
sys.setrecursionlimit(new_recursion_limit)
# print('recursion limit is now', sys.getrecursionlimit())

# --- block 2 ---
def GetPdcResults(parts, start=0, maxDepth=999, curDepth=0):

# --- block 3 ---
# if response.status_code == 401:
    # logger.log_error('[-] Cookie Error', part=part)
    # print('\n[-] Cookie Error')
    if curDepth < maxDepth: 
        GetPdcResults(parts, start=i, maxDepth=maxDepth, curDepth=curDepth+1)
    ## else: print(curDepth, 'is too deep') # if you want an alternate action...
    # break
