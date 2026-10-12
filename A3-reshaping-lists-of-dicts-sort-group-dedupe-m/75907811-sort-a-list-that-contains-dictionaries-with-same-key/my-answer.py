# Code from my Stack Overflow answer https://stackoverflow.com/a/75911088 (posted 2023-04-02), extracted verbatim; may need the question's context to run.

# --- block 1 ---
sortedList = sorted(dictList, key=lambda d: [d.get(k) for k in keysList])

# --- block 2 ---
dictList.sort(key=lambda d: [d.get(k) for k in keysList])
