# Code from my Stack Overflow answer https://stackoverflow.com/a/75807943 (posted 2023-03-22), extracted verbatim; may need the question's context to run.

# --- block 1 ---
> df = pd.json_normalize(data, 'healthRuleMembers') 
>

# --- block 2 ---
> df[['model.id', 'model.name', 'model.scheduleName', ... ]].to_excel('test_file.xlsx', index=False)
>
