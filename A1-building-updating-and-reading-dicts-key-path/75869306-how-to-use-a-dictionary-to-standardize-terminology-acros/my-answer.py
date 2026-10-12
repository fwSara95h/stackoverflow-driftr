# Code from my Stack Overflow answer https://stackoverflow.com/a/75871953 (posted 2023-03-28), extracted verbatim; may need the question's context to run.

# --- block 1 ---
> for i in super_list:
>     for key, value in voc_dict.items():
>          i.replace(voc_dict[key], voc_dict[value])
>

# --- block 2 ---
for si, sub_list in enumerate(super_list):
    for i, sl_item in enumerate(sub_list):
        for k, kw in Voc_dict.items():
            super_list[si][i] = sl_item.replace(k, kw)

# --- block 3 ---
Voc_dict = {'('+'|'.join([
    k for k,v in Voc_dict.items() if v==kw
])+')':kw for kw in set(Voc_dict.values())}
