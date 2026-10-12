# Code from my Stack Overflow answer https://stackoverflow.com/a/75104085 (posted 2023-01-13), extracted verbatim; may need the question's context to run.

# --- block 1 ---
>     if table_row.a.text is not None:
>         print(table_row.a.text) 
>

# --- block 2 ---
for i, table_row in enumerate(df_tr): 
    if not table_row.a: continue
    print(table_row.a.text)
