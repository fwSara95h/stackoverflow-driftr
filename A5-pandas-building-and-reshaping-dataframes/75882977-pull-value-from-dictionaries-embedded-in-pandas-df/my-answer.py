# Code from my Stack Overflow answer https://stackoverflow.com/a/75894702 (posted 2023-03-31), extracted verbatim; may need the question's context to run.

# --- block 1 ---
df = pd.DataFrame([
    [ 'XYZ', {'all': 27026}, {'all': 2042} ], 
    [ 'QWE', {'$overall': {'all': 6}, 'Mar 18, 2021': {'all': 3}, 'Mar 3, 2021': {'all': 3}}, {'$overall': {'all': 3}, 'Mar 3, 2021': {'all': 2}, 'Mar 18, 2021': {'all': 1}}]
], index=['$XYZ', 'QWE'], columns=['Name', 'A', 'B'])

# --- block 2 ---
nested_index = 'Date'
expand_rows = ['QWE'] # include indices of rows with dates
expand_cols = ['A','B'] # include names of columns with dates

static_cols = [c for c in df.columns if c not in expand_cols]
exp_dfs = []
for ind in expand_rows:
    df_ind = pd.DataFrame(df.loc[ind][expand_cols].to_dict())
    df_ind = df_ind.drop('$overall',axis='rows')
    df_ind = df_ind.rename_axis(nested_index).reset_index()
    for c in static_cols: df_ind[c] = df.loc[ind][c]
    exp_dfs.append(df_ind.set_index(pd.Series([ind]*len(df_ind))))

exp_df = pd.concat([df.drop(expand_rows, axis='rows')]+exp_dfs)
exp_df = exp_df.applymap(lambda x: getattr(x,'get',{'all':x}.get)('all', x))
