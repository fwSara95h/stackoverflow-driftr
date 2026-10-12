# Code from my Stack Overflow answer https://stackoverflow.com/a/74961683 (posted 2022-12-30), extracted verbatim; may need the question's context to run.

# --- block 1 ---
> Exception has occurred: KeyError
> 'class'
>

# --- block 2 ---
if col.div:
    if not col.div.get('class'): continue
    print(f"{col.div['class']}")

# --- block 3 ---
# for col in row.select('td:not(:has(div.stars)):not(:has(img))'):
for col in row.select('td:not(:has(div.stars))'):
