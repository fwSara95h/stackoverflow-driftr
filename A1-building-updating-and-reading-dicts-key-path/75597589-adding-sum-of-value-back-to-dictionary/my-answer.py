# Code from my Stack Overflow answer https://stackoverflow.com/a/75651237 (posted 2023-03-06), extracted verbatim; may need the question's context to run.

# --- block 1 ---
> for value in artist_dict.values():
>   value += 100
>

# --- block 2 ---
for k in artist_dict:
    artist_dict[k] += 100
