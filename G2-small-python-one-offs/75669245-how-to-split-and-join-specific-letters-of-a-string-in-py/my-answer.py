# Code from my Stack Overflow answer https://stackoverflow.com/a/75669353 (posted 2023-03-08), extracted verbatim; may need the question's context to run.

# --- block 1 ---
keep_substring = 'al'
keep_whitespace = False # set True to keep spaces, newline characters, etc
original_words = "installation altitude international"

opList = []
for ss in original_words.split('al'):
    if opList: opList.append(keep_substring)
    opList += [c for c in ss if c.strip() or keep_whitespace]
print(opList)

# --- block 2 ---
> ['i', 'n', 's', 't', 'al', 'l', 'a', 't', 'i', 'o', 'n', 'al', 't', 'i', 't', 'u', 'd', 'e', 'i', 'n', 't', 'e', 'r', 'n', 'a', 't', 'i', 'o', 'n', 'al']
>

# --- block 3 ---
> ['i', 'n', 's', 't', 'al', 'l', 'a', 't', 'i', 'o', 'n', ' ', 'al', 't', 'i', 't', 'u', 'd', 'e', ' ', 'i', 'n', 't', 'e', 'r', 'n', 'a', 't', 'i', 'o', 'n', 'al']
>
