# Code from my Stack Overflow answer https://stackoverflow.com/a/74190308 (posted 2022-10-25), extracted verbatim; may need the question's context to run.

# --- block 1 ---
def truncateIfLong(str, maxLen=15):
    if type(maxLen) != int: maxLen = 15 # [just in case]
    if maxLen < 4: maxLen = 5
    return str if len(str) < maxLen else str[:maxLen-3]+'...'

# --- block 2 ---
print(soup.prettify(formatter=truncateIfLong))

# --- block 3 ---
with open('x.html', 'w', encoding="utf8") as f:
    f.write(str(soup))
